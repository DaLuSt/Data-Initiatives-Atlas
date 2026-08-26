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
confidence: high
coverage: high
verification: primary-source

start_date: 2022-11-24
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading both WALLEX texts directly (2026-08-26), resolving which of the two ELI records is which. 2022207332 is 'Décret relatif à la diffusion et à la réutilisation des informations du secteur public (« Open Data »)', whose Article 1 states: 'Le présent décret transpose la directive (UE) 2019/1024 du Parlement européen et du Conseil du 20 juin 2019 ... concernant les données ouvertes et la réutilisation des informations du secteur public.' 2022206865 is a *different* instrument (see the `amends`-adjacent note below), confirming the entity's earlier caution that the mapping between the two ELI references was unconfirmed."
    confidence: high
    valid_from: 2022-11-24
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "Confirmed by reading the WALLEX text directly (2026-08-26): the décret is an act of the Walloon Parliament and applies within the Walloon Region, a constituent unit of Belgium. Anchor edge under metadata/relationship-types.md §2.3; the Atlas has no sub-national anchor entities, so a subnational instrument anchors to its state."
    confidence: medium
    valid_from: 2022-11-24
    valid_until: null

sources:
  - title: "Décret du 24 novembre 2022 — WALLEX (2022207332) — transposing décret"
    url: "https://wallex.wallonie.be/eli/loi-decret/2022/11/24/2022207332"
    publisher: "Service public de Wallonie — WALLEX"
    accessed: "2026-08-26"
  - title: "Décret du 24 novembre 2022 — WALLEX (2022206865) — assent décret"
    url: "https://wallex.wallonie.be/eli/loi-decret/2022/11/24/2022206865"
    publisher: "Service public de Wallonie — WALLEX"
    accessed: "2026-08-26"
  - title: "Directive (EU) 2019/1024 — national implementing measures"
    url: "https://eur-lex.europa.eu/legal-content/nl/NIM/?uri=oj:JOL_2019_172_R_0003"
    publisher: "EUR-Lex — Publications Office of the European Union"
    accessed: "2026-08-26"
---

# Walloon open data décret (24 November 2022)

> **Verified 2026-08-26.** All three cited sources were read directly, and
> the mapping between the two WALLEX ELI references — flagged as unconfirmed
> since this entity was first written — is now resolved. `verification:
> primary-source`.

## Description

A décret of the **Walloon Parliament** of **24 November 2022** on the
dissemination and re-use of public sector information, transposing
[[EU-OPEN-DATA-DIRECTIVE]] for the Walloon Region. Confirmed directly from
its own Article 1: *"Le présent décret transpose la directive (UE)
2019/1024."*

## Two décrets, one date, and a cooperation agreement — now confirmed which is which

[[BE-HERGEBRUIK-WET-2023]] recorded *"two décrets on the dissemination and
re-use of public sector information, 24 November 2022"* without saying what
the second one was, and this entity previously carried a stated limit: two
WALLEX ELI references were cited without establishing which was which.
Both texts were read directly this pass:

| ELI reference | What it does |
|---|---|
| **2022207332** (this entity) | Transposes the directive for the Walloon Region — confirmed by its own Article 1 |
| **2022206865** | *"Décret portant assentiment ... à l'accord de coopération du 24 mars 2022 entre la Région wallonne et la Communauté française relatif à l'abrogation des décrets conjoints du 12 juillet 2017 et du 19 juillet 2017"* — gives **assent to a cooperation agreement of 24 March 2022** between the Walloon Region and the French Community, repealing the **joint décrets of 12 July 2017 and 19 July 2017** on the re-use of public sector information |

**Only the transposing décret is modelled.** The second is an assent act
clearing away a prior joint regime, and a joint décret is an instrument
adopted identically by two legislatures — Region and Community — which the
Atlas has no way to represent: a single entity would have two `level:
subnational` parents and `country: BE` would be the only honest scoping.
Recorded here in prose, now on confirmed rather than inferred grounds.

## Wallonia was sixteen months late, and still ahead of the federal state

| Level | Instrument | Date | Against the 17 July 2021 deadline |
|---|---|---|---|
| Flanders | [[BE-VL-BESTUURSDECREET-2021]] | 2 July 2021 | **on time** |
| Brussels-Capital | [[BE-BRU-ORDONNANCE-2021]] | 10 Dec 2021 | 5 months late |
| **Wallonia** | **this décret** | **24 Nov 2022** | **16 months late** |
| Federal | [[BE-HERGEBRUIK-WET-2023]] | 25 Dec 2023 (dated) / 23 Jan 2024 (published) | ~29-30 months late |

Belgium was referred to the Court of Justice in **February 2023** — by which
date all three sub-federal instruments were in force and only the federal one
was missing.

## Relationships

- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]].
- `applies-in` [[BE]] — see [[BE-VL-BESTUURSDECREET-2021]].

## Sources

All three read directly this pass — both WALLEX ELI records for décrets of
24 November 2022, and the EUR-Lex register of national implementing
measures. `coverage` is raised to `high`: the previously unconfirmed
mapping between the two WALLEX references is now settled from the texts
themselves.
