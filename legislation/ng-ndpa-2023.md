---
id: NG-NDPA-2023
type: act
name: "Nigeria Data Protection Act 2023"
alternative_names:
  - "NDP Act 2023"
  - "NDPA"
description: >
  Nigeria's data protection statute, signed into law on 12 June 2023. It
  established the Nigeria Data Protection Commission and sets the rights of
  data subjects (sections 34 to 38 on the Commission's site) and the duties
  of data controllers and processors. The Act's own text was not read.

level: national
country: NG
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2023-06-12
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NG-NDPC
related_entities:
  - NG
  - NG-NDPC
  - NG-NDPA-GAID-2025
relationships:
  - type: applies-in
    target: NG
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Commission's About page, read directly (2026-10-16): 'the Federal Government of Nigeria signed into law the Nigeria Data Protection Act 2023 (NDP Act) on June 12, 2023'."
    confidence: high
    valid_from: 2023-06-12
    valid_until: null

sources:
  - title: "About Us — Nigeria Data Protection Commission"
    url: "https://ndpc.gov.ng/about-us/"
    publisher: "Nigeria Data Protection Commission"
    accessed: "2026-10-16"
  - title: "Nigeria Data Protection Commission — home page"
    url: "https://ndpc.gov.ng/"
    publisher: "Nigeria Data Protection Commission"
    accessed: "2026-10-16"
---

# Nigeria Data Protection Act 2023

> **Created 2026-10-16** (roadmap #475, Nigeria). Known from the Commission's own pages and from the directive that implements it; the Act's text was not read. `start_date` is the date the About page gives for signature; whether the Act took effect the same day was not checked.

## What is sourced

- The About page: signed 12 June 2023; it established the Commission ([[NG-NDPC]]); objectives are to safeguard natural persons' data-privacy rights, promote secure processing and strengthen the digital economy's legal foundations.
- The home page lists data-subject rights under ss. 34-38 and controller and processor responsibilities under s. 29.
- The 2025 directive ([[NG-NDPA-GAID-2025]]) cites ss. 1(a), 6(c), 61 and 62 of the Act as its enabling powers.

## Relationships

Applies in [[NG]] (anchor edge). Implemented by [[NG-NDPA-GAID-2025]]; [[NG-NDPC]] is `governed-by` it.
