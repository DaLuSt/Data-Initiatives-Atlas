---
id: EU-SKILLS-DATA-SPACE
type: data-space
name: Common European skills data space
alternative_names:
  - Skills data space
  - Data space for skills
description: >
  One of the fourteen common European data spaces, covering skills. It is
  named by the Commission among the strategic sectors of the European Data
  Strategy and is positioned alongside the cultural heritage and tourism
  data spaces in the Commission's own presentation of the ecosystem.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains: 
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-DS4SKILLS
  - EU-EDGE-SKILLS
  - EU-ESCO
  - EU-EUROPASS
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Skills is one of the fourteen common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21 final of 24.1.2024; digital-strategy.ec.europa.eu 'Common European data spaces'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SWD(2024) 21 final — Staff working document on common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/library/staff-working-document-data-spaces"
    publisher: "European Commission"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-09-05"
  - title: "Introducing DS4Skills: Europe's first Data Space for Skills"
    url: "https://hadea.ec.europa.eu/news/introducing-ds4skills-europes-first-data-space-skills-2025-07-01_en"
    publisher: "European Health and Digital Executive Agency (HaDEA)"
    accessed: "2026-09-05"
---

# Common European skills data space

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Updated 2026-09-05**: the deployment-projects gap this entity itself
> flagged is now partly closed. [[EU-DS4SKILLS]] models one of the two named
> rollout projects. The ESCO/Europass/European Skills Agenda question was
> checked directly rather than left as a presumption — see below.
>
> **Closed 2026-09-20**: the second rollout project, EDGE-Skills, is now
> [[EU-EDGE-SKILLS]]. Both named rollout projects are modelled;
> `coverage` moves to `medium`.

## Description

One of the fourteen common European data spaces, covering skills.
It is named by the Commission among the strategic sectors of the European Data Strategy and is positioned alongside the cultural heritage and tourism data spaces in the Commission's own presentation of the ecosystem.

## It gives [[DOMAIN-EDUCATION]] its second entity

Before this batch, [[DOMAIN-EDUCATION]] was reachable from **one** entity in
**one** country — the Netherlands. It is the thinnest domain in the Atlas,
alongside health and research, and this is the first EU-level entity to carry
it.

That does not make the domain well covered. Six of ten countries still have
no education entity at all, and the gap is logged in
`discovery/candidates.md` as part of the lopsided-domain finding.

## `coverage: medium`, both rollout projects now modelled

What this data space contains and who deploys it is now established.
Reading digital-strategy.ec.europa.eu's own page directly (2026-09-05): under
its rollout listing for skills, exactly two projects are named —
**[[EU-DS4SKILLS]]** and **[[EU-EDGE-SKILLS]]**. Both are now modelled: DS4Skills
(2026-09-05) and EDGE-Skills (2026-09-20), the latter sourced from
Prometheus-X's own whitepaper describing itself as "led by Prometheus-X,"
uniting 36 organisations from eight EU countries.

How it relates to Europass, ESCO or the European Skills Agenda was checked
directly this pass, not merely presumed: neither DS4Skills' own site nor
HaDEA's announcement of it mentions any of the three. That is a
checked-and-negative finding, not an unresearched gap.

## Not modelled

- The **European Skills Agenda** — previously presumed to be existing
  EU skills-data machinery this data space builds on. Checked directly
  against [[EU-DS4SKILLS]]'s own sources (2026-09-05): not mentioned.
  Still not an Atlas entity, and still not confirmed connected to this
  data space by any source read.

**ESCO and Europass, researched 2026-09-26**: both now their own
entities, [[EU-ESCO]] (launched 28 July 2017, maintained by DG EMPL) and
[[EU-EUROPASS]] (current legal basis Decision (EU) 2018/646, original
framework from 2004). Re-checked directly against each one's own page:
still no stated connection to this data space for either, so
`related-to` at `confidence: low` is recorded on each entity's own file
rather than a stronger claim.

## Sources

Listed in frontmatter.
