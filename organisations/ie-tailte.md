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
confidence: low
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
related_entities: []
relationships: []

sources:
  - title: "Tailte Éireann"
    url: "https://www.tailte.ie/"
    publisher: "Tailte Éireann"
  - title: "Ordnance Survey Ireland"
    url: "https://en.wikipedia.org/wiki/Ordnance_Survey_Ireland"
    publisher: "Wikipedia"
---

# Tailte Éireann

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `confidence: low`, `coverage: low`.

## Description

Tailte Éireann holds Ireland's national mapping, land registration and
property valuation functions, formed by merging **Ordnance Survey Ireland**,
the **Property Registration Authority** and the **Valuation Office**.

## ⚠ Why `confidence: low`

The merger and its date were **not confirmed against a primary source**.
Search returned the body's own site and an encyclopaedia entry about its
predecessor; the establishing act and the date the merger took effect were
not established, so `start_date` is null.

This is the weakest entity in the batch, and it is included for one reason:
it closes Ireland's [[DOMAIN-GEOSPATIAL]] gap on the day the country joins,
which four existing Atlas countries still have open.

## A combination no other Atlas country has in one body

Mapping and the land registry sit together here. Elsewhere they are split:

- [[GB-OS]] maps; the UK land registries are separate and unmodelled.
- [[NL-KADASTER]] holds the cadastre **and** the topographic register
  [[NL-BRT]] — the closest parallel, and still not a merger of three bodies.
- [[NO-KARTVERKET]] holds mapping and the property register.

If confirmed, Ireland and Norway are the two countries that fuse the
functions. The word "if" is doing real work in that sentence, which is what
`confidence: low` records.

## Not modelled

- The **establishing legislation** and the merger date.
- Whether Ireland has an **INSPIRE** transposition, and Tailte Éireann's
  role in it.
- **data.geohive.ie** and Ireland's spatial data infrastructure.

## Sources

Listed in frontmatter. **Neither is a government legal source**, which is
why this entity is flagged for re-sourcing ahead of the rest of the Irish
set.
