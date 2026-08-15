---
id: UN
type: organisation
name: United Nations
alternative_names:
  - UN
description: >
  International anchor entity for the United Nations. Used as the
  organisation target for UN-system initiatives, strategies and standards
  before their relationships to EU/national entities are recorded.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: unverified

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "United Nations — official website"
    url: "https://www.un.org/"
    publisher: "United Nations"
---

# United Nations

## Description

The United Nations is the first international-level anchor populated in the
Data Initiatives Atlas. UN-system initiatives, strategies and standards
(UN Data Strategy, UN Digital Strategy, UN 2.0, Global Digital Compact,
statistical initiatives, etc.) reference this entity, typically via
`maintained-by`/`governed-by`/`organisations:`.

`coverage: low` is deliberate — this Batch 0 commit only establishes the
anchor node. Substantive UN/international content is researched starting in
Batch 12 (see `progress/backlog.md`).

## ⚠ Verification note (added in Batch 6)

`verification: unverified` — see the identical note on [[NL]]. This entity
was written in Batch 0 with a source URL composed from background knowledge
rather than confirmed by search or fetch. Surfaced by the Batch 6 audit and
recorded in `discovery/unresolved.md`.

## Relationships

See `international/un/index.md` for the curated index of UN-related
entities, built up batch by batch.

## Sources

Listed in frontmatter. **No `accessed` dates and no `last_verified`** — the
Final Quality Gate found both being claimed here when nothing had in fact
been accessed or verified, and removed them. Nothing about this entity has
been checked against a source.
