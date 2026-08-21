---
id: BE-BRU-ORDONNANCE-2016
type: law
name: Ordonnance du 27 octobre 2016 visant à l'établissement d'une politique de données ouvertes
alternative_names:
  - Brussels open data ordonnance (2016)
  - Ordonnance open data 2016
description: >
  Ordonnance of the Brussels-Capital Region of 27 October 2016 establishing an
  open data policy for the region. It predates Directive (EU) 2019/1024 by two
  and a half years and remains in force, having been amended on 10 December
  2021 by the ordonnance that transposes that directive.

level: subnational
country: BE
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 2016-10-27
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE
  - BE-BRU-ORDONNANCE-2021
relationships:
  - type: applies-in
    target: BE
    source: fact
    evidence: "Ordonnance du 27 octobre 2016 visant à l'établissement d'une politique de données ouvertes, an act of the Brussels-Capital Region, a constituent unit of Belgium (ejustice.just.fgov.be Moniteur belge, cn=2016102705). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3; the Atlas has no sub-national anchor entities, so a subnational instrument anchors to its state."
    confidence: medium
    valid_from: 2016-10-27
    valid_until: null

sources:
  - title: "Ordonnance du 27 octobre 2016 visant à l'établissement d'une politique de données ouvertes"
    url: "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?cn=2016102705&la=F&language=fr&table_name=loi"
    publisher: "Service public fédéral Justice — Moniteur belge"
  - title: "Open Data — Institut bruxellois de statistique et d'analyse"
    url: "https://ibsa.brussels/opendata"
    publisher: "Institut bruxellois de statistique et d'analyse (IBSA)"
---

# Brussels open data ordonnance (2016)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

The ordonnance of **27 October 2016** by which the Brussels-Capital Region
established an open data policy. It is still in force, as amended by
[[BE-BRU-ORDONNANCE-2021]].

## Why a 2016 instrument is worth a node

It exists here to carry one edge honestly. [[BE-BRU-ORDONNANCE-2021]] `amends`
it, and an `amends` edge needs a real target — the type was added precisely
because *"an amending act typically carries both: `amends` the domestic act it
edits, `implements-requirement-from` the directive it transposes"*.

Without this entity the Brussels transposition would look like a standalone
2021 instrument, which would misdate the region's open data policy by five
years.

`coverage: low`: two sources, one relationship, and nothing about its content
beyond the fact that it established the policy.

## Relationships

- `applies-in` [[BE]] — anchor edge.
- The `amends` edge lives on [[BE-BRU-ORDONNANCE-2021]], which is the
  amending act.

## Sources

Listed in frontmatter — the Moniteur belge text and the Brussels statistical
institute's open data page.
