#!/usr/bin/env python3
"""Tests for the Atlas graph generator (brief §28).

Run with:  python tools/test_build_graph.py

Deliberately dependency-free (no pytest) so it runs anywhere the validation
suite runs. Covers data parsing, graph generation, relationship direction and
the refusal behaviour that stops a malformed repository producing a graph.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "validation"))

import build_graph  # noqa: E402
from common import load_all_entities, load_schema  # noqa: E402


class TestDataParsing(unittest.TestCase):
    """§28 — YAML parses, Markdown discovered, IDs unique."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_all_entities(entities_only=True)

    def test_entity_files_discovered(self):
        self.assertGreater(len(self.entities), 0, "no entity Markdown files found")

    def test_all_yaml_parses(self):
        broken = [(e.rel_path, e.parse_error) for e in self.entities if e.parse_error]
        self.assertEqual(broken, [], f"frontmatter failed to parse: {broken}")

    def test_ids_unique(self):
        seen = {}
        for e in self.entities:
            eid = e.frontmatter["id"]
            self.assertNotIn(eid, seen, f"duplicate id {eid}: {e.rel_path} / {seen.get(eid)}")
            seen[eid] = e.rel_path

    def test_every_entity_has_required_fields(self):
        required = load_schema()["required_fields"]
        for e in self.entities:
            for field in required:
                self.assertIn(field, e.frontmatter,
                              f"{e.rel_path} missing required field '{field}'")


