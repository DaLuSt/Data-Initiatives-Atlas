---
id: NL-BGT
type: platform
name: Basisregistratie Grootschalige Topografie
alternative_names:
  - BGT
  - Base Registry of Large-Scale Topography
description: >
  The Dutch base registry of large-scale topography: a digital map of the
  Netherlands on which buildings, roads, waterways, land and railway lines
  are uniquely recorded, accurate to 20 centimetres. Its statutory basis is
  the Wet basisregistratie grootschalige topografie, in force from 1 January
  2016 for the bronhouders and the national facility, with the map
  nationally complete on 1 July 2017 when the statutory usage requirement
  took effect. Municipalities, provinces, water boards, Rijkswaterstaat,
  ProRail, the Ministry of Defence and RVO are the bronhouders, each
  responsible for their own part of the map and organised in the
  Samenwerkingsverband Bronhouders BGT. The Kadaster is the provider of the
  national facility. Use is free for everyone and mandatory for government
  bodies and other statutory users.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2016-01-01
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
  - NL-WET-BGT
  - NL-BASISREGISTRATIES
  - NL-KADASTER
  - NL-BRT
  - NL-VNG
relationships:
  - type: governed-by
    target: NL-WET-BGT
    source: fact
    evidence: "The Wet basisregistratie grootschalige topografie is the statutory basis of the Basisregistratie Grootschalige Topografie; its provisions on the register's content and on the obligations of bronhouders and the register holder entered into force on 1 January 2016 (wetten.overheid.nl/BWBR0034026; eerstekamer.nl dossier 33.527). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT, BRK, BRV, BRI, WOZ, BGT (Basisregistratie Grootschalige Topografie) and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "The data is registered in the Landelijke Voorziening BGT, from which the Kadaster as the BGT provider makes data available to users; the Kadaster is the provider of the national BGT (kadaster.nl BGT page; digitaleoverheid.nl BGT page; vng.nl BGT article). NOT READ — search-only. CAVEAT: the bronhouders — municipalities, provinces, water boards, Rijkswaterstaat, ProRail, Defence and RVO — hold the data; this edge records the national-facility role only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistratie Grootschalige Topografie (BGT) — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bgt"
    publisher: "Kadaster"
  - title: "Basisregistratie Grootschalige Topografie (BGT) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bgt/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistratie Grootschalige Topografie (BGT) | VNG"
    url: "https://vng.nl/artikelen/basisregistratie-grootschalige-topografie-bgt"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
  - title: "Regels omtrent de basisregistratie grootschalige topografie (Wet basisregistratie grootschalige topografie)"
    url: "https://www.tweedekamer.nl/kamerstukken/brieven_regering/detail?id=2025D12647&did=2025D12647"
    publisher: "Tweede Kamer der Staten-Generaal"
---

# BGT — Basisregistratie Grootschalige Topografie

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BGT is a **digital map of the Netherlands accurate to 20 centimetres**,
on which buildings, roads, waterways, land and railway lines are uniquely
recorded.

Its statute, the **Wet basisregistratie grootschalige topografie**, came into
force on **1 January 2016** for the bronhouders and the national facility.
The map was **nationally complete on 1 July 2017**, when the statutory usage
requirement took effect.

Use is **free for everyone** and **mandatory for government bodies** and
other statutory users.

## The most distributed register in the stelsel

The BGT has **seven categories of bronhouder** — municipalities, provinces,
water boards, Rijkswaterstaat, ProRail, the Ministry of Defence and RVO —
each responsible for its own section of one national map, organised in the
**Samenwerkingsverband Bronhouders voor de BGT (SVB-BGT)**.

That is a genuinely unusual arrangement: a single authoritative dataset
whose parts are maintained by different tiers of government and by two
infrastructure operators, stitched together into one facility.

**The Atlas models almost none of it.** [[NL-KADASTER]] carries the
`maintained-by` edge because it runs the national facility and is the party
the Atlas can name. Of the seven bronhouder categories:

- **municipalities, provinces and water boards** — no entities; the `level`
  vocabulary has `local` but there is no obvious collective entity to create;
- **Rijkswaterstaat, ProRail, Defence, RVO** — no entities; none was
  researched;
- **SVB-BGT** — no entity; named in one source only.

So the graph shows a register maintained by one organisation. **Seven kinds
of body actually maintain it.** This is the same shape as the WOZ and the
BAG, and it is logged in `discovery/unresolved.md` as a single finding
rather than three.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KADASTER]] — national facility only; see above.

**No relationship to [[NL-BRT]] is asserted**, though both are topographic
base registries. See [[NL-BRT]] for the difference between them.

## Sources

Listed in frontmatter — the Kadaster and digitaleoverheid.nl register pages,
the VNG article written for municipalities as bronhouders, and a Tweede
Kamer document on the Act.
