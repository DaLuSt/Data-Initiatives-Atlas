---
id: SD-TPRA
type: organisation
name: "Telecommunications and Post Regulatory Authority (Sudan)"
alternative_names:
  - "TPRA"
  - "National Telecommunications Authority (former name)"
description: >
  Sudan's telecommunications and postal regulator. The Ministry of Telecommunications and Digital Transformation's page says the National Telecommunications Authority was established in September 1996, that the name changed under the telecommunications and post Act of 2018, which replaced the 2001 telecommunications act, and that the Authority is 'the regulatory body responsible for regulating Telecommunications and post in Sudan', under the supervision of the minister, headquartered in Khartoum.
  The Authority's own site (tpra.gov.sd) answered HTTP 503; the Act was not read.

level: national
country: SD
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-23"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - SD
  - SD-TELECOM-POST-ACT-2018
relationships:
  - type: part-of
    target: SD
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Ministry's page (first read 2026-11-01 through a summarising fetch tool; re-read directly 2026-11-23): 'The Telecommunications and Post Regulatory Authority is the regulatory body responsible for regulating Telecommunications and post in Sudan … It is subject to the supervision of the minister responsible for the telecommunications sector in carrying out its duties'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: SD-TELECOM-POST-ACT-2018
    source: fact
    evidence: "The same page, re-read directly 2026-11-23: 'In early 2018 AD, the new telecommunications and Post Act for the year 2018 was approved, which came as an alternative to the telecommunications Act of 2001, according to which the name of the National Telecommunications Corporation was changed to a new name: Telecommunications and Post Regulatory Authority.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Telecommunications and Post Regulatory Authority (TPRA) - Ministry of Telecommunications and Digital Transformation"
    url: "https://mtdt.gov.sd/en/node/7"
    publisher: "Ministry of Telecommunications and Digital Transformation, Sudan"
    accessed: "2026-11-01"
---

# Telecommunications and Post Regulatory Authority (Sudan)

> **Created 2026-11-01** (roadmap #478). From the ministry's page, read through a summarising fetch tool. `start_date` empty: the page gives 'September 1996' for its predecessor only (a month, not a date).

## Relationships

Part of [[SD]]; governed by [[SD-TELECOM-POST-ACT-2018]].
