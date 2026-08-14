---
id: EU-EUDI-WALLET
type: initiative
name: European Digital Identity Wallet
alternative_names:
  - EUDI Wallet
  - EU Digital Identity Wallet
description: >
  Standardised, government-issued digital identity application to be made
  available to EU citizens, residents and businesses under the European
  Digital Identity Regulation. Every member state must provide at least one
  wallet, with the practical deadline reported as late 2026.

level: regional
country: null
region: EU

status: planned
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
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
    evidence: "The EUDI Wallet is the flagship component of Regulation (EU) 2024/1183, which introduces it (multiple secondary sources). NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "EU Digital Identity Wallet"
    url: "https://en.wikipedia.org/wiki/EU_Digital_Identity_Wallet"
    publisher: "Wikipedia"
  - title: "EUDI Wallet: how prepared are the various EU countries?"
    url: "https://www.namirial.com/en/blog/stories/status-check-eudi-wallet/"
    publisher: "Namirial"
---

# European Digital Identity Wallet (EUDI Wallet)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The EUDI Wallet is a standardised, government-issued digital identity
application to be made available to every EU citizen, resident and business
under [[EU-EIDAS2]]. It is described as a secure mobile app in which
individuals and businesses can store, manage and present digital
credentials — identity documents, professional certificates, business
licences, education diplomas, health credentials and more.

Member states must provide at least one wallet within 24 months of the
implementing acts, giving a reported practical deadline of late 2026. Large
online platforms and organisations in regulated sectors must then accept the
wallet as an authentication method within a further year.

## Status reasoning

`status: planned` rather than `active`. As at this entry's date
(August 2026) the reported member-state deadline of "late 2026" has not yet
passed, and no source located established that wallets are in production in
any particular member state — including the Netherlands.

This is deliberately conservative: `active` would assert deployment that has
not been evidenced. If the rollout has since occurred, the status is wrong
in the safe direction, and the `discovery/unresolved.md` entry says what to
check.

## Sourcing weakness

As with [[EU-EIDAS2]], **no official EU source was located** — citations are
Wikipedia and a vendor blog. This entity should be treated as a placeholder
carrying a real concept rather than as researched content, and rebuilt in
Batch 8 from the Commission's own material.

## Dutch relevance, unasserted

The Netherlands must provide a wallet like every member state, and the
obvious Dutch counterparts are the identity services within [[NL-GDI]]
operated by [[NL-LOGIUS]], plus the assurance-level regime in [[NL-WDO]].
No relationship is asserted: no source located connects them.

## Relationships

- Based on [[EU-EIDAS2]].

## Sources

Listed in frontmatter. **Both are secondary sources.**
