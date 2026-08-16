---
id: EU-DGA
type: regulation
name: Data Governance Act
alternative_names:
  - DGA
  - Regulation (EU) 2022/868
  - European Data Governance Act
description: >
  EU regulation on European data governance, establishing a cross-sectoral
  framework for data access and sharing — covering reuse of protected
  public-sector data, data intermediation services, and data altruism. In
  force from 23 June 2022 and applicable from 24 September 2023.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2023-09-24
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DATA-STRATEGY
  - EU-DIGITAL-OMNIBUS
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "As an EU regulation the DGA is directly applicable in all member states; it entered into force 23 June 2022 and applies from 24 September 2023 (EUR-Lex ELI reg/2022/868). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-09-24
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "As an EU regulation the DGA is directly applicable in all member states, Germany included; it entered into force 23 June 2022 and applies from 24 September 2023 (EUR-Lex ELI reg/2022/868). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-09-24
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "As an EU regulation the DGA is directly applicable in all member states, Belgium included; it entered into force 23 June 2022 and applies from 24 September 2023 (EUR-Lex ELI reg/2022/868). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-09-24
    valid_until: null
  - type: implements
    target: EU-DATA-STRATEGY
    source: interpretation
    evidence: "The data strategy's first pillar is a cross-sectoral governance framework for data access and use, which the DGA gives legal effect to. No source read states this directly; recorded as Atlas interpretation."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2022/868 — Official Journal"
    url: "https://eur-lex.europa.eu/eli/reg/2022/868/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "Regulation (EU) 2022/868 — summary"
    url: "https://eur-lex.europa.eu/legal-content/EN/LSU/?uri=CELEX%3A32022R0868"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "European Data Governance Act (DGA), Regulation (EU) 2022/868"
    url: "https://www.oecd.org/en/publications/access-to-public-research-data-toolkit_a12e8998-en/european-data-governance-act-dga-regulation-eu-2022-868_920b8b28-en.html"
    publisher: "OECD"
---

# Data Governance Act (Regulation (EU) 2022/868)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Data Governance Act establishes a cross-sectoral framework for data
access and sharing across the EU. It entered into force on 23 June 2022 and
has applied since 24 September 2023 — the applicability date is recorded as
`start_date`, since that is when obligations began to bite.

It is the legal counterpart to the first pillar of [[EU-DATA-STRATEGY]]:
a cross-sectoral governance framework for data access and use.

## ⚠ A repeal has been proposed

[[EU-DIGITAL-OMNIBUS]], the Commission proposal of 19 November 2025,
proposes to **repeal this regulation entirely**, transferring its provisions
into [[EU-DATA-ACT]].

**`status` remains `active`.** The Omnibus is a proposal that has been sent
to the European Parliament and Council; adoption is reported as expected
around the end of 2026 and had not occurred at the time of writing. Marking
this regulation `superseded` on the strength of a proposal would be exactly
the kind of premature status inference the metadata schema prohibits.

The relationship is recorded from the Omnibus side using
`proposes-to-supersede` — a relationship type added in Batch 8 precisely so
that pending repeals are visible in the graph without falsely retiring the
instruments they target.

## Relationships

- Applies in [[NL]], [[DE]] and [[BE]] — one entity, three
  countries. Every other member state belongs here too; the
  `applies-in` relationships are added as countries join the Atlas.
- Gives legal effect to pillar 1 of [[EU-DATA-STRATEGY]] (Atlas
  interpretation).
- Targeted for repeal by [[EU-DIGITAL-OMNIBUS]] (recorded on that entity).

## Sources

Listed in frontmatter.
