#!/usr/bin/env python3
"""Tests for tools/reverify.py.

None of these touch the network. The fetching path is exercised through
`FetchResult` values built by hand, because the behaviour worth pinning down
is how the tool *classifies* an outcome — and in this environment every real
fetch produces exactly one of those outcomes, which would test nothing.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import reverify as rv  # noqa: E402


class TestClaimExtraction(unittest.TestCase):
    def test_legal_identifiers_are_extracted(self):
        """The identifiers the Atlas keys entities on must be picked up.

        Each of these resolves to a *different real instrument* when wrong,
        which is the whole reason the tool checks for them."""
        fm = {
            "name": "Kadasterwet",
            "alternative_names": ["BWBR0004541"],
            "description": "Cited as BOE-A-2021-17910 and CETS No. 223 and "
                           "Directive (EU) 2019/1024 and S.I. No. 376/2021.",
        }
        claims = rv.checkable_claims(fm)
        for expected in ("bwbr0004541", "boe-a-2021-17910", "cets no. 223",
                         "directive (eu) 2019/1024", "s.i. no. 376/2021"):
            self.assertIn(expected, claims, f"{expected} not extracted")

    def test_identifiers_inside_relationship_evidence_are_extracted(self):
        """Evidence strings are where most citations actually live."""
        fm = {"name": "Some Act", "relationships": [
            {"type": "amends", "target": "X",
             "evidence": "as recorded in BWBR0023466 (wetten.overheid.nl)"}]}
        self.assertIn("bwbr0023466", rv.checkable_claims(fm))

    def test_short_names_are_not_treated_as_claims(self):
        """A three-letter acronym appears on half the web; finding it proves
        nothing, and reporting it as corroboration would be misleading."""
        fm = {"name": "BAG", "alternative_names": ["WOZ", "NEN"]}
        self.assertEqual(rv.checkable_claims(fm), [])

    def test_long_names_are_claims(self):
        fm = {"name": "Wet basisregistratie adressen en gebouwen"}
        self.assertIn("wet basisregistratie adressen en gebouwen",
                      rv.checkable_claims(fm))

    def test_claims_are_deduplicated(self):
        fm = {"name": "BWBR0004541 Kadasterwet",
              "alternative_names": ["BWBR0004541"],
              "description": "BWBR0004541 again"}
        self.assertEqual(rv.checkable_claims(fm).count("bwbr0004541"), 1)

    def test_an_entity_with_no_identifier_and_no_long_name_yields_nothing(self):
        """Reported honestly rather than silently passing: an entity the tool
        cannot check is not an entity the tool has checked."""
        self.assertEqual(rv.checkable_claims({"name": "EU"}), [])


class TestMatching(unittest.TestCase):
    def test_matching_ignores_case_and_whitespace(self):
        self.assertTrue(rv.page_contains("see  ETS   No. 108 herein", "ets no. 108"))

    def test_absent_claim_is_absent(self):
        self.assertFalse(rv.page_contains("Archiefwet 1995", "bwbr0004541"))

    def test_the_near_miss_this_tool_exists_for(self):
        """A wrong BWBR identifier does not 404 — it returns another real act.

        The Kadasterwet was nearly recorded as BWBR0007376, which is the
        Archiefwet 1995. Fetching that page succeeds; only checking for the
        identifier the entity claims catches it."""
        archiefwet_page = "Archiefwet 1995 — BWBR0007376 — geldend van 01-01-2024"
        self.assertFalse(rv.page_contains(archiefwet_page, "bwbr0004541"))
        self.assertTrue(rv.page_contains(archiefwet_page, "bwbr0007376"))


class TestFetchRobustness(unittest.TestCase):
    def test_a_malformed_url_is_reported_not_raised(self):
        """One unfetchable source must never take down a sweep.

        A source URL containing a literal space raises `http.client.InvalidURL`,
        which on Python 3.11 inherits from HTTPException and *not* from
        ValueError — so the original tuple of expected exception types missed
        it and the first full sweep of the repository died six minutes in."""
        result = rv.fetch("https://example.org/a path with spaces.pdf", timeout=1)
        self.assertFalse(result.ok)
        self.assertIn("InvalidURL", result.error)
        self.assertIn("malformed URL", result.error)
        self.assertFalse(result.blocked, "a bad URL is not an egress block")

    def test_a_proxy_403_is_classified_as_blocked(self):
        """An egress denial does not always arrive as a failed CONNECT.

        A plain-`http://` URL reaches the proxy as an ordinary forward request,
        so a refusal comes back as an HTTP 403 that looks exactly like the
        origin turning us away. The proxy labels its own with `x-deny-reason`;
        the first full sweep miscounted nine such sources as UNREACHABLE
        before this was handled."""
        import email.message, io, urllib.error
        headers = email.message.Message()
        headers["x-deny-reason"] = "host_not_allowed"
        err = urllib.error.HTTPError(
            "http://example.gob.es/x", 403, "Forbidden", headers,
            io.BytesIO(b"Host not in allowlist: example.gob.es."))
        with unittest.mock.patch.object(rv.urllib.request, "urlopen", side_effect=err):
            result = rv.fetch("http://example.gob.es/x", timeout=1)
        self.assertTrue(result.blocked)
        self.assertIn("egress policy", result.error)
        self.assertIn("host_not_allowed", result.error)

    def test_an_origin_403_is_not_blocked(self):
        """A 403 without the proxy's marker is the origin's own answer, and
        calling it an egress block would send someone to fix the wrong thing."""
        import email.message, io, urllib.error
        err = urllib.error.HTTPError(
            "https://example.org/x", 403, "Forbidden", email.message.Message(),
            io.BytesIO(b"Access denied by the site."))
        with unittest.mock.patch.object(rv.urllib.request, "urlopen", side_effect=err):
            result = rv.fetch("https://example.org/x", timeout=1)
        self.assertFalse(result.blocked)
        self.assertIn("HTTP 403", result.error)
        self.assertIn("Access denied by the site", result.error)

    def test_a_nonsense_scheme_is_reported_not_raised(self):
        result = rv.fetch("not-a-url-at-all", timeout=1)
        self.assertFalse(result.ok)
        self.assertTrue(result.error)


class TestMarkupStripping(unittest.TestCase):
    def test_tags_are_removed_and_text_kept(self):
        html = "<html><body><p>ETS <b>No. 108</b></p></body></html>"
        self.assertIn("ETS No. 108", rv.strip_markup(html))

    def test_script_and_style_contents_are_dropped(self):
        """An identifier inside a script block is not the page saying it."""
        html = "<script>var x='BWBR0004541';</script><p>Archiefwet</p>"
        self.assertNotIn("BWBR0004541", rv.strip_markup(html))


def _sr(url, *, ok=False, blocked=False, status=None, found=(), missing=()):
    return rv.SourceReport(
        url=url,
        result=rv.FetchResult(url=url, ok=ok, blocked=blocked, status=status),
        found=list(found), missing=list(missing))


def _rep(sources, claims=("a", "b")):
    r = rv.EntityReport(entity_id="X", rel_path="x.md",
                        verification="search-only", claims=list(claims))
    r.sources = list(sources)
    return r


class TestVerdicts(unittest.TestCase):
    def test_no_sources(self):
        self.assertEqual(rv.decide_verdict(_rep([])), rv.NO_SOURCES)

    def test_all_blocked_is_blocked(self):
        r = _rep([_sr("u1", blocked=True), _sr("u2", blocked=True)])
        self.assertEqual(rv.decide_verdict(r), rv.BLOCKED)

    def test_unreachable_when_nothing_came_back_but_not_by_policy(self):
        r = _rep([_sr("u1", status=404), _sr("u2", status=500)])
        self.assertEqual(rv.decide_verdict(r), rv.UNREACHABLE)

    def test_a_mix_of_blocked_and_dead_is_unreachable_not_blocked(self):
        """Only an all-policy refusal is BLOCKED. One genuinely dead link
        means the allowlist is not the whole story."""
        r = _rep([_sr("u1", blocked=True), _sr("u2", status=404)])
        self.assertEqual(rv.decide_verdict(r), rv.UNREACHABLE)

    def test_all_retrieved_and_all_claims_found_is_corroborated(self):
        r = _rep([_sr("u1", ok=True, status=200, found=("a", "b"))])
        self.assertEqual(rv.decide_verdict(r), rv.CORROBORATED)

    def test_a_missing_claim_forces_review(self):
        r = _rep([_sr("u1", ok=True, status=200, found=("a",), missing=("b",))])
        self.assertEqual(rv.decide_verdict(r), rv.REVIEW)
        self.assertEqual(r.uncorroborated, ["b"])

    def test_a_claim_found_on_any_source_counts(self):
        r = _rep([_sr("u1", ok=True, status=200, found=("a",), missing=("b",)),
                  _sr("u2", ok=True, status=200, found=("b",), missing=("a",))])
        self.assertEqual(rv.decide_verdict(r), rv.CORROBORATED)
        self.assertEqual(r.uncorroborated, [])

    def test_one_unretrieved_source_forces_review_even_if_claims_are_found(self):
        """A source the pass could not read has not been re-verified, whatever
        the other sources say."""
        r = _rep([_sr("u1", ok=True, status=200, found=("a", "b")),
                  _sr("u2", blocked=True)])
        self.assertEqual(rv.decide_verdict(r), rv.REVIEW)

    def test_only_review_and_corroborated_are_writable(self):
        for verdict, writable in ((rv.BLOCKED, False), (rv.UNREACHABLE, False),
                                  (rv.NO_SOURCES, False), (rv.REVIEW, True),
                                  (rv.CORROBORATED, True)):
            r = _rep([])
            r.verdict = verdict
            self.assertEqual(r.writable, writable, verdict)


ENTITY = """---
id: XX-TEST
type: law
name: Testwet
verification: search-only
last_verified: null
sources:
  - title: "One"
    url: "https://example.org/one"
    publisher: "Pub One"
  - title: "Two"
    url: "https://example.org/two"
    publisher: "Pub Two"
