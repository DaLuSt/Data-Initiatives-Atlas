#!/usr/bin/env python3
"""Tests for tools/linkedin_post.py and .github/workflows/linkedin-post.yml.

LinkedIn is replaced by a fake sender; the workflow is checked as data. No network.

    python tools/test_linkedin_post.py
"""

from __future__ import annotations

import ast
import datetime as dt
import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import linkedin_post as lp  # noqa: E402
import release  # noqa: E402

TOKEN = "AQX-the-access-token"
AUTHOR = "urn:li:person:782bbtaQ"
TODAY = dt.date(2026, 10, 12)


def fake_sender(status=201, headers=None, body="", seen=None):
    def sender(req):
        if seen is not None:
            seen.append(req)
        return status, {"x-restli-id": "urn:li:share:6844785523593134080", **(headers or {})}, body
    return sender


class TestEscape(unittest.TestCase):
    def test_every_reserved_character_gets_a_backslash(self):
        for ch in "\\|{}@[]()<>*_~":
            self.assertEqual(lp.escape_commentary(f"a{ch}b"), f"a\\{ch}b", ch)

    def test_a_hashtag_stays_a_hashtag(self):
        self.assertEqual(lp.escape_commentary("#opendata #datagovernance"), "#opendata #datagovernance")

    def test_a_number_after_a_hash_is_text(self):
        self.assertEqual(lp.escape_commentary("(roadmap #459)"), "\\(roadmap \\#459\\)")

    def test_a_hash_inside_a_word_is_text(self):
        self.assertEqual(lp.escape_commentary("a#b"), "a\\#b")

    def test_a_hash_after_a_bracket_is_text(self):
        self.assertEqual(lp.escape_commentary("(#tag)"), "\\(\\#tag\\)")

    def test_plain_text_and_newlines_are_untouched(self):
        self.assertEqual(lp.escape_commentary("Hello, world.\n• item: 2026.10.3"), "Hello, world.\n• item: 2026.10.3")

    def test_the_release_draft_survives(self):
        text = release.linkedin_draft("## Data release 2026.10.9 — 2026-10-12\n\n### Data\n\n- UK: a thing (#1)\n", "2026.10.9")
        out = lp.escape_commentary(text)
        self.assertIn("#opendata #datagovernance #digitalgovernment", out)
        self.assertNotIn("\\#opendata", out)


class TestExtractDraft(unittest.TestCase):
    BODY = "A draft.\n\n```text\nLine one\n\nLine two #tag\n```\n\nRelease: https://example\n"

    def test_takes_the_text_block(self):
        self.assertEqual(lp.extract_draft(self.BODY), "Line one\n\nLine two #tag\n")

    def test_takes_the_owners_edit(self):
        edited = self.BODY.replace("Line one", "Line one, edited")
        self.assertIn("edited", lp.extract_draft(edited))

    def test_handles_windows_line_endings(self):
        out = lp.extract_draft(self.BODY.replace("\n", "\r\n"))
        self.assertTrue(out.startswith("Line one"))
        self.assertIn("Line two #tag", out)

    def test_no_block_is_refused(self):
        with self.assertRaises(lp.PostError) as cm:
            lp.extract_draft("no block here")
        self.assertEqual(cm.exception.code, 2)

    def test_an_empty_block_is_refused(self):
        with self.assertRaises(lp.PostError):
            lp.extract_draft("```text\n\n```")


class TestVersionAndExpiry(unittest.TestCase):
    def test_default_version_is_last_month(self):
        self.assertEqual(lp.default_version(dt.date(2026, 10, 12)), "202609")

    def test_default_version_crosses_the_year(self):
        self.assertEqual(lp.default_version(dt.date(2027, 1, 3)), "202612")

    def test_days_left(self):
        self.assertEqual(lp.days_left("2026-10-20", TODAY), 8)
        self.assertEqual(lp.days_left("2026-10-12", TODAY), 0)
        self.assertEqual(lp.days_left("2026-10-10", TODAY), -2)

    def test_not_recorded_is_none(self):
        self.assertIsNone(lp.days_left("", TODAY))

    def test_garbage_is_refused(self):
        with self.assertRaises(lp.PostError):
            lp.days_left("soon", TODAY)


