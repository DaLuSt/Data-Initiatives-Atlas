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
verification: search-only

start_date: 2009-07-01
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
  - NL-BASISREGISTRATIES
  - NL-KADASTER
  - NL-BRP
  - NL-BRK
  - NL-BRT
relationships:
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG (Basisregistratie Adressen en Gebouwen), BRT, BRK, BRV, BRI, WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "The BAG is part of the Dutch base registrations system, with municipalities as data holders and the Kadaster managing the national BAG system; the Kadasterwet was amended in connection with the allocation of tasks to the Dienst voor het kadaster en de openbare registers regarding the landelijke voorziening for the basisregistraties adressen en gebouwen (kadaster.nl BAG page; tweedekamer.nl wetsvoorstel 31726). NOT READ — search-only. CAVEAT: municipalities are the data holders; this edge records the national-facility role only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistratie Adressen en Gebouwen (BAG) — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bag"
    publisher: "Kadaster"
  - title: "Wet basisregistraties adressen en gebouwen (30.968)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/30968_wet_basisregistraties"
    publisher: "Eerste Kamer der Staten-Generaal"
  - title: "Wet basisregistratie adressen en gebouwen — consolidated text"
    url: "https://www.ndfr.nl/content/BWBR0023466-20220501"
    publisher: "NDFR"
  - title: "Praktijkhandleiding BAG — beleidskaders"
    url: "https://imbag.github.io/praktijkhandleiding/beleidskaders"
    publisher: "IMBAG (Kadaster)"
  - title: "Toelichting — Koppeling BAG-BRP"
    url: "https://www.rvig.nl/bag-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
---

# BAG — Basisregistratie Adressen en Gebouwen

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

Listed in frontmatter — the Kadaster's BAG page, the Eerste Kamer bill
dossier, a consolidated text, the practitioner handbook's policy chapter,
and the RvIG coupling guidance.
