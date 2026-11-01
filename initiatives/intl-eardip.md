---
id: INTL-EARDIP
type: initiative
name: "Eastern Africa Regional Digital Integration Project (EARDIP)"
alternative_names:
  - "EARDIP"
  - "EA-RDIP"
description: >
  A World Bank-financed series of projects for digital integration in Eastern Africa, with four components: connectivity
  (cross-border terrestrial links, backbone and last mile), a data market (secure data exchange, storage and processing across
  regional borders, with data governance and cybersecurity as sub-areas), a digital market (the online market, e-service
  enablers, digital skills) and project management. The EAC page names IGAD, Somalia and South Sudan as implementing partners
  and lists no start date, end date or budget. Read through the fetch tool.

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
organisations:
  - INTL-EAC
related_entities:
  - INTL-EAC
  - INTL-IGAD
  - INTL-WBG
relationships:
  - type: maintained-by
    target: INTL-EAC
    source: fact
    evidence: "The EAC's EARDIP page (read 2026-11-01 through the fetch tool, a summary): the project is presented on the EAC's own site and 'run through the East African Community'; the page gives its funder as the World Bank."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-WBG
    source: fact
    evidence: "The same page: EARDIP is 'a World Bank financed series of projects' (the project code on a document filename is P176181)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-IGAD
    source: fact
    evidence: "The same page names IGAD among three implementing partners (with Somalia and South Sudan). IGAD's own Horn of Africa Digital Market Integration project is not stated to be the same project."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Eastern Africa Regional Digital Integration Project (EARDIP) — EAC"
    url: "https://www.eac.int/eardip"
    publisher: "East African Community"
    accessed: "2026-11-01"
    note: "Read through the fetch tool, which returns a model's summary of the page, because eac.int refuses the agent's direct requests; names and dates are as that summary reported them."
---

# Eastern Africa Regional Digital Integration Project (EARDIP)

> **Created 2026-11-01** (roadmap #550). One page read through the fetch tool (a model's summary; `eac.int` refuses direct requests). `status: active` because the EAC's home page carries EARDIP news items as late as October 2026. Participating countries, dates and amounts are not on that page. The data market component's data-governance and cybersecurity subpages were not read. IGAD's separate HDMI project ([[INTL-IGAD-HDMI]]) is not asserted to be part of or the same as this one.

## Relationships

Maintained by [[INTL-EAC]]; financed by the World Bank ([[INTL-WBG]]); implementing partner [[INTL-IGAD]].
