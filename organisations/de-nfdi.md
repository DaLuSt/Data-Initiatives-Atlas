---
id: DE-NFDI
type: organisation
name: Nationale Forschungsdateninfrastruktur e.V.
alternative_names:
  - NFDI
  - National Research Data Infrastructure (Germany)
description: >
  German national research data infrastructure, coordinated by the non-profit
  association NFDI e.V. It is a federation of 26 funded discipline-specific
  consortia plus the Base4NFDI shared services, funded jointly by the federal
  government and the Länder through the Deutsche Forschungsgemeinschaft. It
  coordinates the development of research data infrastructures and services
  and the standardisation of research data management in Germany, with the
  stated mission of making research data findable, accessible, interoperable
  and reusable across disciplines. NFDI e.V. is a member of the EOSC
  Association.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
organisations: []
related_entities:
  - DE
  - EU-EOSC
  - NL-SURF
relationships:
  - type: related-to
    target: DE
    source: fact
    evidence: "The NFDI is a long-term project funded by the federal government and the German states; it is a federation of 26 funded discipline-specific consortia plus Base4NFDI shared services, coordinated by the non-profit association NFDI e.V., and funded jointly by federal and state governments through the Deutsche Forschungsgemeinschaft (nfdi.de; nfdi.de/association; dfg.de 'National Research Data Infrastructure'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: a registered association (e.V.) funded by but not part of the state takes `related-to`, the same treatment NL-SURF and NL-NICTIZ have."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EOSC
    source: fact
    evidence: "Nationale Forschungsdateninfrastruktur (NFDI) e.V. is listed as a member of the EOSC Association (eosc.eu/members/nationale-forschungsdateninfrastruktur-nfdi-ev). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "NFDI — Nationale Forschungsdateninfrastruktur e.V."
    url: "https://www.nfdi.de/?lang=en"
    publisher: "Nationale Forschungsdateninfrastruktur e.V."
  - title: "Association | NFDI"
    url: "https://www.nfdi.de/association/?lang=en"
    publisher: "Nationale Forschungsdateninfrastruktur e.V."
  - title: "National Research Data Infrastructure"
    url: "https://www.dfg.de/en/research-funding/funding-initiative/nfdi"
    publisher: "Deutsche Forschungsgemeinschaft (DFG)"
  - title: "Nationale Forschungsdateninfrastruktur (NFDI) e.V. — EOSC Association member"
    url: "https://eosc.eu/members/nationale-forschungsdateninfrastruktur-nfdi-ev"
    publisher: "EOSC Association"
---

# NFDI — Nationale Forschungsdateninfrastruktur

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Germany's national research data infrastructure: a federation of **26 funded
discipline-specific consortia** plus the **Base4NFDI** shared services,
coordinated by the non-profit association **NFDI e.V.** and funded jointly by
the federal government and the Länder through the **DFG**.

Its mission is stated in FAIR terms — research data findable, accessible,
interoperable and reusable across disciplines.

## The second country in `DOMAIN-RESEARCH`

Before 2026-08-21 the domain reached **one** country: the Netherlands, through
[[NL-TNO]] and [[NL-SURF]]. That was true in an Atlas that holds
[[EU-EOSC]], the European Open Science Cloud.

NFDI closes it at the level that matters, because the connection is
**sourced**: NFDI e.V. is a listed **member of the EOSC Association**, so the
Atlas can draw a national research data infrastructure attaching to the
European one rather than merely sitting beside it.

## Why `related-to` and not `part-of`

NFDI is an **e.V.** — a registered association — funded by the state but not
part of it. `metadata/relationship-types.md` §2.3 is explicit that a national
body which is not part of the state takes `related-to`, and names
[[NL-SURF]] and [[NL-NICTIZ]] as the precedent. NFDI is the same shape as
SURF: a member-driven body carrying national infrastructure.

## The federal structure is visible and not modelled

26 consortia, funded jointly by the **Bund and the Länder**. Neither the
consortia nor the Länder funding arrangement has an entity. The Länder half is
the interesting one: `level: subnational` was added in this same batch, so the
vocabulary now exists to model German Länder — and nothing in this entity
does, because no source here names them individually.

## Relationships

- `related-to` [[DE]] — anchor edge.
- `participates-in` [[EU-EOSC]] — sourced membership of the EOSC Association.

## Sources

Listed in frontmatter — NFDI's own site and association page, the DFG funding
page, and the EOSC Association's member record.
