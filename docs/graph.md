# The Interactive Atlas

The Atlas publishes an interactive knowledge graph built automatically from
this repository's Markdown and YAML.

**[Open the Interactive Atlas →](https://dalust.github.io/Data-Initiatives-Atlas/)**

The repository is the source of truth. The graph is a **derived view** — a
second way of reading exactly the same knowledge base that Obsidian reads
locally.

```
                    Git repository
                          │
                ┌─────────┴─────────┐
                │                   │
             Obsidian          GitHub Pages
                │                   │
                ▼                   ▼
        Local knowledge       Interactive Atlas
             graph                  graph
```

---

## What you can do with it

### Four views

| View | What it is for |
|---|---|
| **Global Atlas** | The whole landscape, laid out in bands by geographic level — international at the top, regional below it, national below that, sectoral at the bottom — and within each band, one block per scope. Use it to see shape and scale. |
| **Entity Explorer** | One entity and its neighbourhood, drawn as rings by hop distance. Use it to actually read a part of the graph without being overwhelmed. |
| **Compare** | One supra-national instrument per row, one country per column. Use it to ask *"who did what about this directive?"* — see below. |
| **List** | A sortable, searchable table of every entity. Use it if you would rather not use a graph at all — it is a complete, non-visual route into the Atlas. |

### Compare — one instrument, many countries

The most valuable thing the Atlas holds is cross-country comparison, and for a
long time it existed only as prose tables hand-written inside entity bodies —
where they went stale every time a country was added.

The Compare view generates them instead. Rows are supra-national instruments,
columns are countries, and each cell is one of three states:

| Cell | Meaning | Comes from |
|---|---|---|
| **A national entity** | That country implements the instrument | an `implements-requirement-from` edge pointing at the row |
| **Applies — none modelled** | The Atlas records that the instrument covers that country, but models no national instrument for it | an `applies-in` edge from the row |
| **—** | Nothing recorded either way | neither edge |

The third state is **not** a claim that the instrument does not apply there.
It means the Atlas has not established anything, which is a different
statement and is labelled as such.

Two details worth knowing:

- **Rows respect the sidebar filters; columns respect the country filter
  only.** Rows are supra-national instruments with `country: null`, so
  applying the country filter to them would empty the table. Selecting
  Germany and Poland narrows the *columns*; selecting the Cybersecurity
  domain narrows the *rows*.
- **An implementer with no country of its own** — the EU implementing a UN
  convention — belongs in no column. It is reported on the row rather than
  dropped.

### Search

Type in the search box (or press <kbd>/</kbd> from anywhere). It matches:

- entity **name** — "General Data Protection Regulation"
- entity **ID** — `EU-GDPR`, `DE-BDSG`
- **alternative names** — "DSGVO", "BDSG-neu", "Deutschland"
- **type, level, status, country, region and domain** — "regulation",
  "national", "Germany", "geospatial"

Results are ranked: exact ID match first, then prefix matches, then
substring, then metadata matches, with better-connected entities ahead of
isolated ones. Arrow keys navigate the list, <kbd>Enter</kbd> opens.

Selecting a result switches to the Entity Explorer and focuses that entity.

### Filters

Everything in the sidebar is derived from the repository at build time — no
country, level, type or status is hard-coded in the application.

| Filter | Source |
|---|---|
| Geographic level | `level` field (`metadata/schema.json` → `levels`) |
| Country | `country` field; labels come from the country anchor entities themselves |
| Region | `region` field |
| Domain | `domains:` field; labels come from the domain entities themselves |
| Entity type | `type` field |
| Status | `status` field |
| Relationship type | `relationships[].type` |
| Provenance | `relationships[].source` — `fact` or `interpretation` |
| Confidence | `relationships[].confidence` |
| Connections shown | which of the three edge classes to draw |

When a new country or domain joins the Atlas it appears in its filter
automatically. Nothing in `site/` needs editing.

The **domain** filter is the cross-cutting axis described in
`metadata/taxonomy.md` §1.1: it answers *"what connects to cybersecurity?"*
regardless of type, level or country. Selecting a domain keeps the entities
tagged with it **and the domain entity itself** — the hub they all point at,
which carries no `domains:` of its own.

**Provenance** and **confidence** apply to typed relationships only, because
associations and wikilinks carry neither. Filtering to `interpretation`
isolates the connections the Atlas concluded rather than read; filtering to
`low` shows where the Atlas is least sure of its own edges. Both are the
audit route into the graph, and both were previously visible in the detail
panel but impossible to select on.

### Connections shown

The Atlas records three different kinds of link, and the graph keeps them
distinct rather than flattening them into one notion of "connected":

| Class | Drawn as | What it is |
|---|---|---|
| **Typed relationships** | solid, arrowed | The `relationships:` block — typed, directed, and carrying `source: fact \| interpretation`, `evidence` and `confidence`. **On by default.** |
| **Associations** | dashed, no arrow | ID references in `domains:`, `organisations:`, `related_entities:`, `previous_version:` and `successor:`. Real links in the data, but untyped and unprovenanced. |
| **Wikilinks** | dotted, faint | `[[LINKS]]` in the entity body — the same links Obsidian follows. Navigational rather than semantic. |

Relationships marked `source: interpretation` are drawn in the accent
colour and labelled *interpretation* in the detail panel, because the Atlas
distinguishes what a source says from what the Atlas concludes.

### Entity details

Click any node, or any entity name in the List view. The panel shows only
metadata that actually exists on that entity — name, ID, type, level,
country, region, status, description, alternative names, verification,
confidence, coverage, dates, domains, organisations, version lineage,
relationships in both directions with their evidence, and sources.

Every panel ends with **Open entity on GitHub**, linking to the Markdown
file the entity is defined in. The List view links to the same file from
every row.

### Deep links

`…/#EU-GDPR` opens the Atlas focused on that entity. The URL updates as you
navigate, so any view of the graph can be shared or bookmarked.

---

## Reading the picture

- **Colour = geographic level.** Purple international, blue regional, green
  national, orange sectoral.
- **Shape = entity type.** Diamonds are legislation, rounded rectangles
  organisations, hexagons standards, pentagons frameworks, stars country and
  region anchors, and so on.
- **Size = number of typed relationships.** Well-connected entities are
  larger.
- **Arrows = direction.** `EU-GDPR --applies-in--> DE` is drawn as an arrow
  from the regulation to the country, never as an undirected line.

Colour and shape carry different facets on purpose, so neither is the only
cue.

### Position

The Global Atlas places nodes rather than simulating them, so the same
repository always produces the same picture.

- **Vertical band = geographic level**, in order: international, regional,
  national, sectoral. This is the Atlas's core claim about how instruments
  descend, and it is the one thing the layout will not trade away.
- **Block within a band = scope.** For national entities the scope is the
  country, so the national band reads as seven separate clumps rather than
  one continuous ribbon. It is worth knowing why that works so cleanly:
  **every typed relationship between two country-attributed entities stays
  inside one country — 131 of 131.** Not one crosses a border. The blocks
  are not a drawing convention; they are what the data does.
- **Position inside a block = connectivity.** Each block leads with its
  best-connected member and trails off into its periphery.

Connectivity is measured over the **edges currently on screen**, not the
whole Atlas, so turning wikilinks on re-orders the blocks. That is
deliberate: the ordering describes what you are looking at.

Labels fade out when they would be too small to read and return as you zoom
in. In a dense view the status line tells you so.

---

## Accessibility

- The **List view** is a complete non-graph alternative — every entity,
  sortable, searchable, with links to the source Markdown.
- <kbd>/</kbd> focuses search; arrow keys and <kbd>Enter</kbd> drive the
  results; <kbd>Esc</kbd> closes the panel.
- A skip link, a single `h1`, labelled controls, live regions for status,
  and visible focus outlines.
- Light and dark themes follow the operating system setting.
- The canvas itself is not keyboard-traversable. That is a real limitation:
  the List view exists so the graph is never the only way in.

---

## Related documents

- [`graph-architecture.md`](graph-architecture.md) — how data becomes nodes
  and edges, and why the design is what it is.
- [`graph-development.md`](graph-development.md) — running and debugging the
  graph locally.
- [`github-pages.md`](github-pages.md) — how the site is built and deployed.
