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
    evidence: "Confirmed by reading wetten.overheid.nl's own text of BWBR0007119 directly (2026-08-27): 'Deze wet wordt aangehaald als: Wet waardering onroerende zaken' (Article 47), enacted by royal decree 15 December 1994 and in force from 1 January 1995. It designates the Waarderingskamer to oversee valuation and assessment for tax purposes — confirmed independently by waarderingskamer.nl's own pages, also read directly, which cite Article 4 of the Wet WOZ as the source of the Waarderingskamer's own tasks and powers."
    confidence: high
    valid_from: null
    valid_until: null
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "Confirmed by reading geobasisregistraties.nl's own WOZ page directly (2026-08-27), which places the WOZ's value question alongside the address, ownership, function/dimension and subsurface registers as one of the coordinated geo base registrations, and data.overheid.nl's basisregistraties_10 group listing (read directly for sibling entities this pass), which names 'Basisregistratie: Waardering Onroerende Zaken (WOZ)' among the ten."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-WAARDERINGSKAMER
    source: fact
    evidence: "Confirmed by reading kadaster.nl's own LV-WOZ page directly (2026-08-27): 'De Waarderingskamer [is] functioneel beheerder van de LV-WOZ' (the Waarderingskamer is functional manager of the LV-WOZ), while the Kadaster is 'technisch verantwoordelijk' (technically responsible) and municipalities are the bronhouder determining values. geobasisregistraties.nl's own page, also read directly, independently confirms the same three-way split: 'The Waarderingskamer controls whether municipalities execute the [Wet Woz] according to the rules' and 'safeguards the quality of WOZ implementation.' The Waarderingskamer's own catalogue PDF and its LV-WOZ page (503 error this pass) were not readable; the specification role (IMWOZ, the catalogues) is instead confirmed via [[NL-WAARDERINGSKAMER]]'s own re-verified pages this pass. CAVEAT unchanged: municipalities are the data source; Kadaster manages the LV-WOZ technically; this edge records the functional-management and specification role."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Landelijke Voorziening WOZ (503 error this pass, not read)"
    url: "https://www.waarderingskamer.nl/voor-gemeenten/gegevensbeheer/lv-woz"
    publisher: "Waarderingskamer"
  - title: "Catalogus Basisregistratie WOZ versie 1.8 (fetched; binary PDF, not machine-readable)"
    url: "https://www.waarderingskamer.nl/documenten/03.-Voor-gemeenten/04.-Gegevensbeheer/Catalogus-Basisregistratie-WOZ-versie-1.8.pdf"
    publisher: "Waarderingskamer"
  - title: "WOZ — Waardering Onroerende Zaken | Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/landelijke-voorzieningen/woz"
    publisher: "Kadaster"
    accessed: "2026-08-27"
  - title: "Waarde Onroerende Zaken | Geobasisregistraties"
    url: "https://www.geobasisregistraties.nl/basisregistraties/woz"
    publisher: "Geobasisregistraties (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Waardering Onroerende Zaken (WOZ) | CBS"
    url: "https://www.cbs.nl/nl-nl/deelnemers-enquetes/decentrale-overheden/vastgoed-overheden/waardering-onroerende-zaken--woz--"
    publisher: "Centraal Bureau voor de Statistiek (CBS)"
    accessed: "2026-08-27"
  - title: "Wet waardering onroerende zaken — official text"
    url: "https://wetten.overheid.nl/BWBR0007119"
    publisher: "Overheid.nl (Basiswettenbestand)"
    accessed: "2026-08-27"
---

# WOZ — Basisregistratie Waarde Onroerende Zaken

> **Verified 2026-08-27.** Four of six cited pages read directly, plus the
> Wet WOZ's own official text added and read as a new source. The
> Waarderingskamer's LV-WOZ page returned a 503 this pass and its catalogue
> is a binary PDF with no extractable text — both confirmed unreadable, not
> merely unread — but the same facts are independently confirmed via
> kadaster.nl's own LV-WOZ page and [[NL-WAARDERINGSKAMER]]'s own
> re-verified pages.

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
- `governed-by` [[NL-WET-WOZ]] — confirmed this pass by reading the Act's
  own official text.

**The Belastingdienst's use of this register is not modelled.** It is the
single most consequential "afnemer" relationship in the stelsel — WOZ values
feed several national taxes — and the Atlas has no relationship type for
authorised use. See [[NL-BELASTINGDIENST]].

## Sources

Listed in frontmatter, four of six read directly this pass, plus the Wet
WOZ's own official text added and read — the Kadaster's LV-WOZ page, the
geobasisregistraties entry, the CBS page describing who needs the values,
and the Act itself. The Waarderingskamer's own LV-WOZ page (503 this pass)
and its catalogue PDF (binary, not machine-readable) were not read; the same
substance is confirmed instead via kadaster.nl, geobasisregistraties.nl and
[[NL-WAARDERINGSKAMER]]'s own re-verified pages.
