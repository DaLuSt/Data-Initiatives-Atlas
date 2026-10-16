---
id: AU
type: country
name: "Australia"
description: >
  Country anchor entity for Australia. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: AU
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - AU-OAIC
  - AU-PRIVACY-ACT-1988
  - AU-DATA-ACT-2022
relationships: []

sources:
  - title: "About the OAIC"
    url: "https://www.oaic.gov.au/about-the-OAIC"
    publisher: "Office of the Australian Information Commissioner"
    accessed: "2026-10-16"
---

# Australia

## Description

Australia (ISO 3166-1 alpha-2: **`AU`**) is a **base country anchor**. It carries the Privacy Act 1988 ([[AU-PRIVACY-ACT-1988]]), the Data Availability and Transparency Act 2022 ([[AU-DATA-ACT-2022]]) and the Office of the Australian Information Commissioner ([[AU-OAIC]]), read on the Federal Register of Legislation and the Office's own site.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). The Consumer Data Right, the National Data Commissioner's own site, the Digital Transformation Agency, the states and territories and the sectoral laws are not modelled. It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
