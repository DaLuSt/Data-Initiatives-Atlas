#!/usr/bin/env python3
"""Validate relationship data: controlled relationship types, resolvable
targets, and well-formed provenance on the `relationships:` list."""

from __future__ import annotations

import sys

import common


def check_id_list(e: common.EntityFile, field_name: str, ids: set[str], report: common.Report) -> None:
    values = e.frontmatter.get(field_name) or []
    if not isinstance(values, list):
        report.error(f"{e.rel_path}: '{field_name}' must be a list")
        return
    for target in values:
        if isinstance(target, bool):
            # YAML 1.1 resolves NO/YES/ON/OFF/Y/N to booleans, so `- NO` in a
            # list silently becomes False. Same trap as `country: NO`.
            report.error(
                f"{e.rel_path}: {field_name} contains the boolean {target} — an "
                f'unquoted YAML 1.1 boolean keyword. Quote it: - "NO"'
            )
        elif target not in ids:
            report.error(f"{e.rel_path}: {field_name} references unknown id '{target}'")


def check_relationships(e: common.EntityFile, schema: dict, ids: set[str], report: common.Report) -> None:
    relationships = e.frontmatter.get("relationships") or []
    if not isinstance(relationships, list):
        report.error(f"{e.rel_path}: 'relationships' must be a list")
        return

    for i, rel in enumerate(relationships):
        where = f"{e.rel_path}: relationships[{i}]"
        if not isinstance(rel, dict):
            report.error(f"{where} is not a mapping")
            continue

        rel_type = rel.get("type")
        if rel_type not in schema["relationship_types"]:
            report.error(f"{where}: invalid relationship type '{rel_type}'")

        target = rel.get("target")
        own_id = e.frontmatter.get("id")
        if not target:
            report.error(f"{where}: missing 'target'")
        elif target == own_id:
            report.error(f"{where}: target '{target}' is the entity itself — relationships must point at another entity")
        elif target not in ids:
            report.error(f"{where}: target '{target}' does not resolve to a known id")

        source = rel.get("source")
        if source not in schema["relationship_source_values"]:
            report.error(f"{where}: 'source' must be one of {schema['relationship_source_values']}, got '{source}'")
        elif source == "fact" and not rel.get("evidence"):
            report.error(f"{where}: source is 'fact' but no 'evidence' is given")

        confidence = rel.get("confidence")
        if confidence not in schema["confidence_levels"]:
            report.error(f"{where}: invalid confidence '{confidence}'")


def check_every_entity_is_reachable(entities, report: common.Report) -> None:
    """metadata/relationship-types.md §2.3 — every entity carries at least one
    provenanced relationship, in or out. An entity that connects to nothing is
    invisible in the graph.

    `type: domain` entities are exempt: they are classification nodes carrying
    no factual claims, and are reached by *association* through every entity's
    `domains:` list. They are not weakly connected — the largest nodes in the
    association layer are domains."""
    connected: set[str] = set()
    for e in entities:
        if e.parse_error:
            continue
        own_id = e.frontmatter.get("id")
        for rel in e.frontmatter.get("relationships") or []:
            if not isinstance(rel, dict):
                continue
            target = rel.get("target")
            if target:
                connected.add(own_id)
                connected.add(target)

    for e in entities:
        if e.parse_error:
            continue
        fm = e.frontmatter
        if fm.get("type") == "domain":
            continue  # classification node — see the docstring
        if fm.get("id") not in connected:
            report.error(
                f"{e.rel_path}: no provenanced relationship in either direction — "
                f"every entity must reach its scope anchor "
                f"(metadata/relationship-types.md §2.3). Add the substantive edge, "
                f"or an anchor edge to its country, EU or UN."
            )


def main() -> int:
    schema = common.load_schema()
    entities = common.load_all_entities()
    ids = common.known_ids(entities)

    report = common.Report("validate_relationships")

    for e in entities:
        if e.parse_error:
            continue  # already reported by validate_frontmatter
        check_id_list(e, "organisations", ids, report)
        check_id_list(e, "related_entities", ids, report)
        check_id_list(e, "domains", ids, report)
        check_relationships(e, schema, ids, report)

    check_every_entity_is_reachable(entities, report)

    return report.print_and_exit_code()


if __name__ == "__main__":
    sys.exit(main())
