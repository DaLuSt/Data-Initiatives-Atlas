---
id: NL
type: country
name: Netherlands
alternative_names:
  - Kingdom of the Netherlands
  - Nederland
description: >
  Country anchor entity for the Netherlands, the first national scope
  covered by the Data Initiatives Atlas. Used as the target of `country`
  fields and `applies-in` relationships for Dutch-scoped entities.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: unverified

start_date: null
end_date: null
last_verified: "2026-08-14"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "NL — ISO 3166-1 country code"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:NL"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-08-14"
  - title: "Government of the Netherlands"
    url: "https://www.government.nl/"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-14"
---

# Netherlands

## Description

The Netherlands (ISO 3166-1 alpha-2: `NL`) is the first country populated in
the Data Initiatives Atlas. This entity anchors the national layer of the
graph: Dutch initiatives, legislation, organisations, standards and
frameworks reference it via `country: NL`, and EU/international entities
that apply to the Netherlands reference it via an `applies-in` relationship.

`coverage: low` is deliberate — this Batch 0 commit only establishes the
anchor node. Substantive Dutch content is researched and added starting in
Batch 1 (see `progress/backlog.md`).

## ⚠ Verification note (added in Batch 6)

`verification: unverified` — stronger than the `search-only` label carried by
most of the Atlas, and worse.

This entity was written in Batch 0, before the network block was discovered
and before the `verification` field existed. Its source URLs were composed
from background knowledge rather than confirmed by a search index or
fetched. They are very likely correct — these are among the best-known URLs
in existence — but "very likely correct" is precisely the standard the brief
rules out, and the Atlas should not hold itself to a lower bar for easy
facts than for hard ones.

The Batch 6 audit surfaced this. Recorded in `discovery/unresolved.md`.

## Relationships

See `countries/nl/index.md` for the curated index of Dutch entities, built
up batch by batch.

## Sources

Listed in frontmatter.
