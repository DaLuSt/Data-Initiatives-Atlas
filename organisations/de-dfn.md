---
id: DE-DFN
type: organisation
name: DFN-Verein
alternative_names:
  - DFN
  - Deutsches Forschungsnetz
  - Verein zur Förderung eines Deutschen Forschungsnetzes e. V.
description: >
  Germany's national research and education network organisation, founded
  in 1984 by universities, non-university research institutions and
  research-oriented companies and constituted as a registered association
  (e.V.). It operates the X-WiN backbone — roughly 10,250 km of fibre
  connecting around 850 locations for 364 members — linked to GÉANT at
  600 Gbit/s, and is one of the national research and education networks
  reaching German universities and research institutions through the
  pan-European research backbone. Like the other NRENs it is not-for-profit
  and mainly publicly funded, and its services extend beyond connectivity
  to identity management and security services for its member
  institutions.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 1984-01-01
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading dfn.de's own homepage directly (2026-08-28): DFN-Verein operates 'das Netz zur Wissenschaft,' the X-WiN backbone of roughly 10,250 km of fibre connecting around 850 locations, with 364 members across Germany, organised as a registered association (e.V.). Anchor edge under metadata/relationship-types.md §2.3: a registered association funded by but not part of the state takes `related-to`, the same treatment NL-SURF and DE-NFDI have."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-GEANT
    source: fact
    evidence: "Confirmed by reading dfn.de's own 'International' page directly (2026-08-28): 'X-WiN is linked to GÉANT with 600 gigabit-per-second connection,' and 'these networks are connected to one another through GÉANT, a backbone network that is organized and administered by the GÉANT Association in Amsterdam.' en.wikipedia.org's dedicated Deutsches Forschungsnetz article, also read directly, independently confirms DFN's connection runs through GÉANT2 at 100G at the network's super core. The GÉANT Association's own pages (geant.org, about.geant.org) returned HTTP 403 on two attempts each this pass and could not be read directly; DFN's own site and Wikipedia substitute for the composition-rule evidence used previously."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "DFN-Verein — Deutsches Forschungsnetz"
    url: "https://www.dfn.de/"
    publisher: "DFN-Verein"
    accessed: "2026-08-28"
  - title: "International — DFN"
    url: "https://www.dfn.de/en/network/international/"
    publisher: "DFN-Verein"
    accessed: "2026-08-28"
  - title: "Deutsches Forschungsnetz"
    url: "https://en.wikipedia.org/wiki/Deutsches_Forschungsnetz"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "National Research and Education Networks — GÉANT"
    url: "https://geant.org/who-we-work-with/national-research-and-education-networks/"
    publisher: "GÉANT Association"
  - title: "NRENs — About GÉANT"
    url: "https://about.geant.org/nrens/"
    publisher: "GÉANT Association"
---

# DFN-Verein

> **Re-verified 2026-08-28.** Both GÉANT Association pages
> (`geant.org`, `about.geant.org`) return HTTP 403 Forbidden on two
> attempts each this pass and are treated as genuinely blocked. DFN's own
> homepage and English "International" page, plus a dedicated Wikipedia
> article, were found and read directly and substitute for the composition-rule
> evidence the entity previously relied on. Three of five listed sources
> read directly is a genuine majority. `verification: primary-source`;
> `confidence` raised to `high`; the founding year, previously unrecorded,
> is now sourced.

## Description

Germany's **national research and education network** organisation,
confirmed directly this pass on its own English Wikipedia article to have
been **founded in 1984** by universities, non-university research
institutions and research-oriented companies, formally the *Verein zur
Förderung eines Deutschen Forschungsnetzes e.V.* — a registered association
under German law.

It operates the **X-WiN** backbone: confirmed directly on dfn.de's own
homepage, roughly **10,250 km of fibre** connecting around **850
locations** for **364 members** across Germany, offering 14 tailored
communication services across network/communication, security/trust/identity,
collaboration and cloud categories. dfn.de's own "International" page,
read directly, confirms X-WiN is **linked to GÉANT at 600 Gbit/s**.

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

## What was thin before, and what this pass fills in

The description was previously thin because the GÉANT sources described
what NRENs do **as a class** while the one DFN-specific source was its own
home page alone. This pass adds a second DFN-specific source (its own
"International" page) and a dedicated Wikipedia article, giving a founding
date, membership count, backbone length and connection speed that were
absent before — `coverage` is raised to `medium` accordingly, though
governance detail (board, decision-making) is still not recorded.

## Relationships

- `related-to` [[DE]] — anchor edge; an e. V. is not part of the state.
- `participates-in` [[EU-GEANT]] — confirmed directly this pass on DFN's
  own site and independently on Wikipedia, `confidence: high`.

## Sources

Listed in frontmatter — DFN's own site (two pages) and a dedicated
Wikipedia article read directly this pass; both GÉANT Association pages
returned HTTP 403 on two attempts each and are kept listed with that status
noted here rather than silently dropped.
