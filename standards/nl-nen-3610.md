---
id: NL-NEN-3610
type: standard
name: NEN 3610 Basismodel voor geo-informatie
alternative_names:
  - NEN 3610
  - Basismodel Geo-informatie
description: >
  Dutch base model forming the common foundation for all geo-information
  models. It simplifies the exchange of geo-information between parties and
  information systems and supports unambiguous, meaningful reuse of that
  information. Published as a NEN standard, with Geonovum as the point of
  contact for its application.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-NEN
  - NL-GEONOVUM
related_entities: []
relationships:
  - type: maintained-by
    target: NL-GEONOVUM
    source: fact
    evidence: "Geonovum is the point of contact (aanspreekpunt) for the application of NEN 3610 in geo-information models (geonovum.nl NEN 3610 page). NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "NEN 3610 basismodel voor informatiemodellen"
    url: "https://www.geonovum.nl/geo-standaarden/nen-3610-basismodel-voor-informatiemodellen"
    publisher: "Geonovum"
  - title: "NEN 3610 Linked Data Profiel"
    url: "https://docs.geostandaarden.nl/nen3610/cv-st-nldp-20190715/"
    publisher: "Geonovum"
  - title: "Verplichte en aanbevolen standaarden"
    url: "https://www.geonovum.nl/themas/standaardisatie/verplicht-aanbevolen"
    publisher: "Geonovum"
---

# NEN 3610

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

NEN 3610 is the common basis for all Dutch geo-information models. The
NEN 3610:2022 Basismodel Geo-informatie simplifies the exchange of
geo-information between parties and information systems, and helps that
information be reused unambiguously and meaningfully. A Linked Data profile
of NEN 3610 also exists.

## A divided-custody caveat

The `maintained-by` relationship to [[NL-GEONOVUM]] is recorded at
`confidence: low` deliberately. The sourced statement is narrower than the
relationship type implies: Geonovum is described as the *aanspreekpunt*
(point of contact) for applying NEN 3610 in geo-information models, which is
not the same as owning or publishing the standard. As a NEN-numbered
standard it is published by [[NL-NEN]].

Custody is therefore genuinely split between the two, and the Atlas records
both in `organisations:` while asserting the weaker of the two claims as a
relationship. This is recorded in `discovery/unresolved.md`.

## Relationships

- Point of contact for application: [[NL-GEONOVUM]].
- Published as a NEN standard by [[NL-NEN]] (association recorded in
  `organisations:`; no relationship asserted, as the publishing arrangement
  was not sourced).

## Sources

Listed in frontmatter.
