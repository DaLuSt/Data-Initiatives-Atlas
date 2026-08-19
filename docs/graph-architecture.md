# Graph Architecture

How the Atlas's Markdown and YAML become an interactive graph, and why the
design is what it is.

```
                    Git repository
                          │
                 Markdown + YAML  ← the source of truth
                          │
                          ▼
            tools/build_graph.py  ← the only generator
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
     site/graph.json            site/details.json
     (structure, light)         (prose, lazy)
            │                           │
            └─────────────┬─────────────┘
                          ▼
                  site/index.html
                   + app.js/app.css
                   + vendor/cytoscape.min.js
                          │
                          ▼
                    GitHub Pages
```

---

## 1. One parser, not two

`tools/build_graph.py` imports `validation/common.py` and uses its
`load_all_entities()` and `parse_entity_file()`.

This is deliberate. A second, independent Markdown/YAML parser is the
obvious way to introduce a class of bug where validation passes and the
graph disagrees — or worse, where the graph quietly renders something the
validators would have rejected. Sharing the parser makes that impossible by
construction.

It also means the graph automatically respects the repository's own notions
of what counts as an entity file (`FLAT_ENTITY_DIRS`, `GEOGRAPHY_ROOTS`,
`NON_ENTITY_FILENAMES`, `EXCLUDE_DIR_NAMES`).

---

## 2. How data becomes nodes

One entity file → one node. Nothing else becomes a node.

| Node field | Comes from |
|---|---|
| `id` | `id` |
| `label` | `name` |
| `type` | `type` |
| `level` | `level` |
| `country`, `region` | `country`, `region` |
| `scope` | the ID prefix (`NL-`, `DE-`, `EU-`, `UN-`, `INTL-`, `DOMAIN-`), or the ID itself for anchors |
| `status` | `status` |
| `aliases` | `alternative_names` |
| `domains` | `domains` |
| `path` | the file's repository-relative path, used for GitHub links |
| `degree`, `rel_degree` | computed — total edges, and typed-relationship edges |

**Metadata never becomes a node.** `status`, `confidence`, `coverage`,
`verification`, `sources`, `last_verified`, `start_date` and `end_date` are
properties of an entity, so they are properties of a node. There is no
"Active" node and no "medium" node. `tools/test_build_graph.py` asserts
this.

`domains` is the one case that could look like an exception, and is not:
domain entities are real entity files in `domains/` with their own
frontmatter, so they are nodes because they are entities, not because they
appear in a list.

---

## 3. How relationships become edges

The repository records links in three different ways, and the graph keeps
all three as separate **edge classes** rather than merging them.

### `relationship` — the canonical edges

From the `relationships:` block:

```yaml
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "The BDSG was adopted as part of …"
    confidence: medium
```

becomes

```json
{"source":"DE-BDSG","target":"EU-GDPR","class":"relationship",
 "type":"implements-requirement-from","provenance":"fact","confidence":"medium"}
```

with `evidence` and validity dates moved to `details.json`.

- **The type must be in `metadata/schema.json` → `relationship_types`.** An
  unknown type is an error, not a new edge type. The generator never invents
  a relationship.
- **Direction is preserved exactly.** The edge runs from the entity that
  declares it to its `target`. No inverse edge is ever synthesised — if both
  directions exist in the graph, both were declared in the repository. There
  is a test for precisely this.

### `association` — links the repository records without typing

From `domains:`, `organisations:`, `related_entities:`, `previous_version:`
and `successor:`.

These are genuine references in the data, but they carry no entry from the
relationship vocabulary. Rather than invent type names for them (which §4 of
the brief forbids), each association edge records the **frontmatter field it
came from**:

```json
{"source":"DE-DNG","target":"DE-IWG","class":"association","field":"previous_version"}
```

So the UI can say "this came from the `previous_version` field" — which is
true — instead of "this is a `supersedes` relationship" — which would be an
assertion the data does not make.

### `wikilink` — the Obsidian view

`[[LINKS]]` in the entity body. Navigational rather than semantic, drawn
faintly, off by default. This is what makes the web graph and the Obsidian
graph comparable: Obsidian's local graph is built from exactly these.

### Why the separation matters

Merging the three would triple the apparent connectivity of the Atlas and
destroy the distinction between "a sourced, provenanced claim" and "these
two entities are mentioned together". The default view shows only the 346
typed relationships; the other 2,074 edges are one checkbox away.

---

## 4. Refusing rather than fabricating

`build_graph.py` exits non-zero and writes nothing if it finds:

- frontmatter that does not parse;
- a missing or non-string `id`;
- a duplicate `id`;
- a relationship with no `type`, an unknown `type`, or no `target`;
- a relationship, association or wikilink whose target does not resolve to a
  known entity;
- a relationship or lineage field pointing at its own entity.

