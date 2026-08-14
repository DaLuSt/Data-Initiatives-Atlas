---
id: NL-DCAT-AP-NL
type: standard
name: DCAT-AP-NL
alternative_names:
  - Metadataprofiel DCAT-AP-NL
description: >
  Dutch application profile of the DCAT metadata standard. It enables
  metadata about datasets and services (APIs) to be exchanged unambiguously
  between Dutch data catalogues and with European data catalogues.
  Management is assigned to Geonovum; version 3.0 has been adopted.

level: national
country: NL
region: null

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
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-GEONOVUM
related_entities: []
relationships:
  - type: maintained-by
    target: NL-GEONOVUM
    source: fact
    evidence: "The management of DCAT-AP-NL is assigned to Geonovum; Geonovum announced adoption of metadata model DCAT-AP-NL v3.0 (geonovum.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Metadataprofiel DCAT-AP-NL"
    url: "https://www.geonovum.nl/geo-standaarden/metadataprofiel-dcat-ap-nl"
    publisher: "Geonovum"
  - title: "Metadatamodel DCAT-AP-NL v.3.0 vastgesteld"
    url: "https://www.geonovum.nl/nieuws/metadatamodel-dcat-ap-nl-v30-vastgesteld"
    publisher: "Geonovum"
  - title: "DCAT — standaarden.overheid.nl"
    url: "https://standaarden.overheid.nl/dcat"
    publisher: "Overheid.nl"
---

# DCAT-AP-NL

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DCAT-AP-NL is the Dutch application profile of DCAT, the metadata standard
for describing datasets originally developed by the W3C. Applying the
generic DCAT-AP-NL standard makes it possible to exchange metadata about
data and services (APIs) unambiguously between different Dutch data
catalogues **and with European data catalogues** — which is what makes this
standard structurally interesting to the Atlas rather than merely
technically interesting.

DCAT is used across several Dutch platforms, including data.overheid.nl, the
Nationaal Georegister, health data spaces, and open data portals of
provinces and municipalities.

Version 3.0 of the metadata model has been adopted; the adoption date was
not established.

## The cross-level chain this standard sits in

DCAT-AP-NL is a national profile of the European DCAT-AP, which is itself a
profile of W3C DCAT:

```
W3C DCAT  →  EU DCAT-AP  →  NL DCAT-AP-NL
(Batch 14)   (Batch 9)      (this entity)
```

Neither upstream entity exists yet, so no `based-on` or `derived-from`
relationship is asserted. When Batches 9 and 14 land, this chain should be
completed — it is a clean example of the international → EU → national
standards descent the brief's final relationship pass calls for. Recorded in
`discovery/research-queue.md`.

## Relationships

- Maintained by [[NL-GEONOVUM]].
- Upstream relationships to EU DCAT-AP and W3C DCAT pending (see above).

## Sources

Listed in frontmatter.
