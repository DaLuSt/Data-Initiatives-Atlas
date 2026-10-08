#!/usr/bin/env python3
"""Tests for the validators themselves: each rule is shown to fire on a defect
and to stay quiet on a good entity. A tiny repository is built in a temporary
directory, so no real entity is touched.

    python validation/test_validators.py
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import common  # noqa: E402
import validate_frontmatter  # noqa: E402
import validate_ids  # noqa: E402
import validate_links  # noqa: E402
import validate_relationships  # noqa: E402
import validate_sources  # noqa: E402

VALIDATORS = (validate_ids, validate_frontmatter, validate_links, validate_relationships, validate_sources)

ORG = """---
id: XX-ORG
type: organisation
name: Example Organisation
description: >
  A test organisation.
level: national
country: XX
region: null
status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2020-01-01
end_date: null
last_verified: "2026-10-01"
previous_version: null
successor: null
domains: []
organisations: []
related_entities: []
relationships:
  - type: related-to
    target: XX-ACT
    source: fact
    evidence: "A test."
    confidence: medium
    valid_from: 2020-01-01
    valid_until: null
sources:
  - title: "A page"
    url: "https://example.org/a"
    publisher: "Example"
    accessed: "2026-10-01"
---

# Example Organisation
"""

ACT = """---
id: XX-ACT
type: act
name: Example Act
description: >
  A test act.
level: national
country: XX
region: null
status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-01"
previous_version: null
successor: null
domains: []
organisations: []
related_entities: []
relationships:
  - type: applies-in
    target: XX-ORG
    source: fact
    evidence: "A test."
    confidence: medium
    valid_from: null
    valid_until: null
sources:
  - title: "A page"
    url: "https://example.org/b"
    publisher: "Example"
    accessed: "2026-10-01"
---

