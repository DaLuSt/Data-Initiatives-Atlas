---
id: DK-GRUNDDATA
type: programme
name: Grunddataprogrammet
alternative_names:
  - Grunddata
  - The Basic Data Programme
  - Danish basic data
description: >
  Danish programme combining the basic registrations about Denmark and its
  citizens under the common term basic data, standardised so that they can
  be combined and used coherently. The registrations are held in public
  registers including the Civil Registration System, the Central Business
  Register and the Building and Housing Register, and are distributed
  through the Datafordeler.

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
  - DK-DATAFORDELER
  - DK-DIGST
  - NL-BASISREGISTRATIES
relationships:
  - type: part-of
    target: DK
    source: fact
    evidence: "The Basic Data Programme is a public body of DK; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Both are national programmes that designate a defined set of public registers as authoritative base data and standardise them so they can be combined; the Danish programme names the Civil Registration System, the Central Business Register and the Building and Housing Register among its registrations, and distributes them through a shared distributor (grunddata.dk; datafordeler.dk 'Grunddata'). NOT READ - search-only. Recorded as a comparison, not a dependency - neither programme derives from the other."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Grunddata"
    url: "https://datafordeler.dk/vejledning/grunddata/"
    publisher: "Datafordeler / Klimadatastyrelsen"
  - title: "Grunddata - English"
    url: "http://grunddata.dk/english/"
    publisher: "Grunddata.dk"
  - title: "Good basic data for everyone - a driver for growth and efficiency"
    url: "https://ec.europa.eu/isa2/sites/isa/files/isa-2-conference/3-berneke-background-info.pdf"
    publisher: "European Commission / ISA2"
---

# Grunddataprogrammet

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Denmark's basic data programme - and the closest thing in the Atlas to
a controlled comparison.

## The direct analogue of the Dutch stelsel

The Atlas models the ten Dutch [[NL-BASISREGISTRATIES]] in more depth
than anything else it holds: ten registers, their holders, and the seven
statutes beneath them. Until now there was nothing to compare that
against.

Grunddata is the same idea in another jurisdiction - a defined set of
public registers designated as authoritative, standardised so they
combine, distributed through one channel ([[DK-DATAFORDELER]]).

The differences are where the value is, and the Atlas can now hold them:
the Dutch stelsel rests on **seven statutes** while the Danish programme
came out of a **digitalisation strategy**; the Dutch registers are
distributed by their own holders while Denmark built a **single
distributor**.

The `related-to` edge is deliberately weak. Neither programme derives
from the other, and asserting anything stronger would invent a lineage.

## Sources

Listed in frontmatter.
