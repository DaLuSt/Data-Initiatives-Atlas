---
id: EU-PUBLIC-ADMIN-DATA-SPACE
type: data-space
name: Common European data space for public administration
alternative_names:
  - Public administration data space
  - Public administrations data space
description: >
  One of the fourteen common European data spaces, covering public
  administrations. It is named among the strategic sectors of the European
  Data Strategy and sits closest of the fourteen to the Atlas's own
  subject matter.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: 
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-INTEROPERABLE-EUROPE-ACT
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Public administration is one of the fourteen common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21 final of 24.1.2024; digital-strategy.ec.europa.eu 'Common European data spaces'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: EU-INTEROPERABLE-EUROPE-ACT
    source: interpretation
    evidence: "PARTIALLY NARROWS discovery/unresolved.md row #121. data.europa.eu's own article 'Interoperability in data spaces: Building Europe's digital future' (read directly, 2026-09-18) states, of common European data spaces generally: 'Initiatives such as the SEMIC Support Centre and Interoperable Europe Act provide tools and frameworks to support compatibility.' This is a general statement about data spaces collectively, not one naming the public administration data space specifically, so it is recorded as `source: interpretation` (this data space is one of the fourteen the statement describes) rather than `fact`. The EIF and EU-SDG halves of the row's question remain unanswered: no source read connects either to this entity, specifically or generally."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "SWD(2024) 21 final — Staff working document on common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/library/staff-working-document-data-spaces"
    publisher: "European Commission"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Interoperability in data spaces: Building Europe's digital future"
    url: "https://data.europa.eu/en/news-events/news/interoperability-data-spaces-building-europes-digital-future"
    publisher: "data.europa.eu — Publications Office of the European Union"
    accessed: "2026-09-18"
---

# Common European data space for public administration

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Narrowed 2026-09-18** (`discovery/unresolved.md` row #121): one of the
> temptations recorded below now has a thin, general source. See "One
> connection, thinly sourced" below — the row is narrowed, not closed.

## Description

One of the fourteen common European data spaces, covering public administrations.
It is named among the strategic sectors of the European Data Strategy and sits closest of the fourteen to the Atlas's own subject matter.

## The one closest to the rest of this Atlas

Public administration is the sector the Atlas covers most densely: 232 of its
entities carry [[DOMAIN-GOVERNMENT]], making it by a wide margin the largest
node in the association layer.

So this data space is the natural meeting point between the data-space layer
and everything else the Atlas holds — [[EU-INTEROPERABLE-EUROPE-ACT]],
[[EU-EIF]], the national interoperability frameworks, the open data portals.

**Most of those connections remain unasserted**, and this is exactly the
entity where a repository would be most tempted to draw them. Two of the
three temptations are recorded here still open:

- [ ] How does the public administration data space relate to [[EU-EIF]]
  specifically?
- [ ] Does it build on [[EU-SDG]], the Single Digital Gateway?

## One connection, thinly sourced — 2026-09-18

The third — [[EU-INTEROPERABLE-EUROPE-ACT]] — now has a source, though a
thin one. data.europa.eu's own article "Interoperability in data spaces:
Building Europe's digital future," read directly, states of common
European data spaces generally: *"Initiatives such as the SEMIC Support
Centre and Interoperable Europe Act provide tools and frameworks to
support compatibility."*

This names the Act specifically, but describes data spaces **collectively**
rather than this one by name — the Commission's own dedicated page for
this data space (fetched earlier and cited above) says nothing about the
Act. The edge is recorded at `source: interpretation`, `confidence: low`:
this entity is one of the fourteen the general statement describes, but
the statement itself does not single it out. The EIF and SDG questions
above remain fully open — no source read connects either to data spaces
in general or to this one specifically.

Both remaining questions are in `discovery/unresolved.md`.

## ⚠ `coverage: low`

Its deployment, governance and scope were not established beyond its presence
in the list of fourteen.

## Sources

Listed in frontmatter. The data.europa.eu article was added and read
directly 2026-09-18.
