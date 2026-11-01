---
id: IN
type: country
name: "India"
description: >
  Country anchor entity for India. A base anchor: it exists because the Atlas models the sourced national entities
  listed in its index, and it carries no more than that.

level: national
country: IN
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - IN-DPDP-ACT-2023
  - IN-DPDP-RULES-2025
  - IN-DPB
  - IN-MEITY
relationships: []

sources:
  - title: "DPDP Rules, 2025 Notified: A Citizen-Centric Framework for Privacy Protection and Responsible Data Use (17 November 2025)"
    url: "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf"
    publisher: "Press Information Bureau, Government of India"
    accessed: "2026-11-01"
---

# India

## Description

India (ISO 3166-1 alpha-2: **`IN`**) is a **base country anchor**. It carries the Digital Personal Data Protection Act, 2023 ([[IN-DPDP-ACT-2023]]), the Digital Personal Data Protection Rules, 2025 ([[IN-DPDP-RULES-2025]]), the Data Protection Board of India ([[IN-DPB]]) and the Ministry of Electronics and Information Technology ([[IN-MEITY]]), all from the Press Information Bureau's own explainer of the Rules; neither the Act's nor the Rules' text was read (`meity.gov.in` is a JavaScript page, and the Act's usual copies were not reachable).

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). It is a first sourced slice, not a survey of the country's data governance: the Information Technology Act 2000, the Aadhaar Act, the National Data Governance Policy and the Digital India programmes, among much else, are not in the Atlas yet (see `countries/README.md` on the participation model).
