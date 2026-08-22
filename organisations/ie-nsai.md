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

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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

sources:
  - title: "National Standards Authority of Ireland"
    url: "https://www.nsai.ie/"
    publisher: "National Standards Authority of Ireland (NSAI)"
    accessed: "2026-08-22"
  - title: "CEN's National Members"
    url: "https://standards.cencenelec.eu/ords/f?p=CEN:5"
    publisher: "CEN-CENELEC"
    accessed: "2026-08-22"
---

# National Standards Authority of Ireland (NSAI)

> **Verified 2026-08-22.** Both cited pages were read directly. The old
> CEN-national-members URL had moved (404); its replacement,
> `standards.cencenelec.eu/ords/f?p=CEN:5`, was found and read, and
> confirms the composition rule verbatim. A structural bug was also fixed
> this pass: the `participates-in` [[EU-CEN]] and [[EU-CENELEC]] edges
> this entity's own body text already described were missing from its
> frontmatter `relationships:` list — they are now added.

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

**[[INTL-ISO]] is still not asserted.** The rule covers the European
organisations and says nothing about ISO. [[GB-BSI]] and [[DE-DIN]] carry
ISO edges because their own sources state it; NSAI's do not.

## Not modelled

- Any **Irish Standard**. The same is true of [[GB-BSI]], [[NL-NEN]] and
  [[DE-DIN]] — four national standards bodies in the Atlas, and not one
  standard between them that they maintain.
- NSAI's role in **CE marking** and conformity assessment.

## Sources

Listed in frontmatter, both read directly this pass.

## Relationships

- `participates-in` [[EU-CEN]] and [[EU-CENELEC]] — now present in the
  structured data as well as this prose.
