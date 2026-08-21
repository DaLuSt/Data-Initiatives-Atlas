---
id: INTL-ISO-IEC-27002
type: standard
name: "ISO/IEC 27002 — Information security controls"
alternative_names:
  - ISO 27002
  - "ISO/IEC 27002:2022"
  - NEN-EN-ISO/IEC 27002
description: >
  International standard on information security, cybersecurity and privacy
  protection, providing a set of information security controls. Published
  jointly by ISO and IEC under JTC 1/SC 27, and applied in a risk-driven way
  alongside ISO/IEC 27001.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - INTL-ISO
  - INTL-IEC
related_entities:
  - INTL-ISO-IEC-27001
  - NL-BIO
relationships:
  - type: maintained-by
    target: INTL-ISO
    source: fact
    evidence: "ISO/IEC 27002 is published by ISO and the IEC, titled 'Information security, cybersecurity and privacy protection — Information security controls', under JTC 1/SC 27 (iso.org; jtc1info.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ISO/IEC 27002 — Information technology — Security techniques — Code of practice for information security controls"
    url: "https://www.iso.org/obp/ui/#iso:std:iso-iec:27002:ed-2:en"
    publisher: "International Organization for Standardization (ISO)"
  - title: "ISO/IEC 27000 family — Information security management"
    url: "https://www.iso.org/standard/iso-iec-27000-family"
    publisher: "International Organization for Standardization (ISO)"
---

# ISO/IEC 27002

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `iso.org`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

ISO/IEC 27002 is titled *Information security, cybersecurity and privacy
protection — Information security controls*. It supplies the control set
applied alongside [[INTL-ISO-IEC-27001]]: where 27001 specifies ISMS
requirements, 27002 provides the controls to be selected on the basis of
assessed risk.

Published jointly by [[INTL-ISO]] and [[INTL-IEC]] under JTC 1/SC 27.

## An edition mismatch worth flagging

The ISO Online Browsing Platform link located here resolves to **edition 2
(2013)**, whose title is the older *Information technology — Security
techniques — Code of practice for information security controls*. The
current edition is **27002:2022**, with the newer title used in the
`name` field above, and it is that edition [[NL-BIO]]'s BIO2 references
(as NEN-EN-ISO/IEC 27002:2022).

So the cited URL is authoritative but **points at a superseded edition**.
This is exactly the kind of defect a primary-source pass would catch and is
recorded rather than papered over.

`coverage: low`.

## Relationships

- Published by [[INTL-ISO]] and [[INTL-IEC]].
- Companion to [[INTL-ISO-IEC-27001]].
- Basis for [[NL-BIO]]'s control set.

## Sources

Listed in frontmatter — see the edition caveat above.
