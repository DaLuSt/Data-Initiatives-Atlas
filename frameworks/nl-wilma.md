---
id: NL-WILMA
type: framework
name: Waterschaps Informatie & Logisch Model Architectuur
alternative_names:
  - WILMA
description: >
  Reference architecture for the Dutch water authorities (waterschappen)
  — a set of architecture models and principles relevant to all 21
  water authorities, usable both to make mutual agreements between them
  and as a starting point for each authority's own enterprise
  architecture. Part of the NORA family of Dutch government
  architectures, alongside GEMMA (municipalities), PETRA (provinces),
  EAR/RORA (central government) and ROSA (education). Contact for the
  architecture runs through Het Waterschapshuis. The WILMA Academy,
  established autumn 2021, disseminates enterprise-architecture
  knowledge and expertise across the sector.

level: sectoral
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-NORA
  - NL-WATERSCHAPSHUIS
  - NL-UVW
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "Confirmed by reading noraonline.nl's own WILMA wiki page directly (2026-09-04): the page places WILMA under 'Nederlandse overheidsarchitecturen' (Dutch government architectures) and lists it within the NORA Family structure, scoped to 'Werkingsgebied: Waterschappen' (water authorities). Listed at 'Ontwikkelfase' (development phase) with an 'Informatief' (informational) obligation level."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "WILMA (Waterschaps Informatie & Logisch Model Architectuur)"
    url: "https://www.noraonline.nl/wiki/WILMA_(Waterschaps_Informatie_%26_Logisch_Model_Architectuur)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-09-04"
---

# WILMA — Waterschaps Informatie & Logisch Model Architectuur

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged WILMA as completing the
> NORA family, not created for want of a named source in Batch 4's
> scope. The NORA wiki's own WILMA page was read directly this pass.

## Description

WILMA is the reference architecture for the Dutch water authorities —
a set of architecture models and principles relevant to all 21 water
authorities, used both to make mutual agreements between them and as a
starting point for each authority's own enterprise architecture.

## The fifth NORA daughter now modelled

Reading `noraonline.nl`'s own wiki page directly: WILMA sits within the
**NORA Family** of Dutch government architectures, scoped to
**"Werkingsgebied: Waterschappen"** — the water-authority counterpart to
[[NL-GEMMA]] (municipalities), [[NL-ROSA]] (education) and the
provincial and central-government architectures. It is listed at
**"Ontwikkelfase"** (development phase), with an **"Informatief"**
obligation level — a weaker binding force than some of its NORA
siblings.

## Maintainer not stated explicitly

The NORA wiki page lists a contact address at
`WILMA@hetwaterschapshuis.nl`, suggesting [[NL-WATERSCHAPSHUIS]] plays a
coordinating role, but does not explicitly state that Het
Waterschapshuis maintains WILMA — so no `maintained-by` edge is
asserted, consistent with the Atlas's practice of not inferring a
relationship type stronger than what a source states. The **WILMA
Academy**, established autumn 2021, disseminates enterprise-architecture
knowledge across the sector.

## Relationships

- `based-on` [[NL-NORA]].

## Sources

Listed in frontmatter, read directly this pass.
