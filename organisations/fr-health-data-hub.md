---
id: FR-HEALTH-DATA-HUB
type: organisation
name: Plateforme des données de santé
alternative_names:
  - Health Data Hub
  - HDH
  - PDS
description: >
  French groupement d'intérêt public established by the law of 24 July 2019
  on the organisation and transformation of the health system. An order of
  29 November 2019 approved an amendment to the constitutive convention of
  the GIP Institut national des données de santé, creating the GIP
  Plateforme des données de santé with effect from 1 December 2019. It
  associates 56 members, principally public bodies, and gives authorised
  project holders access to non-nominative health data through a secure
  technological platform. It implements the strategic orientations for the
  Système national des données de santé set by the State and in particular
  the health ministry.

level: national
country: FR
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-12-01
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - FR
  - FR-SNDS
  - EU-EHDS
relationships:
  - type: part-of
    target: FR
    source: fact
    evidence: "The Health Data Hub was established by the law of 24 July 2019 relating to the organisation and transformation of the health system; legally it takes the form of a groupement d'intérêt public associating 56 stakeholders, principally public entities; an arrêté of 29 November 2019 approved an amendment to the constitutive convention of the GIP Institut national des données de santé, creating the GIP Plateforme des données de santé with effect from 1 December 2019 (sante.gouv.fr press release 191202; drees.solidarites-sante.gouv.fr 'Plateforme des données de santé'; data.gouv.fr organisation page). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-12-01
    valid_until: null
  - type: governed-by
    target: FR-SNDS
    source: interpretation
    evidence: "The sources state that the Plateforme implements the major strategic orientations relating to the Système national des données de santé established by the State and in particular the Ministry of Solidarity and Health. Reading that as `governed-by` is the Atlas's interpretation: the sources describe the Plateforme as executing the SNDS's strategic orientations, which is weaker than a statement that the SNDS governs it."
    confidence: low
    valid_from: 2019-12-01
    valid_until: null

sources:
  - title: "Le Health Data Hub est officiellement créé — communiqué de presse, 2 décembre 2019"
    url: "https://sante.gouv.fr/IMG/pdf/191202_-_cp_-_health_data_hub.pdf"
    publisher: "Ministère des Solidarités et de la Santé"
  - title: "Plateforme des données de santé"
    url: "https://drees.solidarites-sante.gouv.fr/sources-outils-et-enquetes/plateforme-des-donnees-de-sante"
    publisher: "DREES — Direction de la recherche, des études, de l'évaluation et des statistiques"
  - title: "Plateforme des Données de Santé (Health Data Hub) — organisation"
    url: "https://www.data.gouv.fr/organizations/plateforme-des-donnees-de-sante-health-data-hub/datasets"
    publisher: "data.gouv.fr — Etalab"
---

# Health Data Hub (Plateforme des données de santé)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

A **groupement d'intérêt public** created by the law of **24 July 2019** on
the organisation and transformation of the health system, and constituted with
effect from **1 December 2019** by an arrêté of 29 November 2019 that amended
the constitutive convention of the **GIP Institut national des données de
santé** — so the Health Data Hub is a transformation of an existing body, not
a new one from nothing.

It associates **56 members**, principally public bodies, and gives authorised
project holders access to **non-nominative** health data through a secure
platform where data can be cross-referenced and analysed.

## The three shapes of a national health data regime

With Germany, France and Finland modelled together, three different answers to
the same problem are visible:

| | Instrument | Body | Shape |
|---|---|---|---|
| Germany | [[DE-GDNG]] | [[DE-GEMATIK]] (infrastructure) | statute creates a research data centre; a separate company runs the exchange infrastructure |
| **France** | law of 24 July 2019 | **this GIP** | a public-interest grouping of 56 members holds the platform |
| Finland | [[FI-SECONDARY-USE-ACT]] | [[FI-FINDATA]] | statute creates a **permit authority** that licenses access |

France pools the actors; Finland licenses the access; Germany separates the
statute from the plumbing. [[EU-EHDS]] is the attempt to make these
interoperable, and it is more legible with three national cases under it than
with one.

## Relationships

- `part-of` [[FR]] — anchor edge. A GIP is a public-interest grouping
  established by statute, so `part-of` rather than the `related-to` the
  Atlas uses for member-owned bodies outside the state.
- `governed-by` [[FR-SNDS]], marked **`source: interpretation`** and
  `confidence: low`. The sources say the Plateforme *implements the strategic
  orientations* of the SNDS, which is weaker than governance. The edge is the
  closest available reading and is flagged as a reading rather than a fact.

## What is not modelled

The **law of 24 July 2019** itself — the loi OTSS — has no entity. It is
named in every source here and none of them gives it a JORF or Legifrance
identifier, which is what the Atlas's French legislation entities are keyed
on.

## Sources

Listed in frontmatter — the health ministry's press release announcing the
creation, the DREES page, and the Etalab organisation record.
