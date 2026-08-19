---
id: LU-DATA-PUBLIC
type: platform
name: data.public.lu
alternative_names:
  - Portail Open Data
  - Luxembourg open data portal
description: >
  Luxembourg's national open data portal, on which public bodies including
  the Centre des technologies de l'information de l'État publish their data.

level: national
country: LU
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
  - LU
  - LU-CTIE
relationships:
  - type: part-of
    target: LU
    source: fact
    evidence: "data.public.lu is Luxembourg's national open data portal; the Centre des technologies de l'information de l'État is among the organisations publishing on it (data.public.lu; data.public.lu organisation page for the CTIE). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.public.lu — Portail Open Data"
    url: "https://data.public.lu/"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
  - title: "Centre des technologies de l'information de l'Etat — Portail Open Data"
    url: "https://data.public.lu/en/organizations/centre-des-technologies-de-linformation-de-letat/"
    publisher: "data.public.lu"
---

# data.public.lu

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

data.public.lu is Luxembourg's national open data portal.

## Publishing on a portal is not operating it

The sources show [[LU-CTIE]] with an **organisation page** on data.public.lu
— that is, CTIE publishes datasets there.

**No `maintained-by` edge is asserted.** Having a publisher page proves
publication, not custodianship, and the distinction matters: dozens of bodies
have publisher pages on any national portal and only one runs it.

The sixth national portal in the Atlas without a sourced custodian.

## Relationships

- `part-of` [[LU]] — an anchor edge.

## Sources

Listed in frontmatter.
