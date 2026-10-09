#!/usr/bin/env python3
"""Tests for tools/host_probe.py and .github/workflows/probe-blocked-hosts.yml.

The network is replaced by a fake fetcher; the workflow is checked as data.

    python tools/test_host_probe.py
"""

from __future__ import annotations

import ast
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import host_probe as hp  # noqa: E402
import reverify  # noqa: E402

PAGE = "<html><body>" + "Real content about the Convention. " * 30 + "</body></html>"


class TestClassify(unittest.TestCase):
    def v(self, *a, **kw):
        return hp.classify(*a, **kw)[0]

    def test_a_real_page_is_readable(self):
        self.assertEqual(self.v(200, PAGE), hp.READABLE)

    def test_a_tiny_page_is_a_js_shell(self):
        self.assertEqual(self.v(200, "<html><body><noscript>You need to enable JavaScript</noscript></body></html>"), hp.JS_SHELL)

    def test_an_empty_200_is_a_js_shell(self):
        self.assertEqual(self.v(200, ""), hp.JS_SHELL)

    def test_a_202_with_nothing_is_a_challenge(self):
        self.assertEqual(self.v(202, ""), hp.CHALLENGE)

    def test_a_cloudflare_page_is_a_challenge(self):
        self.assertEqual(self.v(403, "<title>Just a moment...</title>"), hp.CHALLENGE)
        self.assertEqual(self.v(503, "Checking your browser before accessing"), hp.CHALLENGE)

    def test_a_200_challenge_page_is_a_challenge(self):
        self.assertEqual(self.v(200, "<html>Please verify you are a human (captcha)</html>"), hp.CHALLENGE)

    def test_a_long_real_page_that_mentions_a_captcha_is_still_readable(self):
        self.assertEqual(self.v(200, PAGE + " Submit the captcha form to contact us. " + PAGE * 3), hp.READABLE)

    def test_a_plain_403_is_denied(self):
        self.assertEqual(self.v(403, "Forbidden"), hp.DENIED)
        self.assertEqual(self.v(401, ""), hp.DENIED)

    def test_404_and_410_are_not_found(self):
        self.assertEqual(self.v(404, "x"), hp.NOT_FOUND)
        self.assertEqual(self.v(410, "x"), hp.NOT_FOUND)

    def test_5xx_is_a_server_error(self):
        self.assertEqual(self.v(503, "down"), hp.SERVER_ERROR)

    def test_the_proxy_refusing_is_blocked(self):
        self.assertEqual(self.v(403, "", "egress policy: host not allowed", True), hp.BLOCKED)

    def test_no_answer_is_an_error(self):
        self.assertEqual(self.v(None, "", "timed out"), hp.ERROR)

    def test_every_verdict_has_a_reason(self):
        for args in ((200, PAGE), (200, ""), (202, ""), (403, "x"), (404, ""), (503, "x"), (None, "", "dns")):
            self.assertTrue(hp.classify(*args)[1])


class TestHostMatching(unittest.TestCase):
    def test_exact_subdomain_and_www(self):
        self.assertTrue(hp.host_matches("coe.int", "coe.int"))
        self.assertTrue(hp.host_matches("rm.coe.int", "coe.int"))
        self.assertTrue(hp.host_matches("www.iso.org", "iso.org"))
        self.assertTrue(hp.host_matches("iso.org", "www.iso.org"))

    def test_a_lookalike_does_not_match(self):
        self.assertFalse(hp.host_matches("notcoe.int", "coe.int"))
        self.assertFalse(hp.host_matches("coe.int.evil.example", "coe.int"))


def ent(eid, *urls):
    return SimpleNamespace(frontmatter={"id": eid, "sources": [{"url": u} for u in urls]})


ENTS = [
    ent("B", "https://unece.org/a", "https://unece.org/b", "https://www.iso.org/member/1.html"),
    ent("A", "https://unece.org/a", "https://unece.org/c/", "ftp://unece.org/x", "not a url"),
    ent("C", "https://other.example/z"),
    SimpleNamespace(frontmatter=None),
]


