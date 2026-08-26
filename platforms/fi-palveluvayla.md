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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading dvv.fi's own pages directly (2026-08-26), a government-operated service: anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: INTL-X-ROAD
    source: fact
    evidence: "Confirmed by reading niis.org's own history page and en.wikipedia.org's X-Road article directly (2026-08-26): cooperation began in 2013 when the Prime Ministers of Estonia and Finland signed a Memorandum of Understanding — 'considered to be the world's first digitally signed international agreement' — to develop and jointly manage X-Road; NIIS itself, per Wikipedia, 'was founded jointly in June 2017 by Finland and Estonia'; X-Road's central components were released under the MIT licence on 3 October 2016 (niis.org's history page dates the publication to '2015-2016' without a specific day); by 7 February 2018 Finland's and Estonia's data exchange layers were connected to one another."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: FI-DVV
    source: fact
    evidence: "Confirmed by reading dvv.fi's own pages directly (2026-08-26): DVV's 'About the agency' page lists 'Identification Data Exchange Layer' among its own services, and its main agency page confirms it is 'Maintaining the Population Information System' alongside the Suomi.fi services."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Nordic Institute for Interoperability Solutions - History"
    url: "https://www.niis.org/history"
    publisher: "Nordic Institute for Interoperability Solutions (NIIS)"
    accessed: "2026-08-26"
  - title: "X-Road"
    url: "https://en.wikipedia.org/wiki/X-Road"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
  - title: "Digital and Population Data Services Agency"
    url: "https://dvv.fi/en/digital-and-population-data-services-agency"
    publisher: "Digital and Population Data Services Agency (DVV)"
    accessed: "2026-08-26"
---

# Suomi.fi Data Exchange Layer

> **Verified 2026-08-26.** All three cited pages were read directly.
> NIIS's own history page and Wikipedia's X-Road article, read together,
> supply a precise chronology this entity previously only had in
> outline: the 2013 Memorandum of Understanding, NIIS's June 2017
> founding, and the 7 February 2018 date the two countries' data
> exchange layers were actually connected.

## Description

The Finnish half of the only jointly-governed platform in the Atlas.

## A precise chronology, found

Confirmed by reading niis.org's own history page directly: cooperation
between Estonia and Finland on X-Road began in **2013**, when the two
countries' Prime Ministers — Andrus Ansip and Jyrki Katainen — signed a
Memorandum of Understanding described as "the world's first digitally
signed international agreement." Reading en.wikipedia.org's X-Road
article independently adds three dates this entity did not previously
carry: **NIIS was founded in June 2017**; X-Road's central components
were released under the MIT licence on **3 October 2016**; and by
**7 February 2018**, Finland's and Estonia's data exchange layers were
actually connected to one another — the moment the "shared platform"
description became true in practice rather than in intent.

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

Listed in frontmatter, all three read directly this pass.
