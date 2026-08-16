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
build_graph: 233 entities, 2184 edges (320 relationship, 747 association, 1117 wikilink)
             5 countries, 1 region(s), 15 entity types in use
build_graph: wrote site/graph.json (251 KB)
build_graph: wrote site/details.json (365 KB)
```

---

## Tests

```bash
python tools/test_build_graph.py          # required — 32 tests, no extra deps
```

Covers: YAML parsing, file discovery, ID uniqueness, required fields, node
generation, edge generation, **relationship direction**, vocabulary
conformance, phantom-node refusal, dynamic country discovery, dynamic
statistics, the payload split, and whether the committed `site/graph.json`
still matches the repository.

```bash
# optional browser tests — need Playwright + Chromium
python -m http.server 8765 --directory site &
npm install playwright && npx playwright install chromium
node tools/test_ui.mjs
```

47 checks across desktop, mobile (390×844) and accessibility: search by
name/ID/country, keyboard navigation, detail panel content, GitHub links,
deep links, every filter, edge-class toggles, the list view and its sorting,
and console-error freedom throughout.

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

The generic `change` listener wires the checkboxes automatically — there is
no per-filter event handling to write.

### A new node property

Add it in `build_graph.py`'s node construction. Decide whether it belongs on
the critical path (`graph.json`) or in `NODE_DETAIL_FIELDS`
(`details.json`): if search or filtering needs it, it must be in the light
payload.

### A new view

`setView()` toggles `#stage` and `#listview` and calls `refresh()`.
`refresh()` dispatches on `view`. `currentElements()` is where a view decides
which subgraph to show.

### Restyling

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
