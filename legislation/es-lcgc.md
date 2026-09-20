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
  transposition deadline of 17 October 2024, received a reasoned opinion
  from the European Commission on 7 May 2025, and on 8 July 2026 was
  referred, alongside Ireland, France and the Netherlands, to the Court of
  Justice of the EU, with the Commission seeking lump-sum and daily
  financial penalties until full transposition is notified.

level: national
country: ES
region: EU

status: proposed
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - ES-INCIBE
  - ES-CCN
related_entities:
  - EU-NIS2
  - NL-CBW
  - DE-NIS2UMSUCG
  - BE-NIS2-WET
  - FR-NIS2-LOI
  - IE-NCS-BILL
  - EU-CJEU
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading dsn.gob.es's own page directly (2026-08-26): the Anteproyecto incorporates 'la Directiva (UE) 2022/2555 ... conocida como NIS2', and creates the Centro Nacional de Ciberseguridad, attached to the Presidencia del Gobierno, to overcome 'la actual dispersión competencial en materia de ciberseguridad' (the current dispersal of competences in cybersecurity matters). cuatrecasas.com, also read directly, confirms the competence split across the Interior Ministry (Cybersecurity Coordination Office), the Defence Ministry (Centro Criptológico Nacional) and the Digital Transformation Ministry, and the January-2025 approval — though it dates approval one day later than dsn.gob.es (15 January versus 14 January), a minor discrepancy left unresolved. Neither source read gave the specific 24h/72h/one-month notification deadlines or the ten-million-euro penalty figure this entity carries, which rest on nisd2.eu and legiscope.com, not read this pass."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: referred-to-court-over
    target: EU-NIS2
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #91), using the new `referred-to-court-over` type (metadata/relationship-types.md §2.1, added 2026-09-20). Confirmed by reading a Hunton Andrews Kurth law-firm alert directly (2026-09-13): the European Commission referred Spain, alongside Ireland, France and the Netherlands, to the Court of Justice of the EU on 8 July 2026 for failure to notify complete NIS2 transposition, following formal notice on 28 November 2024 and a reasoned opinion on 7 May 2025, with the Commission seeking lump-sum and daily financial penalties until full transposition is notified — the same escalation already recorded on [[IE-NCS-BILL]]."
    confidence: medium
    valid_from: 2026-07-08
    valid_until: null

sources:
  - title: "Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad"
    url: "https://www.dsn.gob.es/en/node/24160"
    publisher: "Departamento de Seguridad Nacional — Gobierno de España"
    accessed: "2026-08-26"
  - title: "European Commission Refers Four Member States to CJEU Over NIS2 Transposition Delays"
    url: "https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-refers-four-member-states-to-cjeu-over-nis2-transposition-delays"
    publisher: "Hunton Andrews Kurth"
    accessed: "2026-09-13"
  - title: "Aprobado el anteproyecto de Ley que transpone la Directiva NIS2"
    url: "https://www.cuatrecasas.com/es/spain/propiedad-intelectual/art/aprobado-anteproyecto-ley-transpone-la-directiva-nis2"
    publisher: "Cuatrecasas"
    accessed: "2026-08-26"
  - title: "Estado de NIS 2 en España: proyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad, CCN, INCIBE"
    url: "https://nisd2.eu/es/wiki/timelines-and-status/nis2-status-spain"
    publisher: "nisd2.eu"
  - title: "NIS2 España 2026: transposición, entidades esenciales, plazos y sanciones"
    url: "https://www.legiscope.com/blog/nis2-espana-transposicion.html"
    publisher: "Legiscope"
---

# LCGC — Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad

> **Escalation added 2026-09-13**, closing part of `discovery/unresolved.md`
> row #91. A law-firm alert, read directly, confirms the Commission
> referred Spain to the CJEU on 8 July 2026 — see below.
>
> **Closed 2026-09-20**: the referral is now a typed `referred-to-court-over`
> edge, a new relationship type.
>
> **Verified 2026-08-26.** Two of four cited pages were read directly:
> dsn.gob.es's own page on the bill and Cuatrecasas's law-firm analysis.
> Both confirm the Centro Nacional de Ciberseguridad and the three-ministry
> competence split; the specific notification deadlines and penalty figure
> rest on the two sources not read this pass.

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
European Commission sent a **reasoned opinion on 7 May 2025** — the stage
after a letter of formal notice, itself sent 28 November 2024.

## Referred to the CJEU, closed 2026-09-13

Confirmed by reading a Hunton Andrews Kurth law-firm alert directly: on
**8 July 2026** the Commission referred Spain — alongside **Ireland,
France and the Netherlands** — to the **Court of Justice of the EU**
over failure to notify complete NIS2 transposition, seeking lump-sum and
daily financial penalties until full transposition is notified. This is
the same escalation, from the same referral batch, already recorded on
[[IE-NCS-BILL]] (which independently sourced an initial €2.8 million
penalty exposure for Ireland specifically; no Spain-specific figure was
found this pass).

Confirmed by reading dsn.gob.es and cuatrecasas.com directly (2026-08-26):
the Centro Nacional de Ciberseguridad would be attached to the
**Presidencia del Gobierno**, not free-floating, and exists specifically
to overcome "the current dispersal of competences in cybersecurity
matters" — a more precise institutional detail than the previous
search-only evidence carried. The two sources give the approval date one
day apart (dsn.gob.es: 14 January 2025; cuatrecasas.com: 15 January 2025);
this entity keeps the government's own date and records the discrepancy
here rather than silently picking one.

## Five countries, five different NIS2 states

This is the most useful thing Spain contributes to the Atlas's EU→national
picture, and it only becomes visible at five countries:

| Country | Instrument | Status in the Atlas |
|---|---|---|
| Netherlands | [[NL-CBW]] | `active` — in force |
| Germany | [[DE-NIS2UMSUCG]] | `active` — amending act, in force |
| Belgium | [[BE-NIS2-WET]] | `active` — in force |
| France | [[FR-NIS2-LOI]] | `planned` — bill in active process, not in force |
| **Spain** | **LCGC** | **`proposed`** — sources agree it is not in force |

Five member states, one directive, one deadline — and five different
paths to it. **Stale as of 2026-09-13, now fixed**: this table previously
called France's status `unknown`, on the grounds that its sources
conflicted about whether the instrument existed in force — but that
contradiction was itself resolved on [[FR-NIS2-LOI]]'s own file back on
2026-08-26, moving its status to `planned`. This table simply was never
updated to match.

The France/Spain pair is still informative, on different grounds now: both
are unimplemented drafts, and both have escalated the same way. On **8 July
2026** the European Commission referred both — alongside Ireland and the
Netherlands — to the **Court of Justice of the EU** over failure to notify
complete NIS2 transposition, seeking lump-sum and daily financial penalties.
See "Referred to the CJEU" above and [[FR-NIS2-LOI]]'s own file for the
same escalation.

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
- `referred-to-court-over` [[EU-NIS2]] — `confidence: medium`, new
  2026-09-20, pulled out of the `implements-requirement-from` edge's
  evidence string into its own typed edge.

## Sources

Listed in frontmatter, two of four read directly this pass: the National
Security Department's own page on the bill and Cuatrecasas's law-firm
analysis. The NIS2 status tracker and compliance commentary were not
re-fetched. **No BOE citation exists to give**, which is itself the
substantive fact about this entity.
