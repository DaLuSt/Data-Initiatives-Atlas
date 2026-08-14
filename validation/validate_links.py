#!/usr/bin/env python3
"""Validate that every [[WIKILINK]] in the repository resolves to a real
entity id."""

from __future__ import annotations

import sys

import common


def main() -> int:
    entities = common.load_all_entities(entities_only=True)
    ids = common.known_ids(entities)

    report = common.Report("validate_links")

    # Wikilinks may also appear in index/README navigation pages, so scan
    # every non-excluded Markdown file, not just entity files.
    for path in common.iter_markdown_files(entities_only=False):
        e = common.parse_entity_file(path)
        for target in e.wikilinks:
            target = target.strip()
            if target not in ids:
                report.error(f"{e.rel_path}: broken wikilink [[{target}]] — no entity with that id")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
