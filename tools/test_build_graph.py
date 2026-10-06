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

    def test_no_id_or_country_parsed_as_a_yaml_boolean(self):
        """YAML 1.1 resolves NO/YES/ON/OFF/Y/N to booleans, so an unquoted
        `country: NO` silently becomes False and the Norwegian entities
        vanish from every country filter. Caught the hard way when Norway
        was added; `validate_frontmatter` now names the trap explicitly."""
        for e in self.entities:
            for field in ("id", "country"):
                value = e.frontmatter.get(field)
                self.assertNotIsInstance(
                    value, bool,
                    f"{e.rel_path}: '{field}' parsed as the boolean {value} — "
                    f'quote it in the YAML, e.g. {field}: "NO"')

    def test_norway_survives_yaml_parsing(self):
        """The regression this repository actually hit, pinned by name."""
        by_id = {e.frontmatter.get("id"): e for e in self.entities}
        self.assertIn("NO", by_id, "the Norway anchor is missing or its id is not the string 'NO'")
        norwegian = [e for e in self.entities if e.frontmatter.get("country") == "NO"]
        self.assertGreater(len(norwegian), 1,
                           "no entities carry country 'NO' as a string — check for YAML boolean coercion")

    def test_every_entity_reaches_its_scope_anchor(self):
        """metadata/relationship-types.md §2.3 — every entity carries at least
        one provenanced relationship, in or out. Domains are exempt: they are
        classification nodes reached by association through every entity's
        `domains:` list, and are in fact the largest nodes in that layer."""
        connected = set()
        for e in self.entities:
            own = e.frontmatter.get("id")
            for rel in e.frontmatter.get("relationships") or []:
                if isinstance(rel, dict) and rel.get("target"):
                    connected.add(own)
                    connected.add(rel["target"])

        orphans = sorted(
            e.frontmatter["id"] for e in self.entities
            if e.frontmatter.get("type") != "domain"
            and e.frontmatter.get("id") not in connected
        )
        self.assertEqual(
            orphans, [],
            f"entities with no provenanced relationship in either direction: {orphans}")

    def test_domains_are_the_exemption_and_earn_it(self):
        """The domain exemption rests on domains being reached by association.
        If a domain stopped being referenced by any entity's `domains:` list it
        would be genuinely unreachable, and the exemption would be hiding it."""
        referenced = set()
        for e in self.entities:
            for d in e.frontmatter.get("domains") or []:
                referenced.add(d)
        domains = {e.frontmatter["id"] for e in self.entities
                   if e.frontmatter.get("type") == "domain"}
        unreferenced = sorted(domains - referenced)
        self.assertEqual(
            unreferenced, [],
            f"domains referenced by no entity's `domains:` list, so exempt from "
            f"§2.3 and unreachable in both layers: {unreferenced}")

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


