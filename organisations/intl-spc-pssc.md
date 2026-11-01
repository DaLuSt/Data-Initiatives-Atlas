---
id: INTL-SPC-PSSC
type: organisation
name: "Pacific Statistics Standing Committee (PSSC)"
alternative_names:
  - "PSSC"
description: >
  The regional body that oversees the implementation of Pacific statistics strategies, first set up by the 3rd Regional Conference of
  Heads of Planning and Statistics (HOPS) in 2010 and renamed in 2017 as an official subsidiary body of HOPS. It is a decision-making
  body empowered to make recommendations to HOPS; its members are Government Statisticians of eleven countries and territories,
  with Samoa in the chair; the SPC Statistics for Development Division provides its secretariat. Its sixth meeting was held in Nadi,
  Fiji on 24-25 September 2026.

level: regional
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - INTL-SPC-SDD
related_entities:
  - INTL-SPC-SDD
  - INTL-SPC-STATS-FRAMEWORK
relationships:
  - type: related-to
    target: INTL-SPC-SDD
    source: fact
    evidence: "The Committee's page on the Division's site (read directly 2026-11-01): 'Secretariat services are provided by the Statistics for Development Division (SDD) of SPC.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-SPC-STATS-FRAMEWORK
    source: fact
    evidence: "The same page: its main purpose is 'to oversee the implementation of Pacific Statistics Strategies, including the Ten-Year Pacific Statistics Strategy (TYPSS) 2010-2020 and the Strategic Framework for the Pacific Statistics 2022-2030'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Pacific Statistics Standing Committee (PSSC) — SDD"
    url: "https://sdd.spc.int/pacific-statistics-standing-committee-pssc"
    publisher: "Pacific Community (SPC)"
    accessed: "2026-11-01"
---

# Pacific Statistics Standing Committee (PSSC)

> **Created 2026-11-01** (roadmap #559-#561). One page read directly. `start_date` is empty: the page says it was established by the 3rd Regional Conference of HOPS "in 2010" without a day. The Heads of Planning and Statistics conference itself is not modelled, and the page does not place the Committee inside SPC, so it carries no `part-of` edge.

## Relationships

Secretariat [[INTL-SPC-SDD]]; oversees [[INTL-SPC-STATS-FRAMEWORK]].
