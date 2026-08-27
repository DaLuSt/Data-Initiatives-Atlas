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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0004541 directly (2026-08-27): Article 1a establishes 'een basisregistratie topografie' (a topographic base registration) consisting of 'landsdekkend topografische bestanden' (nationwide topographic files) at various scale levels, in the same article that establishes the BRK. This closes the item recorded in discovery/research-queue.md as the only one of the ten registers where no statute was found at all — now confirmed by the Act's own text, not just search."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own BRT page directly (2026-08-27), which quotes the Kadaster verbatim: 'Het Kadaster is houder van de Basisregistratie Topografie (BRT)' (the Kadaster is holder of the BRT), and data.overheid.nl's basisregistraties_10 group listing (read directly for sibling entities this pass), which names 'Basisregistratie: Topografie (BRT)' among the ten."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own registrations overview directly (2026-08-27), which lists the BRT among the five base registrations the Kadaster holds and describes it as 'digitale topografische bestanden op verschillende schaalniveaus.' geobasisregistraties.nl's own overview, also read directly, places the BRT's function/dimension question alongside the address, ownership, value and subsurface registers as one of the coordinated geo base registrations."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Overzicht registraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Basisregistratie Topografie (BRT) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brt/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Basisregistraties | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Kadasterwet — official text"
    url: "https://wetten.overheid.nl/BWBR0004541"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
---

# BRT — Basisregistratie Topografie

> **Verified 2026-08-27.** All three cited pages read directly, plus the
> Kadasterwet's own official text added and read as a fourth source. This
> closes the item this entity previously called out as the only one of the
> ten registers with no statute confirmed at all: Article 1a of the
> Kadasterwet now cites the topographic base registration by name.

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
topografie"**. Reading the Act's own text directly this pass confirms it:
Article 1a establishes *both* the cadastral base registration and the
topographic base registration in the same sentence, as authentic data, with
database rights reserved to the Dienst voor het kadaster en de openbare
registers.

So [[NL-BRK]] and this register share one statute — the only such pair among
the ten, and the reason the stelsel's legal underpinning is **seven statutes
for nine registers** rather than one each.

## `coverage: low` still, for everything else

The statute is now read directly, not just sourced. Its scale levels are
still described only as "various" in the pages read, its products are not
enumerated and no commencement date for the topographic registration
specifically is recorded — the Kadasterwet's own text gives 3 May 1989 as
the Act's date, not a separate date for when the BRT provision itself took
effect.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KADASTER]].
- `governed-by` [[NL-KADASTERWET]] — shared with [[NL-BRK]].

## Sources

Listed in frontmatter, all four read directly this pass — the Kadaster and
digitaleoverheid.nl register pages, the geobasisregistraties.nl overview,
and the Kadasterwet's own official text (shared with [[NL-BRK]]).
