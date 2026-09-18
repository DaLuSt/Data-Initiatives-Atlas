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
verification: primary-source

start_date: 2018-01-01
end_date: null
last_verified: "2026-09-18"
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
  - NL-DINOLOKET
relationships:
  - type: governed-by
    target: NL-WET-BRO
    source: fact
    evidence: "Confirmed by reading basisregistratieondergrond.nl's own page directly (2026-08-27): 'Vanaf 1 januari 2018 is de Wet Basisregistratieondergrond (Bro) van kracht' — the Act entered into force 1 January 2018, and functions as a framework law whose specific data requirements are added in phases ('tranches') via the Besluit Bro and Regeling Bro. digitaleoverheid.nl's own BRO page, also read directly, independently confirms the same date. wetten.overheid.nl's official text of BWBR0037095, also read directly this pass, confirms it as the Wet basisregistratie ondergrond ('een basisregistratie van de ondergrond, bestaande uit gegevens en modellen met betrekking tot de ondergrond van Nederland en het continentaal plat', Article 2), signed 30 September 2015 and published in the Staatsblad 16 October 2015, with commencement of individual articles set by royal decree per Article 43 — consistent with, not contradicting, the 1 January 2018 in-force date the programme pages give for the substantive obligations."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own BRO page directly (2026-08-27), which describes the BRO as comprising roughly 26 registration objects across six domains (groundwater monitoring, groundwater use, mining law, soil research, soil quality, models) rather than enumerating all ten basisregistraties on the same page; data.overheid.nl's basisregistraties_10 group listing, also read directly this pass, names 'Basisregistratie: Ondergrond (BRO)' among the ten."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-TNO
    source: fact
    evidence: "Confirmed by reading geologischedienst.nl's own announcement directly (2026-08-27): 'Het beheer van de BRO is vanaf 1 januari 2022 in handen van de Geologische Dienst Nederland (GDN), onderdeel van TNO' — GDN/TNO took over BRO management from that date, not from the register's 2018 commencement. The statutory-tasks page, also read directly, confirms GDN 'has implemented the BRO system and, as of 2022, is responsible for its management and continued development,' with the Ministry of Interior Affairs retaining strategic oversight. CORRECTION: the `valid_from: 2018-01-01` on this edge should more precisely read 2022-01-01 for TNO's management role specifically, though TNO/GDN was already the technical implementer before that date; left unchanged pending a clearer split between 'implementer' and 'official manager' than the Atlas's vocabulary currently draws. CAVEAT unchanged: the bronhouders supply the data; this edge records the national-facility role."
    confidence: high
    valid_from: 2018-01-01
    valid_until: null

sources:
  - title: "Basisregistratie Ondergrond (BRO) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/bro/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "TNO officieel beheerder van de Basisregistratie Ondergrond"
    url: "https://www.geologischedienst.nl/nieuws/tno-officieel-beheerder-van-de-basisregistratie-ondergrond/"
    publisher: "Geologische Dienst Nederland — TNO"
    accessed: "2026-08-27"
  - title: "Basisregistratie Ondergrond — wettelijke taken"
    url: "https://www.geologischedienst.nl/en/about-gdn/statutory-tasks/national-key-registry-subsurface-bro/"
    publisher: "Geologische Dienst Nederland — TNO"
    accessed: "2026-08-27"
  - title: "Wet Bro | Basisregistratieondergrond"
    url: "https://basisregistratieondergrond.nl/inhoud-bro/wet-bro/"
    publisher: "Basisregistratie Ondergrond (programmabureau)"
    accessed: "2026-08-27"
  - title: "BRO — Basisregistratie Ondergrond | Geonovum"
    url: "https://www.geonovum.nl/geo-standaarden/bro-basisregistratie-ondergrond"
    publisher: "Geonovum"
    accessed: "2026-08-27"
  - title: "Wet basisregistratie ondergrond — official text"
    url: "https://wetten.overheid.nl/BWBR0037095"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
  - title: "Actuele bodeminformatie voor een leefbaar landschap"
    url: "https://www.wur.nl/nl/nieuws/actuele-bodeminformatie-voor-een-leefbaar-landschap"
    publisher: "Wageningen University & Research (WUR)"
    accessed: "2026-09-18"
---

# BRO — Basisregistratie Ondergrond

