# Graph Development

Running, changing and debugging the Atlas graph locally.

---

## Prerequisites

Python 3.12 and PyYAML — the same dependency the validation suite already
needs:

```bash
pip install -r validation/requirements.txt
```

The browser tests additionally need Node.js and Playwright, but they are
optional and are not part of CI.

---

## The loop

```bash
# 1. Validate the repository (must pass before anything else is meaningful)
python validation/run_all.py

# 2. Regenerate the graph from the Markdown/YAML
python tools/build_graph.py

# 3. Serve the site — it must be served over HTTP, not opened as a file://
python -m http.server 8765 --directory site

# 4. Open http://127.0.0.1:8765/
```

`file://` does not work: the app `fetch()`es `graph.json`, and browsers block
cross-origin requests for `file://` documents. The app detects this and says
so rather than showing an empty canvas.

---

## `tools/build_graph.py`

```
python tools/build_graph.py [-o OUT] [--indent N] [--check] [--lenient-wikilinks]
```

| Flag | Effect |
|---|---|
| `--check` | Build and report, write nothing. Used by CI on pull requests. |
| `--indent 2` | Pretty-print the JSON. Useful when diffing by eye; the committed files are compact. |
| `--lenient-wikilinks` | Downgrade unresolved body `[[links]]` from error to warning. Escape hatch for work in progress — do not use in CI. |
| `-o PATH` | Write somewhere other than `site/graph.json`. `details.json` is written alongside it. |

Environment:

| Variable | Effect |
|---|---|
| `ATLAS_BRANCH` | Branch used in generated GitHub links. Defaults to the remote's default branch, then `main`. Deliberately **not** the checked-out branch — links baked from a feature branch would 404 once it is deleted. |

Output on success:

```
build_graph: 516 entities, 6170 edges (1095 relationship, 2016 association, 3059 wikilink)
             58 countries, 1 region(s), 17 entity types in use
build_graph: wrote site/graph.json (503 KB)
build_graph: wrote site/details.json (697 KB)
```

---

## Tests

```bash
python tools/test_build_graph.py          # required — 41 tests, no extra deps
```

Covers: YAML parsing (including the **`NO` boolean trap** — `country: NO`
unquoted parses as `False` under YAML 1.1), file discovery, ID uniqueness,
required fields, **scope-anchor reachability** (§2.3 — every entity carries
at least one provenanced relationship, domains excepted), node generation,
edge generation, **relationship direction**, vocabulary
conformance, phantom-node refusal, dynamic country and **domain** discovery,
provenance and confidence facet totals, dynamic statistics, the payload
split, and whether the committed `site/graph.json` still matches the
repository.

```bash
# optional browser tests — need Playwright + Chromium
python -m http.server 8765 --directory site &
npm install playwright && npx playwright install chromium
node tools/test_ui.mjs
```

124 checks across desktop, mobile (390×844) and accessibility: search by
name/ID/country, keyboard navigation (including arrow-key traversal of the
canvas itself), tapping a node or an edge, detail panel content, GitHub
links, deep links, shareable filter/view/depth/search/path/layout state in
the URL hash, every filter, edge-class toggles, path-finding between two
entities (including a path beyond the current depth, a clear action, and
the no-path-found case), **the layered layout's block grouping and band
order**, **the world map layout's geographic ordering, its country/region
clusters never overlapping, a cross-border relationship visibly pulling
its two entities closer together, and a supra-national body pulling far
closer to its member states than an unconnected one**, the comparison
matrix, the list view and its sorting, and console-error freedom
throughout.

These are **not** in CI: they would require installing a browser on every
pull request for a static page whose data is already covered by the Python
suite. Run them when changing `site/app.js`.

---

## Debugging

### The graph will not build

The generator refuses rather than producing a partial graph, and names the
file and the field:

```
ERROR legislation/de-bdsg.md: relationships[0]: target 'NO-SUCH-ENTITY' does not
      resolve to a known entity — refusing to invent a node for it
```

