---
id: NL-BRO
type: platform
name: Basisregistratie Ondergrond
alternative_names:
  - BRO
  - Base Registry of the Subsurface
  - Key Register of the Subsurface
description: >
  The Dutch base registry of the subsurface: a national facility holding
  reliable information about Dutch soil and subsurface, accessible to
  everyone, and the newest of the ten registrations in the stelsel van
  basisregistraties. Its statutory basis is the Wet basisregistratie
  ondergrond, in force from 1 January 2018, and it is being implemented in
  phases. It builds on two predecessor registrations: DINO, held by the
  Geological Survey of the Netherlands at TNO, and the soil information
  system BIS from Alterra at Wageningen UR. TNO, as the Geological Survey of
  the Netherlands, is the designated developer and manager of the national
  facility; the bronhouders are government bodies including municipalities,
  provinces, water boards, Rijkswaterstaat and the Netherlands Enterprise
  Agency.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2018-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-TNO
related_entities:
  - NL-WET-BRO
  - NL-BASISREGISTRATIES
  - NL-TNO
  - NL-GEONOVUM
relationships:
  - type: governed-by
    target: NL-WET-BRO
    source: fact
    evidence: "The Wet basisregistratie ondergrond is the statutory basis of the Basisregistratie Ondergrond and entered into force on 1 January 2018, with articles 27 and 29 following on 1 July 2018 (wetten.overheid.nl/BWBR0037095; basisregistratieondergrond.nl 'Wet Bro'; wetten.overheid.nl/BWBR0040439). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT, BRK, BRV, BRI, WOZ, BGT and BRO (Basisregistratie Ondergrond); the BRO is described as the newest of them (digitaleoverheid.nl '10 basisregistraties' and BRO page; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-TNO
    source: fact
    evidence: "TNO, part of the Geological Survey of the Netherlands (GDN), is designated as the developer and manager of the National Facility (LV) BRO; the Geological Survey publishes it among its statutory tasks and announced that TNO is the official manager of the Basisregistratie Ondergrond (geologischedienst.nl 'TNO officieel beheerder van de Basisregistratie Ondergrond'; geologischedienst.nl statutory tasks page; basisregistratieondergrond.nl). NOT READ — search-only. CAVEAT: the bronhouders — municipalities, provinces, water boards, Rijkswaterstaat and RVO — supply the data; this edge records the national-facility role."
    confidence: medium
    valid_from: 2018-01-01
    valid_until: null

sources:
  - title: "Basisregistratie Ondergrond (BRO) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bro/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "TNO officieel beheerder van de Basisregistratie Ondergrond"
    url: "https://www.geologischedienst.nl/nieuws/tno-officieel-beheerder-van-de-basisregistratie-ondergrond/"
    publisher: "Geologische Dienst Nederland — TNO"
  - title: "Basisregistratie Ondergrond — wettelijke taken"
    url: "https://www.geologischedienst.nl/en/about-gdn/statutory-tasks/national-key-registry-subsurface-bro/"
    publisher: "Geologische Dienst Nederland — TNO"
  - title: "Wet Bro | Basisregistratieondergrond"
    url: "https://basisregistratieondergrond.nl/inhoud-bro/wet-bro/"
    publisher: "Basisregistratie Ondergrond (programmabureau)"
  - title: "BRO — Basisregistratie Ondergrond | Geonovum"
    url: "https://www.geonovum.nl/geo-standaarden/bro-basisregistratie-ondergrond"
    publisher: "Geonovum"
---

# BRO — Basisregistratie Ondergrond

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BRO is the **newest** of the ten base registries: a national facility
holding reliable information about Dutch soil and subsurface, accessible to
everyone. Its statute, the **Wet basisregistratie ondergrond**, came into
force on **1 January 2018**, and the register is being **implemented in
phases**.

[[NL-TNO]], as the **Geological Survey of the Netherlands**, is the
designated developer and manager of the national facility. The **bronhouders**
are government bodies: municipalities, provinces, water boards,
Rijkswaterstaat and the Netherlands Enterprise Agency.

## The only register in the stelsel built by merging predecessors

The BRO **builds on two existing registrations**:

- **DINO** — *Data en Informatie van de Nederlandse Ondergrond*, held by the
  Geological Survey at TNO;
- **BIS** — the soil information system from Alterra at Wageningen UR.

That makes it the only one of the ten whose creation is described as a
consolidation of things that already existed, rather than a new registration
of data government already held.

**Neither predecessor is modelled**, and no `previous_version` or
`supersedes` relationship is asserted. The sources say the BRO *builds on*
them, which is weaker than supersession — DINO in particular appears to
continue to exist. Asserting `supersedes` would claim the predecessors
stopped, which nothing read says.

## It is phased, and the Atlas cannot say so

`status: active` is correct — the Act is in force and the register operates
— but the sources are equally clear that implementation is **in phases** and
therefore incomplete.

The Atlas's `status` vocabulary has no value for "in force and partially
implemented". `planned` would be wrong, `active` is what is recorded, and
the phasing appears only in this prose. It is a smaller instance of the same
problem [[ES-LCGC]] raised from the other end.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-TNO]] — national facility only; the bronhouders
  supply the data.

[[NL-GEONOVUM]] publishes BRO geo-standards according to its own pages, and
is listed as a `related_entities` association. **No relationship is
asserted**: whether Geonovum maintains those standards, or merely publishes
them for the programme, was not established.

## Sources

Listed in frontmatter — the digitaleoverheid.nl register page, two
Geological Survey pages including the announcement of TNO's appointment, the
programme office's page on the Act, and the Geonovum standards page.
