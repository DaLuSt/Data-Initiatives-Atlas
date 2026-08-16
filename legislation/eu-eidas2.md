---
id: EU-EIDAS2
type: regulation
name: European Digital Identity Framework Regulation
alternative_names:
  - eIDAS 2.0
  - Regulation (EU) 2024/1183
  - EUDI Regulation
description: >
  Regulation (EU) 2024/1183 of 11 April 2024, amending Regulation (EU) No
  910/2014 to establish the European Digital Identity Framework. Its central
  reform is an EU-wide framework for European Digital Identity Wallet
  schemes, which member states must provide by the end of 2026.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2024-05-20
end_date: null
last_verified: null
previous_version: EU-EIDAS
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EIDAS
  - EU-EUDI-WALLET
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "The Regulation mandates all Member States to provide European Digital Identity Wallets by the end of 2026 (Reg. (EU) 2024/1183; EUR-Lex ELI reg/2024/1183). NOT READ — search-only."
    confidence: medium
    valid_from: 2024-05-20
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "The Regulation mandates all Member States, Germany included, to provide European Digital Identity Wallets by the end of 2026 (Reg. (EU) 2024/1183; EUR-Lex ELI reg/2024/1183). NOT READ — search-only. Germany's BundID/DeutschlandID is recorded in this Atlas but is NOT asserted to implement this regulation — no source read connects them."
    confidence: medium
    valid_from: 2024-05-20
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "The Regulation mandates all Member States, Belgium included, to provide European Digital Identity Wallets by the end of 2026 (Reg. (EU) 2024/1183; EUR-Lex ELI reg/2024/1183). NOT READ — search-only. No Belgian digital identity scheme is recorded in this Atlas."
    confidence: medium
    valid_from: 2024-05-20
    valid_until: null
  - type: produces
    target: EU-EUDI-WALLET
    source: fact
    evidence: "The most important reform of Regulation 910/2014 introduced by this Regulation is the establishment of an EU-wide framework for European Digital Identity Wallet schemes (EUR-Lex; European Commission digital-building-blocks). NOT READ — search-only."
    confidence: medium
    valid_from: 2024-05-20
    valid_until: null

sources:
  - title: "Regulation (EU) 2024/1183 — Official Journal"
    url: "https://eur-lex.europa.eu/eli/reg/2024/1183/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "Regulation (EU) 2024/1183 — OJ L text (HTML)"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401183"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "The European Digital Identity Regulation"
    url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/EUDIGITALIDENTITYWALLET/pages/915931811/The+European+Digital+Identity+Regulation"
    publisher: "European Commission — Digital Building Blocks"
---

# European Digital Identity Framework Regulation (eIDAS 2.0)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Rebuilt in Batch 8

Batch 7 created this entity from secondary sources only — law-firm articles,
a vendor blog and Wikipedia — and flagged it as needing rebuilding. **It has
been rebuilt here on the EUR-Lex Official Journal text and the Commission's
own Digital Building Blocks page.** The regulation number and the entry into
force date reported in Batch 7 are corroborated; the adoption and
publication dates are new.

## Description

Regulation (EU) 2024/1183 amends [[EU-EIDAS]] (Regulation (EU) No 910/2014)
to establish the European Digital Identity Framework. It was adopted on
11 April 2024, published in the Official Journal on 30 April 2024, and
entered into force on 20 May 2024 — the date recorded as `start_date`.

Its core objective is to let EU citizens, residents and businesses
participate in the digital society with trusted, standardised digital
identification across the Union. The most significant reform it introduces
is an EU-wide framework for [[EU-EUDI-WALLET]] schemes: secure electronic
identification tools allowing individuals to store, manage and share
identity data and electronic attestations for public and private services
across borders. Member states are mandated to provide wallets **by the end
of 2026**.

By 21 November 2024 the Commission was to establish, by implementing acts, a
list of reference standards and, where necessary, specifications and
procedures for wallet implementation. Five implementing regulations are
reported to have been adopted on 28 November 2024, covering wallet
integrity and core functionality, person identification data and electronic
attestations of attributes, interoperability protocols, Commission
notifications, and certification of wallet solutions. Those implementing
acts are not modelled as entities.

## Amendment, not replacement

This regulation **amends** rather than repeals [[EU-EIDAS]]. `previous_version`
points at 910/2014 to record the lineage, but no `supersedes` relationship
is asserted in either direction, because the amended 910/2014 remains the
operative instrument as modified. This differs from the
[[EU-NIS]] → [[EU-NIS2]] case, which is an outright repeal.

## Relationships

- Amends [[EU-EIDAS]] (lineage recorded via `previous_version`).
- Produces / establishes [[EU-EUDI-WALLET]].
- Applies in [[NL]], [[DE]] and [[BE]] — one entity, three
  countries. Every other member state belongs here too; the
  `applies-in` relationships are added as countries join the Atlas.

## Sources

Listed in frontmatter — now including the Official Journal text.