Fix the entity file. `python validation/run_all.py` usually reports the same
problem in more detail — start there.

### The page loads but the graph is empty

1. Open the browser console. A failed `fetch` for `graph.json` shows as an
   overlay with the HTTP status.
2. Check you are on `http://`, not `file://`.
3. Check `site/graph.json` exists — it is committed, but a fresh clone with a
   `.gitignore` mishap could lack it.

### A node is missing

- Is it filtered out? The status line shows `N of M entities`. Press **Reset
  all filters**.
- Is it in the Explorer's neighbourhood? Increase the depth, or switch to
  Global Atlas.
- Does it exist? Check the List view, which ignores graph layout entirely.

### An edge is missing

Most likely the edge class is off. Only **typed relationships** are shown by
default; associations and wikilinks are separate checkboxes.

If a typed relationship is genuinely absent from `graph.json`, it is absent
from the frontmatter — the generator emits every `relationships:` entry or
fails. Check the entity file.

### An edge points the wrong way

The generator never reverses or symmetrises an edge. If `A → B` looks wrong,
the `relationships:` block on `A` says so. See
`metadata/relationship-types.md` §2.1 for what each type means — the
`maintained-by` direction (target maintains subject) catches people out, and
has caught this repository out before.

### The committed graph is stale

`test_generated_graph_matches_repository` fails. Run
`python tools/build_graph.py` and commit both `site/graph.json` and
`site/details.json`.

The test compares **content**, not the file bytes: `generated_at` changes on
every build, so a byte comparison would always report staleness.

---

## Adding a feature

### A new filter

1. Make sure the facet is emitted by `build_graph.py` (`facets` in `build()`).
2. Add a `<details>` block with an empty container in `site/index.html`.
3. Call `facetInto(containerId, filterKey, G.facets.<name>, countElId)` in
   `buildChrome()`.
4. Add the key to the `filters` object and handle it in `passesNodeFilters()`
   or `passesEdgeFilters()`.

The generic `change` listener wires the checkboxes automatically, and
`resetFilters()` iterates the `filters` object, so a new key is cleared by
the reset button without being named there — there is no per-filter event
handling to write.

Two things worth knowing when you get there:

- **Ordering.** Facet rows sort by count. If the vocabulary is ordinal —
  `high, medium, low` — pass `{ order: [...] }` to `facetInto()`, as the
  confidence filter does; alphabetical or by-count ordering makes a scale
  read as an unordered list.
- **Hub nodes.** If the facet is an ID reference to another entity (the
  domain filter is), decide whether the referenced entity passes its own
  filter. `passesNodeFilters()` admits it explicitly, because filtering to a
  domain and dropping the domain entity leaves its entities with no centre.

### A new node property

Add it in `build_graph.py`'s node construction. Decide whether it belongs on
the critical path (`graph.json`) or in `NODE_DETAIL_FIELDS`
(`details.json`): if search or filtering needs it, it must be in the light
payload.

### Country/region centroids

`tools/country_centroids.py` holds a static ISO 3166-1 alpha-2 → (lat, lon)
table (sourced from a public-domain dataset, see the module docstring for
provenance) plus a small, hand-maintained `REGION_CENTROIDS` table for
political groupings like `EU`. `build_graph.py` emits these onto
`facets.countries[].{lat,lon}` and `facets.regions[].{lat,lon}` for the
World map layout (see "Restyling" below) to read, so the site itself never
computes or fetches any geographic data.

The country table is deliberately comprehensive (nearly all ISO codes, not
just the ~60 currently in use): the Atlas discovers countries from the data
as they are added, and a new country should not need a companion PR here.
If one ever does — a code with no entry in either table — `build_graph.py`
refuses the build, the same way a dangling relationship target does, rather
than silently shipping a graph the map view then has nowhere to place a
piece of.

### A new view

`setView()` toggles `#stage`, `#listview` and `#compareview`, then calls
`refresh()`. `refresh()` dispatches on `view`. `currentElements()` is where a
graph view decides which subgraph to show; a non-graph view (List, Compare)
returns from `refresh()` before touching Cytoscape.