class TestGeographicData(unittest.TestCase):
    """Country/region centroids for the site's geographic map layout."""

    @classmethod
    def setUpClass(cls):
        payload, errors, warnings = build_graph.build()
        assert not errors, f"build reported errors: {errors}"
        cls.graph = payload["graph"]

    def test_every_country_facet_carries_a_centroid(self):
        for row in self.graph["facets"]["countries"]:
            self.assertIn(row["code"], build_graph.COUNTRY_CENTROIDS)
            lat, lon = build_graph.COUNTRY_CENTROIDS[row["code"]]
            self.assertEqual(row["lat"], lat, row["code"])
            self.assertEqual(row["lon"], lon, row["code"])
            self.assertTrue(-90 <= row["lat"] <= 90, row["code"])
            self.assertTrue(-180 <= row["lon"] <= 180, row["code"])

    def test_every_region_facet_carries_a_centroid(self):
        for row in self.graph["facets"]["regions"]:
            self.assertIn(row["code"], build_graph.REGION_CENTROIDS)
            lat, lon = build_graph.REGION_CENTROIDS[row["code"]]
            self.assertEqual(row["lat"], lat, row["code"])
            self.assertEqual(row["lon"], lon, row["code"])
            self.assertTrue(-90 <= row["lat"] <= 90, row["code"])
            self.assertTrue(-180 <= row["lon"] <= 180, row["code"])

    def test_country_without_a_centroid_refuses_the_build(self):
        """A country code the map has nowhere to put must not build silently
        into a graph the map view then quietly drops it from."""
        ents = load_all_entities(entities_only=True)
        victim = next(e for e in ents if e.frontmatter.get("country"))
        keep = victim.frontmatter["country"]
        victim.frontmatter["country"] = "ZZ"  # not a real ISO 3166-1 code
        real = build_graph.load_all_entities
        build_graph.load_all_entities = lambda entities_only=True: ents
        try:
            payload, errors, _ = build_graph.build()
            self.assertTrue(errors, "an uncharted country code should be refused")
            self.assertTrue(any("ZZ" in e and "centroid" in e for e in errors))
            self.assertEqual(payload, {}, "no graph should be produced")
        finally:
            victim.frontmatter["country"] = keep
            build_graph.load_all_entities = real

    def test_region_without_a_centroid_refuses_the_build(self):
        ents = load_all_entities(entities_only=True)
        victim = next(e for e in ents if e.frontmatter.get("region"))
        keep = victim.frontmatter["region"]
        victim.frontmatter["region"] = "ZZ"  # not a region this table knows
        real = build_graph.load_all_entities
        build_graph.load_all_entities = lambda entities_only=True: ents
        try:
            payload, errors, _ = build_graph.build()
            self.assertTrue(errors, "an uncharted region code should be refused")
            self.assertTrue(any("ZZ" in e and "centroid" in e for e in errors))
            self.assertEqual(payload, {}, "no graph should be produced")
        finally:
            victim.frontmatter["region"] = keep
            build_graph.load_all_entities = real


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

    def test_build_is_deterministic(self):
        """site/graph.json and site/details.json are not committed: CI and the
        deploy build them from the entity files. That is only safe if the
        build is reproducible, so two builds must agree on everything except
        `generated_at`, which moves on every run."""
        first, errors, _ = build_graph.build()
        self.assertFalse(errors)
        second, errors, _ = build_graph.build()
        self.assertFalse(errors)
        def content(payload, key):
            doc = dict(payload[key])
            doc.pop("generated_at", None)
            return json.dumps(doc, sort_keys=True)

        for key, name in (("graph", "graph.json"), ("details", "details.json")):
            self.assertEqual(content(first, key), content(second, key),
                             f"{name} content differs between two builds of the same data")


class TestLegislationTypes(unittest.TestCase):
    """`law` was split into several types on 2026-10-02. These tests keep the
    schema, the stats, the site and the folder layout in step when a
    legislation type is added or retired."""

    SITE = Path(__file__).resolve().parent.parent / "site"

    @classmethod
    def setUpClass(cls):
        cls.schema = load_schema()
        cls.legislation_types = {
            t for t, folder in cls.schema["type_folder_map"].items()
            if folder == "legislation"
        }

    def test_law_is_retired_and_the_split_types_exist(self):
        self.assertNotIn("law", self.schema["types"])
        self.assertEqual(
            self.legislation_types,
            {"act", "regulation", "directive", "decision",
             "subordinate-legislation", "agreement"})

    def test_soft_law_is_its_own_folder_and_not_counted_as_legislation(self):
        self.assertEqual(self.schema["type_folder_map"]["soft-law"], "soft-law")
        self.assertNotIn("soft-law", self.legislation_types)
        soft = [e for e in load_all_entities() if e.frontmatter.get("type") == "soft-law"]
        self.assertTrue(soft, "no soft-law entity exists")
        for e in soft:
            self.assertEqual(e.path.parent.name, "soft-law", e.frontmatter.get("id"))

    def test_every_schema_type_has_a_folder_and_a_site_shape(self):
        self.assertEqual(set(self.schema["types"]),
                         set(self.schema["type_folder_map"]))
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        block = js[js.index("var TYPE_SHAPE"):]
        block = block[:block.index("};")]
        for t in self.schema["types"]:
            self.assertTrue(t in block or f'"{t}"' in block,
                            f"type {t!r} has no entry in TYPE_SHAPE (site/app.js)")

    def test_legislation_stat_counts_every_legislation_type(self):
        graph, errors, _ = build_graph.build()
        self.assertFalse(errors)
        nodes = graph["graph"]["nodes"]
        expected = sum(1 for n in nodes if n.get("type") in self.legislation_types)
        self.assertEqual(graph["graph"]["stats"]["legislation"], expected)
        self.assertGreater(expected, 0)

    def test_legislation_folder_holds_only_legislation_types(self):
        for e in load_all_entities():
            if e.path.parent.name == "legislation":
                self.assertIn(e.frontmatter.get("type"), self.legislation_types,
                              e.frontmatter.get("id"))