# Example Act
"""


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for d in ("organisations", "legislation"):
            (self.root / d).mkdir()
        self.write("organisations/xx-org.md", ORG)
        self.write("legislation/xx-act.md", ACT)
        self._saved = common.REPO_ROOT
        common.REPO_ROOT = self.root

    def tearDown(self):
        common.REPO_ROOT = self._saved
        self._tmp.cleanup()

    def write(self, rel, text):
        (self.root / rel).write_text(text, encoding="utf-8")

    def edit(self, rel, old, new):
        text = (self.root / rel).read_text(encoding="utf-8")
        self.assertIn(old, text, old)
        self.write(rel, text.replace(old, new, 1))

    def run_all(self):
        """(exit code of the worst validator, all output)."""
        out = io.StringIO()
        worst = 0
        with contextlib.redirect_stdout(out):
            for v in VALIDATORS:
                worst = max(worst, v.main())
        return worst, out.getvalue()

    def assertFails(self, needle):
        code, text = self.run_all()
        self.assertEqual(code, 1, text)
        self.assertIn(needle, text)

    def assertOnlyWarns(self, needle):
        code, text = self.run_all()
        self.assertEqual(code, 0, text)
        self.assertIn("WARN", text)
        self.assertIn(needle, text)


class TestGoodRepository(Base):
    def test_a_good_pair_of_entities_passes_every_check(self):
        code, text = self.run_all()
        self.assertEqual(code, 0, text)
        self.assertNotIn("ERROR", text)
        self.assertNotIn("WARN", text)


class TestDates(Base):
    def test_an_impossible_date_is_reported_not_a_crash(self):
        self.edit("organisations/xx-org.md", "start_date: 2020-01-01", "start_date: 2020-13-45")
        self.assertFails("xx-org.md")  # named, and the run completed

    def test_end_before_start(self):
        self.edit("organisations/xx-org.md", "end_date: null", "end_date: 2019-01-01")
        self.assertFails("end_date 2019-01-01 is before start_date 2020-01-01")

    def test_a_partial_date_is_not_a_date(self):
        self.edit("organisations/xx-org.md", "end_date: null", 'end_date: "2025"')
        self.assertFails("end_date '2025' is not a YYYY-MM-DD date")

    def test_last_verified_in_the_future(self):
        self.edit("organisations/xx-org.md", 'last_verified: "2026-10-01"', 'last_verified: "2999-01-01"')
        self.assertFails("last_verified 2999-01-01 is in the future")

    def test_last_verified_that_is_not_a_date(self):
        self.edit("organisations/xx-org.md", 'last_verified: "2026-10-01"', 'last_verified: "recently"')
        self.assertFails("last_verified 'recently' is not a YYYY-MM-DD date")

    def test_today_and_tomorrow_are_allowed(self):
        import datetime
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        self.edit("organisations/xx-org.md", 'last_verified: "2026-10-01"', f'last_verified: "{tomorrow}"')
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_accessed_in_the_future(self):
        self.edit("organisations/xx-org.md", 'accessed: "2026-10-01"', 'accessed: "2999-01-01"')
        self.assertFails("accessed 2999-01-01 is in the future")

    def test_accessed_that_is_not_a_date(self):
        self.edit("organisations/xx-org.md", 'accessed: "2026-10-01"', 'accessed: "yesterday"')
        self.assertFails("accessed 'yesterday' is not a YYYY-MM-DD date")

    def test_a_relationship_that_ends_before_it_starts(self):
        self.edit("organisations/xx-org.md", "valid_until: null", "valid_until: 2010-01-01")
        self.assertFails("valid_until 2010-01-01 is before valid_from 2020-01-01")


class TestPrimarySourceBasis(Base):
    """`primary-source` has to be visible: an accessed date, or only confirmed domains."""

    def drop_dates(self, rel="organisations/xx-org.md"):
        import re as _re
        text = (self.root / rel).read_text(encoding="utf-8")
        self.write(rel, _re.sub(r'    accessed: .*\n', "", text))

    def test_no_accessed_date_on_an_unconfirmed_domain_fails(self):
        self.drop_dates()
        self.assertFails("verification is 'primary-source' but no source has an 'accessed' date")

    def test_one_accessed_date_is_enough(self):
        text = (self.root / "organisations/xx-org.md").read_text(encoding="utf-8")
        extra = '  - title: "B"\n    url: "https://example.net/b"\n    publisher: "Example"\n'
        self.write("organisations/xx-org.md", text.replace("---\n\n#", extra + "---\n\n#", 1))
        code, out = self.run_all()
        self.assertEqual(code, 0, out)

    def test_only_confirmed_domains_need_no_date(self):
        self.drop_dates()
        self.edit("organisations/xx-org.md", "https://example.org/a", "https://commission.europa.eu/x")
        code, out = self.run_all()
        self.assertEqual(code, 0, out)

    def test_one_unconfirmed_source_among_confirmed_ones_fails(self):
        self.drop_dates()
        text = (self.root / "organisations/xx-org.md").read_text(encoding="utf-8")
        self.write("organisations/xx-org.md", text.replace("https://example.org/a", "https://eur-lex.europa.eu/x").replace(
            "---\n\n#", '  - title: "B"\n    url: "https://example.net/b"\n    publisher: "Example"\n---\n\n#', 1))
        self.assertFails("verification is 'primary-source'")

    def test_a_lookalike_host_is_not_a_confirmed_domain(self):
        self.drop_dates()
        self.edit("organisations/xx-org.md", "https://example.org/a", "https://noteuropa.eu.example.org/x")
        self.assertFails("verification is 'primary-source'")
        self.edit("organisations/xx-org.md", "https://noteuropa.eu.example.org/x", "https://fakeeuropa.eu/x")
        self.assertFails("verification is 'primary-source'")

    def test_an_entity_with_no_sources_is_not_checked(self):
        text = (self.root / "organisations/xx-org.md").read_text(encoding="utf-8")
        i = text.index("sources:\n"); j = text.index("---\n\n#")
        self.write("organisations/xx-org.md", text[:i] + "sources: []\n" + text[j:])
        code, out = self.run_all()
        self.assertEqual(code, 0, out)

    def test_search_only_is_not_held_to_it(self):
        self.drop_dates()
        self.edit("organisations/xx-org.md", "verification: primary-source", "verification: search-only")
        self.edit("organisations/xx-org.md", 'last_verified: "2026-10-01"', "last_verified: null")
        code, out = self.run_all()
        self.assertEqual(code, 0, out)

    def test_the_confirmed_domains_match_the_documentation(self):
        doc = (Path(__file__).resolve().parent.parent / "docs" / "re-verification.md").read_text(encoding="utf-8")
        section = doc[doc.index("## The confirmed domains"):doc.index("### The rule it is applied under")]
        listed = set(__import__("re").findall(r"\| `([a-z.]+)` \|", section))
        self.assertEqual(listed, set(validate_sources.CONFIRMED_DOMAINS))


class TestSuccession(Base):
    """`successor` and `previous_version` are two ends of one statement."""

    def test_a_successor_that_does_not_name_it_back_warns(self):
        self.edit("organisations/xx-org.md", "successor: null", "successor: XX-ACT")
        self.assertOnlyWarns("successor is XX-ACT, but XX-ACT has previous_version 'None' instead of 'XX-ORG'")

    def test_a_previous_version_that_does_not_name_it_back_warns(self):
        self.edit("legislation/xx-act.md", "previous_version: null", "previous_version: XX-ORG")
        self.assertOnlyWarns("previous_version is XX-ORG, but XX-ORG has successor 'None' instead of 'XX-ACT'")

    def test_both_ends_written_is_quiet(self):
        self.edit("organisations/xx-org.md", "successor: null", "successor: XX-ACT")
        self.edit("legislation/xx-act.md", "previous_version: null", "previous_version: XX-ORG")
        code, text = self.run_all()
        self.assertEqual((code, "WARN" in text), (0, False), text)

    def test_two_predecessors_of_one_successor_are_not_reported(self):
        # A third entity; XX-ACT's single previous_version can name only one predecessor.
        self.write("organisations/xx-old.md", ORG.replace("XX-ORG", "XX-OLD").replace(
            "Example Organisation", "Old Organisation").replace("https://example.org/a", "https://example.org/c"))
        self.edit("organisations/xx-org.md", "successor: null", "successor: XX-ACT")
        self.edit("organisations/xx-old.md", "successor: null", "successor: XX-ACT")
        self.edit("legislation/xx-act.md", "previous_version: null", "previous_version: XX-ORG")
        code, text = self.run_all()
        self.assertNotIn("successor is XX-ACT", text)
        self.assertEqual(code, 0, text)

    def test_an_unknown_successor_is_left_to_the_generator(self):
        self.edit("organisations/xx-org.md", "successor: null", "successor: NOT-AN-ID")
        code, text = self.run_all()
        self.assertNotIn("successor is NOT-AN-ID", text)


class TestStructure(Base):
    def test_the_same_relationship_twice(self):
        text = (self.root / "organisations/xx-org.md").read_text(encoding="utf-8")
        block = text[text.index("  - type: related-to"):text.index("sources:")]
        self.write("organisations/xx-org.md", text.replace("sources:", block + "sources:", 1))
        self.assertFails("the same relationship (related-to -> XX-ACT) is already listed")

    def test_the_same_type_to_a_different_target_is_fine(self):
        text = (self.root / "organisations/xx-org.md").read_text(encoding="utf-8")
        block = text[text.index("  - type: related-to"):text.index("sources:")]
        self.write("organisations/xx-org.md", text.replace("sources:", block.replace("XX-ACT", "XX-ORG2") + "sources:", 1))
        # XX-ORG2 does not exist, so this fails for that reason, not as a duplicate
        code, out = self.run_all()
        self.assertEqual(code, 1)
        self.assertNotIn("is already listed", out)

    def test_national_level_needs_a_country(self):
        self.edit("legislation/xx-act.md", "country: XX", "country: null")
        self.assertFails("level 'national' needs a country")

    def test_a_non_national_level_may_have_no_country(self):
        self.edit("legislation/xx-act.md", "level: national", "level: international")
        self.edit("legislation/xx-act.md", "country: XX", "country: null")
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_superseded_without_a_successor_only_warns(self):
        self.edit("legislation/xx-act.md", "status: active", "status: superseded")
        self.assertOnlyWarns("'superseded' but 'successor' is not set")

    def test_superseded_with_a_successor_is_quiet(self):
        self.edit("legislation/xx-act.md", "status: active", "status: superseded")
        self.edit("legislation/xx-act.md", "successor: null", "successor: XX-ORG")
        self.edit("organisations/xx-org.md", "previous_version: null", "previous_version: XX-ACT")
        code, text = self.run_all()
        self.assertEqual((code, "WARN" in text), (0, False), text)

    def test_the_same_source_url_twice_only_warns(self):
        text = (self.root / "organisations/xx-org.md").read_text(encoding="utf-8")
        block = text[text.index('  - title: "A page"'):text.index("---\n\n#")]
        self.write("organisations/xx-org.md", text.replace("---\n\n#", block + "---\n\n#", 1))
        self.assertOnlyWarns("url already cited at sources[0]")


if __name__ == "__main__":
    unittest.main(verbosity=1)
