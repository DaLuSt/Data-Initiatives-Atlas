Data Initiatives Atlas

«Mapping the data landscape across the UN, EU and participating countries as an open, connected knowledge graph.»

Data Initiatives Atlas is an open, machine-readable knowledge base for mapping and connecting data-related initiatives, legislation, policies, standards, frameworks, programmes, organisations and data ecosystems across international, regional and national levels.

The Netherlands is the first participating country, providing the initial national implementation of the Atlas. The underlying information model is deliberately designed to support the addition of other countries over time.

---

🌍 Why Data Initiatives Atlas?

Data governance is increasingly shaped by initiatives operating at different levels.

An international principle can influence an EU strategy.
An EU regulation can lead to national implementation.
A national programme can establish a framework.
A framework can reference standards.
Standards can underpin data spaces and technical ecosystems.

These relationships are often distributed across many websites, documents and organisations.

Data Initiatives Atlas brings them together into one connected knowledge base.

«The objective is not simply to create a catalogue, but to make the relationships between initiatives visible.»

---

🧭 Vision

The long-term vision is to create a global, open Data Governance Atlas that connects international, regional and national data initiatives.

The Atlas should allow users to navigate from an international initiative to its regional and national implications, related standards, responsible organisations and affected data domains.

For example:

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
      ├──────────────► Country B
      │
      └──────────────► Country C

The Netherlands is the starting point, not the boundary of the project.

---

🌐 Geographic Scope

The Atlas uses a multi-level geographic model.

International

International initiatives and organisations, including the United Nations and other global institutions.

Examples include:

- International principles
- Global strategies
- International frameworks
- International standards
- Global programmes
- Cross-border initiatives

Regional

Regional initiatives and organisations.

The European Union is the initial regional focus.

Examples include:

- EU legislation
- EU strategies
- EU policies
- EU programmes
- European standards
- European data spaces
- European governance frameworks

The model should also allow other regional organisations and ecosystems to be added in the future.

National

National initiatives, legislation, strategies, frameworks, organisations and data ecosystems.

The Netherlands is the first participating country.

Additional countries can be added without changing the fundamental information model.

For example:

countries/
├── nl/
├── de/
├── be/
├── fr/
├── uk/
└── ...

Countries should only be added when there is sufficient information and, preferably, an active contributor or participating community maintaining that national scope.

---

🗺️ Country Participation Model

A country is not required to have the same depth or coverage as another country.

The Atlas supports incremental participation.

A country can initially contribute:

Country
 ├── National strategies
 ├── Key legislation
 ├── Major data initiatives
 └── Principal organisations

and progressively expand towards:

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

This makes the project suitable for both individual contributors and organised national communities.

---

🧩 What is being mapped?

The Atlas is designed around a common ontology that can be applied at international, regional and national levels.

Core entity types include:

Initiative
Organisation
Country
Region
Policy
Law
Regulation
Strategy
Standard
Framework
Programme
Data Space
Platform
Technology
Domain
Publication

The ontology is intentionally country-neutral.

Country-specific concepts can be represented through metadata and relationships rather than hard-coded into the core model.

---

🔗 Cross-Border Relationships

A key purpose of the Atlas is to make relationships between geographic levels visible.

For example:

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
        └──────────────► Belgium
                             │
                             └── National implementation

This allows the Atlas to represent both horizontal relationships between countries and vertical relationships between international, regional and national levels.

Examples of relationships include:

influences
implements
implements-in
applies-to
derived-from
based-on
references
related-to
depends-on
supersedes
implemented-by
governed-by
part-of

---

🗂️ Repository Structure

The repository should remain structured around entities rather than individual countries.

data-initiatives-atlas/
│
├── README.md
├── CONTRIBUTING.md
├── LICENSE
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
├── domains/
├── countries/
│   └── nl/
│
├── regions/
│   └── eu/
│
├── international/
│   └── un/
│
└── metadata/
├── ontology.md
├── taxonomy.md
├── relationship-types.md
├── controlled-vocabularies.md
└── validation-rules.md
|
|--- discovery/
     ├── candidates.md
     ├── unresolved.md
     ├── duplicates.md
     └── research-queue.md

As additional countries participate:

countries/
├── nl/
├── de/
├── be/
├── fr/
├── es/
└── ...

The repository should not require a redesign when a new country is introduced.

---

🤝 An Open Participation Model

Data Initiatives Atlas is intended to grow through participation.

The Netherlands provides the initial national contribution, but the Atlas is designed as an internationally extensible project.

Future contributors may:

- add a new country;
- establish a national knowledge area;
- add national initiatives;
- connect national initiatives to EU initiatives;
- connect national initiatives to international initiatives;
- improve existing entities;
- identify missing relationships;
- contribute new domains or standards.

A country does not need to wait for the Atlas to be complete before joining.

«Countries can join incrementally and build their national representation over time.»

---

🎯 Design Principles

Open by design

The Atlas should be open to contributions from countries, organisations, researchers and individuals.

Country-neutral ontology

The core data model should not be designed specifically around Dutch government structures.

Local context, global connections

National initiatives should retain their local context while being connected to international and regional developments.

Interoperability

The same entity and relationship model should work across countries.

Evidence-based

Factual information should be supported by authoritative sources wherever possible.

Relationship-first

Relationships between initiatives are as important as the initiatives themselves.

Incremental participation

Countries can start small and expand their representation over time.

Version-controlled

Git provides a transparent history of changes and enables distributed collaboration.

---

🚀 Future Vision

The long-term ambition is for Data Initiatives Atlas to become a shared international knowledge layer for data governance and data ecosystems.

A future Atlas could look conceptually like:

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

The Netherlands is therefore the first node in the national layer, not the endpoint.

«Start local. Connect globally. Build together.»

---

📜 Licence

The repository uses Creative Commons Zero v1.0 Universal (CC0 1.0) for original content contributed to the Atlas.

CC0 is intended to maximise reuse and minimise barriers for countries, organisations, researchers, developers and other projects consuming or contributing to the Atlas.

Third-party source material remains subject to its own licensing and reuse conditions.

---

🌍 The Principle

«One global landscape.
Many countries.
Connected initiatives.
Shared knowledge.»