class TestBuildRequest(unittest.TestCase):
    def req(self, text="Hello (world) #opendata\n"):
        return lp.build_request(text, AUTHOR, TOKEN, "202609")

    def test_endpoint_and_method(self):
        r = self.req()
        self.assertEqual(r.full_url, "https://api.linkedin.com/rest/posts")
        self.assertEqual(r.get_method(), "POST")

    def test_required_headers(self):
        h = {k.lower(): v for k, v in self.req().header_items()}
        self.assertEqual(h["authorization"], f"Bearer {TOKEN}")
        self.assertEqual(h["x-restli-protocol-version"], "2.0.0")
        self.assertEqual(h["linkedin-version"], "202609")
        self.assertEqual(h["content-type"], "application/json")

    def test_body_is_a_public_text_post_by_the_author(self):
        b = json.loads(self.req().data)
        self.assertEqual(b["author"], AUTHOR)
        self.assertEqual(b["visibility"], "PUBLIC")
        self.assertEqual(b["lifecycleState"], "PUBLISHED")
        self.assertEqual(b["distribution"]["feedDistribution"], "MAIN_FEED")
        self.assertEqual(b["commentary"], "Hello \\(world\\) #opendata\n")
        self.assertNotIn("content", b)

    def test_the_token_is_not_in_the_body(self):
        self.assertNotIn(TOKEN.encode(), self.req().data)


class TestPost(unittest.TestCase):
    def go(self, text="Hello\n", **kw):
        said = []
        kw.setdefault("sender", fake_sender())
        kw.setdefault("today", TODAY)
        link = lp.post(text, kw.pop("author", AUTHOR), kw.pop("token", TOKEN), say=said.append, **kw)
        return link, said

    def test_returns_the_link_from_the_post_id(self):
        link, _ = self.go()
        self.assertEqual(link, "https://www.linkedin.com/feed/update/urn:li:share:6844785523593134080/")

    def test_sends_exactly_one_request(self):
        seen = []
        self.go(sender=fake_sender(seen=seen))
        self.assertEqual(len(seen), 1)

    def test_a_dry_run_sends_nothing_and_shows_the_text(self):
        seen = []
        link, said = self.go("The text\n", dry_run=True, sender=fake_sender(seen=seen))
        self.assertIsNone(link)
        self.assertEqual(seen, [])
        self.assertIn("The text", "\n".join(said))

    def test_a_dry_run_needs_no_token(self):
        link, _ = self.go(token="", dry_run=True)
        self.assertIsNone(link)

    def test_a_real_post_needs_a_token(self):
        with self.assertRaisesRegex(lp.PostError, "ACCESS_TOKEN"):
            self.go(token="")

    def test_a_bad_author_is_refused_before_sending(self):
        seen = []
        with self.assertRaisesRegex(lp.PostError, "AUTHOR_URN"):
            self.go(author="not-a-urn", sender=fake_sender(seen=seen))
        self.assertEqual(seen, [])

    def test_organisation_authors_are_accepted(self):
        self.go(author="urn:li:organization:5515715")

    def test_text_over_the_limit_is_refused_before_sending(self):
        seen = []
        with self.assertRaises(lp.PostError) as cm:
            self.go("x" * 3001, sender=fake_sender(seen=seen))
        self.assertEqual(cm.exception.code, 2)
        self.assertEqual(seen, [])

    def test_the_limit_matches_the_draft_builder(self):
        self.assertEqual(lp.LIMIT, release.LINKEDIN_LIMIT)

    def test_an_expired_token_is_refused_before_sending(self):
        seen = []
        with self.assertRaisesRegex(lp.PostError, "expired 2 day"):
            self.go(expires="2026-10-10", sender=fake_sender(seen=seen))
        self.assertEqual(seen, [])

    def test_a_token_close_to_expiry_warns_but_posts(self):
        link, said = self.go(expires="2026-10-20")
        self.assertTrue(link)
        self.assertTrue(any("8 day" in s for s in said))

    def test_a_token_far_from_expiry_is_quiet(self):
        _, said = self.go(expires="2026-12-01")
        self.assertEqual(said, [])

    def test_the_version_defaults_to_last_month(self):
        seen = []
        self.go(sender=fake_sender(seen=seen))
        self.assertEqual({k.lower(): v for k, v in seen[0].header_items()}["linkedin-version"], "202609")

    def test_an_explicit_version_wins(self):
        seen = []
        self.go(version="202610", sender=fake_sender(seen=seen))
        self.assertEqual({k.lower(): v for k, v in seen[0].header_items()}["linkedin-version"], "202610")

    def test_errors_say_what_to_do_and_never_show_the_token(self):
        for status, needle in ((401, "linkedin_auth.py"), (403, "w_member_social"), (422, "rejected"),
                               (426, "LINKEDIN_API_VERSION"), (429, "rate limit"), (500, "unexpected")):
            with self.subTest(status=status):
                with self.assertRaises(lp.PostError) as cm:
                    self.go(sender=fake_sender(status=status, body=f'{{"message":"nope {TOKEN}"}}'.replace(TOKEN, "x")))
                self.assertIn(needle, str(cm.exception))
                self.assertNotIn(TOKEN, str(cm.exception))

    def test_a_201_without_an_id_is_an_error_that_warns_against_posting_twice(self):
        def sender(req):
            return 201, {}, ""
        with self.assertRaisesRegex(lp.PostError, "before posting again"):
            self.go(sender=sender)


