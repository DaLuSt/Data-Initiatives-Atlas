---
id: EU-ENERSHARE
type: initiative
name: Enershare
alternative_names:
  - "European commoN EneRgy dataSpace framework enabling data sHaring-driven Across- and beyond- eneRgy sErvices"
description: >
  A Horizon Europe Innovation Action (grant agreement 101069831) developing
  a Reference Architecture for a European Energy Data Space, coordinated by
  Engineering — Ingegneria Informatica (Italy), with 30 partners across
  twelve countries. One of the six Horizon Europe energy data space
  projects the European Commission names as supporting deployment of the
  Common European Energy Data Space (CEEDS).

level: regional
country: null
region: EU

status: completed
confidence: medium
coverage: low
verification: primary-source

start_date: 2022-07-01
end_date: 2025-06-30
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-ENERGY
organisations: []
related_entities:
  - EU-CEEDS
  - EU-GAIA-X
relationships:
  - type: part-of
    target: EU-CEEDS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #132's 'six Horizon Europe energy data space projects' gap. Confirmed by reading community.intnet.eu's own page directly (2026-09-20, the coordination site of Int:net, itself one of the six projects): 'the European Commission supports the deployment of the energy data space through six energy data space projects funded under Horizon Europe — five Innovation Action projects (DATA CELLAR; EDDIE; Enershare; Omega-X; SYNERGIES) and one Coordination and Support Action (Int:net)', naming Enershare as one of them. The coordinator's own page (eng.it, read directly) independently states one of Enershare's key results is establishing 'a Common European Energy Data Space' — direct corroboration from the project's own lead partner. `part-of` mirrors the type used for [[EU-INSIEME]] and [[EU-OMEGA-X]]."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-GAIA-X
    source: fact
    evidence: "Confirmed by reading the coordinator's own page (eng.it) directly (2026-09-20): Enershare's reference architecture is stated to be compliant with 'FIWARE, IDSA, and GAIA-X standards.' Compliance-with is a real but looser basis than [[EU-OMEGA-X]]'s title-level Gaia-X framing, recorded at the same `based-on` type for consistency but flagged here as resting on a compliance statement rather than an architectural description."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "ENERSHARE — CORDIS project record (Grant Agreement 101069831)"
    url: "https://cordis.europa.eu/project/id/101069831"
    publisher: "European Commission — CORDIS"
    accessed: "2026-09-20"
  - title: "ENERSHARE — Il dataspace europeo sulla energia"
    url: "https://www.eng.it/en/insights/stories/research-projects/enershare-il-dataspace-europeo-sulla-energia"
    publisher: "Engineering — Ingegneria Informatica S.p.A. (project coordinator)"
    accessed: "2026-09-20"
  - title: "The emerging Common European Energy Data Space — state of play and next steps"
    url: "https://community.intnet.eu/events/35/the-emerging-common-european-energy-data-space---state-of-play-and-next-steps"
    publisher: "Int:net (Horizon Europe Coordination and Support Action)"
    accessed: "2026-09-20"
---

# Enershare

> **Created 2026-09-20**, partially closing `discovery/unresolved.md` row
> #132 alongside [[EU-OMEGA-X]] — see that entity for the full "six named
> projects" finding. Sourced from Enershare's own official CORDIS record
> and its coordinator's own page (`enershare.eu` itself returned HTTP 503
> on every attempt this pass and is not cited).
>
> **Domain added 2026-09-25**: [[DOMAIN-ENERGY]], created because
> "Energie" is one of the Dutch Cyberbeveiligingswet's own named sectors.

## Description

Enershare is a **Horizon Europe Innovation Action**, confirmed via its
official CORDIS record (Grant Agreement **101069831**): coordinated by
**Engineering — Ingegneria Informatica S.p.A.** (Italy), with **30
partners** across **Italy, Germany, Luxembourg, Greece, Spain, Portugal,
France, Slovenia, the Netherlands, Norway, Finland and Latvia**. Total
cost **€9,087,822.50**, EU contribution **€7,645,511.75**, running **1
July 2022 – 30 June 2025**.

CORDIS states its objective as developing **"a Reference Architecture for
a European Energy Data Space"**, combining cloud and digital security with
AI, and building technology enablers — trust connectors, blockchain-based
marketplaces, digital twins — across **7 pilots and 11 use cases**. The
coordinator's own page adds that the architecture is designed to comply
with **FIWARE, IDSA and GAIA-X standards**, with blockchain-based
marketplace infrastructure for compensated (monetary or non-monetary)
data exchange.

## One of six named CEEDS-supporting projects

See [[EU-OMEGA-X]] for the full finding: Int:net's own coordination-site
page names Enershare as one of five Horizon Europe Innovation Actions
(alongside DATA CELLAR, EDDIE, Omega-X and SYNERGIES) supporting CEEDS
deployment, plus Int:net itself as the sixth, a Coordination and Support
Action. **DATA CELLAR, EDDIE, SYNERGIES and Int:net remain unmodelled.**

## Not modelled

- **DATA CELLAR, EDDIE, SYNERGIES** and **Int:net**.
- The project's **7 pilots and 11 use cases** individually.
- Enershare's own **enershare.eu** site was never read directly this pass
  — it returned HTTP 503 on every attempt; CORDIS and the coordinator's
  own page substitute.

## Relationships

- `part-of` [[EU-CEEDS]] — `confidence: medium`.
- `based-on` [[EU-GAIA-X]] — `confidence: low`, a compliance statement
  rather than an architectural description.

## Sources

Listed in frontmatter, all three read directly.
