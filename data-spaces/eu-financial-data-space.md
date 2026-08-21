---
id: EU-FINANCIAL-DATA-SPACE
type: data-space
name: Common European financial data space
alternative_names:
  - Financial data space
  - Finance data space
description: >
  One of the fourteen common European data spaces, covering finance. The
  Commission's proposal for a framework for Financial Data Access (FIDA)
  is one of three components of it, establishing rights and obligations
  for managing customer data sharing in the financial sector beyond
  payment accounts.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Finance is one of the fourteen common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21 final of 24.1.2024; digital-strategy.ec.europa.eu 'Common European data spaces'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SWD(2024) 21 final — Staff working document on common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/library/staff-working-document-data-spaces"
    publisher: "European Commission"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
---

# Common European financial data space

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

One of the fourteen common European data spaces, covering finance.
The Commission's proposal for a framework for Financial Data Access (FIDA) is one of three components of it, establishing rights and obligations for managing customer data sharing in the financial sector beyond payment accounts.

## The only one of the fourteen with a named legislative component

The Commission describes its **Financial Data Access (FIDA)** proposal as
**one of three components** of the financial data space, establishing rights
and obligations for customer data sharing in finance **beyond payment
accounts** — that is, extending past what PSD2 already opened.

That makes finance the second sector, after health, where a common European
data space has legislation attached rather than only funding and governance.
[[EU-EHDS]] is backed by a Regulation and carries `applies-in` edges to eight
countries; this one is not yet, and does not.

## ⚠ FIDA is not modelled, and the other two components are unknown

The sources name FIDA as one of three components and **do not name the other
two**. Creating a data space entity whose own description admits it is
one-third specified is unusual, and it is done deliberately: leaving finance
out would break the set of fourteen, and the gap is more useful stated than
hidden.

- [ ] **FIDA** as a legislation entity, and the other two components.
- [ ] **PSD2**, the backdrop the sources implicitly contrast FIDA against.

Both are logged in `discovery/unresolved.md`.

## Sources

Listed in frontmatter.
