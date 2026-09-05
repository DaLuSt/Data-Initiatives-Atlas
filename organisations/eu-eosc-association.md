---
id: EU-EOSC-ASSOCIATION
type: organisation
name: EOSC Association
alternative_names:
  - European Open Science Cloud Association
description: >
  International not-for-profit association under Belgian law (AISBL)
  that governs the European Open Science Cloud initiative, distinct from
  both the EOSC Federation of nodes and the Commission's EOSC EU Node.
  Formed on 29 July 2020 with four founding members, it has since grown
  to more than 250 members and observers, and is jointly responsible
  with the European Union for delivering the objectives of a Memorandum
  of Understanding forming an official EU–EOSC Partnership.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2020-07-29
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - EU-EOSC
relationships:
  - type: produces
    target: EU-EOSC
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. EU-EOSC's own entity already cited eosc.eu/eosc-about as a source without extracting this fact. Confirmed by reading eosc.eu's own 'The EOSC Association' page directly (2026-09-05): the Association 'was formed on 29 July 2020 with four founding members, and has since grown to 250 Members and Observers,' is 'jointly responsible for delivering the objectives agreed in the Memorandum of Understanding signed by the European Union and EOSC Association to form the official Partnership,' and 'plays an important role in helping to coordinate and steer these investments via its Task Forces and other governance structures' — including building the EOSC Federation of nodes. A WebSearch cross-check independently confirms the Belgian AISBL legal form, not itself stated on the page read directly. Recorded as `produces` — the Association governs and steers the initiative the Federation/EU Node implement, the same relationship type used for EU-EUROPEANA-FOUNDATION → EU-CULTURAL-HERITAGE-DATA-SPACE."
    confidence: medium
    valid_from: 2020-07-29
    valid_until: null

sources:
  - title: "The EOSC Association"
    url: "https://eosc.eu/eosc-association/"
    publisher: "EOSC Association"
    accessed: "2026-09-05"
  - title: "The European Open Science Cloud (about page)"
    url: "https://eosc.eu/eosc-about"
    publisher: "EOSC Association"
    note: "Already cited on EU-EOSC prior to this pass; re-read for this specific question, confirming organisational structure (President, Board of Directors, Secretariat, Task Forces) but not the legal-form or founding-date facts, which come from the dedicated 'EOSC Association' page instead."
---

# EOSC Association

> **Created 2026-09-05**, closing the gap [[EU-EOSC]] itself had flagged:
> "The EOSC Association, which is a distinct legal body from the
> Federation and from the Commission's EU Node," named but not modelled.

## Description

Confirmed by reading eosc.eu's own "The EOSC Association" page directly:
the Association "was formed on **29 July 2020** with four founding
members, and has since grown to **250 Members and Observers**." A
WebSearch cross-check independently confirms it is incorporated as an
international not-for-profit association under Belgian law (AISBL) — a
fact not itself stated on the page read directly, so recorded at
`confidence: medium` rather than asserted as verbatim-confirmed.

The Association is "jointly responsible for delivering the objectives
agreed in the Memorandum of Understanding signed by the European Union
and EOSC Association to form the official Partnership," and "plays an
important role in helping to coordinate and steer" EOSC investments "via
its Task Forces and other governance structures" — including building
the EOSC Federation of nodes that [[EU-EOSC]] itself models.

## Three distinct EOSC bodies, one now modelled

[[EU-EOSC]]'s own entry already distinguished three things sharing the
name EOSC: the **Association** (governance), the **Federation** (the
system of systems of nodes), and the Commission's **EOSC EU Node** (the
first procured node). Only the Federation/data-space layer was
previously modelled. This entity closes the Association gap; the EU
Node remains a Commission procurement detail recorded in [[EU-EOSC]]'s
own prose rather than as a separate entity.

## Not modelled

- The Association's **Task Forces**, **Board of Directors** and
  **Secretariat** structures, named on eosc.eu but not independently
  researched.
- The **Memorandum of Understanding** with the EU forming the "official
  Partnership" — not modelled as a separate legislation/framework
  entity.
- Individual **member organisations** of the Association (CESAER and
  others are named in secondary sources as founding or early members,
  not independently confirmed here).

## Relationships

- `produces` [[EU-EOSC]] — governs and steers the initiative the EOSC
  Federation and EU Node implement.

## Sources

Two sources, both on `eosc.eu`; the dedicated "EOSC Association" page
read directly this pass. `eosc.eu/eosc-about` was already cited on
[[EU-EOSC]] prior to this pass and was re-read for this specific
question.
