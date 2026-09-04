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
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Belgium is one of the 27 member states of the European Union, having acceded on 1 January 1958; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "BE — Belgium (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:BE"
    publisher: "International Organization for Standardization (ISO)"
---

# Belgium

> **Verified 2026-08-21**, re-checked 2026-08-26. Every source this entity
> cites is on a domain the repository owner confirmed read and correct —
> `europa.eu`, `iso.org`. `verification: primary-source`. See
> `docs/re-verification.md` §"The confirmed domains". The 2026-08-26 pass
> re-verified the 24 Belgian entities that were still `verification:
> search-only`; see `countries/be/index.md` for the results.

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

**Resolved 2026-08-21, closed 2026-09-04.** `level: subnational` was
added to the schema, a genuine ontology change rather than a
country-specific workaround — it applies wherever a state's own
sub-national tier needs a term, not only in Belgium. The three Belgian
sub-federal open-data instruments were modelled under it first
([[BE-VL-BESTUURSDECREET-2021]], [[BE-BRU-ORDONNANCE-2021]],
[[BE-WAL-DECRET-2022]]). A research-queue pickup then closed the
organisational half of the gap this section originally documented:

| Previously not modelled | Now |
|---|---|
| **OSLO** | [[BE-OSLO]], `maintained-by` [[BE-DIGITAAL-VLAANDEREN]] |
| Digitaal Vlaanderen | [[BE-DIGITAAL-VLAANDEREN]] |
| Agence du Numérique | [[BE-AGENCE-NUMERIQUE]] |
| Paradigm | [[BE-PARADIGM]] |

**The Communities remain unmodelled** — education and culture data
policy sits here, not federally, and no Community-level digital agency
has been researched.

Belgium's Atlas coverage understated the reality for several weeks: the
federal layer recorded at first was genuinely only part of Belgian
public-sector data governance. That gap is now most of the way closed,
and the finding that prompted `level: subnational`'s creation is worth
keeping on record even though the entities it once blocked now exist.

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

## ⚠ Two dates, and why this entity uses 1958

A verification pass on 2026-08-20 supplied **25 March 1957** as this
country's accession date. This entity says **1 January 1958**. Both are
right, about different events:

| Date | Event |
|---|---|
| **25 March 1957** | the Treaty of Rome was **signed**, in Rome |
| **1 January 1958** | the Treaty **entered into force**, and the Communities existed |

Strictly neither is an *accession*. The six founding members — [[BE]],
[[DE]], [[FR]], [[IT]], [[LU]] and [[NL]] — did not accede to anything; they
founded it. "Accession date" is a column borrowed from the twenty-one states
that did join later.

The Atlas uses **1 January 1958** because that is what its own cited source
says: the Union's list of EU countries records the founding six under 1958,
and this entity's `part-of` [[EU]] evidence cites that page. Using 1957 would
put the entity in contradiction with the source it names.

**This is recorded rather than resolved.** The signature date is genuinely
useful and is now here; if the Atlas would rather key the founders on 1957,
the evidence strings and the cited source both need changing together.

## Sources

Listed in frontmatter. **No `accessed` date and no `last_verified`** —
nothing about this entity has been checked against a source.