class TestRank(unittest.TestCase):
    """The optional `rank` field (ontology section 1.2)."""

    @classmethod
    def setUpClass(cls):
        import validate_frontmatter
        cls.vf = validate_frontmatter
        cls.schema = load_schema()

    def _errors(self, entity_type, rank, status="active"):
        from common import Report
        report = Report("t")
        self.vf.check_rank("x.md", entity_type, rank, self.schema, report, status)
        return report.errors

    def test_schema_is_coherent(self):
        levels = set(self.schema["rank_levels"])
        legislation = {t for t, f in self.schema["type_folder_map"].items()
                       if f == "legislation"}
        self.assertEqual(set(self.schema["rank_by_type"]), legislation - {"agreement"})
        for entity_type, allowed in self.schema["rank_by_type"].items():
            self.assertTrue(set(allowed) <= levels, entity_type)

    def test_valid_and_unset_ranks_pass(self):
        self.assertEqual(self._errors("act", "organic"), [])
        self.assertEqual(self._errors("act", None), [])
        self.assertEqual(self._errors("subordinate-legislation", "delegated"), [])
        self.assertEqual(self._errors("regulation", "delegated"), [])

    def test_bad_ranks_are_rejected(self):
        self.assertTrue(self._errors("act", "supreme"))                    # unknown value
        self.assertTrue(self._errors("policy", "organic"))                 # wrong type
        self.assertTrue(self._errors("soft-law", "ordinary"))              # no rank on soft law
        self.assertTrue(self._errors("agreement", "ordinary"))             # none on treaties
        self.assertTrue(self._errors("act", "delegated"))                  # an act is not delegated
        self.assertTrue(self._errors("subordinate-legislation", "ordinary"))

    def test_a_bill_has_no_rank_until_enacted(self):
        self.assertTrue(self._errors("act", "ordinary", status="proposed"))
        self.assertTrue(self._errors("act", "ordinary", status="planned"))
        self.assertEqual(self._errors("act", "ordinary", status="adopted"), [])
        self.assertEqual(self._errors("act", None, status="proposed"), [])

    def test_rank_reaches_the_details_payload(self):
        payload, errors, _ = build_graph.build()
        self.assertFalse(errors)
        nodes = payload["details"]["nodes"]
        self.assertEqual(nodes["ES-LOPDGDD"]["rank"], "organic")
        self.assertEqual(nodes["ES-LEY-37-2007"]["rank"], "ordinary")
        self.assertEqual(nodes["DE-BDSG"]["rank"], "ordinary")
        self.assertEqual(nodes["EU-GDPR"]["rank"], "ordinary")
        self.assertEqual(nodes["EU-HVD-REGULATION"]["rank"], "delegated")
        # unset stays unset, never defaulted: a bill, an EU proposal, the UK GDPR
        for unset in ("ES-LCGC", "EU-FIDA", "GB-UK-GDPR"):
            self.assertNotIn("rank", nodes[unset], unset)

    def test_every_country_with_a_ranked_entity_has_a_basis_row(self):
        """metadata/rank-basis.md must say how rank is read for each country."""
        import re
        basis = (Path(__file__).resolve().parent.parent / "metadata" / "rank-basis.md"
                 ).read_text(encoding="utf-8")
        listed = set(re.findall(r"^\| ([A-Z]{2}) \|", basis, re.M))
        missing = {
            e.frontmatter["country"] for e in load_all_entities()
            if e.frontmatter.get("rank") and e.frontmatter.get("country")
        } - listed
        self.assertFalse(missing, f"countries with a rank but no row in rank-basis.md: {sorted(missing)}")

    def test_rank_is_shown_in_the_site(self):
        js = (Path(__file__).resolve().parent.parent / "site" / "app.js").read_text(encoding="utf-8")
        self.assertIn("d.rank", js)


