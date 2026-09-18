---
id: EU-FIDA
type: law
name: Regulation on a framework for Financial Data Access
alternative_names:
  - FIDA
  - Financial Data Access Regulation
  - COM(2023) 360
description: >
  European Commission legislative proposal establishing rules for secure
  access to and sharing of customer data across the financial sector
  beyond payment accounts, building on the existing open-banking
  framework under PSD2. One of three named components of the common
  European financial data space. Proposed 28 June 2023 and, as of this
  pass, still moving through interinstitutional trilogue negotiations
  rather than adopted.

level: regional
country: null
region: EU

status: proposed
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-FINANCIAL-DATA-SPACE
  - EU-PSD2
relationships:
  - type: part-of
    target: EU-FINANCIAL-DATA-SPACE
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP — EU-FINANCIAL-DATA-SPACE's own entity named FIDA as 'one of three components' without modelling it, calling the data space 'one-third specified.' Confirmed by reading the European Commission's own finance.ec.europa.eu page directly (2026-09-05): 'The framework would establish clear rights and obligations to manage customer data sharing in the financial sector beyond payment accounts,' proposed 28 June 2023 as COM(2023) 360. eur-lex.europa.eu's own text of the proposal, also read directly, gives the full official title: 'Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on a framework for Financial Data Access and amending Regulations (EU) No 1093/2010, (EU) No 1094/2010, (EU) No 1095/2010 and (EU) 2022/2554,' dated 'Brussels, 28.6.2023.' The other two named components of the financial data space remain unidentified and unmodelled."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-PSD2
    source: fact
    evidence: "The Commission's own finance.ec.europa.eu FIDA page, read directly (2026-09-05, re-confirmed 2026-09-18), states FIDA is 'building on the existing open-banking framework under PSD2' and extends customer data-sharing rights 'beyond payment accounts' — i.e. beyond what PSD2's own open-banking mechanism already covers. PSD2 itself, previously unmodelled (discovery/unresolved.md row #123), is now [[EU-PSD2]]."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Framework for financial data access (FIDA)"
    url: "https://finance.ec.europa.eu/digital-finance/framework-financial-data-access_en"
    publisher: "European Commission — Finance"
    accessed: "2026-09-05"
  - title: "COM(2023) 360 final — Proposal for a Regulation on a framework for Financial Data Access"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A52023PC0360"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-09-05"
---

# Regulation on a framework for Financial Data Access (FIDA)

> **Created 2026-09-05**, closing part of the gap
> [[EU-FINANCIAL-DATA-SPACE]] itself flagged: "FIDA is not modelled, and
> the other two components are unknown." This entity models FIDA; the
> other two components remain unidentified.
>
> **Updated 2026-09-18**: PSD2, the open-banking framework this entity's
> own description already said FIDA builds on, is now [[EU-PSD2]] — see
> "Building on PSD2, now modelled" below, and `discovery/unresolved.md`
> row #123.

## Description

Confirmed by reading the European Commission's own finance.ec.europa.eu
page directly: FIDA "would establish clear rights and obligations to
manage customer data sharing in the financial sector beyond payment
accounts," building on the existing open-banking framework under PSD2
rather than replacing it. It was **proposed 28 June 2023**.

eur-lex.europa.eu's own text of the proposal, also read directly, gives
the full official title: "Proposal for a REGULATION OF THE EUROPEAN
PARLIAMENT AND OF THE COUNCIL on a framework for Financial Data Access
and amending Regulations (EU) No 1093/2010, (EU) No 1094/2010, (EU)
No 1095/2010 and (EU) 2022/2554" — **COM(2023) 360 final**, dated
"Brussels, 28.6.2023."

## Building on PSD2, now modelled

This entity's own description, from the first pass, already stated FIDA
is "building on the existing open-banking framework under PSD2." That
made PSD2 the one named point of comparison for FIDA's own scope that
had never been modelled itself — closed 2026-09-18 as [[EU-PSD2]], with
a `based-on` edge recorded here.

## Still a proposal, not yet adopted

`status: proposed` reflects the legislative stage as of this pass: a
WebSearch cross-check (not independently read against a primary
Parliament or Council source) indicates the proposal reached the
Parliament's negotiating mandate in December 2024 and the Council's
general approach the same month, moving into interinstitutional
trilogue negotiations. No source read this pass confirms final adoption,
so `start_date` (which would record entry into force) stays `null`.

## Two-thirds of the financial data space still unspecified

[[EU-FINANCIAL-DATA-SPACE]]'s own description names FIDA as "one of
three components." Neither of the other two is identified by any source
read this pass, and none is modelled here. This entity closes only the
named third that had a specific proposal to point to.

## Relationships

- `part-of` [[EU-FINANCIAL-DATA-SPACE]].

## Sources

Two sources, both read directly: the Commission's own FIDA page and
EUR-Lex's own text of COM(2023) 360.
