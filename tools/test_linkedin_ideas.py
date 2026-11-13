#!/usr/bin/env python3
"""Tests for tools/linkedin_ideas.py and .github/workflows/linkedin-ideas.yml. No network.

    python tools/test_linkedin_ideas.py
"""

from __future__ import annotations

import datetime as dt
import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import linkedin_ideas as li  # noqa: E402
import linkedin_post as lp  # noqa: E402

AMS = ZoneInfo("Europe/Amsterdam")
TRUSTED = {"github-actions", "daluSt".lower()}

BANK = """# Posts

## 2. Latest

```text
Not an idea post.
```

## 3. Idea posts: a title

Preamble with ### Post 99. nothing

### Post 1. First

*Kind: Fact. Atlas entities: A.*

```text
First text
```

*Check before posting: a date moves.*

### Post 2. Second

```text
Second text
```

### Post 3. Third

```text
Third text
```

### Post 4. Fourth

```text
Fourth text
```

*Hold: pulled by the owner.*

## Before posting

```text
Not a post either.
```
"""


def comment(body, author="github-actions"):
    return {"author": {"login": author}, "body": body}


def at(y, m, d, hh=12, mm=0):
    return dt.datetime(y, m, d, hh, mm, tzinfo=AMS)


def tuesday():
    return dt.date(2026, 11, 17)  # a Tuesday


class TestParseBank(unittest.TestCase):
    def test_reads_only_section_3_in_order(self):
        ideas = li.parse_bank(BANK)
        self.assertEqual([i.number for i in ideas], [1, 2, 3, 4])
        self.assertEqual(ideas[1].text, "Second text\n")
        self.assertEqual(ideas[0].title, "First")

    def test_a_check_or_hold_line_holds_the_post(self):
        held = {i.number: i.hold for i in li.parse_bank(BANK)}
        self.assertEqual(held, {1: True, 2: False, 3: False, 4: True})

    def test_a_missing_section_is_an_error(self):
        with self.assertRaises(li.IdeaError):
            li.parse_bank("# nothing\n")

    def test_a_post_without_a_text_block_is_an_error(self):
        with self.assertRaisesRegex(li.IdeaError, "post 1 has no"):
            li.parse_bank("## 3. Idea posts\n\n### Post 1. X\n\nno block\n")

    def test_duplicate_numbers_are_an_error(self):
        md = "## 3. Idea posts\n\n### Post 1. X\n\n```text\na\n```\n\n### Post 1. Y\n\n```text\nb\n```\n"
        with self.assertRaisesRegex(li.IdeaError, "same number"):
            li.parse_bank(md)


class TestTheRealBank(unittest.TestCase):
    """The workflow reads docs/linkedin-page-posts.md: editing it must not break it."""

    @classmethod
    def setUpClass(cls):
        cls.ideas = li.load_bank()

    def test_there_are_posts_and_enough_in_the_rotation(self):
        self.assertGreaterEqual(len(self.ideas), 45)
        self.assertGreaterEqual(sum(not i.hold for i in self.ideas), 10)

    def test_numbers_run_from_1_without_gaps(self):
        self.assertEqual([i.number for i in self.ideas], list(range(1, len(self.ideas) + 1)))

    def test_every_post_fits_linkedin_and_is_plain_text(self):
        for i in self.ideas:
            self.assertLessEqual(len(i.text), lp.LIMIT, i.number)
            self.assertNotIn("```", i.text, i.number)
            self.assertNotIn("**", i.text, i.number)

    def test_every_post_has_a_title_and_a_question_or_closing_line(self):
        for i in self.ideas:
            self.assertTrue(i.title.strip(), i.number)
            self.assertGreater(len(i.text.strip().splitlines()), 4, i.number)

    def test_the_text_survives_the_poster_escaping_check(self):
        for i in self.ideas:
            lp.escape_commentary(i.text)  # must not raise


