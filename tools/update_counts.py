#!/usr/bin/env python3
"""Keep the headline numbers in README.md and .agent/state.yaml equal to what the data builds to.

Every data change moves these numbers (entities, connections, relationships, countries, open
questions), and writing them by hand is error-prone: a text replace of "771" can hit the wrong
number. This tool reads the numbers from the graph generator and rewrites them in place.

    python tools/update_counts.py           # rewrite README.md and .agent/state.yaml
    python tools/update_counts.py --check   # change nothing; exit 1 and say what drifted

CI runs the second form, so a pull request that changes the data without the numbers fails.
The "Figures as of" date and the `updated` date in state.yaml are set by the writing form only
(they are dates, not counts, and the check ignores them).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "validation"))

README = REPO_ROOT / "README.md"
STATE = REPO_ROOT / ".agent" / "state.yaml"
UNRESOLVED = REPO_ROOT / "discovery" / "unresolved.md"

_ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
         "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def words(n: int) -> str:
    """0 to 199 in lower-case English, hyphenated as the README writes it ('sixty-three')."""
    if not 0 <= n < 200:
        raise ValueError(f"words() covers 0 to 199, got {n}")
    if n < 20:
        return _ONES[n]
    if n < 100:
        t, o = divmod(n, 10)
        return _TENS[t] + (("-" + _ONES[o]) if o else "")
    rest = n - 100
    return "one hundred" + ((" and " + words(rest)) if rest else "")


def commas(n: int) -> str:
    return f"{n:,}"


def open_questions(text: str) -> int:
    """Rows of the table in discovery/unresolved.md (lines that start `| <number> |`)."""
    return sum(1 for line in text.splitlines() if re.match(r"\| \d+ \|", line))


def numbers(stats: dict, countries_with_entities: int, unresolved_rows: int) -> dict:
    return {
        "entities": stats["entities"],
        "connections": stats["edges_total"],
        "relationships": stats["relationships"],
        "associations": stats["associations"],
        "wikilinks": stats["wikilinks"],
        "countries": stats["countries"],
        "regions": stats["regions"],
        "countries_with_entities": countries_with_entities,
        "unresolved_rows": unresolved_rows,
    }


def patch_readme(text: str, n: dict, as_of: str | None) -> str:
    """Rewrite the counts in the README. A pattern that is not found is an error, not a silent skip."""
    steps = [
        (r"(explore )[\d,]+( entities and )[\d,]+( connections across )[a-z-]+(\s+countries)",
         lambda m: f"{m.group(1)}{commas(n['entities'])}{m.group(2)}{commas(n['connections'])}"
                   f"{m.group(3)}{words(n['countries'])}{m.group(4)}"),
        (r"(\| \*\*Entities\*\* \| )[\d,]+( \|)", lambda m: f"{m.group(1)}{commas(n['entities'])}{m.group(2)}"),
        (r"(\| \*\*Connections\*\* \| )[\d,]+( — of which \*\*)[\d,]+(\*\* are typed)",
         lambda m: f"{m.group(1)}{commas(n['connections'])}{m.group(2)}{commas(n['relationships'])}{m.group(3)}"),
        (r"(\| \*\*Country scopes\*\* \| \*\*)\d+(\*\* — )\d+( with national entities)",
         lambda m: f"{m.group(1)}{n['countries']}{m.group(2)}{n['countries_with_entities']}{m.group(3)}"),
        (r"(\*\*All )[\d,]+( entities are `verification: primary-source`)",
         lambda m: f"{m.group(1)}{commas(n['entities'])}{m.group(2)}"),
        (r"(\*\*All )[\d,]+( entities have moved past this stage)",
         lambda m: f"{m.group(1)}{commas(n['entities'])}{m.group(2)}"),
    ]
    for pattern, repl in steps:
        text, count = re.subn(pattern, repl, text)
        if count == 0:
            raise SystemExit(f"update_counts: README.md has no text matching {pattern!r}")
    if as_of:
        text, count = re.subn(r"(\*Figures as of )\d{4}-\d{2}-\d{2}", lambda m: m.group(1) + as_of, text)
        if count == 0:
            raise SystemExit("update_counts: README.md has no 'Figures as of' line")
    return text


def patch_state(text: str, n: dict, as_of: str | None) -> str:
    fields = {
        "entity_count": n["entities"],
        "relationship_edges": n["relationships"],
        "association_edges": n["associations"],
        "wikilink_edges": n["wikilinks"],
        "edges_total": n["connections"],
        "countries": n["countries"],
        "regions": n["regions"],
        "unresolved_rows_open": n["unresolved_rows"],
    }
    for key, value in fields.items():
        text, count = re.subn(rf"(?m)^(\s+{key}: )\d+", lambda m: f"{m.group(1)}{value}", text)
        if count != 1:
            raise SystemExit(f"update_counts: .agent/state.yaml should have exactly one '{key}:' line, found {count}")
    if as_of:
        text, count = re.subn(r'(?m)^(updated: ")\d{4}-\d{2}-\d{2}(")', lambda m: m.group(1) + as_of + m.group(2), text)
        if count != 1:
            raise SystemExit("update_counts: .agent/state.yaml has no 'updated:' line")
    return text


def current_numbers() -> dict:
    import build_graph  # noqa: E402  (built in memory; nothing is written)

    payload, errors, _ = build_graph.build()
    if errors:
        raise SystemExit("update_counts: the graph does not build:\n  " + "\n  ".join(errors[:5]))
    graph = payload["graph"]
    anchors = {n["country"] for n in graph["nodes"] if n.get("country") and n.get("type") != "country"}
    return numbers(graph["stats"], len(anchors),
                   open_questions(UNRESOLVED.read_text(encoding="utf-8")))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="change nothing; exit 1 if a number has drifted")
    args = ap.parse_args(argv)
    n = current_numbers()
    today = date.today().isoformat()
    drift = []
    for path, patch in ((README, patch_readme), (STATE, patch_state)):
        old = path.read_text(encoding="utf-8")
        new = patch(old, n, None if args.check else today)
        if args.check:
            # dates are not counts: compare with the dates held fixed
            if patch(old, n, None) != old:
                drift.append(path.relative_to(REPO_ROOT).as_posix())
        elif new != old:
            path.write_text(new, encoding="utf-8")
            print(f"update_counts: rewrote {path.relative_to(REPO_ROOT)}")
    if args.check:
        if drift:
            print("update_counts: these files hold numbers that no longer match the data: " + ", ".join(drift)
                  + "\n  run: python tools/update_counts.py", file=sys.stderr)
            return 1
        print("update_counts: README.md and .agent/state.yaml match the data.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
