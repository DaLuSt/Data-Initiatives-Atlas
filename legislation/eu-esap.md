---
id: EU-ESAP
type: regulation
name: European single access point
alternative_names:
  - ESAP
  - Regulation (EU) 2023/2859
description: >
  EU regulation establishing a European single access point (ESAP)
  providing centralised, free electronic access to publicly available
  information of relevance to financial services, capital markets and
  sustainability, adopted 13 December 2023 and published 20 December
  2023. The European Securities and Markets Authority (ESMA) is
  instructed to establish and operate it, with the platform required to
  be operational by 10 July 2027. It is the second of the three named
  components of the common European financial data space, alongside
  FIDA (open finance) and the modernisation of supervisory reporting.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2024-01-09
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-FINANCIAL-DATA-SPACE
  - EU-FIDA
relationships:
  - type: part-of
    target: EU-FINANCIAL-DATA-SPACE
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #122 (two-thirds). EUR-Lex's own text of the 2020 Digital Finance Strategy communication (COM(2020) 591, read directly 2026-09-18) names, in its section 4.3, three actions toward the common financial data space: 'Facilitating real-time digital access to all regulated financial information' (this entity, ESAP), 'Promoting innovative IT tools to facilitate reporting and supervision' (the separate supervisory-reporting-modernisation strand, not modelled as its own entity — see EU-FINANCIAL-DATA-SPACE's own file), and 'Promoting business-to-business data sharing in the EU financial sector and beyond (open finance)' — already modelled as EU-FIDA. EUR-Lex's own summary of Regulation (EU) 2023/2859, also read directly, confirms this entity's own details: adopted 13 December 2023, published 20 December 2023, entered into force 9 January 2024, with ESMA instructed to establish and operate the platform by 10 July 2027."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "European single access point — summary"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/european-single-access-point.html"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-09-18"
  - title: "Strategy on supervisory data in EU financial services (2020 Digital Finance Strategy, COM(2020) 591)"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52020DC0591"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-09-18"
---

# European single access point (ESAP)

> **Created 2026-09-18**, closing two-thirds of `discovery/unresolved.md`
> row #122: [[EU-FINANCIAL-DATA-SPACE]]'s own entity named FIDA as "one
> of three components" without identifying the other two. EUR-Lex's own
> text of the 2020 Digital Finance Strategy communication, read directly,
> names all three in the Commission's own words. This entity models the
> second.

## Description

Regulation (EU) 2023/2859, read directly via EUR-Lex's own summary,
establishes the **European single access point (ESAP)**: centralised,
free electronic access to publicly available information relevant to
financial services, capital markets and sustainability. It was **adopted
13 December 2023**, **published 20 December 2023**, and **entered into
force 9 January 2024**.

The regulation instructs the **European Securities and Markets Authority
(ESMA)** to establish and operate the platform, required to be
**operational by 10 July 2027**, with further phased milestones running
to 2030 (technical standards, Member State collection-body designations,
voluntary then eventual entity submissions).

## The three components of the financial data space, now two of three named

[[EU-FINANCIAL-DATA-SPACE]]'s own entity described [[EU-FIDA]] as "one of
three components" without naming the other two — the gap
`discovery/unresolved.md` row #122 flagged. The Commission's own 2020
Digital Finance Strategy communication, read directly this pass at
EUR-Lex, names all three in section 4.3:

| # | Action (Commission's own words) | Atlas entity |
|---|---|---|
| 1 | "Facilitating real-time digital access to all regulated financial information" | **This entity (ESAP)** |
| 2 | "Promoting innovative IT tools to facilitate reporting and supervision" | Not modelled — see below |
| 3 | "Promoting business-to-business data sharing in the EU financial sector and beyond (open finance)" | [[EU-FIDA]] |

## The third component, deliberately not modelled

The supervisory-reporting-modernisation strand is real and sourced — the
Commission adopted a dedicated "Strategy on supervisory data in EU
financial services" (COM(2021) 798) on 15 December 2021, and published a
progress report on 29 February 2024. It is not given its own Atlas entity
here: unlike ESAP and FIDA, it is not itself a Regulation or a proposed
one, but an ongoing policy strategy pursued through multiple staff working
documents and progress reports without one citable legal instrument.
Creating an entity for it would mean picking one of several Commission
documents to stand in for an open-ended strategy, which is a different
kind of thing from what `type: law`/`type: regulation` model elsewhere in
the Atlas. Recorded here in prose instead, with its own communication
cited, so the third component is at least named rather than left as an
unlabelled gap.

## Relationships

- `part-of` [[EU-FINANCIAL-DATA-SPACE]] — see above.

## Sources

Two sources, both read directly: EUR-Lex's own summary of Regulation (EU)
2023/2859, and EUR-Lex's own text of the 2020 Digital Finance Strategy
communication that names all three components.
