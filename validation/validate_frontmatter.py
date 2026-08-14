#!/usr/bin/env python3
"""Validate frontmatter: required fields present, controlled-vocabulary
values valid, and (for flat entity types) file placed in the folder its
`type` maps to."""

from __future__ import annotations

import re
import sys

import common

ISO2_RE = re.compile(r"^[A-Z]{2}$")

# Fields that are required to be *present* but may legitimately hold null
# (e.g. country: null for EU/UN-scoped entities) — metadata-schema.md.
NULLABLE_REQUIRED_FIELDS = {"country"}


def check_placement(e: common.EntityFile, schema: dict, report: common.Report) -> None:
    entity_type = e.frontmatter.get("type")
    if entity_type not in schema["type_folder_map"]:
        return  # unknown type already reported by the type check below

    entity_id = e.frontmatter.get("id")
    if entity_id in schema["anchor_ids"]:
        # NL/EU/UN anchors are exempt from the flat type->folder mapping by
        # design — they live under countries/<iso>/, regions/<code>/ or
        # international/<code>/ instead (metadata/ontology.md §3.1).
        return

    expected_folder = schema["type_folder_map"][entity_type]
    rel_parts = e.path.relative_to(common.REPO_ROOT).parts

    if entity_type in ("country", "region"):
        # Nested one level: countries/<iso>/<file>.md, regions/<code>/<file>.md
        if rel_parts[0] != expected_folder:
            report.error(
                f"{e.rel_path}: type '{entity_type}' entities must live under "
                f"'{expected_folder}/<code>/', found under '{rel_parts[0]}/'"
            )
        return

    if rel_parts[0] != expected_folder:
        report.error(
            f"{e.rel_path}: type '{entity_type}' must live in '{expected_folder}/', "
            f"found in '{rel_parts[0]}/' (metadata/ontology.md §3)"
        )


def main() -> int:
    schema = common.load_schema()
    entities = common.load_all_entities()
    report = common.Report("validate_frontmatter")

    for e in entities:
        if e.parse_error:
            report.error(f"{e.rel_path}: {e.parse_error}")
            continue

        fm = e.frontmatter

        for field_name in schema["required_fields"]:
            if field_name not in fm:
                report.error(f"{e.rel_path}: missing required field '{field_name}'")
            elif field_name not in NULLABLE_REQUIRED_FIELDS and fm[field_name] in (None, ""):
                report.error(f"{e.rel_path}: missing required field '{field_name}'")

        entity_type = fm.get("type")
        if entity_type is not None and entity_type not in schema["types"]:
            report.error(f"{e.rel_path}: invalid type '{entity_type}'")
        elif entity_type is not None:
            check_placement(e, schema, report)

        level = fm.get("level")
        if level is not None and level not in schema["levels"]:
            report.error(f"{e.rel_path}: invalid level '{level}'")

        status = fm.get("status")
        if status is not None and status not in schema["statuses"]:
            report.error(f"{e.rel_path}: invalid status '{status}'")

        confidence = fm.get("confidence")
        if confidence is not None and confidence not in schema["confidence_levels"]:
            report.error(f"{e.rel_path}: invalid confidence '{confidence}'")

        coverage = fm.get("coverage")
        if coverage is not None and coverage not in schema["coverage_levels"]:
            report.error(f"{e.rel_path}: invalid coverage '{coverage}'")

        country = fm.get("country")
        if country is not None and not ISO2_RE.match(str(country)):
            report.error(
                f"{e.rel_path}: country '{country}' is not a plausible "
                f"ISO 3166-1 alpha-2 code (use null if not applicable)"
            )

        if status == "active" and not fm.get("last_verified"):
            report.warn(f"{e.rel_path}: status is 'active' but 'last_verified' is not set")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
