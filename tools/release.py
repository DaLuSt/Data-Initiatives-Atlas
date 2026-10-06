#!/usr/bin/env python3
"""Release tooling: two version tracks, one changelog.

The Atlas has two version numbers (`metadata/versioning.md` has the policy):

* a **schema version** (SemVer) in `metadata/schema.json`, changed by the pull
  request that changes the data model; and
* a **data release** (`YYYY.MM.N`, N counting the releases made that month),
  made from the merged pull requests since the previous release.

This script plans and prepares a release, extracts release notes, lists the
git tags a release needs, and checks in CI that a schema change carries a
schema-version change. It never talks to GitHub: the workflows
(`.github/workflows/release-pr.yml`, `release-publish.yml`) do that.

    python tools/release.py plan                 # print the next release; write nothing
    python tools/release.py prepare              # write version.yaml, CHANGELOG.md, state.yaml
    python tools/release.py notes 2026.10.1      # the CHANGELOG entry, for the GitHub Release
    python tools/release.py tags                 # tags the current version.yaml needs
    python tools/release.py check-schema         # CI: schema changed => schema_version changed

Exit codes: 0 = ok, 1 = a check failed or there is nothing to release.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "validation"))

SCHEMA_PATH = REPO_ROOT / "metadata" / "schema.json"
VERSION_PATH = REPO_ROOT / "metadata" / "version.yaml"
CHANGELOG_PATH = REPO_ROOT / "CHANGELOG.md"
STATE_PATH = REPO_ROOT / ".agent" / "state.yaml"

DATA_TAG_PREFIX = "data-"
SCHEMA_TAG_PREFIX = "schema-"
START_MARK = "<!-- releases:start -->"
END_MARK = "<!-- releases:end -->"

SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
CALVER_RE = re.compile(r"^(\d{4})\.(0[1-9]|1[0-2])\.([1-9]\d*)$")
PR_RE = re.compile(r"\(#(\d+)\)\s*$")

# Where an entity file lives (the folders `metadata/schema.json` maps types to,
# plus the anchors). A pull request touching one of these changes the data.
DATA_DIRS = (
    "initiatives/", "legislation/", "policies/", "soft-law/", "strategies/",
    "standards/", "frameworks/", "programmes/", "organisations/", "data-spaces/",
    "platforms/", "publications/", "domains/", "countries/", "regions/",
    "international/",
)
SCHEMA_FILES = (
    "metadata/schema.json", "metadata/ontology.md", "metadata/metadata-schema.md",
    "metadata/relationship-types.md", "metadata/taxonomy.md", "metadata/rank-basis.md",
)
TOOLING_DIRS = ("tools/", "validation/", ".github/")
DOC_FILES = ("README.md", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md",
             "AGENTS.md", "CHANGELOG.md")
HOUSEKEEPING_DIRS = (".agent/", "discovery/", "progress/")

# Highest first: a pull request is filed under the first category it touches.
CATEGORIES = (
    ("schema", "Schema"),
    ("site", "Site and features"),
    ("data", "Data"),
    ("tooling", "Tooling"),
    ("docs", "Documentation"),
    ("housekeeping", "Housekeeping"),
)


# ── pure functions (unit-tested without git) ─────────────────────────────

def parse_data_versions(tags: list[str]) -> list[tuple[int, int, int]]:
    out = []
    for t in tags:
        if t.startswith(DATA_TAG_PREFIX):
            m = CALVER_RE.match(t[len(DATA_TAG_PREFIX):])
            if m:
                out.append(tuple(int(x) for x in m.groups()))
    return sorted(out)


def next_data_version(today: date, tags: list[str]) -> str:
    """`YYYY.MM.N`: N is one more than the highest release already made in
    that month, so two releases in one month never share a number."""
    n = 0
    for y, mth, k in parse_data_versions(tags):
        if (y, mth) == (today.year, today.month):
            n = max(n, k)
    return f"{today.year}.{today.month:02d}.{n + 1}"


def semver_tuple(s: str) -> tuple[int, int, int]:
    m = SEMVER_RE.match(s or "")
    if not m:
        raise ValueError(f"not a SemVer version: {s!r}")
    return tuple(int(x) for x in m.groups())  # type: ignore[return-value]


def classify(files: list[str]) -> str:
    """The category a change belongs to, from the files it touched."""
    def any_in(prefixes):
        return any(f == p or f.startswith(p) for f in files for p in prefixes)
    if any(f in SCHEMA_FILES for f in files):
        return "schema"
    if any(f.startswith("site/") for f in files):
        return "site"
    if any_in(DATA_DIRS):
        return "data"
    if any_in(TOOLING_DIRS):
        return "tooling"
    if any(f in DOC_FILES or f.startswith("docs/") for f in files):
        return "docs"
    return "housekeeping"


def parse_log(raw: str) -> list[dict]:
    """`git log --first-parent --format=%H%x1f%s%x1f%aI%x1e` output → changes.
    Only squash-merged pull requests ("Title (#123)") are changes; anything
    else on main (direct commits) is ignored, because the workflow never makes
    them."""
    changes = []
    for rec in raw.split("\x1e"):
        rec = rec.strip("\n")
        if not rec:
            continue
        sha, subject, when = rec.split("\x1f")[:3]
        m = PR_RE.search(subject)
        if not m:
            continue
        changes.append({
            "sha": sha.strip(), "number": int(m.group(1)),
            "title": PR_RE.sub("", subject).strip(), "date": when[:10],
        })
    return changes


def is_release_change(change: dict) -> bool:
    return change["title"].lower().startswith("release data ")


def group_changes(changes: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {k: [] for k, _ in CATEGORIES}
    for c in changes:
        groups[c["category"]].append(c)
    return groups


def render_entry(*, version: str, schema: str, prev_schema: str | None, released: str,
                 counts: dict, prev_counts: dict | None, changes: list[dict],
                 issues: list[dict], baseline: bool) -> str:
    lines = [f"## Data release {version} — {released}", ""]
    schema_line = f"**Schema {schema}**"
    if prev_schema and prev_schema != schema:
        schema_line += f" (changed from {prev_schema})"
    elif prev_schema:
        schema_line += " (unchanged)"
    lines += [schema_line, ""]

    def delta(key, label):
        now = counts.get(key)
        if prev_counts and key in prev_counts and now is not None:
            d = now - prev_counts[key]
            return f"{now:,} {label} ({d:+,})"
        return f"{now:,} {label}"
    lines.append("In the Atlas at this release: " + ", ".join([
        delta("entities", "entities"), delta("relationships", "typed relationships"),
        delta("countries", "countries")]) + ".")
    lines.append("")

    if baseline:
        lines += [
            "This is the first tagged release. The changes before it are not listed here: "
            "they are in the git history (`git log`) and, from 2026-09-26, in "
            "`.agent/run-history/`. Schema changes before versioning are listed in "
            "`metadata/versioning.md`.", ""]
    else:
        groups = group_changes(changes)
        shown = False
        for key, label in CATEGORIES:
            items = groups.get(key) or []
            if not items:
                continue
            shown = True
            lines.append(f"### {label}")
            lines.append("")
            for c in items:
                lines.append(f"- {c['title']} (#{c['number']})")
            lines.append("")
        if not shown:
            lines += ["No pull requests were merged since the previous release.", ""]

    if issues:
        lines += ["### Roadmap items completed", ""]
        for i in issues:
            lines.append(f"- {i['title']} (#{i['number']})")
        lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


def insert_entry(changelog: str, entry: str) -> str:
    if START_MARK not in changelog or END_MARK not in changelog:
        raise ValueError(f"CHANGELOG.md must contain {START_MARK} and {END_MARK}")
    head, rest = changelog.split(START_MARK, 1)
    return head + START_MARK + "\n\n" + entry + "\n" + rest.lstrip("\n")


def entry_for(changelog: str, version: str) -> str | None:
    """The CHANGELOG section for one data release, without its heading."""
    m = re.search(rf"^## Data release {re.escape(version)} — .*$", changelog, re.M)
    if not m:
        return None
    rest = changelog[m.end():]
    nxt = re.search(r"^## |^<!-- releases:end -->", rest, re.M)
    body = rest[:nxt.start()] if nxt else rest
    return body.strip("\n") + "\n"


def schema_change_error(base_text: str | None, head_text: str) -> str | None:
    """CI rule: if the data model in schema.json changed, `schema_version` must
    have changed too, and must have gone up. Returns an error message or None."""
    head = json.loads(head_text)
    try:
        head_v = semver_tuple(head.get("schema_version", ""))
    except ValueError:
        return "metadata/schema.json: 'schema_version' is missing or not MAJOR.MINOR.PATCH"
    if base_text is None:
        return None
    base = json.loads(base_text)
    strip = lambda d: {k: v for k, v in d.items() if k != "schema_version"}
    if strip(base) == strip(head):
        return None  # no model change; a version bump on its own is allowed
    try:
        base_v = semver_tuple(base.get("schema_version", "0.0.0"))
    except ValueError:
        return None
    if head_v == base_v:
        return ("metadata/schema.json changed but 'schema_version' did not. Bump it "
                "(metadata/versioning.md says how: MAJOR for a removal or rename, MINOR for "
                "an addition, PATCH for a clarification) in this pull request.")
    if head_v < base_v:
        return f"'schema_version' went backwards ({base.get('schema_version')} → {head.get('schema_version')})"
    return None


def update_state_text(state: str, version: str, schema: str, released: str) -> str:
    block = (f"release:\n  data: \"{version}\"\n  schema: \"{schema}\"\n"
             f"  released: \"{released}\"\n")
    if re.search(r"^release:\n(?:  .*\n)+", state, re.M):
        return re.sub(r"^release:\n(?:  .*\n)+", block, state, count=1, flags=re.M)
    return re.sub(r"^(validation_status:.*\n)", r"\1\n" + block, state, count=1, flags=re.M) \
        if re.search(r"^validation_status:", state, re.M) else state + "\n" + block


# ── git and files ────────────────────────────────────────────────────────

def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO_ROOT, check=True,
                          capture_output=True, text=True).stdout


def existing_tags() -> list[str]:
    return [t for t in git("tag", "--list").split("\n") if t]


def read_yaml(path: Path) -> dict:
    import yaml
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}


def current_schema_version() -> str:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))["schema_version"]


def changes_since(tag: str | None) -> list[dict]:
    rng = [f"{tag}..HEAD"] if tag else []
    raw = git("log", "--first-parent", "--format=%H%x1f%s%x1f%aI%x1e", *rng)
    changes = [c for c in parse_log(raw) if not is_release_change(c)]
    for c in changes:
        files = git("show", "--name-only", "--format=", c["sha"]).split("\n")
        c["category"] = classify([f for f in files if f])
    return changes


def last_data_tag() -> str | None:
    versions = parse_data_versions(existing_tags())
    if not versions:
        return None
    y, m, n = versions[-1]
    return f"{DATA_TAG_PREFIX}{y}.{m:02d}.{n}"


def graph_counts() -> dict:
    import build_graph
    payload, errors, _ = build_graph.build()
    if errors:
        raise SystemExit("build_graph refused: " + "; ".join(errors[:3]))
    s = payload["graph"]["stats"]
    return {"entities": s["entities"], "relationships": s["relationships"],
            "countries": s["countries"]}


def plan(today: date, issues: list[dict]) -> dict:
    tags = existing_tags()
    prev_tag = last_data_tag()
    prev = read_yaml(VERSION_PATH)
    version = next_data_version(today, tags)
    changes = changes_since(prev_tag)
    schema = current_schema_version()
    counts = graph_counts()
    entry = render_entry(
        version=version, schema=schema, prev_schema=prev.get("schema_version"),
        released=today.isoformat(), counts=counts, prev_counts=prev.get("counts"),
        changes=changes, issues=issues, baseline=prev_tag is None)
    releasable = [c for c in changes if c["category"] != "housekeeping"]
    return {"version": version, "schema": schema, "prev_tag": prev_tag, "entry": entry,
            "counts": counts, "changes": changes, "releasable": releasable,
            "baseline": prev_tag is None, "released": today.isoformat()}


# ── commands ─────────────────────────────────────────────────────────────

def load_issues(path: str | None) -> list[dict]:
    if not path:
        return []
    return [{"number": i["number"], "title": i["title"]}
            for i in json.loads(Path(path).read_text(encoding="utf-8"))]


def parse_today(s: str | None) -> date:
    return date.fromisoformat(s) if s else datetime.now(timezone.utc).date()


def cmd_plan(a) -> int:
    p = plan(parse_today(a.date), load_issues(a.issues_json))
    print(f"next data release: {p['version']}   schema: {p['schema']}   "
          f"since: {p['prev_tag'] or '(first release)'}")
    print(f"pull requests since: {len(p['changes'])}, of which {len(p['releasable'])} "
          f"beyond housekeeping\n")
    print(p["entry"])
    return 0


def cmd_prepare(a) -> int:
    p = plan(parse_today(a.date), load_issues(a.issues_json))
    if not p["baseline"] and not p["releasable"] and not a.force:
        print("nothing to release: no pull request beyond housekeeping since "
              f"{p['prev_tag']}", file=sys.stderr)
        return 1
    VERSION_PATH.write_text(
        "# Written by tools/release.py when a release is prepared. Do not edit by hand.\n"
        f"data_release: \"{p['version']}\"\n"
        f"schema_version: \"{p['schema']}\"\n"
        f"released: \"{p['released']}\"\n"
        "counts:\n"
        f"  entities: {p['counts']['entities']}\n"
        f"  relationships: {p['counts']['relationships']}\n"
        f"  countries: {p['counts']['countries']}\n", encoding="utf-8")
    CHANGELOG_PATH.write_text(
        insert_entry(CHANGELOG_PATH.read_text(encoding="utf-8"), p["entry"]), encoding="utf-8")
    if STATE_PATH.exists():
        STATE_PATH.write_text(update_state_text(
            STATE_PATH.read_text(encoding="utf-8"), p["version"], p["schema"], p["released"]),
            encoding="utf-8")
    print(f"prepared data release {p['version']} (schema {p['schema']})")
    return 0


def cmd_notes(a) -> int:
    body = entry_for(CHANGELOG_PATH.read_text(encoding="utf-8"), a.version)
    if body is None:
        print(f"no CHANGELOG entry for {a.version}", file=sys.stderr)
        return 1
    print(body, end="")
    return 0


def cmd_tags(_a) -> int:
    v = read_yaml(VERSION_PATH)
    if not v:
        print("no metadata/version.yaml: nothing released yet", file=sys.stderr)
        return 1
    have = set(existing_tags())
    wanted = [f"{DATA_TAG_PREFIX}{v['data_release']}"]
    stag = f"{SCHEMA_TAG_PREFIX}{v['schema_version']}"
    if stag not in have:
        wanted.append(stag)
    for t in wanted:
        print(f"{t}\t{'exists' if t in have else 'missing'}")
    return 0


def cmd_check_schema(a) -> int:
    head = SCHEMA_PATH.read_text(encoding="utf-8")
    base = None
    if a.base_ref:
        try:
            base = git("show", f"{a.base_ref}:metadata/schema.json")
        except subprocess.CalledProcessError:
            base = None
    err = schema_change_error(base, head)
    if err:
        print(f"ERROR {err}")
        return 1
    print(f"schema version {json.loads(head)['schema_version']}: ok")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("plan", "prepare"):
        sp = sub.add_parser(name)
        sp.add_argument("--date", help="release date, YYYY-MM-DD (default: today, UTC)")
        sp.add_argument("--issues-json", help="JSON list of closed roadmap issues "
                                              "([{number, title}, ...])")
        if name == "prepare":
            sp.add_argument("--force", action="store_true",
                            help="release even if only housekeeping changed")
    sp = sub.add_parser("notes")
    sp.add_argument("version")
    sub.add_parser("tags")
    sp = sub.add_parser("check-schema")
    sp.add_argument("--base-ref", help="git ref to compare schema.json against, e.g. origin/main")
    a = ap.parse_args()
    return {"plan": cmd_plan, "prepare": cmd_prepare, "notes": cmd_notes,
            "tags": cmd_tags, "check-schema": cmd_check_schema}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
