---
id: CH-SWISSTOPO
type: organisation
name: swisstopo
name_en: "Federal Office of Topography swisstopo"
alternative_names:
  - Federal Office of Topography swisstopo
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
last_verified: "2026-11-17"
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
    evidence: "EuroGeographics' own member list, read directly 2026-11-17: the members feed (eurogeographics.org/members/feed/) lists this authority, and its member page (eurogeographics.org/members/federal-office-of-topography-swisstopo/) gives 'English spelling Federal Office of Topography swisstopo', 'Member status Full'. Replaces evidence that inferred membership from the association's composition rule without a source naming this authority."
    confidence: high
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
  - title: "Federal Office of Topography swisstopo (English home page)"
    url: "https://www.swisstopo.admin.ch/en"
    publisher: "Bundesamt für Landestopografie swisstopo"
    accessed: "2026-10-10"
  - title: "EuroGeographics member page"
    url: "https://eurogeographics.org/members/federal-office-of-topography-swisstopo/"
    publisher: "EuroGeographics"
    accessed: "2026-11-17"
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
