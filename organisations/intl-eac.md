---
id: INTL-EAC
type: organisation
name: "East African Community (EAC)"
alternative_names:
  - "EAC"
description: >
  The regional intergovernmental organisation of Burundi, DR Congo, Kenya, Rwanda, Somalia, South Sudan, Uganda and Tanzania,
  headquartered in Arusha, Tanzania. The Treaty for its establishment was signed on 30 November 1999 by Kenya, Uganda and
  Tanzania. Its digital and data work, from its own pages, is the World Bank-financed Eastern Africa Regional Digital
  Integration Project, the EAC Open Data Portal, and an AI Strategy and a Digital Transformation Strategy adopted by its
  Sectoral Council in October 2026. Read through the fetch tool, not directly.

level: regional
country: null
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

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - INTL-EAC-AI-STRATEGY
  - INTL-EAC-DIGITAL-TRANSFORMATION-STRATEGY
  - INTL-EARDIP
  - INTL-EAC-OPEN-DATA
  - KE
  - SO
  - TZ
  - UG
relationships:
  - type: related-to
    target: KE
    source: fact
    evidence: "The EAC home page (read 2026-11-01 through the fetch tool, a summary of the page): the EAC's eight Partner States are Burundi, DR Congo, Kenya, Rwanda, Somalia, South Sudan, Uganda and Tanzania. Kenya is one of them."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: SO
    source: fact
    evidence: "The EAC home page (read 2026-11-01 through the fetch tool, a summary of the page): the EAC's eight Partner States are Burundi, DR Congo, Kenya, Rwanda, Somalia, South Sudan, Uganda and Tanzania. Somalia is one of them."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: TZ
    source: fact
    evidence: "The EAC home page (read 2026-11-01 through the fetch tool, a summary of the page): the EAC's eight Partner States are Burundi, DR Congo, Kenya, Rwanda, Somalia, South Sudan, Uganda and Tanzania. Tanzania is one of them."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: UG
    source: fact
    evidence: "The EAC home page (read 2026-11-01 through the fetch tool, a summary of the page): the EAC's eight Partner States are Burundi, DR Congo, Kenya, Rwanda, Somalia, South Sudan, Uganda and Tanzania. Uganda is one of them."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "East African Community — home page"
    url: "https://www.eac.int/"
    publisher: "East African Community"
    accessed: "2026-11-01"
    note: "Read through the fetch tool, which returns a model's summary of the page, because eac.int refuses the agent's direct requests; names and dates are as that summary reported them."
---

# East African Community (EAC)

> **Created 2026-11-01** (roadmap #550, Eastern Africa). `eac.int` refuses the agent's direct requests (HTTP 403), so its home page and three pages under it were read through the fetch tool, which returns a model's summary of a page rather than its text. Facts are limited to those the summary gave with their wording (member states, the treaty's signing date, headquarters, the names of the project and strategies); `start_date` is left empty because the signing date is not the date of entry into force. The Treaty itself, the member-state edges for Burundi, DR Congo, Rwanda and South Sudan (no anchors) and the Community's cyber-laws and data-protection work were not read.

## Relationships

Runs [[INTL-EARDIP]] and [[INTL-EAC-OPEN-DATA]]; adopted [[INTL-EAC-AI-STRATEGY]] and [[INTL-EAC-DIGITAL-TRANSFORMATION-STRATEGY]]. Partner States with anchors: [[KE]], [[SO]], [[TZ]], [[UG]].
