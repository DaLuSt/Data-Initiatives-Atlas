---
id: UG-PDPO
type: organisation
name: "Personal Data Protection Office"
alternative_names:
  - "PDPO"
description: >
  Uganda's personal-data protection office, listed on the site of the
  National Information Technology Authority – Uganda with its own address
  and domain (pdpo.go.ug). The Act behind it was not read.

level: national
country: UG
region: null

status: active
organisation_role: regulatory
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UG
  - UG-NITA-U
relationships:
  - type: part-of
    target: UG
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. NITA-U's own site (read 2026-10-11) lists the 'Personal Data Protection Office' at 7th Floor, Padre Pio House, Plot 32 Lumumba Ave, Kampala, with the address info@pdpo.go.ug."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: UG-NITA-U
    source: fact
    evidence: "Listed in NITA-U's own menu and footer (read 2026-10-11). Association only; the Act that sets out the Office's legal position was not read."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Information Technology Authority – Uganda (NITA-U) — home"
    url: "https://www.nita.go.ug/"
    publisher: "NITA-U"
    accessed: "2026-10-11"
---

# Personal Data Protection Office (Uganda)

> **Created 2026-10-11** (roadmap #471, Uganda). Known from NITA-U's site only; the Office's own site `pdpo.go.ug` is a JavaScript shell (one character of text) for the agent and the runner, and the Data Protection and Privacy Act 2019 could not be read (`ulii.org` returns a 403 challenge).

## Description

Uganda's personal-data protection office. NITA-U's site lists it as a service with a Kampala address and its own domain. Secondary sources say the Data Protection and Privacy Act 2019 (assented 25 February 2019) created it as an independent office under NITA-U, that it became operational in August 2021 and that regulations followed in March 2021; **none of that was read** and none is asserted here.

## Relationships

`part-of` [[UG]] (anchor edge); `related-to` [[UG-NITA-U]].
