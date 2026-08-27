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
verification: primary-source

start_date: 2016-01-01
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
  - NL-WET-BGT
  - NL-BASISREGISTRATIES
  - NL-KADASTER
  - NL-BRT
  - NL-VNG
relationships:
  - type: governed-by
    target: NL-WET-BGT
    source: fact
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0034026 directly (2026-08-27): it is the Wet basisregistratie grootschalige topografie, enacted 25 September 2013, with entry into force set by royal decree per article. kadaster.nl's own BGT page, read directly, states plainly: 'Op 1 januari 2016 is de wet in werking getreden voor bronhouders en de Landelijke Voorziening (LV-BGT)' (the Act entered into force on 1 January 2016 for bronhouders and the national facility) — confirming the date independently of the eerstekamer.nl dossier, which was not re-fetched this pass."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading data.overheid.nl's basisregistraties_10 group listing directly (2026-08-27): it names all ten registers by exact abbreviation, including BGT (Basisregistratie Grootschalige Topografie). digitaleoverheid.nl's BGT page, also read directly, describes the same register though the page does not itself enumerate all ten."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KADASTER
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own BGT page directly (2026-08-27): Kadaster operates the national facility (Landelijke Voorziening BGT), handling quality control and data distribution to the seven bronhouder categories — confirmed by name via VNG's own article, read directly: 'Gemeenten, provincies en waterschappen maken de BGT samen met het ministerie van Landbouw, Natuur en Voedselkwaliteit (LNV), Defensie en Infrastructuur en Waterstaat (IenW)', coordinated through the Samenwerkingsverband Bronhouders voor de BGT (SVB-BGT), established 1 April 2014 per the same VNG page. CAVEAT unchanged: the bronhouders hold the data; this edge records the national-facility role only."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Basisregistratie Grootschalige Topografie (BGT) — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties/bgt"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Basisregistratie Grootschalige Topografie (BGT) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bgt/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Basisregistratie Grootschalige Topografie (BGT) | VNG"
    url: "https://vng.nl/artikelen/basisregistratie-grootschalige-topografie-bgt"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-27"
  - title: "Wet basisregistratie grootschalige topografie — official text"
    url: "https://wetten.overheid.nl/BWBR0034026"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
  - title: "Regels omtrent de basisregistratie grootschalige topografie (Wet basisregistratie grootschalige topografie) (not re-read this pass)"
    url: "https://www.tweedekamer.nl/kamerstukken/brieven_regering/detail?id=2025D12647&did=2025D12647"
    publisher: "Tweede Kamer der Staten-Generaal"
---

# BGT — Basisregistratie Grootschalige Topografie

> **Verified 2026-08-27.** Four of five cited pages were read directly, plus
> the official BWBR0034026 text added as a new source and read: Kadaster's
> and VNG's own pages confirm the 1 January 2016 commencement and the seven
> bronhouder categories by name. The Tweede Kamer document was not re-fetched.

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

Listed in frontmatter, four of five read directly this pass plus the
official BWBR0034026 text added and read — the Kadaster and
digitaleoverheid.nl register pages, the VNG article written for
municipalities as bronhouders, and the Act's own text. The Tweede Kamer
document was not re-fetched.
