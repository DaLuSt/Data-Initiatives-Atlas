---
id: EU-EIDAS2
type: regulation
name: European Digital Identity Regulation
alternative_names:
  - eIDAS 2.0
  - Regulation (EU) 2024/1183
  - European Digital Identity Framework
description: >
  EU regulation amending the original eIDAS framework and establishing the
  European Digital Identity Framework, whose flagship component is the
  European Digital Identity Wallet. Entered into force on 20 May 2024.

level: regional
country: null
region: EU

status: active
confidence: low
coverage: low
verification: search-only

start_date: 2024-05-20
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EUDI-WALLET
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "By 2026 every EU member state must provide at least one European Digital Identity Wallet to citizens and companies, within 24 months of the implementing acts (multiple secondary sources). NOT READ — search-only."
    confidence: low
    valid_from: 2024-05-20
    valid_until: null

sources:
  - title: "EU Digital Identity Wallet"
    url: "https://en.wikipedia.org/wiki/EU_Digital_Identity_Wallet"
    publisher: "Wikipedia"
  - title: "The European Digital Identity Framework: introducing the new EU Digital Identity Wallet"
    url: "https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-european-digital-identity-framework-introducing-the-new-eu-digital-identity-wallet/"
    publisher: "Kennedys Law"
---

# European Digital Identity Regulation (eIDAS 2.0)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Regulation (EU) 2024/1183 replaces the original eIDAS Regulation and
establishes the European Digital Identity Framework, whose flagship
component is [[EU-EUDI-WALLET]]. It entered into force on 20 May 2024. Five
implementing regulations were adopted on 28 November 2024, covering wallet
integrity and core functionality, person identification data and electronic
attestations of attributes, protocols and interfaces for interoperability,
notifications to the Commission, and certification of wallet solutions.

## Sourcing weakness — read this before relying on the entity

`confidence: low` and `coverage: low` are doing real work here. **No
EUR-Lex or official EU source for this regulation was located in Batch 7
research** — the searches that surfaced it returned law-firm articles,
vendor blogs and Wikipedia. Every citation below is therefore secondary, and
the regulation number, dates and implementing-act details all rest on
secondary reporting.

This is materially weaker than the sourcing behind [[EU-GDPR]],
[[EU-NIS2]] and [[EU-OPEN-DATA-DIRECTIVE]], all of which have EUR-Lex
citations. Batch 8 must locate the authoritative text before this entity is
relied upon, and the `applies-in → NL` relationship is recorded at
`confidence: low` for the same reason.

## Bearing on the Dutch layer

This regulation is relevant to the open question on [[NL-WDO]] (whether the
Dutch digital government act has an EU origin), but **does not resolve it**
and may be a red herring: the Wdo came into force in July 2023, before
eIDAS 2.0 entered into force in May 2024. If the Wdo transposes anything, it
is more likely the *original* eIDAS Regulation (910/2014), which is not yet
an Atlas entity. Recorded in `discovery/unresolved.md`; no relationship is
asserted in either direction.

## Relationships

- Establishes [[EU-EUDI-WALLET]].
- Applies in [[NL]] (`confidence: low` — see above).

## Sources

Listed in frontmatter. **Both are secondary sources**, low in the README's
preference order.
