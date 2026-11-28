#!/usr/bin/env python3
"""Tests for tools/source_hosts.py, the generator of discovery/reverification-allowlist.md.

The entity loader is replaced by a small fake set, so the counts are known; one test also runs the
real repository through it. No network.

    python tools/test_source_hosts.py
"""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import source_hosts as sh  # noqa: E402


def entity(eid, urls, verification="primary-source"):
    return SimpleNamespace(frontmatter={
        "id": eid, "verification": verification,
        "sources": [{"title": "t", "url": u} for u in urls],
    })


FAKE = [
    entity("EU-ONE", ["https://eur-lex.europa.eu/a", "https://www.europa.eu/b"]),
    entity("GB-ONE", ["https://www.legislation.gov.uk/ukpga/1", "https://example.co.uk/x"]),
    entity("NL-ONE", ["https://data.overheid.nl/c"], verification="search-only"),
    entity("XX-ONE", ["not a url", "ftp://old.example.org/f"]),
    SimpleNamespace(frontmatter=None),                       # a file that failed to parse
    SimpleNamespace(frontmatter={"id": "XX-TWO", "sources": ["a bare string, not a mapping"]}),
]


class TestRegistrable(unittest.TestCase):
    def test_two_labels_for_an_ordinary_domain(self):
        self.assertEqual(sh.registrable("eur-lex.europa.eu"), "europa.eu")
        self.assertEqual(sh.registrable("www.boe.es"), "boe.es")

    def test_three_labels_under_a_second_level_suffix(self):
        self.assertEqual(sh.registrable("www.legislation.gov.uk"), "legislation.gov.uk")
        self.assertEqual(sh.registrable("ico.org.uk"), "ico.org.uk")
        self.assertEqual(sh.registrable("www.oaic.com.au"), "oaic.com.au")

    def test_case_and_www_are_ignored(self):
        self.assertEqual(sh.registrable("WWW.Overheid.NL"), "overheid.nl")

    def test_a_bare_suffix_or_single_label_is_returned_as_is(self):
        self.assertEqual(sh.registrable("gov.uk"), "gov.uk")
        self.assertEqual(sh.registrable("localhost"), "localhost")


class TestInstitutional(unittest.TestCase):
    def test_government_eu_and_standards_domains_count(self):
        for d in ("europa.eu", "legislation.gov.uk", "overheid.nl", "iso.org", "coe.int"):
            self.assertTrue(sh.is_institutional(d), d)

    def test_commentary_does_not(self):
        for d in ("wikipedia.org", "linklaters.com", "example.co.uk"):
            self.assertFalse(sh.is_institutional(d), d)


class TestCollect(unittest.TestCase):
    def setUp(self):
        with mock.patch.object(sh, "load_all_entities", return_value=FAKE):
            self.d = sh.collect()

    def test_counts_entities_and_unread_ones(self):
        self.assertEqual(self.d["entities"], len(FAKE))
        self.assertEqual(self.d["unread"], 1)

    def test_only_http_urls_are_counted(self):
        self.assertEqual(self.d["total_urls"], 5)
        self.assertNotIn("old.example.org", self.d["hosts"])

    def test_hosts_collapse_into_registrable_domains(self):
        self.assertEqual(self.d["domains"]["europa.eu"], 2)
        self.assertEqual(self.d["domain_hosts"]["europa.eu"], {"eur-lex.europa.eu", "www.europa.eu"})
        self.assertEqual(self.d["domain_entities"]["legislation.gov.uk"], {"GB-ONE"})


class TestMarkdown(unittest.TestCase):
    def setUp(self):
        with mock.patch.object(sh, "load_all_entities", return_value=FAKE):
            self.text = sh.render_markdown(sh.collect())

    def test_says_it_is_generated_and_how_to_regenerate(self):
        self.assertTrue(self.text.startswith("# Re-verification Allowlist\n"))
        self.assertIn("Generated file — do not hand-edit", self.text)
        self.assertIn("python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md", self.text)

    def test_headline_numbers(self):
        self.assertIn(f"**1 of the Atlas's {len(FAKE)} entities have never had a cited source read.**", self.text)
        self.assertIn("**5 source URLs** across **5 hosts**, collapsing to **4 registrable domains**", self.text)

    def test_table_marks_the_confirmed_domain_and_an_example_host(self):
        row = next(l for l in self.text.splitlines() if l.startswith("| `europa.eu`"))
        self.assertIn("`eur-lex.europa.eu`", row)          # the alphabetically first host
        self.assertIn("✅ 2026-08-21", row)
        gb = next(l for l in self.text.splitlines() if l.startswith("| `legislation.gov.uk`"))
        self.assertNotIn("2026-08-21", gb)

    def test_institutional_and_other_domains_are_listed_apart(self):
        inst = self.text.split("## Institutional domains", 1)[1].split("## Remaining domains", 1)[0]
        rest = self.text.split("## Remaining domains", 1)[1]
        self.assertIn("\noverheid.nl\n", inst)
        self.assertIn("\nexample.co.uk\n", rest)
        self.assertNotIn("example.co.uk", inst)


class TestMain(unittest.TestCase):
    def run_main(self, *args):
        buf = io.StringIO()
        with mock.patch.object(sh, "load_all_entities", return_value=FAKE), \
             mock.patch.object(sys, "argv", ["source_hosts.py", *args]), redirect_stdout(buf):
            self.assertEqual(sh.main(), 0)
        return buf.getvalue()

    def test_default_prints_hosts(self):
        self.assertEqual(self.run_main().split(), sorted(["eur-lex.europa.eu", "www.europa.eu",
                         "www.legislation.gov.uk", "example.co.uk", "data.overheid.nl"]))

    def test_domains_prints_registrable_domains(self):
        self.assertEqual(self.run_main("--domains").split(),
                         ["europa.eu", "example.co.uk", "legislation.gov.uk", "overheid.nl"])

    def test_out_writes_the_file_and_reports_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "sub" / "allow.md"
            said = self.run_main("--markdown", "-o", str(out))
            self.assertTrue(out.read_text(encoding="utf-8").startswith("# Re-verification Allowlist"))
            self.assertIn("1/6 entities unread; 5 URLs, 5 hosts, 4 domains", said)


class TestRealRepository(unittest.TestCase):
    def test_the_real_data_renders(self):
        text = sh.render_markdown(sh.collect())
        self.assertIn("## Institutional domains", text)
        self.assertIn("| `europa.eu`", text)


if __name__ == "__main__":
    unittest.main(verbosity=1)
