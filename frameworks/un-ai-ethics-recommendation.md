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
verification: primary-source

start_date: 2021-11-23
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading three of the five cited pages directly (2026-08-28). unesco.org's own recommendation-ethics page and its article both confirm November 2021 adoption by 193 Member States, ten core principles, four core values and eleven policy areas. The EU-partnership article, also read directly, confirms the accord with the European Commission, a EUR 4 million budget for least-developed countries, the 'AI Ethics Experts without Borders' facility, the annual Global Forum on the Ethics of AI, and a judicial-operators toolkit — all in UNESCO's own words. Neither fetched page states the 'nearly thirty countries' adoption figure or names Czechia/Slovenia as Global Forum hosts; those two specific claims are downgraded to unconfirmed-this-pass rather than repeated as read. unesdoc.unesco.org (403) and unesco.org.uk's PDF (403) were not read."
    confidence: high
    valid_from: 2021-11-23
    valid_until: null

sources:
  - title: "Recommendation on the Ethics of Artificial Intelligence"
    url: "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics"
    publisher: "UNESCO"
    accessed: "2026-08-28"
  - title: "Recommendation on the Ethics of Artificial Intelligence (article)"
    url: "https://www.unesco.org/en/articles/recommendation-ethics-artificial-intelligence"
    publisher: "UNESCO"
    accessed: "2026-08-28"
  - title: "Implementation of the Recommendation on the Ethics of Artificial Intelligence (AI)"
    url: "https://unesdoc.unesco.org/ark:/48223/pf0000387369"
    publisher: "UNESCO"
  - title: "Artificial intelligence: Partnership between UNESCO and the EU to speed implementation of ethical rules"
    url: "https://www.unesco.org/en/articles/artificial-intelligence-partnership-between-unesco-and-eu-speed-implementation-ethical-rules"
    publisher: "UNESCO"
    accessed: "2026-08-28"
  - title: "UNESCO Recommendation on the Ethics of Artificial Intelligence — key facts"
    url: "https://unesco.org.uk/site/assets/files/14137/unesco_recommendation_on_the_ethics_of_artificial_intelligence_-_key_facts.pdf"
    publisher: "UK National Commission for UNESCO"
---

# UNESCO Recommendation on the Ethics of Artificial Intelligence

> **Verified 2026-08-28.** Three of five cited pages were read directly —
> both unesco.org recommendation pages and the EU-partnership article — all
> confirming the Recommendation's own core content in UNESCO's own words.
> Two specific figures previously stated without qualification (the "nearly
> thirty countries" adoption claim and Czechia/Slovenia as Global Forum
> hosts) were **not** confirmed by any page read this pass and are
> downgraded below rather than silently repeated.

## Description

Adopted on **23 November 2021 by UNESCO's 193 member states** — confirmed by
reading unesco.org's own pages directly — the Recommendation sets ethical
rules for artificial intelligence grounded in **ten core principles** and
**four core values** (human dignity and rights, just societies, diversity
and inclusiveness, environmental flourishing), operationalised across
**eleven policy areas**. **Nearly thirty countries** are *reported* to have
begun using it to establish national legislation — this specific figure was
not repeated on any page read this pass, so it is carried forward as an
unconfirmed claim from the original research rather than a re-verified fact.

UNESCO and the European Commission have agreed to accelerate its global
implementation — confirmed directly this pass via UNESCO's own partnership
article: the **"AI Ethics Experts without Borders" (AIEB)** global expert
facility, an annual **Global Forum on the Ethics of AI**, a **EUR 4 million**
budget for least-developed countries, and a **judicial-operators toolkit**.
The claim that the Forum is "hosted by Czechia and later Slovenia during
their Council Presidencies" was **not** found on any page read this pass and
is likewise carried forward unconfirmed rather than verified.

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

Listed in frontmatter, three of five read directly this pass: both
unesco.org recommendation pages and the EU-partnership article. The
UNESDOC implementation document and the UK National Commission's PDF both
returned HTTP 403 and were not read.
