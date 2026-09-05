---
id: UN-CCL
type: standard
name: UN/CEFACT Core Components Library
alternative_names:
  - UN/CCL
  - Core Components Library
description: >
  Standardized set of Core Components and Business Information Entities
  maintained by UN/CEFACT, used as the business-semantics building blocks
  for its reference data models and business messages covering
  cross-border trade (procurement, transport and payment processes). Split
  into an UN/CEFACT Message Components Library (validated components) and
  an UN/CEFACT Reference Components Library (harmonised components,
  including all message components), with new versions released twice a
  year.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains: []
organisations:
  - UN-CEFACT
related_entities:
  - UN-CEFACT
  - UN-UNECE
  - UN-EDIFACT
  - UN-LOCODE
relationships:
  - type: maintained-by
    target: UN-CEFACT
    source: fact
    evidence: "Confirmed by reading interoperable-europe.ec.europa.eu's own UN/CEFACT solution page directly (2026-09-05, reached via a 301 redirect from joinup.ec.europa.eu — unece.org itself remains 403-blocked this session, as it was for UN-EDIFACT and UN-LOCODE): 'The library is maintained by UN/CEFACT (United Nations Centre for Trade Facilitation and Electronic Business), part of the United Nations Economic Commission for Europe.' The page names two sub-libraries — the Message Components Library, maintained by the Bureau Programme Support Validation Domain, and the Reference Components Library, maintained by the Bureau Programme Support Library Maintenance Domain — and states new versions are released twice a year."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Core Components Library (UN/CCL)"
    url: "https://interoperable-europe.ec.europa.eu/collection/uncefact/solution/core-compenents-library-unccl"
    publisher: "European Commission — Interoperable Europe Portal (mirroring UN/CEFACT content)"
    accessed: "2026-09-05"
---

# UN/CEFACT Core Components Library (UN/CCL)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` and [[UN-EDIFACT]]'s own file had both
> previously declined to create this entity: "nothing beyond a name was
> found, and a node built on that would be the thin encyclopedic entity
> the taxonomy threshold exists to prevent." This pass found real
> substance on `interoperable-europe.ec.europa.eu` (reached via a
> redirect from `joinup.ec.europa.eu`, since `unece.org` itself remains
> 403-blocked this session) and read it directly.

## Description

The UN/CCL is "a standardized set of Core Components and Business
Information Entities," per the page read directly — the business-
semantics building blocks UN/CEFACT uses to develop reference data models
and business messages for cross-border trade (the "Buy, Ship, Pay"
processes: procurement, transport and payment). It is split into two
parts: the **UN/CEFACT Message Components Library** (validated
components) and the **UN/CEFACT Reference Components Library**
(harmonised components, including all message components). New versions
are released **twice a year**.

## Same cluster as UN/EDIFACT and UN/LOCODE

This completes the trio [[UN-EDIFACT]]'s own file named as "the actual
UN/CEFACT outputs" when only two of the three existed. Like [[UN-EDIFACT]],
this entity carries a single relationship — `maintained-by` [[UN-CEFACT]] —
and no sourced connection into the European layer was found this pass, so
none is asserted; `coverage: low` reflects that honestly, matching
[[UN-EDIFACT]]'s own precedent rather than overstating what one page
supports.

## Relationships

- `maintained-by` [[UN-CEFACT]].

## Sources

Listed in frontmatter, read directly this pass.
