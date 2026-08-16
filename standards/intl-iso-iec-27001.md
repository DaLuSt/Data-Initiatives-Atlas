---
id: INTL-ISO-IEC-27001
type: standard
name: "ISO/IEC 27001 — Information security management systems"
alternative_names:
  - ISO 27001
  - "ISO/IEC 27001:2022"
  - NEN-EN-ISO/IEC 27001
description: >
  International standard specifying the requirements for establishing,
  implementing, maintaining and continually improving an information
  security management system. Published jointly by ISO and IEC under
  JTC 1/SC 27.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - INTL-ISO
  - INTL-IEC
related_entities:
  - INTL-ISO-IEC-27002
  - NL-BIO
relationships:
  - type: maintained-by
    target: INTL-ISO
    source: fact
    evidence: "ISO/IEC 27001 is jointly published by ISO and the IEC, under Subcommittee 27 of ISO/IEC JTC 1 (iso.org/standard/27001; jtc1info.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ISO/IEC 27001:2022 — Information security management systems"
    url: "https://www.iso.org/standard/27001"
    publisher: "International Organization for Standardization (ISO)"
  - title: "ISO/IEC 27000 family — Information security management"
    url: "https://www.iso.org/standard/iso-iec-27000-family"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Information security, cybersecurity and privacy protection — JTC 1/SC 27"
    url: "https://jtc1info.org/technology/subcommittees/information-security-cybersecurity-privacy-protection/"
    publisher: "ISO/IEC JTC 1"
---

# ISO/IEC 27001

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

ISO/IEC 27001 is the international standard specifying requirements for
establishing, implementing, maintaining and continually improving an
information security management system (ISMS). It is described as the
world's best-known standard for information security management, and is
published jointly by [[INTL-ISO]] and [[INTL-IEC]] under JTC 1/SC 27.

The current edition is **ISO/IEC 27001:2022**.

## What this closes

[[NL-BIO]], the Dutch government security baseline, has carried a pending
relationship to the ISO/IEC 27000 family since Batch 4. BIO2 is explicitly
based on **NEN-EN-ISO/IEC 27001:2023 and 27002:2022**, applying 27001 to
formulate ISMS requirements and 27002 to select risk-driven controls.

The `based-on` relationship is now recorded on `NL-BIO`, giving another
international → national standards chain:

```
INTL-ISO-IEC-27001 / -27002  (ISO/IEC)
        │ based-on
NL-BIO / BIO2                (Dutch government baseline)
```

**One caveat is recorded on that relationship.** BIO2 cites
*NEN-EN-ISO/IEC 27001:**2023***, while the ISO page located here is the
**2022** edition. The `NEN-EN-` prefix indicates the European/Dutch adoption
of the ISO standard, and adoption years commonly lag the ISO edition — so
these are very likely the same standard under its Dutch designation. That is
an inference, not a sourced equivalence, and it is flagged rather than
smoothed over.

`coverage: low`: the standard's own structure and Annex A controls were not
researched.

## Relationships

- Published by [[INTL-ISO]] and [[INTL-IEC]].
- Companion to [[INTL-ISO-IEC-27002]].
- Basis for [[NL-BIO]].

## Sources

Listed in frontmatter.
