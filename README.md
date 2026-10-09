<div align="center">

# 🌍 Data Initiatives Atlas

**Mapping the data landscape across the UN, EU and participating countries
as an open, connected knowledge graph.**

### [**→ Open the Interactive Atlas**](https://dalust.github.io/Data-Initiatives-Atlas/)

*Search, filter and explore 771 entities and 9,610 connections across sixty-three
countries — no install, no account.*

[![Validation](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/validate.yml/badge.svg)](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/validate.yml)
[![Pages](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/pages.yml/badge.svg)](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/pages.yml)
[![Licence: CC0-1.0](https://img.shields.io/badge/licence-CC0--1.0-blue.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-%E2%9D%A4-db61a2?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/DaLuSt)

</div>

---

## What it is

An open, machine-readable knowledge base connecting data-related
**initiatives, legislation, policies, standards, frameworks, programmes,
organisations and data ecosystems** across international, regional and
national levels.

Every entity is a Markdown file with YAML frontmatter. Every relationship
carries its own provenance — whether it is a sourced fact or the Atlas's own
interpretation, with the evidence attached. Nothing in the graph is
hand-maintained.

| | |
|---|---|
| **Entities** | 771 |
| **Connections** | 9,610 — of which **1,609** are typed relationships, each with its provenance |
| **Country scopes** | **58** — 23 with national entities beyond the anchor itself, the rest base anchors |
| **Layers** | UN · Council of Europe · EU · national · subnational (sector is carried by `domains`) |
| **Source of truth** | Git + Markdown/YAML — no database |
| **Licence** | CC0 1.0 |
| **✅ Sourcing** | **All 771 entities are `verification: primary-source`** — every cited source has been opened, read and confirmed |

*Figures as of 2026-10-08. The live counts are always on the site itself.*

### Read this before you cite anything

Every entity carries a `verification` field in its frontmatter, and it means
exactly what it says:

- **`verification: search-only`** — the URLs in `sources:` were confirmed by
  a search index to exist, but nobody has actually opened and read them yet.
  The claims may well be accurate; they simply haven't been checked against
  the primary source. **All 771 entities have moved past this stage**, after
  a sustained multi-batch re-verification effort — none remain `search-only`,
  though a newly-added entity can still start out there before it is
  verified.
- **`verification: primary-source`** — someone opened every cited page
  directly, confirmed it supports what the entity says, and recorded the
  date in `accessed:` (for entities whose sources are all on the five domains the
  repository owner confirmed on 2026-08-21 (`europa.eu`, `iso.org`, `coe.int`,
  `bund.de`, `legifrance.gouv.fr`) that confirmation stands in for per-page dates;
  `validation/validate_sources.py` checks one or the other is there). Entities at this level also drop the sourcing caveat
  from their body text, because it is no longer true of them.

This is disclosed rather than buried, and enforced rather than just stated:
`validate_frontmatter.py` **refuses `confidence: high`** on any entity that
is still `search-only`, so an unverified claim can never quietly present
itself as a checked one, and the site shows each entity's verification state
on its own page.

**How to verify an entity.** Re-verification means opening every URL in an
entity's `sources:` list, reading the page, and checking that it actually
supports the entity's claims — not just that the page exists.

- `tools/reverify.py` runs this pass wherever a host allows automated
  fetching: it fetches each source with an honest, identifying User-Agent
  and reports what it read. `docs/re-verification.md` is the full procedure.
- Some hosts block automated fetches outright — an HTTP 403 wall, a
  bot-defense challenge page, a dead domain or a TLS reset — and those
  entities need a manual read instead.
- Once a source has genuinely been read and confirmed, set
  `verification: primary-source`, add an `accessed:` date, rewrite the
  evidence with what the source actually says (a verbatim quote where
  possible), and drop the sourcing caveat from the body.
- Never pad a partial date — a bare year or month found in a source — into a
  fabricated `YYYY-MM-DD`. Leave `start_date`/`end_date` as `null` and record
  the real precision in prose instead.
- `discovery/unresolved.md` is the standing register of what is still
  unknown, and `discovery/reverification-allowlist.md` is the generated
  worklist of what to try next, ranked by how many entities each host
  unblocks.

**Use it as a map of the territory, not as a legal source.** Structure,
relationships and the questions it raises are the value here; every specific
date, identifier and citation needs checking against the primary source
before you rely on it.

### Explore it

| Where | What you get |
|---|---|
| **[The interactive graph](https://dalust.github.io/Data-Initiatives-Atlas/)** | Search by name, ID, country, type or domain. Filter by level, country, region, **domain**, type, status, relationship type — and by **provenance and confidence**, so you can isolate what a source states from what the Atlas concludes. A sidebar control switches the Global Atlas between a **grouped** arrangement (bands by level, blocks by country) and a **force-directed** one that pulls connected entities together. The **Compare** view puts one supra-national instrument per row and one country per column, so you can see who implemented what — generated from the graph, not hand-written. Click any entity for its metadata, sourced relationships and citations, and a link to the underlying Markdown. Names show in English by default, with the official name alongside. The filtered list can be downloaded as **CSV**, and the address bar holds the whole view, so a link shares it. |
| **This repository** | The source of truth. Browse `countries/`, `legislation/`, `organisations/` and the rest directly. |
| **As an Obsidian vault** | Open the repository folder in Obsidian and the `[[wikilinks]]` become a local graph. |

♿ [`ACCESSIBILITY.md`](ACCESSIBILITY.md) says what has been checked, what is known to
be hard, and how to report a barrier ·
📖 [`docs/graph.md`](docs/graph.md) is a tour of the site ·
[`docs/graph-architecture.md`](docs/graph-architecture.md) explains how
entity files become nodes and edges ·
[`docs/re-verification.md`](docs/re-verification.md) is the procedure for
turning `search-only` entities into read ones.

---

## Why

Data governance is shaped by initiatives operating at different levels:

1. An **international principle** influences an EU strategy.
2. An **EU regulation** leads to national implementation.
3. A **national programme** establishes a framework.
4. A **framework** references standards.
5. **Standards** underpin data spaces and technical ecosystems.

Each of those pieces is documented somewhere. **The connections between them
usually are not** — they are scattered across many websites, documents and
organisations.

The Atlas brings them into one connected knowledge base.

> *The objective is not simply to create a catalogue, but to make the
> relationships between initiatives visible.*

---

## 🧭 Vision

A global, open Data Governance Atlas connecting international, regional and
national data initiatives — one you can navigate from an international
initiative down to its regional and national implications, related
standards, responsible organisations and affected data domains.

- **United Nations**
  - **European Union**
    - **European Initiative**, implemented nationally by each of:
      - Netherlands, Germany, Belgium, France, Spain, Poland, ... — each
        with its own national initiative, framework and data ecosystem

- **United Kingdom** — not below the EU branch, since it is a non-member
  state — with its own national initiative, framework and data ecosystem

The Netherlands is the starting point, not the boundary of the project, and the
EU is not the only route into a national scope. Which further countries to add
is on the roadmap (see below).

---

## 🌐 Geographic scope

The Atlas uses a multi-level geographic model.

### International

International initiatives and organisations, including the United Nations
and other global institutions — international principles, global strategies
and frameworks, international standards, global programmes, cross-border
initiatives.

### Regional

Regional initiatives and organisations, with the European Union as the
initial focus — EU legislation, strategies, policies and programmes,
European standards, European data spaces, European governance frameworks.

The model also allows other regional organisations and ecosystems to be
added later.

### National

National initiatives, legislation, strategies, frameworks, organisations and
data ecosystems.

The Netherlands was the first participating country; many others have followed
(see [`countries/README.md`](countries/README.md)). Additional countries
can be added **without changing the fundamental information model**:

```
countries/
├── nl/
├── de/
├── be/
├── fr/
├── es/
├── pl/
├── gb/
└── ...
```

Countries should only be added when there is sufficient information and,
preferably, an active contributor or participating community maintaining
that national scope.

> **That claim has been tested repeatedly.** Adding further countries has not
> required a change to the schema, ontology, taxonomy, relationship types,
> folder structure or any validation rule, including the **United Kingdom**, which is not an EU member
> state: no EU instrument carries `applies-in` to it and its entities have
> `region: null`. See
> [`countries/README.md`](countries/README.md) and
> [`validation/germany-second-country-report.md`](validation/germany-second-country-report.md).

---

## 🗺️ Country participation model

A country is not required to match another country's depth or coverage. The
Atlas supports **incremental participation**.

A country can start with:

```
Country
 ├── National strategies
 ├── Key legislation
 ├── Major data initiatives
 └── Principal organisations
```

and progressively expand towards:

```
Country
 ├── Legislation
 ├── Strategies
 ├── Policies
 ├── Programmes
 ├── Standards
 ├── Frameworks
 ├── Organisations
 ├── Data spaces
 ├── Domains
 └── EU / international relationships
```

This makes the project suitable for both individual contributors and
organised national communities.

---

## 🧩 What is being mapped

The Atlas is built on a common ontology applied identically at
international, regional and national levels.

**Core entity types**

`initiative` · `organisation` · `country` · `region` · `policy` · `soft-law` · `act` ·
`regulation` · `directive` · `decision` · `subordinate-legislation` ·
`agreement` · `strategy` · `standard` · `framework` ·
`programme` · `data-space` · `platform` · `technology` · `domain` ·
`publication`

The ontology is **intentionally country-neutral**. Country-specific concepts
are represented through metadata and relationships rather than hard-coded
into the core model.

📄 Full definitions: [`metadata/ontology.md`](metadata/ontology.md) ·
[`metadata/taxonomy.md`](metadata/taxonomy.md) ·
[`metadata/relationship-types.md`](metadata/relationship-types.md)

---

## 🔗 Cross-border relationships

A key purpose of the Atlas is to make relationships between geographic
levels visible.

- **International Initiative**
  - **EU Strategy**
    - **EU Regulation**, implemented nationally by each of:
      - Netherlands, Germany, Belgium, France, Spain, Poland — each with
        its own national implementation

This lets the Atlas represent **horizontal** relationships between countries
and **vertical** relationships between international, regional and national
levels.

**Relationship types include**

`influences` · `implements` · `implemented-by` · `implements-requirement-from` ·
`applies-to` · `applies-in` · `derived-from` · `based-on` · `references` ·
`related-to` · `depends-on` · `supersedes` · `replaces` ·
`proposes-to-supersede` · `amends` · `supplements` · `part-of` · `governed-by` ·
`produces` · `maintained-by` · `owned-by` · `participates-in` · `aligned-with` ·
`cooperates-with` · `measures` · `uses-data-from` · `carries-identifier-of` ·
`referred-to-court-over` — each defined, with when to use it, in
[`metadata/relationship-types.md`](metadata/relationship-types.md)

Every relationship records whether it is a **sourced fact** or an **Atlas
interpretation**, with the evidence and a confidence level attached.

---

## 🗂️ Repository structure

The repository is structured around **entities**, not around individual
countries.

<details>
<summary>Show the full repository layout</summary>

```
data-initiatives-atlas/
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md       # data releases, prepared automatically
├── AGENTS.md          # operating model for Claude Code sessions
├── LICENSE
├── .agent/            # session state, policies, run history
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
│       ├── validate.yml         # every pull request
│       ├── pages.yml            # deploy, main only
│       ├── release-pr.yml       # weekly release pull request
│       ├── release-publish.yml  # tags and Release after merge
│       └── project-board.yml    # keeps the roadmap board in step
├── initiatives/
├── legislation/
├── policies/
├── strategies/
├── standards/
├── frameworks/
├── soft-law/
├── programmes/
├── organisations/
├── data-spaces/
├── platforms/
├── publications/
├── domains/
├── countries/
│   ├── nl/
│   ├── de/
│   ├── be/
│   ├── fr/
│   ├── es/
│   ├── pl/
│   └── ...             # one folder per country
├── regions/eu/
├── international/un/
├── metadata/
│   ├── ontology.md
│   ├── taxonomy.md
│   ├── relationship-types.md
│   ├── metadata-schema.md
│   ├── controlled-vocabularies.md
│   ├── rank-basis.md
│   ├── versioning.md
│   ├── version.yaml
│   └── schema.json
├── templates/
├── discovery/
├── validation/
├── progress/
├── tools/              # generator, reverify, tests
│   ├── build_graph.py
│   ├── release.py      # versions, changelog, release PR
│   ├── project_board.py # roadmap board sync (run by a workflow)
│   ├── reverify.py     # re-verification pass
│   ├── source_hosts.py # egress allowlist
│   ├── test_board_health.py
│   ├── test_browser_ci.py
│   ├── test_build_graph.py
│   ├── test_project_board.py
│   ├── test_release.py
│   ├── test_reverify.py
│   └── test_ui.mjs
├── site/               # published GitHub Pages app
│   ├── index.html
│   ├── app.css
│   ├── app.js
│   ├── csv.js
│   ├── graph.json      # generated, not committed (gitignored)
│   ├── details.json    # generated, not committed (gitignored)
│   └── vendor/         # Cytoscape.js, vendored
└── docs/
    ├── graph.md
    ├── graph-architecture.md
    ├── graph-development.md
    ├── re-verification.md
    ├── roadmap.md
    ├── ux-analysis.md
    └── github-pages.md
```

</details>

As additional countries participate, only `countries/` grows:

```
countries/
├── nl/
├── de/
├── be/
├── fr/
├── es/
├── pl/
└── ...
```

The repository does not require a redesign when a new country is introduced.

---

## 🔁 No manual graph maintenance

`site/graph.json` and `site/details.json` are **generated artefacts**, built
by CI and the Pages deploy and **not committed** (they are gitignored).

Contributors never edit them, and never edit `site/index.html` to add an
entity. The source remains **Markdown + YAML frontmatter + `[[wikilinks]]`**
— nothing else.

Build them locally to run the validation tests or to view the site from a
clone (nothing to commit afterwards):

```bash
python tools/build_graph.py
```

The graph must always be reproducible from the repository.
The generated files are not committed; `tools/test_build_graph.py` asserts
that two builds of the same data are identical, and the deployment workflow
regenerates the graph before publishing.

The same rule keeps the two views consistent: **Obsidian** reads the
Markdown and wikilinks directly, and the **web graph** reads them through the
generator. Neither is authoritative over the source.

---

## 🏷️ Versions and releases

The Atlas carries two version numbers: a **schema version** (SemVer, in
`metadata/schema.json`) that changes when the data model does, and a dated
**data release** (`YYYY.MM.N`) for each snapshot. Releases are prepared
automatically from the merged pull requests: [`CHANGELOG.md`](CHANGELOG.md) says
what changed, the [Releases page](https://github.com/DaLuSt/Data-Initiatives-Atlas/releases)
holds the tagged snapshots, and [`metadata/versioning.md`](metadata/versioning.md)
explains the rules. The site's footer shows the release it was built from.

What is planned next is on the public
[Atlas roadmap board](https://github.com/users/DaLuSt/projects/1), fed by the repository's issues labelled
`roadmap`; [`docs/roadmap.md`](docs/roadmap.md) explains how it works.

## 🤝 An open participation model

The Atlas is intended to grow through participation. The Netherlands
provided the initial national contribution. But the Atlas is designed as an internationally extensible
project.

Contributors may:

- add a new country;
- establish a national knowledge area;
- add national initiatives;
- connect national initiatives to EU initiatives;
- connect national initiatives to international initiatives;
- improve existing entities;
- identify missing relationships;
- contribute new domains or standards.

A country does not need to wait for the Atlas to be complete before joining.

> *Countries can join incrementally and build their national representation
> over time.*

📋 Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) ·
🤝 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) sets the ground rules ·
🔐 [`SECURITY.md`](SECURITY.md) covers vulnerability reporting **and how to
report a sourcing or data-integrity problem**.

---

## 🎯 Design principles

| Principle | What it means |
|---|---|
| **Open by design** | Open to contributions from countries, organisations, researchers and individuals. |
| **Country-neutral ontology** | The core model is not designed around Dutch government structures. |
| **Local context, global connections** | National initiatives keep their local context while connecting to regional and international developments. |
| **Interoperability** | The same entity and relationship model works across countries. |
| **Evidence-based** | Factual claims are supported by authoritative sources wherever possible, with provenance recorded per relationship. |
| **Relationship-first** | The relationships between initiatives matter as much as the initiatives. |
| **Incremental participation** | Countries can start small and expand over time. |
| **Version-controlled** | Git gives a transparent history and enables distributed collaboration. |

---

## 🚀 Future vision

The long-term ambition is for the Atlas to become a shared international
knowledge layer for data governance and data ecosystems.

```
                         GLOBAL
                           │
                    ┌──────┴──────┐
                    │             │
                   UN       Other global
                    │        organisations
                    │
                  REGIONAL
                    │
          ┌─────────┼─────────┐
          │         │         │
         EU       Other      ...
          │       regions
          │
       NATIONAL
          │
   ┌──────┼──────┬──────┐
   │      │      │      │
  NL     DE     BE     ...
   │      │      │
   └──────┴──────┴──────┘
          │
       DOMAINS
          │
   ┌──────┼───────┐
 Mobility Health Government
```

The Netherlands is the first node in the national layer, not the endpoint.

---

## 💜 Support this project

The Atlas is free, open and maintained without funding. If it's useful to
you, consider [sponsoring it on GitHub](https://github.com/sponsors/DaLuSt)
— it helps keep the research and the infrastructure going.

---

## 📜 Licence

Original content contributed to the Atlas is released under
**[Creative Commons Zero v1.0 Universal (CC0 1.0)](LICENSE)**, to maximise
reuse and minimise barriers for countries, organisations, researchers,
developers and other projects.

Third-party source material remains subject to its own licensing and reuse
conditions.

[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) is adapted from the Contributor
Covenant and keeps that document's own **CC BY 4.0** licence and attribution,
as its terms require. Everything else in this repository is CC0.

---

<div align="center">

### One global landscape. Many countries. Connected initiatives.

**Start local. Connect globally. Build together.**

[**→ Open the Interactive Atlas**](https://dalust.github.io/Data-Initiatives-Atlas/)

</div>
