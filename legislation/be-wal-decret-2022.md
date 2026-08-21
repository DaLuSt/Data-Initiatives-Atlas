---
id: BE-WAL-DECRET-2022
type: law
name: Décret du 24 novembre 2022 relatif à la diffusion et à la réutilisation des informations du secteur public
alternative_names:
  - Walloon open data décret
  - Décret Open Data (Wallonie)
description: >
  Décret of the Walloon Parliament of 24 November 2022 on the dissemination
  and re-use of public sector information, transposing Directive (EU)
  2019/1024 on open data and the re-use of public sector information for the
  Walloon Region. It was adopted alongside a second décret of the same date
  giving assent to a cooperation agreement of 24 March 2022 between the
  Walloon Region and the French Community, which repealed the joint décrets of
  12 July 2017 and 19 July 2017 on the re-use of public sector information.

level: subnational
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2022-11-24
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
  - BE-BRU-ORDONNANCE-2021
relationships:
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "A décret of 24 November 2022 concerns the dissemination and re-use of public sector information ('Open Data') and refers to Directive (EU) 2019/1024 of the European Parliament and of the Council of 20 June 2019 on open data and the re-use of public sector information (recast) (wallex.wallonie.be ELI loi-decret/2022/11/24/2022207332 and /2022206865; eur-lex.europa.eu national implementing measures for 32019L1024). NOT READ — search-only."
    confidence: medium
    valid_from: 2022-11-24
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "The décret is an act of the Walloon Parliament and applies within the Walloon Region, a constituent unit of Belgium (wallex.wallonie.be ELI loi-decret/2022/11/24). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3; the Atlas has no sub-national anchor entities, so a subnational instrument anchors to its state."
    confidence: medium
    valid_from: 2022-11-24
    valid_until: null

sources:
  - title: "Décret du 24 novembre 2022 — WALLEX (2022207332)"
    url: "https://wallex.wallonie.be/eli/loi-decret/2022/11/24/2022207332"
    publisher: "Service public de Wallonie — WALLEX"
  - title: "Décret du 24 novembre 2022 — WALLEX (2022206865)"
    url: "https://wallex.wallonie.be/eli/loi-decret/2022/11/24/2022206865"
    publisher: "Service public de Wallonie — WALLEX"
  - title: "Directive (EU) 2019/1024 — national implementing measures"
    url: "https://eur-lex.europa.eu/legal-content/nl/NIM/?uri=oj:JOL_2019_172_R_0003"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# Walloon open data décret (24 November 2022)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

A décret of the **Walloon Parliament** of **24 November 2022** on the
dissemination and re-use of public sector information, transposing
[[EU-OPEN-DATA-DIRECTIVE]] for the Walloon Region.

## Two décrets, one date, and a cooperation agreement

[[BE-HERGEBRUIK-WET-2023]] recorded *"two décrets on the dissemination and
re-use of public sector information, 24 November 2022"* without saying what
the second one was. It was an instrument of a different kind:

| Décret | What it does |
|---|---|
| This one | Transposes the directive for the Walloon Region |
| The second | Gives **assent to a cooperation agreement of 24 March 2022** between the Walloon Region and the French Community, repealing the **joint décrets of 12 July 2017 and 19 July 2017** on the re-use of public sector information |

**Only the transposing décret is modelled.** The second is an assent act
clearing away a prior joint regime, and a joint décret is an instrument
adopted identically by two legislatures — Region and Community — which the
Atlas has no way to represent: a single entity would have two `level:
subnational` parents and `country: BE` would be the only honest scoping.
Recorded here in prose.

## Wallonia was sixteen months late, and still ahead of the federal state

| Level | Instrument | Date | Against the 17 July 2021 deadline |
|---|---|---|---|
| Flanders | [[BE-VL-BESTUURSDECREET-2021]] | 2 July 2021 | **on time** |
| Brussels-Capital | [[BE-BRU-ORDONNANCE-2021]] | 10 Dec 2021 | 5 months late |
| **Wallonia** | **this décret** | **24 Nov 2022** | **16 months late** |
| Federal | [[BE-HERGEBRUIK-WET-2023]] | 25 Dec 2023 | 29 months late |

Belgium was referred to the Court of Justice in **February 2023** — by which
date all three sub-federal instruments were in force and only the federal one
was missing.

## Relationships

- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]].
- `applies-in` [[BE]] — see [[BE-VL-BESTUURSDECREET-2021]].

## Sources

Listed in frontmatter — two WALLEX ELI records for décrets of 24 November
2022, and the EUR-Lex register of national implementing measures.

**A limit worth naming.** The searches returned three WALLEX ELI references
for that date and did not establish which is the transposing décret and which
the assent act. Two are cited; the pages are on a blocked host and were not
opened, so the mapping is unconfirmed and the entity is `coverage: medium`
rather than high.