class TestGraphGeneration(unittest.TestCase):
    """§28 — nodes, relationships and direction."""

    @classmethod
    def setUpClass(cls):
        payload, errors, warnings = build_graph.build()
        assert not errors, f"build reported errors: {errors}"
        cls.graph = payload["graph"]
        cls.details = payload["details"]
        cls.entities = load_all_entities(entities_only=True)

    def test_node_per_entity(self):
        self.assertEqual(len(self.graph["nodes"]), len(self.entities))

    def test_node_ids_match_repository(self):
        self.assertEqual(
            {n["id"] for n in self.graph["nodes"]},
            {e.frontmatter["id"] for e in self.entities},
        )

    def test_edges_generated(self):
        self.assertGreater(len(self.graph["edges"]), 0)
        classes = {e["class"] for e in self.graph["edges"]}
        self.assertEqual(classes, {"relationship", "association", "wikilink"})

    def test_every_relationship_becomes_an_edge(self):
        """Every frontmatter relationship must appear, in its own direction."""
        want = set()
        for e in self.entities:
            for rel in e.frontmatter.get("relationships") or []:
                want.add((e.frontmatter["id"], rel["target"], rel["type"]))
        got = {
            (x["source"], x["target"], x.get("type"))
            for x in self.graph["edges"] if x["class"] == "relationship"
        }
        self.assertEqual(want - got, set(), "relationships missing from the graph")

    def test_relationship_direction_is_preserved(self):
        """§5 — a directed relationship must not be flipped or symmetrised."""
        rel_edges = [e for e in self.graph["edges"] if e["class"] == "relationship"]
        pairs = {(e["source"], e["target"], e.get("type")) for e in rel_edges}
        for e in self.entities:
            src = e.frontmatter["id"]
            for rel in e.frontmatter.get("relationships") or []:
                fwd = (src, rel["target"], rel["type"])
                rev = (rel["target"], src, rel["type"])
                self.assertIn(fwd, pairs)
                # The reverse may exist only if the repository itself declares
                # it on the other entity — never as a generator side effect.
                if rev in pairs:
                    other = next(x for x in self.entities
                                 if x.frontmatter["id"] == rel["target"])
                    declared = any(
                        r.get("target") == src and r.get("type") == rel["type"]
                        for r in other.frontmatter.get("relationships") or []
                    )
                    self.assertTrue(
                        declared,
                        f"generator invented a reverse edge {rev}",
                    )

    def test_relationship_types_are_from_the_vocabulary(self):
        """§4 — no invented relationship types."""
        allowed = set(load_schema()["relationship_types"])
        for e in self.graph["edges"]:
            if e["class"] == "relationship":
                self.assertIn(e.get("type"), allowed)

    def test_association_edges_name_their_source_field(self):
        """Associations carry the frontmatter field, not an invented type."""
        fields = {e.get("field") for e in self.graph["edges"] if e["class"] == "association"}
        self.assertTrue(fields <= set(
            build_graph.ASSOCIATION_LIST_FIELDS + build_graph.ASSOCIATION_SCALAR_FIELDS
        ), f"unexpected association fields: {fields}")
        for e in self.graph["edges"]:
            if e["class"] == "association":
                self.assertNotIn("type", e, "association edge must not claim a relationship type")

    def test_no_edge_endpoint_is_a_phantom_node(self):
        """§27 — never fabricate a node for an unresolved reference."""
        ids = {n["id"] for n in self.graph["nodes"]}
        for e in self.graph["edges"]:
            self.assertIn(e["source"], ids)
            self.assertIn(e["target"], ids)

    def test_no_self_loops(self):
        for e in self.graph["edges"]:
            self.assertNotEqual(e["source"], e["target"])

    def test_no_metadata_became_a_node(self):
        """§3 — status/confidence/coverage etc. are properties, not entities."""
        types = {n.get("type") for n in self.graph["nodes"]}
        self.assertTrue(types <= set(load_schema()["types"]))
        ids = {n["id"] for n in self.graph["nodes"]}
        for forbidden in ("active", "medium", "high", "search-only", "fact"):
            self.assertNotIn(forbidden, ids)

    def test_countries_discovered_dynamically(self):
        """§6/§8 — countries come from the data, never hard-coded."""
        from_data = {
            e.frontmatter["country"] for e in self.entities
            if e.frontmatter.get("country")
        }
        from_graph = {c["code"] for c in self.graph["facets"]["countries"]}
        self.assertEqual(from_data, from_graph)
        self.assertGreaterEqual(len(from_graph), 2,
                                "expected at least two countries in this Atlas")

    def test_country_labels_come_from_anchor_entities(self):
        labels = {c["code"]: c["label"] for c in self.graph["facets"]["countries"]}
        anchors = {
            e.frontmatter["id"]: e.frontmatter["name"]
            for e in self.entities if e.frontmatter.get("type") == "country"
        }
        for code, name in anchors.items():
            self.assertEqual(labels.get(code), name)

    def test_domains_discovered_dynamically(self):
        """taxonomy.md §1.1 — the domain facet is the cross-cutting axis."""
        from_data = {
            d for e in self.entities
            for d in (e.frontmatter.get("domains") or [])
        }
        from_graph = {d["code"] for d in self.graph["facets"]["domains"]}
        self.assertEqual(from_data, from_graph)

    def test_domain_labels_come_from_domain_entities(self):
        """A domain facet row is named by its entity, not by its id."""
        labels = {d["code"]: d["label"] for d in self.graph["facets"]["domains"]}
        domains = {
            e.frontmatter["id"]: e.frontmatter["name"]
            for e in self.entities if e.frontmatter.get("type") == "domain"
        }
        self.assertTrue(domains, "expected at least one domain entity")
        for code, name in domains.items():
            if code in labels:          # a domain nobody tags has no facet row
                self.assertEqual(labels[code], name)

    def test_domain_counts_match_the_tagging(self):
        for row in self.graph["facets"]["domains"]:
            tagged = sum(
                1 for e in self.entities
                if row["code"] in (e.frontmatter.get("domains") or [])
            )
            self.assertEqual(row["count"], tagged, row["code"])

    def test_provenance_and_confidence_facets_are_relationship_only(self):
        """Only typed relationships carry provenance and confidence."""
        rels = [e for e in self.graph["edges"] if e["class"] == "relationship"]
        for facet, key in (("provenances", "provenance"), ("confidences", "confidence")):
            rows = self.graph["facets"][facet]
            self.assertTrue(rows, f"{facet} facet is empty")
            self.assertEqual(
                sum(r["count"] for r in rows),
                sum(1 for e in rels if e.get(key)),
                f"{facet} counts must total the relationship edges carrying {key}",
            )
            for row in rows:
                self.assertEqual(
                    row["count"],
                    sum(1 for e in rels if e.get(key) == row["code"]),
                    row["code"],
                )

    def test_provenance_and_confidence_use_the_controlled_vocabulary(self):
        schema = load_schema()
        self.assertTrue(
            {r["code"] for r in self.graph["facets"]["provenances"]}
            <= set(schema["relationship_source_values"])
        )
        self.assertTrue(
            {r["code"] for r in self.graph["facets"]["confidences"]}
            <= set(schema["confidence_levels"])
        )

    def test_levels_cover_the_schema_vocabulary(self):
        allowed = set(load_schema()["levels"])
        used = {lv["code"] for lv in self.graph["facets"]["levels"]}
        self.assertTrue(used <= allowed, f"unknown level(s): {used - allowed}")

    def test_stats_are_computed_not_hardcoded(self):
        """§25 — statistics must match the data."""
        s = self.graph["stats"]
        self.assertEqual(s["entities"], len(self.graph["nodes"]))
        self.assertEqual(s["edges_total"], len(self.graph["edges"]))
        self.assertEqual(
            s["relationships"],
            sum(1 for e in self.graph["edges"] if e["class"] == "relationship"),
        )
        self.assertEqual(
            s["organisations"],
            sum(1 for n in self.graph["nodes"] if n.get("type") == "organisation"),
        )
        self.assertEqual(s["countries"], len(self.graph["facets"]["countries"]))

    def test_generated_at_present_and_iso(self):
        """§26 — generation date is produced, not hard-coded."""
        from datetime import datetime
        stamp = self.graph["generated_at"]
        datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ")

    def test_payload_split_keeps_graph_light(self):
        """§24 — the render-critical file must not carry the prose."""
        for n in self.graph["nodes"]:
            self.assertNotIn("description", n)
            self.assertNotIn("sources", n)
        for e in self.graph["edges"]:
            self.assertNotIn("evidence", e)
        # ...and the detail file must actually carry it.
        self.assertTrue(any("description" in d for d in self.details["nodes"].values()))

    def test_search_fields_stay_on_the_critical_path(self):
        """Aliases and domains are needed by search before details.json lands."""
        light = {n["id"]: n for n in self.graph["nodes"]}
        with_alias = [e for e in self.entities if e.frontmatter.get("alternative_names")]
        self.assertTrue(with_alias)
        self.assertIn("aliases", light[with_alias[0].frontmatter["id"]])

    def test_every_node_has_a_repo_path(self):
        """§19 — two-way navigation needs a real file path per node."""
        for n in self.graph["nodes"]:
            self.assertIn("path", n)
            self.assertTrue((REPO_ROOT / n["path"]).is_file(), f"missing {n['path']}")

    def test_detail_edge_keys_resolve(self):
        keys = {f"{e['source']}|{e['target']}|{e.get('type', '')}"
                for e in self.graph["edges"]}
        for key in self.details["edges"]:
            self.assertIn(key, keys)


