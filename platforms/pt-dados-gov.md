---
id: PT-DADOS-GOV
type: platform
name: dados.gov.pt
alternative_names:
  - dados.gov
  - Portal de Dados Abertos
  - Portuguese open data portal
description: >
  Portugal's national open data portal, publishing datasets from Portuguese
  public bodies.

level: national
country: PT
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
  - PT
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "dados.gov.pt is Portugal's national open data portal, publishing open data from Portuguese public administration bodies (dados.gov.pt). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "dados.gov.pt — Portal de Dados Abertos"
    url: "https://dados.gov.pt/"
    publisher: "Governo de Portugal"
  - title: "Open Data Directive"
    url: "https://digital-strategy.ec.europa.eu/en/policies/open-data"
    publisher: "European Commission — Shaping Europe's digital future"
---

# dados.gov.pt

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

dados.gov.pt is Portugal's national open data portal.

## The fifth portal without a custodian

[[NL-DATA-OVERHEID]], [[ES-DATOS-GOB-ES]], [[IE-DATA-GOV-IE]] and now this
one carry no `maintained-by` edge. [[PT-AMA]] is the obvious operator and no
source read says so.

Only [[CH-OPENDATA-SWISS]] has a sourced custodian, because [[CH-BFS]] says
in its own words that it operates the portal. One in five.

## Portugal's Open Data Directive transposition is not identified

Joining Belgium, France, Spain and Ireland on that list. Five countries is
comfortably a batch of its own, and it is recorded as such in
`discovery/research-queue.md`.

## Relationships

- `part-of` [[PT]] — an anchor edge.

## Sources

Listed in frontmatter.
