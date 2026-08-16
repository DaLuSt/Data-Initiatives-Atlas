---
id: BE
type: country
name: Belgium
alternative_names:
  - Kingdom of Belgium
  - België
  - Belgique
  - Belgien
description: >
  Country anchor entity for Belgium, the third national scope covered by the
  Data Initiatives Atlas. Used as the target of `country` fields and
  `applies-in` relationships for Belgian-scoped entities.

level: national
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "BE — Belgium (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:BE"
    publisher: "International Organization for Standardization (ISO)"
---

# Belgium

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited page was confirmed to exist but was not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Belgium (ISO 3166-1 alpha-2: `BE`) is the **third country** populated in
the Data Initiatives Atlas, after [[NL]] and [[DE]].

Belgian entities live in the same flat type folders as Dutch, German and EU
ones, tagged `country: BE`. EU instruments that apply in Belgium reference
it via an `applies-in` relationship — the same single entity that already
carries `applies-in` to the Netherlands and Germany.

## What the third country was for

Germany demonstrated that the country-neutral model is reusable. It also
found one limitation: **the `level` vocabulary is lossy for federal
states**, with no term between `national` and `local` for a German Land.
`progress/backlog.md` recorded the obvious follow-up — *"a third would test
whether the limitation is general."*

**It is general, and Belgium makes it worse.**

In Germany the problem is that no term fits. In Belgium the problem is that
the term that would fit is **already taken**:

- Belgium is a federation of **Regions** (Flanders, Wallonia,
  Brussels-Capital) and **Communities** (Flemish, French, German-speaking).
- In this Atlas, `level: regional` means **supra-national** — it is what
  [[EU]] and every `EU-` entity carries.

So a Belgian Region cannot even borrow the word. Recording Digitaal
Vlaanderen at `level: regional` would place a sub-national agency in the
same band as the European Union, which is worse than not modelling it.

The consequence is concrete and is not a small omission:

| Not modelled | Why it matters |
|---|---|
| **OSLO** (Open Standaarden voor Linkende Organisaties) | One of Europe's most developed public-sector **semantic interoperability** and linked-data standards programmes, and squarely in this Atlas's subject matter. A product of Digitaal Vlaanderen — a Flemish, not federal, body. |
| Digitaal Vlaanderen, Agence du Numérique, Paradigm | The Region-level digital agencies that do much of Belgium's actual public-sector digitalisation. |
| The Communities | Education and culture data policy sits here, not federally. |

Belgium is therefore the country whose Atlas coverage most **understates**
the reality: the federal layer recorded here is genuinely only part of
Belgian public-sector data governance. That is stated plainly rather than
left for a reader to discover.

No sub-national level was invented — for one country, or now for three.
Doing so is the country-specific ontology change the model exists to
prevent. This is logged in `discovery/unresolved.md`, and after three
countries it is the Atlas's best-evidenced ontology defect.

## What Belgium confirmed rather than broke

Everything else held, again, with no change to `metadata/schema.json`,
`metadata/ontology.md`, `metadata/taxonomy.md`,
`metadata/relationship-types.md`, the folder structure, any validation rule
or the graph generator:

- **No `BE-EU-*` entity.** [[EU-GDPR]] is still one entity; it now applies
  in three countries and is implemented by three national acts.
- **[[EU-NIS2]] now has three national transpositions**, and the three
  differ in date *and* technique — see [[BE-NIS2-WET]].
- **The DCAT chain forks three ways** — [[EU-DCAT-AP]] now has Dutch,
  German and Belgian national profiles.

## A note the other two countries did not need

Belgium has **three official languages** (Dutch, French, German). Entity
`name` fields use the Dutch form where the sources found were Dutch, with
the French form in `alternative_names`. That is a sourcing artefact, not a
statement about which language is authoritative — Belgian federal bodies
are equally `FOD BOSA` and `SPF BOSA`, `KSZ` and `BCSS`.

The Atlas has no field for a multilingual name, and did not gain one for
Belgium. Logged in `discovery/unresolved.md`.

## Relationships

See `countries/be/index.md` for the curated index of Belgian entities.

## Sources

Listed in frontmatter. **No `accessed` date and no `last_verified`** —
nothing about this entity has been checked against a source.
