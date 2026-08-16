---
id: NL-BASISREGISTRATIES
type: framework
name: Stelsel van Basisregistraties
alternative_names:
  - Stelsel van basisregistraties
  - System of Base Registries
description: >
  The Dutch system of base registries: ten designated national registrations
  plus supporting system services, established so that core data of each
  kind is collected and managed in one authoritative place and reused across
  government rather than re-collected. The ten are the BRP, the
  Handelsregister, the BAG, the BRT, the BRK, the BRV, the BRI, the WOZ, the
  BGT and the BRO. System facilities support data exchange between the
  registrations and the accuracy of the data: Digikoppeling for exchange
  between government organisations, and Digimelding for reporting suspected
  errors. Each registration has an initiating organisation, a supervisor, a
  provider and one or more holders, and one organisation can be provider,
  holder and user at the same time.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-BRP
  - NL-NHR
  - NL-BAG
  - NL-BRT
  - NL-BRK
  - NL-BGT
  - NL-WOZ
  - NL-BRV
  - NL-BRI
  - NL-BRO
  - NL-DIGIKOPPELING
  - NL-FDS
relationships: []

sources:
  - title: "10 basisregistraties — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Rollen — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/rollen-stelsel-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Stelsel van Basisregistraties — toegankelijke beschrijving"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/stelsel-van-basisregistraties-toegankelijke-beschrijving/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Het huidige Stelsel van Basisregistraties — NORA Online"
    url: "https://www.noraonline.nl/wiki/Het_huidige_Stelsel_van_Basisregistraties"
    publisher: "NORA Online"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
  - title: "Basisregistraties | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
---

# Stelsel van Basisregistraties

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Stelsel van Basisregistraties is the Dutch system of base registries.
Ten designated registrations, plus supporting system services, form the
stelsel. The organising principle is **single-point collection**: core data
of each kind is collected and maintained in one authoritative place, then
reused across government rather than repeatedly re-collected.

## The ten registrations

All ten are now Atlas entities:

| Register | What it answers | Holder / provider modelled |
|---|---|---|
| [[NL-BRP]] | who people are, and where they live | [[NL-RVIG]] |
| [[NL-NHR]] | which businesses and legal entities exist | [[NL-KVK]] |
| [[NL-BAG]] | addresses and buildings | [[NL-KADASTER]] (national facility) |
| [[NL-BRT]] | topography, small and medium scale | [[NL-KADASTER]] |
| [[NL-BRK]] | who owns real property | [[NL-KADASTER]] |
| [[NL-BGT]] | topography, large scale, 20 cm accuracy | [[NL-KADASTER]] (national facility) |
| [[NL-WOZ]] | what property is worth | [[NL-WAARDERINGSKAMER]] (functional manager) |
| [[NL-BRV]] | vehicles and their keepers | [[NL-RDW]] |
| [[NL-BRI]] | what people earn | [[NL-BELASTINGDIENST]] |
| [[NL-BRO]] | what is underneath the ground | [[NL-TNO]] (national facility) |

The **geo** subset — BAG, BRT, BRK, BGT, WOZ, BRO — is described as a
division of labour over the same physical object: the address (BAG), the
function of a location and its dimensions (BRT/BGT), ownership (BRK), value
(WOZ) and the subsurface (BRO). See [[NL-BRK]] for that table.

## System services

The stelsel is not only the registrations. System facilities support
exchange between them and the accuracy of the data:

- **[[NL-DIGIKOPPELING]]** — data exchange between government organisations;
- **Digimelding** — reporting suspected errors in the registrations.

Digimelding is **not** an Atlas entity: it is named in one sentence of one
source and nothing else about it was established. Queued.

## Roles, not owners — and why the graph shows fewer parties than exist

The stelsel's own documentation does not describe a register as having an
owner. It describes **four roles**: an initiating organisation, a
supervisor, a provider, and one or more holders — and states that one
organisation can be provider, holder and user at the same time, giving
[[NL-RDW]] as the example.

**The Atlas has one relationship type for this**, `maintained-by`, and every
register carries exactly one. Where the roles diverge, the edge points at
the party the Atlas can name, and the divergence is written into the
relationship's own `evidence` string so it is visible in the graph data
rather than only in prose.

The cost is concentrated in three registers:

| Register | Who actually holds the data | What the graph shows |
|---|---|---|
| [[NL-BAG]] | municipalities | Kadaster (national facility) |
| [[NL-BGT]] | **seven** categories of bronhouder, organised in SVB-BGT | Kadaster (national facility) |
| [[NL-WOZ]] | municipalities | Waarderingskamer (functional manager) |

**Dutch municipalities are not modelled.** Unlike the German Länder, Belgian
Regions and Spanish Comunidades Autónomas, this is *not* blocked by the
`level` vocabulary — `local` exists. It is blocked by there being no obvious
entity to create: there are hundreds of municipalities, and a single node
for "the municipalities" would be an invention. Logged in
`discovery/unresolved.md`.

## What this batch could not express, and why it matters here

Three distinct gaps surfaced, and they may be one gap:

1. **Authorised use.** No relationship type says "is an authorised user
   of". The [[NL-BELASTINGDIENST]] consumes [[NL-WOZ]]; the [[NL-RDW]]
   consumes [[NL-BRP]]. Neither is recorded.
2. **Key-sharing couplings.** [[NL-BRK]] products carry the KvK number from
   [[NL-NHR]]; [[NL-BAG]] couples to [[NL-BRP]] through documented RvIG
   guidance. Neither is recorded.
3. **`Authentiek gegeven`.** The legal status that makes a base registry a
   base registry — data other bodies are obliged to use and may not
   independently re-determine — has no field.

Taken together: **the Atlas models what these registers *are* and what they
*descend from*, and has almost no vocabulary for how data actually moves
between them.** For a system whose entire purpose is data movement, that is
the honest headline finding of this batch.

It is the same shape as the two failures the UN batch recorded, which brings
the count to five sourced connections left unmodelled for want of a type —
past the threshold `metadata/relationship-types.md` §2.3 sets for proposing
one.

## Statutes: named, not modelled

Nine of the ten registers have a statutory basis, and where it was sourced
it is named in the register's description — the Wet BAG (partially in force
1 July 2009), the Wet BGT (1 January 2016), the Wet BRO (1 January 2018),
Chapter IVA of the AWR for the BRI (1 January 2009), the Wet WOZ.

**No law entity was created for any of them.** Only [[NL-BRP]] carries a
`governed-by` edge, to [[NL-WET-BRP]], which already existed from Batch 3.
Creating six or seven Dutch statutes would be a legislation batch, not a
registry batch, and doing half of it would leave the layer inconsistent.
Queued in `discovery/research-queue.md`.

**[[NL-BRT]] has no sourced statute at all** — the one register of the ten
where none was found.

## Relationship to [[NL-FDS]] is still open

Whether the Federatief Datastelsel extends, replaces or sits beside the
stelsel remains unestablished, as it has since Batch 2. Nothing in this
batch touched it, and nothing is asserted.

## Relationships

None asserted from this entity. All ten registers carry `part-of` edges
pointing here — `part-of` belongs on the part, not the whole.

**The `governed-by` edge to [[NL-WET-BRP]] has been removed from this
entity** and moved to [[NL-BRP]], where it belongs. This file previously
said so itself: *"Once the individual registrations become entities, this
link should move down to the BRP entity."* They have, and it has.

## Sources

Listed in frontmatter.
