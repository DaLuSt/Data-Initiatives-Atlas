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


def check_dates(rel_path: str, fm: dict, report: common.Report) -> None:
    """start_date, end_date and last_verified are real dates (or empty), the
    end is not before the start, and a verification date is not in the future.
    A partial date ("2020") is not a date here: the repository's rule is to leave
    the field empty and say the precision in prose."""
    days = {}
    for key in ("start_date", "end_date", "last_verified"):
        value = fm.get(key)
        if value in (None, ""):
            continue
        day = common.as_date(value)
        if day is None:
            report.error(f"{rel_path}: {key} '{value}' is not a YYYY-MM-DD date "
                         f"(leave it empty rather than padding a partial date)")
        else:
            days[key] = day
    if "start_date" in days and "end_date" in days and days["end_date"] < days["start_date"]:
        report.error(f"{rel_path}: end_date {days['end_date']} is before start_date {days['start_date']}")
    if "last_verified" in days and common.is_in_the_future(days["last_verified"]):
        report.error(f"{rel_path}: last_verified {days['last_verified']} is in the future")


def check_rank(rel_path: str, entity_type, rank, schema: dict,
               report: common.Report, status=None) -> None:
    """`rank` is optional. Where it is set it must be a known value, and the
    entity's type must be one that has a place in a legal hierarchy and allow
    that value (an `act` is never `delegated`; subordinate legislation always is).
    A bill or draft (`proposed`, `planned`) has no rank until it is enacted.
    """
    if rank is None:
        return
    if status in ("proposed", "planned"):
        report.error(
            f"{rel_path}: a '{status}' instrument has no rank yet; "
            f"remove 'rank' until it is enacted"
        )
        return
    if rank not in schema["rank_levels"]:
        report.error(f"{rel_path}: invalid rank '{rank}'")
        return
    allowed = schema["rank_by_type"].get(entity_type)
    if allowed is None:
        report.error(
            f"{rel_path}: 'rank' is only valid on legislation types "
            f"({', '.join(schema['rank_by_type'])}), found on type '{entity_type}'"
        )
    elif rank not in allowed:
        report.error(
            f"{rel_path}: rank '{rank}' is not allowed on type '{entity_type}' "
            f"(allowed: {', '.join(allowed)})"
        )


def check_name_en(rel_path: str, name, name_en, alternative_names,
                  report: common.Report) -> None:
    """`name_en` is an optional short English display name. Where it is set it
    must be a non-empty string that says something `name` does not, and it must
    also be listed in `alternative_names` so that search and de-duplication,
    which read that list, see it."""
    if name_en is None:
        return
    if not isinstance(name_en, str) or not name_en.strip():
        report.error(f"{rel_path}: 'name_en' must be a non-empty string")
        return
    if name_en != name_en.strip():
        report.error(f"{rel_path}: 'name_en' has leading or trailing whitespace")
    if isinstance(name, str) and name_en.strip().casefold() == name.strip().casefold():
        report.error(
            f"{rel_path}: 'name_en' repeats 'name'; remove it (an English "
            f"official name needs no separate English name)"
        )
        return
    listed = [str(a).strip().casefold() for a in (alternative_names or [])]
    if name_en.strip().casefold() not in listed:
        report.error(f"{rel_path}: 'name_en' must also be listed in 'alternative_names'")


def main() -> int:
    schema = common.load_schema()
    entities = common.load_all_entities()
    report = common.Report("validate_frontmatter")
    # The countries the Atlas has an anchor for: an entity's `country` must be one of them.
    # (tools/build_graph.py also needs a map position for it, and refuses a build without one.)
    country_anchors = {e.frontmatter.get("id") for e in entities
                       if not e.parse_error and e.frontmatter.get("type") == "country"}

    for e in entities:
        if e.parse_error:
            report.error(f"{e.rel_path}: {e.parse_error}")
            continue

        fm = e.frontmatter

        if isinstance(fm.get("id"), bool):
            report.error(
                f"{e.rel_path}: id parsed as the boolean {fm['id']} — an unquoted "
                f"YAML 1.1 boolean keyword. Quote it: id: \"NO\""
            )

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

        verification = fm.get("verification")
        if verification is not None and verification not in schema["verification_levels"]:
            report.error(f"{e.rel_path}: invalid verification '{verification}'")

        check_dates(e.rel_path, fm, report)
        if fm.get("level") == "national" and fm.get("country") in (None, ""):
            report.error(f"{e.rel_path}: level 'national' needs a country (use another level "
                         f"for an entity that is not one country's)")
        if fm.get("status") == "superseded" and not fm.get("successor"):
            report.warn(f"{e.rel_path}: status is 'superseded' but 'successor' is not set "
                        f"(fine if nothing replaced it that the Atlas holds, otherwise name it)")

        check_name_en(e.rel_path, fm.get("name"), fm.get("name_en"),
                      fm.get("alternative_names"), report)
        check_rank(e.rel_path, entity_type, fm.get("rank"), schema, report,
                   fm.get("status"))

        organisation_role = fm.get("organisation_role")
        if organisation_role is not None:
            if entity_type != "organisation":
                report.error(
                    f"{e.rel_path}: 'organisation_role' is only valid on "
                    f"type 'organisation', found on type '{entity_type}'"
                )
            elif organisation_role not in schema["organisation_role_levels"]:
                report.error(
                    f"{e.rel_path}: invalid organisation_role '{organisation_role}'"
                )

        # An entity may only claim high confidence if a human/agent actually
        # read a primary source for it.
        if verification in ("search-only", "unverified") and fm.get("confidence") == "high":
            report.error(
                f"{e.rel_path}: confidence 'high' is not permitted with "
                f"verification '{verification}' — no primary source has been read"
            )

        country = fm.get("country")
        if isinstance(country, bool):
            # YAML 1.1 resolves NO/ON/OFF/YES/N/Y to booleans, so an unquoted
            # `country: NO` silently becomes False. PyYAML's safe_load follows
            # YAML 1.1 here. Norway is the only ISO 3166-1 alpha-2 code the
            # Atlas uses that collides, but the same trap catches `id: NO`.
            report.error(
                f"{e.rel_path}: country parsed as the boolean {country} — an "
                f"unquoted YAML 1.1 boolean keyword. Quote it: country: \"NO\""
            )
        elif country is not None and not ISO2_RE.match(str(country)):
            report.error(
                f"{e.rel_path}: country '{country}' is not a plausible "
                f"ISO 3166-1 alpha-2 code (use null if not applicable)"
            )
        elif country is not None and country not in country_anchors:
            report.error(
                f"{e.rel_path}: country '{country}' has no country anchor in the Atlas "
                f"(an entity of type 'country' with id {country}, under countries/{str(country).lower()}/; "
                f"metadata/ontology.md §3.1)"
            )

        # A search-only/unverified entity correctly has no last_verified date
        # (nothing was verified), so the reminder would be pure noise there —
        # the verification field already flags it for a re-verification pass.
        if (
            status == "active"
            and not fm.get("last_verified")
            and verification not in ("search-only", "unverified")
        ):
            report.warn(f"{e.rel_path}: status is 'active' but 'last_verified' is not set")

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
