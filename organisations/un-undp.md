---
id: UN-UNDP
type: organisation
name: United Nations Development Programme
alternative_names:
  - UNDP
description: >
  UN entity focused on supporting sustainable human development, active
  in nearly 170 countries and territories. Functions as a substantive
  integrator across the 2030 Agenda, connecting the economic, social and
  environmental dimensions of development, and as the system backbone at
  country level — convener, capacity-builder and service provider. Its
  Administrator serves as Vice-Chair of the UN Sustainable Development
  Group.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UN
  - UN-2030-AGENDA
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading sdgs.un.org's own UNDP page directly (2026-09-05): described as 'a UN entity' operating in nearly 170 countries and territories, with its Administrator serving as Vice-Chair of the UN Sustainable Development Group."
    confidence: high
    valid_from: null
    valid_until: null
  - type: implements
    target: UN-2030-AGENDA
    source: fact
    evidence: "Confirmed by reading sdgs.un.org's own UNDP page directly (2026-09-05): UNDP 'serves as a substantive integrator across the 2030 Agenda, helping countries connect economic, social, and environmental dimensions of development,' and functions as the 'system backbone' at country level for SDG implementation. Its Strategic Plan (2018-2021) is described as 'fully aligned with the 2030 Agenda.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "United Nations Development Programme (UNDP)"
    url: "https://sdgs.un.org/un-system-sdg-implementation/united-nations-development-programme-undp-24528"
    publisher: "United Nations (Department of Economic and Social Affairs — SDGs)"
    accessed: "2026-09-05"
---

# United Nations Development Programme (UNDP)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` had named "UN DESA, UNDP, WHO" together as
> "refused for want of sources" in Batch 13. `undp.org` itself returned
> HTTP 403 on every attempt this pass; `sdgs.un.org`, an official UN
> subdomain, was read directly instead and gave enough to model UNDP on
> its own terms.

## Description

UNDP is a UN entity focused on supporting sustainable human development,
active in nearly **170 countries and territories**. Reading `sdgs.un.org`'s
own page directly, it operates in four capacities: **specialised
expertise** across development topics; an **integration function**
connecting the economic, social and environmental dimensions of
development; the **system backbone** at country level, as convener and
capacity-builder; and a **service provider**, offering project management
and execution where needed. Its **Administrator serves as Vice-Chair of
the UN Sustainable Development Group**.

## Implements the 2030 Agenda

UNDP is described as "a substantive integrator across the 2030 Agenda,"
with its Strategic Plan (2018–2021) "fully aligned with" it — recorded as
`implements` [[UN-2030-AGENDA]], the Atlas's existing entity for the
General Assembly resolution (A/RES/70/1) this integrates.

## Relationships

- Part of [[UN]].
- `implements` [[UN-2030-AGENDA]].

## Sources

Listed in frontmatter, read directly this pass.
