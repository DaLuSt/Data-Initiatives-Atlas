---
id: NL-SURF
type: organisation
name: SURF
alternative_names:
  - Coöperatie SURF
  - Samenwerkende Universitaire RekenFaciliteiten
description: >
  Dutch ICT cooperative of education and research institutions. Founded in
  1986, SURF is owned by its members — more than 100 universities,
  universities of applied sciences, vocational institutions, university
  medical centres and research institutes — and realises national ICT
  facilities for education and research.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 1986-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - NL
  - EU-GEANT
relationships:
  - type: related-to
    target: NL
    source: fact
    evidence: "SURF is the Dutch ICT cooperative of education and research institutions, founded in 1986 and owned by its members — more than 100 universities, universities of applied sciences, vocational institutions, university medical centres and research institutes (surf.nl). NOT READ — search-only. `related-to` and not `part-of`: SURF is member-owned, not a body of the Dutch state, so structural containment is not claimed. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-GEANT
    source: fact
    evidence: "The GÉANT Association comprises 37 national research and education networks plus NORDUnet; GÉANT provides the pan-European backbone and coordinates shared services while each NREN delivers those capabilities at national level, and the NRENs are not-for-profit and mainly publicly funded (about.geant.org/nrens; geant.org 'National Research and Education Networks'). NOT READ — search-only. Membership follows from the sourced composition rule rather than from a source naming SURF."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SURF is de ict-coöperatie van onderwijs en onderzoek"
    url: "https://www.surf.nl/en"
    publisher: "SURF"
  - title: "SURF Strategie 2022–2027"
    url: "https://www.surf.nl/files/2022-03/surf-strategie-2022-2027-pv4-nl_0_1.pdf"
    publisher: "SURF"
  - title: "SURF"
    url: "https://nl.wikipedia.org/wiki/SURF"
    publisher: "Wikipedia"
---

# SURF

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

SURF is the ICT cooperative of Dutch education and research. It is a
cooperative association whose members — reported as more than 100
institutions, including universities, universities of applied sciences,
vocational institutions, university medical centres and research institutes
— are also its owners.

Its principal task is to let education and research make the best use of
what ICT offers, which it does by exploring new technologies and then
realising national ICT facilities. Its role therefore spans research
infrastructure, research data and the digital foundations of the education
and research sector.

The organisation was founded in 1986; the name originally stood for
Samenwerkende Universitaire RekenFaciliteiten. The `start_date` records that
founding year, though the precise date was not established and the
organisation has been restructured since (the present form is a
coöperatie).

## Relationships

SURF spans both research and education, and is now tagged
[[DOMAIN-RESEARCH]] and [[DOMAIN-EDUCATION]]. The latter was withheld in
Batch 2 because it would have connected this entity alone; it was created
in Batch 5 once [[NL-ROSA]] brought it to the two-entity threshold.

Beyond that, SURF's most significant Atlas relationships are likely to
be to research data infrastructure and European research-data initiatives
(EOSC and related, Batch 10), and to national research-data bodies such as
DANS and Health-RI, none of which are yet entities. Queued in
`discovery/research-queue.md`.

## Sources

Listed in frontmatter.