> **Verified 2026-08-27.** All five cited pages read directly. One
> correction: TNO/GDN became the BRO's *official manager* on 1 January 2022,
> not at the register's 2018 commencement — the entity previously implied a
> single continuous role. Geonovum's own page, read directly, also confirms
> it is standards lead (trekker), not merely a publisher, closing a caveat
> the entity previously left open.
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #140): BIS's own
> current operator and status, the one gap left after DINO's own closure,
> are now sourced too — see "The only register in the stelsel built by
> merging predecessors" below.

## Description

The BRO is the **newest** of the ten base registries: a national facility
holding reliable information about Dutch soil and subsurface, accessible to
everyone. Its statute, the **Wet basisregistratie ondergrond**, came into
force on **1 January 2018**, and the register is being **implemented in
phases**.

[[NL-TNO]], as the **Geological Survey of the Netherlands (GDN)**, built the
national facility from the start and has been its **official manager since
1 January 2022** — a date confirmed by reading geologischedienst.nl's own
announcement directly this pass, correcting the entity's previous
implication of one continuous role since 2018. The **bronhouders** are
government bodies: municipalities, provinces, water boards, Rijkswaterstaat
and the Netherlands Enterprise Agency.

## The only register in the stelsel built by merging predecessors

The BRO **builds on two existing registrations**:

- **DINO** — *Data en Informatie van de Nederlandse Ondergrond*, held by the
  Geological Survey at TNO;
- **BIS** — the soil information system from Alterra at Wageningen UR.

That makes it the only one of the ten whose creation is described as a
consolidation of things that already existed, rather than a new registration
of data government already held.

**Narrowed 2026-09-17**: DINO's continuing existence is now modelled.
[[NL-DINOLOKET]], the public portal TNO's Geologische Dienst Nederland
operates, delivers both DINO's own data and the BRO's — confirmed by
reading the portal's own pages directly. No `previous_version` or
`supersedes` relationship is asserted between the two: the sources say the
BRO *builds on* DINO, which is weaker than supersession, and DINO
continues to exist as a distinct data source served through the same
portal.

**BIS closed 2026-09-18.** Wageningen University & Research's own news
page, "Actuele bodeminformatie voor een leefbaar landschap" (published
13 March 2024, updated 12 December 2024), read directly, confirms BIS
Nederland — the *Bodemkundig Informatie Systeem*, comprising the Soil
Map, the Geomorphological Map, the Groundwater Table Depth Model and
associated boreholes and soil analyses — is still actively maintained:
*"De informatie wordt door WENR actueel gehouden voor het ministerie van
LNV"* (the information is kept current by WENR for the Ministry of
Agriculture, Nature and Food Quality). WENR — Wageningen Environmental
Research, Alterra's renamed successor since 2016 — is neither TNO nor
otherwise an existing Atlas entity, and is not created here on one news
page alone. The same source states BIS's data is *"beschikbaar gesteld
in de Basisregistratie Ondergrond"* (made available within the BRO),
served alongside additional detail and thematic maps through two
portals, `bodemdata.nl` and `broloket.nl` — the same continuing-source,
not-superseded relationship already established for DINO. No entity or
edge is added for WENR or the bodemdata.nl portal; the operator and
status question the row asked is answered in prose.

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

[[NL-GEONOVUM]] is confirmed, by reading its own BRO standards page directly
this pass, to be **trekker** (lead) for developing BRO's standards — 'Geonovum
is trekker for making the standards of the BRO,' working with TNO/GDN and
outside subject-matter experts to produce the catalogues, handbooks and
interface descriptions for each registration object. That is a stronger
claim than "merely publishes them," closing the caveat this entity
previously left open, and is listed as a `related_entities` association
still; **no relationship is asserted**, since the Atlas has no type for a
standards-lead role distinct from `maintained-by`.

## Sources

Listed in frontmatter. All five original sources read directly in the
2026-08-27 pass, plus the Act's own official text (BWBR0037095) — the
digitaleoverheid.nl register page, two Geological Survey pages including
the announcement of TNO/GDN's 2022 appointment as official manager, the
programme office's page on the Act, and the Geonovum standards page
confirming its lead role. WUR's own news page on BIS Nederland, added
and read directly 2026-09-18, closes the BIS operator/status question.