class TestLevels(unittest.TestCase):
    """`level` is a geographic axis. `sectoral` was retired on 2026-10-03
    (discovery/unresolved.md item #228); sector is carried by `domains`."""

    SITE = Path(__file__).resolve().parent.parent / "site"

    @classmethod
    def setUpClass(cls):
        cls.schema = load_schema()

    def test_sectoral_is_retired(self):
        self.assertNotIn("sectoral", self.schema["levels"])
        self.assertEqual(self.schema["levels"],
                         ["international", "regional", "national", "subnational", "local"])
        for e in load_all_entities():
            self.assertNotEqual(e.frontmatter.get("level"), "sectoral", e.frontmatter.get("id"))

    def test_every_level_has_a_band_and_a_colour_in_the_site(self):
        import re
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        css = (self.SITE / "app.css").read_text(encoding="utf-8")
        order = re.search(r"var LEVEL_ORDER = \[(.*?)\];", js).group(1)
        for level in self.schema["levels"]:
            self.assertIn(f'"{level}"', order, f"{level} missing from LEVEL_ORDER")
            self.assertIn(f"--lvl-{level}:", css, f"{level} has no colour in app.css")
        for stale in re.findall(r"--lvl-([a-z]+):", css):
            self.assertIn(stale, self.schema["levels"], f"app.css has a colour for retired level {stale}")


class TestSiteWording(unittest.TestCase):
    """The sidebar is read by people who have never seen the repository. The
    three connection classes used to be labelled with its internals
    ("frontmatter", "Obsidian navigation", "provenanced"); keep them in plain
    words, and keep the Explorer's selection hint tied to the selection."""

    SITE = Path(__file__).resolve().parent.parent / "site"

    def test_connection_labels_use_no_repository_jargon(self):
        import re
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        block = re.search(r"var CLASS_LABEL = \{(.*?)\};", js, re.S).group(1)
        labels = " ".join(re.findall(r':\s*"([^"]*)"', block))  # the text, not the keys
        self.assertTrue(labels)
        for word in ("frontmatter", "Obsidian", "provenanced", "wikilink", "Wikilink"):
            self.assertNotIn(word, labels, f"jargon {word!r} is back in CLASS_LABEL")

    def test_explorer_hint_follows_the_selection(self):
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        self.assertIn("function updateExplorerHint", js)
        # selectEntity must refresh it, or a deep link says "No entity selected"
        body = js[js.index("function selectEntity"):]
        body = body[:body.index("function closeDetail")]
        self.assertIn("updateExplorerHint()", body)

    def test_only_a_chosen_depth_reaches_the_url(self):
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        self.assertIn('if (depthUser !== null) p.set("depth"', js)


