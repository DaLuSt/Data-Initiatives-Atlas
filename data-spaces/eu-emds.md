---
id: EU-EMDS
type: data-space
name: Common European Mobility Data Space
alternative_names:
  - EMDS
  - European Mobility Data Space
description: >
  One of the common European data spaces, covering mobility and transport
  data. Described as a resource for managing intermodal logistics in the
  freight sector as well as for personal mobility.

level: regional
country: null
region: EU

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
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - NL-NTM
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Mobility is one of the 14 common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21; digital-strategy.ec.europa.eu data-spaces). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Towards a common European mobility data space (EMDS)"
    url: "https://www.data-spaces-symposium.eu/wp-content/uploads/2024/03/1535DI1.pdf"
    publisher: "Data Spaces Symposium"
  - title: "Common European Data Spaces — SWD(2024) 21 final"
    url: "https://www.tcontas.pt/en-gb/seminars/sais-data/Documents/Documents/Common%20European%20Data%20Spaces%20-%20latest%20report%20Jan%202024.pdf"
    publisher: "European Commission (copy hosted by Tribunal de Contas)"
---

# Common European Mobility Data Space (EMDS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The mobility data space is one of the fourteen common European data spaces.
Sources describe it as an important resource for managing intermodal
logistics in the freight sector as well as for personal mobility.

`confidence: low` and `coverage: low`. Beyond that purpose statement,
**almost nothing was established**: not its governance, responsible
organisations, standards, technical infrastructure, participating countries,
or current stage of development. Batch 10's brief asks for all of those; for
this data space they are unanswered.

## Relationship to the national access points, not asserted

[[NL-NTM]] is the Dutch national access point for mobility data, existing
under [[EU-ITS-DIRECTIVE]]. National access points are the obvious
building blocks of an EU mobility data space, and the connection is close to
self-evident.

**It is not asserted.** No source read states that the EMDS builds on the
NAP network, and "obvious" has repeatedly turned out to be the wrong
standard in this project. The association is recorded via
`related_entities`; the relationship awaits a source.

Note the contrast with [[NL-NTM]] itself, where Batch 5 left the same kind
of gap open and Batch 8 closed it with a real citation. That is the pattern
to repeat here.

## Sources

Listed in frontmatter. The third is a Commission staff working document
hosted by a third party rather than on a Commission domain — usable, but a
direct Commission copy should replace it.
