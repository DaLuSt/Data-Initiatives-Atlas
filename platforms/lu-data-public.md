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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
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
    evidence: "Confirmed by reading data.public.lu directly (2026-08-25): it describes itself as 'La plateforme de données ouvertes luxembourgeoise' (the Luxembourgish open data platform), with 3,173 datasets, 217 organisations and 2,846 users at the time of reading. Corroborated by reading its 'Centre des technologies de l'information de l'État' organisation page directly, which lists 22 datasets published by LU-CTIE. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.public.lu — Portail Open Data"
    url: "https://data.public.lu/"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-08-25"
  - title: "Centre des technologies de l'information de l'État — Portail Open Data"
    url: "https://data.public.lu/en/organizations/centre-des-technologies-de-linformation-de-letat/"
    publisher: "data.public.lu"
    accessed: "2026-08-25"
  - title: "Governance of the Open data project"
    url: "https://data.public.lu/en/pages/governance/"
    publisher: "data.public.lu"
    accessed: "2026-09-06"
---

# data.public.lu

> **Verified 2026-08-25, custodian question answered 2026-09-06.** The
> portal's own "Governance" page, read directly, names the actual
> operator and steward — and it is neither CTIE nor a single body, and
> neither is currently an Atlas entity. See below.

## Description

data.public.lu is Luxembourg's national open data portal.

## Publishing on a portal is not operating it

The sources show [[LU-CTIE]] with an **organisation page** on data.public.lu
— that is, CTIE publishes datasets there.

**No `maintained-by` edge is asserted to [[LU-CTIE]].** Having a publisher
page proves publication, not custodianship, and the distinction matters:
dozens of bodies have publisher pages on any national portal and only one
runs it.

## The custodian question, answered but not modellable yet

**Closed as a sourcing question, 2026-09-06.** data.public.lu's own
"Governance of the Open data project" page, read directly, names the real
split: "The geoportal service operates the national Open data portal and
ensures its daily operation and technical availability," while "the Open
data and Access to information Division of the Information and Press
Service (SIP)" handles content and community management — strategic
coordination runs through a working group of SIP, the Ministry of
Digitalisation, CTIE and the Media and Communications Service. Neither the
Geoportal Service (part of the Administration du cadastre et de la
topographie) nor SIP's Open Data Division is currently an Atlas entity, so
no `maintained-by` edge is asserted to either — but the sixth-portal
"custodian unknown" framing no longer applies here: the custodian is
known, just not yet modellable.

## Relationships

- `part-of` [[LU]] — an anchor edge.

## Sources

Listed in frontmatter. The first two pages were read directly in the
original pass (2026-08-25); the governance page was read directly this
pass (2026-09-06).