class TestMain(unittest.TestCase):
    ENV = {"LINKEDIN_ACCESS_TOKEN": TOKEN, "LINKEDIN_AUTHOR_URN": AUTHOR,
           "LINKEDIN_TOKEN_EXPIRES": "", "LINKEDIN_API_VERSION": ""}

    def run_main(self, argv, post_result=None, post_error=None, body="Hello\n"):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "post.txt"
            f.write_text(body, encoding="utf-8")
            argv = [a.replace("FILE", str(f)) for a in argv]
            out, err = io.StringIO(), io.StringIO()
            with mock.patch.dict("os.environ", self.ENV), \
                    mock.patch.object(lp, "post", return_value=post_result, side_effect=post_error) as p, \
                    redirect_stdout(out), redirect_stderr(err):
                code = lp.main(argv)
            return code, out.getvalue(), err.getvalue(), p

    def test_success_prints_the_link(self):
        code, out, _, _ = self.run_main(["post", "--text-file", "FILE"], post_result="https://x/")
        self.assertEqual((code, out), (0, "posted: https://x/\n"))

    def test_a_dry_run_prints_no_link_and_passes_the_flag(self):
        code, out, _, p = self.run_main(["post", "--text-file", "FILE", "--dry-run"])
        self.assertEqual((code, out), (0, ""))
        self.assertTrue(p.call_args.kwargs["dry_run"])

    def test_a_failure_exits_with_the_errors_code_and_no_token(self):
        code, _, err, _ = self.run_main(["post", "--text-file", "FILE"], post_error=lp.PostError("HTTP 401: nope", 1))
        self.assertEqual(code, 1)
        self.assertIn("HTTP 401", err)
        self.assertNotIn(TOKEN, err)

    def test_a_refusal_exits_2(self):
        code, *_ = self.run_main(["post", "--text-file", "FILE"], post_error=lp.PostError("too long", 2))
        self.assertEqual(code, 2)

    def test_a_missing_file_exits_2(self):
        err = io.StringIO()
        with mock.patch.dict("os.environ", self.ENV), redirect_stderr(err):
            self.assertEqual(lp.main(["post", "--text-file", "/no/such/file"]), 2)

    def test_extract_prints_the_draft(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "issue.md"
            f.write_text("x\n```text\nThe draft\n```\n", encoding="utf-8")
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(lp.main(["extract", "--issue-body-file", str(f)]), 0)
            self.assertEqual(out.getvalue(), "The draft\n")


class TestSourceSafety(unittest.TestCase):
    SRC = (REPO_ROOT / "tools" / "linkedin_post.py").read_text(encoding="utf-8")

    def test_standard_library_only(self):
        mods = set()
        for node in ast.walk(ast.parse(self.SRC)):
            if isinstance(node, ast.Import):
                mods |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom) and node.module:
                mods.add(node.module.split(".")[0])
        self.assertLessEqual(mods, set(sys.stdlib_module_names) | {"__future__"}, mods)

    def test_it_only_talks_to_the_posts_api(self):
        urls = set(re.findall(r"https?://[^\s\"']+", self.SRC))
        hosts = {u.split("/")[2] for u in urls if "example" not in u}
        self.assertLessEqual(hosts, {"api.linkedin.com", "www.linkedin.com"}, hosts)

    def test_it_never_prints_or_raises_with_the_token(self):
        # No print(), say() or PostError() call may take the token variable as an argument
        # (directly or inside an f-string); it goes to build_request and nowhere else.
        for node in ast.walk(ast.parse(self.SRC)):
            if isinstance(node, ast.Call):
                name = getattr(node.func, "id", getattr(node.func, "attr", ""))
                if name in ("print", "say", "PostError", "write"):
                    names = {n.id for arg in node.args for n in ast.walk(arg) if isinstance(n, ast.Name)}
                    self.assertNotIn("token", names, ast.dump(node)[:100])


