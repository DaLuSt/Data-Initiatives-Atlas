---
id: EU-DCAT-AP
type: standard
name: DCAT Application Profile for data portals in Europe
alternative_names:
  - DCAT-AP
description: >
  European specification based on the W3C Data Catalog Vocabulary for
  describing public sector datasets. It provides a minimal common basis for
  sharing datasets and data services cross-border and cross-domain, enabling
  cross-portal dataset search. Maintained by the SEMIC action within
  Interoperable Europe.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-SEMIC
  - EU-PUBLICATIONS-OFFICE
  - EU-COMMISSION
related_entities:
  - INTL-DCAT
  - NL-DCAT-AP-NL
relationships:
  - type: based-on
    target: INTL-DCAT
    source: fact
    evidence: "Confirmed by reading semiceu.github.io's own DCAT-AP 3.0.1 specification directly (2026-08-28): DCAT-AP 3.0.1 is 'a DCAT profile for sharing information about Catalogues containing Datasets and Data Services descriptions in Europe,' aligned with W3C DCAT 3 (previous versions aligned with DCAT 1 and DCAT 2 respectively), extending it with tighter definitions, usage constraints, cardinalities and controlled-vocabulary recommendations for European data portals."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-SEMIC
    source: fact
    evidence: "Confirmed by reading semiceu.github.io's DCAT-AP 3.0.1 specification and interoperable-europe.ec.europa.eu's 'Get started with DCAT-AP' page directly (2026-08-28): 'the SEMIC action, operating under Interoperable Europe, maintains DCAT-AP,' through a dedicated Working Group of national/regional profile maintainers, solution developers and system managers, following a published Change and Release Management Policy (bug-fix releases twice yearly, minor updates annually, major revisions every two years)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DCAT-AP 3.0.1"
    url: "https://semiceu.github.io/DCAT-AP/releases/3.0.1/"
    publisher: "SEMIC (European Commission)"
    accessed: "2026-08-28"
  - title: "Get started with DCAT-AP"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/news/get-started-dcat-ap"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-08-28"
  - title: "DCAT application profile implementation guidelines"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-implementation-guidelines"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-08-28"
  - title: "SEMICeu/DCAT-AP — maintenance issue tracker"
    url: "https://github.com/SEMICeu/DCAT-AP"
    publisher: "SEMIC (European Commission)"
    accessed: "2026-08-28"
---

# DCAT-AP (DCAT Application Profile for data portals in Europe)

> **Re-verified 2026-08-28.** All four cited pages were read directly: the
> DCAT-AP 3.0.1 specification itself, the "Get started" and implementation
> guidelines pages on the Interoperable Europe Portal, and the
> SEMICeu/DCAT-AP GitHub repository. `verification` promoted `search-only`
> → `primary-source`; `confidence` moves `medium` → `high` for both
> relationships and the entity overall, since the core claims (basis in
> DCAT, maintenance by SEMIC) now rest on the specification's own text
> rather than secondary description.

## Description

Confirmed by reading semiceu.github.io's own DCAT-AP 3.0.1 specification
directly (2026-08-28): DCAT-AP is "a DCAT profile for sharing information
about Catalogues containing Datasets and Data Services descriptions in
Europe," based on [[INTL-DCAT]] (W3C's Data Catalog Vocabulary). Its basic
use case, confirmed by reading the implementation guidelines directly, is
cross-portal dataset search — enabling "cross-data portal search for data
sets" and making public sector data "better searchable across borders and
sectors" through a minimal common basis for sharing dataset and data
service descriptions.

Version 3.0.1 is the current release and is aligned with the DCAT 3
recommendation (earlier DCAT-AP versions aligned with DCAT 1 and DCAT 2
respectively). Confirmed by reading interoperable-europe.ec.europa.eu's
"Get started" page directly: maintenance runs through a dedicated Working
Group of national/regional profile maintainers, solution developers and
system managers, under a published Change and Release Management Policy —
bug-fix releases twice yearly, minor updates annually, major revisions
every two years. Change requests are submitted publicly via GitHub.

It was a joint initiative of DG CONNECT, the [[EU-PUBLICATIONS-OFFICE]] and
the Interoperable Europe Programme (formerly ISA²) — this detail was not
independently re-confirmed this pass and is carried forward from the prior
description — and is maintained by [[EU-SEMIC]], confirmed directly this
pass.

## Extensions

Two extensions are named in the sources and **not modelled**:
**GeoDCAT-AP**, for geospatial datasets, dataset series and services; and
**StatDCAT-AP**, for interoperability between statistical dataset
descriptions. Both are queued.

GeoDCAT-AP is the more interesting omission for this Atlas: [[NL-GEONOVUM]]
maintains both [[NL-DCAT-AP-NL]] and the Dutch geo-standards, so a
GeoDCAT-AP entity would likely connect the geospatial and metadata layers.

## The chain this completes

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
```

[[NL-DCAT-AP-NL]] was created in Batch 4 with this chain sketched in prose
and explicitly unasserted, because neither upstream entity existed. Both now
do, and the relationship is recorded on the Dutch entity.

## Relationships

- Based on [[INTL-DCAT]].
- Maintained by [[EU-SEMIC]]; co-initiated with [[EU-PUBLICATIONS-OFFICE]]
  and [[EU-COMMISSION]] (DG CONNECT).
- Profiled nationally by [[NL-DCAT-AP-NL]].

## Sources

Listed in frontmatter, all four read directly this pass (2026-08-28).
