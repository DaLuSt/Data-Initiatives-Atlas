---
id: FI-PALVELUVAYLA
type: platform
name: Suomi.fi Data Exchange Layer
alternative_names:
  - Suomi.fi-palveluvayla
  - Suomi.fi-palveluväylä
  - Finnish X-Road instance
description: >
  Finland's national data exchange layer, the Finnish deployment of the
  X-Road software. Finland co-founded the Nordic Institute for
  Interoperability Solutions with Estonia in 2017 to develop and
  strategically manage X-Road jointly, rather than each country
  maintaining its own fork.

level: national
country: FI
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FI
  - FI-DVV
  - INTL-X-ROAD
  - INTL-NIIS
  - EE-X-TEE
relationships:
  - type: part-of
    target: FI
    source: fact
    evidence: "The Suomi.fi Data Exchange Layer is a public body of FI; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: INTL-X-ROAD
    source: fact
    evidence: "NIIS is a non-profit association established in 2017 by the governments of Estonia and Finland with the mission to ensure the development and strategic management of X-Road and other cross-border solutions for digital government infrastructure; X-Road is released under the MIT licence and used internationally (niis.org 'History'; e-estonia.com 'NIIS'; en.wikipedia.org 'X-Road'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: FI-DVV
    source: fact
    evidence: "DVV develops and maintains the centralised support services for e-services, which include the Suomi.fi services (dvv.fi 'About the agency'; suomi.fi organisation page). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Nordic Institute for Interoperability Solutions - History"
    url: "https://www.niis.org/history"
    publisher: "Nordic Institute for Interoperability Solutions (NIIS)"
  - title: "X-Road"
    url: "https://en.wikipedia.org/wiki/X-Road"
    publisher: "Wikipedia"
  - title: "Digital and Population Data Services Agency"
    url: "https://dvv.fi/en/digital-and-population-data-services-agency"
    publisher: "Digital and Population Data Services Agency (DVV)"
---

# Suomi.fi Data Exchange Layer

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The Finnish half of the only jointly-governed platform in the Atlas.

## Why this entity completes something

[[EE-X-TEE]] and this entity are **two national deployments of one
shared codebase**, [[INTL-X-ROAD]], governed by [[INTL-NIIS]] - an
association Estonia and Finland founded together in 2017 and Iceland
joined in 2021.

Every other platform in the Atlas is one country's own: [[NL-DIGIKOPPELING]],
[[ES-CLAVE]], [[FR-FRANCECONNECT]]. This is the first case of two states
sharing the artefact and the governance, and it could not be shown with
Estonia alone - which is exactly why the shortlist ranked Estonia and
Finland as a pair.

## Relationships

- `based-on` [[INTL-X-ROAD]], alongside [[EE-X-TEE]].
- `maintained-by` [[FI-DVV]].

## Sources

Listed in frontmatter.
