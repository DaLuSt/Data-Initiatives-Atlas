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
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-27"
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
    evidence: "Confirmed by reading jtc1info.org and two Wikipedia articles directly (2026-08-28): jtc1info.org states SC 27 is 'responsible for helping to mitigate against the growing problems of cyber risks and attacks' and names ISO/IEC 27001 as one of its standards; Wikipedia's ISO/IEC 27001 article confirms 'The International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC) jointly publish this standard' under 'ISO/IEC JTC 1/SC 27,' with the current edition '2022,' supplemented by 'ISO/IEC 27001:2022/Amd 1:2024'; Wikipedia's ISO/IEC 27000 family article confirms the family is 'developed jointly by' ISO and IEC. Both `iso.org` sources in the frontmatter list (`/standard/27001`, `/standard/iso-iec-27000-family`) remain unread — `iso.org` is domain-wide 403-blocked for this pass's retrieval tool, confirmed on [[INTL-ISO]]. Confirmed a second, stronger way 2026-09-27, matching the workaround already used to close [[INTL-ISO-IEC-27002]] (discovery/unresolved.md row #220): standards.iteh.ai, an authorized ISO/IEC standards reseller, serves a free 'redline' preview PDF of the actual ISO/IEC 27001:2022 text (catalog number 82875, matching iso.org/standard/82875.html), read directly — its own Foreword states in as many words 'This document was prepared by Joint Technical Committee ISO/IEC JTC 1, Information Technology, Subcommittee SC 27, Information security, cybersecurity and privacy protection' and 'This third edition cancels and replaces the second edition (ISO/IEC 27001:2013), which has been technically revised,' with 'Copyright Protected Document © ISO/IEC 2022' and ISO's own copyright-office address on every page. `iso.org` itself remains domain-wide blocked, but this is the standard's own published text, not a page about it."
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
  - title: "ISO/IEC 27001 Europees aanvaard"
    url: "https://www.nen.nl/nieuws/ict/iso-iec-27001-europees-aanvaard/"
    publisher: "NEN"
    accessed: "2026-09-18"
  - title: "ISO/IEC 27001:2022 — redline preview PDF (catalog 82875)"
    url: "https://cdn.standards.iteh.ai/samples/82875/726bcf58250e43d9a666b4d929c8fbdb/ISO-IEC-27001-2022.pdf"
    publisher: "standards.iteh.ai (authorized ISO/IEC standards reseller)"
    accessed: "2026-09-27"
    note: "iso.org itself remains domain-wide 403-blocked. This free preview PDF reproduces the standard's own published text (Foreword, Introduction, Scope, Normative references, and clauses 4-6.3 in full) rather than a page about it — the same workaround already used to close INTL-ISO-IEC-27002 (discovery/unresolved.md row #220)."
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
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #33): the
> NEN-EN-ISO/IEC 27001:2023 vs. ISO/IEC 27001:2022 equivalence flagged
> below is now confirmed, not inferred, via NEN's own page.
>
> **Closed 2026-09-27**: `iso.org` remains domain-wide blocked, but
> `standards.iteh.ai`'s free "redline" preview PDF (the same workaround
> already used to close [[INTL-ISO-IEC-27002]], row #220) reproduces the
> standard's own published text directly — 4 of 6 sources now read
> directly. This gives, for the first time, the standard's own internal
> structure (ten main clauses plus a normative Annex A) and confirms the
> third edition "cancels and replaces the second edition (ISO/IEC
> 27001:2013)" — see "Structure, read directly" below.

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

**The 2023-vs-2022 caveat is now closed (2026-09-18).** BIO2 cites
*NEN-EN-ISO/IEC 27001:**2023***, while the ISO edition catalogued here is
**2022**. With `iso.org` itself still domain-wide blocked, the
equivalence is confirmed from the European/Dutch side instead: NEN's own
dedicated news page, "ISO/IEC 27001 Europees aanvaard," read directly,
states plainly that the European version is equal to the global version
plus a European foreword, published roughly a year later — which is why
the two carry different year designations. No longer an inference.

## Structure, read directly 2026-09-27

`coverage: low` previously stood because the standard's own structure and
Annex A controls were not researched, only described from outside. The
redline preview PDF (11 pages of the front matter and body text) closes
part of that gap. Ten main clauses: 4 Context of the organization,
5 Leadership, 6 Planning, 7 Support, 8 Operation, 9 Performance
evaluation, 10 Improvement — plus a normative **Annex A, "Information
security controls reference"** (the redline stops at clause 6.3;
Annex A's own content, and clauses 7-10 in full, are not reproduced in
this free sample). The Foreword confirms this third edition (2022-10)
"cancels and replaces the second edition (ISO/IEC 27001:2013), which has
been technically revised," and that its main structural change is
alignment "with the harmonized structure for management system standards
and ISO/IEC 27002:2022" — the same edition-to-edition alignment this
entity already recorded from the outside via Wikipedia, now confirmed
from the standard's own Foreword. `coverage` raised low→medium.

## Relationships

- Published by [[INTL-ISO]] and [[INTL-IEC]].
- Companion to [[INTL-ISO-IEC-27002]].
- Basis for [[NL-BIO]].

## Sources

Listed in frontmatter. **4 of 6 now read directly.** jtc1info.org and two
Wikipedia articles (2026-08-28 pass); NEN's own equivalence page
(2026-09-18), closing the 2023-vs-2022 edition question; and, added
2026-09-27, standards.iteh.ai's redline preview PDF of the standard's own
text (catalog 82875) — the workaround already used to close
[[INTL-ISO-IEC-27002]] (`discovery/unresolved.md` row #220). The two
`iso.org` sources stay unread (domain-wide 403 block).
