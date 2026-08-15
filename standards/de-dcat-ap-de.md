---
id: DE-DCAT-AP-DE
type: standard
name: DCAT-AP.de
alternative_names:
  - DCAT-AP.de Spezifikation
description: >
  German adaptation of the European DCAT-AP metadata application profile,
  established by IT-Planungsrat resolution of 28 June 2018 as the common
  binding basis for metadata exchange between German open data portals from
  2019. Since early 2019 metadata is accepted only in the DCAT-AP.de
  standard. It comprises a specification, a URI concept and a conventions
  handbook, and version 3.0 is the German adaptation of DCAT-AP 3.0.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-IT-PLANUNGSRAT
related_entities:
  - EU-DCAT-AP
  - DE-GOVDATA
  - NL-DCAT-AP-NL
relationships:
  - type: based-on
    target: EU-DCAT-AP
    source: fact
    evidence: "DCAT-AP.de is a standard-conformant German adaptation of DCAT-AP, the standard for data exchange at European level; the DCAT-AP.de Spezifikation 3.0 is titled 'Deutsche Adaption von DCAT-AP 3.0' (dcat-ap.de; dcat-ap.de/def/dcatde/3.0/spec/specification.pdf). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-GOVDATA
    source: fact
    evidence: "The DCAT-AP.de conventions handbook was created for GovData to further increase interoperability, with rules standardising communication with GovData; the specification, the URI concept and the conventions handbook together provide guidance on metadata exchange in the GovData portal network, and GovData established DCAT-AP.de as a recognised data exchange standard for open government data (dcat-ap.de/def/dcatde/2.0/implRules; govdata.de/metadatenschema; fitko.de/produktmanagement/govdata). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "DCAT-AP.de — Start"
    url: "https://www.dcat-ap.de/"
    publisher: "DCAT-AP.de"
  - title: "DCAT-AP.de Spezifikation 3.0 — Deutsche Adaption von DCAT-AP 3.0"
    url: "https://www.dcat-ap.de/def/dcatde/3.0/spec/"
    publisher: "DCAT-AP.de"
  - title: "DCAT-AP.de Konventionenhandbuch 2.0"
    url: "https://www.dcat-ap.de/def/dcatde/2.0/implRules/"
    publisher: "DCAT-AP.de"
  - title: "Metadaten-Struktur — GovData"
    url: "https://www.govdata.de/metadatenschema"
    publisher: "GovData"
---

# DCAT-AP.de

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

DCAT-AP.de is the **German adaptation of [[EU-DCAT-AP]]**. It was
established by **IT-Planungsrat resolution of 28 June 2018** as the common
binding basis for metadata exchange between German open data portals from
2019 onwards, and since early 2019 metadata is **accepted only** in this
standard.

It has three components:

1. the **Spezifikation** — currently version 3.0, the German adaptation of
   DCAT-AP 3.0;
2. the **URI-Konzept**;
3. the **Konventionenhandbuch**, created for [[DE-GOVDATA]] to raise
   interoperability further, defining additional value lists and URIs for
   data types where DCAT-AP.de allows more freedom than Germany needs —
   licence literals, for example.

## This completes the DCAT chain in a second country

Batch 15 named the DCAT descent as one of only two international→national
chains in the Atlas and called it *"the template for what the UN layer
lacks"*. It now forks:

```
                    INTL-DCAT (W3C)
                          │ based-on
                          ▼
                   EU-DCAT-AP (SEMIC)
                    │              │
              based-on          based-on
                    ▼              ▼
          NL-DCAT-AP-NL       DE-DCAT-AP-DE
          (Geonovum)          (IT-Planungsrat)
```

This is the **first complete four-level structure in the Atlas that
branches across two countries**: an international standards body, a
European profile, and two national adaptations of that profile — each
recorded once, with no duplication of the layers above.

It is a stronger demonstration of country-neutrality than the legislative
chains, because a metadata profile is exactly the kind of artefact a
country-shaped model would have been tempted to fold into its parent. The
Atlas holds [[EU-DCAT-AP]] as one entity with two national children, in the
same folder, distinguished only by their `country` field.

**No relationship between [[NL-DCAT-AP-NL]] and this entity is asserted.**
They are siblings; their shared parent is the relationship.

## A custody contrast worth noting

The two national profiles are maintained differently. [[NL-DCAT-AP-NL]] is
custodied by [[NL-GEONOVUM]], a foundation with a geospatial remit.
DCAT-AP.de was established by [[DE-IT-PLANUNGSRAT]] resolution — a
Bund-Länder political decision — and is operated in the [[DE-GOVDATA]]
portal network.

Same standard family, same parent profile, different institutional logic.
That contrast is only visible because two countries are modelled, and it is
recorded rather than smoothed into a common pattern.

## Relationships

- `based-on` [[EU-DCAT-AP]].
- `applies-to` [[DE-GOVDATA]].

## Sources

Listed in frontmatter. The dcat-ap.de pages are the standard's own
publication site; the GovData metadata-schema page ties it to the portal.
**No IT-Planungsrat decision document is cited** for the 28 June 2018
resolution, which is the one fact here that rests on a single secondary
statement.
