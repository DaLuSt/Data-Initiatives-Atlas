---
id: DK-DATAFORDELER
type: platform
name: Datafordeleren
alternative_names:
  - Datafordeler
  - The Data Distributor
description: >
  Denmark's public IT solution for the distribution of basic data. It
  emerged from a public digitalisation strategy, was implemented through
  the Basic Data Programme, and is operated by Klimadatastyrelsen. It
  distributes basic data about persons, companies, addresses, real estate,
  geography and maps.

level: national
country: DK
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
  - DK
  - DK-GRUNDDATA
relationships:
  - type: part-of
    target: DK
    source: fact
    evidence: "The Datafordeler is a public body of DK; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements
    target: DK-GRUNDDATA
    source: fact
    evidence: "Datafordeleren is the public IT solution for distribution of basic data; it emerged from a public digitalisation strategy, was implemented via the Basic Data Programme and is operated by Klimadatastyrelsen, and collects basic data about persons, companies, addresses, real estate, geographical data and maps (datafordeler.dk; grunddata.dk 'Datafordeleren'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Datafordeler.dk"
    url: "https://datafordeler.dk/"
    publisher: "Datafordeler / Klimadatastyrelsen"
  - title: "Datafordeleren"
    url: "http://grunddata.dk/datafordeleren/"
    publisher: "Grunddata.dk"
---

# Datafordeleren

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The single channel through which Danish basic data is distributed.

## One distributor, where the Netherlands has ten holders

This is the structural difference between [[DK-GRUNDDATA]] and
[[NL-BASISREGISTRATIES]] made concrete. Dutch registers are served by
their own holders - [[NL-KADASTER]], [[NL-KVK]], [[NL-RVIG]] and the
rest - coordinated through [[NL-DIGIKOPPELING]]. Denmark built one
distributor and put every basic register behind it.

**Klimadatastyrelsen**, which operates it, is not modelled.

## Sources

Listed in frontmatter.
