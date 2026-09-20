---
id: EU-OMEGA-X
type: initiative
name: OMEGA-X
alternative_names:
  - "Orchestrating an interoperable sovereign federated Multi-vector Energy data space built on open standards and ready for GAia-X"
description: >
  A Horizon Europe Innovation Action (grant agreement 101069287) building a
  federated, Gaia-X-ready energy data space spanning electricity, gas and
  heat. Coordinated by Atos IT Solutions and Services Iberia (Spain), with
  34 participants plus 5 partner organisations across eleven countries. One
  of the six Horizon Europe energy data space projects the European
  Commission names as supporting deployment of the Common European Energy
  Data Space (CEEDS).

level: regional
country: null
region: EU

status: completed
confidence: medium
coverage: low
verification: primary-source

start_date: 2022-05-01
end_date: 2025-04-30
last_verified: "2026-09-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-CEEDS
  - EU-GAIA-X
relationships:
  - type: part-of
    target: EU-CEEDS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #132's 'six Horizon Europe energy data space projects' gap. Confirmed by reading community.intnet.eu's own page directly (2026-09-20, the coordination site of Int:net, itself one of the six projects): 'the European Commission supports the deployment of the energy data space through six energy data space projects funded under Horizon Europe — five Innovation Action projects (DATA CELLAR; EDDIE; Enershare; Omega-X; SYNERGIES) and one Coordination and Support Action (Int:net)', naming OMEGA-X as one of them. [[EU-CEEDS]]'s own entity independently describes itself as 'building on the results of six energy data space projects funded under Horizon Europe.' `part-of` mirrors the type already used for [[EU-INSIEME]] and the skills data space's deployment projects ([[EU-DS4SKILLS]], [[EU-EDGE-SKILLS]]), though the framing here (a predecessor project CEEDS 'builds on') is slightly different from INSIEME's (a project that itself 'pilots and operationalises' CEEDS) — noted rather than smoothed over."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-GAIA-X
    source: fact
    evidence: "The project's own full title, confirmed via its official CORDIS record (id 101069287, read directly 2026-09-20) and corroborated by omega-x.eu's own homepage (read directly), is 'Orchestrating an interoperable sovereign federated Multi-vector Energy data space built on open standards and ready for GAia-X' — stating Gaia-X alignment as a design goal in the project's own name, though neither source elaborates the technical basis beyond the title itself."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "OMEGA-X — CORDIS project record (Grant Agreement 101069287)"
    url: "https://cordis.europa.eu/project/id/101069287"
    publisher: "European Commission — CORDIS"
    accessed: "2026-09-20"
  - title: "Omega-X — Orchestrating an interoperable sovereign federated Multi-vector Energy Data Space built on open standards and ready for GAia-X"
    url: "https://omega-x.eu/"
    publisher: "OMEGA-X project"
    accessed: "2026-09-20"
  - title: "The emerging Common European Energy Data Space — state of play and next steps"
    url: "https://community.intnet.eu/events/35/the-emerging-common-european-energy-data-space---state-of-play-and-next-steps"
    publisher: "Int:net (Horizon Europe Coordination and Support Action)"
    accessed: "2026-09-20"
---

# OMEGA-X

> **Created 2026-09-20**, partially closing `discovery/unresolved.md` row
> #132's remaining gap: naming and modelling the "six Horizon Europe
> energy data space projects" [[EU-CEEDS]] and [[EU-INSIEME]] were already
> known to build on but that no source had individually named. Sourced
> from OMEGA-X's own official CORDIS record, its own project site, and
> Int:net's own coordination-site page naming all six projects by name.

## Description

OMEGA-X is a **Horizon Europe Innovation Action**, confirmed via its
official CORDIS record (Grant Agreement **101069287**): coordinated by
**Atos IT Solutions and Services Iberia** (Spain), with **34 participants
plus 5 partner organisations** across **Spain, France, Germany, Portugal,
Italy, Greece, Belgium, Denmark, Norway, Serbia and Ireland**. Total cost
**€10,223,435**, EU contribution **€7,995,320.38**, running **1 May 2022 –
30 April 2025**.

Its own site describes the aim as a **federated infrastructure, data
marketplace and service marketplace** for the multi-vector energy sector
(electricity, gas, heat), addressing low data availability for innovative
uses while preserving privacy, security and data sovereignty, and
"guaranteeing scalability and interoperability with other data space
initiatives."

## One of six named CEEDS-supporting projects

Int:net's own coordination-site page, read directly, names all six
Horizon Europe projects the Commission funds to support CEEDS deployment:
five Innovation Actions — **DATA CELLAR, EDDIE, Enershare, Omega-X,
SYNERGIES** — and one Coordination and Support Action, **Int:net** itself.
This closes the naming half of the row #132 gap first flagged on
[[EU-INSIEME]]'s own creation. Of the five Innovation Actions, this entity
and [[EU-ENERSHARE]] are now modelled; **DATA CELLAR, EDDIE and SYNERGIES**
remain unmodelled, as does Int:net itself.

## Not modelled

- **DATA CELLAR, EDDIE, SYNERGIES** and **Int:net** — the four other named
  Horizon Europe CEEDS-supporting projects.
- The project's **individual pilot/demonstration sites** (renewables,
  local energy communities, electromobility, grid flexibility) — named
  only categorically on the project's own site, not itemised.
- The **specific technical basis** of the Gaia-X alignment stated in the
  project's own title.

## Relationships

- `part-of` [[EU-CEEDS]] — `confidence: medium`.
- `based-on` [[EU-GAIA-X]] — `confidence: medium`, from the project's own
  title.

## Sources

Listed in frontmatter, all three read directly.
