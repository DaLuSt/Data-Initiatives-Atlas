---
id: INTL-IETF
type: organisation
name: Internet Engineering Task Force
alternative_names:
  - IETF
description: >
  International standards organisation for internet protocols, operating on
  direct membership rather than national delegation, and **not** a UN body.

level: international
country: null
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-ISOC
  - INTL-W3C
relationships:
  - type: part-of
    target: INTL-ISOC
    source: fact
    evidence: "The IETF Administration LLC provides the corporate legal home for the IETF, the Internet Architecture Board and the Internet Research Task Force, and the IETF LLC is a single-member disregarded entity of the Internet Society, operating as a branch or division of ISOC; under an operating agreement ISOC provides significant funding support to the IETF, and one member of the IETF LLC board is appointed by ISOC's Board of Trustees (datatracker.ietf.org draft-ietf-iasa2-rfc2031bis-08 'The IETF-ISOC Relationship'; ietf.org/administration/overview; ietf.org/blog/isoc-financial-commitment). NOT READ — search-only. The IETF LLC is not modelled, so this edge simplifies IETF → IETF LLC → ISOC to IETF → ISOC; see INTL-ISOC. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Standards overview: the global digital standardisation ecosystem"
    url: "https://epc.ac.uk/toolkit/standards-overview-the-global-digital-standardisation-ecosystem/"
    publisher: "Engineering Professors Council"
---

# IETF (Internet Engineering Task Force)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited page was confirmed to exist but was not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The IETF is the standards organisation for internet protocols. Like
[[INTL-W3C]] and unlike [[INTL-ISO]], [[INTL-IEC]] and [[UN-ITU]], it is a
**direct-membership** organisation rather than one based on national
delegation.

`INTL` scope, not `UN`.

## ⚠ Thinnest entity in this batch

`confidence: low`, `coverage: low`, and a single source — an academic
toolkit page that names the IETF in a list of eight standards development
organisations. **No ietf.org source was located**, and no IETF standard is
modelled.

The IETF is named in Batch 13's scope, which is why it exists here. But it
carries almost no information beyond its category, and a reader should treat
it as a placeholder. The honest alternative was to omit it and queue it;
including it with the weakness marked follows the precedent set by
[[NL-PETRA]] and [[UN-DATA-COMMONS]].

Note that internet protocol standards do underpin parts of the Dutch layer —
[[NL-PAS-TOE-OF-LEG-UIT]] mandates HTTPS, DNSSEC and mail-security standards
that originate in IETF RFCs — so a properly researched IETF entity would
connect to real content. That connection is queued, not asserted.

## Relationships

- Peer direct-membership standards body to [[INTL-W3C]].

## Sources

Listed in frontmatter — one, and indirect.

## `part-of` [[INTL-ISOC]]

Added under the rule that every entity must reach its scope anchor. The IETF
was the hardest case in the repository: it belongs to no country, is not
part of the European Union or the United Nations, and the Atlas has no
`INTL` anchor to fall back on.

Rather than attach it somewhere convenient, the edge points at its **actual**
parent. The **IETF Administration LLC** is the corporate legal home of the
IETF, the IAB and the IRTF, and is a *single-member disregarded entity* of
the Internet Society — a branch of ISOC for tax purposes. ISOC funds the
IETF under an operating agreement and appoints one member of the LLC's
board.

The LLC itself is **not modelled**, so this edge collapses
`IETF → IETF LLC → ISOC` into one hop. That simplification is stated here
and on [[INTL-ISOC]] rather than left for a reader to discover.
