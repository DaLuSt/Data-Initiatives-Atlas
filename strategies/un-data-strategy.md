---
id: UN-DATA-STRATEGY
type: strategy
name: UN Secretary-General's Data Strategy
alternative_names:
  - UN Data Strategy
description: >
  "Data Strategy for Action by Everyone, Everywhere, with Insight, Impact
  and Integrity" — the UN Secretary-General's organisation-wide data
  strategy, approved in April 2020 and jointly designed by 50 UN entities.
  It predates UN 2.0 by three years; UN 2.0's later "quintet of change"
  draws on it for the data capability rather than the strategy having been
  produced by UN 2.0.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2020-04-01
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - UN
related_entities:
  - UN-2-0
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading un.org's own dedicated data-strategy pages directly this pass (2026-08-28): un.org/en/content/datastrategy/index.shtml and un.org/en/content/datastrategy/, both titled 'Data Strategy for Action by Everyone, Everywhere with Insight, Impact and Integrity'. These replace the previous single indirect citation (the UN 2.0 quintet PDF, which never actually named this strategy). A WebSearch cross-check of un.int's announcement and the UN Digital Library's own catalogue record (digitallibrary.un.org/record/3872047, titled '...2020-22') corroborates April 2020 as the approval period, though neither un.org page itself states an exact approval date."
    confidence: medium
    valid_from: 2020-04-01
    valid_until: null

sources:
  - title: "UN Secretary-General's Data Strategy"
    url: "https://www.un.org/en/content/datastrategy/index.shtml"
    publisher: "United Nations"
    accessed: "2026-08-28"
  - title: "UN Secretary-General's Data Strategy (landing page)"
    url: "https://www.un.org/en/content/datastrategy/"
    publisher: "United Nations"
    accessed: "2026-08-28"
  - title: "UN 2.0 — Quintet of Change"
    url: "https://www.un.org/sites/un2.un.org/files/2021/09/un_2.0_-_quintet_of_change.pdf"
    publisher: "United Nations"
---

# UN Secretary-General's Data Strategy

> **Verified 2026-08-28, rebuilt on a real dedicated source and a
> corrected relationship.** The prior pass's only citation was the UN 2.0
> quintet PDF, which never actually named this strategy — a documented
> placeholder, not a citation error, but still thin. A dedicated un.org page
> for the strategy exists and is read directly here, and it corrects the
> framing that this strategy was produced *by* or *for* UN 2.0.

## Description

The UN Secretary-General's Data Strategy — full title *"Data Strategy for
Action by Everyone, Everywhere, with Insight, Impact and Integrity"* — was
approved around **April 2020** (per un.int's announcement and the UN
Digital Library's own catalogue record; neither un.org page fetched this
pass states the date in so many words) and jointly designed by **50 UN
entities**. Its own page frames it as the UN's "agenda for the data-driven
transformation," built on **eight priority areas** (the Decade of Action,
climate change, gender equality, human rights and rule of law, peace and
security, governance and ethics, UN reform, and data protection/privacy),
**two core capabilities** (analytics and data management), and **four
organisational enablers** (people/culture, data governance, partnerships,
technology).

## A correction: this strategy predates UN 2.0, not the reverse

The prior description said the strategy "sits behind the data element of the
[[UN-2-0]] quintet of change", which could be misread as the strategy having
been produced for or by UN 2.0. Reading the strategy's own pages this pass
makes the chronology clear: this strategy dates to **April 2020**, while
[[UN-2-0]]'s policy brief was issued in **September 2023** — three years
later. Neither un.org page fetched this pass mentions "UN 2.0" at all. The
correct relationship is the opposite direction: the pre-existing 2020 Data
Strategy is one of the things UN 2.0's later "quintet of change" draws on
for its data capability, not something UN 2.0 created. The relationship type
(`part-of` [[UN]]) is unchanged, but the body text and the framing in
[[UN-2-0]]'s own entity should be read with this correction in mind.

## No longer the weakest entity in the batch

The prior pass called this "the weakest entity in Batch 12" on the strength
of a single indirect PDF citation. That is resolved: two dedicated un.org
pages are now read directly, giving genuine primary-source confirmation of
the strategy's existence, title, structure and priority areas. What remains
unconfirmed is the precise approval date (month-level via search corroboration,
not a directly-read un.org statement) and the strategy's current status —
whether it has been superseded, renewed, or folded into UN 2.0's later data
capability work. `confidence` moves from `low` to `medium`; `coverage`
stays `low` pending that status question.

## Relationships

- Precedes and is drawn upon by [[UN-2-0]]'s data capability — not the
  reverse, per the correction above.
- Issued within [[UN]].

## Sources

Listed in frontmatter — two of three read directly this pass: both dedicated
un.org data-strategy pages. The UN 2.0 quintet PDF was fetched again but
remained unparseable binary.
