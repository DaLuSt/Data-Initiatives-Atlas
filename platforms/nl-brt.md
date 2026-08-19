---
id: NL-BRT
type: platform
name: Basisregistratie Topografie
alternative_names:
  - BRT
  - Base Registry of Topography
description: >
  The Dutch base registry of topography, held by the Kadaster, and one of
  the ten registrations in the stelsel van basisregistraties. It consists of
  digital topographic files at various scale levels. Within the geo base
  registries it provides information about the function of a location and
  about dimensions, complementing the address registry for location, the
  cadastral registry for ownership, the property-value registry for value
  and the subsurface registry for what lies beneath. It is the small- and
  medium-scale counterpart to the large-scale topographic registry.

level: national
country: NL
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
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-KADASTER
related_entities:
  - NL-KADASTERWET
  - NL-BASISREGISTRATIES
  - NL-KADASTER
  - NL-BGT
  - NL-BAG
relationships:
  - type: governed-by
    target: NL-KADASTERWET
    source: fact
    evidence: "The Kadasterwet of 3 May 1989 contains rules on the public registers for registered property and on the cadastre; the cadastral base registration and the topographic base registration are maintained under it as authentic data, with database rights reserved to the Dienst voor het kadaster en de openbare registers (wetten.overheid.nl/BWBR0004541). NOT READ — search-only. This closes the item recorded in discovery/research-queue.md as the only one of the ten registers where no statute was found at all."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT (Basisregistratie Topografie), BRK, BRV, BRI, WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "The Kadaster holds the Basisregistratie Topografie, which consists of digital topographic files at various scale levels (kadaster.nl 'Overzicht registraties'; geobasisregistraties.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Overzicht registraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties"
    publisher: "Kadaster"
  - title: "Basisregistratie Topografie (BRT) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brt/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistraties | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
---

# BRT — Basisregistratie Topografie

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BRT is the Dutch base registry of topography, held by [[NL-KADASTER]]
and consisting of **digital topographic files at various scale levels**.

In the geo base registries' division of labour it answers **what is at a
location** and **what size it is** — the function of a place and its
dimensions — alongside [[NL-BAG]] for the address, [[NL-BRK]] for
ownership, [[NL-WOZ]] for value and [[NL-BRO]] for the subsurface.

## Two topographic registers, and the difference between them

The stelsel contains **two** topographic base registries, which is initially
confusing and is the main thing this entity exists to make clear:

| | BRT | [[NL-BGT]] |
|---|---|---|
| Scale | small and medium, multiple scale levels | **large scale** |
| Precision | not established in sources read | **20 centimetres** |
| Holder | Kadaster | many bronhouders; Kadaster runs the national facility |
| Statute | **[[NL-KADASTERWET]]** — shared with [[NL-BRK]] | [[NL-WET-BGT]], in force 1 January 2016 |

They are not versions of each other and neither supersedes the other. **No
relationship between them is asserted** — no source read states one, and
`related-to` would add nothing a reader cannot see from both being
topographic registers in the same stelsel.

## Its statutory basis — found, and shared

This entity was recorded as **the only one of the ten registers where no
statute was found at all**, and `discovery/research-queue.md` called it the
weakest of the ten for that reason.

The statute is the **[[NL-KADASTERWET]]** of 3 May 1989, and the reason it
took a dedicated search to find is that **there is no "Wet basisregistratie
topografie"**. The Kadasterwet's rules on the public registers and the
cadastre carry *both* the cadastral base registration and the topographic
base registration as authentic data, with database rights reserved to the
Dienst voor het kadaster en de openbare registers.

So [[NL-BRK]] and this register share one statute — the only such pair among
the ten, and the reason the stelsel's legal underpinning is **seven statutes
for nine registers** rather than one each.

## `coverage: low` still, for everything else

The statute is now sourced. Its scale levels are still described only as
"various", its products are not enumerated and no date is recorded. The
Kadaster's registry overview and the digitaleoverheid.nl register page carry
it, and neither was read.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KADASTER]].
- `governed-by` [[NL-KADASTERWET]] — shared with [[NL-BRK]].

## Sources

Listed in frontmatter.
