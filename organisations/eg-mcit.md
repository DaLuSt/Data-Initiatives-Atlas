---
id: EG-MCIT
type: organisation
name: "Ministry of Communications and Information Technology"
alternative_names:
  - "MCIT"
  - "ICT Ministry"
description: >
  Egypt's ministry for communications and information technology, which
  leads the Digital Egypt vision and the national AI strategy and has
  affiliated bodies such as ITIDA, NTI and ITI.

level: national
country: EG
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
  - EG
  - EG-ITIDA
relationships:
  - type: part-of
    target: EG
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. mcit.gov.eg, read directly (2026-10-11), is the site of the 'Ministry of Communications and Information Technology' of Egypt; its menu lists ITIDA among the ministry's affiliated bodies."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: EG-ITIDA
    source: fact
    evidence: "mcit.gov.eg's menu, read directly (2026-10-11), lists 'ITIDA' alongside ITI, NTI and others under the ministry. An association; the page states no formal affiliation type."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Information Technology Industry Development Agency (ITIDA)"
    url: "https://itida.gov.eg/English/Pages/default.aspx"
    publisher: "ITIDA"
    accessed: "2026-10-11"
  - title: "Ministry of Communications and Information Technology — home"
    url: "https://www.mcit.gov.eg/en"
    publisher: "Ministry of Communications and Information Technology (MCIT), Egypt"
    accessed: "2026-10-11"
---

# Ministry of Communications and Information Technology (MCIT), Egypt

> **Created 2026-10-11** (roadmap #471, Egypt). Its English home page was read directly; most of the content is a menu and news.

## Description

The ministry that leads Egypt's digital policy. Its site presents "Digital Egypt" as "an all-encompassing vision and plan laying the foundations for the transformation of Egypt into a digital society", lists programmes in digital transformation, telecommunications, human development, industry development, innovation, artificial intelligence and institutional development, and publishes the **National AI Strategy – Second Edition 2025-2030**, which is only seen as a title in a list and was not read. It also lists affiliated bodies including ITIDA ([[EG-ITIDA]]).

## What was not found

The Personal Data Protection Law (Law No. 151 of 2020) and the Personal Data Protection Centre are described by law-firm and compliance-vendor sources only; nothing on `mcit.gov.eg` or `itida.gov.eg` read on 2026-10-11 mentions them, so neither is recorded as an entity.

## Relationships

`part-of` [[EG]] (anchor edge); `related-to` [[EG-ITIDA]].
