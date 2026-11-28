# Graph Development

Running, changing and debugging the Atlas graph locally.

---

## Prerequisites

Python 3.12 and PyYAML — the same dependency the validation suite already
needs:

```bash
pip install -r validation/requirements.txt
```

The browser tests and the layout step (`tools/build_layout.mjs`) additionally
need Node.js; the browser tests also need Playwright. CI runs the browser tests
in the `browser` job.

---

## The loop

```bash
# 1. Validate the repository (must pass before anything else is meaningful)
python validation/run_all.py

# 2. Regenerate the graph from the Markdown/YAML
python tools/build_graph.py

# 3. Work out the whole-graph force layout (about 4 s; needs Node)
node tools/build_layout.mjs

# 4. Serve the site — it must be served over HTTP, not opened as a file://
python -m http.server 8765 --directory site

# 5. Open http://127.0.0.1:8765/
```

Step 3 is optional for looking around: without `site/layout.json` the page works, but
it logs a 404 for the file, and the force layout runs the slow live simulation instead
of drawing the stored positions. The browser tests expect the file, as CI builds it.

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
build_graph: 1032 entities, 11844 edges (2167 relationship, 4473 association, 5204 wikilink)
             114 countries, 1 region(s), 21 entity types in use
build_graph: wrote site/graph.json (1391 KB)
build_graph: wrote site/details.json (2283 KB)
```

---

## Tests

```bash
python tools/check_all.py                 # everything CI runs, about a minute (needs only PyYAML)
python tools/test_build_graph.py          # just the generator's tests
```

`check_all.py` is the one list of checks that CI runs (`.github/actions/checks`): the validation suite, every
test suite that needs no network, the headline numbers and `build_graph.py --check`. The generator's tests
share one build of the real data (`real_build()` in the test file), so adding a test that reads the graph
costs no extra build.

Covers: YAML parsing (including the **`NO` boolean trap** — `country: NO`
unquoted parses as `False` under YAML 1.1), file discovery, ID uniqueness,
required fields, **scope-anchor reachability** (§2.3 — every entity carries
at least one provenanced relationship, domains excepted), node generation,
edge generation, **relationship direction**, vocabulary
conformance, phantom-node refusal, dynamic country and **domain** discovery,
provenance and confidence facet totals, dynamic statistics, the payload
split, and whether the build is deterministic (the generated files are not
committed, so they must be reproducible).

```bash
# browser tests — the client library plus any Chrome (CI runs them in the `browser` job
# of validate.yml, on the runner's own Chrome; the job is a required check since 2026-10-10)
python tools/build_graph.py
node tools/build_layout.mjs
python -m http.server 8765 --directory site &
npm install playwright-core
CHROME_PATH=/path/to/chrome node tools/test_ui.mjs
```

CI runs the suite as two shards at once, `UI_SHARD=desktop` (the long 1440 px walk-through, 112 checks) and
`UI_SHARD=rest` (every other section, 62 checks), so the job takes about 90 s instead of 140 s on a laptop and in CI alike.
Run one shard by itself when you are working on that part; with no `UI_SHARD` everything runs. A new top-level
section in `test_ui.mjs` must start with `if (runs('rest')) {` (or `runs('desktop')`): `tools/test_browser_ci.py` fails on a bare block.

A section of the suite that throws is recorded as one failed check and the run goes on, so
a stale selector shows up as one line instead of hiding every check after it; entity counts
come from `graph.json`, not from numbers frozen in the suite.

The checks run across desktop, mobile (390×844) and accessibility: search by
name/ID/country, keyboard navigation (including arrow-key traversal of the
canvas itself), tapping a node or an edge, detail panel content, GitHub
links, deep links, shareable filter/view/depth/search/path/layout state in
the URL hash, every filter, edge-class toggles, path-finding between two
entities (including a path beyond the current depth, a clear action, and
the no-path-found case), **the layered layout's block grouping and band
order**, the layout selector (and an old `layout=map` link opening the
grouped layout), the comparison
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
3. Check `site/graph.json` exists. It is **not committed**, so a fresh clone
   has none until you run `python tools/build_graph.py`.

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

### The graph looks out of date

`site/graph.json` and `site/details.json` are not committed, so a stale copy
can only be one you built earlier. Run `python tools/build_graph.py` again.

If `test_build_is_deterministic` fails, two builds of the same data produced
different content. That breaks the assumption that makes not committing the
files safe. The test compares **content**, not bytes: `generated_at` changes
on every build and is excluded.

---

## Adding a feature

### The overview and the stored layout

Two things keep the page fast as the Atlas grows (roadmap #508, numbers in
`docs/performance.md`).

**The overview.** A bare address opens on the international and regional
entities and every country (`inOverview()`), not on every entity. It is not a
filter the visitor set: `overviewActive()` is true exactly when the Atlas view
is untouched (no filter, no focus, no path, default connections) and "Show all"
has not been chosen, so it ends by itself when anything is chosen and returns
when it is cleared. "Show all" is remembered as `all=1` in the address. The
List and Compare views are not affected. If the overview's definition changes,
`test_ui.mjs` (the overview section) and the Start card's wording follow.

**The stored layout.** `tools/build_layout.mjs` lays out every entity over the
typed relationships with the vendored Cytoscape and `site/force-options.js`,
using a seeded random-number generator, and writes `site/layout.json`
(`{ fingerprint, positions }`, about 10 KB gzipped). `build_graph.py` puts the
matching `layout_fingerprint` in `graph.json`: a hash of the entity ids, the
typed relationships and `force-options.js`. The page uses the stored positions
only when the two fingerprints are equal, only when the connections shown are
typed relationships alone, and only when every node on screen has a position;
otherwise it runs the simulation as before. So a stale or missing file is never
shown, only unused, and editing a number in `force-options.js` invalidates every
stored layout until `build_layout.mjs` runs again. `layout.json` is not
committed: `pages.yml` and the `browser` job build it after `build_graph.py`.

A filtered view shows its entities where they sit in the full layout (it does
not re-lay-out the subset), which is cheap at any size and keeps the map
the same from one view to the next; the cost is gaps where the filtered-out
entities were.

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

Node **position** has two modes, switched from the sidebar and dispatched
in `runLayout()`. `sizeBlock()` sorts a block's nodes by connectivity and
picks its grid size. (A third mode, the world map, was removed on
2026-11-28, roadmap #645; it and `tools/country_centroids.py` are in the git
history if it comes back.)

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
- **Force** — `cose`, tuned in `site/force-options.js` (shared with the build
  step). With typed relationships only, the default, the page draws the layout
  stored at build time (`site/layout.json`, see below) for any number of nodes;
  otherwise it runs the simulation itself, seeded from the grouped positions
  (`randomize: false`) so it is reproducible. The live simulation is gated by
  `FORCE_MAX` (900); above it the grouped layout is kept and the sidebar
  explains why. Tune distance in `idealEdgeLength()` (in `force-options.js`).
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
