---
id: DE-DFN
type: organisation
name: DFN-Verein
alternative_names:
  - DFN
  - Deutsches Forschungsnetz
  - Verein zur Förderung eines Deutschen Forschungsnetzes e. V.
description: >
  Germany's national research and education network organisation, constituted
  as a registered association. It is one of the 37 national research and
  education networks in the GÉANT Association, through which the pan-European
  research backbone reaches German universities and research institutions.
  Like the other NRENs it is not-for-profit and mainly publicly funded, and
  its services extend beyond connectivity to identity management and
  security services for its member institutions.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - DE
  - EU-GEANT
  - DE-NFDI
  - NL-SURF
relationships:
  - type: related-to
    target: DE
    source: fact
    evidence: "DFN-Verein operates the German national research and education network; the NRENs are not-for-profit and mainly publicly funded and provide dedicated high-speed connectivity and value-added services for their knowledge institutions (dfn.de; geant.org 'National Research and Education Networks'; about.geant.org/nrens). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: a registered association (e. V.) funded by but not part of the state takes `related-to`, the same treatment NL-SURF and DE-NFDI have."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-GEANT
    source: fact
    evidence: "The GÉANT Association comprises 37 NRENs plus NORDUnet and associates; GÉANT provides the pan-European backbone and coordinates shared services while each NREN delivers those capabilities at national level (about.geant.org/nrens; geant.org 'National Research and Education Networks'). NOT READ — search-only. Membership follows from the sourced composition rule — the national research and education networks of Europe — rather than from a source naming DFN-Verein, the same basis on which the national standardisation bodies were attached to EU-CEN."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "DFN-Verein — Deutsches Forschungsnetz"
    url: "https://www.dfn.de/"
    publisher: "DFN-Verein"
  - title: "National Research and Education Networks — GÉANT"
    url: "https://geant.org/who-we-work-with/national-research-and-education-networks/"
    publisher: "GÉANT Association"
  - title: "NRENs — About GÉANT"
    url: "https://about.geant.org/nrens/"
    publisher: "GÉANT Association"
---

# DFN-Verein

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Germany's **national research and education network** organisation, a
registered association and one of the 37 NRENs in [[EU-GEANT]].

## The second country in `DOMAIN-EDUCATION`

Before 2026-08-21 the education domain reached exactly one country — the
Netherlands, through [[NL-SURF]] and [[NL-ROSA]] — which
`discovery/candidates.md` recorded alongside health and research as the
Atlas's thinnest coverage.

DFN-Verein and [[NL-SURF]] are the same kind of body doing the same job in
two countries, which is the comparison the domain existed to make possible
and could not.

## Germany now has two research-data bodies and they are not the same thing

| | [[DE-DFN]] | [[DE-NFDI]] |
|---|---|---|
| What it is | the **network** | the **data infrastructure** |
| Delivers | connectivity, identity, security | standards, services, RDM coordination |
| Attaches to | [[EU-GEANT]] | [[EU-EOSC]] |
| Legal form | registered association | registered association |

Two European layers, two national bodies, no overlap. That is a genuine
finding rather than a modelling artefact: the Netherlands collapses both roles
into [[NL-SURF]], and Germany does not.

## What is `coverage: low` here

The description above is thin, and deliberately so. The GÉANT sources describe
what NRENs do **as a class**; the one DFN-specific source is its own home
page. Nothing here rests on a source about DFN's own history, governance,
network or services — so no founding date, no network name, no service list.

The `participates-in` edge rests on the same class-level rule, and its
evidence string says so.

## Relationships

- `related-to` [[DE]] — anchor edge; an e. V. is not part of the state.
- `participates-in` [[EU-GEANT]], on the sourced composition rule.

## Sources

Listed in frontmatter — DFN's own site and two GÉANT pages on the NREN
relationship.
