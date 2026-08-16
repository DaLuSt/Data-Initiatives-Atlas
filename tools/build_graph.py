#!/usr/bin/env python3
"""Generate the Atlas knowledge graph from the repository's Markdown+YAML.

The repository is the source of truth; `site/graph.json` is a derived
artefact and must never be hand-edited (README §"No manual graph
maintenance"). Regenerate with:

    python tools/build_graph.py

This script deliberately reuses `validation/common.py` as its parser, so
the graph and the validation suite can never disagree about what an entity
file says.

Exit codes: 0 = graph written, 1 = refused (see the reported errors).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "validation"))

from common import (  # noqa: E402  (path set above)
    REPO_ROOT as COMMON_REPO_ROOT,
    load_all_entities,
    load_schema,
)

DEFAULT_OUT = REPO_ROOT / "site" / "graph.json"

# The payload is split so the graph can render before the heavy prose has
# loaded (brief §24: design for 1,000+ nodes). `graph.json` carries only what
# rendering, search and filtering need; `details.json` carries description,
# sources and relationship evidence, fetched in the background and consumed by
# the detail panel.
#
# `aliases` and `domains` deliberately stay in the light payload: search must
# match aliases and domains from the first keystroke (brief §7), so they are
# on the critical path even though the detail panel also uses them.
NODE_DETAIL_FIELDS = (
    "description", "organisations", "sources",
    "confidence", "coverage", "verification", "last_verified",
    "start_date", "end_date", "previous_version", "successor",
)

# Frontmatter fields holding lists of entity IDs. These are associations the
# repository records, not entries in the relationship vocabulary, so they are
# emitted as a separate edge class rather than given an invented type name.
ASSOCIATION_LIST_FIELDS = ("domains", "organisations", "related_entities")

# Frontmatter fields holding a single entity ID (temporal lineage).
ASSOCIATION_SCALAR_FIELDS = ("previous_version", "successor")

# Scope prefixes that are not countries (metadata/ontology.md §2.1).
NON_COUNTRY_SCOPES = {"EU", "UN", "INTL", "DOMAIN"}

# Human-readable country names, filled in from the country anchor entities
# themselves so no country list is ever hard-coded here.


class BuildError(Exception):
    pass


def scope_of(entity_id: str, anchor_ids: set[str]) -> str:
    """ID scope: NL, DE, EU, UN, INTL, DOMAIN ... (metadata/ontology.md §2.1)."""
    if entity_id in anchor_ids:
        return entity_id
    return entity_id.split("-")[0]


def git_default_branch() -> str:
    """Branch that entity links should point at.

    Deliberately NOT the checked-out branch: the graph is built on feature
    branches too, and links baked from a feature branch would 404 once it is
    deleted. Resolution order: ATLAS_BRANCH env var, the remote's default
    branch, then "main".
    """
    override = os.environ.get("ATLAS_BRANCH", "").strip()
    if override:
        return override
    try:
        out = subprocess.run(
            ["git", "symbolic-ref", "--short", "refs/remotes/origin/HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=10,
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip().split("/")[-1]
    except (OSError, subprocess.SubprocessError):
        pass
    return "main"


def git_remote_slug() -> tuple[str, str]:
    """(owner, repo) from the git remote, so GitHub links are never hard-coded."""
    try:
        out = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return ("", "")
    url = out.stdout.strip()
    if not url:
        return ("", "")
    url = url.removesuffix(".git")
    if url.startswith("git@"):
        url = url.split(":", 1)[-1]
    parts = [p for p in url.split("/") if p]
    if len(parts) >= 2:
        return (parts[-2], parts[-1])
    return ("", "")


def compact(mapping: dict) -> dict:
    """Drop empty values — the UI shows only metadata that actually exists
    (brief §7) and the payload stays small (§14)."""
    return {
        k: v for k, v in mapping.items()
        if v is not None and v != [] and v != "" and v != {}
    }


def build(strict_wikilinks: bool = True) -> tuple[dict, list[str], list[str]]:
    """Return (graph, errors, warnings). Never invents a node (brief §27)."""
    errors: list[str] = []
    warnings: list[str] = []

    schema = load_schema()
    anchor_ids = set(schema.get("anchor_ids") or [])
    valid_rel_types = set(schema.get("relationship_types") or [])

    entities = load_all_entities(entities_only=True)
    if not entities:
        raise BuildError("No entity files found — is the repository layout intact?")

    # --- parse + identity ------------------------------------------------
    by_id: dict[str, object] = {}
    for e in entities:
        if e.parse_error:
            errors.append(f"{e.rel_path}: {e.parse_error}")
            continue
        eid = e.frontmatter.get("id")
        if not isinstance(eid, str) or not eid:
            errors.append(f"{e.rel_path}: missing or non-string 'id'")
            continue
        if eid in by_id:
            errors.append(
                f"{e.rel_path}: duplicate id '{eid}' "
                f"(already defined by {by_id[eid].rel_path})"
            )
            continue
        by_id[eid] = e

    if errors:
        return ({}, errors, warnings)

    ids = set(by_id)

    # --- nodes -----------------------------------------------------------
    nodes = []
    for eid, e in sorted(by_id.items()):
        fm = e.frontmatter
        sources = []
        for s in fm.get("sources") or []:
            if isinstance(s, dict):
                sources.append(compact({
                    "title": s.get("title"),
                    "url": s.get("url"),
                    "publisher": s.get("publisher"),
                }))
        nodes.append(compact({
            "id": eid,
            "label": fm.get("name") or eid,
            "type": fm.get("type"),
            "level": fm.get("level"),
            "country": fm.get("country"),
            "region": fm.get("region"),
            "scope": scope_of(eid, anchor_ids),
            "status": fm.get("status"),
            "description": (fm.get("description") or "").strip() or None,
            "aliases": [a for a in (fm.get("alternative_names") or []) if a],
            "domains": list(fm.get("domains") or []),
            "organisations": list(fm.get("organisations") or []),
            "confidence": fm.get("confidence"),
            "coverage": fm.get("coverage"),
            "verification": fm.get("verification"),
            "last_verified": str(fm.get("last_verified")) if fm.get("last_verified") else None,
            "start_date": str(fm.get("start_date")) if fm.get("start_date") else None,
            "end_date": str(fm.get("end_date")) if fm.get("end_date") else None,
            "previous_version": fm.get("previous_version"),
            "successor": fm.get("successor"),
            "sources": sources,
            "path": e.rel_path.replace("\\", "/"),
        }))

    # --- edges -----------------------------------------------------------
    edges = []
    seen_edges: set[tuple] = set()

    def add_edge(src, tgt, etype, cls, extra=None):
        key = (src, tgt, etype, cls)
        if key in seen_edges:
            return
        seen_edges.add(key)
        edge = {"source": src, "target": tgt, "class": cls}
        if etype:
            edge["type"] = etype
        if extra:
            edge.update(compact(extra))
        edges.append(edge)

    for eid, e in sorted(by_id.items()):
        fm = e.frontmatter
        where = e.rel_path

        # 1. Typed, directed, provenanced relationships — the canonical edges.
        for i, rel in enumerate(fm.get("relationships") or []):
            loc = f"{where}: relationships[{i}]"
            if not isinstance(rel, dict):
                errors.append(f"{loc}: not a mapping")
                continue
            rtype, target = rel.get("type"), rel.get("target")
            if not rtype:
                errors.append(f"{loc}: missing 'type'")
                continue
            if rtype not in valid_rel_types:
                errors.append(f"{loc}: unknown relationship type '{rtype}'")
                continue
            if not target:
                errors.append(f"{loc}: missing 'target'")
                continue
            if target == eid:
                errors.append(f"{loc}: target is the entity itself")
                continue
            if target not in ids:
                # Never fabricate a node for a dangling target (brief §27).
                errors.append(
                    f"{loc}: target '{target}' does not resolve to a known entity "
                    f"— refusing to invent a node for it"
                )
                continue
            add_edge(eid, target, rtype, "relationship", {
                "provenance": rel.get("source"),
                "confidence": rel.get("confidence"),
                "evidence": rel.get("evidence"),
                "valid_from": str(rel["valid_from"]) if rel.get("valid_from") else None,
                "valid_until": str(rel["valid_until"]) if rel.get("valid_until") else None,
            })

        # 2. Associations the frontmatter records as ID lists/scalars. These
        #    carry no type from the relationship vocabulary, so the emitted
        #    edge names the *field* it came from rather than inventing a type.
        for field in ASSOCIATION_LIST_FIELDS:
            for target in fm.get(field) or []:
                if target == eid or target not in ids:
                    if target not in ids:
                        errors.append(
                            f"{where}: {field} entry '{target}' does not resolve "
                            f"to a known entity — refusing to invent a node for it"
                        )
                    continue
                add_edge(eid, target, None, "association", {"field": field})

        for field in ASSOCIATION_SCALAR_FIELDS:
            target = fm.get(field)
            if not target:
                continue
            if target not in ids:
                errors.append(
                    f"{where}: {field} '{target}' does not resolve to a known "
                    f"entity — refusing to invent a node for it"
                )
                continue
            if target == eid:
                errors.append(f"{where}: {field} points at the entity itself")
                continue
            add_edge(eid, target, None, "association", {"field": field})

        # 3. Wikilinks authored in the body — navigational, Obsidian's view.
        for target in dict.fromkeys(e.wikilinks):
            if target == eid:
                continue
            if target not in ids:
                msg = f"{where}: wikilink [[{target}]] does not resolve to a known entity"
                (errors if strict_wikilinks else warnings).append(msg)
                continue
            add_edge(eid, target, None, "wikilink")

    if errors:
        return ({}, errors, warnings)

    # --- degrees (used for level-of-detail rendering) --------------------
    degree = Counter()
    rel_degree = Counter()
    for edge in edges:
        degree[edge["source"]] += 1
        degree[edge["target"]] += 1
        if edge["class"] == "relationship":
            rel_degree[edge["source"]] += 1
            rel_degree[edge["target"]] += 1
    for n in nodes:
        n["degree"] = degree.get(n["id"], 0)
        n["rel_degree"] = rel_degree.get(n["id"], 0)

    # --- facets, discovered from the data, never hard-coded --------------
    country_names: dict[str, str] = {}
    for n in nodes:
        if n.get("type") == "country":
            country_names[n["id"]] = n.get("label") or n["id"]

    country_counts = Counter(n["country"] for n in nodes if n.get("country"))
    for code in country_counts:
        country_names.setdefault(code, code)

    region_counts = Counter(n["region"] for n in nodes if n.get("region"))
    scope_counts = Counter(n["scope"] for n in nodes)

    # Domain labels come from the domain entities themselves, exactly as
    # country labels come from country entities. A domain tagged on an entity
    # but never created as an entity still gets a facet row, labelled by its
    # id — the facet reports what the data says rather than hiding the gap.
    domain_names: dict[str, str] = {}
    for n in nodes:
        if n.get("type") == "domain":
            domain_names[n["id"]] = n.get("label") or n["id"]

    domain_counts = Counter(d for n in nodes for d in (n.get("domains") or []))
    for code in domain_counts:
        domain_names.setdefault(code, code)

    facets = {
        "countries": [
            {"code": c, "label": country_names.get(c, c), "count": n}
            for c, n in sorted(country_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
        "regions": [
            {"code": r, "count": n}
            for r, n in sorted(region_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
        "scopes": [
            {"code": s, "count": n, "is_country": s not in NON_COUNTRY_SCOPES}
            for s, n in sorted(scope_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
        "levels": [
            {"code": lv, "count": n} for lv, n in
            sorted(Counter(x["level"] for x in nodes if x.get("level")).items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
        "types": [
            {"code": t, "count": n} for t, n in
            sorted(Counter(x["type"] for x in nodes if x.get("type")).items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
        "statuses": [
            {"code": s, "count": n} for s, n in
            sorted(Counter(x["status"] for x in nodes if x.get("status")).items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
        "relationship_types": [
            {"code": t, "count": n} for t, n in
            sorted(Counter(e["type"] for e in edges if e["class"] == "relationship").items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
        "association_fields": [
            {"code": f, "count": n} for f, n in
            sorted(Counter(e.get("field") for e in edges
                           if e["class"] == "association" and e.get("field")).items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
        # Domains are the cross-cutting axis (metadata/taxonomy.md §1.1):
        # "what connects to Cybersecurity?" regardless of type, level or
        # country. The label comes from the domain entity itself so the
        # facet never hard-codes a name.
        "domains": [
            {"code": d, "label": domain_names.get(d, d), "count": n}
            for d, n in sorted(domain_counts.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
        # Provenance and confidence come off relationship edges. They are
        # what makes the Atlas auditable: a reader can isolate the Atlas's
        # own interpretations from sourced facts.
        "provenances": [
            {"code": p, "count": n} for p, n in
            sorted(Counter(e["provenance"] for e in edges
                           if e["class"] == "relationship" and e.get("provenance")).items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
        "confidences": [
            {"code": c, "count": n} for c, n in
            sorted(Counter(e["confidence"] for e in edges
                           if e["class"] == "relationship" and e.get("confidence")).items(),
                   key=lambda kv: (-kv[1], kv[0]))
        ],
    }

    by_class = Counter(e["class"] for e in edges)
    by_type = Counter(n["type"] for n in nodes if n.get("type"))
    stats = {
        "entities": len(nodes),
        "relationships": by_class.get("relationship", 0),
        "associations": by_class.get("association", 0),
        "wikilinks": by_class.get("wikilink", 0),
        "edges_total": len(edges),
        "countries": len(country_counts),
        "regions": len(region_counts),
        "organisations": by_type.get("organisation", 0),
        "standards": by_type.get("standard", 0),
        "initiatives": by_type.get("initiative", 0),
        "legislation": sum(by_type.get(t, 0) for t in ("law", "regulation", "directive")),
        "frameworks": by_type.get("framework", 0),
        "data_spaces": by_type.get("data-space", 0),
        "domains": by_type.get("domain", 0),
        "provenance_fact": sum(
            1 for e in edges
            if e["class"] == "relationship" and e.get("provenance") == "fact"
        ),
        "provenance_interpretation": sum(
            1 for e in edges
            if e["class"] == "relationship" and e.get("provenance") == "interpretation"
        ),
    }

    # --- split the payload ----------------------------------------------
    details: dict[str, dict] = {}
    light_nodes = []
    for n in nodes:
        detail = {k: n[k] for k in NODE_DETAIL_FIELDS if k in n}
        if detail:
            details[n["id"]] = detail
        light_nodes.append({
            k: v for k, v in n.items() if k not in NODE_DETAIL_FIELDS
        })

    edge_details: dict[str, dict] = {}
    light_edges = []
    for edge in edges:
        heavy = {k: edge[k] for k in ("evidence", "valid_from", "valid_until")
                 if k in edge}
        light = {k: v for k, v in edge.items()
                 if k not in ("evidence", "valid_from", "valid_until")}
        if heavy:
            key = f"{edge['source']}|{edge['target']}|{edge.get('type', '')}"
            edge_details[key] = heavy
        light_edges.append(light)

    owner, repo = git_remote_slug()
    graph = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "tools/build_graph.py",
        "source_of_truth": "Markdown + YAML in this repository — do not hand-edit this file",
        "repository": compact({
            "owner": owner, "name": repo, "branch": git_default_branch(),
        }),
        "vocabularies": {
            "types": schema.get("types", []),
            "levels": schema.get("levels", []),
            "statuses": schema.get("statuses", []),
            "relationship_types": schema.get("relationship_types", []),
            "edge_classes": ["relationship", "association", "wikilink"],
        },
        "facets": facets,
        "stats": stats,
        "nodes": light_nodes,
        "edges": light_edges,
    }
    detail_payload = {
        "generated_at": graph["generated_at"],
        "nodes": details,
        "edges": edge_details,
    }
    return ({"graph": graph, "details": detail_payload}, errors, warnings)


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate site/graph.json from the Atlas.")
    ap.add_argument("-o", "--out", type=Path, default=DEFAULT_OUT,
                    help=f"output path (default: {DEFAULT_OUT.relative_to(REPO_ROOT)})")
    ap.add_argument("--indent", type=int, default=None,
                    help="pretty-print with this indent (default: compact)")
    ap.add_argument("--lenient-wikilinks", action="store_true",
                    help="downgrade unresolved body wikilinks from error to warning")
    ap.add_argument("--check", action="store_true",
                    help="build and report, but do not write the file")
    args = ap.parse_args()

    if COMMON_REPO_ROOT != REPO_ROOT:
        print(f"ERROR: parser root {COMMON_REPO_ROOT} != {REPO_ROOT}", file=sys.stderr)
        return 1

    try:
        payload, errors, warnings = build(strict_wikilinks=not args.lenient_wikilinks)
    except BuildError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1

    for w in warnings:
        print(f"  WARN  {w}")
    if errors:
        for e in errors:
            print(f"  ERROR {e}", file=sys.stderr)
        print(f"\nbuild_graph: refused — {len(errors)} error(s). "
              f"Graph NOT written.", file=sys.stderr)
        return 1

    graph, detail_payload = payload["graph"], payload["details"]
    s = graph["stats"]
    print(f"build_graph: {s['entities']} entities, {s['edges_total']} edges "
          f"({s['relationships']} relationship, {s['associations']} association, "
          f"{s['wikilinks']} wikilink)")
    print(f"             {s['countries']} countries, {s['regions']} region(s), "
          f"{len(graph['facets']['types'])} entity types in use")
    if warnings:
        print(f"             {len(warnings)} warning(s)")

    if args.check:
        print("build_graph: --check given, file not written.")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    details_out = args.out.with_name("details.json")

    for path, data in ((args.out, graph), (details_out, detail_payload)):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=args.indent,
                      separators=(",", ":") if args.indent is None else None)
            f.write("\n")
        print(f"build_graph: wrote {path.relative_to(REPO_ROOT)} "
              f"({path.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
