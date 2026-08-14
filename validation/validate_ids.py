#!/usr/bin/env python3
"""Validate entity IDs: uniqueness, format, and filename/id agreement."""

from __future__ import annotations

import re
import sys
from collections import defaultdict

import common


def main() -> int:
    schema = common.load_schema()
    id_pattern = re.compile(schema["id_scope_pattern"])
    anchor_ids = set(schema["anchor_ids"])

    entities = common.load_all_entities()
    report = common.Report("validate_ids")

    by_id: dict[str, list[str]] = defaultdict(list)

    for e in entities:
        if e.parse_error:
            report.error(f"{e.rel_path}: cannot check ID — {e.parse_error}")
            continue

        entity_id = e.frontmatter.get("id")
        if not entity_id or not isinstance(entity_id, str):
            report.error(f"{e.rel_path}: missing or non-string 'id' field")
            continue

        by_id[entity_id].append(e.rel_path)

        if entity_id not in anchor_ids and not id_pattern.match(entity_id):
            report.error(
                f"{e.rel_path}: id '{entity_id}' does not match the required "
                f"format <SCOPE>-<SLUG> (SCOPE = UN | EU | INTL | ISO2), "
                f"see metadata/ontology.md §2"
            )

        expected_filename = f"{entity_id.lower()}.md"
        if e.path.name != expected_filename:
            report.error(
                f"{e.rel_path}: filename does not match id '{entity_id}' "
                f"(expected '{expected_filename}')"
            )

    for entity_id, paths in sorted(by_id.items()):
        if len(paths) > 1:
            report.error(f"Duplicate id '{entity_id}' used in: {', '.join(paths)}")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
