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
  facilities for education and research. Legally, Coöperatie SURF U.A.
  wholly owns a subsidiary, SURF B.V., through which most services are
  delivered.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading surf.nl/en directly (2026-08-27): SURF describes itself as 'the collaborative organisation for IT in Dutch education and research', with '33 Communities' and '8500+ Members' across MBO, HBO and WO institutions. nl.wikipedia.org's SURF article, also read directly, confirms the 1986 founding by astrophysicist Hans Rosenberg of Utrecht University and the cooperative-association ('coöperatieve vereniging') structure. `related-to` and not `part-of`: SURF is member-owned, not a body of the Dutch state, so structural containment is not claimed. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-GEANT
    source: fact
    evidence: "Upgraded this pass (2026-08-27) from a composition-rule inference to a directly-sourced fact: about.geant.org's membership listing (retrieved via search after a direct WebFetch to the page was blocked with HTTP 403) names SURF explicitly as 'a National Member of GÉANT', with Ron Augustus as its General Assembly Representative and Floor Jas as substitute. The GÉANT Association comprises 37 NRENs plus NORDUnet; each NREN is not-for-profit and mainly publicly funded, and SURF is confirmed as the Dutch NREN."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "SURF is de ict-coöperatie van onderwijs en onderzoek"
    url: "https://www.surf.nl/en"
    publisher: "SURF"
    accessed: "2026-08-27"
  - title: "SURF Strategie 2022–2027"
    url: "https://www.surf.nl/files/2022-03/surf-strategie-2022-2027-pv4-nl_0_1.pdf"
    publisher: "SURF"
  - title: "SURF"
    url: "https://nl.wikipedia.org/wiki/SURF"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# SURF

> **Verified 2026-08-27.** Two of three cited pages were read directly this
> pass, closing the previous `search-only` status (never previously
> `last_verified`). The strategy PDF was not re-fetched. The GÉANT
> relationship, previously an unconfirmed composition-rule inference, is
> now directly sourced.

## Description

SURF is the ICT cooperative of Dutch education and research. Reading
nl.wikipedia.org's own article directly identifies its **founder** —
astrophysicist **Hans Rosenberg** of Utrecht University — and confirms it
operates as a **coöperatieve vereniging** (cooperative association) whose
member institutions collectively own it and decide together which projects
to pursue. A separate search of SURF's own annual reports confirms the
current legal form precisely as **Coöperatie SURF U.A.**, which wholly owns
and manages a subsidiary company, **SURF B.V.**, through which most
services are delivered — a structural detail not previously recorded here.

Its principal task, per surf.nl's own page, is to let education and
research make the best use of ICT, spanning **33 communities** and
**8,500+ members** across vocational (MBO), higher professional (HBO) and
university (WO) education. Reading the Wikipedia article directly also adds
a structural history point not previously recorded: until **1 January
2021**, SURF comprised three specialised divisions — SURFnet, SURFmarket
and SURFsara — which were legally merged into the single organisation on
that date.

The organisation was founded in 1986; the name originally stood for
Samenwerkende Universitaire RekenFaciliteiten. `start_date` remains `null`:
no source read gives a specific founding day, only the year.

## GÉANT membership, now confirmed directly

Previously recorded only via the sourced composition rule ("GÉANT has 37
NRENs, SURF is presumably the Dutch one"). A search of GÉANT's own
membership listing, retrieved after a direct fetch of the page returned
HTTP 403, names **SURF explicitly** as the Dutch National Member, with
named General Assembly representatives. This closes a genuine gap: SURF is
now the only entity in this batch where a composition-rule inference was
upgraded to a fact by finding the composing body's own membership list.

## Relationships

SURF spans both research and education, tagged [[DOMAIN-RESEARCH]] and
[[DOMAIN-EDUCATION]].

Beyond that, SURF's most significant Atlas relationships are likely to be
to research data infrastructure and European research-data initiatives
(EOSC and related), and to national research-data bodies such as DANS and
Health-RI, none of which are yet entities. Queued in
`discovery/research-queue.md`.

## Sources

Two of three read directly this pass: `surf.nl/en` and the Dutch Wikipedia
article. The 2022–2027 strategy PDF was not re-fetched. The GÉANT
membership confirmation came via a WebSearch of `about.geant.org` content
after a direct fetch of that page was blocked (403).