class TestStartHere(unittest.TestCase):
    """The "Start here" card links to examples by hash. Every id they name must
    exist, every chain they promise must be a real path, and every one must
    name its view explicitly (only an explicit hash resets the filters)."""

    SITE = Path(__file__).resolve().parent.parent / "site"

    @classmethod
    def setUpClass(cls):
        import re
        js = (cls.SITE / "app.js").read_text(encoding="utf-8")
        block = re.search(r"var START_EXAMPLES = \[(.*?)\n  \];", js, re.S).group(1)
        cls.hashes = re.findall(r'hash:\s*"(#[^"]+)"', block)
        cls.graph, errors, _ = build_graph.build()
        assert not errors
        cls.nodes = {n["id"] for n in cls.graph["graph"]["nodes"]}

    def _params(self, h):
        from urllib.parse import parse_qs
        return {k: v[0] for k, v in parse_qs(h[1:]).items()}

    def test_there_are_examples_and_each_names_its_view(self):
        self.assertGreaterEqual(len(self.hashes), 3)
        for h in self.hashes:
            self.assertIn("view=", h, f"{h} must be an explicit hash, not #ENTITY-ID")

    def test_every_entity_named_exists(self):
        for h in self.hashes:
            p = self._params(h)
            for key in ("focus", "to"):
                if key in p:
                    self.assertTrue(p[key] in self.nodes, f"{h}: {key}={p[key]} is not an entity")
            if "country" in p:
                self.assertTrue(p["country"] in self.nodes, f"{h}: unknown country {p['country']}")

    def test_every_promised_chain_is_a_path_of_typed_relationships(self):
        from collections import deque, defaultdict
        adj = defaultdict(set)
        for e in self.graph["graph"]["edges"]:
            if e["class"] == "relationship":
                adj[e["source"]].add(e["target"]); adj[e["target"]].add(e["source"])
        checked = 0
        for h in self.hashes:
            p = self._params(h)
            if "to" not in p:
                continue
            seen, q = {p["focus"]}, deque([p["focus"]])
            while q:
                x = q.popleft()
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y); q.append(y)
            self.assertTrue(p["to"] in seen, f"{h}: no chain from {p['focus']} to {p['to']}")
            checked += 1
        self.assertTrue(checked, "no example promises a chain any more")


class TestSidebarOrder(unittest.TestCase):
    """The filters people use come first; statistics (once the first thing in
    the sidebar) come last. See docs/ux-analysis.md, point 4."""

    SITE = Path(__file__).resolve().parent.parent / "site"

    def test_panels_are_in_use_order(self):
        import re
        html = (self.SITE / "index.html").read_text(encoding="utf-8")
        ids = re.findall(r'<section class="panel" aria-labelledby="([a-z-]+-h)"', html)
        self.assertEqual(ids, ["explorer-h", "filters-h", "legend-h", "names-h",
                               "edges-h", "layout-h", "stats-h"])

    def test_country_type_and_domain_lead_and_are_open(self):
        import re
        html = (self.SITE / "index.html").read_text(encoding="utf-8")
        panel = html[html.index('aria-labelledby="filters-h"'):html.index('aria-labelledby="legend-h"')]
        details = re.findall(r'<details class="sub"( open)?>\s*<summary>(.*?) <span', panel, re.S)
        self.assertEqual([d[1] for d in details[:3]], ["Country", "Entity type", "Domain"])
        self.assertTrue(all(d[0] for d in details[:3]), "the three lead filters must be open")
        self.assertFalse(any(d[0] for d in details[3:]), "the rest start collapsed")
        for fid in ("f-country", "f-type", "f-domain"):
            self.assertIn(f'class="checks scroll filter-scroll" id="{fid}"', panel)

    def test_filter_badges_exist_and_run_on_refresh(self):
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        self.assertIn("function updateFilterBadges", js)
        body = js[js.index("  function refresh()"):]
        self.assertIn("updateFilterBadges()", body[:200])


