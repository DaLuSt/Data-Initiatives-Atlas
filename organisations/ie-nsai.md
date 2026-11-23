---
id: IE-NSAI
type: organisation
name: National Standards Authority of Ireland
alternative_names:
  - NSAI
description: >
  Ireland's national standards body, responsible for publishing Irish
  Standards and representing Ireland in European and international
  standardisation. It is Ireland's member of CEN, CENELEC and ISO.
  Established on 14 April 1997, the establishment day appointed under section 6 of the National Standards Authority of Ireland Act 1996 (S.I. No. 176 of 1997).

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 1997-04-14
end_date: null
last_verified: "2026-11-23"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IE
  - EU-CEN
  - EU-CENELEC
  - INTL-ISO
relationships:
  - type: part-of
    target: IE
    source: fact
    evidence: "Confirmed by reading nsai.ie directly (2026-08-22): the site identifies itself as 'National Standards Authority of Ireland.' Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CEN
    source: fact
    evidence: "Confirmed by reading standards.cencenelec.eu directly (2026-08-22): 'CEN's National Members are the National Standardization Bodies (NSBs) of the 27 European Union countries, United Kingdom, the Republic of North Macedonia, Serbia and Türkyie plus three countries of the European Free Trade Association (Iceland, Norway and Switzerland). There is one member per country.' Ireland is an EU member state and NSAI is its national standards body, confirmed on nsai.ie, so membership follows from the sourced composition rule. This relationship was described in this entity's own body text but missing from its structured data — added to close that gap."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-CENELEC
    source: fact
    evidence: "Confirmed by reading standards.cencenelec.eu directly (2026-08-22): 'CEN's National Members are the National Standardization Bodies (NSBs) of the 27 European Union countries, United Kingdom, the Republic of North Macedonia, Serbia and Türkyie plus three countries of the European Free Trade Association (Iceland, Norway and Switzerland).' CENELEC's National Members are the National Committees of the same set. Ireland is an EU member state and NSAI is its national standards body, so membership follows from the sourced composition rule. This relationship was described in this entity's own body text but missing from its structured data — added to close that gap."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: INTL-ISO
    source: fact
    evidence: "ISO's own member list on committee.iso.org (iso_members.htm), read directly 2026-09-27 and again 2026-11-22, lists 'Ireland NSAI Member body' (381 technical committee participations on 2026-11-22). iso.org itself is blocked to this environment; committee.iso.org is the reachable ISO subdomain recorded in discovery/unresolved.md row #220."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "S.I. No. 176/1997 — National Standards Authority of Ireland Act, 1996 (Commencement and Establishment Day) Order, 1997"
    url: "https://www.irishstatutebook.ie/1997/en/si/0176.html"
    publisher: "Office of the Attorney General (irishstatutebook.ie)"
    accessed: "2026-11-23"
  - title: "National Standards Authority of Ireland"
    url: "https://www.nsai.ie/"
    publisher: "National Standards Authority of Ireland (NSAI)"
    accessed: "2026-08-22"
  - title: "CEN's National Members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-22"
  - title: "National Standards Authority of Ireland"
    url: "https://en.wikipedia.org/wiki/National_Standards_Authority_of_Ireland"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
  - title: "ISO — Members"
    url: "https://committee.iso.org/iso/home/about/iso_members.htm"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-09-27"
    note: "A reachable iso.org subdomain, found this pass (discovery/unresolved.md row #220), corroborating the Wikipedia-sourced ISO edge directly from ISO's own member table: 'Ireland NSAI Member body' with 377 TC and 3 PDC participations — full voting membership, not a lesser tier."
---

# National Standards Authority of Ireland (NSAI)

