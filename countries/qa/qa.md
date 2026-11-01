---
id: QA
type: country
name: "Qatar"
description: >
  Country anchor entity for Qatar. A base anchor: it exists because the Atlas models the sourced national entities listed
  in its index, and it carries no more than that.

level: national
country: QA
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
  - QA-CRA
  - QA-CSP-REGULATION
relationships: []

sources:
  - title: "About CRA — Communications Regulatory Authority, State of Qatar"
    url: "https://cra.gov.qa/en/about-us"
    publisher: "Communications Regulatory Authority (CRA), State of Qatar"
    accessed: "2026-11-01"
---

# Qatar

## Description

Qatar (ISO 3166-1 alpha-2: **`QA`**) is a **base country anchor**. It carries the Communications Regulatory Authority ([[QA-CRA]]) and the Regulation for Certification Service Providers ([[QA-CSP-REGULATION]]) that makes the Authority the national supervisory body for trust services, from the Authority's own English site; neither document's text was opened. The personal data privacy law and the national cybersecurity bodies are not here: the Ministry of Communications and Information Technology's site (`mcit.gov.qa`) answers 403 and the cybersecurity agency's site is a JavaScript shell.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). It is a first sourced slice, not a survey of the country's data governance: the personal data privacy protection law, the Ministry and the National Cyber Security Agency, among others, are not in the Atlas yet (see `countries/README.md` on the participation model).
