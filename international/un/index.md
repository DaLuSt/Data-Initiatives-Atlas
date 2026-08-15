# International — Index

Curated navigation hub for international-level entities: UN-system bodies
and initiatives, and non-UN international organisations and standards.

Anchor entity: [[UN]]

> **Sourcing caveat.** Every entity below was compiled from search-engine
> results only and carries `verification: search-only`. Several are
> single-source placeholders that say so in their own bodies — see
> `progress/current-batch.md`.

## UN scope (`UN-` IDs)

### Strategies, initiatives and policy

- [[UN-2-0]] — UN 2.0 and the quintet of change _(Sept 2023)_
- [[UN-DATA-STRATEGY]] — UN Secretary-General's Data Strategy ⚠ weakly sourced
- [[UN-GDC]] — Global Digital Compact

### Organisations

- [[UN-UNSD]] — UN Statistics Division / Statistical Commission
- [[UN-UNCTAD]] — UN Trade and Development _(data governance working group)_
- [[UN-ITU]] — International Telecommunication Union _(UN specialised agency)_

### Standards and platforms

- [[UN-FPOS]] — Fundamental Principles of Official Statistics
- [[UN-DATA-COMMONS]] — UN Data Commons ⚠ single weak source

## Non-UN international scope (`INTL-` IDs)

Batch 13's brief warns against classifying non-UN organisations as UN
bodies. These are **not** part of the UN system, and the ID scope records
that distinction:

### Standards organisations

| Organisation | Basis |
|---|---|
| [[INTL-ISO]] | National delegation |
| [[INTL-IEC]] | National delegation |
| [[INTL-W3C]] | Direct membership |
| [[INTL-IETF]] | Direct membership ⚠ thinnest entity |

_Compare [[UN-ITU]], which is also national-delegation based but **is** a UN
specialised agency — the case where the distinction matters most._

### Intergovernmental

- [[INTL-OECD]] — data governance workstream

### Standards

- [[INTL-DCAT]] — W3C Data Catalog Vocabulary _(root of the metadata chain)_
- [[INTL-ISO-IEC-27001]] — information security management systems
- [[INTL-ISO-IEC-27002]] — information security controls

## Cross-level chains rooted here

Two international → EU → national / international → national descents:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)

INTL-ISO-IEC-27001 + -27002 (ISO/IEC) → NL-BIO / BIO2
```

Statistical, with the upper link **missing**:

```
UN-UNSD + UN-FPOS   (global apex)
      ⋮  (no source connects these levels)
EU-EUROSTAT / European Statistical System
      ↓
NL-CBS
```

---

Last updated: 2026-08-14 (Batches 12–14).
