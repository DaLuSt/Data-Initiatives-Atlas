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
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
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
    evidence: "The National Standards Authority of Ireland is Ireland's national standards body (nsai.ie). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Standards Authority of Ireland"
    url: "https://www.nsai.ie/"
    publisher: "National Standards Authority of Ireland (NSAI)"
  - title: "CEN Members"
    url: "https://www.cencenelec.eu/about-cen/cen-national-members/"
    publisher: "CEN-CENELEC"
---

# National Standards Authority of Ireland (NSAI)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

NSAI is Ireland's national standards body.

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

Listed in frontmatter.

## Relationships

- `participates-in` [[EU-CEN]] and [[EU-CENELEC]].
