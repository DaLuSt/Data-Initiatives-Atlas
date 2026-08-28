---
id: DE-DCAT-AP-DE
type: standard
name: DCAT-AP.de
alternative_names:
  - DCAT-AP.de Spezifikation
description: >
  German adaptation of the European DCAT-AP metadata application profile,
  established by IT-Planungsrat resolution in June 2018 as the common
  binding basis for metadata exchange between German open data portals,
  taking effect in 2019. Since early 2019 metadata is accepted only in the
  DCAT-AP.de standard. It comprises a specification, a URI concept and a
  conventions handbook (Konventionenhandbuch 2.0, published 1 March 2022,
  with 41 MUST/SHOULD/CAN conventions and a nine-month transition period),
  and version 3.0 is the German adaptation of DCAT-AP 3.0.

level: national
country: DE
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2019-01-01
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading dcat-ap.de's own homepage and Specification 3.0 page directly (2026-08-28): DCAT-AP.de is 'the joint German metadata model for exchanging open administrative data,' described as 'an extension of DCAT-AP,' and the 3.0 specification's own introduction states it 'übernimmt die Regeln des europäischen Metadatenaustauschschemas DCAT-AP mit zusätzlichen Einschränkungen und Erweiterungen' (adopts the rules of the European metadata exchange schema DCAT-AP with additional restrictions and extensions). govdata.de's own metadata-schema page, also read directly, independently confirms DCAT-AP.de is 'eine standardkonforme deutsche Ableitung von DCAT-AP.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-GOVDATA
    source: fact
    evidence: "Confirmed by reading the Konventionenhandbuch 2.0 page and govdata.de's metadata-schema page directly (2026-08-28): the handbook, published 1 March 2022 by the GovData coordination office, sets out 41 technical, semantic and organisational conventions (MUST/SHOULD/CAN) governing 'exchange with GovData' specifically, with a nine-month transition period for data providers; govdata.de's own page confirms the specification, URI concept and conventions manual together establish semantic rules 'für GovData und den europäischen Portalverbund' and that DCAT-AP.de was designated the binding metadata exchange standard for German open data portals by IT-Planungsrat resolution in 2018, taking effect in 2019."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DCAT-AP.de — Start"
    url: "https://www.dcat-ap.de/"
    publisher: "DCAT-AP.de"
    accessed: "2026-08-28"
  - title: "DCAT-AP.de Spezifikation 3.0 — Deutsche Adaption von DCAT-AP 3.0"
    url: "https://www.dcat-ap.de/def/dcatde/3.0/spec/"
    publisher: "DCAT-AP.de"
    accessed: "2026-08-28"
  - title: "DCAT-AP.de Konventionenhandbuch 2.0"
    url: "https://www.dcat-ap.de/def/dcatde/2.0/implRules/"
    publisher: "DCAT-AP.de"
    accessed: "2026-08-28"
  - title: "Metadaten-Struktur — GovData"
    url: "https://www.govdata.de/metadatenschema"
    publisher: "GovData"
    accessed: "2026-08-28"
---

# DCAT-AP.de

> **Re-verified 2026-08-28.** All four cited pages read directly.
> `verification: primary-source`; `confidence` raised to `high`. The exact
> day of the founding IT-Planungsrat resolution ("28 June 2018") is
> unchanged from the previous pass but was not independently re-confirmed
> to the day this pass — both directly-read sources this time give only
> "June 2018" / "2018" — so it is kept as previously sourced rather than
> re-stated as newly verified to that precision.

## Description

DCAT-AP.de is the **German adaptation of [[EU-DCAT-AP]]**, confirmed
directly this pass in the standard's own words: its Specification 3.0 page
states it "übernimmt die Regeln des europäischen Metadatenaustauschschemas
DCAT-AP mit zusätzlichen Einschränkungen und Erweiterungen" (adopts the
rules of DCAT-AP with additional restrictions and extensions). It was
established by **IT-Planungsrat resolution in June 2018** as the common
binding basis for metadata exchange between German open data portals,
**taking effect in 2019** — confirmed directly this pass on govdata.de's
own metadata-schema page — and since early 2019 metadata is **accepted
only** in this standard.

It has three components:

1. the **Spezifikation** — currently version 3.0, the German adaptation of
   DCAT-AP 3.0, confirmed directly this pass to be "officially adopted by
   the GovData expert group" as the binding standard within the GovData
   federation;
2. the **URI-Konzept**, confirmed directly this pass on govdata.de's own
   page to standardise naming conventions across the `dcat-ap.de` and
   `govdata.de` namespaces;
3. the **Konventionenhandbuch**, confirmed directly this pass to have been
   published on **1 March 2022** by the GovData coordination office, with
   **41 conventions** (marked MUST, SHOULD or CAN) covering dataset
   descriptions, file distributions, licensing, geographic coding and
   quality standards, and a **nine-month transition period** for data
   providers — none of these specifics previously recorded on this entity.

## This completes the DCAT chain in a second country

Batch 15 named the DCAT descent as one of only two international→national
chains in the Atlas and called it *"the template for what the UN layer
lacks."* It now forks:

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
portal network, with governance now confirmed in more granular form this
pass (a dedicated GovData coordination office issuing versioned convention
handbooks with formal transition periods).

Same standard family, same parent profile, different institutional logic.
That contrast is only visible because two countries are modelled, and it is
recorded rather than smoothed into a common pattern.

## Relationships

- `based-on` [[EU-DCAT-AP]] — confirmed directly this pass, `confidence:
  high`.
- `applies-to` [[DE-GOVDATA]] — confirmed directly this pass, `confidence:
  high`.

## Sources

Listed in frontmatter. All four are the standard's own publication site or
GovData's own metadata page, all read directly this pass. **No
IT-Planungsrat decision document is cited** for the founding 2018
resolution, which remains the one fact here resting on secondary
restatement rather than the decision text itself.
