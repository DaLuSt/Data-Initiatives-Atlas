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
last_verified: "2026-08-27"
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

**No relationship to [[NL-BAG]] is asserted.** The coupling is documented as
a technical and administrative arrangement between two registers; the
Atlas's vocabulary has `depends-on`, which would overstate it, and
`related-to`, which would say almost nothing. The registers are listed in
each other's `related_entities` — an association, visible in the graph as
such — and the substance is recorded here in prose.

That is a deliberate choice, and it is the same one made for the nine other
registers: **the stelsel's internal couplings are its most interesting
property and the Atlas can only gesture at them.** See
[[NL-BASISREGISTRATIES]].

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-RVIG]].
- `governed-by` [[NL-WET-BRP]] — **moved down from the stelsel entity**,
  where it had sat at `confidence: low` with a note saying it governs one
  registration rather than the whole system. That note asked for exactly
  this move.

## Sources

Listed in frontmatter, all four read directly this pass — RvIG's own BRP
page, the digitaleoverheid.nl BRP page, and both RvIG coupling-guidance
pages, which between them reveal the coupling's two-stage history.
