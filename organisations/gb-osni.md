---
id: GB-OSNI
type: organisation
name: Ordnance Survey of Northern Ireland
alternative_names:
  - OSNI
description: >
  The government mapping agency for Northern Ireland and the official producer
  of geographic mapping data for it. It is part of the Land and Property
  Services agency, and runs Spatial NI, a web mapping platform and portal for
  sharing and using geospatial data about Northern Ireland. It covers the part
  of the United Kingdom that Ordnance Survey (Great Britain) does not map.

level: subnational
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
organisation_role: executive
start_date: null
end_date: null
last_verified: "2026-10-09"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - GB-OS
relationships:
  - type: related-to
    target: GB-OS
    source: fact
    evidence: "Confirmed by reading OSNI's own pages directly (2026-10-09): the Department of Finance (Northern Ireland) page describes OSNI as 'the official producer of high quality, accurate and current geographic mapping data for Northern Ireland', and GOV.UK's about page calls it 'the government mapping agency for Northern Ireland'. That is the same national-mapping role that [[GB-OS]] holds for Great Britain, which is how the two are linked here; no source read states a formal relationship between the two bodies."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Ordnance Survey of Northern Ireland — Department of Finance"
    url: "https://www.finance-ni.gov.uk/topics/ordnance-survey-northern-ireland"
    publisher: "Department of Finance (Northern Ireland)"
    accessed: "2026-10-09"
  - title: "About us — Ordnance Survey of Northern Ireland — GOV.UK"
    url: "https://www.gov.uk/government/organisations/ordnance-survey-of-northern-ireland/about"
    publisher: "GOV.UK"
    accessed: "2026-10-09"
  - title: "Land & Property Services (LPS) — Department of Finance"
    url: "https://www.finance-ni.gov.uk/articles/land-property-services-lps"
    publisher: "Department of Finance (Northern Ireland)"
    accessed: "2026-10-09"
  - title: "Spatial NI — Background"
    url: "https://www.spatialni.gov.uk/about-background.html"
    publisher: "Ordnance Survey of Northern Ireland"
    accessed: "2026-10-09"
---

# Ordnance Survey of Northern Ireland

> **Verified 2026-10-09.** The Department of Finance's OSNI and Land &
> Property Services pages, GOV.UK's OSNI "About us" page and the Spatial NI
> background page were read directly.

## Description

Confirmed by reading the Department of Finance's page (2026-10-09): "Ordnance
Survey of Northern Ireland (OSNI) is the official producer of high quality,
accurate and current geographic mapping data for Northern Ireland." GOV.UK's
"About us" page: "OSNI is the government mapping agency for Northern Ireland.
It is a part of Land and Property Services agency." The Land & Property
Services page lists, among the services it provides, "mapping expertise and
specialist geospatial services through Ordnance Survey Northern Ireland
(OSNI)".

**Spatial NI** is, in its own words, "Ordnance Survey of Northern Ireland's web
mapping platform", a "one-stop-shop" for geospatial data about Northern
Ireland. It has a component, Spatial NI for INSPIRE, which "provides a network
of spatial data, accessible under the INSPIRE Directive". The Department's
page also lists the Pointer address database ("the common standard address for
every property in Northern Ireland") among OSNI's topics.

## Why this entity exists

[[GB-OS]] maps **Great Britain**, not the United Kingdom. Until this entity the
UK's geospatial picture had no Northern Ireland body. `level: subnational`
because OSNI's scope is one part of the United Kingdom; `country: GB` is the
only ISO code that covers it.

## `coverage: low`

Not modelled: **Land & Property Services** (the parent agency) and the
Department of Finance above it; the Pointer address database, Spatial NI and the
Northern Ireland Mapping Agreement as entities of their own; OSNI's open data
and its licences; whether OSNI participates in [[UN-GGIM]] or other bodies
([[GB-OS]] does), which the pages read do not say. The date OSNI was founded
and the legal basis of its role were not on the pages read.

## Relationships

- `related-to` [[GB-OS]] — the same role for the other part of the UK. No
  formal relationship is asserted.

## Sources

Listed in frontmatter.
