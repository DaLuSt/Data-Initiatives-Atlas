---
id: CH-AGOV
type: platform
name: AGOV
alternative_names:
  - Behörden-Login AGOV
description: >
  Switzerland's government login, usable at federal, cantonal and
  municipal authorities without a username or password, authenticating
  instead via smartphone app or security key. A federal service led by
  the Federal Chancellery as part of Digitale Verwaltung Schweiz, in
  collaboration with cantons, municipalities and the Federal IT Office.
  Launched in early 2024, reaching one million accounts by December 2025
  and two million by August 2026, with fourteen cantons and a growing
  set of municipalities and national organisations connected as of 2026.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2024-01-01
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - CH-DVS
related_entities:
  - CH
  - CH-DVS
  - GB-ONE-LOGIN
  - NL-DIGID
relationships:
  - type: part-of
    target: CH
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (CH-DVS's own file: 'a Swiss analogue to GB-ONE-LOGIN not yet an Atlas entity'). Confirmed by reading agov.ch's own page directly (2026-09-13): AGOV is 'das neue Behörden-Login der Schweiz' (Switzerland's new government login), 'eine Dienstleistung des Bundes' (a federal service). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 2024-01-01
    valid_until: null
  - type: maintained-by
    target: CH-DVS
    source: fact
    evidence: "Confirmed by reading agov.ch's own page directly (2026-09-13): AGOV is operated by 'Digitale Verwaltung Schweiz' (Digital Administration Switzerland — CH-DVS) in collaboration with cantons, municipalities, the Federal Chancellery and the Federal IT Office. Independently corroborated by admin.ch's own bwo.admin.ch news page, read directly, which states the Federal Chancellery leads AGOV as part of the Digitale Verwaltung Schweiz initiative."
    confidence: high
    valid_from: 2024-01-01
    valid_until: null

sources:
  - title: "AGOV — Ihr neues Behörden-Login"
    url: "https://www.agov.ch/?l=de"
    publisher: "AGOV / Digitale Verwaltung Schweiz"
    accessed: "2026-09-13"
  - title: "Behörden-Login AGOV mit über zwei Millionen Nutzerkonten"
    url: "https://www.bwo.admin.ch/de/newnsb/-ST56dHpC-WRtARraVlYF"
    publisher: "Bundesamt für Wohnungswesen / admin.ch"
    accessed: "2026-09-13"
---

# AGOV

> **Created 2026-09-13.** [[CH-DVS]]'s own file had flagged AGOV as "a
> Swiss analogue to [[GB-ONE-LOGIN]] not yet an Atlas entity" — a finding
> recorded but not acted on. AGOV's own site and an official `admin.ch`
> news page were both read directly.

## Description

Confirmed by reading `agov.ch` directly: AGOV is **"das neue
Behörden-Login der Schweiz"** (Switzerland's new government login),
usable "beim Bund sowie bei kantonalen und kommunalen Behörden" (at
federal, cantonal and municipal authorities) — for example to file tax
returns electronically. It eliminates the need for a username and
password, authenticating instead via smartphone app or security key,
with additional identity-verification steps (by mail, at post offices,
at home, or by video) available where a higher login-quality level is
required.

## Operator and scale

Confirmed by reading `bwo.admin.ch`'s own news page directly: the
**Federal Chancellery** leads AGOV as part of **Digitale Verwaltung
Schweiz** ([[CH-DVS]]). AGOV **launched in early 2024**, reached **one
million accounts by December 2025** and **two million by August 2026**,
growing at roughly 25,000 new users weekly at the time of reading.
**Fourteen cantons** (AG, AR, BE, BL, BS, GR, GL, LU, NE, SG, SH, VS, ZG,
ZH) plus a growing set of municipalities, the Swiss Army and national
organisations were connected as of the same reading.

## A Swiss analogue, structurally distinct from the others

Like [[GB-ONE-LOGIN]] and [[NL-DIGID]], AGOV is a passwordless
government-wide login rather than a full digital-identity credential.
Unlike [[NL-DIGID]] (a single national scheme) it explicitly spans
**three tiers of Swiss federalism** — federal, cantonal and municipal —
in one login, which [[CH-DVS]]'s own multi-level governance structure
(Bund, cantons and communes as joint parties to its founding framework
agreement) makes possible.

## Not modelled

- AGOV's **legal basis** — neither page read this pass states an
  enabling statute or ordinance.
- The distinction between AGOV's own login-quality levels and any
  relationship to eIDAS or Swiss federal identity law.

## Relationships

- `part-of` [[CH]] — anchor edge.
- `maintained-by` [[CH-DVS]] — the Federal Chancellery-led body operating
  it, per its own site.

## Sources

Listed in frontmatter, both read directly 2026-09-13.
