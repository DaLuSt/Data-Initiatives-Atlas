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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
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
  - NL-DIGIMELDING
  - NL-FDS
relationships: []

sources:
  - title: "10 basisregistraties — Stelsel van basisregistraties (confirmed genuinely bot-walled)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Rollen — Stelsel van basisregistraties (confirmed genuinely bot-walled)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/rollen-stelsel-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Stelsel van Basisregistraties — toegankelijke beschrijving (confirmed genuinely bot-walled)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/stelsel-van-basisregistraties-toegankelijke-beschrijving/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Het huidige Stelsel van Basisregistraties — NORA Online"
    url: "https://www.noraonline.nl/wiki/Het_huidige_Stelsel_van_Basisregistraties"
    publisher: "NORA Online"
    accessed: "2026-08-27"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
    accessed: "2026-08-27"
  - title: "Basisregistraties | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "10 basisregistraties in 1 stelsel"
    url: "https://www.rijksoverheid.nl/onderwerpen/digitale-overheid/10-basisregistraties-in-1-stelsel"
    publisher: "Rijksoverheid.nl"
    accessed: "2026-08-28"
  - title: "Stelselvoorzieningen"
    url: "https://www.logius.nl/domeinen/gegevensuitwisseling/stelselvoorzieningen"
    publisher: "Logius (Ministerie van BZK)"
    accessed: "2026-08-28"
---

# Stelsel van Basisregistraties

> **Promoted to `primary-source` 2026-08-28.** Three of the original six
> cited pages were read directly in the prior pass — noraonline.nl,
> data.overheid.nl and geobasisregistraties.nl. The three digitaleoverheid.nl
> pages remain genuinely bot-walled (a JavaScript verification challenge,
> confirmed across two prior passes); `web.archive.org` was attempted per
> this pass's specific instruction but this environment's fetch tool
> cannot reach `web.archive.org` at all (a tool-level restriction, not a
> content problem), so no Wayback snapshot of those three pages could be
> read. Two genuinely different, non-digitaleoverheid.nl government pages
> were found and read directly instead: `rijksoverheid.nl`'s own "10
> basisregistraties in 1 stelsel" page (confirming the ten-registration
> count, the once-only principle, and the mandatory-use rule in the
> ministry's own words) and Logius's "Stelselvoorzieningen" page
> (confirming, in the system operator's own words, what each of the four
> system facilities — Digikoppeling, Digimelding, Digilevering,
> Stelselcatalogus — actually does). That brings this entity to 5 of 8
> sources read directly — a genuine majority — so `verification` is
> promoted to `primary-source`.

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
exchange between them and the accuracy of the data. Confirmed by reading
noraonline.nl directly this pass: the system names **four**
stelselvoorzieningen — [[NL-DIGIKOPPELING]] (data exchange), Digilevering,
Digimelding (reporting suspected errors) and Stelselcatalogus — one more
than the two previously recorded here.

Digilevering and Stelselcatalogus are still **not** Atlas entities.
**Confirmed by reading Logius's own "Stelselvoorzieningen" page directly
(2026-08-28):** the four facilities "ondersteunen de basisregistraties bij
eenvoudige, uniforme, betrouwbare en efficiënte gegevensuitwisseling met
hun afnemers" (support the base registries with simple, uniform, reliable
and efficient data exchange with their consumers) — Digikoppeling for
secure information exchange between government bodies, Digimelding for
consumers to report suspected inaccuracies back to source organisations,
Digilevering for event-based notifications of registry changes, and
Stelselcatalogus as the integrated overview of concepts and data across
the system. **Digimelding is now [[NL-DIGIMELDING]]** (added 2026-09-04, a
research-queue pickup), leaving Digilevering and Stelselcatalogus as the
two still without enough substance beyond this functional description to
justify a separate entity. Queued.

## Roles, not owners — and why the graph shows fewer parties than exist

