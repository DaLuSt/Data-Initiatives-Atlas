---
id: UG-NITA-U
type: organisation
name: "National Information Technology Authority – Uganda"
alternative_names:
  - "NITA-U"
description: >
  Uganda's national IT authority, mandated to coordinate, promote and
  monitor IT development. It runs e-government services, IT certification
  and information security and hosts the Personal Data Protection Office.

level: national
country: UG
region: null

status: active
organisation_role: executive
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
  - UG-PDPO
relationships:
  - type: part-of
    target: UG
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. nita.go.ug, read directly via a runner (2026-10-11): 'The National Information Technology Authority – Uganda (NITA-U) is mandated to coordinate, promote, and monitor IT development in line with national social and economic goals', based in Kampala."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: UG-PDPO
    source: fact
    evidence: "NITA-U's own site (read 2026-10-11) lists the 'Personal Data Protection Office' in its main menu and quick links, with its own address and domain (pdpo.go.ug). Secondary sources say the Data Protection and Privacy Act 2019 set it up as an independent office under NITA-U; the Act was not read, so only the association on NITA-U's own site is recorded."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Information Technology Authority – Uganda (NITA-U) — home"
    url: "https://www.nita.go.ug/"
    publisher: "NITA-U"
    accessed: "2026-10-11"
---

# National Information Technology Authority – Uganda (NITA-U)

> **Created 2026-10-11** (roadmap #471, Uganda). Its home page was read directly on a runner. The statute establishing it was not read.

## Description

NITA-U is mandated, in the words of its site, "to coordinate, promote, and monitor IT development in line with national social and economic goals". The page lists e-government services, information security, IT certification, the **Personal Data Protection Office** ([[UG-PDPO]]), consumer affairs and technical services, and projects including the Uganda Digital Acceleration Project (UDAP-GovNet), the Uganda Enterprise Architecture and Interoperability Framework and the National Backbone Infrastructure project. It reports a NITA-U strategic plan FY2025/26-FY2029/30 launched on 18 June 2026 and an updated National Information Security Framework (NISF) 2026 launched in July 2026, both seen as headlines only.

## Relationships

`part-of` [[UG]] (anchor edge); `related-to` [[UG-PDPO]].
