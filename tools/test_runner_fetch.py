#!/usr/bin/env python3
"""Tests for tools/runner_fetch.py and .github/workflows/fetch-pages.yml.

The network is replaced by a fake fetcher; the workflow is checked as data.

    python tools/test_runner_fetch.py
"""

from __future__ import annotations

import ast
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import host_probe  # noqa: E402
import reverify  # noqa: E402
import runner_fetch as rf  # noqa: E402

HTML = "<html><head><title>x</title><script>var a=1</script></head><body><p>" + "The Association says so. " * 30 + "</p></body></html>"


def page(url="https://efta.int/a", status=200, ctype="text/html", body=None, error="", blocked=False):
    return rf.Page(url, status, ctype, HTML.encode() if body is None else body, error, blocked)


class TestParseUrls(unittest.TestCase):
    def test_separators(self):
        self.assertEqual(rf.parse_urls("https://a.org/x, https://b.org/y\nhttps://c.org/z"),
                         ["https://a.org/x", "https://b.org/y", "https://c.org/z"])

    def test_order_is_kept_and_duplicates_dropped(self):
        self.assertEqual(rf.parse_urls("https://b.org https://a.org https://b.org"), ["https://b.org", "https://a.org"])

    def test_only_https(self):
        for bad in ("http://a.org/", "ftp://a.org/", "file:///etc/passwd", "javascript:alert(1)", "a.org/x", "//a.org"):
            with self.subTest(bad=bad), self.assertRaises(rf.FetchError):
                rf.parse_urls(f"https://ok.org/ {bad}")

    def test_nothing_is_an_error(self):
        for empty in ("", "  ", " , ,"):
            with self.assertRaises(rf.FetchError):
                rf.parse_urls(empty)

    def test_the_limit(self):
        ok = " ".join(f"https://h{i}.org/" for i in range(rf.MAX_URLS))
        self.assertEqual(len(rf.parse_urls(ok)), rf.MAX_URLS)
        with self.assertRaisesRegex(rf.FetchError, "limit"):
            rf.parse_urls(ok + " https://extra.org/")


class TestNames(unittest.TestCase):
    def test_file_stems_are_safe(self):
        self.assertEqual(rf.file_stem(3, "https://www.EFTA.int/a/b"), "03-www.efta.int")
        self.assertNotIn("/", rf.file_stem(1, "https://a.org/../../etc"))
        self.assertLessEqual(len(rf.file_stem(1, "https://" + "a" * 200 + ".org/")), 60)

    def test_text_types(self):
        self.assertTrue(rf.is_text("text/html"))
        self.assertTrue(rf.is_text("application/xhtml+xml"))
        self.assertFalse(rf.is_text("application/pdf"))
        self.assertFalse(rf.is_text(""))


class TestSave(unittest.TestCase):
    def saved(self, p, index=1):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            s = rf.save(p, index, out)
            files = {f.name: f.read_bytes() for f in out.iterdir()}
            return s, files

    def test_a_readable_page_is_saved_as_visible_text(self):
        s, files = self.saved(page())
        self.assertEqual((s.verdict, s.file), (host_probe.READABLE, "01-efta.int.txt"))
        text = files["01-efta.int.txt"].decode()
        self.assertTrue(text.startswith("https://efta.int/a\n"))
        self.assertIn("The Association says so.", text)
        self.assertNotIn("var a=1", text)
        self.assertNotIn("<p>", text)

    def test_a_pdf_is_saved_as_it_is(self):
        raw = b"%PDF-1.7 binary \x00\x01 data"
        s, files = self.saved(page("https://x.org/a.pdf", ctype="application/pdf", body=raw), 2)
        self.assertEqual(s.file, "02-x.org.pdf")
        self.assertEqual(files["02-x.org.pdf"], raw)

    def test_a_pdf_served_with_the_wrong_type_is_still_a_pdf(self):
        s, files = self.saved(page("https://x.org/a", ctype="application/octet-stream", body=b"%PDF-1.4 ..."))
        self.assertTrue(s.file.endswith(".pdf"))

    def test_a_challenge_page_is_reported_and_not_saved(self):
        s, files = self.saved(page(status=403, body=b"<title>Just a moment...</title>"))
        self.assertEqual((s.verdict, s.file, files), (host_probe.CHALLENGE, "", {}))

    def test_a_shell_is_not_saved(self):
        s, files = self.saved(page(body=b"<html><body>enable javascript</body></html>"))
        self.assertEqual((s.verdict, files), (host_probe.JS_SHELL, {}))

    def test_a_failed_request_is_a_row_not_a_crash(self):
        s, files = self.saved(page(status=None, ctype="", body=b"", error="timed out"))
        self.assertEqual((s.verdict, files), (host_probe.ERROR, {}))

    def test_a_blocked_request_is_labelled(self):
        s, _ = self.saved(page(status=403, ctype="", body=b"", error="egress policy: no", blocked=True))
        self.assertEqual(s.verdict, host_probe.BLOCKED)

    def test_a_404_is_not_found(self):
        s, _ = self.saved(page(status=404, body=b"nope"))
        self.assertEqual(s.verdict, host_probe.NOT_FOUND)

    def test_a_declared_charset_is_honoured(self):
        body = ("<html><head><meta charset=\"iso-8859-1\"></head><body><p>" + "Zürich Straße. " * 40 + "</p></body></html>").encode("iso-8859-1")
        s, files = self.saved(page(body=body))
        self.assertIn("Zürich Straße.", files[s.file].decode())


