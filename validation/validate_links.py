#!/usr/bin/env python3
"""Validate that every [[WIKILINK]] in the repository resolves to a real
entity id."""

from __future__ import annotations

import re
import sys

import common

# `discovery/unresolved.md` drops a row when it is closed, and row numbers are never reused, so a
# gap means "closed" and many files rightly say "closing row #113". A file that calls a row still
# OPEN while the table has no such row is out of date. Only that is reported (as a warning): the
# wording is a heuristic, so a reference that says the row is closed is left alone.
ROW_REFERENCE = re.compile(r"(?:rows?|items?)\s+#(\d+)(?:(?:\s*,\s*|\s+and\s+|\s+to\s+)#?(\d+))*", re.I)
SAYS_OPEN = re.compile(
    r"(still|remains?|is|stays?|currently|yet)\s+(open|unresolved|undecided|pending)"
    r"|open (question|item|row)|not yet (closed|decided|resolved)", re.I)
SAYS_CLOSED = re.compile(r"clos|resolv|settled|decided|declined|answered|removed|narrowed|moved", re.I)


DETAIL_LINK = re.compile(r"\[full detail\]\(unresolved/([a-z0-9-]+)\.md#row-(\d+)\)")
LONG_CELL = 700


def unresolved_table_problems(text: str, detail_dir_files: dict[str, str]) -> list[tuple[str, str]]:
    """(severity, message) for the master table of discovery/unresolved.md: seven cells per row, each
    "[full detail]" link pointing at a section that exists, and a long detail cell with no link."""
    problems: list[tuple[str, str]] = []
    for line in text.splitlines():
        m = re.match(r"\| (\d+) \|", line)
        if not m:
            continue
        n = int(m.group(1))
        cells = re.split(r"(?<!\\) \| ", line.rstrip())
        if len(cells) != 7:
            problems.append(("error", f"row #{n} has {len(cells)} cells, not 7 (an unescaped '|' inside a cell? write \\|)"))
            continue
        link = DETAIL_LINK.search(cells[4])
        if link:
            body = detail_dir_files.get(link.group(1))
            if body is None or f'<a id="row-{link.group(2)}"></a>' not in body or int(link.group(2)) != n:
                problems.append(("error", f"row #{n}: the detail link {link.group(0)} points at a section that does not exist"))
        elif len(cells[4]) > LONG_CELL:
            problems.append(("warn", f"row #{n}: the detail cell is {len(cells[4])} characters; move the long text to "
                                     f"discovery/unresolved/<area>.md and link it"))
    return problems


def open_row_numbers(unresolved_text: str) -> set[int]:
    return {int(m.group(1)) for line in unresolved_text.splitlines() if (m := re.match(r"\| (\d+) \|", line))}


def stale_row_references(text: str, open_rows: set[int]) -> list[int]:
    """Row numbers that `text` describes as open although the table no longer has them."""
    stale: list[int] = []
    for m in ROW_REFERENCE.finditer(text):
        numbers = [int(x) for x in re.findall(r"\d+", m.group(0))]
        missing = [n for n in numbers if n not in open_rows]
        if not missing:
            continue
        context = text[max(0, m.start() - 120): m.end() + 120]
        if SAYS_OPEN.search(context) and not SAYS_CLOSED.search(context):
            stale.extend(missing)
    return stale


def main() -> int:
    entities = common.load_all_entities(entities_only=True)
    ids = common.known_ids(entities)

    report = common.Report("validate_links")

    unresolved = common.REPO_ROOT / "discovery" / "unresolved.md"
    open_rows = open_row_numbers(unresolved.read_text(encoding="utf-8")) if unresolved.exists() else None
    if unresolved.exists():
        detail_dir = unresolved.parent / "unresolved"
        files = {f.stem: f.read_text(encoding="utf-8") for f in detail_dir.glob("*.md")} if detail_dir.is_dir() else {}
        for severity, message in unresolved_table_problems(unresolved.read_text(encoding="utf-8"), files):
            (report.error if severity == "error" else report.warn)(f"discovery/unresolved.md: {message}")

    # Wikilinks may also appear in index/README navigation pages, so scan
    # every non-excluded Markdown file, not just entity files.
    for path in common.iter_markdown_files(entities_only=False):
        e = common.parse_entity_file(path)
        for target in e.wikilinks:
            target = target.strip()
            if target not in ids:
                report.error(f"{e.rel_path}: broken wikilink [[{target}]] — no entity with that id")
        if open_rows is not None and e.rel_path != "discovery/unresolved.md":
            for n in stale_row_references(path.read_text(encoding="utf-8"), open_rows):
                report.warn(f"{e.rel_path}: calls row #{n} of discovery/unresolved.md open, but the table has no such "
                            f"row (closed rows are removed): update the sentence")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
