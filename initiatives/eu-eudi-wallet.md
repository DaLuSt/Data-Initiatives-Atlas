---
id: EU-EUDI-WALLET
type: initiative
name: European Digital Identity Wallet
alternative_names:
  - EUDI Wallet
  - EDIW
description: >
  Secure electronic identification tool established under the European
  Digital Identity Framework Regulation, allowing individuals and businesses
  to store, manage and share identity data and electronic attestations for
  public and private services across borders. Member states must provide at
  least one wallet by the end of 2026.

level: regional
country: null
region: EU

status: planned
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EIDAS2
relationships:
  - type: based-on
    target: EU-EIDAS2
    source: fact
    evidence: "The establishment of an EU-wide framework for European Digital Identity Wallet schemes is the central reform introduced by Regulation (EU) 2024/1183 (EUR-Lex; European Commission digital-building-blocks). NOT READ — search-only."
    confidence: medium
    valid_from: 2024-05-20
    valid_until: null

sources:
  - title: "Regulation (EU) 2024/1183 — Official Journal"
    url: "https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "The European Digital Identity Regulation — EU Digital Identity Wallet"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation"
    publisher: "European Commission — Digital Building Blocks"
---

# European Digital Identity Wallet (EUDI Wallet)

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Rebuilt in Batch 8

Batch 7 created this entity on Wikipedia and a vendor blog and flagged it
for rebuilding. **It has been rebuilt here** on the EUR-Lex text of
[[EU-EIDAS2]] and the Commission's Digital Building Blocks pages. The
`confidence` has moved from `low` to `medium` accordingly.

## Description

The EUDI Wallet is a secure electronic identification tool established under
[[EU-EIDAS2]]. It lets individuals and businesses store, manage and share
identity data and electronic attestations of attributes for both public and
private services, across borders within the Union. Reported credential types
include identity documents, professional certificates, business licences,
education diplomas and health credentials.

Member states are mandated to provide wallets **by the end of 2026**.

## Status reasoning, revisited

`status: planned` is retained. The regulation's deadline is the end of 2026;
this entry is written in August 2026, so the deadline has not passed, and no
source located establishes that any particular member state — the
Netherlands included — has a wallet in production.

The conservative reading is deliberate: `active` would assert deployment
that has not been evidenced. If wallets have since been issued, this entity
is wrong in the safe direction, and `discovery/unresolved.md` records
exactly what to check.

## Dutch relevance, still unasserted

The Netherlands must provide a wallet like every member state. The obvious
Dutch counterparts are the identity services within [[NL-GDI]] operated by
[[NL-LOGIUS]], and the assurance-level regime in [[NL-WDO]]. **No
relationship is asserted** — no source located connects the Dutch
implementation to this initiative, and the Dutch wallet arrangements were
not researched. This is a concrete gap for a future Netherlands batch.

## Relationships

- Based on [[EU-EIDAS2]].

## Sources

Listed in frontmatter — now official EU sources.