class TestTargetTime(unittest.TestCase):
    def test_always_between_08_and_22(self):
        day = dt.date(2026, 1, 1)
        for n in range(1500):
            m = li.target_minute(day + dt.timedelta(days=n))
            self.assertGreaterEqual(m, 8 * 60)
            self.assertLess(m, 22 * 60)

    def test_the_same_day_gives_the_same_time(self):
        self.assertEqual(li.target_minute(tuesday()), li.target_minute(tuesday()))

    def test_it_is_spread_over_the_day_and_not_a_constant(self):
        times = {li.target_minute(dt.date(2026, 1, 1) + dt.timedelta(days=n)) for n in range(400)}
        self.assertGreater(len(times), 200)
        hours = {t // 60 for t in times}
        self.assertEqual(hours, set(range(8, 22)))

    def test_a_different_salt_gives_a_different_draw(self):
        days = [dt.date(2026, 1, 1) + dt.timedelta(days=n) for n in range(30)]
        self.assertNotEqual([li.target_minute(d) for d in days], [li.target_minute(d, "x") for d in days])

    def test_hhmm(self):
        self.assertEqual(li.hhmm(8 * 60 + 5), "08:05")


class TestLedger(unittest.TestCase):
    def test_reads_posted_and_failed_lines_from_trusted_authors(self):
        posted, days = li.ledger([
            comment("Posted idea post 2 on 2026-11-17: https://x/"),
            comment("Failed idea post 3 on 2026-11-19: why"),
        ], TRUSTED)
        self.assertEqual(posted, {2})
        self.assertEqual(days, {dt.date(2026, 11, 17), dt.date(2026, 11, 19)})

    def test_a_stranger_cannot_skip_a_post_or_block_a_day(self):
        posted, days = li.ledger([comment("Posted idea post 2 on 2026-11-17: x", author="stranger")], TRUSTED)
        self.assertEqual((posted, days), (set(), set()))

    def test_the_owner_can_mark_a_post_done_by_hand(self):
        posted, _ = li.ledger([comment("Posted idea post 5 on 2026-11-17: by hand", author="DaLuSt")], TRUSTED)
        self.assertEqual(posted, {5})

    def test_other_comments_and_missing_fields_are_ignored(self):
        posted, days = li.ledger([{"body": None}, {"author": None, "body": "hi"}, comment("hello")], TRUSTED)
        self.assertEqual((posted, days), (set(), set()))


class TestDecide(unittest.TestCase):
    IDEAS = li.parse_bank(BANK)

    def decide(self, now, comments=(), **kw):
        return li.decide(self.IDEAS, list(comments), now, trusted=TRUSTED, **kw)

    def after_target(self, day, extra_minutes=1):
        m = li.target_minute(day) + extra_minutes
        return dt.datetime(day.year, day.month, day.day, m // 60, m % 60, tzinfo=AMS)

    def test_due_on_a_tuesday_once_the_drawn_time_has_passed(self):
        d = self.decide(self.after_target(tuesday()))
        self.assertTrue(d.due)
        self.assertEqual(d.number, 2)  # post 1 is held

    def test_not_due_before_the_drawn_time(self):
        m = li.target_minute(tuesday()) - 1
        d = self.decide(dt.datetime(2026, 11, 17, m // 60, m % 60, tzinfo=AMS))
        self.assertFalse(d.due)
        self.assertIn("too early", d.reason)

    def test_due_on_a_thursday_and_not_on_other_days(self):
        thursday = dt.date(2026, 11, 19)
        self.assertTrue(self.decide(self.after_target(thursday)).due)
        for offset in (-1, 1, 3, 4, 5, 6):  # Mon, Wed, Fri, Sat, Sun
            day = tuesday() + dt.timedelta(days=offset)
            d = self.decide(at(day.year, day.month, day.day, 21, 59))
            self.assertFalse(d.due, day.strftime("%a"))
            self.assertIn("Tuesday or Thursday", d.reason)

    def test_only_one_attempt_a_day(self):
        now = self.after_target(tuesday(), 30)
        for body in ("Posted idea post 2 on 2026-11-17: x", "Failed idea post 2 on 2026-11-17: x"):
            self.assertFalse(self.decide(now, [comment(body)]).due, body)

    def test_the_next_post_skips_posted_and_held_ones(self):
        now = self.after_target(dt.date(2026, 11, 19))
        d = self.decide(now, [comment("Posted idea post 2 on 2026-11-17: x")])
        self.assertEqual(d.number, 3)  # 1 and 4 are held, 2 is posted

    def test_a_failed_post_is_tried_again_next_time(self):
        now = self.after_target(dt.date(2026, 11, 19))
        d = self.decide(now, [comment("Failed idea post 2 on 2026-11-17: token")])
        self.assertEqual(d.number, 2)

    def test_the_window_closes_at_22(self):
        # Find a day whose drawn time is before 22:00 (all are) and run just after the window.
        d = self.decide(at(2026, 11, 17, 22, 5))
        self.assertFalse(d.due)
        self.assertIn("missed", d.reason)

    def test_an_empty_queue_is_reported_and_posts_nothing(self):
        done = [comment("Posted idea post 2 on 2026-11-10: x"), comment("Posted idea post 3 on 2026-11-12: x")]
        d = self.decide(self.after_target(tuesday()), done)
        self.assertFalse(d.due)
        self.assertIn("queue is empty", d.reason)

    def test_force_ignores_day_time_and_todays_attempt_but_not_the_queue(self):
        self.assertTrue(self.decide(at(2026, 11, 15, 3, 0), force=True).due)  # a Sunday at 03:00
        self.assertTrue(self.decide(at(2026, 11, 17, 9, 0), [comment("Failed idea post 2 on 2026-11-17: x")], force=True).due)
        done = [comment("Posted idea post 2 on 2026-11-10: x"), comment("Posted idea post 3 on 2026-11-12: x")]
        self.assertFalse(self.decide(at(2026, 11, 17, 9, 0), done, force=True).due)

    def test_the_decision_names_the_day_and_the_time(self):
        d = self.decide(self.after_target(tuesday()))
        self.assertEqual(d.date, "2026-11-17")
        self.assertRegex(d.target, r"^\d\d:\d\d$")

    def test_a_week_has_exactly_two_posting_days_and_one_post_each(self):
        # Walk a whole week in 15-minute steps: exactly two posts, one on Tuesday, one on Thursday,
        # each after its drawn time, with the ledger growing as the workflow would write it.
        comments, posts = [], []
        start = dt.datetime(2026, 11, 16, 0, 0, tzinfo=AMS)
        for step in range(7 * 24 * 4):
            now = start + dt.timedelta(minutes=15 * step)
            d = self.decide(now, comments)
            if d.due:
                posts.append((now, d.number))
                comments.append(comment(li.record_line("posted", d.number, d.date, "https://x/")))
        self.assertEqual(len(posts), 2)
        self.assertEqual([p[0].strftime("%a") for p in posts], ["Tue", "Thu"])
        for now, _ in posts:
            minute = now.hour * 60 + now.minute
            self.assertGreaterEqual(minute, li.target_minute(now.date()))
            self.assertLess(minute - li.target_minute(now.date()), 15)
        self.assertEqual([p[1] for p in posts], [2, 3])

    def test_the_summer_and_winter_clocks_both_fall_inside_the_cron_hours(self):
        # The cron fires 05:00-21:59 UTC. Every local minute from 08:00 to 21:59 must be covered
        # in winter (UTC+1) and in summer (UTC+2) time.
        for month in (1, 7):
            for local in (8 * 60, 21 * 60 + 59):
                when = dt.datetime(2026, month, 15, local // 60, local % 60, tzinfo=AMS)
                utc = when.astimezone(dt.timezone.utc)
                self.assertTrue(5 <= utc.hour <= 21, (month, local, utc))


class TestRecordLine(unittest.TestCase):
    def test_the_line_is_what_the_ledger_reads(self):
        line = li.record_line("posted", 12, "2026-11-17", "https://x/")
        self.assertEqual(line, "Posted idea post 12 on 2026-11-17: https://x/")
        self.assertEqual(li.ledger([comment(line)], TRUSTED), ({12}, {dt.date(2026, 11, 17)}))
        self.assertEqual(li.ledger([comment(li.record_line("failed", 3, "2026-11-19", "why\nnow"))], TRUSTED),
                         (set(), {dt.date(2026, 11, 19)}))

    def test_a_bad_kind_or_date_is_refused(self):
        with self.assertRaises(li.IdeaError):
            li.record_line("done", 1, "2026-11-17", "x")
        with self.assertRaises(ValueError):
            li.record_line("posted", 1, "17-11-2026", "x")

    def test_long_text_is_cut(self):
        self.assertLessEqual(len(li.record_line("failed", 1, "2026-11-17", "x" * 1000)), 400)


class TestMain(unittest.TestCase):
    def run_main(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = li.main(argv)
        return code, out.getvalue(), err.getvalue()

    def bank_file(self):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        f.write(BANK)
        f.close()
        return f.name

    def comments_file(self, comments):
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        json.dump({"comments": comments}, f)
        f.close()
        return f.name

    def test_decide_prints_key_value_lines_for_the_output_file(self):
        m = li.target_minute(tuesday()) + 5
        now = f"2026-11-17T{m // 60:02d}:{m % 60:02d}:00"
        code, out, _ = self.run_main(["--bank", self.bank_file(), "decide", "--comments-file",
                                      self.comments_file([]), "--now", now])
        self.assertEqual(code, 0)
        lines = dict(l.split("=", 1) for l in out.strip().splitlines())
        self.assertEqual(set(lines), {"due", "number", "date", "target", "reason"})
        self.assertEqual((lines["due"], lines["number"], lines["date"]), ("true", "2", "2026-11-17"))

    def test_decide_when_not_due_prints_an_empty_number(self):
        code, out, _ = self.run_main(["--bank", self.bank_file(), "decide", "--comments-file",
                                      self.comments_file([]), "--now", "2026-11-15T12:00:00"])
        self.assertEqual(code, 0)
        self.assertIn("due=false\nnumber=\n", out)

    def test_decide_reads_a_bare_list_of_comments_too(self):
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump([], f)
        f.close()
        code, _, _ = self.run_main(["--bank", self.bank_file(), "decide", "--comments-file", f.name,
                                    "--now", "2026-11-15T12:00:00"])
        self.assertEqual(code, 0)

    def test_text_prints_the_post_and_an_unknown_number_fails(self):
        self.assertEqual(self.run_main(["--bank", self.bank_file(), "text", "3"])[:2], (0, "Third text\n"))
        code, _, err = self.run_main(["--bank", self.bank_file(), "text", "9"])
        self.assertEqual(code, 2)
        self.assertIn("no post 9", err)

    def test_queue_lists_the_posts_with_their_state(self):
        code, out, _ = self.run_main(["--bank", self.bank_file(), "queue"])
        self.assertEqual(code, 0)
        self.assertRegex(out, r"HELD\s+1")
        self.assertRegex(out, r"next\s+2")
        self.assertRegex(out, r"queued\s+3")
        self.assertIn("2 of 4 posts are in the rotation", out)

    def test_record_prints_the_line(self):
        code, out, _ = self.run_main(["record", "posted", "--number", "7", "--date", "2026-11-17", "--text", "L"])
        self.assertEqual((code, out), (0, "Posted idea post 7 on 2026-11-17: L\n"))

    def test_a_bad_bank_exits_2(self):
        f = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
        f.write("# nothing")
        f.close()
        self.assertEqual(self.run_main(["--bank", f.name, "queue"])[0], 2)


class TestWorkflow(unittest.TestCase):
    TEXT = (REPO_ROOT / ".github" / "workflows" / "linkedin-ideas.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.on = cls.wf.get("on", cls.wf.get(True))
        cls.decide, cls.post = cls.wf["jobs"]["decide"], cls.wf["jobs"]["post"]

    def step(self, job, name):
        return next(s for s in job["steps"] if s.get("name") == name)

    def test_it_runs_every_15_minutes_on_tuesday_and_thursday_only(self):
        (sched,) = self.on["schedule"]
        minute, hour, dom, month, dow = sched["cron"].split()
        self.assertEqual((minute, dom, month, dow), ("*/15", "*", "*", "2,4"))
        self.assertEqual(hour, "5-21")

    def test_the_cron_hours_cover_08_to_22_in_amsterdam(self):
        lo, hi = (int(x) for x in self.on["schedule"][0]["cron"].split()[1].split("-"))
        self.assertLessEqual(lo, 8 - 2)   # 08:00 in summer time is 06:00 UTC
        self.assertGreaterEqual(hi, 21)   # 21:59 in winter time is 20:59 UTC, summer 19:59

    def test_it_cannot_be_started_by_a_pull_request_or_a_push(self):
        self.assertEqual(set(self.on), {"schedule", "workflow_dispatch"})

    def test_a_manual_run_is_a_dry_run_by_default(self):
        self.assertIs(self.on["workflow_dispatch"]["inputs"]["dry_run"]["default"], True)

    def test_it_is_off_until_the_variable_is_set(self):
        self.assertIn("vars.LINKEDIN_IDEAS_ENABLED == 'true'", self.decide["if"])
        self.assertIn("workflow_dispatch", self.decide["if"])

    def test_the_wake_ups_never_see_the_secrets(self):
        self.assertNotIn("environment", self.decide)
        self.assertNotIn("secrets.", json.dumps(self.decide))

    def test_only_the_posting_job_has_the_environment_and_the_secrets(self):
        self.assertEqual(self.post["environment"], "linkedin-ideas")
        self.assertEqual(self.post["needs"], "decide")
        self.assertIn("needs.decide.outputs.due == 'true'", self.post["if"])
        self.assertEqual(self.TEXT.count("secrets.LINKEDIN_ACCESS_TOKEN"), 1)
        self.assertEqual(self.TEXT.count("secrets.LINKEDIN_AUTHOR_URN"), 1)
        for s in self.post["steps"]:
            self.assertNotIn("secrets.", json.dumps(s.get("run", "")), s.get("name"))
        self.assertIn("secrets.LINKEDIN_ACCESS_TOKEN", json.dumps(self.step(self.post, "Post to LinkedIn")["env"]))

    def test_it_never_uses_the_pages_or_the_release_environments(self):
        self.assertNotIn("LINKEDIN_PAGE", self.TEXT)
        self.assertNotIn("environment: linkedin\n", self.TEXT)

    def test_least_privilege(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read", "issues": "write"})

    def test_one_run_at_a_time(self):
        self.assertEqual(self.wf["concurrency"]["group"], "linkedin-ideas")
        self.assertIs(self.wf["concurrency"]["cancel-in-progress"], False)

    def test_a_scheduled_run_posts_for_real_and_a_manual_one_forces_the_next_post(self):
        run = self.step(self.decide, "Is a post due?")["run"]
        self.assertIn('[ "$EVENT" = "workflow_dispatch" ]', run)
        self.assertIn("--force", run)
        post = self.step(self.post, "Post to LinkedIn")
        self.assertIn("inputs.dry_run", post["env"]["DRY_RUN"])
        self.assertIn("--dry-run", post["run"])

    def test_only_trusted_authors_count_in_the_log(self):
        run = self.step(self.decide, "Is a post due?")["run"]
        self.assertIn("--trusted", run)
        self.assertIn("github-actions", run)

    def test_a_dry_run_writes_nothing_to_the_log_and_a_failed_dry_run_uses_no_day(self):
        self.assertIn("steps.post.outputs.link != ''", self.step(self.post, "Log the post")["if"])
        fail = self.step(self.post, "Log the failure")["if"]
        self.assertIn("failure()", fail)
        self.assertIn("inputs.dry_run != true", fail)

    def test_the_log_issue_is_created_once_and_never_closed(self):
        self.assertIn("gh issue create", self.TEXT)
        self.assertNotIn("gh issue close", self.TEXT)
        self.assertIn("--state all --label linkedin-ideas", self.TEXT)

    def test_the_tool_it_calls_exists_and_posts_with_the_profile_poster(self):
        self.assertTrue((REPO_ROOT / "tools" / "linkedin_ideas.py").exists())
        self.assertIn("python tools/linkedin_post.py post --text-file post.txt", self.TEXT)
        self.assertNotIn("--page", self.TEXT)

    def test_actions_are_on_current_node_versions(self):
        for job in (self.decide, self.post):
            for s in job["steps"]:
                uses = s.get("uses", "")
                if uses.startswith(("actions/checkout", "actions/setup-python")):
                    self.assertRegex(uses, r"@v[7-9]")

    def test_the_workflow_text_matches_the_marker_the_tool_documents(self):
        doc = li.__doc__
        self.assertIn("*Check before posting", doc)
        self.assertIn("*Hold", doc)
        self.assertTrue(re.search(r"Posted idea post", self.TEXT))


if __name__ == "__main__":
    unittest.main(verbosity=1)
