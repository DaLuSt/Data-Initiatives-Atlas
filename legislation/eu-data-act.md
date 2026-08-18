---
id: EU-DATA-ACT
type: regulation
name: Data Act
alternative_names:
  - Regulation (EU) 2023/2854
  - EU Data Act
description: >
  EU regulation on harmonised rules on fair access to and use of data,
  published in the Official Journal on 13 December 2023 and applicable from
  12 September 2025. Under the Digital Omnibus proposal it would become the
  consolidated home of EU data legislation.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2025-09-12
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IE
  - EU-DATA-STRATEGY
  - EU-DIGITAL-OMNIBUS
relationships:
  - type: applies-in
    target: IE
    source: fact
    evidence: "As an EU regulation, Data Act is binding in its entirety and directly applicable in all member states without national transposition, and Ireland is a member state (eur-lex.europa.eu; digital-strategy.ec.europa.eu; consilium.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "As an EU regulation the Data Act is directly applicable in all member states; published in the OJ on 13 December 2023 and applicable from 12 September 2025 (EUR-Lex ELI reg/2023/2854). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-09-12
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "As an EU regulation the Data Act is directly applicable in all member states, Germany included; published in the OJ on 13 December 2023 and applicable from 12 September 2025 (EUR-Lex ELI reg/2023/2854). NOT READ — search-only. No German implementing or accompanying instrument is recorded in this Atlas."
    confidence: medium
    valid_from: 2025-09-12
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "As an EU regulation the Data Act is directly applicable in all member states, Belgium included; published in the OJ on 13 December 2023 and applicable from 12 September 2025 (EUR-Lex ELI reg/2023/2854). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-09-12
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "As an EU regulation the Data Act is directly applicable in all member states, France included; published in the OJ on 13 December 2023 and applicable from 12 September 2025 (EUR-Lex ELI reg/2023/2854). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-09-12
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "As an EU regulation the Data Act is directly applicable in all member states, Spain included; published in the OJ on 13 December 2023 and applicable from 12 September 2025 (EUR-Lex ELI reg/2023/2854). NOT READ - search-only."
    confidence: medium
    valid_from: 2025-09-12
    valid_until: null
  - type: applies-in
    target: PL
    source: fact
    evidence: "As an EU regulation the Data Act is directly applicable in all member states, Poland included; published in the OJ on 13 December 2023 and applicable from 12 September 2025 (EUR-Lex ELI reg/2023/2854). NOT READ - search-only."
    confidence: medium
    valid_from: 2025-09-12
    valid_until: null

sources:
  - title: "Regulation (EU) 2023/2854 (Data Act) — Official Journal"
    url: "https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# Data Act (Regulation (EU) 2023/2854)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Data Act sets harmonised rules on fair access to and use of data in the
EU. It was published in the Official Journal on 13 December 2023 and became
applicable on 12 September 2025, 20 months after entry into force. The
applicability date is recorded as `start_date`.

`coverage: medium`: the regulation's substantive content — its provisions on
IoT data access, cloud switching, and business-to-government data sharing —
was **not researched**. Only its identity, dates and position in the
legislative landscape are recorded here.

## ⚠ Central to a proposed consolidation

Under [[EU-DIGITAL-OMNIBUS]], this regulation would become the consolidated
home of EU data legislation: the proposal would repeal [[EU-DGA]], the
[[EU-OPEN-DATA-DIRECTIVE]] and the Free Flow of Non-Personal Data
Regulation, and **transfer those instruments into the Data Act**. The
Omnibus also proposes direct amendments to the Data Act itself.

If adopted, this would materially reshape the EU layer of the Atlas — three
entities retired and their substance folded into this one. That is a strong
argument for keeping the proposal visible in the graph now, which is what
the `proposes-to-supersede` relationship type added in Batch 8 does.

None of this changes any `status` today: the Omnibus is a proposal.

## Relationships

- Applies in [[NL]], [[DE]], [[BE]], [[FR]], [[ES]] and [[PL]] — one entity, six
  countries. Every other member state belongs here too; the
  `applies-in` relationships are added as countries join the Atlas.
- Would absorb [[EU-DGA]] and [[EU-OPEN-DATA-DIRECTIVE]] under
  [[EU-DIGITAL-OMNIBUS]] (recorded on that entity).
- Gives effect to parts of [[EU-DATA-STRATEGY]]; the specific pillar was not
  sourced, so no relationship is asserted — unlike [[EU-DGA]], where the
  pillar-1 mapping is clearer.

## Sources

Listed in frontmatter.
