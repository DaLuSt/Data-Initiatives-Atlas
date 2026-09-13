---
id: NO-KARTVERKET
type: organisation
name: Kartverket
alternative_names:
  - Norwegian Mapping Authority
  - Statens kartverk
description: >
  Norway's national mapping and cadastral authority, responsible for
  official maps, geodetic reference frames, the property register and the
  national spatial data infrastructure. It is Norway's counterpart to the
  mapping agencies that anchor the geospatial domain in other Atlas
  countries.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - "NO"
  - EU-EUROGEOGRAPHICS
  - UN-GGIM
  - NO-GEODATALOVEN
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "Confirmed by reading kartverket.no directly (2026-08-22), which describes itself managing the property register, sea charts, topographic mapping and geodata work for Norway. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EUROGEOGRAPHICS
    source: fact
    evidence: "EuroGeographics is the membership association for the European National Mapping, Cadastral and Land Registry Authorities, an international not-for-profit association (AISBL/IVZW under Belgian law, BCE 833 607 112) bringing together 63 organisations from 46 countries covering the whole of geographical Europe (eurogeographics.org/our-members/; eurogeographics.org). NOT READ — search-only. Membership follows from the sourced composition rule rather than from a source naming this authority, the same basis on which the national standardisation bodies were attached to EU-CEN. This entity is Norway's national mapping and cadastre authority."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: UN-GGIM
    source: fact
    evidence: "Confirmed by reading kartverket.no directly (2026-08-22): a homepage news item states 'Fikk bred støtte i FN' (broad support at the UN) and describes participation this week at a meeting of 'FNs ekspertkomité for geografisk informasjon' (the UN's expert committee for geographic information) in New York — i.e. UN-GGIM. The item confirms attendance and involvement rather than stating a formal membership role comparable to GB-OS's Head-of-Delegation position, so this edge is carried at lower confidence."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Kartverket"
    url: "https://www.kartverket.no/"
    publisher: "Kartverket (Norwegian Mapping Authority)"
    accessed: "2026-08-22"
  - title: "Norge digitalt"
    url: "https://www.geonorge.no/"
    publisher: "Geonorge / Kartverket"
    accessed: "2026-08-22"
  - title: "Kartverket — English"
    url: "https://www.kartverket.no/en/"
    publisher: "Kartverket (Norwegian Mapping Authority)"
    accessed: "2026-08-22"
  - title: "Kartverket"
    url: "https://no.wikipedia.org/wiki/Kartverket"
    publisher: "Wikipedia (norsk bokmål)"
    accessed: "2026-08-22"
---

# Kartverket

> **Verified 2026-08-22.** All four cited pages were read directly. A
> finding closes one of the four gaps this entity previously flagged as
> unresearched: kartverket.no's own homepage shows Kartverket
> participating in a UN-GGIM committee meeting in New York, so
> `participates-in` [[UN-GGIM]] is now asserted, at `confidence: low`
> since the evidence is a news item about attendance rather than a
> stated delegation role. The English alternative name was confirmed on
> kartverket.no's own English page; the historical Norwegian name
> "Statens kartverk" was confirmed on Norwegian Wikipedia, added as a
> source this pass.
>
> **Updated 2026-09-13**: Norway's INSPIRE transposition is now
> [[NO-GEODATALOVEN]], closing `discovery/unresolved.md` row #108.

## Description

Confirmed by reading kartverket.no directly (2026-08-22). Kartverket is Norway's national mapping and cadastral authority.

## Why it is here despite being thin

[[DOMAIN-GEOSPATIAL]] was reachable from **three** of seven countries before
this batch — the Netherlands, Germany and the United Kingdom. Belgium,
Spain, France and Poland have no geospatial entity at all.

Kartverket makes Norway the fourth country in that domain on the day it
joins the Atlas, which is a better position than four existing countries
hold. The entity is deliberately minimal rather than absent.

## What is not established, and therefore not asserted

- Its **statutory basis** — no act was identified for Kartverket itself
  (as distinct from Norway's INSPIRE transposition, closed below).
- Its relationship to **Geonorge** and *Norge digitalt*, Norway's spatial
  data infrastructure and portal, which the second source names.

**Closed 2026-09-13**: Norway's INSPIRE transposition is now
[[NO-GEODATALOVEN]] (LOV-2010-09-03-56), `implements-requirement-from`
[[EU-INSPIRE]] via [[INTL-EEA-JCD-55-2010]] (the EEA Joint Committee
Decision that incorporated the directive, 30 April 2010) — closing
`discovery/unresolved.md` row #108. Whether Kartverket itself
administers the Act is plausible but not sourced, so no edge is asserted
between them.

Its participation in [[UN-GGIM]] is asserted above. The remaining gaps
are logged in `discovery/unresolved.md`.

## Sources

Listed in frontmatter, all four read directly this pass.