class TestRun(unittest.TestCase):
    def test_it_writes_an_index_and_one_file_per_readable_page(self):
        pages = {"https://a.org/1": page("https://a.org/1", body=(HTML + "one").encode()),
                 "https://b.org/2": page("https://b.org/2", status=403, body=b"Access Denied captcha"),
                 "https://c.org/3": page("https://c.org/3", ctype="application/pdf", body=b"%PDF-1.7 x")}
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "report"
            saved = rf.run(list(pages), out, 0, fetcher=lambda u: pages[u], sleep=lambda s: None)
            self.assertEqual(sorted(f.name for f in out.iterdir()), ["01-a.org.txt", "03-c.org.pdf", "index.md"])
            index = (out / "index.md").read_text()
            for url in pages:
                self.assertIn(url, index)
            self.assertIn("nothing in the repository was changed", index)
        self.assertEqual([s.verdict for s in saved], [host_probe.READABLE, host_probe.CHALLENGE, host_probe.READABLE])

    def test_it_pauses_between_pages_but_not_before_the_first(self):
        slept = []
        with tempfile.TemporaryDirectory() as d:
            rf.run(["https://a.org/1", "https://a.org/2", "https://a.org/3"], Path(d), 2.5,
                   fetcher=lambda u: page(u, body=(HTML + u).encode()), sleep=slept.append)
        self.assertEqual(slept, [2.5, 2.5])

    def test_one_text_served_for_two_addresses_of_one_host_is_a_shell(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            saved = rf.run(["https://spa.org/1", "https://spa.org/2"], out, 0,
                           fetcher=lambda u: page(u, body=HTML.encode()), sleep=lambda s: None)
            self.assertEqual({s.verdict for s in saved}, {host_probe.JS_SHELL})
            self.assertEqual([f.name for f in out.iterdir()], ["index.md"])

    def test_the_same_text_on_two_hosts_is_kept(self):
        with tempfile.TemporaryDirectory() as d:
            saved = rf.run(["https://a.org/1", "https://b.org/1"], Path(d), 0,
                           fetcher=lambda u: page(u, body=HTML.encode()), sleep=lambda s: None)
            self.assertEqual({s.verdict for s in saved}, {host_probe.READABLE})


class TestMain(unittest.TestCase):
    def test_bad_input_exits_2_and_fetches_nothing(self):
        err = io.StringIO()
        with mock.patch.object(rf, "fetch", side_effect=AssertionError("fetched")), redirect_stderr(err):
            self.assertEqual(rf.main(["--urls", "http://insecure.org/"]), 2)
        self.assertIn("only https", err.getvalue())

    def test_a_run_prints_the_index(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(rf, "fetch", side_effect=lambda u: page(u)), \
                mock.patch.object(rf.time, "sleep"):
            out = io.StringIO()
            with redirect_stdout(out):
                code = rf.main(["--urls", "https://efta.int/a", "--out", str(Path(d) / "o")])
            self.assertEqual(code, 0)
            self.assertIn("| 1 | READABLE |", out.getvalue())


class TestSource(unittest.TestCase):
    SRC = (REPO_ROOT / "tools" / "runner_fetch.py").read_text(encoding="utf-8")

    def test_tls_verification_is_never_relaxed(self):
        for bad in ("_create_unverified_context", "CERT_NONE", "check_hostname = False", "verify=False"):
            self.assertNotIn(bad, self.SRC)
        self.assertIn("reverify._ssl_context()", self.SRC)

    def test_it_uses_the_honest_user_agent_only(self):
        self.assertIn("reverify.USER_AGENT", self.SRC)
        self.assertNotIn("Mozilla", self.SRC)

    def test_it_writes_only_into_the_output_directory(self):
        calls = [n for n in ast.walk(ast.parse(self.SRC)) if isinstance(n, ast.Call)
                 and getattr(n.func, "attr", "") in ("write_text", "write_bytes")]
        for c in calls:
            self.assertTrue(ast.dump(c.func.value).count("out") >= 1, ast.dump(c)[:120])

    def test_it_never_edits_entities(self):
        for bad in ("apply_verification", "--write", "subprocess", "git "):
            self.assertNotIn(bad, self.SRC)


class TestWorkflow(unittest.TestCase):
    TEXT = (REPO_ROOT / ".github" / "workflows" / "fetch-pages.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.on = cls.wf.get("on", cls.wf.get(True))
        cls.job = cls.wf["jobs"]["fetch"]

    def test_manual_only(self):
        self.assertEqual(set(self.on), {"workflow_dispatch"})

    def test_read_only_and_no_secrets(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read"})
        self.assertNotIn("${{ secrets", self.TEXT)

    def test_it_changes_nothing_in_the_repository(self):
        for bad in ("git push", "git commit", "gh pr", "gh issue", "--write"):
            self.assertNotIn(bad, self.TEXT)

    def test_the_addresses_reach_the_shell_through_an_env_variable(self):
        self.assertEqual(self.job["env"]["URLS"], "${{ inputs.urls }}")
        self.assertNotIn("${{ inputs.urls }}", "\n".join(s.get("run", "") for s in self.job["steps"]))
        run = next(s["run"] for s in self.job["steps"] if s.get("name") == "Read the pages")
        self.assertIn('--urls "$URLS"', run)

    def test_the_pages_are_attached_even_if_a_step_fails(self):
        step = next(s for s in self.job["steps"] if s.get("uses", "").startswith("actions/upload-artifact"))
        self.assertEqual(step["if"], "always()")
        self.assertRegex(step["uses"], r"@v[7-9]")

    def test_the_input_is_required(self):
        self.assertIs(self.on["workflow_dispatch"]["inputs"]["urls"]["required"], True)


if __name__ == "__main__":
    unittest.main()