class TestSmallFixes(unittest.TestCase):
    """The small items of docs/ux-analysis.md, point 9."""

    SITE = Path(__file__).resolve().parent.parent / "site"
    HTML = (SITE / "index.html").read_text(encoding="utf-8")
    JS = (SITE / "app.js").read_text(encoding="utf-8")

    def test_button_names_contain_their_visible_text(self):
        import re
        # WCAG 2.5.3 (label in name): an aria-label must contain what is shown.
        for m in re.finditer(r'<button[^>]*aria-label="([^"]+)"[^>]*>([^<]+)</button>', self.HTML):
            label, text = m.group(1).lower(), m.group(2).strip().lower()
            if text.replace("-", "").isalpha():  # skip the + and − glyph buttons
                self.assertIn(text, label, "aria-label %r must contain %r" % (m.group(1), text))

    def test_wheel_sensitivity_is_left_at_the_default(self):
        self.assertNotIn("wheelSensitivity", self.JS)

    def test_every_view_has_one_main_landmark(self):
        for vid in ("stage", "listview", "compareview"):
            self.assertRegex(self.HTML, r'<main [^>]*id="%s"' % vid)

    def test_detail_sections_are_h3_under_the_h2_title(self):
        self.assertIn('<div class="d-sec"><h3>', self.JS)
        self.assertNotIn("<h4>", self.JS)

    def test_copy_link_and_data_downloads(self):
        self.assertIn('id="copy-link"', self.HTML)
        self.assertIn("function copyLink", self.JS)
        for name in ("graph.json", "details.json"):
            self.assertIn('<a href="%s" download>' % name, self.HTML)
        # the links must point at what the app itself loads
        self.assertIn('fetch("graph.json"', self.JS)


