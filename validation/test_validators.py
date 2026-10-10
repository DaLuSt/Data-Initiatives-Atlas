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


COUNTRY = """---
id: XX
type: country
name: Examplia
description: >
  A test country anchor.
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
  - type: related-to
    target: XX-ORG
    source: fact
    evidence: "A test."
    confidence: medium
    valid_from: null
    valid_until: null
sources:
  - title: "A page"
    url: "https://example.org/country"
    publisher: "Example"
    accessed: "2026-10-01"
---

# Examplia
"""


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        for d in ("organisations", "legislation", "countries/xx"):
            (self.root / d).mkdir(parents=True)
        self.write("countries/xx/xx.md", COUNTRY)
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

    def test_an_unknown_successor_is_an_error(self):
        self.edit("organisations/xx-org.md", "successor: null", "successor: NOT-AN-ID")
        self.assertFails("organisations/xx-org.md: successor 'NOT-AN-ID' does not resolve to a known entity")

    def test_an_unknown_previous_version_is_an_error(self):
        self.edit("legislation/xx-act.md", "previous_version: null", "previous_version: NOT-AN-ID")
        self.assertFails("legislation/xx-act.md: previous_version 'NOT-AN-ID' does not resolve to a known entity")

    def test_the_unknown_successor_is_not_also_reported_as_a_one_sided_pair(self):
        self.edit("organisations/xx-org.md", "successor: null", "successor: NOT-AN-ID")
        _, text = self.run_all()
        self.assertNotIn("successor is NOT-AN-ID, but", text)

    def test_the_wording_matches_the_generators(self):
        # tools/build_graph.py says "<field> '<id>' does not resolve to a known entity".
        gen = (Path(__file__).resolve().parent.parent / "tools" / "build_graph.py").read_text(encoding="utf-8")
        self.assertIn("does not resolve to a known", gen)
        self.assertIn("does not resolve to a known entity", (Path(__file__).resolve().parent / "validate_relationships.py").read_text(encoding="utf-8"))


class TestCountryAnchor(Base):
    """An entity's `country` must be a country the Atlas has an anchor for."""

    def test_a_country_without_an_anchor_is_an_error(self):
        self.edit("organisations/xx-org.md", "country: XX", "country: ZZ")
        self.assertFails("organisations/xx-org.md: country 'ZZ' has no country anchor in the Atlas")

    def test_the_message_says_what_to_add(self):
        self.edit("organisations/xx-org.md", "country: XX", "country: ZZ")
        _, text = self.run_all()
        self.assertIn("countries/zz/", text)

    def test_a_country_with_an_anchor_passes(self):
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_no_country_is_fine(self):
        self.edit("organisations/xx-org.md", "country: XX", "country: null")
        self.edit("organisations/xx-org.md", "level: national", "level: international")
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_a_malformed_code_still_gets_its_own_message(self):
        self.edit("organisations/xx-org.md", "country: XX", "country: xyz")
        self.assertFails("is not a plausible ISO 3166-1 alpha-2 code")

    def test_removing_the_anchor_breaks_every_entity_that_uses_it(self):
        (self.root / "countries/xx/xx.md").unlink()
        code, text = self.run_all()
        self.assertEqual(code, 1, text)
        self.assertEqual(text.count("has no country anchor"), 2)  # the organisation and the act

    def test_a_region_is_not_a_country_anchor(self):
        self.write("countries/xx/xx.md", COUNTRY.replace("type: country", "type: region"))
        self.assertFails("has no country anchor")


class TestDomains(Base):
    """A domain on an entity must be a domain entity the Atlas holds (roadmap #461).

    Otherwise the site's domain filter shows a row labelled with the bare ID.
    """

    def test_an_unknown_domain_is_an_error(self):
        self.edit("organisations/xx-org.md", "domains: []", "domains:\n  - DOMAIN-NOWHERE")
        self.assertFails("domains references unknown id 'DOMAIN-NOWHERE'")

    def test_no_domain_is_fine(self):
        code, text = self.run_all()
        self.assertEqual(code, 0, text)


