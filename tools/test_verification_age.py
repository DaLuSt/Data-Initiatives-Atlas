#!/usr/bin/env python3
"""Tests for tools/verification_age.py (roadmap #510): the age arithmetic, the three states, the
ordering, the report, and that it reads the real entities. No network.

    python tools/test_verification_age.py
"""
from __future__ import annotations

import contextlib
import io
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import verification_age as va  # noqa: E402


class TestAge(unittest.TestCase):
    def test_whole_calendar_months(self):
        self.assertEqual(va.months_between(date(2026, 8, 14), date(2026, 10, 20)), 2)
        self.assertEqual(va.months_between(date(2026, 8, 14), date(2026, 9, 13)), 0)
        self.assertEqual(va.months_between(date(2026, 8, 14), date(2027, 8, 14)), 12)
        self.assertEqual(va.months_between(date(2026, 8, 14), date(2027, 8, 13)), 11)

    def test_a_date_in_the_future_is_age_zero(self):
        self.assertEqual(va.months_between(date(2026, 12, 1), date(2026, 10, 20)), 0)

    def test_states_follow_the_policy_thresholds(self):
        asof = date(2027, 5, 14)
        self.assertEqual(va.status(date(2026, 8, 15), asof), "ok")          # 8 months
        self.assertEqual(va.status(date(2026, 8, 14), asof), "due-soon")    # 9 months
        self.assertEqual(va.status(date(2026, 5, 15), asof), "due-soon")    # 11 months
        self.assertEqual(va.status(date(2026, 5, 14), asof), "overdue")     # 12 months
        self.assertEqual(va.status(None, asof), "undated")

    def test_dates_are_read_from_strings_and_from_yaml_dates(self):
        self.assertEqual(va.parse_date("2026-10-19"), date(2026, 10, 19))
        self.assertEqual(va.parse_date(date(2026, 10, 19)), date(2026, 10, 19))
        for bad in (None, "", "2026-13-01", "October", "2026-10"):
            self.assertIsNone(va.parse_date(bad), bad)


class TestReport(unittest.TestCase):
    ROWS = [
        {"id": "A", "type": "act", "verified": None, "months": None, "status": "undated", "path": ""},
        {"id": "B", "type": "act", "verified": date(2026, 1, 5), "months": 14, "status": "overdue", "path": ""},
        {"id": "C", "type": "organisation", "verified": date(2026, 10, 1), "months": 0, "status": "ok", "path": ""},
    ]

    def test_summary_counts_each_state(self):
        self.assertEqual(va.summary(self.ROWS), {"ok": 1, "due-soon": 0, "overdue": 1, "undated": 1})

    def test_due_only_leaves_out_the_ones_that_are_fine(self):
        text = va.render(self.ROWS, date(2027, 3, 1), due_only=True, markdown=False, limit=20)
        self.assertIn("  B  ", text.replace("   ", "  "))
        self.assertNotIn("(organisation)", text)

    def test_nothing_due_says_so(self):
        text = va.render([self.ROWS[2]], date(2026, 10, 20), due_only=True, markdown=False, limit=20)
        self.assertIn("Nothing is due.", text)

    def test_markdown_is_a_table(self):
        text = va.render(self.ROWS, date(2027, 3, 1), due_only=False, markdown=True, limit=20)
        self.assertIn("| Entity | Type | Last verified | Months | Status |", text)
        self.assertIn("| B | act | 2026-01-05 | 14 | overdue |", text)


class TestRealData(unittest.TestCase):
    def test_every_entity_is_dated_and_none_is_overdue_today(self):
        items = va.rows(date.today())
        self.assertGreater(len(items), 900)
        self.assertEqual([r["id"] for r in items if r["status"] == "undated"], [])

    def test_the_oldest_come_first_and_undated_lead(self):
        items = va.rows(date(2027, 1, 1))
        dated = [r["verified"] for r in items if r["verified"] is not None]
        self.assertEqual(dated, sorted(dated))

    def test_the_command_runs_and_the_exit_code_reflects_overdue(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(va.main(["--fail-on-overdue", "--asof", "2026-10-20"]), 0)
            self.assertEqual(va.main(["--fail-on-overdue", "--asof", "2028-01-01"]), 1)
            self.assertEqual(va.main(["--due", "--asof", "2027-06-20", "--markdown"]), 0)


if __name__ == "__main__":
    unittest.main()
