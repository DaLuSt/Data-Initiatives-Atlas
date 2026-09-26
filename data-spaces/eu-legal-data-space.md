---
id: EU-LEGAL-DATA-SPACE
type: data-space
name: European Legal Data Space
alternative_names:
  - ELDS
  - European legal data space
description: >
  One of the fourteen common European data spaces, launched by the
  European Commission on 31 October 2025 to make EU and national legal
  data — legislation, case law and justice-system data — more accessible,
  interoperable and reusable. Operated by the Publications Office of the
  European Union, it provides common standards built on the ELI
  (European Legislation Identifier) and ECLI (European Case Law
  Identifier) schemes, centralised collections of legislation and
  case-law linking to EU and national legal depositories, justice-system
  data via the European e-Justice Portal, and a EUR-Lex bulk data dump
  for research and application development.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2025-10-31
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-PUBLIC-ADMIN-DATA-SPACE
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "NARROWS discovery/unresolved.md row #125 (via EU-PUBLIC-ADMIN-DATA-SPACE's own 'Not modelled' section, which named the European Legal Data Space as 'not independently researched this pass'). Confirmed by reading data.europa.eu's own dedicated ELDS page directly (2026-09-26): 'one of the Common European Data Spaces designated to harness the value of data for the benefit of the European economy and society,' operated by the Publications Office of the European Union, providing common standards (ELI/ECLI identifiers), legislation/case-law collections, justice-system data via the European e-Justice Portal, and a EUR-Lex data dump. The Interoperable Europe Portal's own launch announcement, also read directly, confirms the 31 October 2025 launch date and describes the same four-part structure."
    confidence: high
    valid_from: "2025-10-31"
    valid_until: null
  - type: related-to
    target: EU-PUBLIC-ADMIN-DATA-SPACE
    source: fact
    evidence: "Confirmed by reading the European Commission's own 'Common European data spaces' overview page (already cited on [[EU-PUBLIC-ADMIN-DATA-SPACE]]), which lists the European Legal Data Space as one of three items under its 'Public administration' heading, alongside OOTS and PPDS. No source states a governance or dependency relationship beyond both being catalogued under the same data-space heading, so `related-to` rather than `part-of`."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "European Legal Data Space (ELDS)"
    url: "https://data.europa.eu/en/ELDS"
    publisher: "Publications Office of the European Union"
    accessed: "2026-09-26"
  - title: "The European Legal Data Space has been launched"
    url: "https://interoperable-europe.ec.europa.eu/collection/open-government/news/european-legal-data-space-has-been-launched"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-09-26"
---

# European Legal Data Space (ELDS)

> **Created 2026-09-26**, narrowing `discovery/unresolved.md` row #125
> via [[EU-PUBLIC-ADMIN-DATA-SPACE]]'s own "Not modelled" section, which
> had named this data space as one of the Commission's own listed items
> under public administration, "not independently researched this pass."
> Sourced from data.europa.eu's own dedicated ELDS page and the
> Interoperable Europe Portal's launch announcement, both read directly.

## Description

The European Legal Data Space is one of the **fourteen common European
data spaces**, **launched on 31 October 2025** by the European
Commission to make EU and national **legal information** — legislation,
case law and justice-system data — more accessible, interoperable and
reusable across Member States and EU bodies.

Confirmed directly on data.europa.eu's own dedicated page: it is
**operated by the Publications Office of the European Union**, and
provides four components:

- **Common standards**, built on the **ELI** (European Legislation
  Identifier) and **ECLI** (European Case Law Identifier) schemes.
- **Collections of legislation and case-law**, with access points to EU
  and national legal depositories.
- **Justice-system data**, via the **European e-Justice Portal**.
- A **EUR-Lex data dump**, for bulk downloading legal acts to support
  research and application development.

## One of three items under the public administration data space

The Commission's own "Common European data spaces" overview page lists
this data space alongside **OOTS** (Once Only Technical System) and
**PPDS** (Public Procurement Data Space) under its "Public
administration" heading — the same page already cited on
[[EU-PUBLIC-ADMIN-DATA-SPACE]]. No source read states a governance or
dependency relationship between them beyond this shared catalogue entry,
so `related-to` is recorded rather than `part-of`.

## Not modelled

- **ELI** and **ECLI**, the two identifier schemes this data space
  builds on — technical standards, not organisations or instruments in
  their own right.
- The **European e-Justice Portal** as a separate platform entity —
  described here in prose as the source of justice-system data.
- The **Publications Office of the European Union** as a separate
  organisation entity.

## Relationships

- `part-of` [[EU-COMMON-DATA-SPACES]] — `confidence: high`.
- `related-to` [[EU-PUBLIC-ADMIN-DATA-SPACE]] — `confidence: medium`,
  catalogued together, not a stated dependency.

## Sources

Listed in frontmatter, both read directly.