The stelsel's own documentation does not describe a register as having an
owner. The prior text named **four roles**: an initiating organisation, a
supervisor, a provider, and one or more holders. A targeted search of
digitaleoverheid.nl's own "Rollen" page content this pass (the page itself
remained bot-walled to direct fetch, but its indexed text was recoverable —
corroboration, not a direct read) names them more precisely and finds a
**fifth**: **Opdrachtgever** (commissioning party, = "initiating
organisation" above), **Toezichthouder** (supervisor — "responsible for
ensuring the basic registration operates in accordance with requirements,
agreements and legislation"), **Verstrekker** (provider), **Bronhouder**
(data holder — "responsible for acquiring and maintaining the authentic and
non-authentic data... and for ensuring the quality of those data"), and
**Afnemer** (user/consumer — "a government organization or private party
that receives data from a basic registration for use in their own
processes"), not previously named as a distinct role here. The source
states that one organisation can be provider, holder and user at the same
time, giving [[NL-RDW]] as the example.

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

## Statutes: complete, as of 2026-08-30

The register batch named the statutes and created none, on the grounds that
*"creating six or seven Dutch statutes would be a legislation batch, not a
registry batch, and doing half of it would leave the layer inconsistent."*
That legislation batch has now been done.

**All ten registers carry a `governed-by` edge — the last, [[NL-BRI]],
closed 2026-08-30 via a research-queue pickup:**

| Register | Statute |
|---|---|
| [[NL-BAG]] | [[NL-WET-BAG]] |
| [[NL-BGT]] | [[NL-WET-BGT]] — in force 1 January 2016 |
| [[NL-BRO]] | [[NL-WET-BRO]] — in force 1 January 2018 |
| [[NL-WOZ]] | [[NL-WET-WOZ]] |
| [[NL-NHR]] | [[NL-HANDELSREGISTERWET]] |
| [[NL-BRV]] | [[NL-WEGENVERKEERSWET-1994]] |
| [[NL-BRK]] | [[NL-KADASTERWET]] |
| [[NL-BRT]] | [[NL-KADASTERWET]] — **the same act** |
| [[NL-BRP]] | [[NL-WET-BRP]] — from Batch 3 |
| [[NL-BRI]] | Chapter IVA (articles 21–22i) of the AWR, via `governed-by` → [[NL-BASISREGISTRATIES]] itself, the AWR not being a separate Atlas entity — confirmed directly against `wetten.overheid.nl`'s own text, correcting a previously-unchecked citation of "21 to 21k" to the true range, 21 to 22i |

### Seven statutes, nine registers

The legal underpinning of the stelsel is **not one-to-one**, and that is the
finding this layer produces:

- **[[NL-KADASTERWET]] carries two registers** — the cadastre and the
  topography. There is no *Wet basisregistratie topografie*, which is why
  [[NL-BRT]] was recorded as the one register with no statute at all.
- **Three of the seven acts are general statutes** that happen to contain a
  registration: [[NL-KADASTERWET]], [[NL-WET-WOZ]] (a valuation act) and
  [[NL-WEGENVERKEERSWET-1994]] (a road traffic act). Four were written to
  constitute a registration.

Neither fact is visible from the register entities. Both are visible from
the statutes, which is the argument for having created them.

**[[NL-BRI]] was the one still open, and is now closed.** Chapter IVA of the
Algemene wet inzake rijksbelastingen is its basis — confirmed directly
against `wetten.overheid.nl`'s own consolidated AWR text on 2026-08-30,
which also corrected the article range from a previously-unchecked "21 to
21k" to the true "21 to 22i".

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

Listed in frontmatter. Five of eight read directly: noraonline.nl,
data.overheid.nl and geobasisregistraties.nl (prior pass), plus
rijksoverheid.nl and Logius's Stelselvoorzieningen page (this pass,
2026-08-28). The three digitaleoverheid.nl pages remain confirmed
genuinely bot-walled on every attempt (a JavaScript verification
challenge, not static content); a vng.nl PDF alternate was fetched in the
prior pass but returned unparseable binary; `web.archive.org` was
attempted this pass but this environment's fetch tool cannot reach that
domain at all. A genuine majority was reached instead via two further
non-digitaleoverheid.nl government sources.
