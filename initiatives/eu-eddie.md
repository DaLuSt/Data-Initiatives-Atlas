---
id: EU-EDDIE
type: initiative
name: EDDIE
alternative_names:
  - "European Distributed Data Infrastructure for Energy"
description: >
  A Horizon Europe Innovation Action (grant agreement 101069510) building a
  decentralised, distributed data infrastructure for the energy sector, so
  that energy service companies can work and compete in a common European
  market. Coordinated by FH OÖ Forschungs & Entwicklungs GmbH (the research
  arm of the University of Applied Sciences Upper Austria), with 18
  participants across eight countries. One of the six Horizon Europe
  energy data space projects the European Commission names as supporting
  deployment of the Common European Energy Data Space (CEEDS).

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2023-01-01
end_date: 2026-06-30
last_verified: "2026-09-20"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-CEEDS
  - EU-INSIEME
relationships:
  - type: part-of
    target: EU-CEEDS
    source: fact
    evidence: "FURTHER CLOSES discovery/unresolved.md row #132's 'six Horizon Europe energy data space projects' gap (see [[EU-OMEGA-X]] for the full finding). Confirmed by reading community.intnet.eu's own page directly (2026-09-20): EDDIE is named as one of five Innovation Action projects the Commission funds under Horizon Europe to support CEEDS deployment. EDDIE's own CORDIS objective (read directly) independently describes building 'a streamlined, uniform European interface to energy data' — consistent with but not itself naming CEEDS."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EDDIE — CORDIS project record (Grant Agreement 101069510)"
    url: "https://cordis.europa.eu/project/id/101069510"
    publisher: "European Commission — CORDIS"
    accessed: "2026-09-20"
  - title: "The emerging Common European Energy Data Space — state of play and next steps"
    url: "https://community.intnet.eu/events/35/the-emerging-common-european-energy-data-space---state-of-play-and-next-steps"
    publisher: "Int:net (Horizon Europe Coordination and Support Action)"
    accessed: "2026-09-20"
---

# EDDIE

> **Created 2026-09-20**, further closing `discovery/unresolved.md` row
> #132 alongside [[EU-OMEGA-X]], [[EU-ENERSHARE]] and [[EU-DATA-CELLAR]] —
> see [[EU-OMEGA-X]] for the full "six named projects" finding. Sourced
> from EDDIE's own official CORDIS record and Int:net's own
> coordination-site page.

## Description

EDDIE is a **Horizon Europe Innovation Action**, confirmed via its
official CORDIS record (Grant Agreement **101069510**): coordinated by
**FH OÖ Forschungs & Entwicklungs GmbH** (Austria) — the research arm of
the University of Applied Sciences Upper Austria, the same institution
that coordinates [[EU-INSIEME]] — with **18 participants** across
**Austria, Denmark, Italy, Germany, Spain, Greece, France and Belgium**.
Total cost **€8,900,168.77**, EU contribution **€7,989,333.01**, running
**1 January 2023 – 30 June 2026**.

CORDIS states its objective as addressing barriers to the clean energy
transition by establishing a decentralised data infrastructure: the
"EDDIE Framework lets energy service companies work and compete in a
common European market," aiming at "a streamlined, uniform European
interface to energy data usable by everyone from service companies to
end-user customers."

## Shared coordinator with INSIEME, not stated as a formal link

Both EDDIE and [[EU-INSIEME]] are coordinated by the same institution, FH
OÖ / SAIL. No source read this pass states this shared coordination
creates any organisational relationship between the two projects
themselves — recorded here as an observation, not asserted as an edge.

## One of six named CEEDS-supporting projects

See [[EU-OMEGA-X]] for the full finding: Int:net's own coordination-site
page names EDDIE as one of five Horizon Europe Innovation Actions
(alongside DATA CELLAR, Enershare, Omega-X and SYNERGIES) supporting
CEEDS deployment, plus Int:net itself as the sixth, a Coordination and
Support Action.

## Not modelled

- **SYNERGIES** and **Int:net** — the remaining named projects.
- EDDIE's **Common Information Model** and individual pilot deployments,
  described on `eddie.energy` but not read directly this pass.

## Relationships

- `part-of` [[EU-CEEDS]] — `confidence: medium`.

## Sources

Listed in frontmatter, both read directly.
