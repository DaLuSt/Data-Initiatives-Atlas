---
id: NL-SVB-BGT
type: organisation
name: Stichting Samenwerkingsverband Bronhouders BGT
alternative_names:
  - SVB-BGT
  - Samenwerkingsverband Bronhouders voor de BGT
description: >
  Dutch foundation (stichting) coordinating the seven categories of
  bronhouder (data-source holder) that jointly maintain the
  Basisregistratie Grootschalige Topografie: municipalities, water
  boards, provinces, the Ministry of Defence, the Ministry of
  Agriculture, Fisheries, Food Security and Nature, ProRail and
  Rijkswaterstaat. Its statutes were ratified on 15 April 2014 with all
  seven parties represented on the board, which has an independent
  chair. It coordinates quality, uniformity and completeness across the
  bronhouders and processes over 40,000 BGT mutations.

level: national
country: NL
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2014-04-15
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - NL-BGT
  - NL-RIJKSWATERSTAAT
  - NL
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. SVB-BGT is a foundation representing all seven bronhouder categories jointly, with no single sourced parent tier of government. Confirmed by reading svb-bgt.nl's own homepage directly (2026-09-06): 'Op 15 april 2014 is de oprichting van de definitieve Stichting met alle zeven partijen in het bestuur officieel met statuten bekrachtigd' (on 15 April 2014 the foundation's establishment, with all seven parties on the board, was formally ratified by statute)."
    confidence: high
    valid_from: 2014-04-15
    valid_until: null
  - type: participates-in
    target: NL-BGT
    source: fact
    evidence: "Confirmed by reading svb-bgt.nl's own homepage directly (2026-09-06): SVB-BGT coordinates the bronhouders who jointly maintain the BGT, 'bundelen de krachten van bronhouders' (combining the bronhouders' strength) to ensure quality, uniformity and completeness. Recorded at the same relationship type as the individual bronhouders' own participation (see [[NL-RIJKSWATERSTAAT]]), since SVB-BGT's role is coordinating that same joint maintenance rather than a distinct legal function."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Homepage"
    url: "https://www.svb-bgt.nl/homepage/"
    publisher: "SVB-BGT"
    accessed: "2026-09-06"
  - title: "Bestuursleden"
    url: "https://www.svb-bgt.nl/bestuursleden/"
    publisher: "SVB-BGT"
    accessed: "2026-09-06"
---

# Stichting Samenwerkingsverband Bronhouders BGT (SVB-BGT)

> **Created 2026-09-06**, closing part of a gap [[NL-BGT]]'s own entity
> flagged: "SVB-BGT — no entity; named in one source only." SVB-BGT's own
> site, read directly, gives its legal form, founding date, board
> composition and coordinating role in full.

## Description

Confirmed by reading svb-bgt.nl's own homepage directly: "Alle gemeenten,
waterschappen, provincies, het Ministerie van Defensie, het Ministerie
van Landbouw, Visserij, Voedselzekerheid en Natuur, ProRail en
Rijkswaterstaat werken samen aan de BGT" — all municipalities, water
boards, provinces, the Ministry of Defence, the Ministry of Agriculture,
Fisheries, Food Security and Nature, ProRail and Rijkswaterstaat work
together on the BGT, [[NL-BGT]]. SVB-BGT's own description of its role:
"Wij werken samen, bundelen de krachten van bronhouders" (we work
together, combining the bronhouders' strength), coordinating quality,
uniformity and completeness ("actualiteit, uniformiteit en volledigheid")
across more than 40,000 daily BGT mutations.

## Governance

Confirmed by reading svb-bgt.nl's own "Bestuursleden" page directly: "Het
bestuur van het SVB-BGT bestaat uit vertegenwoordigers van alle typen
bronhouders en heeft een onafhankelijke voorzitter" — the board consists
of representatives of every type of bronhouder and has an independent
chair. As read this pass, the board named a representative from the
Unie van Waterschappen (chair), Defensie (treasurer), RVO, Rijkswaterstaat
and IPO, with ProRail's and VNG's seats vacant at the time of reading —
a snapshot, not expected to remain current. "Het bestuur is
besluitvormend ten aanzien van de taken die nodig zijn richting het doel
van de stichting" — the board has decision-making authority over the
tasks needed to achieve the foundation's purpose, including policy plans
and the annual budget.

## Relationships

- `part-of` [[NL]] — anchor; represents all seven bronhouder categories
  jointly, with no single sourced parent.
- `participates-in` [[NL-BGT]] — coordinates the bronhouders' joint
  maintenance of the register; recorded at the same type as
  [[NL-RIJKSWATERSTAAT]]'s own bronhouder participation, distinct from
  [[NL-KADASTER]]'s `maintained-by` edge for the national facility.

## Not modelled

- The individual bronhouder categories beyond [[NL-RIJKSWATERSTAAT]]
  (already an Atlas entity): municipalities, water boards, provinces, the
  Ministry of Defence, the Ministry of Agriculture (LVVN), ProRail and
  RVO. See [[NL-BGT]]'s own "Not modelled" section.

## Sources

Listed in frontmatter, both read directly 2026-09-06.
