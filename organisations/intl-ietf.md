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
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading all three cited pages directly (2026-08-28): ietf.org/administration/overview states 'The IETF Administration LLC (IETF LLC) provides the corporate legal home for the IETF, the Internet Architecture Board (IAB), and the Internet Research Task Force (IRTF)' and that 'The IETF LLC is a single member LLC disregarded entity of the Internet Society'; RFC 8712 (datatracker.ietf.org draft-ietf-iasa2-rfc2031bis-08, 'The IETF-ISOC Relationship') states 'Under the terms of the Operating Agreement between ISOC and the IETF, ISOC has agreed to provide significant funding support for the IETF' and 'The IETF LLC is managed by a Board of Directors, one of whom is appointed by the ISOC's Board of Trustees'; ietf.org/blog/isoc-financial-commitment confirms a specific figure, that ISOC committed 'up to $71,400,000 over the term of th[e] agreement' announced 30 November 2020. The IETF LLC is not modelled, so this edge simplifies IETF → IETF LLC → ISOC to IETF → ISOC; see INTL-ISOC. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Standards overview: the global digital standardisation ecosystem"
    url: "https://epc.ac.uk/toolkit/standards-overview-the-global-digital-standardisation-ecosystem/"
    publisher: "Engineering Professors Council"
    accessed: "2026-08-28"
  - title: "IETF Administration — overview"
    url: "https://www.ietf.org/administration/overview/"
    publisher: "Internet Engineering Task Force (IETF)"
    accessed: "2026-08-28"
  - title: "Internet Society extends major financial support commitment to the IETF"
    url: "https://www.ietf.org/blog/isoc-financial-commitment/"
    publisher: "Internet Engineering Task Force (IETF)"
    accessed: "2026-08-28"
  - title: "The Updated IETF-ISOC Relationship (RFC 8712 / draft-ietf-iasa2-rfc2031bis)"
    url: "https://datatracker.ietf.org/doc/draft-ietf-iasa2-rfc2031bis/08/"
    publisher: "IETF Datatracker"
    accessed: "2026-08-28"
---

# IETF (Internet Engineering Task Force)

> **Verified 2026-08-28.** All four cited pages were read directly —
> the original epc.ac.uk source plus the three sources that previously
> only backed the `part-of` [[INTL-ISOC]] relationship, now promoted into
> the frontmatter `sources` list since they were genuinely read.
> `verification` moves from `search-only` to `primary-source`; `confidence`
> moves from `low` to `medium` since the IETF-ISOC relationship — the
> entity's one substantive claim — is now confirmed in the primary
> documents' own words rather than a single indirect academic listing.

## Description

The IETF is the standards organisation for internet protocols. Like
[[INTL-W3C]] and unlike [[INTL-ISO]], [[INTL-IEC]] and [[UN-ITU]], it is a
**direct-membership** organisation rather than one based on national
delegation.

`INTL` scope, not `UN`.

## ⚠ Still thin, but no longer a placeholder

`coverage: low` remains accurate: no IETF standard (RFC) is modelled, and
the IETF's own process, structure and output are not researched beyond its
relationship to ISOC. But the earlier "no ietf.org source was located" gap
is closed — three ietf.org/datatracker.ietf.org pages are now read and
cited, confirming the IETF-ISOC relationship in the primary documents'
own words rather than resting on a single academic listing.

The IETF is named in Batch 13's scope, which is why it exists here. A
reader should still expect a thin entity — including it with the weakness
marked follows the precedent set by [[NL-PETRA]] and [[UN-DATA-COMMONS]] —
but the thinness is now about breadth of coverage, not depth of sourcing
for the one relationship the entity asserts.

Note that internet protocol standards do underpin parts of the Dutch layer —
[[NL-PAS-TOE-OF-LEG-UIT]] mandates HTTPS, DNSSEC and mail-security standards
that originate in IETF RFCs — so a properly researched IETF entity would
connect to real content. That connection is queued, not asserted.

## Relationships

- Peer direct-membership standards body to [[INTL-W3C]].

## Sources

Listed in frontmatter, all four read directly this pass.

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