class TestRefusalBehaviour(unittest.TestCase):
    """§27 — malformed metadata is reported, never silently ignored."""

    def _build_with(self, tmp_entities):
        """Run build() against a patched entity list."""
        real = build_graph.load_all_entities
        build_graph.load_all_entities = lambda entities_only=True: tmp_entities
        try:
            return build_graph.build()
        finally:
            build_graph.load_all_entities = real

    def _entities(self):
        return load_all_entities(entities_only=True)

    def test_dangling_relationship_target_is_refused(self):
        ents = self._entities()
        victim = next(e for e in ents if e.frontmatter.get("relationships"))
        original = json.dumps(victim.frontmatter["relationships"][0]["target"])
        victim.frontmatter["relationships"][0]["target"] = "NO-SUCH-ENTITY"
        try:
            payload, errors, _ = self._build_with(ents)
            self.assertTrue(errors, "dangling target should be an error")
            self.assertTrue(any("NO-SUCH-ENTITY" in e for e in errors))
            self.assertTrue(any("refusing to invent" in e for e in errors))
            self.assertEqual(payload, {}, "no graph should be produced")
        finally:
            victim.frontmatter["relationships"][0]["target"] = json.loads(original)

    def test_unknown_relationship_type_is_refused(self):
        ents = self._entities()
        victim = next(e for e in ents if e.frontmatter.get("relationships"))
        keep = victim.frontmatter["relationships"][0]["type"]
        victim.frontmatter["relationships"][0]["type"] = "invented-by-the-generator"
        try:
            _, errors, _ = self._build_with(ents)
            self.assertTrue(any("unknown relationship type" in e for e in errors))
        finally:
            victim.frontmatter["relationships"][0]["type"] = keep

    def test_duplicate_id_is_refused(self):
        ents = self._entities()
        clash = ents[1].frontmatter["id"]
        keep = ents[0].frontmatter["id"]
        ents[0].frontmatter["id"] = clash
        try:
            _, errors, _ = self._build_with(ents)
            self.assertTrue(any("duplicate id" in e for e in errors))
        finally:
            ents[0].frontmatter["id"] = keep

    def test_malformed_frontmatter_is_refused(self):
        with tempfile.TemporaryDirectory() as td:
            bad = Path(td) / "broken.md"
            bad.write_text("---\nid: X\n  bad: [unclosed\n---\nbody\n", encoding="utf-8")
            from common import parse_entity_file
            parsed = parse_entity_file(bad)
            self.assertIsNotNone(parsed.parse_error)

    def test_unresolved_wikilink_is_reported(self):
        ents = self._entities()
        victim = ents[0]
        keep = list(victim.wikilinks)
        victim.wikilinks.append("GHOST-ENTITY")
        try:
            _, errors, _ = self._build_with(ents)
            self.assertTrue(any("GHOST-ENTITY" in e for e in errors))
        finally:
            victim.wikilinks[:] = keep


