---
id: ES-LCGC
type: law
name: Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad
alternative_names:
  - Ley de Coordinación y Gobernanza de la Ciberseguridad
  - LCGC
  - Spanish Cybersecurity Coordination and Governance Bill
description: >
  Spanish draft law transposing the NIS2 Directive, approved by the Council
  of Ministers on 14 January 2025 and still in parliamentary process. It
  would create a Centro Nacional de Ciberseguridad and distribute
  competences between the Ministry of the Interior, the Ministry of Defence
  through the Centro Criptológico Nacional, and the Ministry for Digital
  Transformation. It would oblige essential and important entities in
  critical sectors to implement risk management measures, notify incidents
  in staged deadlines — early warning within 24 hours, notification within
  72 hours and a final report within one month — and answer at management
  level, with penalties of up to ten million euros. Spain missed the
  transposition deadline of 17 October 2024 and received a reasoned opinion
  from the European Commission in May 2025.

level: national
country: ES
region: EU

status: proposed
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
organisations:
  - ES-INCIBE
  - ES-CCN
related_entities:
  - EU-NIS2
  - NL-CBW
  - DE-NIS2UMSUCG
  - BE-NIS2-WET
  - FR-NIS2-LOI
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Directive NIS2 (EU) 2022/2555 is transposed in Spain by the Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, approved by the Council of Ministers on 14 January 2025 and still in process as of 2026 without publication in the BOE; Spain did not meet the transposition deadline of 17 October 2024 and the European Commission sent a reasoned opinion in May 2025 (dsn.gob.es 'Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad'; cuatrecasas.com 'Aprobado el anteproyecto de Ley que transpone la Directiva NIS2'; nisd2.eu status page for Spain). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad"
    url: "https://www.dsn.gob.es/en/node/24160"
    publisher: "Departamento de Seguridad Nacional — Gobierno de España"
  - title: "Aprobado el anteproyecto de Ley que transpone la Directiva NIS2"
    url: "https://www.cuatrecasas.com/es/spain/propiedad-intelectual/art/aprobado-anteproyecto-ley-transpone-la-directiva-nis2"
    publisher: "Cuatrecasas"
  - title: "Estado de NIS 2 en España: proyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, CCN, INCIBE"
    url: "https://nisd2.eu/es/wiki/timelines-and-status/nis2-status-spain"
    publisher: "nisd2.eu"
  - title: "NIS2 España 2026: transposición, entidades esenciales, plazos y sanciones"
    url: "https://www.legiscope.com/blog/nis2-espana-transposicion.html"
    publisher: "Legiscope"
---

# LCGC — Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The LCGC is Spain's transposition of [[EU-NIS2]]. It was **approved by the
Council of Ministers on 14 January 2025** and, as of 2026, is still in
process and **not published in the BOE**.

What it would do:

- create a **Centro Nacional de Ciberseguridad**;
- distribute competences between the **Ministry of the Interior**, the
  **Ministry of Defence** through [[ES-CCN]], and the **Ministry for Digital
  Transformation**;
- oblige essential and important entities in critical sectors to implement
  risk management measures and answer **at management level**;
- set staged incident notification — **24 hours** early warning, **72
  hours** notification, **one month** final report;
- provide penalties of **up to ten million euros**.

Spain missed the transposition deadline of **17 October 2024**, and the
European Commission sent a **reasoned opinion in May 2025** — the stage
after a letter of formal notice.

## Five countries, five different NIS2 states

This is the most useful thing Spain contributes to the Atlas's EU→national
picture, and it only becomes visible at five countries:

| Country | Instrument | Status in the Atlas |
|---|---|---|
| Netherlands | [[NL-CBW]] | `active` — in force |
| Germany | [[DE-NIS2UMSUCG]] | `active` — amending act, in force |
| Belgium | [[BE-NIS2-WET]] | `active` — in force |
| France | [[FR-NIS2-LOI]] | **`unknown`** — sources contradict each other |
| **Spain** | **LCGC** | **`proposed`** — sources agree it is not in force |

Five member states, one directive, one deadline — and five different
answers, two of which are not "yes" or "no".

The France/Spain pair is the informative one. Both are unimplemented; only
one is *uncertain*. [[FR-NIS2-LOI]] carries `status: unknown` because its
sources conflict about whether the instrument exists in force. This entity
carries `status: proposed` because its sources **agree**: approved as a
draft, still in process, not in the BOE.

That distinction — *we do not know* versus *we know it has not happened* —
is expressible in the Atlas's status vocabulary, and this batch is the first
time both values appear side by side on instruments transposing the same
directive. The vocabulary earns its keep here.

## What is deliberately not recorded

- **No relationship to [[ES-INCIBE]] or [[ES-CCN]]**, though both are named
  in the reporting and one is reported publicly defending its competences
  against the proposed new centre. A contested draft allocation of
  competences is not a relationship; it becomes one if and when the law
  passes.
- **The Centro Nacional de Ciberseguridad is not an entity.** It does not
  exist. Creating a node for a body a draft law proposes would be exactly
  the invention the Atlas refuses — the error would be invisible in the
  graph, which would show a plausible Spanish cybersecurity centre with no
  indication that nothing of the kind has been constituted.
- **No `start_date`.** There is no date on which anything came into force.

## Relationships

- `implements-requirement-from` [[EU-NIS2]] — the obligation the draft
  addresses, recorded with no `valid_from` because it has not taken effect.

## Sources

Listed in frontmatter — the National Security Department's own page on the
bill, a law-firm analysis, a NIS2 status tracker and a compliance
commentary. **No BOE citation exists to give**, which is itself the
substantive fact about this entity.