class TestStaleRowReferences(Base):
    """A file that calls a row of discovery/unresolved.md open must name a row the table still has."""

    UNRESOLVED = ("| # | A | T | Q | D | S | N |\n|---|---|---|---|---|---|---|\n"
                  "| 5 | Spain | x | q | d | Open | 2026-10-10 |\n| 9 | Poland | x | q | d | Open | 2026-10-10 |\n")

    def setUp(self):
        super().setUp()
        (self.root / "discovery").mkdir()
        self.write("discovery/unresolved.md", self.UNRESOLVED)

    def body(self, sentence):
        path = self.root / "legislation" / "xx-act.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n" + sentence + "\n", encoding="utf-8")

    def test_an_open_row_that_is_gone_is_a_warning(self):
        self.body("The question stays open in row #32 of the table.")
        self.assertOnlyWarns("calls row #32 of discovery/unresolved.md open")

    def test_a_row_that_still_exists_is_quiet(self):
        self.body("The question stays open in row #5 of the table.")
        code, text = self.run_all()
        self.assertEqual(code, 0, text)
        self.assertNotIn("calls row", text)

    def test_a_closed_row_may_be_cited_after_it_is_gone(self):
        self.body("This closes row #32, which is gone from the table.")
        code, text = self.run_all()
        self.assertNotIn("calls row", text)

    def test_a_row_cited_without_saying_it_is_open_is_quiet(self):
        self.body("See row #32 for the history.")
        code, text = self.run_all()
        self.assertNotIn("calls row", text)

    def test_without_the_table_nothing_is_checked(self):
        (self.root / "discovery" / "unresolved.md").unlink()
        self.body("The question stays open in row #32 of the table.")
        code, text = self.run_all()
        self.assertNotIn("calls row", text)

    def test_every_number_of_a_list_is_checked(self):
        self.body("Rows #5 and #77 are still open.")
        self.assertOnlyWarns("calls row #77")


class TestUnresolvedTable(Base):
    """The master table of discovery/unresolved.md: seven cells a row, working detail links, no long unlinked cell."""

    HEAD = "| # | Area | Topic | Question | Detail | Status | Noted |\n|---|---|---|---|---|---|---|\n"

    def setUp(self):
        super().setUp()
        (self.root / "discovery" / "unresolved").mkdir(parents=True)

    def table(self, *rows):
        self.write("discovery/unresolved.md", self.HEAD + "\n".join(rows) + "\n")

    def test_a_good_table_is_quiet(self):
        self.table("| 1 | Spain | x | q | short | Open | 2026-10-10 |")
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_a_row_with_the_wrong_number_of_cells_is_an_error(self):
        self.table("| 1 | Spain | x | q | has a stray | pipe | Open | 2026-10-10 |")
        self.assertFails("row #1 has 8 cells, not 7")

    def test_an_escaped_pipe_is_not_a_cell_break(self):
        self.table("| 1 | Spain | x | q | a title \\| with a pipe | Open | 2026-10-10 |")
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_a_detail_link_to_a_missing_section_is_an_error(self):
        self.table("| 1 | Spain | x | q | excerpt … [full detail](unresolved/spain.md#row-1) | Open | 2026-10-10 |")
        self.assertFails("points at a section that does not exist")

    def test_a_detail_link_to_an_existing_section_is_quiet(self):
        self.write("discovery/unresolved/spain.md", '# Spain\n\n<a id="row-1"></a>\n## Row 1\n\ntext\n')
        self.table("| 1 | Spain | x | q | excerpt … [full detail](unresolved/spain.md#row-1) | Open | 2026-10-10 |")
        code, text = self.run_all()
        self.assertEqual(code, 0, text)

    def test_a_link_to_another_rows_section_is_an_error(self):
        self.write("discovery/unresolved/spain.md", '<a id="row-2"></a>\n## Row 2\n')
        self.table("| 1 | Spain | x | q | excerpt … [full detail](unresolved/spain.md#row-2) | Open | 2026-10-10 |")
        self.assertFails("points at a section that does not exist")

    def test_a_long_cell_with_no_link_is_a_warning(self):
        self.table("| 1 | Spain | x | q | " + "long " * 200 + " | Open | 2026-10-10 |")
        self.assertOnlyWarns("the detail cell is")


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
