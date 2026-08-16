---
id: EU-EHDS
type: data-space
name: European Health Data Space
alternative_names:
  - EHDS
  - Regulation (EU) 2025/327
description: >
  The EU health data space, established by Regulation (EU) 2025/327. It
  governs secondary use of health data for research, innovation,
  policymaking and regulation, with member states creating health data
  access bodies to manage it. In force from 26 March 2025, applying in
  phases from 2027.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2025-03-26
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - NL-HEALTH-RI
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Health is one of the 14 common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21; digital-strategy.ec.europa.eu data-spaces). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "As an EU regulation it is directly applicable in all member states; EU countries create health data access bodies during the 2027-2029 preparation phase (Reg. (EU) 2025/327; multiple legal analyses). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-03-26
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "As an EU regulation it is directly applicable in all member states, Germany included; EU countries create health data access bodies during the 2027-2029 preparation phase (Reg. (EU) 2025/327; multiple legal analyses). NOT READ — search-only. No German health data access body or implementing instrument is recorded in this Atlas."
    confidence: medium
    valid_from: 2025-03-26
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "As an EU regulation it is directly applicable in all member states, Belgium included; EU countries create health data access bodies during the 2027-2029 preparation phase (Reg. (EU) 2025/327). NOT READ — search-only. No Belgian health data access body is recorded in this Atlas."
    confidence: medium
    valid_from: 2025-03-26
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "As an EU regulation it is directly applicable in all member states, France included; EU countries create health data access bodies during the 2027-2029 preparation phase (Reg. (EU) 2025/327). NOT READ — search-only. No French health data access body is recorded in this Atlas."
    confidence: medium
    valid_from: 2025-03-26
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "As an EU regulation it is directly applicable in all member states, Spain included; EU countries create health data access bodies during the 2027-2029 preparation phase (Reg. (EU) 2025/327). NOT READ - search-only. No Spanish health data access body is recorded in this Atlas."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: PL
    source: fact
    evidence: "As an EU regulation it is directly applicable in all member states, Poland included; EU countries create health data access bodies during the 2027-2029 preparation phase (Reg. (EU) 2025/327). NOT READ - search-only. No Polish health data access body is recorded in this Atlas."
    confidence: medium
    valid_from: 2025-03-26
    valid_until: null

sources:
  - title: "European Health Data Space — legislative procedure file"
    url: "https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1805726"
    publisher: "European Parliament — Legislative Observatory"
  - title: "European Health Data Space"
    url: "https://en.wikipedia.org/wiki/European_Health_Data_Space"
    publisher: "Wikipedia"
  - title: "Regulation (EU) 2025/327: Establishing the European Health Data Space (EHDS)"
    url: "https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-2025-327-establishing-ehds"
    publisher: "EY"
---

# European Health Data Space (EHDS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The EHDS is established by Regulation (EU) 2025/327, published in the
Official Journal on 5 March 2025 and in force from **26 March 2025**. It is
the most legally developed of the common European data spaces — the only one
of the fourteen with its own regulation.

It covers **secondary use** of health data: allowing researchers, companies
and regulators to use large volumes of health data to develop treatments,
train AI systems and improve healthcare efficiency. Governance runs through
**health data access bodies (HDABs)**, which member states must establish.

## Phased application

| Date | Milestone |
|---|---|
| 26 March 2025 | Entry into force |
| 2025–2027 | Commission drafts implementing and delegated acts |
| 26 March 2027 | General date of application |
| 2027–2029 | Member states create data hubs / HDABs |
| 26 March 2029 | Most secondary-use provisions apply |
| 2031, 2035 | Further milestones |

`status: active` means in force, not fully applicable — most substantive
secondary-use obligations land in 2029. As with [[EU-AI-ACT]], a staged
timetable makes `last_verified` load-bearing.

## The Dutch connection, not yet asserted

[[NL-HEALTH-RI]] is the Netherlands' national health data infrastructure for
research and innovation — federated, with regional nodes around a central
hub, governed by an afsprakenstelsel. It is the obvious candidate to become
or host the Dutch HDAB.

**No relationship is asserted.** No source read connects Health-RI to the
EHDS or names it as the designated Dutch body, and the HDAB designation
phase (2027–2029) had not begun at the time of writing. This is one of the
highest-value open questions in the Atlas: it would complete an
EU-regulation → national-infrastructure chain in the health domain.

## Modelling note

The EHDS is recorded as **one entity typed `data-space`**, not split into a
regulation plus a data space, even though Regulation (EU) 2025/327 is
substantial legislation. The reasoning matches [[NL-BIO]] and
[[NL-HEALTH-RI]]: the regulation and the space it establishes share one
name and one identity in the sources. If a future batch needs to cite the
regulation as legislation in its own right, it should be split. Flagged in
`discovery/unresolved.md`.

**No EUR-Lex citation was located** — the strongest source is the European
Parliament's Legislative Observatory file. Queued.

## Relationships

- Part of [[EU-COMMON-DATA-SPACES]].
- Applies in [[NL]], [[DE]], [[BE]], [[FR]], [[ES]] and [[PL]] — one entity, six
  countries. Every other member state belongs here too; the
  `applies-in` relationships are added as countries join the Atlas.

## Sources

Listed in frontmatter.
