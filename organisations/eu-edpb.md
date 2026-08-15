---
id: EU-EDPB
type: organisation
name: European Data Protection Board
alternative_names:
  - EDPB
description: >
  EU body established under the GDPR to ensure consistent application of
  data protection law across member states. It comprises representatives of
  each national supervisory authority together with the European Data
  Protection Supervisor.

level: regional
country: null
region: EU

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
  - EU-GDPR
  - EU-EDPS
  - NL-AP
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "The EDPB is an EU body established under the GDPR to ensure consistent application of data protection law across member states (edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EU-GDPR
    source: fact
    evidence: "The European Data Protection Board was established under the GDPR to ensure consistent application of data protection laws across all EU member states (edpb.europa.eu; legiscope). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "European Data Protection Board — news"
    url: "https://www.edpb.europa.eu/news/news/2026/edpb-and-edps-support-strengthening-eus-cybersecurity-and-easing-compliance-while_en"
    publisher: "European Data Protection Board"
  - title: "The Role of the European Data Protection Board (EDPB)"
    url: "https://www.legiscope.com/blog/role-european-data-protection-board.html"
    publisher: "Legiscope"
---

# European Data Protection Board (EDPB)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The EDPB was established under [[EU-GDPR]] to ensure the regulation is
applied consistently across all member states. It comprises representatives
of each national supervisory authority together with [[EU-EDPS]], which has
the right to appoint one representative — an arrangement intended to keep
the Board and the Supervisor closely coordinated.

## What this closes, and how far

[[NL-AP]] has carried a pending EDPB relationship since Batch 2. It is now
closable in principle: the Dutch data protection authority is a national
supervisory authority under the GDPR, and the Board is composed of exactly
those authorities.

The `participates-in` relationship is recorded on [[NL-AP]] at
`confidence: medium`, because the composition rule is sourced generically
("representatives from each national supervisory authority") rather than by
a source naming the Dutch authority as a member. That is a reasonable
inference from a sourced rule rather than a guess — but the distinction is
worth preserving, so the evidence field says so.

`coverage: low`: the Board's guidelines, consistency mechanism and
enforcement coordination were not researched.

## Relationships

- Established under [[EU-GDPR]].
- Composed of national supervisory authorities including [[NL-AP]], plus
  [[EU-EDPS]].

## Sources

Listed in frontmatter. The second is a commercial blog — a weak source for
an EU institution, and the sort of citation a re-verification pass should
replace with the EDPB's own "about" material.