The unresolved-target case is the important one. The tempting behaviour is
to create a placeholder node so the graph still renders. The generator
refuses, and says so:

```
ERROR legislation/de-bdsg.md: relationships[0]: target 'NO-SUCH-ENTITY' does not
      resolve to a known entity — refusing to invent a node for it
```

A phantom node would be an entity the Atlas does not contain, appearing in a
view of the Atlas. `tools/test_build_graph.py` injects each of these faults
and asserts the build refuses.

---

## 5. The payload split

`graph.json` carries what rendering, search and filtering need.
`details.json` carries description text, sources and relationship evidence.

|  | `graph.json` | `details.json` |
|---|---|---|
| Size (384 entities) | ~487 KB (~46 KB gzipped) | ~675 KB (~150 KB gzipped) |
| When fetched | immediately, blocking first render | in the background after first paint |
| Contains | ids, labels, types, levels, countries, regions, statuses, aliases, domains, degrees, paths, all edges | descriptions, sources, evidence, dates, verification, confidence, coverage, organisations, lineage |

Evidence strings dominate the payload — they are full sentences with
citations — so keeping them out of the critical path is most of the win.

`aliases` and `domains` deliberately stay in the light file: search must
match them from the first keystroke, before `details.json` has landed. When
it does land, its fields are folded onto the in-memory node records so the
list view and search can use them too.

At 384 entities this split is not strictly necessary. It is there because
§24 asks the design to assume 1,000+ nodes, and at that size a single
2 MB blob before first paint would be the wrong architecture.

---

## 6. Why Cytoscape.js

| Requirement | How it is met |
|---|---|
| Licence | MIT |
| GitHub Pages compatibility | single UMD file, vendored at `site/vendor/cytoscape.min.js`, **no CDN and no build step** |
| Directed relationships | first-class, with arrow styling per edge class |
| Filtering | selector engine over element data |
| Neighbourhood views | graph traversal built in |
| Bundle size | 435 KB minified (~120 KB gzipped), loaded once and cached |

Alternatives considered:

- **Sigma.js + graphology** — faster at 10,000+ nodes thanks to WebGL, but
  needs an ESM bundling step, which means a toolchain, a lockfile and a
  build in CI. Rejected because the level-of-detail strategy below matters
  far more than the renderer at the sizes this Atlas will plausibly reach.
- **D3.js** — more flexible, but layout, hit-testing, zoom/pan and selection
  would all be hand-rolled. More code to maintain for no gain here.

The library is **vendored rather than loaded from a CDN** so the site has no
third-party runtime dependency, works offline, and cannot break because
someone else's CDN changed. `tools/test_build_graph.py` asserts that
`index.html` references no external URLs.

---

## 7. Handling a large graph

The default view is deliberately not "everything at full detail":

1. **Typed relationships only by default** — 641 edges instead of 4,549.
2. **Level-of-detail labels** — `min-zoomed-font-size` hides labels that
   would render too small to read, and they return on zoom. Above 260
   visible nodes labels are dropped entirely.
3. **Deterministic layered layout** — the Global Atlas uses computed
   positions grouped into bands by level, and within a band into one block
   per scope, ordered by visible connectivity. It is `O(n log n)` arithmetic
   with no simulation to converge, so layout cost does not explode and the
   same repository always produces the same picture.
4. **Entity Explorer** — a bounded breadth-first traversal to a chosen depth
   (1–3 hops) over the *filtered* edge set. This is the answer to "the Atlas
   may eventually contain thousands of nodes": you look at a neighbourhood,
   not the hairball.
5. **Search-first** — the search box, deep links and List view all land the
   user on a specific entity rather than on the whole graph.
6. **Rendering hints** — `textureOnViewport`, `hideEdgesOnViewport`, no
   motion blur, `pixelRatio: 1`.

Measured on a synthetic 1,500-node / 12,000-edge graph (random edges — a
worst case for layout and for edge crossing):

| Operation | Time |
|---|---|
| Load to interactive | ~3.4 s |
| Search keystroke → results | ~220 ms |
| Country filter applied | ~350 ms |
| Explorer focus (2 hops, 191 nodes) | ~3.1 s |

No console errors, and label LOD engaged automatically. These are honest
numbers from a stress test, not a projection.

---

## 8. What is *not* in this design

- **No graph database.** Git plus Markdown/YAML remains the sole source of
  truth (README §"Source of Truth"). `graph.json` is a build artefact.
- **No backend.** The site is static files.
- **No manual graph data.** Nobody edits `site/graph.json`. It is
  regenerated from the repository, and a test fails if the committed copy no
  longer matches the entity files.
- **No change to the Markdown or YAML.** The graph reads the existing
  frontmatter and the existing `[[wikilinks]]`. Obsidian compatibility is
  untouched, which is the point of the two-view architecture.
