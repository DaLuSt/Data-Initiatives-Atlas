---
id: IE-TAILTE
type: organisation
name: Tailte Éireann
alternative_names:
  - Tailte Eireann
  - Ordnance Survey Ireland
  - OSi
  - Property Registration Authority
description: >
  Ireland's national mapping, land registration and property valuation
  body, formed by the merger of Ordnance Survey Ireland, the Property
  Registration Authority and the Valuation Office. It holds the national
  mapping function and the land registry in a single organisation.

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2023-03-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - IE
  - EU-EUROGEOGRAPHICS
relationships:
  - type: part-of
    target: IE
    source: fact
    evidence: "Confirmed by reading tailte.ie directly (2026-08-22), which lists Property Registration, Valuations and GeoHive Geospatial Data among its services. The merger itself and its date are confirmed on en.wikipedia.org's Ordnance Survey Ireland article, read directly: 'Dissolved 1 March 2023 ... a new body called Tailte Éireann, which also incorporates the Property Registration Authority and the Valuation Office.' Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics is the membership association for the European National Mapping, Cadastral and Land Registry Authorities, an international not-for-profit association (AISBL/IVZW under Belgian law, BCE 833 607 112) bringing together 63 organisations from 46 countries covering the whole of geographical Europe (eurogeographics.org/our-members/; eurogeographics.org). NOT READ — search-only. Membership follows from the sourced composition rule rather than from a source naming this authority, the same basis on which the national standardisation bodies were attached to EU-CEN. This entity is Ireland's national mapping, land registration and valuation authority."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Tailte Éireann"
    url: "https://www.tailte.ie/"
    publisher: "Tailte Éireann"
    accessed: "2026-08-22"
  - title: "Ordnance Survey Ireland"
    url: "https://en.wikipedia.org/wiki/Ordnance_Survey_Ireland"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# Tailte Éireann

> **Verified 2026-08-22.** Both cited pages were read directly. The
> Wikipedia article on Ordnance Survey Ireland, read this pass, confirms
> the merger and its exact date verbatim, upgrading `confidence` from low
> to medium and setting `start_date`. The Property Registration Authority
> and Valuation Office predecessors are confirmed on the same page.

## Description

Confirmed by reading en.wikipedia.org's Ordnance Survey Ireland article
directly (2026-08-22): Ordnance Survey Ireland was "Dissolved 1 March
2023 ... its functions transferred to a new body called Tailte Éireann,
which also incorporates the Property Registration Authority and the
Valuation Office." Tailte Éireann holds Ireland's national mapping, land
registration and property valuation functions, formed by merging
**Ordnance Survey Ireland**, the **Property Registration Authority** and
the **Valuation Office** on **1 March 2023**.

## `confidence: medium`, upgraded from `low`

The merger and its exact date are now confirmed against a source that
states them directly — Wikipedia's Ordnance Survey Ireland article,
rather than the two general-purpose pages this entity previously relied
on. `start_date: 2023-03-01` is set on that basis. `confidence` stops
short of the level the UK batch's better-sourced organisations carry
because neither page is a government legal source — see Sources below.

This is still the thinnest-sourced entity in the batch, and it is
included for one reason: it closes Ireland's [[DOMAIN-GEOSPATIAL]] gap on
the day the country joins, which four existing Atlas countries still have
open.

## A combination no other Atlas country has in one body

Mapping and the land registry sit together here. Elsewhere they are split:

- [[GB-OS]] maps; the UK land registries are separate and unmodelled.
- [[NL-KADASTER]] holds the cadastre **and** the topographic register
  [[NL-BRT]] — the closest parallel, and still not a merger of three bodies.
- [[NO-KARTVERKET]] holds mapping and the property register.

The merger is now confirmed: Ireland and Norway are the two countries in
the Atlas that fuse mapping and the land registry into one body.

## Not modelled

- The **establishing legislation** itself (the merger date is now known;
  the Act that authorised it is not).
- Whether Ireland has an **INSPIRE** transposition, and Tailte Éireann's
  role in it.
- **data.geohive.ie** and Ireland's spatial data infrastructure.

## Sources

Listed in frontmatter, both read directly this pass. **Neither is a
government legal source** — the establishing Act itself was not located —
which is why `confidence` stops at medium rather than reaching the level
of entities sourced directly from legislation.gov equivalents.