class TestEnglishNames(unittest.TestCase):
    """The optional `name_en` field and how the site shows it. See
    docs/ux-analysis.md, point 8."""

    SITE = Path(__file__).resolve().parent.parent / "site"

    @classmethod
    def setUpClass(cls):
        import validate_frontmatter
        cls.vf = validate_frontmatter
        cls.entities = [e for e in load_all_entities() if e.frontmatter]

    def _errors(self, name, name_en, aliases=None):
        from common import Report
        report = Report("t")
        if aliases is None:
            aliases = [name_en] if isinstance(name_en, str) else []
        self.vf.check_name_en("x.md", name, name_en, aliases, report)
        return report.errors

    def test_validator(self):
        self.assertEqual(self._errors("Wet digitale overheid", None), [])
        self.assertEqual(self._errors("Wet digitale overheid", "Digital Government Act"), [])
        self.assertTrue(self._errors("Wet digitale overheid", ""))
        self.assertTrue(self._errors("Wet digitale overheid", 5))
        self.assertTrue(self._errors("Wet digitale overheid", " Digital Government Act"))
        self.assertTrue(self._errors("Digital Government Act", "digital government act"))

    def test_name_en_must_also_be_an_alternative_name(self):
        self.assertTrue(self._errors("Wet digitale overheid", "Digital Government Act", ["Wdo"]))
        self.assertEqual(self._errors("Wet digitale overheid", "Digital Government Act",
                                      ["Wdo", "digital government act"]), [])

    def test_every_value_in_the_repository_is_valid(self):
        n = 0
        for e in self.entities:
            fm = e.frontmatter
            if "name_en" in fm:
                n += 1
                self.assertEqual(self._errors(fm.get("name"), fm["name_en"],
                                              fm.get("alternative_names")), [], fm["id"])
        self.assertGreater(n, 100, "the backfill should have set well over a hundred")

    def test_batch_two_values_cite_the_source_they_came_from(self):
        # The 2026-10-06 second pass added 23 names from bodies' own English
        # pages and official translations; each one cites its page in `sources`.
        cited = [e.frontmatter["id"] for e in self.entities
                 if e.frontmatter.get("name_en") and any(
                     str(s.get("accessed")) == "2026-10-06" for s in (e.frontmatter.get("sources") or []))]
        self.assertGreaterEqual(len(cited), 23)

    def test_graph_nodes_carry_name_en(self):
        payload, errors, _ = build_graph.build()
        self.assertFalse(errors)
        graph = payload["graph"]
        with_name = {n["id"] for n in graph["nodes"] if n.get("name_en")}
        expected = {e.frontmatter["id"] for e in self.entities if e.frontmatter.get("name_en")}
        self.assertEqual(with_name, expected)

    def test_site_wiring(self):
        js = (self.SITE / "app.js").read_text(encoding="utf-8")
        html = (self.SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="names-mode"', html)
        self.assertIn("function applyNames", js)
        boot = js[js.index("function boot()"):][:700]
        self.assertIn("applyNames()", boot)
        self.assertIn('params.get("names")', js)
        self.assertIn('p.set("names", nameMode)', js)
        # both names stay searchable whichever is shown
        self.assertIn("[n.label, n.official, n.id].concat(n.name_en", js)
        # the sidebar and the detail panel both say an English name is not
        # necessarily official
        self.assertIn("not necessarily an official translation", html)
        self.assertIn("official translation", js[js.index("function nameNote"):][:700])


class TestMobileLayout(unittest.TestCase):
    """On a phone the top bar is compact, the detail panel is a strip under the
    graph (not a sheet over it) and touch targets are 40 px. See
    docs/ux-analysis.md, point 5."""

    SITE = Path(__file__).resolve().parent.parent / "site"
    CSS = (SITE / "app.css").read_text(encoding="utf-8")
    HTML = (SITE / "index.html").read_text(encoding="utf-8")
    JS = (SITE / "app.js").read_text(encoding="utf-8")

    def phone_block(self):
        start = self.CSS.index("@media (max-width: 860px) {")
        return self.CSS[start:self.CSS.index("@media (max-width: 520px)")]

    def test_detail_is_stacked_under_the_canvas_not_floated_over_it(self):
        block = self.phone_block()
        self.assertIn("flex-direction: column", block)
        detail = block[block.index("  .detail {"):]
        detail = detail[:detail.index("}")]
        self.assertNotIn("position: absolute", detail)
        self.assertIn("max-height: 40%", detail)

    def test_handle_expands_and_reports_state(self):
        self.assertIn('id="detail-expand"', self.HTML)
        self.assertIn('aria-expanded="false" aria-controls="detail-body"', self.HTML)
        self.assertIn("function setDetailExpanded", self.JS)
        close = self.JS[self.JS.index("function closeDetail"):][:200]
        self.assertIn("setDetailExpanded(false)", close)
        # hidden on desktop
        self.assertIn(".detail-handle { display: none; }", self.CSS)

    def test_touch_targets_are_40px(self):
        coarse = self.CSS[self.CSS.index("@media (pointer: coarse)"):]
        for rule in (".view-btn, .icon-btn, .secondary, .mini { min-height: 40px; }",
                     ".check { min-height: 40px;"):
            self.assertIn(rule, coarse)

    def test_sponsor_button_keeps_an_accessible_name(self):
        self.assertIn('<span class="sponsor-text">Sponsor</span>', self.HTML)
        self.assertIn(".sponsor-text { position: absolute;", self.phone_block())


class TestDetailPanel(unittest.TestCase):
    """The detail panel explains the Atlas's own record in plain words and keeps
    long evidence out of the way. See docs/ux-analysis.md, point 7."""

    ROOT = Path(__file__).resolve().parent.parent
    JS = (ROOT / "site" / "app.js").read_text(encoding="utf-8")

    def test_plain_labels_and_iso_dates(self):
        for label in ('"Sourcing"', '"Atlas confidence"', '"Research depth"', '"Last checked"'):
            self.assertIn(label, self.JS)
        for old in ('["Verification"', '["Coverage"', '["Confidence"'):
            self.assertNotIn(old, self.JS)
        self.assertIn('["Last checked", d.last_verified, String', self.JS)
        self.assertIn('["Start date", d.start_date, String', self.JS)

    def test_hint_says_it_describes_the_record(self):
        self.assertIn("not the entity itself", self.JS)
        self.assertIn('sec("About this record"', self.JS)

    def test_evidence_is_collapsed_and_unread_sources_are_flagged(self):
        self.assertIn('<details class="ev"><summary>Evidence</summary>', self.JS)
        self.assertIn("rel-unread", self.JS)
        self.assertIn("function evidenceNotRead", self.JS)

    def test_not_read_marker_still_present_in_data(self):
        # The chip is derived from this wording in the evidence text; if the
        # repository stops writing it, the chip silently disappears.
        hits = sum(1 for f in (self.ROOT / "legislation").glob("*.md")
                   if "NOT READ" in f.read_text(encoding="utf-8"))
        self.assertGreater(hits, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
