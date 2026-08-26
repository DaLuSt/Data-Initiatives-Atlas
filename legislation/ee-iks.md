---
id: EE-IKS
type: law
name: Isikuandmete kaitse seadus
alternative_names:
  - Personal Data Protection Act
  - IKS
description: >
  Estonian act implementing the General Data Protection Regulation, which
  entered into force on 15 January 2019 — nearly eight months after the
  Regulation itself became applicable on 25 May 2018.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2019-01-15
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EE
  - EU-GDPR
  - EE-AKI
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading all three cited pages directly (2026-08-26). gdprhub.eu states plainly: 'In Estonia the GDPR is implemented by the Isikuandmete kaitse seadus.' linklaters.com confirms the dates verbatim: 'The GDPR has applied since 25 May 2018. The Personal Data Protection Act entered into force on 15 January 2019.' whitecase.com corroborates the same date and adds a second act this entity did not previously carry: 'Personal Data Protection Act Implementation Act — Date in force: 15 March 2019' — a follow-on implementing act, not modelled as its own entity."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: EE
    source: fact
    evidence: "Confirmed by reading gdprhub.eu directly (2026-08-26): 'The Estonian Data Protection Inspectorate (Andmekaitse Inspektsioon) is the national data protection authority for Estonia.' Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Data Protection in Estonia"
    url: "https://gdprhub.eu/Data_Protection_in_Estonia"
    publisher: "GDPRhub"
    accessed: "2026-08-26"
  - title: "Data Protected — Estonia"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---estonia"
    publisher: "Linklaters"
    accessed: "2026-08-26"
  - title: "GDPR Guide to National Implementation: Estonia"
    url: "https://www.whitecase.com/insight-our-thinking/gdpr-guide-national-implementation-estonia"
    publisher: "White & Case LLP"
    accessed: "2026-08-26"
---

# Isikuandmete kaitse seadus

> **Verified 2026-08-26.** All three cited pages were read directly and
> confirm the 15 January 2019 date verbatim. White & Case's page
> surfaced a second, related act this entity did not previously carry:
> a Personal Data Protection Act Implementation Act, in force 15 March
> 2019 — mentioned here in prose rather than given its own entity.

## Description

Estonia's implementation of [[EU-GDPR]], **in force 15 January 2019**.
A related follow-on act — the Personal Data Protection Act
Implementation Act — entered into force two months later, on **15
March 2019**; it is not modelled as a separate Atlas entity.

## Nearly eight months after the Regulation applied

The GDPR became applicable on **25 May 2018**. The Estonian act entered into
force on **15 January 2019** — a gap of almost eight months in which the
Regulation bound Estonia directly while the national specifications did not
exist.

That is not the same failure as a missed transposition deadline: a
regulation applies of its own force, so nothing was un-protected. What was
missing were the derogations and specifications the GDPR *permits* a member
state to make. The Atlas holds seven other national GDPR instruments and
this is the only one where a date this far after 25 May 2018 is recorded.

## Relationships

- `implements-requirement-from` [[EU-GDPR]].
- [[EE-AKI]] is the supervisory authority; that edge runs from the
  authority, matching [[PT-CNPD]] and the rest.

## Sources

Listed in frontmatter, all three read directly this pass.

