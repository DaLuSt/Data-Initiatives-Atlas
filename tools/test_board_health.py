#!/usr/bin/env python3
"""Tests for tools/board_health.py and the token-watching parts of project-board.yml.

    python tools/test_board_health.py
"""

from __future__ import annotations

import datetime as dt
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import board_health as bh  # noqa: E402

TODAY = dt.date(2026, 10, 12)


def levels(msgs):
    return [lvl for lvl, _ in msgs]


class TestCheck(unittest.TestCase):
    def check(self, present=True, expires="", enabled=False):
        return bh.check(present, expires, enabled, TODAY)

    def test_no_secret_before_the_board_is_set_up_is_a_quiet_notice(self):
        msgs, failed, warn = self.check(present=False, enabled=False)
        self.assertEqual((levels(msgs), failed, warn), (["notice"], False, False))

    def test_no_secret_once_the_board_is_set_up_is_a_failure(self):
        msgs, failed, warn = self.check(present=False, enabled=True)
        self.assertEqual((levels(msgs), failed), (["error"], True))
        self.assertIn("BOARD_SYNC_ENABLED", msgs[0][1])
        self.assertIn("docs/credentials.md", msgs[0][1])

    def test_no_recorded_expiry_is_a_notice_and_does_not_block(self):
        msgs, failed, warn = self.check(expires="")
        self.assertEqual((levels(msgs), failed, warn), (["notice"], False, False))
        self.assertIn("PROJECT_TOKEN_EXPIRES", msgs[0][1])

    def test_far_from_expiry_is_silent(self):
        self.assertEqual(self.check(expires="2027-01-05"), ([], False, False))

    def test_the_warning_starts_fourteen_days_before(self):
        self.assertEqual(self.check(expires="2026-10-27")[0], [])            # 15 days
        msgs, failed, warn = self.check(expires="2026-10-26")                # 14 days
        self.assertEqual((levels(msgs), failed, warn), (["warning"], False, True))
        self.assertIn("14 day", msgs[0][1])

    def test_the_last_day_still_works_and_warns(self):
        msgs, failed, warn = self.check(expires="2026-10-12")
        self.assertEqual((levels(msgs), failed, warn), (["warning"], False, True))
        self.assertIn("0 day", msgs[0][1])

    def test_after_the_date_it_fails_and_says_how_long_ago(self):
        msgs, failed, warn = self.check(expires="2026-10-10")
        self.assertEqual((levels(msgs), failed, warn), (["error"], True, False))
        self.assertIn("2 day(s) ago", msgs[0][1])
        self.assertIn("Rotate", msgs[0][1])

    def test_a_malformed_date_fails(self):
        for bad in ("soon", "2026-13-40", "12/10/2026"):
            with self.subTest(bad=bad):
                msgs, failed, _ = self.check(expires=bad)
                self.assertEqual((levels(msgs), failed), (["error"], True))

    def test_whitespace_around_the_date_is_ignored(self):
        self.assertEqual(self.check(expires="  2027-01-05\n")[0], [])

    def test_a_secret_that_is_missing_wins_over_the_date(self):
        msgs, failed, _ = self.check(present=False, expires="2020-01-01", enabled=True)
        self.assertEqual(len(msgs), 1)
        self.assertIn("not set", msgs[0][1])

    def test_truthy(self):
        for v in ("true", "TRUE", " True "):
            self.assertTrue(bh.truthy(v))
        for v in ("", "false", "1", "yes", None):
            self.assertFalse(bh.truthy(v))


