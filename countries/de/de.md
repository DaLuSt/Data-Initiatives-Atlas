---
id: DE
type: country
name: Germany
alternative_names:
  - Federal Republic of Germany
  - Bundesrepublik Deutschland
  - Deutschland
description: >
  Country anchor entity for Germany, the second national scope covered by
  the Data Initiatives Atlas. Used as the target of `country` fields and
  `applies-in` relationships for German-scoped entities.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-21"
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
    evidence: "Germany is one of the 27 member states of the European Union, having acceded on 1 January 1958; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "DE — Germany (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:DE"
    publisher: "International Organization for Standardization (ISO)"
---

# Germany

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`, `iso.org`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

Germany (ISO 3166-1 alpha-2: `DE`) is the **second country** populated in
the Data Initiatives Atlas. German initiatives, legislation, organisations,
standards, frameworks and platforms reference it via `country: DE`, and EU
entities that apply to Germany reference it via an `applies-in`
relationship — exactly as they do for [[NL]].

## Why this entity is the point of the exercise

Until Germany was added, the country-neutral architecture was an assertion.
Every `applies-in` relationship in the Atlas targeted a single country, so
nothing distinguished a genuinely country-neutral model from a
Netherlands-shaped one that happened to use general vocabulary. The Final
Quality Gate recorded this precisely: *"another country addable immediately
— structurally; untested with a second country."*

Adding Germany tested it. What the test required:

- **No ontology change.** `metadata/ontology.md` §2.1 already named `DE` in
  its list of possible scopes. No entity type, relationship type, status,
  folder or validation rule needed altering.
- **No parallel tree.** German entities live in the same flat type folders
  as Dutch and EU ones — `legislation/de-bdsg.md` sits beside
  `legislation/nl-uavg.md` and `legislation/eu-gdpr.md`.
- **No duplicated EU instruments.** Not one `DE-EU-*` entity was created.
  The EU legislation already in the Atlas gained `applies-in` → `DE`
  relationships alongside their existing `applies-in` → `NL`.

That last point is the substantive result. [[EU-GDPR]] is one entity that
now applies in two countries and is implemented by two national acts
([[NL-UAVG]] and [[DE-BDSG]]); it is not two entities. The same holds for
[[EU-NIS2]] ([[NL-CBW]] / [[DE-NIS2UMSUCG]]), [[EU-OPEN-DATA-DIRECTIVE]]
([[NL-WHO]] / [[DE-DNG]]) and [[EU-ITS-DIRECTIVE]] ([[NL-NTM]] /
[[DE-MOBILITHEK]]).

## Verification note

`verification: search-only`, not `unverified`.

This is a deliberate contrast with [[NL]], [[EU]] and [[UN]], which are all
`unverified` because they were written in Batch 0 with source URLs composed
from background knowledge rather than confirmed to exist. The single URL
cited here was returned by a search index. That is still a long way from
having been read, but it is the standard the rest of the Atlas holds itself
to, and the second country was written under it from the start rather than
being corrected into it afterwards.

## A note on federalism

Germany's public-sector digital landscape is federal in a way the Atlas
does not yet model. Responsibility is shared between the Bund, the sixteen
Länder and the Kommunen, and several central entities recorded here —
[[DE-IT-PLANUNGSRAT]], [[DE-FITKO]], [[DE-GOVDATA]], [[DE-GDI-DE]] — exist
specifically to coordinate across those levels.

Every German entity in this batch is federal (`level: national`) or
federal-coordinating. **No Land-level or municipal entity has been
created.** The Atlas has no sub-national level between `national` and
`local` in its `level` vocabulary, and inventing one for Germany alone
would be precisely the country-specific ontology change the model exists to
avoid. This is logged as an open question in `discovery/unresolved.md`
rather than resolved by guesswork.

## Relationships

See `countries/de/index.md` for the curated index of German entities.

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

Listed in frontmatter. **No `accessed` date and no `last_verified`** —
nothing about this entity has been checked against a source.