class TestCollect(unittest.TestCase):
    def picks(self, hosts=("unece.org",), n=3):
        return hp.collect_urls(hosts, n, ENTS)

    def test_the_root_comes_first(self):
        self.assertEqual(self.picks()["unece.org"][0], ("https://unece.org/", []))

    def test_cited_urls_follow_with_their_entities_and_are_sorted(self):
        urls = [u for u, _ in self.picks()["unece.org"]]
        self.assertEqual(urls, ["https://unece.org/", "https://unece.org/a", "https://unece.org/b", "https://unece.org/c/"])
        self.assertEqual(dict(self.picks()["unece.org"])["https://unece.org/a"], ["A", "B"])

    def test_the_limit_applies_to_cited_urls_not_the_root(self):
        self.assertEqual(len(self.picks(n=1)["unece.org"]), 2)

    def test_non_http_and_malformed_urls_are_ignored(self):
        urls = [u for u, _ in self.picks()["unece.org"]]
        self.assertNotIn("ftp://unece.org/x", urls)

    def test_a_host_with_no_citations_still_gets_its_root(self):
        self.assertEqual(hp.collect_urls(("nowhere.example",), 3, ENTS)["nowhere.example"], [("https://nowhere.example/", [])])

    def test_www_hosts_match_a_bare_host(self):
        urls = [u for u, _ in hp.collect_urls(("iso.org",), 3, ENTS)["iso.org"]]
        self.assertIn("https://www.iso.org/member/1.html", urls)

    def test_it_is_deterministic(self):
        self.assertEqual(self.picks(), self.picks())

    def test_citing_entities(self):
        self.assertEqual(hp.citing_entities(("unece.org",), ENTS), ["A", "B"])
        self.assertEqual(hp.citing_entities(("nowhere.example",), ENTS), [])


class TestRun(unittest.TestCase):
    def test_it_classifies_each_answer_and_keeps_the_entities(self):
        answers = {"https://unece.org/": (403, "Just a moment", "", False),
                   "https://unece.org/a": (200, PAGE, "", False)}
        probes = hp.run(("unece.org",), 1, "UA", 5, 0, ENTS, fetcher=lambda u, ua, t: answers[u], sleep=lambda s: None)
        self.assertEqual([(p.url, p.verdict) for p in probes],
                         [("https://unece.org/", hp.CHALLENGE), ("https://unece.org/a", hp.READABLE)])
        self.assertEqual(probes[1].entities, ["A", "B"])

    def test_it_waits_between_requests_to_one_host_but_not_before_the_first(self):
        slept = []
        hp.run(("unece.org",), 2, "UA", 5, 1.5, ENTS, fetcher=lambda u, ua, t: (200, PAGE, "", False), sleep=slept.append)
        self.assertEqual(slept, [1.5, 1.5])

    def test_it_passes_the_user_agent_and_timeout(self):
        seen = []
        hp.run(("unece.org",), 0, "THE-UA", 7, 0, ENTS, fetcher=lambda u, ua, t: seen.append((ua, t)) or (200, PAGE, "", False),
               sleep=lambda s: None)
        self.assertEqual(seen, [("THE-UA", 7)])

    def test_one_failing_url_does_not_stop_the_sweep(self):
        probes = hp.run(("unece.org", "iso.org"), 1, "UA", 5, 0, ENTS,
                        fetcher=lambda u, ua, t: (None, "", "boom", False), sleep=lambda s: None)
        self.assertEqual({p.verdict for p in probes}, {hp.ERROR})
        self.assertEqual({p.host for p in probes}, {"unece.org", "iso.org"})


class TestVerdictsAndReport(unittest.TestCase):
    def P(self, host, verdict, url="https://x/", detail="d", ents=()):
        return hp.Probe(host, url, 200, verdict, detail, list(ents))

    def test_host_verdicts(self):
        r, d, n = self.P("h", hp.READABLE), self.P("h", hp.DENIED), self.P("h", hp.NOT_FOUND)
        self.assertEqual(hp.host_verdict([r, r]), "READABLE")
        self.assertEqual(hp.host_verdict([r, d]), "PARTLY READABLE")
        self.assertEqual(hp.host_verdict([d, d, n]), "NOT READABLE (DENIED)")
        self.assertEqual(hp.host_verdict([n]), "NOT READABLE (NOT_FOUND)")

    def test_the_report_names_the_agent_the_hosts_and_each_url(self):
        probes = [self.P("a.org", hp.READABLE, "https://a.org/", ents=["E1", "E2", "E3", "E4", "E5"]),
                  self.P("b.org", hp.CHALLENGE, "https://b.org/", "a challenge page")]
        md = hp.render_markdown(probes, "browser-like")
        self.assertIn("User-Agent used: **browser-like**", md)
        self.assertIn("| `a.org` | READABLE | 1 of 1 |", md)
        self.assertIn("| `b.org` | NOT READABLE (CHALLENGE) | 0 of 1 |", md)
        self.assertIn("**Readable here:** `a.org`", md)
        self.assertIn("E1, E2, E3, E4 …", md)
        self.assertIn("nothing in the repository was changed", md)


