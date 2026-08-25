---
id: DK-DATAFORDELER
type: platform
name: Datafordeleren
alternative_names:
  - Datafordeler
  - The Data Distributor
description: >
  Denmark's public IT solution for the distribution of basic data — the
  single channel through which Danish authorities' basic data on
  persons, companies, addresses, real estate, water and climate, and
  maps and geography is made available. It emerged from a public
  digitalisation strategy and was implemented through the Basic Data
  Programme. Klimadatastyrelsen is its governing authority.

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
  - DK-GRUNDDATA
  - DK-KLIMADATASTYRELSEN
relationships:
  - type: part-of
    target: DK
    source: fact
    evidence: "Confirmed by reading datafordeler.dk directly (2026-08-25): 'Din indgang til offentlige Grunddata fra Danmarks myndigheder' (your gateway to public basic data from Denmark's authorities). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements
    target: DK-GRUNDDATA
    source: fact
    evidence: "Confirmed by reading datafordeler.dk directly (2026-08-25): the platform's own dataset overview groups its data by 'Personer, Fast ejendom, Virksomheder, Vand og klima, Landkort og geografi, Adresser, veje og områder' (persons, real property, businesses, water and climate, maps and geography, addresses/roads/areas) — the Basic Data Programme's own domains. `grunddata.dk`, cited here since this entity's creation, no longer resolves (DNS failure, tried both https and http) and is retained as a citation of record rather than removed, since a dead domain is not evidence the original claim was wrong."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: DK-KLIMADATASTYRELSEN
    source: fact
    evidence: "Confirmed verbatim by reading datafordeler.dk directly (2026-08-25): 'Klimadatastyrelsen er myndighed for Datafordeleren' — Klimadatastyrelsen is the governing authority for Datafordeleren. Corroborated by reading klimadatastyrelsen.dk's own 'Organisation' page directly, which names a dedicated internal 'Kontor for Datafordeleren' (Office for the Data Distributor) covering 'Datafordeleren, Grunddata-governance'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Datafordeleren"
    url: "https://datafordeler.dk/"
    publisher: "Datafordeler / Klimadatastyrelsen"
    accessed: "2026-08-25"
  - title: "Organisation — Klimadatastyrelsen"
    url: "https://klimadatastyrelsen.dk/om-klimadatastyrelsen/organisation"
    publisher: "Klimadatastyrelsen"
    accessed: "2026-08-25"
  - title: "Datafordeleren"
    url: "http://grunddata.dk/datafordeleren/"
    publisher: "Grunddata.dk"
---

# Datafordeleren

> **Verified 2026-08-25.** Closes the gap this entity itself named:
> "Klimadatastyrelsen, which operates it, is not modelled." Now
> [[DK-KLIMADATASTYRELSEN]], confirmed as this platform's governing
> authority in the platform's own words. `grunddata.dk` no longer
> resolves at all (checked both https and http) and is retained as a
> citation of record rather than removed.

## Description

Confirmed by reading datafordeler.dk directly (2026-08-25): "Din indgang
til offentlige Grunddata fra Danmarks myndigheder" — the single channel
through which Danish authorities' basic data is distributed. Its own
dataset overview groups that data as persons, real property, businesses,
water and climate, maps and geography, and addresses/roads/areas —
including the Central Person Register (CPR), the Central Business
Register (CVR), the Buildings and Housing Register (BBR) and the Address
Register (DAR), all named directly on the platform's homepage.

## One distributor, where the Netherlands has ten holders

This is the structural difference between [[DK-GRUNDDATA]] and
[[NL-BASISREGISTRATIES]] made concrete. Dutch registers are served by
their own holders - [[NL-KADASTER]], [[NL-KVK]], [[NL-RVIG]] and the
rest - coordinated through [[NL-DIGIKOPPELING]]. Denmark built one
distributor and put every basic register behind it.

## Who operates it, confirmed in the platform's own words

Confirmed verbatim by reading datafordeler.dk directly (2026-08-25):
"Klimadatastyrelsen er myndighed for Datafordeleren" — Klimadatastyrelsen
is the governing authority for Datafordeleren. [[DK-KLIMADATASTYRELSEN]]'s
own "Organisation" page, read the same pass, corroborates this with a
dedicated internal "Kontor for Datafordeleren" (Office for the Data
Distributor).

## Not modelled

- **CPR, CVR, BBR and DAR** as separate register entities, though all
  four are named directly on the platform's own homepage. This mirrors
  the Netherlands' own registers, but Denmark's single-distributor
  design means the Atlas has not yet decided whether they warrant
  individual nodes the way [[NL-KADASTER]] and [[NL-KVK]] do.
- The **transition deadline** the platform's homepage announces —
  parallel operation of all non-modernised services ends 15 January
  2027 — an operational detail rather than a structural fact.

## Relationships

- `part-of` [[DK]] — anchor edge.
- `implements` [[DK-GRUNDDATA]].
- `maintained-by` [[DK-KLIMADATASTYRELSEN]].

## Sources

Listed in frontmatter. `datafordeler.dk` and
`klimadatastyrelsen.dk/.../organisation` were read directly this pass;
`grunddata.dk` no longer resolves.