---

# Testwet

> **Sourcing caveat.** Compiled from search-engine results only.

Body text.
"""


class TestWriteBack(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / "x.md"
        self.path.write_text(ENTITY, encoding="utf-8")

    def tearDown(self):
        self.dir.cleanup()

    def test_verification_and_last_verified_are_stamped(self):
        rv.apply_verification(self.path, {"https://example.org/one",
                                          "https://example.org/two"}, "2026-08-19")
        out = self.path.read_text(encoding="utf-8")
        self.assertIn("verification: primary-source", out)
        self.assertIn('last_verified: "2026-08-19"', out)

    def test_accessed_goes_only_on_retrieved_sources(self):
        """A source that did not come back was not accessed, and stamping it
        would be the exact false claim `verification` exists to prevent."""
        rv.apply_verification(self.path, {"https://example.org/one"}, "2026-08-19")
        out = self.path.read_text(encoding="utf-8")
        one = out.index("Pub One")
        two = out.index("Pub Two")
        self.assertIn("accessed", out[one:two])
        self.assertNotIn("accessed", out[two:])

    def test_the_body_is_untouched(self):
        rv.apply_verification(self.path, {"https://example.org/one"}, "2026-08-19")
        out = self.path.read_text(encoding="utf-8")
        self.assertIn("Sourcing caveat", out)
        self.assertIn("Body text.", out)

    def test_the_result_still_parses_as_an_entity(self):
        rv.apply_verification(self.path, {"https://example.org/one",
                                          "https://example.org/two"}, "2026-08-19")
        sys.path.insert(0, str(REPO_ROOT / "validation"))
        import common
        parsed = common.parse_entity_file(self.path)
        self.assertIsNone(parsed.parse_error)
        self.assertEqual(parsed.frontmatter["verification"], "primary-source")
        self.assertEqual(parsed.frontmatter["sources"][0]["accessed"], "2026-08-19")

    def test_partial_coverage_stamps_accessed_but_not_verification(self):
        """Some sources read, some not: the entity is not primary-source yet.

        Throwing away the reading that *was* done would be as wrong as
        claiming the entity is verified. Six entities were in this state when
        the first content check landed on 2026-08-20."""
        rv.apply_verification(self.path, {"https://example.org/one"},
                              "2026-08-19", set_verification=False)
        out = self.path.read_text(encoding="utf-8")
        self.assertIn("verification: search-only", out,
                      "partial coverage must not claim primary-source")
        self.assertIn("last_verified: null", out,
                      "last_verified belongs to the whole entity, not one source")
        one, two = out.index("Pub One"), out.index("Pub Two")
        self.assertIn("accessed", out[one:two], "the read source must be stamped")
        self.assertNotIn("accessed", out[two:], "the unread source must not be")

    def test_writing_twice_does_not_duplicate_accessed(self):
        for _ in range(2):
            rv.apply_verification(self.path, {"https://example.org/one"}, "2026-08-19")
        self.assertEqual(self.path.read_text(encoding="utf-8").count("accessed:"), 1)


class TestTlsPolicy(unittest.TestCase):
    def test_certificate_verification_is_never_disabled(self):
        """The environment's TLS posture is information, not an obstacle.

        A tool that silently turned verification off would make every future
        `primary-source` claim in this repository worth less."""
        ctx = rv._ssl_context()
        self.assertTrue(ctx.check_hostname)
        import ssl
        self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)

    def test_an_unreadable_ca_bundle_does_not_break_the_context(self):
        """`Path.exists()` raises on a path inside an unreadable directory.

        The agent proxy's bundle lives under `/root/`, which is readable in the
        container this repository is normally worked in and **not** readable by
        the `runner` user in CI. The first version of this module called
        `.exists()` directly and died with PermissionError on GitHub Actions —
        a machine that simply does not have the file. Extra trust anchors are
        an optimisation for one environment; they must never be able to break
        the tool in another."""
        class Unreadable:
            def __fspath__(self):
                return "/root/.ccr/ca-bundle.crt"

        original = rv.CA_BUNDLE
        try:
            rv.CA_BUNDLE = Unreadable()
            # Both are patched so this test fails for *any* implementation
            # that does not guard the filesystem probe, not just the one
            # written today.
            with unittest.mock.patch.object(
                    rv.Path, "is_file", side_effect=PermissionError(13, "denied")), \
                 unittest.mock.patch.object(
                    rv.Path, "exists", side_effect=PermissionError(13, "denied")):
                ctx = rv._ssl_context()
        finally:
            rv.CA_BUNDLE = original

        import ssl
        self.assertTrue(ctx.check_hostname)
        self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)

    def test_readable_is_false_rather_than_raising(self):
        self.assertFalse(rv._readable(None))
        self.assertFalse(rv._readable("/nonexistent/path/to/nothing"))
        self.assertTrue(rv._readable(REPO_ROOT / "tools" / "reverify.py"))
        # a directory is not a usable CA bundle
        self.assertFalse(rv._readable(REPO_ROOT / "tools"))

    def test_source_has_no_verification_escape_hatch(self):
        """Checked against the syntax tree, not the text.

        A substring search would fire on this module's own prose about not
        disabling verification, which is how the first version of this test
        failed. What matters is whether the *code* does it."""
        import ast
        tree = ast.parse((REPO_ROOT / "tools" / "reverify.py").read_text(encoding="utf-8"))

        for node in ast.walk(tree):
            # ctx.verify_mode = ssl.CERT_NONE  /  ctx.check_hostname = False
            if isinstance(node, ast.Assign):
                names = {t.attr for t in node.targets if isinstance(t, ast.Attribute)}
                if "check_hostname" in names:
                    self.assertNotEqual(getattr(node.value, "value", True), False,
                                        "check_hostname must never be turned off")
                if "verify_mode" in names:
                    self.assertNotEqual(getattr(node.value, "attr", ""), "CERT_NONE",
                                        "verify mode must never be CERT_NONE")
            # ssl._create_unverified_context()
            if isinstance(node, ast.Call):
                fn = node.func
                name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", "")
                self.assertNotEqual(name, "_create_unverified_context",
                                    "unverified TLS context must never be created")
                for kw in node.keywords:
                    if kw.arg == "verify":
                        self.assertNotEqual(getattr(kw.value, "value", True), False,
                                            "verify=False must never be passed")


class TestRealRepository(unittest.TestCase):
    def test_every_entity_is_selectable_and_reviewable_offline(self):
        """The tool must cope with every shape of entity actually committed —
        including ones with no sources and ones with no checkable claims."""
        sys.path.insert(0, str(REPO_ROOT / "validation"))
        from common import load_all_entities
        entities = [e for e in load_all_entities() if e.frontmatter]
        self.assertGreater(len(entities), 100)
        for e in entities:
            rep = rv.review_entity(e, timeout=1, offline=True)
            self.assertIn(rep.verdict, (rv.NO_SOURCES, rv.UNREACHABLE))
            self.assertFalse(rep.writable,
                             f"{rep.entity_id}: offline must never be writable")

    def test_the_priority_seven_all_have_extractable_identifiers(self):
        """The Dutch register statutes are the batch flagged high-priority for
        re-verification, precisely because a wrong BWBR resolves to a real but
        unrelated act. If the tool cannot extract their identifiers it cannot
        do the one job they need."""
        sys.path.insert(0, str(REPO_ROOT / "validation"))
        from common import load_all_entities
        wanted = {"NL-WET-BAG", "NL-WET-BGT", "NL-WET-BRO", "NL-WET-WOZ",
                  "NL-HANDELSREGISTERWET", "NL-WEGENVERKEERSWET-1994",
                  "NL-KADASTERWET"}
        seen = set()
        for e in load_all_entities():
            if not e.frontmatter or e.frontmatter.get("id") not in wanted:
                continue
            seen.add(e.frontmatter["id"])
            claims = rv.checkable_claims(e.frontmatter)
            self.assertTrue(any(c.startswith("bwbr") for c in claims),
                            f"{e.frontmatter['id']}: no BWBR identifier extracted")
        self.assertEqual(seen, wanted, "a priority statute is missing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
