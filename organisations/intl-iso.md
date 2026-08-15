---
id: INTL-ISO
type: organisation
name: International Organization for Standardization
alternative_names:
  - ISO
description: >
  International standards organisation based on national delegation, and
  **not** a UN body. With the IEC it operates Joint Technical Committee 1
  on information technology, which publishes the ISO/IEC 27000 family of
  information security standards.

level: international
country: null
region: null

status: active
confidence: medium
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
  - INTL-IEC
  - NL-NEN
relationships: []

sources:
  - title: "ISO/IEC 27000 family — Information security management"
    url: "https://www.iso.org/standard/iso-iec-27000-family"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Standards overview: the global digital standardisation ecosystem"
    url: "https://epc.ac.uk/toolkit/standards-overview-the-global-digital-standardisation-ecosystem/"
    publisher: "Engineering Professors Council"
---

# ISO (International Organization for Standardization)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

ISO is an international standards organisation operating on national
delegation — its members are national standards bodies, including
[[NL-NEN]], which Batch 2 research recorded as a co-founder of ISO in 1947.

With [[INTL-IEC]] it operates **ISO/IEC Joint Technical Committee 1** on
information technology, whose Subcommittee 27 (information security,
cybersecurity and privacy protection) publishes [[INTL-ISO-IEC-27001]] and
[[INTL-ISO-IEC-27002]].

## Not a UN organisation

`INTL` scope, not `UN`. ISO is an independent international organisation,
not part of the UN system — the distinction Batch 13's brief specifically
warns about. It appears alongside [[UN-ITU]] in standards-ecosystem
listings, but only the ITU is a UN specialised agency.

## The NEN relationship, still unasserted

Batch 2 recorded that NEN was a co-founder of ISO in 1947 and works closely
with it. **No relationship is asserted here**, because the sourced statement
concerns NEN's own page rather than an ISO membership list, and because the
`participates-in` links added in Batch 9 ([[NL-NEN]] → [[EU-CEN]]) rested on
an explicit composition rule that is not available here. The association is
recorded via `related_entities`. This is a smaller gap than it looks and
should be easy to close.

`coverage: low`: ISO's governance, membership structure and wider catalogue
were not researched.

## Relationships

- Operates JTC 1 jointly with [[INTL-IEC]].
- Associated with [[NL-NEN]].

## Sources

Listed in frontmatter.
