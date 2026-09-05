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
last_verified: "2026-09-05"
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
  - title: "De EDI-wallet Identiteit"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/identiteit/edi-wallet/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-05"
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

## Status reasoning — confirmed still correct, 2026-09-05

`status: planned` is retained, and this pass confirms it directly rather
than by absence of evidence. Reading digitaleoverheid.nl's own EDI-wallet
page directly: the Dutch **"publieke NL-wallet"** — "moet een toegankelijke
en betrouwbare digitale oplossing zijn voor alle gebruikers" — is
explicitly "nog in ontwikkeling en komt later beschikbaar" (still in
development and becomes available later). Its national implementing
legislation is still being prepared and was expected to go to public
consultation only by the end of 2026 — meaning the Dutch wallet is likely
to arrive **after** the EU-wide end-2026 deadline this entity's own
`description` records, not by it. No source read states any member state
has a wallet in production.

The conservative reading was the right call: `active` would have asserted
deployment that had not happened, and still has not.

## Dutch relevance — now sourced

The Netherlands must provide a wallet like every member state, and the
Dutch effort now has a name and a direct source: the **publieke NL-wallet**,
confirmed on digitaleoverheid.nl's own page (2026-09-05). No relationship
is asserted from this entity to a Dutch counterpart yet — the NL-wallet
itself is not a separate Atlas entity, and creating one for an
"in ontwikkeling, komt later beschikbaar" initiative with no production
timeline would be premature. The obvious Dutch counterparts remain the
identity services within [[NL-GDI]] operated by [[NL-LOGIUS]], and the
assurance-level regime in [[NL-WDO]].

## Relationships

- Based on [[EU-EIDAS2]].

## Sources

Listed in frontmatter — now official EU sources.
