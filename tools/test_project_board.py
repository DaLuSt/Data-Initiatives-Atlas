#!/usr/bin/env python3
"""Tests for tools/project_board.py and its workflow.

Pure functions and an in-memory fake of GitHub's GraphQL API; no network.

    python tools/test_project_board.py
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import project_board as pb  # noqa: E402


class TestMilestoneDates(unittest.TestCase):
    def test_start_is_the_first_of_the_month_and_target_is_the_due_date(self):
        self.assertEqual(pb.milestone_dates("2027-02-28T00:00:00Z"), ("2027-02-01", "2027-02-28"))

    def test_leap_day(self):
        self.assertEqual(pb.milestone_dates("2028-02-29T00:00:00Z"), ("2028-02-01", "2028-02-29"))

    def test_no_milestone_gives_nothing(self):
        self.assertIsNone(pb.milestone_dates(None))
        self.assertIsNone(pb.milestone_dates(""))

    def test_garbage_gives_nothing(self):
        self.assertIsNone(pb.milestone_dates("soon"))


class TestPlanIssue(unittest.TestCase):
    def issue(self, state="open", due="2027-01-31T00:00:00Z", number=470):
        return pb.Issue(number=number, node_id=f"I_{number}", state=state, due_on=due)

    def test_new_open_issue_is_added_as_backlog_with_dates(self):
        plan = pb.plan_issue(self.issue(), None)
        self.assertTrue(plan.add)
        self.assertEqual(plan.status, "Backlog")
        self.assertEqual((plan.start, plan.target), ("2027-01-01", "2027-01-31"))

    def test_new_closed_issue_is_added_as_done(self):
        plan = pb.plan_issue(self.issue(state="closed"), None)
        self.assertEqual(plan.status, "Done")

    def test_an_item_already_in_step_needs_nothing(self):
        item = pb.Item("PVTI_1", status="Next", start="2027-01-01", target="2027-01-31")
        self.assertTrue(pb.plan_issue(self.issue(), item).is_empty())

    def test_next_and_in_progress_are_never_overwritten_for_an_open_issue(self):
        for status in ("Next", "In Progress", "Backlog"):
            item = pb.Item("PVTI_1", status=status, start="2027-01-01", target="2027-01-31")
            self.assertIsNone(pb.plan_issue(self.issue(), item).status)

    def test_a_closed_issue_moves_to_done_from_any_status(self):
        for status in ("Backlog", "Next", "In Progress", None):
            item = pb.Item("PVTI_1", status=status, start="2027-01-01", target="2027-01-31")
            self.assertEqual(pb.plan_issue(self.issue(state="closed"), item).status, "Done")

    def test_a_done_closed_issue_is_left_alone(self):
        item = pb.Item("PVTI_1", status="Done", start="2027-01-01", target="2027-01-31")
        self.assertTrue(pb.plan_issue(self.issue(state="closed"), item).is_empty())

    def test_a_moved_milestone_updates_both_dates(self):
        item = pb.Item("PVTI_1", status="Next", start="2027-01-01", target="2027-01-31")
        plan = pb.plan_issue(self.issue(due="2027-03-31T00:00:00Z"), item)
        self.assertEqual((plan.start, plan.target), ("2027-03-01", "2027-03-31"))
        self.assertFalse(plan.add)

    def test_no_milestone_keeps_the_existing_dates(self):
        item = pb.Item("PVTI_1", status="Next", start="2027-01-01", target="2027-01-31")
        self.assertTrue(pb.plan_issue(self.issue(due=None), item).is_empty())

    def test_a_reopened_issue_with_status_done_is_not_moved_back(self):
        # The owner decides where a reopened issue goes; the sync only fills gaps.
        item = pb.Item("PVTI_1", status="Done", start="2027-01-01", target="2027-01-31")
        self.assertTrue(pb.plan_issue(self.issue(state="open"), item).is_empty())

    def test_plan_all_skips_issues_in_step_and_sorts(self):
        issues = [self.issue(number=3), self.issue(number=1)]
        items = {3: pb.Item("a", status="Backlog", start="2027-01-01", target="2027-01-31")}
        plans = pb.plan_all(issues, items)
        self.assertEqual([p.number for p in plans], [1])


class FakeGitHub:
    """Just enough of the GraphQL API for project_board.sync."""

    def __init__(self, items=None, with_date_fields=True):
        self.project_id = "PVT_1"
        self.fields = {
            "Status": {"id": "F_status", "dataType": "SINGLE_SELECT",
                       "options": {"Backlog": "O_b", "Next": "O_n", "In Progress": "O_p", "Done": "O_d"}},
            "Title": {"id": "F_title", "dataType": "TITLE", "options": {}},
        }
        if with_date_fields:
            self.fields["Start date"] = {"id": "F_start", "dataType": "DATE", "options": {}}
            self.fields["Target date"] = {"id": "F_target", "dataType": "DATE", "options": {}}
        # issue number -> {"id", "status", "start", "target"}
        self.items = items or {}
        self.calls = []

    def graphql(self, query, variables):
        self.calls.append((query.strip().split("(")[0].split()[-1], variables))
        if "projectV2(number" in query:
            nodes = []
            for name, f in self.fields.items():
                node = {"__typename": "ProjectV2Field", "id": f["id"], "name": name, "dataType": f["dataType"]}
                if f["options"]:
                    node["options"] = [{"id": i, "name": n} for n, i in f["options"].items()]
                nodes.append(node)
            return {"user": {"projectV2": {"id": self.project_id, "title": "Atlas roadmap", "fields": {"nodes": nodes}}}}
        if "items(first" in query:
            nodes = []
            for number, it in self.items.items():
                values = []
                if it.get("status"):
                    values.append({"__typename": "ProjectV2ItemFieldSingleSelectValue", "name": it["status"], "field": {"name": "Status"}})
                if it.get("start"):
                    values.append({"__typename": "ProjectV2ItemFieldDateValue", "date": it["start"], "field": {"name": "Start date"}})
                if it.get("target"):
                    values.append({"__typename": "ProjectV2ItemFieldDateValue", "date": it["target"], "field": {"name": "Target date"}})
                nodes.append({
                    "id": it["id"],
                    "content": {"__typename": "Issue", "number": number, "repository": {"nameWithOwner": "DaLuSt/Data-Initiatives-Atlas"}},
                    "fieldValues": {"nodes": values},
                })
            # a draft issue and an issue from another repository, which must be ignored
            nodes.append({"id": "draft", "content": {"__typename": "DraftIssue"}, "fieldValues": {"nodes": []}})
            nodes.append({"id": "other", "content": {"__typename": "Issue", "number": 5, "repository": {"nameWithOwner": "x/y"}}, "fieldValues": {"nodes": []}})
            return {"node": {"items": {"pageInfo": {"hasNextPage": False, "endCursor": None}, "nodes": nodes}}}
        if "addProjectV2ItemById" in query:
            number = int(variables["content"].split("_")[1])
            self.items[number] = {"id": f"PVTI_{number}"}
            return {"addProjectV2ItemById": {"item": {"id": f"PVTI_{number}"}}}
        if "createProjectV2Field" in query:
            name = variables["name"]
            self.fields[name] = {"id": f"F_{name}", "dataType": "DATE", "options": {}}
            return {"createProjectV2Field": {"projectV2Field": {"id": f"F_{name}", "name": name, "dataType": "DATE"}}}
        if "updateProjectV2ItemFieldValue" in query:
            number = int(variables["item"].split("_")[1])
            fid, value = variables["field"], variables["value"]
            it = self.items[number]
            if fid == "F_status":
                it["status"] = next(n for n, i in self.fields["Status"]["options"].items() if i == value["singleSelectOptionId"])
            elif fid in ("F_start", "F_Start date"):
                it["start"] = value["date"]
            else:
                it["target"] = value["date"]
            return {"updateProjectV2ItemFieldValue": {"projectV2Item": {"id": variables["item"]}}}
        raise AssertionError("unexpected query: " + query[:60])


def rest_pages(*issues):
    """A fake REST listing: one page, plus a pull request that must be skipped."""
    raw = [
        {"number": n, "node_id": f"I_{n}", "state": s, "milestone": ({"due_on": d} if d else None)}
        for n, s, d in issues
    ]
    raw.append({"number": 999, "node_id": "PR_999", "state": "open", "milestone": None, "pull_request": {}})
    pages = {1: raw}
    return lambda url: pages.get(int(re.search(r"[&?]page=(\d+)", url).group(1)), [])


def run_sync(gh, rest, dry_run=False):
    log = []
    changed = pb.sync(gh.graphql, rest, "DaLuSt", 1, "DaLuSt/Data-Initiatives-Atlas", None, dry_run, log.append)
    return changed, log


class TestSync(unittest.TestCase):
    ISSUES = [(470, "open", "2027-01-31T00:00:00Z"), (471, "open", "2027-02-28T00:00:00Z"), (444, "closed", "2026-10-31T00:00:00Z")]

    def test_empty_board_gets_every_roadmap_issue_with_status_and_dates(self):
        gh = FakeGitHub()
        changed, _ = run_sync(gh, rest_pages(*self.ISSUES))
        self.assertEqual(changed, 3)
        self.assertEqual(gh.items[470], {"id": "PVTI_470", "status": "Backlog", "start": "2027-01-01", "target": "2027-01-31"})
        self.assertEqual(gh.items[444]["status"], "Done")
        self.assertNotIn(999, gh.items)  # a pull request is not a roadmap item

    def test_second_run_changes_nothing(self):
        gh = FakeGitHub()
        run_sync(gh, rest_pages(*self.ISSUES))
        before = len(gh.calls)
        changed, _ = run_sync(gh, rest_pages(*self.ISSUES))
        self.assertEqual(changed, 0)
        mutations = [c for c in gh.calls[before:] if c[0] in ("addProjectV2ItemById", "updateProjectV2ItemFieldValue", "createProjectV2Field")]
        self.assertEqual(mutations, [])

    def test_dry_run_makes_no_mutation(self):
        gh = FakeGitHub(with_date_fields=False)
        changed, log = run_sync(gh, rest_pages(*self.ISSUES), dry_run=True)
        self.assertEqual(changed, 3)
        self.assertEqual(gh.items, {})
        self.assertNotIn("Start date", gh.fields)
        self.assertTrue(any(line.startswith("would: ") for line in log))

    def test_missing_date_fields_are_created(self):
        gh = FakeGitHub(with_date_fields=False)
        run_sync(gh, rest_pages(*self.ISSUES))
        self.assertIn("Start date", gh.fields)
        self.assertIn("Target date", gh.fields)
        self.assertEqual(gh.items[471]["target"], "2027-02-28")

    def test_the_owners_status_choices_survive(self):
        gh = FakeGitHub(items={470: {"id": "PVTI_470", "status": "In Progress", "start": "2027-01-01", "target": "2027-01-31"}})
        run_sync(gh, rest_pages(*self.ISSUES))
        self.assertEqual(gh.items[470]["status"], "In Progress")

    def test_a_missing_status_option_is_reported_not_fatal(self):
        gh = FakeGitHub()
        del gh.fields["Status"]["options"]["Backlog"]
        changed, log = run_sync(gh, rest_pages((470, "open", "2027-01-31T00:00:00Z")))
        self.assertEqual(changed, 1)
        self.assertTrue(any("no Status option" in line for line in log))
        self.assertEqual(gh.items[470]["target"], "2027-01-31")

    def test_a_non_date_field_with_the_same_name_is_an_error(self):
        gh = FakeGitHub()
        gh.fields["Start date"]["dataType"] = "TEXT"
        with self.assertRaises(pb.GitHubError):
            run_sync(gh, rest_pages(*self.ISSUES))

    def test_unknown_project_is_an_error(self):
        def graphql(query, variables):
            return {"user": {"projectV2": None}}
        with self.assertRaises(pb.GitHubError):
            pb.load_project(graphql, "DaLuSt", 99)


class TestLoadItems(unittest.TestCase):
    def test_only_issues_of_this_repository_are_loaded(self):
        gh = FakeGitHub(items={470: {"id": "PVTI_470", "status": "Next"}})
        items = pb.load_items(gh.graphql, "PVT_1", "dalust/data-initiatives-atlas")
        self.assertEqual(sorted(items), [470])  # not the draft, not x/y#5
        self.assertEqual(items[470].status, "Next")


class TestMain(unittest.TestCase):
    def test_without_a_token_it_does_nothing_and_succeeds(self):
        env = {k: v for k, v in os.environ.items() if k != "PROJECT_TOKEN"}
        done = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools" / "project_board.py"), "--owner", "o", "--number", "1", "--repo", "o/r"],
            capture_output=True, text=True, env=env,
        )
        self.assertEqual(done.returncode, 0)
        self.assertIn("PROJECT_TOKEN is not set", done.stdout)


class TestWorkflow(unittest.TestCase):
    def setUp(self):
        self.text = (REPO_ROOT / ".github" / "workflows" / "project-board.yml").read_text(encoding="utf-8")

    def test_the_token_is_only_read_from_the_secret(self):
        self.assertIn("${{ secrets.PROJECT_TOKEN }}", self.text)

    def test_no_issue_text_is_interpolated_into_a_shell_command(self):
        # github.event.issue.title / body in a run: step would be script injection.
        self.assertNotRegex(self.text, r"github\.event\.(issue|comment)\.(title|body)")

    def test_it_reacts_to_the_events_that_move_an_item(self):
        for event in ("issues:", "workflow_dispatch:", "schedule:"):
            self.assertIn(event, self.text)
        for kind in ("opened", "labeled", "milestoned", "closed", "reopened"):
            self.assertIn(kind, self.text)

    def test_it_cannot_write_to_the_repository(self):
        self.assertRegex(self.text, r"contents:\s*read")
        self.assertNotRegex(self.text, r"contents:\s*write")

    def test_runs_are_serialised(self):
        self.assertIn("concurrency:", self.text)


if __name__ == "__main__":
    unittest.main()
