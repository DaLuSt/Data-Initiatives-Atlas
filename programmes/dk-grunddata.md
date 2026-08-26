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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
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
    evidence: "The Basic Data Programme is a public body of DK; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading datafordeler.dk's own 'Grunddata' page directly (2026-08-25): it lists the registers under Grunddata by name, including 'Det Centrale Personregister (CPR)' (the Civil Registration System), 'Det Centrale Virksomhedsregister (CVR)' (the Central Business Register) and 'Bygnings- og Boligregistret (BBR)' (the Building and Housing Register), matching this entity's claim exactly. A European Commission ISA2 conference document, also read directly, adds a specific origin this entity did not previously carry: 'The basic data program was established in 2012 as part of the e-government strategy agreed between the Danish Government, Local Government Denmark and Danish Regions.' `grunddata.dk` no longer resolves (checked https and http) — a dead domain, not a bot-wall, confirmed again this pass. Recorded as a comparison, not a dependency - neither programme derives from the other."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Grunddata"
    url: "https://datafordeler.dk/vejledning/grunddata/"
    publisher: "Datafordeler / Klimadatastyrelsen"
    accessed: "2026-08-25"
  - title: "Good basic data for everyone - a driver for growth and efficiency"
    url: "https://ec.europa.eu/isa2/sites/isa/files/isa-2-conference/3-berneke-background-info.pdf"
    publisher: "European Commission / ISA2"
    accessed: "2026-08-25"
  - title: "Grunddata - English"
    url: "http://grunddata.dk/english/"
    publisher: "Grunddata.dk"
---

# Grunddataprogrammet

> **Verified 2026-08-25.** `datafordeler.dk` and the European
> Commission's ISA2 document were both read directly. The programme's
> own register list matches this entity's claims exactly, and the ISA2
> document adds a specific origin — a 2012 e-government strategy agreed
> between the Danish state, Local Government Denmark and the Danish
> regions — this entity did not previously carry. `grunddata.dk`
> remains dead (no DNS resolution).

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

## A 2012 origin, confirmed

The European Commission's own ISA2 conference document, read directly
this pass, dates the programme precisely: "The basic data program was
established in 2012 as part of the e-government strategy agreed
between the Danish Government, Local Government Denmark and Danish
Regions." This is the first specific establishment date this entity
has carried.

## Sources

Listed in frontmatter. `datafordeler.dk` and the ISA2 document were
read directly this pass; `grunddata.dk` remains dead — no DNS
resolution over either https or http, confirmed again this pass.