class TestMain(unittest.TestCase):
    def run_main(self, argv, env_out=True):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "out"
            f.write_text("")
            env = {"GITHUB_OUTPUT": str(f)} if env_out else {}
            out = io.StringIO()
            with mock.patch.dict("os.environ", env, clear=False), \
                    mock.patch.object(bh.dt, "date", wraps=dt.date) as fake, redirect_stdout(out):
                fake.today.return_value = TODAY
                code = bh.main(argv)
            return code, out.getvalue(), f.read_text()

    def test_annotations_and_outputs_for_a_warning(self):
        code, out, outputs = self.run_main(["--secret-present", "true", "--expires", "2026-10-20", "--enabled", "true"])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("::warning::"))
        self.assertIn("warn=true", outputs)
        self.assertIn("failed=false", outputs)
        self.assertIn("message=The PROJECT_TOKEN expires on 2026-10-20", outputs)

    def test_exit_status_one_and_outputs_for_a_failure(self):
        code, out, outputs = self.run_main(["--secret-present", "true", "--expires", "2026-10-01", "--enabled", "true"])
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("::error::"))
        self.assertIn("failed=true", outputs)
        self.assertIn("warn=false", outputs)

    def test_a_healthy_run_is_silent_and_exits_0(self):
        code, out, outputs = self.run_main(["--secret-present", "true", "--expires", "2027-06-01", "--enabled", "true"])
        self.assertEqual((code, out), (0, ""))
        self.assertIn("warn=false", outputs)
        self.assertNotIn("message=", outputs)

    def test_empty_variables_are_accepted(self):
        code, out, _ = self.run_main(["--secret-present", "false", "--expires", "", "--enabled", ""])
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("::notice::"))

    def test_it_works_without_a_github_output_file(self):
        code, out, _ = self.run_main(["--secret-present", "true", "--expires", "2027-06-01"], env_out=False)
        self.assertEqual(code, 0)


class TestWorkflow(unittest.TestCase):
    TEXT = (REPO_ROOT / ".github" / "workflows" / "project-board.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.steps = {s.get("name", s.get("uses")): s for s in cls.wf["jobs"]["sync"]["steps"]}

    def test_the_health_check_runs_before_the_sync(self):
        names = list(self.steps)
        self.assertLess(names.index("Check the token's health"), names.index("Sync the board"))
        self.assertLess(names.index("Check the secret"), names.index("Check the token's health"))

    def test_the_health_check_reads_the_two_variables_through_env(self):
        step = self.steps["Check the token's health"]
        self.assertEqual(step["env"]["EXPIRES"], "${{ vars.PROJECT_TOKEN_EXPIRES }}")
        self.assertEqual(step["env"]["ENABLED"], "${{ vars.BOARD_SYNC_ENABLED }}")
        self.assertNotIn("${{", step["run"])

    def test_the_health_check_is_not_skipped_and_can_stop_the_sync(self):
        self.assertNotIn("if", self.steps["Check the token's health"])
        self.assertNotIn("always()", self.steps["Sync the board"].get("if", ""))

    def test_a_secret_is_only_ever_passed_through_env(self):
        for step in self.steps.values():
            self.assertNotIn("secrets.", step.get("run", ""))
        self.assertEqual(self.TEXT.count("secrets.PROJECT_TOKEN"), 2 + self.TEXT.count("# secrets.PROJECT_TOKEN"))

    def test_the_issue_is_opened_on_failure_or_warning_and_only_once(self):
        step = self.steps['Open the "needs attention" issue']
        self.assertIn("failure()", step["if"])
        self.assertIn("steps.health.outputs.warn == 'true'", step["if"])
        self.assertIn("already open", step["run"])
        self.assertNotIn("gh issue comment", step["run"])

    def test_the_issue_is_closed_only_by_a_healthy_real_run(self):
        step = self.steps["Close the issue once the sync works again"]
        cond = step["if"]
        for part in ("success()", "steps.secret.outputs.present == 'true'", "steps.health.outputs.warn != 'true'",
                     "inputs.dry_run != true"):
            self.assertIn(part, cond)
        self.assertIn("gh issue close", step["run"])

    def test_the_message_reaches_the_shell_through_env(self):
        step = self.steps['Open the "needs attention" issue']
        self.assertEqual(step["env"]["MESSAGE"], "${{ steps.health.outputs.message }}")
        self.assertNotIn("${{", step["run"])

    def test_least_privilege(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read", "issues": "write"})

    def test_both_steps_use_the_same_title(self):
        title = 'title="Roadmap board sync needs attention"'
        self.assertEqual(sum(s.get("run", "").count(title) for s in self.steps.values()), 2)

    def test_the_credentials_page_describes_what_the_workflow_does(self):
        text = (REPO_ROOT / "docs" / "credentials.md").read_text(encoding="utf-8")
        for needle in ("PROJECT_TOKEN_EXPIRES", "BOARD_SYNC_ENABLED", "Roadmap board sync needs attention"):
            self.assertIn(needle, text)


if __name__ == "__main__":
    unittest.main()
