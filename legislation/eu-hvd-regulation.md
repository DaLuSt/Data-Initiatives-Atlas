---
id: EU-HVD-REGULATION
type: regulation
name: Commission Implementing Regulation (EU) 2023/138 laying down a list of high-value datasets
alternative_names:
  - High-Value Datasets Regulation
  - HVD Regulation
  - Implementing Regulation (EU) 2023/138
description: >
  Commission implementing act adopted 21 December 2022 under Article 14(1)
  of the Open Data Directive (Directive (EU) 2019/1024), listing specific
  "high-value datasets" that member states must publish free of charge, in
  machine-readable formats, through APIs and, where relevant, as bulk
  download. Establishes six thematic categories — geospatial, Earth
  observation and environment, meteorological, statistics, companies and
  company ownership, and mobility.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2023-02-09
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: implements
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md: 'a gap affecting every member state, not one'). Confirmed by reading eur-lex.europa.eu's own text of CELEX:32023R0138 directly (2026-09-06, via the plain-colon URL form, which succeeded where the percent-encoded and PDF forms both returned empty content): Article 1(1) states the Regulation 'establishes the list of high-value datasets belonging to the thematic categories set out in Annex I to Directive (EU) 2019/1024,' adopted under 'Article 14(1)' of that Directive. The Regulation operationalises the Directive's own high-value-dataset provision rather than amending its text, so `implements` fits better than `implements-requirement-from` (which the Atlas reserves for the EU→national legislative chain) or `amends`."
    confidence: high
    valid_from: 2023-02-09
    valid_until: null

sources:
  - title: "Commission Implementing Regulation (EU) 2023/138 of 21 December 2022 laying down a list of specific high-value datasets and the arrangements for their publication and re-use"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R0138"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-09-06"
  - title: "High Value Datasets (HVD)"
    url: "https://www.cso.ie/en/statistics/highvaluedatasetshvd/"
    publisher: "Central Statistics Office, Ireland"
    accessed: "2026-09-06"
  - title: "High value datasets: what has changed and what will come next"
    url: "https://data.europa.eu/en/news-events/news/high-value-datasets-what-has-changed-and-what-will-come-next"
    publisher: "data.europa.eu (Publications Office of the European Union)"
    accessed: "2026-09-06"
---

# Commission Implementing Regulation (EU) 2023/138 (High-Value Datasets)

> **Added 2026-09-06.** `discovery/unresolved.md` had flagged this
> Implementing Regulation as unmodelled, "a gap affecting every member
> state, not one." EUR-Lex's own text, `data.europa.eu`'s own news page,
> and Ireland's Central Statistics Office (a directly-affected national
> body) were read directly. The EUR-Lex fetch itself needed a specific
> URL form: the plain-colon CELEX URI (`uri=CELEX:32023R0138`) returned
> the actual regulation text, where both the percent-encoded form
> (`uri=CELEX%3A32023R0138`) and the PDF form returned empty content —
> worth noting for any future EUR-Lex fetch on this Atlas.

## Description

Confirmed by reading EUR-Lex's own text directly: this Commission
implementing act, adopted **21 December 2022** under **Article 14(1)**
of [[EU-OPEN-DATA-DIRECTIVE]] (Directive (EU) 2019/1024), lists specific
categories of **high-value datasets** — data "whose re-use is associated
with important benefits for society, the environment and the economy,"
per the Directive's own framing. Article 1(1) states the Regulation
"establishes the list of high-value datasets belonging to the thematic
categories set out in Annex I to Directive (EU) 2019/1024."

**Six thematic categories**, confirmed directly from the Regulation's own
Annex sections and corroborated by Ireland's CSO (a national statistical
office already publishing under category 4):

1. Geospatial
2. Earth observation and environment
3. Meteorological
4. Statistics
5. Companies and company ownership
6. Mobility

Datasets in these categories must be published **free of charge**, in
**machine-readable formats**, through **APIs** and, where relevant, as
**bulk download** — the same obligations [[EU-OPEN-DATA-DIRECTIVE]]'s own
entity already describes for high-value datasets in general terms.

## Dates, confirmed directly from the Regulation's own text

- **Adopted**: 21 December 2022.
- **Published**: Official Journal L 19/43, 20 January 2023.
- **Entered into force**: Article 6 states the Regulation "shall enter
  into force on the twentieth day following that of its publication in
  the Official Journal" — **9 February 2023**, recorded as `start_date`.
- **Applied from**: the same article states it "shall apply from 16
  months after entry into force" — **9 June 2024**, corroborated by
  `data.europa.eu`'s own page stating "since 2024, the Commission
  Implementing Regulation (EU) 2023/138 has applied across all Member
  States."

## Relationship to the Open Data Directive

`implements` rather than `implements-requirement-from` is used
deliberately: the latter type is reserved by this Atlas for the
EU-directive → national-transposition chain (README §"Cross-Border
Relationships"), and this is a Commission implementing act operationalising
one specific provision of the Directive at Union level, not a national
instrument transposing it.

## Not modelled

Per-country publication of specific high-value datasets (e.g. which
national geospatial or company registers now publish under this
Regulation) is not researched. This entity records the Union-level
instrument only, matching [[EU-OPEN-DATA-DIRECTIVE]]'s own `coverage: low`
scope note.

## Relationships

- `implements` [[EU-OPEN-DATA-DIRECTIVE]] — Article 14(1), `confidence: high`.

## Sources

Listed in frontmatter, all three read directly this pass.
