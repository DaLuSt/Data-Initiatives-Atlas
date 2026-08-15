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
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
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
    evidence: "DCAT-AP is a specification based on W3C's Data Catalogue vocabulary (DCAT) for describing public sector datasets in Europe; version 3.0.1 is fully aligned and compatible with the DCAT 3 recommendation (interoperable-europe.ec.europa.eu; semiceu.github.io). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EU-SEMIC
    source: fact
    evidence: "DCAT-AP is under maintenance by the SEMIC action, Interoperable Europe (interoperable-europe.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "DCAT-AP 3.0.1"
    url: "https://semiceu.github.io/DCAT-AP/releases/3.0.1/"
    publisher: "SEMIC (European Commission)"
  - title: "Get started with DCAT-AP"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/news/get-started-dcat-ap"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "DCAT application profile implementation guidelines"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-implementation-guidelines"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "SEMICeu/DCAT-AP — maintenance issue tracker"
    url: "https://github.com/SEMICeu/DCAT-AP"
    publisher: "SEMIC (European Commission)"
---

# DCAT-AP (DCAT Application Profile for data portals in Europe)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DCAT-AP is a specification based on [[INTL-DCAT]] for describing public
sector datasets in Europe. Its basic use case is cross-portal dataset
search: making public sector data findable across borders and sectors by
providing a minimal common basis for sharing datasets and data services
cross-border and cross-domain.

Version 3.0.1 is the current release and is fully aligned with the DCAT 3
recommendation. The specification is maintained openly on GitHub with
community contributions.

It was a joint initiative of DG CONNECT, the [[EU-PUBLICATIONS-OFFICE]] and
the Interoperable Europe Programme, and is maintained by [[EU-SEMIC]].

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

Listed in frontmatter.
