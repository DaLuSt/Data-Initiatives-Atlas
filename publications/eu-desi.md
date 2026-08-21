---
id: EU-DESI
type: publication
name: Digital Economy and Society Index
alternative_names:
  - DESI
description: >
  Composite index published by the European Commission summarising indicators
  on Europe's digital performance and tracking the evolution of EU member
  states across four dimensions: human capital, connectivity, integration of
  digital technology, and digital public services. The Commission has
  monitored member states' digital progress through DESI since 2014. As of
  2023, in line with the Digital Decade Policy Programme 2030, DESI is
  integrated into the annual State of the Digital Decade report and used to
  monitor progress towards the Digital Decade targets rather than published
  as a standalone index.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2014-01-01
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-COMMISSION
related_entities:
  - EU
  - EU-COMMISSION
  - EU-DIGITAL-DECADE
  - EU-EGOV-BENCHMARK
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "The Digital Economy and Society Index (DESI) is a composite index published by the European Commission that summarises relevant indicators on Europe's digital performance and tracks the evolution of EU Member States (digital-strategy.ec.europa.eu/en/policies/desi). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity."
    confidence: medium
    valid_from: 2014-01-01
    valid_until: null
  - type: part-of
    target: EU-DIGITAL-DECADE
    source: fact
    evidence: "As of 2023, and in line with the Digital Decade Policy Programme 2030, DESI is now integrated into the State of the Digital Decade report and used to monitor progress towards the digital targets (digital-strategy.ec.europa.eu/en/policies/desi; digital-strategy.ec.europa.eu 'Digital Decade 2025: DESI methodological note'). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-01-01
    valid_until: null

sources:
  - title: "The Digital Economy and Society Index (DESI)"
    url: "https://digital-strategy.ec.europa.eu/en/policies/desi"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Digital Decade 2025: DESI methodological note"
    url: "https://digital-strategy.ec.europa.eu/en/library/digital-decade-2025-desi-methodological-note"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Digital Public Services in the Digital Economy and Society Index"
    url: "https://digital-strategy.ec.europa.eu/en/policies/desi-digital-public-services"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Digital Decade DESI visualisation tool"
    url: "https://digital-decade-desi.digital-strategy.ec.europa.eu/datasets/desi/charts"
    publisher: "European Commission — Shaping Europe's digital future"
---

# DESI — Digital Economy and Society Index

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval of
> `digital-strategy.ec.europa.eu` is blocked by the network egress proxy.
> `verification: search-only`.

## Description

A **composite index** summarising indicators on Europe's digital performance
and tracking member states' evolution across four dimensions:

| Dimension |
|---|
| Human capital |
| Connectivity |
| Integration of digital technology |
| Digital public services |

The Commission has monitored member states' digital progress through DESI
**since 2014**.

## It is no longer published on its own

**As of 2023**, in line with the Digital Decade Policy Programme 2030, DESI
is **integrated into the annual State of the Digital Decade report** and used
to monitor progress towards the Digital Decade targets. The standalone DESI
reports run 2014–2022; the visualisation tool marks that series *"until
2022"*, and the methodological notes from 2024 onward are titled *Digital
Decade DESI*.

This is why the entity is `status: active` rather than `superseded`. The
index still exists and is still computed; what changed is the publication it
appears in. `supersedes` would need a successor publication entity and would
misdescribe an index that was absorbed rather than replaced.

## The Atlas's first `type: publication` entity

`discovery/candidates.md` recorded `publication` as one of the entity types
the vocabulary defines and nothing uses — **0 uses** against 17 defined types
— and named DESI and the [[EU-EGOV-BENCHMARK]] as the highest-value seeds,
because they *"would give the Atlas its first comparative-measurement
layer"*.

That is what these two entities are for. Everything else the Atlas holds is
an instrument, a body, a system or a standard: things that **prescribe**.
DESI and the eGovernment Benchmark **measure**, and until now there was
nowhere in the graph to say that some entities exist to score other entities'
countries.

## What is deliberately not asserted

No `applies-in` or `references` edge is asserted to any of the 27 member
states DESI covers. An index measuring a country is not an instrument
applying in it, and no relationship type in `metadata/relationship-types.md`
means "measures". Twenty-seven edges of the wrong type would be worse than
none.

Whether a `measures` type is warranted is a real question, now that two
entities would use it. It is raised in `discovery/candidates.md` rather than
decided here, because a type added in the same batch that creates its only
two instances has not been tested against anything.

## Relationships

- `part-of` [[EU]] — anchor edge.
- `part-of` [[EU-DIGITAL-DECADE]] — the report DESI is now published inside.

## Sources

Listed in frontmatter — the Commission's DESI policy page, the 2025
methodological note, the digital public services dimension page, and the
visualisation tool.