class TestWorkflow(unittest.TestCase):
    TEXT = (REPO_ROOT / ".github" / "workflows" / "linkedin-post.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.job = cls.wf["jobs"]["post"]
        cls.on = cls.wf.get("on", cls.wf.get(True))  # YAML reads a bare `on` as True

    def test_it_runs_only_in_the_protected_environment(self):
        self.assertEqual(self.job["environment"], "linkedin")

    def test_it_cannot_be_started_by_a_pull_request_or_a_push(self):
        self.assertEqual(set(self.on), {"workflow_run", "workflow_dispatch"})

    def test_the_automatic_path_needs_the_enabling_variable_and_a_successful_release(self):
        cond = self.job["if"]
        self.assertIn("vars.LINKEDIN_POST_ENABLED == 'true'", cond)
        self.assertIn("workflow_run.conclusion == 'success'", cond)

    def test_it_follows_the_publish_workflow_on_main_only(self):
        wr = self.on["workflow_run"]
        self.assertEqual(wr["workflows"], ["Publish release"])
        self.assertEqual(wr["branches"], ["main"])

    def test_a_manual_run_is_a_dry_run_by_default(self):
        self.assertIs(self.on["workflow_dispatch"]["inputs"]["dry_run"]["default"], True)

    def test_least_privilege(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read", "issues": "write"})

    def test_the_job_does_not_import_yaml_it_never_installs(self):
        # The automatic path (no `version` input) once read metadata/version.yaml with
        # `python -c "import yaml ..."`; the job installs nothing, so the bare runner Python
        # has no PyYAML and the step failed with ModuleNotFoundError (2026-10-12).
        installs = "pip install" in self.TEXT
        self.assertTrue(installs or "import yaml" not in self.TEXT,
                        "the workflow imports yaml but does not install PyYAML")

    def test_the_version_is_found_without_python_when_no_input_is_given(self):
        import re, subprocess
        step = next(s for s in self.job["steps"] if s.get("id") == "draft")
        line = next(l for l in step["run"].splitlines() if "metadata/version.yaml" in l)
        self.assertIn("data_release", line)
        out = subprocess.run(["bash", "-c", line.split("=", 1)[0].strip() + "=" + line.split("=", 1)[1].strip() + '; echo "$version"'],
                             cwd=REPO_ROOT, capture_output=True, text=True)
        expected = re.search(r'data_release: "?([^"\n]+)"?', (REPO_ROOT / "metadata" / "version.yaml").read_text()).group(1)
        self.assertEqual(out.stdout.strip(), expected)

    def test_one_post_at_a_time(self):
        self.assertEqual(self.wf["concurrency"]["group"], "linkedin-post")
        self.assertIs(self.wf["concurrency"]["cancel-in-progress"], False)

    def test_secrets_appear_only_in_the_posting_steps_env(self):
        for step in self.job["steps"]:
            blob = json.dumps(step.get("run", ""))
            self.assertNotIn("secrets.", blob, step.get("name"))
            if "secrets.LINKEDIN_ACCESS_TOKEN" in json.dumps(step.get("env", {})):
                self.assertEqual(step["name"], "Post to LinkedIn")
        self.assertEqual(self.TEXT.count("secrets.LINKEDIN_ACCESS_TOKEN"), 1)

    def test_the_issue_is_read_in_a_step_after_the_environment_approval(self):
        # The environment's approval happens before any step runs, so reading the issue
        # inside a step means the owner's edits made while waiting are what is posted.
        step = next(s for s in self.job["steps"] if s.get("name") == "Find the release and its draft issue")
        self.assertIn("gh issue view", step["run"])
        self.assertIn("Read after the approval", step["run"])

    def test_it_will_not_post_twice(self):
        run = next(s["run"] for s in self.job["steps"] if s.get("name") == "Find the release and its draft issue")
        self.assertIn("linkedin-posted", run)
        self.assertIn('"$state" != "OPEN"', run)
        rec = next(s for s in self.job["steps"] if s.get("name") == "Record the post on the issue")
        self.assertIn("linkedin-posted", rec["run"])
        self.assertIn("gh issue close", rec["run"])

    def test_a_failure_is_reported_on_the_issue_and_leaves_it_open(self):
        fail = next(s for s in self.job["steps"] if s.get("name") == "Say it failed")
        self.assertIn("failure()", fail["if"])
        self.assertNotIn("gh issue close", fail["run"])
        self.assertIn("by hand", fail["run"])

    def test_actions_are_on_current_node_versions(self):
        for step in self.job["steps"]:
            uses = step.get("uses", "")
            if uses.startswith("actions/checkout"):
                self.assertRegex(uses, r"@v[7-9]")
            if uses.startswith("actions/setup-python"):
                self.assertRegex(uses, r"@v[7-9]")

    def test_the_versions_input_is_validated_before_use(self):
        run = next(s["run"] for s in self.job["steps"] if s.get("name") == "Find the release and its draft issue")
        self.assertIn("is not a data release", run)

    def test_the_draft_issue_has_the_block_the_tool_extracts(self):
        pub = (REPO_ROOT / ".github" / "workflows" / "release-publish.yml").read_text(encoding="utf-8")
        self.assertIn("echo '```text'", pub)
        self.assertIn("Post data release $version on LinkedIn", pub)
        self.assertIn('title="Post data release $version on LinkedIn"', pub)
        self.assertIn("--label linkedin", pub)
        self.assertIn("gh issue list --state all --label linkedin", self.TEXT)

    def test_the_draft_issue_reminds_the_owner_to_post_on_the_page(self):
        pub = (REPO_ROOT / ".github" / "workflows" / "release-publish.yml").read_text(encoding="utf-8")
        self.assertIn("Also post it on the Data Initiatives Atlas LinkedIn Page.", pub)
        self.assertIn("Post release on LinkedIn Page", pub)
        self.assertIn("docs/linkedin-page-posts.md", pub)
        # The reminder comes before the draft block, so extraction still finds the draft first.
        self.assertLess(pub.index("Also post it on the Data Initiatives Atlas LinkedIn Page"), pub.index("echo '```text'"))
        body = "A draft.\n\n**Also post it on the Data Initiatives Atlas LinkedIn Page.** x\n\n```text\nThe draft\n```\n"
        self.assertEqual(lp.extract_draft(body), "The draft\n")

    def test_the_text_is_shown_on_the_runs_summary_page(self):
        step = next(s for s in self.job["steps"] if s.get("name") == "Post to LinkedIn")
        self.assertIn("GITHUB_STEP_SUMMARY", step["run"])
        self.assertIn("cat post.txt", step["run"])
        # The summary gets the draft, never anything from the environment's secrets.
        summary = step["run"][step["run"].index("GITHUB_STEP_SUMMARY") - 600:]
        self.assertNotIn("LINKEDIN_ACCESS_TOKEN", summary)
        self.assertNotIn("LINKEDIN_AUTHOR_URN", summary)

    def test_the_tool_it_calls_exists(self):
        self.assertTrue((REPO_ROOT / "tools" / "linkedin_post.py").exists())
        self.assertIn("python tools/linkedin_post.py extract", self.TEXT)
        self.assertIn("python tools/linkedin_post.py post", self.TEXT)


PAGE = "urn:li:organization:123456789"


class TestPagePost(unittest.TestCase):
    """The same poster, in the name of the LinkedIn Page (--page)."""

    def go(self, **kw):
        args = dict(text="Hello Page\n", author=PAGE, token=TOKEN, version="202610", today=TODAY,
                    sender=fake_sender(), say=lambda *_: None, page=True)
        args.update(kw)
        return lp.post(**args)

    def test_the_post_is_made_in_the_name_of_the_page(self):
        seen = []
        self.go(sender=fake_sender(seen=seen))
        self.assertEqual(json.loads(seen[0].data)["author"], PAGE)

    def test_the_text_sent_is_the_same_as_for_the_profile(self):
        page, profile = [], []
        self.go(sender=fake_sender(seen=page))
        self.go(author=AUTHOR, page=False, sender=fake_sender(seen=profile))
        self.assertEqual(json.loads(page[0].data)["commentary"], json.loads(profile[0].data)["commentary"])

    def test_a_person_is_refused_as_the_page(self):
        with self.assertRaisesRegex(lp.PostError, "LINKEDIN_PAGE_URN must look like urn:li:organization"):
            self.go(author=AUTHOR)

    def test_a_page_id_that_is_not_a_number_is_refused(self):
        with self.assertRaises(lp.PostError):
            self.go(author="urn:li:organization:abc")

    def test_a_missing_token_names_the_pages_secret(self):
        with self.assertRaisesRegex(lp.PostError, "LINKEDIN_PAGE_ACCESS_TOKEN is not set"):
            self.go(token="")

    def test_an_expired_token_names_the_pages_renewal(self):
        with self.assertRaisesRegex(lp.PostError, r"linkedin_auth\.py --page"):
            self.go(expires="2026-10-01")

    def test_a_bad_expiry_names_the_pages_variable(self):
        with self.assertRaisesRegex(lp.PostError, "LINKEDIN_PAGE_TOKEN_EXPIRES"):
            self.go(expires="soon")

    def test_errors_name_the_pages_permission_and_environment(self):
        for status, needle in ((401, "linkedin-page"), (403, "w_organization_social")):
            with self.subTest(status=status):
                with self.assertRaises(lp.PostError) as cm:
                    self.go(sender=fake_sender(status=status, body="nope"))
                self.assertIn(needle, str(cm.exception))
                self.assertNotIn("w_member_social", str(cm.exception))

    def test_a_dry_run_sends_nothing(self):
        seen, said = [], []
        self.assertIsNone(self.go(dry_run=True, token="", sender=fake_sender(seen=seen), say=said.append))
        self.assertEqual(seen, [])
        self.assertIn(PAGE, said[0])

    def test_main_reads_the_pages_variables_not_the_profiles(self):
        env = {"LINKEDIN_PAGE_URN": PAGE, "LINKEDIN_PAGE_ACCESS_TOKEN": TOKEN,
               "LINKEDIN_PAGE_TOKEN_EXPIRES": "2027-01-01", "LINKEDIN_AUTHOR_URN": AUTHOR,
               "LINKEDIN_ACCESS_TOKEN": "profile-token"}
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
            fh.write("hi")
        out = io.StringIO()
        with mock.patch.dict("os.environ", env, clear=True), \
                mock.patch.object(lp, "post", return_value="https://x/") as p, redirect_stdout(out):
            code = lp.main(["post", "--page", "--text-file", fh.name])
        self.assertEqual(code, 0)
        args = p.call_args
        self.assertEqual(args.args[1], PAGE)
        self.assertEqual(args.args[2], TOKEN)
        self.assertEqual(args.kwargs["expires"], "2027-01-01")
        self.assertIs(args.kwargs["page"], True)

    def test_main_without_page_still_uses_the_profile(self):
        env = {"LINKEDIN_PAGE_URN": PAGE, "LINKEDIN_PAGE_ACCESS_TOKEN": "page-token",
               "LINKEDIN_AUTHOR_URN": AUTHOR, "LINKEDIN_ACCESS_TOKEN": TOKEN}
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
            fh.write("hi")
        with mock.patch.dict("os.environ", env, clear=True), \
                mock.patch.object(lp, "post", return_value="https://x/") as p, redirect_stdout(io.StringIO()):
            lp.main(["post", "--text-file", fh.name])
        self.assertEqual(p.call_args.args[1], AUTHOR)
        self.assertEqual(p.call_args.args[2], TOKEN)
        self.assertIs(p.call_args.kwargs["page"], False)


class TestPageWorkflow(unittest.TestCase):
    PATH = REPO_ROOT / ".github" / "workflows" / "linkedin-page-post.yml"
    TEXT = PATH.read_text(encoding="utf-8")
    PROFILE = (REPO_ROOT / ".github" / "workflows" / "linkedin-post.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.job = cls.wf["jobs"]["post"]
        cls.on = cls.wf.get("on", cls.wf.get(True))

    def step(self, name):
        return next(s for s in self.job["steps"] if s.get("name") == name)

    def test_it_runs_only_in_its_own_protected_environment(self):
        self.assertEqual(self.job["environment"], "linkedin-page")

    def test_it_is_a_separate_pipeline_from_the_profile_post(self):
        self.assertNotEqual(self.wf["name"], "Post release on LinkedIn")
        self.assertEqual(self.wf["concurrency"]["group"], "linkedin-page-post")
        self.assertIs(self.wf["concurrency"]["cancel-in-progress"], False)

    def test_it_cannot_be_started_by_a_pull_request_or_a_push(self):
        self.assertEqual(set(self.on), {"workflow_run", "workflow_dispatch"})
        wr = self.on["workflow_run"]
        self.assertEqual((wr["workflows"], wr["branches"]), (["Publish release"], ["main"]))

    def test_the_automatic_path_has_its_own_switch(self):
        cond = self.job["if"]
        self.assertIn("vars.LINKEDIN_PAGE_POST_ENABLED == 'true'", cond)
        self.assertNotIn("vars.LINKEDIN_POST_ENABLED", cond)
        self.assertIn("workflow_run.conclusion == 'success'", cond)

    def test_a_manual_run_is_a_dry_run_by_default(self):
        self.assertIs(self.on["workflow_dispatch"]["inputs"]["dry_run"]["default"], True)

    def test_least_privilege(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read", "issues": "write"})

    def test_the_pages_secrets_appear_only_in_the_posting_step(self):
        for step in self.job["steps"]:
            self.assertNotIn("secrets.", json.dumps(step.get("run", "")), step.get("name"))
        self.assertEqual(self.TEXT.count("secrets.LINKEDIN_PAGE_ACCESS_TOKEN"), 1)
        self.assertEqual(self.TEXT.count("secrets.LINKEDIN_PAGE_URN"), 1)
        env = self.step("Post to the LinkedIn Page")["env"]
        self.assertIn("secrets.LINKEDIN_PAGE_ACCESS_TOKEN", env["LINKEDIN_PAGE_ACCESS_TOKEN"])

    def test_it_never_uses_the_profiles_secrets(self):
        self.assertNotIn("secrets.LINKEDIN_ACCESS_TOKEN", self.TEXT)
        self.assertNotIn("secrets.LINKEDIN_AUTHOR_URN", self.TEXT)
        self.assertNotIn("secrets.LINKEDIN_PAGE_ACCESS_TOKEN", self.PROFILE)

    def test_it_posts_the_same_draft_as_the_profile(self):
        # Same issue, same extraction, read after the approval.
        for needle in ('title="Post data release $version on LinkedIn"', "--label linkedin ",
                       "python tools/linkedin_post.py extract --issue-body-file issue.md",
                       "Read after the approval"):
            self.assertIn(needle, self.TEXT)
            self.assertIn(needle, self.PROFILE)
        self.assertIn("python tools/linkedin_post.py post --page --text-file post.txt", self.TEXT)

    def test_it_will_not_post_twice_and_works_on_a_closed_issue(self):
        run = self.step("Find the release and its draft issue")["run"]
        self.assertIn("linkedin-page-posted", run)
        self.assertNotIn('"$state" != "OPEN"', run)  # the profile post closes the issue first
        self.assertNotIn(",linkedin-posted,", run)   # the profile's label says nothing about the Page
        rec = self.step("Record the post on the issue")
        self.assertIn("linkedin-page-posted", rec["run"])

    def test_it_never_closes_the_issue(self):
        self.assertNotIn("gh issue close", self.TEXT)

    def test_a_failure_is_reported_on_the_issue(self):
        fail = self.step("Say it failed")
        self.assertIn("failure()", fail["if"])
        self.assertIn("by hand", fail["run"])
        self.assertIn("--page", fail["run"])

    def test_the_version_input_is_validated_and_found_without_python(self):
        run = self.step("Find the release and its draft issue")["run"]
        self.assertIn("is not a data release", run)
        self.assertIn("metadata/version.yaml", run)
        self.assertNotIn("import yaml", self.TEXT)

    def test_actions_are_on_current_node_versions(self):
        for step in self.job["steps"]:
            uses = step.get("uses", "")
            if uses.startswith(("actions/checkout", "actions/setup-python")):
                self.assertRegex(uses, r"@v[7-9]")

    def test_the_summary_shows_the_draft_and_no_secret(self):
        run = self.step("Post to the LinkedIn Page")["run"]
        self.assertIn("GITHUB_STEP_SUMMARY", run)
        self.assertNotIn("LINKEDIN_PAGE_ACCESS_TOKEN", run[run.index("GITHUB_STEP_SUMMARY") - 600:])


if __name__ == "__main__":
    unittest.main()
