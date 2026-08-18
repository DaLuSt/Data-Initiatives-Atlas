<div align="center">

# 🌍 Data Initiatives Atlas

**Mapping the data landscape across the UN, EU and participating countries
as an open, connected knowledge graph.**

### [**→ Open the Interactive Atlas**](https://dalust.github.io/Data-Initiatives-Atlas/)

*Search, filter and explore 340 entities and 3,932 connections across ten
countries — no install, no account.*

[![Validation](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/validate.yml/badge.svg)](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/validate.yml)
[![Pages](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/pages.yml/badge.svg)](https://github.com/DaLuSt/Data-Initiatives-Atlas/actions/workflows/pages.yml)
[![Licence: CC0-1.0](https://img.shields.io/badge/licence-CC0--1.0-blue.svg)](LICENSE)

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
| **Entities** | 340 |
| **Connections** | 3,932 — of which **498** are sourced, typed relationships |
| **Countries** | 🇳🇱 Netherlands · 🇩🇪 Germany · 🇧🇪 Belgium · 🇫🇷 France · 🇪🇸 Spain · 🇵🇱 Poland · 🇬🇧 United Kingdom |
| **Layers** | UN · EU · national · sectoral |
| **Source of truth** | Git + Markdown/YAML — no database |
| **Licence** | CC0 1.0 |

*Figures as of 2026-08-17. The live counts are always on the site itself.*

### Explore it

| Where | What you get |
|---|---|
| **[The interactive graph](https://dalust.github.io/Data-Initiatives-Atlas/)** | Search by name, ID, country, type or domain. Filter by level, country, region, **domain**, type, status, relationship type — and by **provenance and confidence**, so you can isolate what a source states from what the Atlas concludes. A sidebar control switches the Global Atlas between a **grouped** arrangement (bands by level, blocks by country) and a **force-directed** one that pulls connected entities together. The **Compare** view puts one supra-national instrument per row and one country per column, so you can see who implemented what — generated from the graph, not hand-written. Click any entity for its metadata, sourced relationships and citations, and a link to the underlying Markdown. |
| **This repository** | The source of truth. Browse `countries/`, `legislation/`, `organisations/` and the rest directly. |
| **As an Obsidian vault** | Open the repository folder in Obsidian and the `[[wikilinks]]` become a local graph. |

📖 [`docs/graph.md`](docs/graph.md) is a tour of the site ·
[`docs/graph-architecture.md`](docs/graph-architecture.md) explains how
entity files become nodes and edges.

---

## Why

Data governance is shaped by initiatives operating at different levels:

```
An international principle   →   influences an EU strategy
An EU regulation             →   leads to national implementation
A national programme         →   establishes a framework
A framework                  →   references standards
Standards                    →   underpin data spaces and technical ecosystems
```

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

```
United Nations
      │
      ▼
European Union
      │
      ▼
European Initiative
      │
      ├──────────────► Netherlands
      │                    │
      │                    ├── National initiative
      │                    ├── Framework
      │                    └── Data ecosystem
      │
      ├──────────────► Germany
      │                    │
      │                    ├── National initiative
      │                    ├── Framework
      │                    └── Data ecosystem
      │
      ├──────────────► Belgium
      │                    │
      │                    ├── National initiative
      │                    ├── Framework
      │                    └── Data ecosystem
      │
      ├──────────────► France
      │                    │
      │                    ├── National initiative
      │                    ├── Framework
      │                    └── Data ecosystem
      │
      ├──────────────► Spain
      │                    │
      │                    ├── National initiative
      │                    ├── Framework
      │                    └── Data ecosystem
      │
      ├──────────────► Poland
      │                    │
      │                    ├── National initiative
      │                    ├── Framework
      │                    └── Data ecosystem
      │
      └──────────────► Country G

United Kingdom  ◄── not below the EU branch: a non-member state
      │
      ├── National initiative
      ├── Framework
      └── Data ecosystem
```

The Netherlands is the starting point, not the boundary of the project — and
since the United Kingdom joined, the EU is not the only route into a national
scope either.

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

The Netherlands is the first participating country; Germany, Belgium,
France, Spain, Poland and the United Kingdom followed. Additional countries
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

> **That claim has been tested seven times, and the seventh was the real
> test.** Adding Germany, Belgium, France, Spain and Poland each required no
> change to the schema, ontology, taxonomy, relationship types, folder
> structure or any validation rule — but all five are EU member states. The
> **United Kingdom is not**, so no EU instrument carries `applies-in` to it
> and its entities are the first with `region: null`. That needed no change
> either. See
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
 └── Relationships to EU / international initiatives
```

This makes the project suitable for both individual contributors and
organised national communities.

---

## 🧩 What is being mapped

The Atlas is built on a common ontology applied identically at
international, regional and national levels.

**Core entity types**

`initiative` · `organisation` · `country` · `region` · `policy` · `law` ·
`regulation` · `directive` · `strategy` · `standard` · `framework` ·
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

```
International Initiative
        │
        ▼
EU Strategy
        │
        ▼
EU Regulation
        │
        ├──────────────► Netherlands
        │                    │
        │                    └── National implementation
        │
        ├──────────────► Germany
        │                    │
        │                    └── National implementation
        │
        ├──────────────► Belgium
        │                    │
        │                    └── National implementation
        │
        ├──────────────► France
        │                    │
        │                    └── National implementation
        │
        ├──────────────► Spain
        │                    │
        │                    └── National implementation
        │
        └──────────────► Poland
                             │
                             └── National implementation
```

This lets the Atlas represent **horizontal** relationships between countries
and **vertical** relationships between international, regional and national
levels.

**Relationship types include**

`influences` · `implements` · `implements-requirement-from` · `applies-to` ·
`applies-in` · `derived-from` · `based-on` · `references` · `related-to` ·
`depends-on` · `supersedes` · `implemented-by` · `governed-by` ·
`maintained-by` · `participates-in` · `part-of`

Every relationship records whether it is a **sourced fact** or an **Atlas
interpretation**, with the evidence and a confidence level attached.

---

## 🗂️ Repository structure

The repository is structured around **entities**, not around individual
countries.

```
data-initiatives-atlas/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
│
├── .github/
│   └── workflows/
│       ├── validate.yml    # validation — runs on every pull request
│       └── pages.yml       # build + deploy the graph — main only
│
├── initiatives/
├── legislation/
├── policies/
├── strategies/
├── standards/
├── frameworks/
├── programmes/
├── organisations/
├── data-spaces/
├── platforms/
├── publications/
├── domains/
│
├── countries/
│   ├── nl/
│   ├── de/
│   ├── be/
│   ├── fr/
│   ├── es/
│   └── pl/
│
├── regions/
│   └── eu/
│
├── international/
│   └── un/
│
├── metadata/
│   ├── ontology.md
│   ├── taxonomy.md
│   ├── relationship-types.md
│   ├── metadata-schema.md
│   ├── controlled-vocabularies.md
│   └── schema.json
│
├── templates/
├── discovery/
├── validation/
├── progress/
│
├── tools/                  # graph generator + its tests
│   ├── build_graph.py
│   ├── test_build_graph.py
│   └── test_ui.mjs
│
├── site/                   # the published GitHub Pages application
│   ├── index.html
│   ├── app.css
│   ├── app.js
│   ├── graph.json          # GENERATED — do not hand-edit
│   ├── details.json        # GENERATED — do not hand-edit
│   └── vendor/             # Cytoscape.js (MIT), vendored, no CDN
│
└── docs/
    ├── graph.md
    ├── graph-architecture.md
    ├── graph-development.md
    └── github-pages.md
```

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

`site/graph.json` and `site/details.json` are **generated artefacts**.

Contributors never edit them, and never edit `site/index.html` to add an
entity. The source remains:

```
Markdown  +  YAML frontmatter  +  [[wikilinks]]
```

Regenerate after changing entity data:

```bash
python tools/build_graph.py
```

The graph must always be reproducible from the repository.
`tools/test_build_graph.py` fails if the committed graph no longer matches
the entity files, and the deployment workflow regenerates it before
publishing regardless.

The same rule keeps the two views consistent: **Obsidian** reads the
Markdown and wikilinks directly, and the **web graph** reads them through the
generator. Neither is authoritative over the source.

---

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
