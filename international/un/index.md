# International — Index

Curated navigation hub for international-level entities: UN-system bodies
and initiatives, and non-UN international organisations and standards.

Anchor entity: [[UN]] (`primary-source`, verified 2026-08-27)

> **Re-verification pass complete (2026-08-28).** The entire UN-scope
> cluster below (20 entities, plus the anchor [[UN]] verified in an earlier
> pass) has now been re-verified. **17 of 20 promoted to
> `verification: primary-source`** by genuinely reading a majority of each
> entity's cited sources — several via direct fetch of `unece.org`,
> `unesco.org`, `itu.int`, `unstats.un.org` and `un.org` pages; several
> others via a documented **`unece.org`/`unctad.org` domain-wide 403 block**
> this session, worked around per this batch's instruction by substituting
> directly-read alternates (Wikipedia, legislation.gov.uk, OSCE, service-
> architecture.com, NEPC, cepal.org) for the dead citations. **Three stayed
> at `verification: search-only`** — [[UN-CES]], [[UN-EDIFACT]] and
> [[UN-UNCTAD]] — where the block left fewer than half of each entity's
> sources genuinely read even after seeking alternates. See each entity's
> own frontmatter and body for the full evidence trail, and
> `discovery/unresolved.md`'s "UN bodies cluster re-verification
> (2026-08-28)" section for the batch-level findings (the `unece.org` block,
> two genuine platform/strategy rebuilds, and a founding-year discrepancy
> left open rather than silently resolved).
>
> Entities outside this pass's 20-file scope — [[UN-GDC]] and the non-UN
> `INTL-` entries below — were not touched and still carry whatever
> verification state their own last pass left them in.

## UN scope (`UN-` IDs)

### Strategies, initiatives and policy

- [[UN-2-0]] — UN 2.0 and the quintet of change _(Sept 2023)_ — `primary-source`
- [[UN-DATA-STRATEGY]] — UN Secretary-General's Data Strategy _(April 2020,
  predates UN 2.0 by three years — see the entity for a corrected framing)_
  — `primary-source`
- [[UN-2030-AGENDA]] — the 2030 Agenda for Sustainable Development
  (A/RES/70/1, 25 Sept 2015) — `primary-source`
- [[UN-GDC]] — Global Digital Compact _(not in this pass's scope; untouched)_

### Organisations

- [[UN-UNECE]] — Economic Commission for Europe (1947, Res. 36(IV)) —
  `primary-source`
- [[UN-UNESCO]] — Educational, Scientific and Cultural Organization (1945)
  — `primary-source`, all four cited sources read
- [[UN-UNSC]] — Statistical Commission — `primary-source` _(founding year
  genuinely disputed across sources — 1946 vs. 1947 — left open, see the
  entity)_
- [[UN-UNSD]] — UN Statistics Division — `primary-source`
- [[UN-CEFACT]] — Centre for Trade Facilitation and Electronic Business,
  under UNECE (est. 1996) — `primary-source`
- [[UN-ITU]] — International Telecommunication Union _(UN specialised
  agency since 1949)_ — `primary-source`
- [[UN-UNCTAD]] — UN Trade and Development _(data governance working
  group)_ — **`search-only`**: `unctad.org` returned HTTP 403 on every page
  tried this pass

### Programmes

- [[UN-CES]] — Conference of European Statisticians, organised by UNECE —
  **`search-only`**: only the Eurostat corroborating page was readable;
  all three `unece.org` citations stayed 403-blocked
- [[UN-GGIM]] — Committee of Experts on Global Geospatial Information
  Management (est. **27 July 2011**, ECOSOC resolution 2011/24 — date now
  confirmed to the day, not just the month) — `primary-source`
- [[UN-GGIM-EUROPE]] — European regional committee of UN-GGIM (est. 1
  October 2014) — `primary-source`

### Standards and platforms

- [[UN-FPOS]] — Fundamental Principles of Official Statistics (1991 → 1994
  → 2014 lineage confirmed in UNSD's own words) — `primary-source`
- [[UN-SDG-INDICATORS]] — global SDG indicator framework (234 indicators,
  under UN-UNSC supervision) — `primary-source`
- [[UN-EDIFACT]] — electronic data interchange standard, under UN-CEFACT —
  **`search-only`**: both `unece.org` citations 403-blocked, only one
  Wikipedia alternate found (short of a majority)
- [[UN-LOCODE]] — trade/transport location codes, named in Regulation (EU)
  2019/1239 — `primary-source`
- [[UN-DATA-COMMONS]] — UN Data Commons for the SDGs, launched 4 October
  2023 with Google.org, expanded September 2024 — `primary-source`
  _(rebuilt this pass: the prior sole citation, a Grokipedia page, is
  replaced entirely by a dedicated un.org/DESA page — the correct primary
  source simply hadn't been found before)_

### Frameworks and legislation

- [[UN-AI-ETHICS-RECOMMENDATION]] — UNESCO Recommendation on the Ethics of
  AI (Nov 2021) — `primary-source`
- [[UN-AARHUS]] — Aarhus Convention on environmental information access,
  under UNECE (1998 / in force 2001) — `primary-source` _(sourced this pass
  via Wikipedia + OSCE after a domain-wide `unece.org` block)_

## Non-UN international scope (`INTL-` IDs)

Batch 13's brief warns against classifying non-UN organisations as UN
bodies. These are **not** part of the UN system, and the ID scope records
that distinction. **Not in this pass's scope** — listed here for
navigation only, untouched this pass:

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
  — `primary-source`
- [[INTL-ISO-IEC-27001]] — information security management systems
- [[INTL-ISO-IEC-27002]] — information security controls

## Cross-level chains rooted here

Two international → EU → national / international → national descents:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)

INTL-ISO-IEC-27001 + -27002 (ISO/IEC) → NL-BIO / BIO2
```

A UN → EU → national descent in law, not metadata, confirmed this pass:

```
UN-AARHUS  (UNECE convention, 1998 / in force 2001)
     │  implements-requirement-from
     ▼
EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE  (2003/4/EC)
     │  applies-in
     ▼
NL · DE · BE · FR · ES · PL
```

A UN → EU trade-standards descent, also confirmed this pass:

```
UN-UNECE → UN-CEFACT → UN-LOCODE ◀── references ── EU-EMSWE ──▶ EU
```

Statistical, with the upper link still **missing** (this pass could not
close it — no source found connects UNSD/the Statistical Commission
directly to the European Statistical System; they meet only in the CES
forum, which stayed `search-only` this pass):

```
UN-UNSD + UN-UNSC + UN-FPOS   (global apex)
      ⋮  (no direct source connects these levels)
UN-CES   (forum both UNECE and Eurostat sit in — search-only this pass)
      ↓  participates-in (EU-EUROSTAT side)
EU-EUROSTAT / European Statistical System
      ↓
NL-CBS
```

---

Last updated: 2026-08-28 (UN bodies cluster re-verification pass — 17 of 20
entities promoted to `primary-source`; see `discovery/unresolved.md` for
the full write-up).
