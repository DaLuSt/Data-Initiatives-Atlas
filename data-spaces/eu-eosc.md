---
id: EU-EOSC
type: data-space
name: European Open Science Cloud
alternative_names:
  - EOSC
  - EOSC Federation
  - Research and innovation data space
description: >
  The European Open Science Cloud, the common European data space for
  research and innovation. It is a federation rather than a single system:
  the EOSC EU Node, procured by the Commission, launched in October 2024
  as the first node, and an operational EOSC Federation was demonstrated
  in 2025 with thirteen candidate nodes including CERN and EMBL. It
  implements the FAIR principles — findability, accessibility,
  interoperability and reusability.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: 
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-EOSC-ASSOCIATION
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Confirmed by reading digital-strategy.ec.europa.eu's own 'Common European data spaces' overview directly (2026-08-28): research and innovation, anchored by EOSC, is named among the fourteen. The Commission's Research and Innovation page on EOSC, read directly, confirms the EOSC EU Node 'was procured and launched... in October 2024 as the first node of the EOSC Federation.' A November 2025 Research and Innovation news article, read directly, confirms the Federation milestone celebrated 5 November 2025 at the EOSC Symposium in Brussels, with '13 candidate EOSC Nodes' including CERN and EMBL. The 'staff working document on data spaces' URL originally cited pointed to the wrong Commission document (SWD(2022) 45 final, not SWD(2024) 21 final) — corrected below."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Norway — Tripartite collaboration"
    url: "https://eosc.eu/tripartite-collaboration/norway"
    publisher: "EOSC Association"
    accessed: "2026-09-18"
  - title: "Switzerland — Tripartite collaboration"
    url: "https://eosc.eu/tripartite-collaboration/switzerland"
    publisher: "EOSC Association"
    accessed: "2026-09-18"
  - title: "Second staff working document on data spaces — SWD(2024) 21 final"
    url: "https://digital-strategy.ec.europa.eu/en/library/second-staff-working-document-data-spaces"
    publisher: "European Commission"
    accessed: "2026-08-28"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-28"
  - title: "The European Open Science Cloud"
    url: "https://eosc.eu/eosc-about"
    publisher: "EOSC Association"
    accessed: "2026-08-28"
  - title: "European Open Science Cloud (EOSC)"
    url: "https://research-and-innovation.ec.europa.eu/strategy/strategy-research-and-innovation/our-digital-future/open-science/european-open-science-cloud-eosc_en"
    publisher: "European Commission — Research and Innovation"
    accessed: "2026-08-28"
  - title: "Welcoming the EOSC Federation, a major milestone for open science"
    url: "https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/welcoming-eosc-federation-major-milestone-open-science-2025-11-05_en"
    publisher: "European Commission — Research and Innovation"
    accessed: "2026-08-28"
---

# European Open Science Cloud

> **Re-verified 2026-08-28.** All five cited sources were read directly
> (after correcting one stale SWD URL to the right Commission document),
> and every substantive claim in this entity's description — the October
> 2024 EOSC EU Node launch, the November 2025 Federation milestone, the
> thirteen candidate nodes including CERN and EMBL — was confirmed word
> for word against the Commission's own pages. `verification` moves to
> `primary-source` and `confidence` rises to `high`.
>
> **Updated 2026-09-05**: the EOSC Association, this entity's own flagged
> gap, is now modelled as [[EU-EOSC-ASSOCIATION]].
>
> **Updated 2026-09-18**: the Federation's own non-EU participation
> question, flagged below since the batch that created this entity, is
> answered — see "The most operational of the fourteen."

## Description

The European Open Science Cloud, the common European data space for research and innovation.
It is a federation rather than a single system: the EOSC EU Node, procured by the Commission, launched in October 2024 as the first node, and an operational EOSC Federation was demonstrated in 2025 with thirteen candidate nodes including CERN and EMBL.
It implements the FAIR principles — findability, accessibility, interoperability and reusability.

## The most operational of the fourteen

EOSC is the one common European data space that already runs.

| Date | Milestone |
|---|---|
| **October 2024** | The **EOSC EU Node**, procured by the Commission, launches as the first node of the Federation |
| **2025** | An operational **EOSC Federation** is demonstrated, with **thirteen candidate nodes** — including CERN and EMBL, several ESFRI Landmarks and ERICs, and national research data initiatives |

It is explicitly **not a monolith**: a *system of systems*, federating many
independent organisations and resource providers around the **FAIR
principles** — findability, accessibility, interoperability, reusability.

## Why it matters to this Atlas beyond the sector

[[DOMAIN-RESEARCH]] was reachable from **one** country before this batch —
the Netherlands, through [[NL-HEALTH-RI]] and [[NL-SURF]]. EOSC gives the
research domain its EU-level anchor, which it did not have.

The federated model is also the closest thing in the Atlas to what
[[NO]] and the EEA states would need: a structure that admits participants
who are not member states. **Researched 2026-09-18 — yes, on a
Horizon-Europe-association basis, not EU membership.** EOSC's own
"tripartite collaboration" pages, read directly, confirm it in both
directions: Norway's page names a Norwegian EOSC Steering Board
representative (Ola Berge, Ministry of Education and Research) and states
outright, "Although Norway is not an EU member state, it draws on the ERA
policy agenda for the development of its national policies." Switzerland's
own page gives the eligibility rule explicitly: *"The relationship between
the EOSC and Switzerland is different from most countries... due to the
fact that Switzerland is currently not associated to Horizon Europe or of
the EOSC Steering Board"* — tying Steering Board participation to Horizon
Europe association, not EU membership, and confirming why Norway (fully
associated) sits on it while Switzerland (not, at the time of that page)
does not. No relationship edge is added — this is a governance-eligibility
fact about EOSC itself, not a sourced participation claim for [[NO]] or
any specific EEA state's own entity, which would need its own citation.

## The EOSC Association, modelled 2026-09-05

Previously flagged as unmodelled here: the distinct legal body governing
the EOSC initiative, separate from the Federation and from the
Commission's EU Node, is now [[EU-EOSC-ASSOCIATION]] — formed 29 July
2020 as a Belgian AISBL, `produces` this data space.

## Not modelled

- The **thirteen candidate nodes**, **CERN**, **EMBL**, the **ESFRI**
  landmarks and the **ERICs**.
- The **FAIR principles** themselves, which would sit in the standards layer
  alongside [[INTL-DCAT]].

## Sources

Listed in frontmatter, all five read directly in the 2026-08-28 pass.
`eosc.eu/eosc-about` was re-read 2026-09-05 to research the Association
question, which led to modelling [[EU-EOSC-ASSOCIATION]] from a
dedicated page on the same site.
