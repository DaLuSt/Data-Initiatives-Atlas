#!/usr/bin/env python3
"""Tests for tools/update_counts.py (the headline numbers in README.md and .agent/state.yaml).

    python tools/test_update_counts.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import update_counts as uc  # noqa: E402

N = uc.numbers(
    {"entities": 801, "edges_total": 10002, "relationships": 1700, "associations": 3500, "wikilinks": 4802,
     "countries": 64, "regions": 1},
    countries_with_entities=30, unresolved_rows=55)

README = """*Search, filter and explore 774 entities and 9,644 connections across sixty-three
countries — no install, no account.*

| **Entities** | 774 |
| **Connections** | 9,644 — of which **1,618** are typed relationships, each with its provenance |
| **Country scopes** | **63** — 28 with national entities beyond the anchor itself, the rest base anchors |
| **✅ Sourcing** | **All 774 entities are `verification: primary-source`** — every cited source |

*Figures as of 2026-10-08. The live counts are always on the site itself.*

the primary source. **All 774 entities have moved past this stage**, after
"""

STATE = """updated: "2026-10-09"
graph:
  entity_count: 774
  relationship_edges: 1618
  association_edges: 3407
  wikilink_edges: 4619
  edges_total: 9644
  countries: 63
  regions: 1

discovery:
  unresolved_rows_open: 62
"""


class TestWords(unittest.TestCase):
    def test_the_numbers_the_readme_writes_out(self):
        self.assertEqual(uc.words(58), "fifty-eight")
        self.assertEqual(uc.words(63), "sixty-three")
        self.assertEqual(uc.words(70), "seventy")
        self.assertEqual(uc.words(100), "one hundred")
        self.assertEqual(uc.words(120), "one hundred and twenty")
        self.assertEqual(uc.words(7), "seven")

    def test_out_of_range_is_an_error_not_a_guess(self):
        with self.assertRaises(ValueError):
            uc.words(200)

    def test_open_questions_counts_table_rows_only(self):
        text = "| # | Area |\n|---|---|\n| 1 | a |\n| 22 | b |\nnot | 3 | a row\n"
        self.assertEqual(uc.open_questions(text), 2)


class TestPatchReadme(unittest.TestCase):
    def test_every_number_is_rewritten(self):
        out = uc.patch_readme(README, N, "2026-11-01")
        self.assertIn("801 entities and 10,002 connections across sixty-four\ncountries", out)
        self.assertIn("| **Entities** | 801 |", out)
        self.assertIn("| **Connections** | 10,002 — of which **1,700** are typed", out)
        self.assertIn("**64** — 30 with national entities", out)
        self.assertIn("**All 801 entities are `verification: primary-source`**", out)
        self.assertIn("**All 801 entities have moved past this stage**", out)
        self.assertIn("*Figures as of 2026-11-01.", out)
        self.assertNotIn("774", out)

    def test_nothing_else_changes(self):
        out = uc.patch_readme(README, N, None)
        self.assertIn("*Figures as of 2026-10-08.", out)
        self.assertEqual(out.count("\n"), README.count("\n"))

    def test_a_missing_pattern_is_an_error(self):
        with self.assertRaises(SystemExit):
            uc.patch_readme("nothing to see here\n", N, None)

    def test_the_same_numbers_change_nothing(self):
        once = uc.patch_readme(README, N, None)
        self.assertEqual(uc.patch_readme(once, N, None), once)


class TestPatchState(unittest.TestCase):
    def test_every_field_is_rewritten(self):
        out = uc.patch_state(STATE, N, "2026-11-01")
        for line in ("entity_count: 801", "relationship_edges: 1700", "association_edges: 3500",
                     "wikilink_edges: 4802", "edges_total: 10002", "countries: 64", "regions: 1",
                     "unresolved_rows_open: 55", 'updated: "2026-11-01"'):
            self.assertIn(line, out)

    def test_the_date_is_left_alone_without_one(self):
        self.assertIn('updated: "2026-10-09"', uc.patch_state(STATE, N, None))

    def test_a_field_that_is_missing_is_an_error(self):
        with self.assertRaises(SystemExit):
            uc.patch_state(STATE.replace("regions: 1\n", ""), N, None)


class TestTheRepositoryIsInStep(unittest.TestCase):
    def test_readme_and_state_match_the_data(self):
        self.assertEqual(uc.main(["--check"]), 0,
                         "run: python tools/update_counts.py")

    def test_the_check_is_in_the_shared_checks(self):
        action = (REPO_ROOT / ".github" / "actions" / "checks" / "action.yml").read_text(encoding="utf-8")
        self.assertIn("python tools/update_counts.py --check", action)
        self.assertIn("python tools/test_update_counts.py", action)


if __name__ == "__main__":
    unittest.main()
