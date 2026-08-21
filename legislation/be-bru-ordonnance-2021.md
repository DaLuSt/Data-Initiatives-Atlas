---
id: BE-BRU-ORDONNANCE-2021
type: law
name: Ordonnance du 10 décembre 2021 modifiant l'ordonnance du 27 octobre 2016
alternative_names:
  - Brussels open data ordonnance
  - Ordonnance open data (Bruxelles)
description: >
  Ordonnance of the Brussels-Capital Region of 10 December 2021 amending the
  ordonnance of 27 October 2016 establishing an open data policy, transposing
  Directive (EU) 2019/1024 on open data and the re-use of public sector
  information. It strengthens access to and re-use of public data, requires
  availability in open, interoperable and accessible formats, improves the
  conditions of re-use and widens the categories of data covered.

level: subnational
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-12-10
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE
  - EU-OPEN-DATA-DIRECTIVE
  - BE-HERGEBRUIK-WET-2023
  - BE-VL-BESTUURSDECREET-2021
  - BE-WAL-DECRET-2022
relationships:
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "Ordonnance du 10 décembre 2021 modifiant l'ordonnance du 27 octobre 2016 visant à l'établissement d'une politique de données ouvertes et portant transposition de la directive 2019/1024/UE du Parlement européen et du Conseil du 20 juin 2019 (refonte) concernant les données ouvertes et la réutilisation des informations du secteur public (etaamb.openjustice.be ordonnance-du-10-decembre-2021 n2021034364; ibsa.brussels/opendata). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-12-10
    valid_until: null
  - type: amends
    target: BE-BRU-ORDONNANCE-2016
    source: fact
    evidence: "The ordonnance of 10 December 2021 modifies the ordonnance of 27 October 2016 establishing an open data policy for the Brussels-Capital Region, which continues to exist under its own name and date (etaamb.openjustice.be n2021034364; ejustice.just.fgov.be ordonnance open data, cn=2016102705). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-12-10
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "The ordonnance is an act of the Brussels-Capital Region, a constituent unit of Belgium (etaamb.openjustice.be n2021034364). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3; the Atlas has no sub-national anchor entities, so a subnational instrument anchors to its state."
    confidence: medium
    valid_from: 2021-12-10
    valid_until: null

sources:
  - title: "Ordonnance du 10 décembre 2021 modifiant l'ordonnance du 27 octobre 2016 visant à l'établissement d'une politique de données ouvertes et portant transposition de la directive 2019/1024/UE"
    url: "https://etaamb.openjustice.be/fr/ordonnance-du-10-decembre-2021_n2021034364"
    publisher: "eTaamb — OpenJustice (Belgisch Staatsblad / Moniteur belge)"
  - title: "Ordonnance du 27 octobre 2016 visant à l'établissement d'une politique de données ouvertes"
    url: "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?cn=2016102705&la=F&language=fr&table_name=loi"
    publisher: "Service public fédéral Justice — Moniteur belge"
  - title: "Open Data — Institut bruxellois de statistique et d'analyse"
    url: "https://ibsa.brussels/opendata"
    publisher: "Institut bruxellois de statistique et d'analyse (IBSA)"
---

# Brussels open data ordonnance (10 December 2021)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

An **ordonnance** of the Brussels-Capital Region of **10 December 2021**,
amending the region's ordonnance of **27 October 2016** on open data policy
to transpose [[EU-OPEN-DATA-DIRECTIVE]]. It:

- requires public data in **open, interoperable and accessible formats**;
- improves the conditions of re-use;
- widens the categories of data covered.

## Brussels had an open data policy five years before the directive

The instrument this one amends dates from **27 October 2016** — two and a half
years before Directive (EU) 2019/1024 was adopted. Brussels was not building
an open data regime because Europe required one; it already had one, and the
2021 ordonnance adapted it.

That is the same shape three of the five Open Data Directive transpositions
already in the Atlas turned out to have, and the reason the `amends`
relationship type exists at all: an amending act carries **both** `amends`,
for the instrument it edits, and `implements-requirement-from`, for the
obligation it discharges. This entity carries both.

## The Belgian timeline, now visible

| Level | Instrument | Date |
|---|---|---|
| Flanders | [[BE-VL-BESTUURSDECREET-2021]] | 2 July 2021 (in force 17 July) |
| **Brussels-Capital** | **this ordonnance** | **10 December 2021** |
| Wallonia | [[BE-WAL-DECRET-2022]] | 24 November 2022 |
| Federal | [[BE-HERGEBRUIK-WET-2023]] | 25 December 2023 |

Brussels was **five months late** against the 17 July 2021 deadline — late,
but by less than a year, and more than two years ahead of the federal act.

## Relationships

- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]].
- `amends` [[BE-BRU-ORDONNANCE-2016]], the 2016 ordonnance it edits.
- `applies-in` [[BE]] — see [[BE-VL-BESTUURSDECREET-2021]] on why a
  subnational instrument anchors to its state.

## Sources

Listed in frontmatter — the published text on eTaamb, the 2016 ordonnance on
the Moniteur belge, and the Brussels statistical institute's open data page.
