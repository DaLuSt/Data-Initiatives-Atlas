---
id: DE-AEROSPACE-X
type: data-space
name: Aerospace-X
alternative_names:
  - Aerospace-X data space
description: >
  German lighthouse project under Manufacturing-X, building a federated
  data-space platform for aerospace supply chains, covering use cases such
  as demand/capacity management, cross-company carbon-footprint
  calculation and digital product passports. Led industrially by Airbus
  Operations GmbH, with Fraunhofer ISST coordinating the participating
  Fraunhofer institutes, funded by the German Federal Ministry for
  Economic Affairs and Energy (BMWE) with NextGenEU support, the project
  ran from 1 April 2024 to June 2026.

level: sectoral
country: DE
region: EU

status: completed
confidence: medium
coverage: medium
verification: primary-source

start_date: 2024-04-01
end_date: 2026-06-30
last_verified: "2026-09-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - DE-MANUFACTURING-X
  - DE-CATENA-X
  - DE-FACTORY-X
relationships:
  - type: part-of
    target: DE-MANUFACTURING-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own Aerospace-X page directly (2026-09-20), which states Aerospace-X operates 'as part of the Manufacturing-X initiative, which focuses on the digitalization of supply chains,' transferring lessons from Gaia-X, Catena-X and the Industrie 4.0 Platform to the aviation sector. Fraunhofer IPT's own page, also read directly, independently confirms the project is 'supported by the Federal Ministry of Economics and Energy through the Manufacturing-X program,' funding code 13MX004A."
    confidence: high
    valid_from: "2024-04-01"
    valid_until: null
  - type: based-on
    target: DE-CATENA-X
    source: fact
    evidence: "Confirmed by reading Fraunhofer ISST's own page directly (2026-09-20): the project 'transfers lessons from related efforts like Gaia-X, Catena-X and Industry 4.0 Platform to the aviation sector.' Recorded as `based-on` [[DE-CATENA-X]] on the same basis [[DE-FACTORY-X]] already carries, since Catena-X is the family's own originating data space in the Atlas."
    confidence: medium
    valid_from: "2024-04-01"
    valid_until: null

sources:
  - title: "Aerospace-X: Ecosystem for an efficient and sustainable Aerospace Supply Chain"
    url: "https://www.isst.fraunhofer.de/en/departments/industrial-manufacturing/projects/aerospace-x.html"
    publisher: "Fraunhofer ISST"
    accessed: "2026-09-20"
  - title: "Aerospace-X"
    url: "https://www.ipt.fraunhofer.de/en/projects/aerospace-x.html"
    publisher: "Fraunhofer IPT"
    accessed: "2026-09-20"
---

# Aerospace-X

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md` row
> #131 ("Factory-X, Aerospace-X, energy data-X, Plattform Industrie 4.0
> not modelled"), whose Factory-X half closed in PR #276. Sourced from
> Fraunhofer ISST's own page and Fraunhofer IPT's own page, both read
> directly. Construct-X, HealthTrack-X and Plattform Industrie 4.0 remain
> unmodelled — see "Not modelled" below.

## Description

Aerospace-X is a **lighthouse project under [[DE-MANUFACTURING-X]]**,
building a federated data-space platform for **aerospace supply chains**.
Confirmed by reading Fraunhofer ISST's own page directly: its stated aim
is standardising and improving those supply chains, with named use cases
including demand/capacity management, cross-company **product
carbon-footprint** calculation, and **digital product passports** for
components and aircraft.

**Industrially led by Airbus Operations GmbH**, per Fraunhofer IPT's own
page, with **Fraunhofer ISST coordinating** the participating Fraunhofer
institutes (IFAM, IPT, ISST and IPK, per IPK's own page, not independently
re-fetched here). Partner counts differ slightly between the two sources
read directly: ISST's own page gives **33 organisations** including
Airbus, Rolls-Royce, MTU Aero Engines, SAP and Capgemini; IPT's own page
gives **14 top-class partners plus 16 associated partners** (30 total).
Both figures are recorded rather than reconciled, since neither source
read contradicts the other outright — they may be counting different
tiers of participation.

Funded by the German Federal Ministry for Economic Affairs and Energy
(BMWE), grant reference 13MX004F (ISST) / 13MX004A (IPT), with
**NextGenEU** support per ISST's own page.

## Timeline

Ran from **1 April 2024** to **June 2026** — confirmed independently on
both sources read directly.

## Not modelled

- **Construct-X**, **HealthTrack-X** — the remaining named lighthouse
  projects/siblings on [[DE-MANUFACTURING-X]]'s own entity, not
  independently researched this pass.
- **Plattform Industrie 4.0** — the concept base Manufacturing-X and its
  lighthouse projects build on.
- Aerospace-X's **individual named partners** (Airbus, Rolls-Royce, MTU
  Aero Engines, SAP, Capgemini and others).

## Relationships

- `part-of` [[DE-MANUFACTURING-X]] — `confidence: high`.
- `based-on` [[DE-CATENA-X]] — `confidence: medium`.

## Sources

Listed in frontmatter, both read directly.