If the view interprets a filter differently from the graph — Compare treats
`country` as its columns rather than as a row predicate — say so in the view's
own hint text. `passesNodeFilters(n, ignoreCountry)` takes a second argument
for exactly that case. Call it with an explicit wrapper, never as
`.filter(passesNodeFilters)`: `Array#filter` passes the index as the second
argument, which would silently switch the flag on for every element but the
first.

### Restyling

Node **position** has three modes, switched from the sidebar and dispatched
in `runLayout()`. `sizeBlock()` (sort by connectivity, pick a grid size) and
`placeBlock()` (drop a sized grid at a centre point) are shared by the two
that pack nodes into per-scope/per-country blocks:

- **Grouped** (default) — `layeredPositions()`: bands by level, blocks by
  scope within a band, connectivity order within a block. Pure arithmetic,
  no threshold needed.
  - `blockGapY` is deliberately much larger than `blockGapX` (190 vs 110).
    Blocks wrap onto new lines, so it is the **vertical** distance between
    two blocks that a growing country eats into, and `test_ui.mjs` asserts
    that no two block centroids sit closer than the largest block's own
    radius. That margin ran out at 447 vs 464 when the Dutch block reached
    85 entities. If it fails again, raise `blockGapY` — not `blockGapX`,
    which does not move the binding pair.
- **Force** — `cose` with `forceOptions()`, seeded from the grouped
  positions (`randomize: false`) so it is reproducible. Gated by `FORCE_MAX`;
  above it the grouped layout is kept and the sidebar explains why. Tune
  distance in `idealEdgeLength()`.
  - The default filters leave the graph in 44 disconnected components (see
    `componentSpacing`'s own comment), and cose lays each one out on its own
    before packing the components into a grid — which routinely lines up
    several components' worth of nodes on the same row. `test_ui.mjs`'s
    "rearranges the graph off the grid" check learned this the flaky way: an
    absolute "80% of nodes get a unique y" bar looked like it needed a
    longer wait, but waiting for cose's own `layoutstop` (rather than a
    fixed timeout) still landed at 511–519 of 652 every time — a stable
    property of this graph and this layout, not a race. The check now
    compares against the grouped layout's own distinct-y count instead of
    an absolute number, which is what actually mattered.