class TestMain(unittest.TestCase):
    def run_main(self, argv):
        out = io.StringIO()
        with mock.patch.object(hp, "load_all_entities", return_value=ENTS), redirect_stdout(out):
            code = hp.main(argv)
        return code, out.getvalue()

    def test_offline_lists_urls_and_fetches_nothing(self):
        with mock.patch.object(hp, "fetch", side_effect=AssertionError("fetched")):
            code, out = self.run_main(["--hosts", "unece.org", "--offline"])
        self.assertEqual(code, 0)
        self.assertIn("unece.org\thttps://unece.org/a\tA,B", out)

    def test_list_entities(self):
        code, out = self.run_main(["--hosts", "unece.org", "--list-entities"])
        self.assertEqual(out.split(), ["A", "B"])

    def test_it_writes_the_two_report_files_only_where_asked(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(hp, "fetch", return_value=(200, PAGE, "", False)), \
                mock.patch.object(hp.time, "sleep"):
            j, m = Path(d) / "p.json", Path(d) / "p.md"
            code, out = self.run_main(["--hosts", "unece.org", "--per-host", "1", "--json", str(j), "--markdown", str(m)])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(j.read_text())[0]["verdict"], "READABLE")
            self.assertIn("unece.org", m.read_text())
            self.assertEqual(sorted(p.name for p in Path(d).iterdir()), ["p.json", "p.md"])

    def test_the_honest_agent_is_the_default_and_the_browser_one_is_opt_in(self):
        seen = []
        def fake(url, ua, timeout):
            seen.append(ua)
            return 200, PAGE, "", False
        with mock.patch.object(hp, "fetch", side_effect=fake), mock.patch.object(hp.time, "sleep"):
            self.run_main(["--hosts", "unece.org", "--per-host", "0"])
            self.run_main(["--hosts", "unece.org", "--per-host", "0", "--browser-ua"])
        self.assertEqual(seen, [reverify.USER_AGENT, hp.BROWSER_UA])


class TestSource(unittest.TestCase):
    SRC = (REPO_ROOT / "tools" / "host_probe.py").read_text(encoding="utf-8")

    def test_tls_verification_is_never_relaxed(self):
        for bad in ("_create_unverified_context", "CERT_NONE", "check_hostname = False", "verify=False"):
            self.assertNotIn(bad, self.SRC)

    def test_it_uses_the_reverify_tls_context(self):
        self.assertIn("reverify._ssl_context()", self.SRC)

    def test_it_only_writes_to_paths_it_is_given(self):
        calls = [n for n in ast.walk(ast.parse(self.SRC)) if isinstance(n, ast.Call)
                 and getattr(n.func, "attr", "") in ("write_text", "write_bytes", "mkdir")]
        self.assertEqual(len(calls), 2)  # --json and --markdown, nothing else

    def test_it_never_edits_entities(self):
        for bad in ("apply_verification", "--write", "subprocess", "git "):
            self.assertNotIn(bad, self.SRC)

    def test_the_default_hosts_are_the_known_block_rows(self):
        text = (REPO_ROOT / "discovery" / "unresolved.md").read_text(encoding="utf-8")
        for host in ("coe.int", "iso.org", "unece.org", "unctad.org", "bmi.bund.de", "geant.org",
                     "digitaleoverheid.nl", "eur-lex.europa.eu", "efta.int"):
            self.assertIn(host, hp.DEFAULT_HOSTS)
            self.assertIn(host, text)


class TestWorkflow(unittest.TestCase):
    TEXT = (REPO_ROOT / ".github" / "workflows" / "probe-blocked-hosts.yml").read_text(encoding="utf-8")

    @classmethod
    def setUpClass(cls):
        import yaml
        cls.wf = yaml.safe_load(cls.TEXT)
        cls.on = cls.wf.get("on", cls.wf.get(True))
        cls.steps = cls.wf["jobs"]["probe"]["steps"]

    def test_it_starts_only_by_hand(self):
        self.assertEqual(set(self.on), {"workflow_dispatch"})

    def test_it_can_read_the_repository_and_nothing_more(self):
        self.assertEqual(self.wf["permissions"], {"contents": "read"})

    def test_it_uses_no_secrets(self):
        self.assertNotIn("${{ secrets", self.TEXT)

    def test_it_changes_nothing_in_the_repository(self):
        for bad in ("git push", "git commit", "--write", "gh pr", "gh issue"):
            self.assertNotIn(bad, self.TEXT)

    def test_the_slow_reverify_is_off_by_default_and_the_browser_probe_is_on(self):
        inputs = self.on["workflow_dispatch"]["inputs"]
        self.assertIs(inputs["reverify"]["default"], False)
        self.assertIs(inputs["browser_ua"]["default"], True)

    def test_the_report_is_attached_even_if_a_step_fails(self):
        step = next(s for s in self.steps if s.get("uses", "").startswith("actions/upload-artifact"))
        self.assertEqual(step["if"], "always()")
        self.assertRegex(step["uses"], r"@v[7-9]")

    def test_the_host_list_reaches_the_shell_through_an_env_variable_not_the_script_text(self):
        self.assertNotIn("${{ inputs.hosts }}", "\n".join(s.get("run", "") for s in self.steps))
        self.assertEqual(self.wf["jobs"]["probe"]["env"]["HOSTS"], "${{ inputs.hosts }}")

    def test_the_tools_it_calls_exist(self):
        for name in ("host_probe.py", "reverify.py"):
            self.assertTrue((REPO_ROOT / "tools" / name).exists())


if __name__ == "__main__":
    unittest.main()