class TestSiteArtefacts(unittest.TestCase):
    """The deployed site must be self-contained and free of stale data."""

    SITE = REPO_ROOT / "site"

    def test_site_files_exist(self):
        for f in ("index.html", "app.css", "app.js", "vendor/cytoscape.min.js"):
            self.assertTrue((self.SITE / f).is_file(), f"missing site/{f}")

    def test_no_external_script_or_style_references(self):
        """§13/§15 — must work as a static site with no third-party fetches."""
        html = (self.SITE / "index.html").read_text(encoding="utf-8")
        import re
        for m in re.finditer(r'<(?:script|link)[^>]*?(?:src|href)="([^"]+)"', html):
            url = m.group(1)
            if url.startswith(("http://", "https://", "//")):
                self.fail(f"external asset referenced in index.html: {url}")

    def test_generated_graph_matches_repository(self):
        """The committed graph.json must not drift from the source of truth."""
        path = self.SITE / "graph.json"
        if not path.exists():
            self.skipTest("site/graph.json not built yet")
        committed = json.loads(path.read_text(encoding="utf-8"))
        payload, errors, _ = build_graph.build()
        self.assertFalse(errors)
        fresh = payload["graph"]
        hint = "site/graph.json is stale — run `python tools/build_graph.py`"
        # Compare content, not the whole file: `generated_at` moves on every
        # build, so a byte/timestamp comparison would always report staleness.
        self.assertEqual(committed["stats"], fresh["stats"], hint)
        self.assertEqual(committed["facets"], fresh["facets"], hint)
        self.assertEqual(committed["repository"], fresh["repository"], hint)
        self.assertEqual(
            sorted(json.dumps(n, sort_keys=True) for n in committed["nodes"]),
            sorted(json.dumps(n, sort_keys=True) for n in fresh["nodes"]),
            hint,
        )
        self.assertEqual(
            sorted(json.dumps(e, sort_keys=True) for e in committed["edges"]),
            sorted(json.dumps(e, sort_keys=True) for e in fresh["edges"]),
            hint,
        )

    def test_committed_details_match_repository(self):
        path = self.SITE / "details.json"
        if not path.exists():
            self.skipTest("site/details.json not built yet")
        committed = json.loads(path.read_text(encoding="utf-8"))
        payload, errors, _ = build_graph.build()
        self.assertFalse(errors)
        self.assertEqual(committed["nodes"], payload["details"]["nodes"],
                         "site/details.json is stale — run `python tools/build_graph.py`")
        self.assertEqual(committed["edges"], payload["details"]["edges"],
                         "site/details.json is stale — run `python tools/build_graph.py`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