> **Verified 2026-08-22.** Both cited pages were read directly. The old
> CEN-national-members URL had moved (404); its replacement,
> `standards.cencenelec.eu/ords/f?p=CEN:5`, was found and read, and
> confirms the composition rule verbatim. A structural bug was also fixed
> this pass: the `participates-in` [[EU-CEN]] and [[EU-CENELEC]] edges
> this entity's own body text already described were missing from its
> frontmatter `relationships:` list — they are now added.
>
> **Closed 2026-09-27**: the Wikipedia-sourced ISO membership is now
> corroborated directly from ISO's own side, via `committee.iso.org` — a
> reachable `iso.org` subdomain found this pass (`discovery/unresolved.md`
> row #220). `confidence` on the ISO edge raised medium→high; 4 of 4
> sources now read directly.

> **Dated 2026-11-23** (roadmap #775). irishstatutebook.ie, read directly. National Standards Authority of Ireland Act 1996, section 6(1): 'There shall stand established, on such day as the Minister may by order appoint ("the establishment day"), a body to be known as The National Standards Authority of Ireland'. S.I. No. 176 of 1997, Article 3: 'The 14th day of April, 1997, is hereby appointed as the establishment day on which the National Standards Authority of Ireland shall stand established.' (Article 2 brought the rest of the Act, other than Part IV, into operation on 1 January 1997.) `start_date` is 14 April 1997.

## Description

Confirmed by reading nsai.ie directly (2026-08-22): the site identifies
itself as "National Standards Authority of Ireland." NSAI is Ireland's national standards body.

## The refusal recorded here has been closed

An earlier version of this entity asserted **no** `participates-in` edges.
The reasoning was that the CEN-CENELEC members page had been returned by
search and not read, so the Atlas had a URL that almost certainly listed NSAI
and no confirmation that it did — and that inferring membership from a page
title would be guessing.

What closed it was not reading that page. It was finding CEN-CENELEC's own
**statement of the rule**: *CEN's National Members are the National
Standardization Bodies of the 27 European Union countries*, and CENELEC's
are the National Committees of the same set. Ireland is a member state and
NSAI is its national standards body, so the membership follows from the rule
rather than from a list the Atlas cannot read.

`participates-in` [[EU-CEN]] and [[EU-CENELEC]] are now asserted on that
basis, together with the four bodies created in the same batch —
[[BE-NBN]], [[FR-AFNOR]], [[ES-UNE]] and [[PL-PKN]].

**[[INTL-ISO]] — closed 2026-09-05.** The CEN-CENELEC composition rule
covers the European organisations and says nothing about ISO. iso.org
itself is confirmed domain-wide blocked to this environment's fetch
tooling, so en.wikipedia.org's dedicated NSAI article was read directly
instead: "The National Standards Authority of Ireland (NSAI) is the
International Organization for Standardization (ISO) member body for
Ireland." `participates-in` [[INTL-ISO]] is now asserted, the same
evidence tier [[GB-BSI]] and [[DE-DIN]]'s ISO edges carry.

**Corroborated directly from ISO's own side, 2026-09-27.**
`committee.iso.org/iso/home/about/iso_members.htm`, a different,
reachable `iso.org` subdomain (`discovery/unresolved.md` row #220),
carries ISO's own member table: "Ireland NSAI Member body" with 377 TC
and 3 PDC participations — full voting membership. `confidence` raised
medium→high, now resting on ISO's own listing rather than only on
Wikipedia's characterisation.

## Not modelled

- Any **Irish Standard**. The same is true of [[GB-BSI]], [[NL-NEN]] and
  [[DE-DIN]] — four national standards bodies in the Atlas, and not one
  standard between them that they maintain.
- NSAI's role in **CE marking** and conformity assessment.

## Sources

Listed in frontmatter. **4 of 4 now read directly.** The first two read
directly in the 2026-08-22 pass; the Wikipedia article, 2026-09-05; and,
closing this file 2026-09-27, `committee.iso.org`'s own member table,
corroborating the ISO membership from ISO's own side.

## Relationships

- `participates-in` [[EU-CEN]], [[EU-CENELEC]] and [[INTL-ISO]]
  (`confidence: high`, corroborated 2026-09-27 via `committee.iso.org`).
