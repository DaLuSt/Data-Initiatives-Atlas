#!/usr/bin/env python3
"""List the entities by the age of their `last_verified` date (roadmap #510).

The policy is in docs/re-verification.md ("How old may `last_verified` get"): an entity is due
for a new read of its sources 12 months after its `last_verified` date, and is listed as due
soon from 9 months. This tool measures that; it changes nothing.

    python tools/verification_age.py                    # a summary and the 20 oldest
    python tools/verification_age.py --due              # everything due soon or overdue
    python tools/verification_age.py --markdown         # the same as a table, for a pull request or issue
    python tools/verification_age.py --asof 2027-06-01  # plan a cycle: who will be due by then
    python tools/verification_age.py --fail-on-overdue  # exit 1 if any entity is overdue (not run in CI)
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "validation"))

from common import load_all_entities  # noqa: E402

DUE_SOON_MONTHS = 9
DUE_MONTHS = 12
_DATE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def parse_date(value) -> date | None:
    """A `last_verified` value (a string, or a date the YAML loader already made) as a date."""
    if isinstance(value, date):
        return value
    m = _DATE.match(str(value or "").strip())
    if not m:
        return None
    try:
        return date(int(m[1]), int(m[2]), int(m[3]))
    except ValueError:
        return None


def months_between(start: date, end: date) -> int:
    """Whole calendar months from start to end (never negative)."""
    months = (end.year - start.year) * 12 + end.month - start.month
    if end.day < start.day:
        months -= 1
    return max(months, 0)


def status(verified: date | None, asof: date) -> str:
    """`ok`, `due-soon`, `overdue` or `undated`."""
    if verified is None:
        return "undated"
    age = months_between(verified, asof)
    if age >= DUE_MONTHS:
        return "overdue"
    if age >= DUE_SOON_MONTHS:
        return "due-soon"
    return "ok"


def rows(asof: date) -> list[dict]:
    out = []
    for e in load_all_entities():
        fm = e.frontmatter or {}
        if not isinstance(fm.get("id"), str):
            continue
        verified = parse_date(fm.get("last_verified"))
        out.append({
            "id": fm["id"],
            "type": fm.get("type", ""),
            "verified": verified,
            "months": None if verified is None else months_between(verified, asof),
            "status": status(verified, asof),
            "path": str(Path(e.path).relative_to(REPO_ROOT)) if getattr(e, "path", None) else "",
        })
    # Oldest first; undated entities lead, since they are the most overdue of all.
    out.sort(key=lambda r: (r["verified"] is not None, r["verified"] or date.min, r["id"]))
    return out


def summary(items: list[dict]) -> dict[str, int]:
    counts = {"ok": 0, "due-soon": 0, "overdue": 0, "undated": 0}
    for r in items:
        counts[r["status"]] += 1
    return counts


def by_month(items: list[dict]) -> list[tuple[str, int]]:
    seen: dict[str, int] = {}
    for r in items:
        key = "undated" if r["verified"] is None else r["verified"].strftime("%Y-%m")
        seen[key] = seen.get(key, 0) + 1
    return sorted(seen.items())


def render(items: list[dict], asof: date, due_only: bool, markdown: bool, limit: int) -> str:
    counts = summary(items)
    lines = [f"Entities by the age of `last_verified`, as of {asof.isoformat()} "
             f"(due soon from {DUE_SOON_MONTHS} months, due at {DUE_MONTHS}):", ""]
    lines.append(f"{len(items)} entities: {counts['ok']} ok, {counts['due-soon']} due soon, "
                 f"{counts['overdue']} overdue, {counts['undated']} without a date.")
    lines.append("")
    lines.append("By month verified: " + ", ".join(f"{m} {n}" for m, n in by_month(items)))
    lines.append("")
    shown = [r for r in items if r["status"] != "ok"] if due_only else items[:limit]
    if not shown:
        lines.append("Nothing is due." if due_only else "")
        return "\n".join(lines)
    title = "Due soon or overdue" if due_only else f"The {len(shown)} oldest"
    lines.append(f"{title}:")
    lines.append("")
    if markdown:
        lines += ["| Entity | Type | Last verified | Months | Status |", "|---|---|---|---|---|"]
        for r in shown:
            lines.append(f"| {r['id']} | {r['type']} | {r['verified'] or '—'} | "
                         f"{'—' if r['months'] is None else r['months']} | {r['status']} |")
    else:
        for r in shown:
            lines.append(f"  {r['verified'] or 'undated   '}  {'' if r['months'] is None else r['months']!s:>3} mo  "
                         f"{r['status']:<8}  {r['id']}  ({r['type']})")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--asof", help="measure at this date (YYYY-MM-DD) instead of today")
    ap.add_argument("--due", action="store_true", help="list only the entities due soon or overdue")
    ap.add_argument("--markdown", action="store_true", help="print the list as a Markdown table")
    ap.add_argument("--limit", type=int, default=20, help="how many of the oldest to list (default 20)")
    ap.add_argument("--fail-on-overdue", action="store_true", help="exit 1 if any entity is overdue or undated")
    args = ap.parse_args(argv)

    asof = parse_date(args.asof) if args.asof else date.today()
    if asof is None:
        ap.error("--asof must be a date, YYYY-MM-DD")
    items = rows(asof)
    print(render(items, asof, args.due, args.markdown, args.limit))
    counts = summary(items)
    return 1 if args.fail_on_overdue and (counts["overdue"] or counts["undated"]) else 0


if __name__ == "__main__":
    sys.exit(main())
