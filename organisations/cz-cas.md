---
id: CZ-CAS
type: organisation
name: Česká agentura pro standardizaci
alternative_names:
  - ČAS
  - Czech Standardization Agency
description: >
  Czechia's state contributory organisation (státní příspěvková organizace)
  responsible for the operational work of technical standardisation: the
  creation, publication and distribution of Czech technical standards
  (ČSN). Established by the Office for Technical Standardization,
  Metrology and State Testing (ÚNMZ), which retains formal international
  membership and legal responsibility on ISO, IEC, CEN and CENELEC.

level: national
country: CZ
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2018-01-01
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ-UNMZ
relationships:
  - type: part-of
    target: CZ-UNMZ
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading agenturacas.gov.cz's own page directly (2026-09-06): the agency 'byla zřízena jako státní příspěvková organizace Úřadem pro technickou normalizaci, metrologii a státní zkušebnictví (ÚNMZ)' — was established as a state contributory organisation by ÚNMZ — under Law No. 265/2017 Coll., which amended Law No. 90/2016 Coll. (conformity assessment) and Law No. 22/1997 Coll. (technical requirements for products). It took over all standardisation-related activities from ÚNMZ on 1 January 2018."
    confidence: high
    valid_from: 2018-01-01
    valid_until: null

sources:
  - title: "Agentura"
    url: "https://agenturacas.gov.cz/o-nas/agentura/"
    publisher: "Česká agentura pro standardizaci (ČAS)"
    accessed: "2026-09-06"
---

# ČAS — Česká agentura pro standardizaci

> **Created 2026-09-06**, closing a gap [[CZ-UNMZ]]'s own entity flagged:
> "ČAS is not modelled... the body that actually produces ČSN standards
> is absent from the graph." Reading agenturacas.gov.cz's own page
> directly confirms the founding instrument, date and legal form.

## Description

Confirmed by reading agenturacas.gov.cz's own page directly: ČAS "byla
zřízena jako státní příspěvková organizace Úřadem pro technickou
normalizaci, metrologii a státní zkušebnictví (ÚNMZ)" — was established as
a state contributory organisation by [[CZ-UNMZ]] — under **Law No.
265/2017 Coll.**, which amended Law No. 90/2016 Coll. on conformity
assessment and Law No. 22/1997 Coll. on technical requirements for
products. ČAS took over all standardisation-related activities from ÚNMZ
on **1 January 2018**.

## The membership/operations split, now both sides modelled

[[CZ-UNMZ]]'s own entity already described this split: ÚNMZ holds the
formal international membership (at [[INTL-ISO]], [[INTL-IEC]],
[[EU-CEN]], [[EU-CENELEC]]) and the legal responsibility on behalf of the
state, while ČAS performs the operational work — technical committees,
standard drafting, publication. This entity is that second half, closing
the gap ÚNMZ's own "Not modelled" note flagged.

No `participates-in` edge is asserted from this entity to any of the four
international bodies: the membership itself belongs to ÚNMZ, per the
sourcing already established there. The open question about which body
holds ETSI membership (noted on [[CZ-UNMZ]]) is unaffected and remains
open.

## Relationships

- `part-of` [[CZ-UNMZ]] — founding relationship; ČAS was created by ÚNMZ
  as a state contributory organisation.

## Sources

Listed in frontmatter, read directly 2026-09-06.
