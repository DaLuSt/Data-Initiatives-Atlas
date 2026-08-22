---
id: CH-SWISSTOPO
type: organisation
name: swisstopo
alternative_names:
  - Bundesamt für Landestopografie
  - Federal Office of Topography
description: >
  Switzerland's federal office of topography, responsible for official
  national mapping, geodetic reference systems and the federal geodata
  infrastructure.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - CH
  - EU-EUROGEOGRAPHICS
relationships:
  - type: part-of
    target: CH
    source: fact
    evidence: "Confirmed by reading swisstopo.admin.ch and geo.admin.ch directly (2026-08-22). swisstopo.admin.ch confirms the office's identity as Switzerland's federal topography office; geo.admin.ch, which swisstopo publishes, describes itself as the Confederation's geoportal for geolocated information, data and services. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics is the membership association for the European National Mapping, Cadastral and Land Registry Authorities, an international not-for-profit association (AISBL/IVZW under Belgian law, BCE 833 607 112) bringing together 63 organisations from 46 countries covering the whole of geographical Europe (eurogeographics.org/our-members/; eurogeographics.org). NOT READ — search-only. Membership follows from the sourced composition rule rather than from a source naming this authority, the same basis on which the national standardisation bodies were attached to EU-CEN. This entity is Switzerland's federal office of topography."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "swisstopo — Bundesamt für Landestopografie"
    url: "https://www.swisstopo.admin.ch/"
    publisher: "Bundesamt für Landestopografie swisstopo"
    accessed: "2026-08-22"
  - title: "geo.admin.ch — Das Geoportal des Bundes"
    url: "https://www.geo.admin.ch/"
    publisher: "Bundesamt für Landestopografie swisstopo"
    accessed: "2026-08-22"
  - title: "swisstopo — Federal Office of Topography"
    url: "https://www.swisstopo.admin.ch/en/home.html"
    publisher: "Federal Office of Topography swisstopo"
    accessed: "2026-08-22"
---

# swisstopo

> **Verified 2026-08-22.** All three cited pages were read directly and
> confirm the claims below verbatim. The English alternative name
> "Federal Office of Topography" was not attested on the German-only
> pages originally cited, so swisstopo's own English homepage was added
> to confirm it.

## Description

Confirmed verbatim by reading swisstopo.admin.ch (2026-08-22): "Das
Bundesamt für Landestopografie swisstopo ist das Geoinformationszentrum
der Schweiz." swisstopo is Switzerland's federal office of topography — the national
mapping authority.

## Why a thin entity is still worth having

Together with [[NO-KARTVERKET]] and [[IE-TAILTE]], this batch takes
[[DOMAIN-GEOSPATIAL]] from **3 of 7** countries to **6 of 10**. Belgium,
Spain, France and Poland remain without any geospatial entity, which is now
the more conspicuous gap.

## Not established

- Its **statutory basis** — the Geoinformationsgesetz (GeoIG) was not
  researched.
- Its relationship to **geo.admin.ch**, the federal geoportal, which the
  second source shows it publishes.
- Any relationship to [[EU-INSPIRE]] or [[UN-GGIM]]. Switzerland is outside
  the Union and the EEA, so the INSPIRE question does not even arise the way
  it does for [[NO-KARTVERKET]] — but whether Switzerland aligns
  voluntarily, as it did on data protection, was not researched.

## Sources

Listed in frontmatter, all three read directly this pass.
