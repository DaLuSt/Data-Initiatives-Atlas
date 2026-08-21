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
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - "NO"
  - EU-EUROGEOGRAPHICS
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "Kartverket is Norway's national mapping and cadastral authority (kartverket.no; geonorge.no). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
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

sources:
  - title: "Kartverket"
    url: "https://www.kartverket.no/"
    publisher: "Kartverket (Norwegian Mapping Authority)"
  - title: "Norge digitalt"
    url: "https://www.geonorge.no/"
    publisher: "Geonorge / Kartverket"
---

# Kartverket

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

Kartverket is Norway's national mapping and cadastral authority.

## Why it is here despite being thin

[[DOMAIN-GEOSPATIAL]] was reachable from **three** of seven countries before
this batch — the Netherlands, Germany and the United Kingdom. Belgium,
Spain, France and Poland have no geospatial entity at all.

Kartverket makes Norway the fourth country in that domain on the day it
joins the Atlas, which is a better position than four existing countries
hold. The entity is deliberately minimal rather than absent.

## What is not established, and therefore not asserted

- Its **statutory basis** — no act was identified.
- Its relationship to **Geonorge** and *Norge digitalt*, Norway's spatial
  data infrastructure and portal, which the second source names.
- Whether Norway has transposed the **INSPIRE Directive**. [[EU-INSPIRE]]
  applies in six member states in this Atlas; whether it was incorporated
  into the EEA Agreement, and by which act it takes effect in Norway, was
  **not researched**. Given the [[NO]] anchor's whole argument, that
  question cannot be answered by assuming the member-state answer.
- Its participation in [[UN-GGIM]], which [[GB-OS]] carries.

All four are logged in `discovery/unresolved.md`.

## Sources

Listed in frontmatter.
