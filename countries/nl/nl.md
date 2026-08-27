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
region: EU

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
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Confirmed by reading european-union.europa.eu's own page directly (2026-08-27): 'EU Member State since 1958, Euro area member since 1999, Schengen area member since 1995.' government.nl, also read directly, describes itself as the official portal providing 'Information from the Government of the Netherlands.' ISO's OBP is confirmed genuinely bot-walled (403) elsewhere in this Atlas's re-verification work — it is a JavaScript application, not a static page. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-27"
  - title: "NL — ISO 3166-1 country code (confirmed genuinely bot-walled, 403)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:NL"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Government of the Netherlands"
    url: "https://www.government.nl/"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-27"
---

# Netherlands

> **Verified 2026-08-27.** Two of three cited pages were read directly,
> closing the Batch 6 audit finding that this entity's source URLs had
> been composed from background knowledge and never actually confirmed.
> ISO's OBP is confirmed genuinely bot-walled (403) — a JavaScript
> application, not a static page.

## Description

The Netherlands (ISO 3166-1 alpha-2: `NL`) is the first country populated in
the Data Initiatives Atlas. This entity anchors the national layer of the
graph: Dutch initiatives, legislation, organisations, standards and
frameworks reference it via `country: NL`, and EU/international entities
that apply to the Netherlands reference it via an `applies-in` relationship.

`coverage: low` is deliberate — this Batch 0 commit only establishes the
anchor node. Substantive Dutch content is researched and added starting in
Batch 1 (see `progress/backlog.md`).

## The Batch 6 audit finding is now closed

`verification` was `unverified` — stronger than the `search-only` label
carried by most of the Atlas, and worse.

This entity was written in Batch 0, before the network block was discovered
and before the `verification` field existed. Its source URLs were composed
from background knowledge rather than confirmed by a search index or
fetched. They turned out to be correct: reading european-union.europa.eu
directly confirms the Netherlands as an "EU Member State since 1958, Euro
area member since 1999, Schengen area member since 1995," and
government.nl's own front page confirms itself as the official government
information portal. Two of the entity's three sources are now read
directly — the ISO OBP remains confirmed genuinely bot-walled (403)
elsewhere in this Atlas's re-verification work.

The Batch 6 audit surfaced this. Recorded in `discovery/unresolved.md`.

## Relationships

See `countries/nl/index.md` for the curated index of Dutch entities, built
up batch by batch.

## ⚠ Two dates, and why this entity uses 1958

A verification pass on 2026-08-20 supplied **25 March 1957** as this
country's accession date. This entity says **1 January 1958**. Both are
right, about different events:

| Date | Event |
|---|---|
| **25 March 1957** | the Treaty of Rome was **signed**, in Rome |
| **1 January 1958** | the Treaty **entered into force**, and the Communities existed |

Strictly neither is an *accession*. The six founding members — [[BE]],
[[DE]], [[FR]], [[IT]], [[LU]] and [[NL]] — did not accede to anything; they
founded it. "Accession date" is a column borrowed from the twenty-one states
that did join later.

The Atlas uses **1 January 1958** because that is what its own cited source
says: the Union's list of EU countries records the founding six under 1958,
and this entity's `part-of` [[EU]] evidence cites that page. Using 1957 would
put the entity in contradiction with the source it names.

**This is recorded rather than resolved.** The signature date is genuinely
useful and is now here; if the Atlas would rather key the founders on 1957,
the evidence strings and the cited source both need changing together.

## Sources

Listed in frontmatter, two of three read directly this pass —
european-union.europa.eu and government.nl. ISO's OBP is genuinely
bot-walled (403).
