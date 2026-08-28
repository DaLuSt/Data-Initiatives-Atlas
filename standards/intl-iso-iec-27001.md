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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading jtc1info.org and two Wikipedia articles directly (2026-08-28): jtc1info.org states SC 27 is 'responsible for helping to mitigate against the growing problems of cyber risks and attacks' and names ISO/IEC 27001 as one of its standards; Wikipedia's ISO/IEC 27001 article confirms 'The International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) jointly publish this standard' under 'ISO/IEC JTC 1/SC 27,' with the current edition '2022,' supplemented by 'ISO/IEC 27001:2022/Amd 1:2024'; Wikipedia's ISO/IEC 27000 family article confirms the family is 'developed jointly by' ISO and IEC. Both `iso.org` sources in the frontmatter list (`/standard/27001`, `/standard/iso-iec-27000-family`) remain unread — `iso.org` is domain-wide 403-blocked for this pass's retrieval tool, confirmed on [[INTL-ISO]]."
    confidence: high
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
    accessed: "2026-08-28"
  - title: "ISO/IEC 27001"
    url: "https://en.wikipedia.org/wiki/ISO/IEC_27001"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "ISO/IEC 27000 family"
    url: "https://en.wikipedia.org/wiki/ISO/IEC_27000_family"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# ISO/IEC 27001

> **Verified 2026-08-28, with a documented block.** `iso.org` is
> domain-wide 403-blocked for this pass's retrieval tool (see
> [[INTL-ISO]] for the detail across multiple paths), so neither
> `iso.org` source could be read. jtc1info.org was read directly, and two
> Wikipedia articles (on ISO/IEC 27001 itself and on the wider 27000
> family) were added as substitute sources and read directly, bringing
> three of five cited sources to a genuine read. `verification` moves
> from `search-only` to `primary-source` on that basis. The **2022**
> edition is confirmed current, now itself amended by "ISO/IEC
> 27001:2022/Amd 1:2024" addressing climate-action considerations — a
> detail not in any previously-cited source.

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

Listed in frontmatter. Three of five read directly this pass —
jtc1info.org and two Wikipedia articles added as substitutes for the
two `iso.org` sources, which stay unread (domain-wide block; see
verification note above).
