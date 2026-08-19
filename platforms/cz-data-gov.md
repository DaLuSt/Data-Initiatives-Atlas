---
id: CZ-DATA-GOV
type: platform
name: data.gov.cz
alternative_names:
  - Národní katalog otevřených dat
  - Czech National Open Data Catalogue
description: >
  Czechia's national open data catalogue, publishing datasets from Czech
  public bodies.

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ
  - CZ-DIA
relationships:
  - type: part-of
    target: CZ
    source: fact
    evidence: "data.gov.cz is the Czech national open data catalogue (Národní katalog otevřených dat), publishing open data from Czech public bodies (data.gov.cz). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gov.cz — Národní katalog otevřených dat"
    url: "https://data.gov.cz/"
    publisher: "Digitální a informační agentura / Government of the Czech Republic"
---

# data.gov.cz

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

data.gov.cz is Czechia's national open data catalogue.

## The seventh portal without a sourced custodian

[[CZ-DIA]] is the obvious operator, and [[CZ-ZAKON-60-2026]] makes DIA the
node connecting Czech data sources to the European data portal — which is
adjacent to running the national catalogue and **is not the same claim**.

No `maintained-by` edge is asserted. Seven national portals in the Atlas now
lack a custodian and one has it.

## Relationships

- `part-of` [[CZ]] — an anchor edge.

## Sources

Listed in frontmatter.
