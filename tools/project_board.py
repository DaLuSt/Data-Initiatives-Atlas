#!/usr/bin/env python3
"""Keep the Atlas roadmap Project board in step with the `roadmap` issues.

Run by .github/workflows/project-board.yml, because Projects v2 can only be
changed through GitHub's GraphQL API and the agent's own environment blocks
that. The workflow runs on GitHub's side with a personal access token that can
edit the owner's projects (the `PROJECT_TOKEN` repository secret).

What one run does (all of it idempotent; a second run changes nothing):

* adds every issue labelled `roadmap` that is not on the board yet;
* sets its **Status**: *Done* when the issue is closed, *Backlog* when it is
  open and has no status yet. *Next* and *In Progress* are the owner's choices
  and are never overwritten for an open issue;
* gives it **Start date** and **Target date** from its milestone, which is what
  the board's Roadmap (timeline) layout draws bars from: the target is the
  milestone's due date, the start is the first day of that month. An issue with
  no milestone keeps whatever dates it has;
* creates the two date fields if the board does not have them yet.

It never removes an item from the board and never edits an issue.

    python tools/project_board.py --owner DaLuSt --number 1 \
        --repo DaLuSt/Data-Initiatives-Atlas [--dry-run]

Environment: PROJECT_TOKEN (edits the project) and GITHUB_TOKEN or GH_TOKEN
(reads the issues; optional for a public repository).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Callable

API = "https://api.github.com"
LABEL = "roadmap"
START_FIELD = "Start date"
TARGET_FIELD = "Target date"
STATUS_FIELD = "Status"
STATUS_DONE = "Done"
STATUS_NEW = "Backlog"


# --------------------------------------------------------------------------
# Pure functions: what should this item look like?


def milestone_dates(due_on: str | None) -> tuple[str, str] | None:
    """(start, target) as YYYY-MM-DD from a milestone's due date, or None.

    GitHub returns due_on as an ISO timestamp whose date part is the date the
    owner picked; the start is the first day of that month.
    """
    if not due_on:
        return None
    day = due_on[:10]
    if len(day) != 10 or day[4] != "-" or day[7] != "-":
        return None
    return day[:8] + "01", day


@dataclass
class Item:
    """One roadmap issue on the board, as currently recorded."""

    item_id: str
    status: str | None = None
    start: str | None = None
    target: str | None = None


@dataclass
class Issue:
    number: int
    node_id: str
    state: str  # "open" | "closed"
    due_on: str | None = None


@dataclass
class Plan:
    """The changes needed for one issue. Empty means nothing to do."""

    number: int
    add: bool = False
    status: str | None = None
    start: str | None = None
    target: str | None = None

    def is_empty(self) -> bool:
        return not (self.add or self.status or self.start or self.target)

    def describe(self) -> str:
        parts = []
        if self.add:
            parts.append("add to the board")
        if self.status:
            parts.append(f"Status -> {self.status}")
        if self.start:
            parts.append(f"{START_FIELD} -> {self.start}")
        if self.target:
            parts.append(f"{TARGET_FIELD} -> {self.target}")
        return f"#{self.number}: " + ", ".join(parts)


def plan_issue(issue: Issue, item: Item | None) -> Plan:
    plan = Plan(number=issue.number)
    current = item or Item(item_id="")
    plan.add = item is None
    if issue.state == "closed":
        if current.status != STATUS_DONE:
            plan.status = STATUS_DONE
    elif current.status is None:
        plan.status = STATUS_NEW
    dates = milestone_dates(issue.due_on)
    if dates:
        start, target = dates
        if current.start != start:
            plan.start = start
        if current.target != target:
            plan.target = target
    return plan


def plan_all(issues: list[Issue], items: dict[int, Item]) -> list[Plan]:
    plans = [plan_issue(i, items.get(i.number)) for i in sorted(issues, key=lambda i: i.number)]
    return [p for p in plans if not p.is_empty()]


# --------------------------------------------------------------------------
# GitHub access. `graphql` and `rest` are injected so tests never hit the network.


class GitHubError(RuntimeError):
    pass


def _request(url: str, token: str | None, body: dict | None = None) -> dict | list:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "atlas-project-board")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        detail = err.read().decode(errors="replace")[:500]
        raise GitHubError(f"HTTP {err.code} from {url}: {detail}") from None
    except urllib.error.URLError as err:
        raise GitHubError(f"could not reach {url}: {err.reason}") from None


def make_graphql(token: str) -> Callable[[str, dict], dict]:
    def graphql(query: str, variables: dict) -> dict:
        out = _request(f"{API}/graphql", token, {"query": query, "variables": variables})
        if not isinstance(out, dict):
            raise GitHubError("unexpected GraphQL response")
        if out.get("errors"):
            messages = "; ".join(e.get("message", "?") for e in out["errors"])
            raise GitHubError(f"GraphQL error: {messages}")
        return out["data"]

    return graphql


def fetch_issues(repo: str, token: str | None, rest: Callable[[str], list] | None = None) -> list[Issue]:
    """Every issue (not pull request) labelled `roadmap`, open and closed."""
    get = rest or (lambda url: _request(url, token))
    issues: list[Issue] = []
    page = 1
    while True:
        batch = get(f"{API}/repos/{repo}/issues?labels={LABEL}&state=all&per_page=100&page={page}")
        if not batch:
            break
        for raw in batch:
            if "pull_request" in raw:
                continue
            milestone = raw.get("milestone") or {}
            issues.append(
                Issue(
                    number=raw["number"],
                    node_id=raw["node_id"],
                    state=raw["state"],
                    due_on=milestone.get("due_on"),
                )
            )
        if len(batch) < 100:
            break
        page += 1
    return issues


PROJECT_QUERY = """
query($login: String!, $number: Int!) {
  user(login: $login) {
    projectV2(number: $number) {
      id
      title
      fields(first: 50) {
        nodes {
          __typename
          ... on ProjectV2Field { id name dataType }
          ... on ProjectV2SingleSelectField { id name dataType options { id name } }
          ... on ProjectV2IterationField { id name dataType }
        }
      }
    }
  }
}
"""

ITEMS_QUERY = """
query($project: ID!, $cursor: String) {
  node(id: $project) {
    ... on ProjectV2 {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          content {
            __typename
            ... on Issue { number repository { nameWithOwner } }
          }
          fieldValues(first: 30) {
            nodes {
              __typename
              ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
            }
          }
        }
      }
    }
  }
}
"""

ADD_ITEM = """
mutation($project: ID!, $content: ID!) {
  addProjectV2ItemById(input: {projectId: $project, contentId: $content}) { item { id } }
}
"""

SET_VALUE = """
mutation($project: ID!, $item: ID!, $field: ID!, $value: ProjectV2FieldValue!) {
  updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field, value: $value}) {
    projectV2Item { id }
  }
}
"""

CREATE_DATE_FIELD = """
mutation($project: ID!, $name: String!) {
  createProjectV2Field(input: {projectId: $project, dataType: DATE, name: $name}) {
    projectV2Field { ... on ProjectV2Field { id name dataType } }
  }
}
"""


@dataclass
class Project:
    project_id: str
    title: str
    fields: dict[str, dict] = field(default_factory=dict)  # name -> {id, dataType, options{name: id}}


def load_project(graphql: Callable, owner: str, number: int) -> Project:
    data = graphql(PROJECT_QUERY, {"login": owner, "number": number})
    node = (data.get("user") or {}).get("projectV2")
    if not node:
        raise GitHubError(f"project {number} of {owner} not found, or the token cannot see it")
    fields: dict[str, dict] = {}
    for f in node["fields"]["nodes"]:
        if not f or "name" not in f:
            continue
        fields[f["name"]] = {
            "id": f["id"],
            "dataType": f.get("dataType"),
            "options": {o["name"]: o["id"] for o in f.get("options", [])},
        }
    return Project(project_id=node["id"], title=node["title"], fields=fields)


def load_items(graphql: Callable, project_id: str, repo: str) -> dict[int, Item]:
    """Roadmap items on the board, keyed by issue number (this repository only)."""
    items: dict[int, Item] = {}
    cursor = None
    while True:
        data = graphql(ITEMS_QUERY, {"project": project_id, "cursor": cursor})
        page = data["node"]["items"]
        for node in page["nodes"]:
            content = node.get("content") or {}
            if content.get("__typename") != "Issue":
                continue
            if content["repository"]["nameWithOwner"].lower() != repo.lower():
                continue
            item = Item(item_id=node["id"])
            for value in node["fieldValues"]["nodes"]:
                if not value:
                    continue
                name = (value.get("field") or {}).get("name")
                if name == STATUS_FIELD and "name" in value:
                    item.status = value["name"]
                elif name == START_FIELD and "date" in value:
                    item.start = value["date"]
                elif name == TARGET_FIELD and "date" in value:
                    item.target = value["date"]
            items[content["number"]] = item
        if not page["pageInfo"]["hasNextPage"]:
            return items
        cursor = page["pageInfo"]["endCursor"]


def ensure_date_fields(graphql: Callable, project: Project, dry_run: bool, log: Callable[[str], None]) -> None:
    for name in (START_FIELD, TARGET_FIELD):
        existing = project.fields.get(name)
        if existing:
            if existing["dataType"] != "DATE":
                raise GitHubError(f"the board has a field '{name}' that is not a date field")
            continue
        log(f"creating the date field '{name}'")
        if dry_run:
            project.fields[name] = {"id": "(dry run)", "dataType": "DATE", "options": {}}
            continue
        data = graphql(CREATE_DATE_FIELD, {"project": project.project_id, "name": name})
        created = data["createProjectV2Field"]["projectV2Field"]
        project.fields[name] = {"id": created["id"], "dataType": "DATE", "options": {}}


def apply_plans(
    graphql: Callable,
    project: Project,
    issues: list[Issue],
    items: dict[int, Item],
    plans: list[Plan],
    dry_run: bool,
    log: Callable[[str], None],
) -> int:
    """Carry out the plans; return how many issues were changed."""
    by_number = {i.number: i for i in issues}
    status_field = project.fields.get(STATUS_FIELD)
    changed = 0
    for plan in plans:
        log(("would: " if dry_run else "") + plan.describe())
        if dry_run:
            changed += 1
            continue
        item_id = items[plan.number].item_id if plan.number in items else None
        if plan.add:
            data = graphql(ADD_ITEM, {"project": project.project_id, "content": by_number[plan.number].node_id})
            item_id = data["addProjectV2ItemById"]["item"]["id"]

        def set_value(field_name: str, value: dict) -> None:
            graphql(
                SET_VALUE,
                {"project": project.project_id, "item": item_id, "field": project.fields[field_name]["id"], "value": value},
            )

        if plan.status:
            option = (status_field or {}).get("options", {}).get(plan.status)
            if option:
                set_value(STATUS_FIELD, {"singleSelectOptionId": option})
            else:
                log(f"  the board has no Status option '{plan.status}'; status left as it is")
        if plan.start:
            set_value(START_FIELD, {"date": plan.start})
        if plan.target:
            set_value(TARGET_FIELD, {"date": plan.target})
        changed += 1
    return changed


def sync(
    graphql: Callable,
    rest: Callable[[str], list] | None,
    owner: str,
    number: int,
    repo: str,
    read_token: str | None,
    dry_run: bool,
    log: Callable[[str], None] = print,
) -> int:
    project = load_project(graphql, owner, number)
    log(f"board: {project.title}")
    issues = fetch_issues(repo, read_token, rest)
    log(f"{len(issues)} roadmap issues in {repo}")
    items = load_items(graphql, project.project_id, repo)
    ensure_date_fields(graphql, project, dry_run, log)
    plans = plan_all(issues, items)
    changed = apply_plans(graphql, project, issues, items, plans, dry_run, log)
    log(f"{changed} issue(s) {'would change' if dry_run else 'changed'}, {len(issues) - changed} already in step")
    return changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--owner", required=True, help="user that owns the project")
    ap.add_argument("--number", required=True, type=int, help="project number")
    ap.add_argument("--repo", required=True, help="owner/name whose roadmap issues are synced")
    ap.add_argument("--dry-run", action="store_true", help="print the changes, make none")
    args = ap.parse_args(argv)

    token = os.environ.get("PROJECT_TOKEN", "").strip()
    if not token:
        print("PROJECT_TOKEN is not set; nothing to do.")
        return 0
    read_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    try:
        sync(make_graphql(token), None, args.owner, args.number, args.repo, read_token, args.dry_run)
    except GitHubError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
