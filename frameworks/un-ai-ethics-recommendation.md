---
id: UN-AI-ETHICS-RECOMMENDATION
type: framework
name: Recommendation on the Ethics of Artificial Intelligence
alternative_names:
  - UNESCO Recommendation on the Ethics of AI
  - UNESCO AI Ethics Recommendation
description: >
  UNESCO instrument adopted on 23 November 2021 by the organisation's 193
  member states, setting out ethical rules for artificial intelligence
  intended to ensure that AI respects fundamental freedoms and human rights.
  Nearly thirty countries are reported to have begun using it to establish
  national legislation. UNESCO and the European Commission have agreed to
  accelerate its global implementation, including a global facility of
  experts, an annual Global Forum on the Ethics of AI — hosted by Czechia
  and later Slovenia during their Presidencies of the Council of the
  European Union — and a budget dedicated to supporting least developed
  countries in establishing national legislation.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-11-23
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations:
  - UN-UNESCO
related_entities:
  - UN-UNESCO
  - EU-AI-ACT
  - ES-AESIA
relationships:
  - type: maintained-by
    target: UN-UNESCO
    source: fact
    evidence: "The Recommendation on the Ethics of Artificial Intelligence was adopted in November 2021 by the 193 Member States of UNESCO, and UNESCO publishes and maintains it, including implementation material and the Global Forum on the Ethics of AI (unesco.org/en/artificial-intelligence/recommendation-ethics; unesco.org/en/articles/recommendation-ethics-artificial-intelligence; unesdoc.unesco.org ark:/48223/pf0000387369). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-11-23
    valid_until: null

sources:
  - title: "Recommendation on the Ethics of Artificial Intelligence"
    url: "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics"
    publisher: "UNESCO"
  - title: "Recommendation on the Ethics of Artificial Intelligence (article)"
    url: "https://www.unesco.org/en/articles/recommendation-ethics-artificial-intelligence"
    publisher: "UNESCO"
  - title: "Implementation of the Recommendation on the Ethics of Artificial Intelligence (AI)"
    url: "https://unesdoc.unesco.org/ark:/48223/pf0000387369"
    publisher: "UNESCO"
  - title: "Artificial intelligence: Partnership between UNESCO and the EU to speed implementation of ethical rules"
    url: "https://www.unesco.org/en/articles/artificial-intelligence-partnership-between-unesco-and-eu-speed-implementation-ethical-rules"
    publisher: "UNESCO"
  - title: "UNESCO Recommendation on the Ethics of Artificial Intelligence — key facts"
    url: "https://unesco.org.uk/site/assets/files/14137/unesco_recommendation_on_the_ethics_of_artificial_intelligence_-_key_facts.pdf"
    publisher: "UK National Commission for UNESCO"
---

# UNESCO Recommendation on the Ethics of Artificial Intelligence

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Adopted on **23 November 2021 by UNESCO's 193 member states**, the
Recommendation sets ethical rules for artificial intelligence intended to
ensure AI respects fundamental freedoms and human rights. **Nearly thirty
countries** are reported to have begun using it to establish national
legislation.

UNESCO and the European Commission have agreed to accelerate its global
implementation — a global expert facility, an annual **Global Forum on the
Ethics of AI** (hosted by Czechia and later Slovenia during their Council
Presidencies), and a budget for least developed countries.

## The AI timeline the Atlas can now show

Adding this entity makes a sequence visible that no single layer contained:

| Date | Instrument / body | Layer |
|---|---|---|
| Nov 2021 | **this Recommendation** — 193 states | UN |
| Aug 2023 | [[ES-AESIA]] created — the EU's first AI supervisory agency | national |
| 2024 | [[EU-AI-ACT]] — Regulation (EU) 2024/1689 | EU |

The Spain batch already recorded the oddity that AESIA *predates the
regulation that governs it*. With the Recommendation in place the picture is
larger and less odd: a UN soft-law instrument came first, national bodies
formed, and the binding EU regulation arrived last.

**No relationship is asserted between this Recommendation and
[[EU-AI-ACT]].** That is the important restraint here. The sequence above is
chronology, not causation, and nothing read says the AI Act implements,
derives from or references the Recommendation. Asserting an edge because the
dates line up is precisely the error the Atlas's provenance model exists to
prevent — and it would be a particularly attractive error, because a
UN → EU → national AI chain is exactly the shape this batch was looking for.

The genuine UN → EU chain in this batch is [[UN-AARHUS]] →
[[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]], which has a source saying so.
This one does not, and is left open.

## Soft law, and the Atlas has no way to say so

A UNESCO Recommendation is **not binding**. [[UN-AARHUS]] is a convention
and binds its Parties. Both are recorded here with the same vocabulary —
`UN-AARHUS` as `type: law`, this as `type: framework` — and neither type
carries the binding/non-binding distinction.

The Atlas has now hit this from two directions: the Spain batch found that
`type: law` flattens Spain's constitutional `Ley Orgánica` rank, and this
batch finds that nothing distinguishes a treaty from a recommendation. They
are the same missing property at different levels.

Logged together in `discovery/unresolved.md`. **No field was added** — six
country and layer batches have run without one, and adding it would require
re-reading every instrument in the Atlas to populate it honestly.

## Relationships

- `maintained-by` [[UN-UNESCO]].

## Sources

Listed in frontmatter — three UNESCO publications including the
implementation document, the EU partnership announcement, and the UK
National Commission's key-facts summary.
