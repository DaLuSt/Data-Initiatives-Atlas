---
id: NL-WOZ
type: platform
name: Basisregistratie Waarde Onroerende Zaken
alternative_names:
  - WOZ
  - BR WOZ
  - Base Registry of Real Estate Values
description: >
  The Dutch base registry of real property values, and one of the ten
  registrations in the stelsel van basisregistraties. Municipalities are the
  data source and are responsible for entering data in the Landelijke
  Voorziening WOZ and for its quality. The Waarderingskamer supervises
  whether municipalities properly implement the Wet WOZ, supervises the
  implementation of the base registry, acts as functional manager of the
  national facility, and publishes the IMWOZ information model and the WOZ
  catalogues that specify its content. The Kadaster manages the national
  facility technically. The register holds the WOZ value, the cadastral
  reference, address data and stakeholder data of WOZ objects, and is used
  by the tax administration, water boards and municipalities for taxation.

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
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-WAARDERINGSKAMER
related_entities:
  - NL-WET-WOZ
  - NL-BASISREGISTRATIES
  - NL-WAARDERINGSKAMER
  - NL-KADASTER
  - NL-BELASTINGDIENST
  - NL-BRK
relationships:
  - type: governed-by
    target: NL-WET-WOZ
    source: fact
    evidence: "The Wet waardering onroerende zaken, adopted in 1994, regulates the valuation of all real estate in the Netherlands for tax collection and the housing valuation system, and is the statutory basis of the Basisregistratie Waarde Onroerende Zaken (wetten.overheid.nl/BWBR0007119; nl.wikipedia.org 'Wet waardering onroerende zaken'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR, BAG, BRT, BRK, BRV, BRI, WOZ (Basisregistratie Waarde Onroerende Zaken), BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-WAARDERINGSKAMER
    source: fact
    evidence: "The Waarderingskamer supervises the implementation of the Wet WOZ and of the Basisregistratie WOZ, is the functional manager of the LV-WOZ, and publishes the IMWOZ information model that is the basis for the specification of the content of the Basisregistratie WOZ, the content of the LV-WOZ and the further registration municipalities keep (waarderingskamer.nl 'Landelijke Voorziening WOZ'; waarderingskamer.nl Catalogus Basisregistratie WOZ v1.8; waarderingskamer.nl IMWOZ). NOT READ — search-only. CAVEAT: municipalities are the data source and the Kadaster manages the LV-WOZ technically; this edge records the functional-management and specification role."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Landelijke Voorziening WOZ"
    url: "https://www.waarderingskamer.nl/voor-gemeenten/gegevensbeheer/lv-woz"
    publisher: "Waarderingskamer"
  - title: "Catalogus Basisregistratie WOZ versie 1.8"
    url: "https://www.waarderingskamer.nl/documenten/03.-Voor-gemeenten/04.-Gegevensbeheer/Catalogus-Basisregistratie-WOZ-versie-1.8.pdf"
    publisher: "Waarderingskamer"
  - title: "WOZ — Waardering Onroerende Zaken | Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/landelijke-voorzieningen/woz"
    publisher: "Kadaster"
  - title: "Waarde Onroerende Zaken | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties/woz"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
  - title: "Waardering Onroerende Zaken (WOZ) | CBS"
    url: "https://www.cbs.nl/nl-nl/deelnemers-enquetes/decentrale-overheden/vastgoed-overheden/waardering-onroerende-zaken--woz--"
    publisher: "Centraal Bureau voor de Statistiek (CBS)"
---

# WOZ — Basisregistratie Waarde Onroerende Zaken

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The WOZ base registry holds the assessed value of real property. It contains
the **WOZ value, the cadastral reference, address data and stakeholder
data** of WOZ objects in the Netherlands.

It is used by the [[NL-BELASTINGDIENST]] for income tax (the owner-occupied
home allowance), corporate income tax, gift and inheritance tax and the
landlord levy, and by water boards and municipalities for their own taxes.

## Three organisations, three distinct roles, one register

The WOZ is the clearest case in the stelsel of a register with **no single
owner**, and it is the reason the stelsel's own documentation describes
roles rather than owners:

| Role | Party | What they do |
|---|---|---|
| **Data source / holder** | municipalities | determine values, enter data in the LV-WOZ, responsible for quality |
| **Supervisor + functional manager + specification author** | [[NL-WAARDERINGSKAMER]] | supervises implementation of the Wet WOZ and the register; functional manager of the LV-WOZ; publishes IMWOZ and the catalogues |
| **Technical manager** | [[NL-KADASTER]] | manages the LV-WOZ for authorised users |

The Atlas's `maintained-by` edge points at the **Waarderingskamer**, because
of the three roles that one comes closest to what `maintained-by` means: it
defines what the register is and supervises its production.

That is a judgement, and it is recorded as one — the caveat is written into
the relationship's own `evidence` string, not just here, so a reader
querying the graph data sees it without opening this file.

**The municipalities remain unmodelled**, as they do for [[NL-BAG]] and
[[NL-BGT]]. For the WOZ that omission removes the party that actually
determines the values.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-WAARDERINGSKAMER]] — see the role table above.

**The Belastingdienst's use of this register is not modelled.** It is the
single most consequential "afnemer" relationship in the stelsel — WOZ values
feed several national taxes — and the Atlas has no relationship type for
authorised use. See [[NL-BELASTINGDIENST]].

## Sources

Listed in frontmatter — three Waarderingskamer publications, the Kadaster's
LV-WOZ page, the geobasisregistraties entry and the CBS page describing who
needs the values.
