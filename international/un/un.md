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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    accessed: "2026-08-27"
  - title: "About Us | United Nations"
    url: "https://www.un.org/en/about-us"
    publisher: "United Nations"
    accessed: "2026-08-27"
---

# United Nations

> **Verified 2026-08-27.** Both cited pages were read directly, closing
> the Batch 6 audit finding that this entity's sole source URL had been
> composed from background knowledge and never actually confirmed.

## Description

The United Nations is the first international-level anchor populated in the
Data Initiatives Atlas. UN-system initiatives, strategies and standards
(UN Data Strategy, UN Digital Strategy, UN 2.0, Global Digital Compact,
statistical initiatives, etc.) reference this entity, typically via
`maintained-by`/`governed-by`/`organisations:`.

Confirmed by reading un.org's own "About Us" page directly: the UN is "an
international organization founded in 1945," now "made up of 193 Member
States," guided by "the purposes and principles contained in its founding
Charter." The page gives the founding year but not a specific date, so
`start_date` stays `null` rather than being padded to the well-known 24
October 1945 Charter-effective date that background knowledge would supply.

`coverage: low` is deliberate — this Batch 0 commit only establishes the
anchor node. Substantive UN/international content is researched starting in
Batch 12 (see `progress/backlog.md`).

## The Batch 6 audit finding is now closed

`verification` was `unverified` — stronger than the `search-only` label
carried by most of the Atlas, and worse — because this entity's one source
URL was composed from background knowledge in Batch 0, before the
`verification` field existed, and never actually confirmed by search or
fetch. Both `un.org`'s homepage and its "About Us" page are now read
directly, and a second, more substantive source has been added.

## Relationships

See `international/un/index.md` for the curated index of UN-related
entities, built up batch by batch.

## Sources

Listed in frontmatter, both read directly this pass.
