---
id: AT-EGOVG
type: law
name: E-Government-Gesetz
alternative_names:
  - E-GovG
  - Bundesgesetz über Regelungen zur Erleichterung des elektronischen Verkehrs mit öffentlichen Stellen
description: >
  Austrian federal law facilitating electronic transactions with public
  authorities, in force since 1 January 2005 (BGBl. I Nr. 10/2004). Its
  §§4-7 define the Elektronischer Identitätsnachweis (E-ID) function — a
  "Personenbindung" combining a qualified electronic signature with an
  encrypted Stammzahl and sector-specific personal identifiers (bPK) to
  prove identity uniquely while protecting privacy — which is the legal
  basis for ID Austria. Full operational conditions for issuing the E-ID
  were set by a later regulation, BGBl. II Nr. 340/2023, with most
  provisions applicable from 5 December 2023.

level: national
country: AT
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2005-01-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - AT
  - AT-ID-AUSTRIA
relationships: []

sources:
  - title: "E-Government-Gesetz - Bundesrecht konsolidiert"
    url: "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003230"
    publisher: "Rechtsinformationssystem des Bundes (RIS)"
    accessed: "2026-09-04"
  - title: "Meldegesetz 1991 - Bundesrecht konsolidiert"
    url: "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005799"
    publisher: "Rechtsinformationssystem des Bundes (RIS)"
    accessed: "2026-09-04"
  - title: "Passgesetz 1992 - Bundesrecht konsolidiert"
    url: "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005798"
    publisher: "Rechtsinformationssystem des Bundes (RIS)"
    accessed: "2026-09-04"
  - title: "Personenstandsgesetz 2013 - Bundesrecht konsolidiert"
    url: "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008228"
    publisher: "Rechtsinformationssystem des Bundes (RIS)"
    accessed: "2026-09-04"
  - title: "E-Government-Gesetz: Bestimmungen und Prinzipien"
    url: "https://www.digitalaustria.gv.at/wissenswertes/e-government-a-z/egovernment-gesetz.html"
    publisher: "Digital Austria"
    accessed: "2026-09-04"
---

# E-Government-Gesetz

> **Added 2026-09-04, `verification: primary-source` from creation.**
> [[AT-ID-AUSTRIA]] had previously recorded a claim — sourced only to a
> now-dead `bmdw.gv.at` page — that ID Austria required amendments to
> "the E-Government Act, the Registration Act, the Civil Status Act and
> the Passport Act," and marked it unconfirmed rather than repeat it
> without a live source. This entity closes that gap: all four statutes
> were read directly this pass via `ris.bka.gv.at`, Austria's official
> consolidated-law database, and the finding is a **correction** of the
> original claim, not a confirmation of it — see below.

## Description

The E-Government-Gesetz (E-GovG) is Austria's federal law facilitating
electronic transactions with public bodies, in force since **1 January
2005** (BGBl. I Nr. 10/2004), confirmed by reading `ris.bka.gv.at`'s own
consolidated text directly.

Its **§§4-7** define the **E-ID function** — Elektronischer
Identitätsnachweis — the legal basis ID Austria implements:

- **§4** defines the E-ID as proving unique identity, additional
  attributes and transaction authenticity through a qualified electronic
  signature bound to a "Personenbindung" (personal binding).
- **§4a** requires citizens aged 14 and over to register in person
  through a passport authority or the police, with identity verification.
- **§4b** lists what may be processed: name, birth date, birthplace,
  gender, nationality, the bPK (sector-specific personal identifier),
  contact address, photograph and certificate identity codes.
- **§6** establishes the **Stammzahl** (master number) system — drawn
  from the Zentrales Melderegister (ZMR) for registered residents, and
  from supplementary registers otherwise, with separate identifiers for
  businesses, associations and agricultural operations.
- **§7** names the ministry responsible for digitalisation as the
  administering authority, with power to delegate functions to the
  interior and finance ministries — a provision that pre-dates, and does
  not resolve, the ministry-reorganisation question [[AT-ID-AUSTRIA]]'s
  own file already flags as unresolved.

## One statute, not four

[[AT-ID-AUSTRIA]]'s file had carried, unconfirmed since its `bmdw.gv.at`
source went dead, a claim that ID Austria required **four separate**
legislative amendments. Reading all four statutes directly this pass on
`ris.bka.gv.at` finds a different shape: **only the E-GovG defines and
grants the E-ID function.** The other three each *reference* or
*consume* that same function rather than independently authorising it:

- **Meldegesetz 1991** (residency registration; BGBl. Nr. 9/1992) permits
  online registration and de-registration "unter Verwendung der Funktion
  E-ID" where the requisite data are already in the central register,
  citing the E-GovG as its legal basis.
- **Passgesetz 1992** (passports; BGBl. Nr. 839/1992, in force 1 January
  1993) references the E-GovG's bPK mechanism in its own §22a, and its
  §22b(7) lets citizens request passport-expiry notifications using the
  E-ID function.
- **Personenstandsgesetz 2013** (civil status; BGBl. I Nr. 16/2013)
  states directly that a mother may determine her child's given name
  "unter Verwendung der Funktion E-ID (§§4 ff E-GovG)" — again citing the
  E-GovG's own sections, not a standalone civil-status power.

So the original four-statute claim was not wrong about which laws are
involved, but it implied four independent legal bases where the primary
sources show one: the E-GovG grants the E-ID function, and the other
three statutes are consumers of it. No relationship is asserted from
this entity to the Meldegesetz, Passgesetz or Personenstandsgesetz —
none of the three is an Atlas entity, and the citation runs the other
way (each cites the E-GovG, not vice versa).

## Operationalised in 2023, amended since

The E-ID provisions above existed in the E-GovG before 2023, but the
conditions for their **operational use** were set by a separate
regulation, **BGBl. II Nr. 340/2023**, with most cited provisions
applicable from **5 December 2023** — this is a Verordnung (ordinance)
issued under the Act, not a novelle (amending act) to the Act itself, a
distinction an earlier WebSearch-only pass would have missed. A further
amendment, **BGBl. I Nr. 117/2024**, is referenced but its content was
not read this pass.

## Relationships

None asserted from this entity. [[AT-ID-AUSTRIA]] should carry the
inbound `governed-by` edge to this law.

## Sources

Listed in frontmatter. The four RIS pages (E-GovG, Meldegesetz 1991,
Passgesetz 1992, Personenstandsgesetz 2013) and the Digital Austria page
were all read directly this pass.
