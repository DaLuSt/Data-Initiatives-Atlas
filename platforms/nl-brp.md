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
verification: search-only

start_date: 2014-01-06
end_date: null
last_verified: null
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
    evidence: "The ten base registrations are the BRP (Basisregistratie personen), HR, BAG, BRT, BRK, BRV, BRI, WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl 'Basisregistraties: de 10 basisregistraties'; noraonline.nl 'Het huidige Stelsel van Basisregistraties'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-RVIG
    source: fact
    evidence: "The Basisregistratie Personen contains personal data of residents registered by the Dutch government, and RvIG is responsible for the secure storage and exchange of this data (rvig.nl 'Basisregistratie Personen'; digitaleoverheid.nl BRP page). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WET-BRP
    source: fact
    evidence: "The Wet BRP governs the Basisregistratie Personen, one of the registrations within the stelsel (rvig.nl; digitaleoverheid.nl BRP page). NOT READ — search-only. This relationship was moved down from NL-BASISREGISTRATIES, where it had been recorded at confidence: low with a note that it governs one registration rather than the stelsel as a whole."
    confidence: medium
    valid_from: 2014-01-06
    valid_until: null

sources:
  - title: "Basisregistratie Personen | RvIG"
    url: "https://www.rvig.nl/basisregistratie-personen"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
  - title: "Basisregistratie Personen (BRP) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brp/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Toelichting — Koppeling BAG-BRP"
    url: "https://www.rvig.nl/bag-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
  - title: "Koppeling BAG-GBA-BRP"
    url: "https://www.rvig.nl/hup/koppeling-bag-gba-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
---

# BRP — Basisregistratie Personen

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

Listed in frontmatter.
