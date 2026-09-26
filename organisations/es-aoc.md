---
id: ES-AOC
type: organisation
name: Consorci Administració Oberta de Catalunya
alternative_names:
  - AOC Consortium
  - Consorci AOC
  - Open Administration of Catalonia
description: >
  Catalan public-sector consortium for digital-administration
  interoperability, created following the "Pact for the promotion and
  development of the Information Society in Catalan public
  administrations" signed in the Parliament of Catalonia on 23 July
  2001 by the parliamentary group presidents, the Generalitat de
  Catalunya and local governments represented by Localret, with the
  consortium's creation and statutes finally approved by Resolution
  PRE/606/2002 of 27 March 2002. Law 29/2010, of 3 August, on the use
  of electronic media in the Catalan public sector, assigns the AOC
  Consortium responsibility for promoting the interoperability of
  Catalan information systems with other administrations and for
  creating and providing common e-government services, including the
  Via Oberta interoperable-data-exchange service.

level: subnational
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2002-03-27
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-MADRID-DIGITAL
  - ES-LOCALRET
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Confirmed by reading aoc.cat's own 'What is AOC' page directly (2026-09-20): the consortium originates in the Pact signed in the Parliament of Catalonia on 23 July 2001 between parliamentary group presidents, the Generalitat de Catalunya and local governments represented by Localret, with the consortium's creation and statutes formally approved by Resolution PRE/606/2002 of 27 March 2002. The same page states Llei 29/2010, de 3 d'agost (Law 29/2010 of 3 August) on the use of electronic media in the Catalan public sector, assigns the Consortium responsibility for promoting interoperability of Catalan information systems and creating common e-government services, quoting the law directly: 'Promote the interoperability of Catalan information systems with other administrations.' Anchor edge under metadata/relationship-types.md §2.3, asserting Catalan sub-federal scope via `level: subnational` — the same treatment given to Belgium's regional digital agencies. A public inter-administrative consortium (Generalitat + local government association) is closer in shape to a state body than a private association, matching the anchor-edge rule's `part-of` test."
    confidence: medium
    valid_from: 2002-03-27
    valid_until: null

sources:
  - title: "What is AOC — AOC Consortium"
    url: "https://www.aoc.cat/en/consorci-aoc/"
    publisher: "Consorci AOC"
    accessed: "2026-09-20"
  - title: "Què és el Consorci AOC — OLD"
    url: "https://www.aoc.cat/en/que-es-el-consorci-aoc-old/"
    publisher: "Consorci AOC"
    accessed: "2026-09-20"
---

# Consorci Administració Oberta de Catalunya (AOC)

> **Created 2026-09-20**, closing part of `discovery/unresolved.md` item
> #5 — Spain's own sub-national digital-government bodies, unmodelled
> even after `level: subnational` was added to the schema for Belgium's
> equivalents on 2026-08-21. Sourced from AOC's own site, read directly.

## Description

The AOC Consortium promotes digital transformation and, specifically,
**interoperability** among Catalan public administrations. It originates
in a **Pact signed in the Parliament of Catalonia on 23 July 2001**
between the parliamentary group presidents, the **Generalitat de
Catalunya** and local governments represented by **Localret**, with its
creation and statutes formally approved by **Resolution PRE/606/2002 of
27 March 2002**.

## The interoperability mandate, from the law itself

Confirmed directly on AOC's own page: **Llei 29/2010** (Law 29/2010 of 3
August), on the use of electronic media in the Catalan public sector,
assigns the Consortium responsibility to *"promote the interoperability
of Catalan information systems with other administrations"* and to
create and provide common e-government services. Its flagship
interoperability service, **Via Oberta**, lets administrations exchange
data electronically rather than requiring citizens to supply documents
already held by another public body.

## An inter-administrative consortium, not a single-government agency

Unlike [[BE-DIGITAAL-VLAANDEREN]] (a Flemish government agency) or
[[DE-AKDB]] (owned by Bavaria's municipal associations), the AOC
Consortium was created jointly by the Catalan regional government and a
local-government association (Localret) together — a genuinely
inter-administrative public body. It is nonetheless recorded `part-of`
[[ES]] rather than `related-to`, matching the anchor-edge rule's test for
a public body rather than a private association: both its founding
parties are public administrations, and its statutory mandate under Law
29/2010 is a public-sector function.

## Not modelled

**Localret, researched 2026-09-26**: now its own entity, [[ES-LOCALRET]]
(a consortium of Catalan municipalities founded 1997), carrying its own
`participates-in` edge back to this entity.

- The **Via Oberta** service and AOC's other named e-government
  platforms (eNOTUM, eTRAM, e-FACT) individually.
- **The 2025 statutory reform (Agreement GOV/160/2025), checked
  2026-09-26**: aoc.cat's own statutes listing, read directly, describes
  it as "authorizing the modification of articles 7 and 11.1 of the
  Statutes of the Open Administration Consortium of Catalonia and
  determining the designation of the represent members of the
  Generalitat Administration and the independent members" — a governance
  procedure amendment (board designation process), not a change to the
  consortium's name, founding date or core membership. Deliberately not
  modelled as a separate fact or relationship: it does not affect
  anything else in this entity's frontmatter.
- Any relationship to [[ES-MADRID-DIGITAL]] (Madrid's own regional IT
  agency, added 2026-09-20) — no source connects them; recorded for
  navigation only, as siblings under `discovery/unresolved.md` item #5.

## Relationships

- `part-of` [[ES]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
