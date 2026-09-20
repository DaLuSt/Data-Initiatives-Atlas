---
id: NL-BRP
type: platform
name: Basisregistratie Personen
alternative_names:
  - BRP
  - Personal Records Database
description: >
  The Dutch base registry of persons: the authoritative registration of
  personal data of residents registered by the Dutch government, and one of
  the ten registrations in the stelsel van basisregistraties. It is governed
  by the Wet basisregistratie personen, and the Rijksdienst voor
  Identiteitsgegevens is responsible for the secure storage and exchange of
  the data it holds. It succeeded the municipal GBA registration, and it
  couples to the base registry of addresses and buildings so that municipal
  address data reaches the population register.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2014-01-06
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-RVIG
related_entities:
  - NL-BASISREGISTRATIES
  - NL-RVIG
  - NL-BAG
  - NL-WET-BRP
relationships:
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading rvig.nl's own BRP page directly (2026-08-27), which describes the BRP as the register of personal data of Dutch residents and of non-residents staying under four months, and digitaleoverheid.nl's own BRP page, also read directly, which names the Wet Basisregistratie Personen as the statutory foundation. Neither page enumerates all ten registers on the page itself; data.overheid.nl's basisregistraties_10 group listing (read directly for sibling entities this pass) independently confirms 'Basisregistratie: Personen (BRP)' as one of the ten."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-RVIG
    source: fact
    evidence: "Confirmed by reading rvig.nl's own BRP page directly (2026-08-27): 'RvIG is verantwoordelijk voor de veilige opslag van deze gegevens en de uitwisseling ervan' (RvIG is responsible for secure storage of this data and its exchange). digitaleoverheid.nl's BRP page, also read directly, names RvIG as provider/distributor while municipalities hold resident data and the minister holds non-resident data."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WET-BRP
    source: fact
    evidence: "Confirmed by reading rvig.nl's own BRP page directly (2026-08-27), which links to the Wet BRP as its legal basis, and rvig.nl's dedicated legislation page (read for [[NL-WET-BRP]] this pass), which states 'De Wet Basisregistratie Personen (Wet BRP) vormt sinds 2014 de basis voor de registratie van persoonsgegevens.' A WebSearch cross-check of wetten.overheid.nl (BWBR0033715) independently confirms the exact commencement date as 6 January 2014 — the version of the Act effective from that date is titled '/2014-01-06' in the government's own consolidated-text archive. This relationship was moved down from NL-BASISREGISTRATIES in a prior batch, where it had been recorded at confidence: low; it is now confirmed at high confidence."
    confidence: high
    valid_from: 2014-01-06
    valid_until: null
  - type: carries-identifier-of
    target: NL-BAG
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #149's BAG-BRP half, using a new relationship type (metadata/relationship-types.md §2.1, added 2026-09-20). Confirmed by reading RvIG's own 'Toelichting — Koppeling BAG-BRP' and 'Koppeling BAG-GBA-BRP' pages directly (2026-08-27): since the mandatory Logisch Ontwerp 2024-Q1 coupling took effect in January 2024, every current residential or postal address in the BRP must carry a BAG identification code and match BAG's own values exactly, with location descriptions, 'dot addresses,' reference addresses and secondary addresses as primary residences now prohibited outright. `carries-identifier-of` records the BAG identification code the BRP's own address fields must carry, distinct from the broader operational coupling described in prose."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistratie Personen | RvIG"
    url: "https://www.rvig.nl/basisregistratie-personen"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
  - title: "Basisregistratie Personen (BRP) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brp/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Toelichting — Koppeling BAG-BRP"
    url: "https://www.rvig.nl/bag-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
  - title: "Koppeling BAG-GBA-BRP"
    url: "https://www.rvig.nl/hup/koppeling-bag-gba-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
---

# BRP — Basisregistratie Personen

> **Verified 2026-08-27.** All four cited pages read directly. The
> BAG–BRP coupling turns out to have **two distinct phases**, not one: a
> one-time technical coupling in 2011–2012, and a separate, much stricter
> **mandatory** coupling in force since January 2024 that bans point
> addresses, location descriptions and reference addresses outright. The
> entity's prior text described only the general arrangement.
>
> **Closed 2026-09-20** (`discovery/unresolved.md` row #149): the mandatory
> BAG identification-code requirement is now a typed `carries-identifier-of`
> edge, a new relationship type. `valid_from` stays `null` — the sources
> give the month (January 2024) the mandatory coupling took effect, not a
> specific day, and no day is guessed.

## Description

The BRP is the authoritative Dutch registration of the personal data of
residents registered by government. It is one of the ten registrations in
[[NL-BASISREGISTRATIES]], governed by [[NL-WET-BRP]], with [[NL-RVIG]]
responsible for the secure storage and exchange of its data.

It succeeded the municipal **GBA** registration, and the RvIG guidance on
the **BAG–GBA–BRP coupling** documents that lineage alongside the current
arrangement.

## The clearest documented coupling in the stelsel

The **BAG–BRP coupling** has its own RvIG guidance, which makes it the
best-sourced inter-register link in the stelsel: municipal address data from
[[NL-BAG]] reaches the population register, so that a person's registered
address is the same object the buildings register describes.

Reading both RvIG pages directly this pass shows the coupling happened in
**two distinct stages**, not one continuous arrangement:

- **2011–2012**: a one-time technical coupling (Logisch Ontwerp 2, July
  2009) matching four fields — street, city, and two identification codes —
  between BAG and GBA/BRP records, executed once by each municipality.
- **Since January 2024**: a **mandatory, ongoing** coupling (Logisch Ontwerp
  2024-Q1) requiring every current residential or postal address in the BRP
  to carry a BAG identification code and match BAG's own values exactly.
  Location descriptions, "dot addresses," reference addresses ("near",
  "opposite") and secondary addresses as primary residences are now
  prohibited outright, and a monthly Kwaliteitsmonitor (KWM) report flags
  municipalities' non-conforming addresses.

That second stage is considerably stronger than the general "coupling"
description this entity previously carried — it is a hard data-quality
mandate with monthly compliance reporting, not just a one-off technical link.

**A relationship to [[NL-BAG]] is now asserted** for the identifier-coupling
half of the picture, closed 2026-09-20 via a new `carries-identifier-of`
type: the mandatory Logisch Ontwerp 2024-Q1 coupling requires every current
BRP address to carry a BAG identification code and match BAG's own values
exactly. The broader two-stage administrative history above — the 2011–2012
one-time technical coupling and the ongoing monthly Kwaliteitsmonitor
compliance reporting — remains recorded only in prose: `carries-identifier-of`
captures the shared key, not the surrounding process, and the Atlas has no
type for the latter.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-RVIG]].
- `governed-by` [[NL-WET-BRP]] — **moved down from the stelsel entity**,
  where it had sat at `confidence: low` with a note saying it governs one
  registration rather than the whole system. That note asked for exactly
  this move.
- `carries-identifier-of` [[NL-BAG]] — `confidence: high`, new 2026-09-20.

## Sources

Listed in frontmatter, all four read directly this pass — RvIG's own BRP
page, the digitaleoverheid.nl BRP page, and both RvIG coupling-guidance
pages, which between them reveal the coupling's two-stage history.