- **World map** — `mapPositions()`: each country's (or region's) block is
  centred on its real centroid (`tools/country_centroids.py`, via facets),
  projected with a plain equirectangular transform (`x = lon`, `y = -lat`,
  scaled by `MAP_SCALE`). Entities with neither a country nor a region — the
  `EU`/`UN`/`INTL`/`DOMAIN` scopes (metadata/ontology.md §2.1) that have no
  single true location — start in a panel beside the map instead of a
  fabricated point (pinning "Council of Europe" to Strasbourg would need the
  same sourcing rigor as any other fact here, and a convention with several
  depositaries has no one point to pin at all), then get pulled toward
  whatever they actually connect to — see `relaxTowardEdges()` below.
  - A country's true centroid is routinely closer to its neighbours than its
    own entity cluster is wide (the Netherlands and Belgium are under 1.5°
    apart; either cluster alone can be a thousand pixels across), so overlap
    at the raw projected position is the normal case, not a bug.
    `declutterCircles()` resolves it: circles are pushed apart only enough
    to stop overlapping, with a small spring pulling each one back toward
    its true position every iteration so a crowded region spreads out
    locally instead of the correction cascading across the whole map. The
    earlier version had no spring and pushed straight to zero overlap every
    pair, full strength — with a dozen large mutually-overlapping circles
    (western Europe) that cascaded until the Netherlands drifted past
    Portugal's true position. `test_ui.mjs` asserts immediate-neighbour
    ordering survives (Norway stays north of Spain, Germany stays east of
    the Netherlands) as well as zero overlap.
  - `MAP_SCALE` trades off against that cascade: too small, and block size
    dominates the declutter pass and can invert real ordering between close
    neighbours; too large, and distant countries end up needing an
    impractically zoomed-out canvas. 360 was tuned against the current ~60
    countries and their entity counts — if it drifts again as the Atlas
    grows, re-tune this constant before touching the declutter algorithm
    itself.
  - Country placement alone leaves an individual entity exactly as far from
    a related entity as their two countries happen to be, however direct
    the relationship — two national base-registry programmes that reference
    each other still rendered on opposite sides of their blocks, since nothing
    about `declutterCircles()` looks at edges at all, only country shapes.
    `relaxTowardEdges()` runs after the country blocks are placed: a small
    mass-spring pass where every node has a spring back to its block position
    (`RELATION_HOME_SPRING`) and a spring toward every entity it actually has
    an edge to (`RELATION_PULL`, normalised by degree so a hub's dozens of
    edges do not each pull at full strength). `RELATION_MAX_DRIFT` hard-caps
    how far any single node may move from its block position, so a country's
    entities drift toward a connected neighbour's border rather than into the
    neighbour's own territory — 350 is the largest value that still keeps
    every pair of clusters non-overlapping against the current data;
    `test_ui.mjs` checks both that (zero overlap between country/region
    clusters — a tray entity is allowed to overlap what it gets pulled
    toward) and that the pull is real (a documented cross-border
    relationship ends up closer than its two countries' bare cluster
    separation).
  - The panel's own starting position anchors to countries with at least
    `TRAY_ANCHOR_MIN_ENTITIES` entities, not the single leftmost circle
    overall — a country whose only content so far is its own anchor node
    (Mexico, Argentina, Cape Verde…) can sit at an extreme longitude with
    nothing else nearby, and anchoring the panel to it stranded every
    supra-national entity tens of thousands of pixels from Europe, where
    almost all of their actual relationships point. Tray-origin nodes also
    use a far weaker home spring and longer drift cap (`TRAY_HOME_SPRING`,
    `TRAY_MAX_DRIFT`) than country-anchored ones, since the panel is a
    parking spot for whatever the relationship pull doesn't reach, not a
    fact worth preserving the way a country's centroid is — a body like the
    Council of Europe, with real edges to two dozen member states, ends up
    rendering near Europe as a result, not at a hard-coded point.
    `test_ui.mjs` checks it against a domain entity, which (tagged only via
    an association, not a relationship) has nothing pulling it under the
    default filters and stays exactly where the panel puts it — the fair
    "unpulled" baseline for how far from a real country a panel entity
    would otherwise sit.

`LOD_LABELS` still thins labels above 260 visible nodes.

Two things to know before tuning `idealEdgeLength()`: a **slack spring is
not a long one** — dropping `edgeElasticity` makes an edge class stop
mattering, not stretch — and `confidence: high` is currently on only 2 of
354 relationships, so it cannot demonstrate anything.

Node colour is driven by `level` and shape by `type`, both in the Cytoscape
stylesheet at the top of `initGraph()`. Colours come from CSS custom
properties (`--lvl-*`) so light and dark themes stay consistent — read them
with the `css()` helper rather than hard-coding hex values.

---

## Upgrading Cytoscape.js

```bash
npm install cytoscape@latest
cp node_modules/cytoscape/dist/cytoscape.min.js site/vendor/
cp node_modules/cytoscape/LICENSE site/vendor/cytoscape.LICENSE
node -e "const p=require('cytoscape/package.json');console.log(p.name,p.version,p.license)" \
  > site/vendor/cytoscape.VERSION
node tools/test_ui.mjs   # confirm nothing regressed
```

The library is vendored on purpose: no CDN, no runtime third-party
dependency, and the site works offline. A test asserts `index.html`
references no external URLs.

---

## Obsidian

Nothing in this batch changes the Markdown or the YAML. `site/`, `tools/`
and `docs/` are ordinary folders in the vault; if their presence in
Obsidian's own graph is unwanted, exclude them under
*Settings → Files & Links → Excluded files*. The Atlas's entity files,
frontmatter and `[[wikilinks]]` are untouched.
