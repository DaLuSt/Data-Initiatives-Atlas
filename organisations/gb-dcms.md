---
id: GB-DCMS
type: organisation
name: Department for Culture, Media and Sport
alternative_names:
  - DCMS
  - Department for Digital, Culture, Media and Sport
  - DDCMS
description: >
  United Kingdom ministerial department which, following the abolition of
  the Department for Science, Innovation and Technology in July 2026, took
  responsibility for digital transformation and online harms, together with
  cyber security, digital identity, inclusion and infrastructure and the
  Government Digital Service. Reported as being renamed to the Department
  for Digital, Culture, Media and Sport on taking on those functions.

level: national
country: GB
region: null

status: active
confidence: low
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-GDS
  - GB-DSIT
relationships: []

sources:
  - title: "DSIT to be scrapped with 'strengthened DCMS to take responsibility for digital transformation'"
    url: "https://www.publictechnology.net/2026/07/21/government-and-politics/dsit-to-be-scrapped-with-strengthened-dcms-to-take-responsibility-for-digital-transformation/"
    publisher: "PublicTechnology"
    accessed: "2026-08-22"
  - title: "DSIT scrapped as Burnham government reshapes Whitehall tech functions"
    url: "https://www.ukauthority.com/articles/dsit-scrapped-as-burnham-government-reshapes-whitehall-tech-functions"
    publisher: "UKAuthority"
  - title: "Burnham Breaks the Mould: Government Confirms DSIT Break-Up and departmental reshuffle"
    url: "https://www.dma.org.uk/about/articles/burnham-breaks-the-mould-government-confirms-dsit-break-up-and-departmental-reshuffle"
    publisher: "Data & Marketing Association"
    accessed: "2026-08-22"
  - title: "Government abolishes DSIT as AI gains a seat at the Cabinet table"
    url: "https://www.thinkdigitalpartners.com/news/2026/07/21/government-abolishes-dsit-as-ai-gains-a-seat-at-the-cabinet-table/"
    publisher: "THINK Digital Partners"
    accessed: "2026-08-22"
---

# Department for Culture, Media and Sport

> **Verified 2026-08-22.** Three independent trade-press accounts were read
> directly, including a written ministerial statement they each quote.
> `ukauthority.com` returned a bot-defense challenge (403) and was not
> read; the naming ambiguity (DCMS vs DDCMS) is confirmed rather than
> resolved.

## Description

Confirmed by reading thinkdigitalpartners.com (2026-08-22): "The Department
for Culture, Media and Sport (DCMS) will be renamed the Department for
Digital, Culture, Media and Sport (DDCMS), taking responsibility for
digital government functions including the Government Digital Service
(GDS)." dma.org.uk, read the same day, confirms via a written ministerial
statement: "Online harms and digital identity ... go to DCMS." DCMS is the department that, since **21 July 2026**, holds the UK's digital
transformation brief — including **[[GB-GDS]]**, cyber security, digital
identity, inclusion and infrastructure, and online harms — after
[[GB-DSIT]] was abolished.

## `confidence: low`, deliberately

This is the least certain entity in the UK batch, and the reason is worth
being explicit about.

DCMS is a long-standing department that has existed for decades under
several names; **nothing about that history is established here.** What is
recorded is only its position after July 2026, and that rests on trade-press
reporting published within days of the change, including one account of an
internal document. No machinery-of-government order, departmental page or
statutory instrument was located.

The naming is unsettled in the sources themselves: the department is
reported both as **DCMS** and as renamed to the **Department for Digital,
Culture, Media and Sport (DDCMS)**. Both forms are carried in
`alternative_names` because the Atlas cannot say which is correct.

`status: active` is a claim only that the department exists — which is
uncontroversial — and not that its digital remit is settled.

## Why it exists as an entity

Purely so that [[GB-GDS]]'s `governed-by` edge has a target that is not
invented. Without it, the alternative was to point GDS at an abolished
department, or to leave its governance unstated. Both are worse.

This is the same reasoning that created register-holding organisations in
the basisregistraties batch: an entity may exist to make a *sourced*
relationship expressible, provided the entity itself is honestly scoped.
`coverage: low` says how little of it is here.

## Not modelled

**DBIST** — the Department for Business, Innovation, Science and Trade,
which took DSIT's business, innovation, science and trade functions — and
the **Cabinet Office**, which took AI policy. Both are real and neither was
researched, so neither is here. See [[GB-DSIT]] for why that makes the
three-way split unrepresentable in the structured data.

## Relationships

None asserted from this entity. [[GB-GDS]] carries the `governed-by` edge
pointing here.

## Sources

Listed in frontmatter. **All four are trade press**, though two of them
(dma.org.uk, thinkdigitalpartners.com) quote directly from a written
ministerial statement rather than reporting second-hand. No government
source for the post-July-2026 arrangement was found and read directly, and
that remains the single most important gap in this batch.
`ukauthority.com` is bot-walled (403) and was not read.
