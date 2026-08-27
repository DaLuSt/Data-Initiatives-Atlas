---
id: NL-BAG
type: platform
name: Basisregistratie Adressen en Gebouwen
alternative_names:
  - BAG
  - Base Registry of Addresses and Buildings
description: >
  The Dutch base registry of addresses and buildings, and one of the ten
  registrations in the stelsel van basisregistraties. Its statutory basis is
  the Wet basisregistraties adressen en gebouwen, adopted by the Eerste
  Kamer on 22 January 2008 and partially in force from 1 July 2009, which
  regulates a base registry of address data and a base registry of certain
  building-related objects. From mid-2009 municipalities were required to
  keep core data on buildings and addresses in one automated system, and all
  government bodies were required to use it. Municipalities are the data
  holders; the Kadaster manages the national BAG facility.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2009-07-01
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
  - NL-WET-BAG
  - NL-BASISREGISTRATIES
  - NL-KADASTER
  - NL-BRP
  - NL-BRK
  - NL-BRT
relationships:
  - type: governed-by
    target: NL-WET-BAG
    source: fact
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0023466 directly (2026-08-27): it is the Wet basisregistratie adressen en gebouwen, whose commencement is set article-by-article by royal decree rather than a single fixed date in the text itself. The Eerste Kamer's own bill dossier (30.968), read directly, confirms the Eerste Kamer disposed of the bill as a hamerstuk (uncontested) on 22 January 2008. IMBAG's practitioner handbook (Kadaster), read directly, names the Besluit BAG (2009, amended 2017) and the Regeling BAG as the implementing instruments beneath the Act, and the Catalogus BAG 2018 as the content specification — corroborating rather than independently re-dating the 1 July 2018 amendment previously sourced only to geobasisregistraties.nl. ndfr.nl's consolidated text was not re-fetched this pass."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own BAG page directly (2026-08-27): 'onderdeel van het overheidsstelsel van basisregistraties' (part of the government's system of base registrations). data.overheid.nl's basisregistraties_10 group listing, read directly, names all ten registers by their exact abbreviations — BRV, BRK, BAG, BGT, HR, BRI, BRO, WOZ, BRT, BRP — matching this entity's description."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own BAG page directly (2026-08-27): 'Gemeenten zijn bronhouders van de BAG. Zij zijn verantwoordelijk voor het opnemen van de gegevens in de BAG en voor de kwaliteit ervan' (municipalities are bronhouders and responsible for data and quality) and 'Het Kadaster beheert de LV-BAG en stelt de gegevens beschikbaar aan de diverse afnemers' (Kadaster manages the national facility and distributes the data). This confirms the caveat already recorded here rather than removing it: municipalities hold the data, Kadaster runs the national facility."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistratie Adressen en Gebouwen (BAG) — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Wet basisregistraties adressen en gebouwen (30.968)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/30968_wet_basisregistraties"
    publisher: "Eerste Kamer der Staten-Generaal"
    accessed: "2026-08-27"
  - title: "Wet basisregistratie adressen en gebouwen — official text"
    url: "https://wetten.overheid.nl/BWBR0023466"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
  - title: "Wet basisregistratie adressen en gebouwen — consolidated text (not re-read this pass)"
    url: "https://www.ndfr.nl/content/BWBR0023466-20220501"
    publisher: "NDFR"
  - title: "Praktijkhandleiding BAG — beleidskaders"
    url: "https://imbag.github.io/praktijkhandleiding/beleidskaders"
    publisher: "IMBAG (Kadaster)"
    accessed: "2026-08-27"
  - title: "Toelichting — Koppeling BAG-BRP"
    url: "https://www.rvig.nl/bag-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
---

# BAG — Basisregistratie Adressen en Gebouwen

> **Verified 2026-08-27.** Five of six cited pages were read directly:
> Kadaster's own BAG page, the Eerste Kamer bill dossier, the official
> BWBR0023466 text, the IMBAG practitioner handbook, and RvIG's BAG–BRP
> coupling page. Only NDFR's consolidated text was not re-fetched.

## Description

The BAG is the Dutch base registry of addresses and buildings. Its statute,
the **Wet basisregistraties adressen en gebouwen**, was adopted by the
Eerste Kamer on **22 January 2008** and came partially into force on
**1 July 2009**. It regulates two things: a base registry of address data,
and a base registry of certain building-related objects.

From mid-2009 **municipalities** were required to hold core building and
address data in one automated system, and **all government bodies** were
required to use it. Municipalities are the data holders; [[NL-KADASTER]]
manages the national facility.

## The holder/provider split, and what the edge actually says

The BAG is the first register in this batch where the `maintained-by` edge
needs a caveat in its own evidence string, and it will not be the last.

**Municipalities hold the data. The Kadaster runs the national facility.**
Those are different jobs, and the stelsel's own documentation separates them
as distinct roles — initiator, supervisor, provider, holder. The Atlas has
one relationship type here, `maintained-by`, and it is pointed at the
Kadaster because the Kadaster is the party the Atlas can name.

**Dutch municipalities are not modelled**, and cannot easily be: there are
hundreds, and an entity for "the municipalities" collectively would be an
invention. The `level` vocabulary does contain `local`, so unlike the
Länder/Regions/Comunidades problem this is *not* blocked by the ontology —
it is blocked by the absence of an obvious entity to create. Logged in
`discovery/unresolved.md`.

The consequence is concrete and worth stating plainly: **for the BAG, the
BGT and the WOZ, the party that actually creates the data is absent from
the graph.**

## Its couplings

The BAG is the most-connected register in the stelsel by description:

- **BAG → BRP.** The RvIG BAG–BRP coupling guidance is the best-sourced
  inter-register link in the system. See [[NL-BRP]].
- **BAG ↔ BRK / BRT.** The address and building registries are described as
  related to the cadastral and topographic base registries in the
  geo-information domain.

None of these is asserted as a relationship, for the reason given on
[[NL-BRP]]. They are recorded as `related_entities` associations, which the
graph shows as such.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KADASTER]] — national facility only; see above.

## Sources

Listed in frontmatter, five of six read directly this pass — the Kadaster's
BAG page, the Eerste Kamer bill dossier, the official BWBR0023466 text on
`wetten.overheid.nl`, the practitioner handbook's policy chapter, and the
RvIG BAG–BRP coupling guidance. NDFR's consolidated text was not re-fetched.
