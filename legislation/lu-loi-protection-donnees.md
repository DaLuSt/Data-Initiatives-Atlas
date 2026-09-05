---
id: LU-LOI-PROTECTION-DONNEES
type: law
name: "Loi du 1er août 2018 portant organisation de la Commission nationale pour la protection des données et du régime général sur la protection des données"
alternative_names:
  - "Loi 'Protection des données'"
  - Luxembourg GDPR Implementation Act
description: >
  Luxembourg act of 1 August 2018 organising the Commission nationale pour
  la protection des données (CNPD) and implementing the general data
  protection framework set by the GDPR at national level. Published as
  Mémorial A No. 686.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2018-08-01
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - LU-CNPD
related_entities:
  - EU-GDPR
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading cnpd.public.lu's own 'Droit luxembourgeois' legislation page directly (2026-09-05), which lists two distinct laws both dated 1 August 2018: this one, cited there as 'Loi du 1er août 2018 portant organisation de la Commission nationale pour la protection des données et du régime général sur la protection des données' (Mémorial A reference a686), and a second, separate law on data protection in criminal and national-security matters (a689, implementing the Law Enforcement Directive 2016/680 — not this entity). A WebSearch cross-check independently returned the same a686 title in fuller form, naming it as implementing Regulation (EU) 2016/679 (the GDPR) and repealing the prior law of 2 August 2002. legilux.public.lu itself, which would carry the act's full text, is a JavaScript single-page application returning no static content, confirmed unreadable on a prior pass (LU-CNPD, 2026-08-25) and not re-attempted."
    confidence: medium
    valid_from: 2018-08-01
    valid_until: null
  - type: applies-to
    target: LU-CNPD
    source: fact
    evidence: "The act's own title, confirmed by reading cnpd.public.lu's 'Droit luxembourgeois' page directly (2026-09-05), states it is 'portant organisation de la Commission nationale pour la protection des données' (organising the National Commission for Data Protection) — the same title-level evidence tier used for NL-WET-CBS's applies-to NL-CBS edge."
    confidence: medium
    valid_from: 2018-08-01
    valid_until: null

sources:
  - title: "Droit luxembourgeois — CNPD"
    url: "https://cnpd.public.lu/fr/legislation/droit-lux.html"
    publisher: "Commission nationale pour la protection des données (CNPD)"
    accessed: "2026-09-05"
  - title: "Loi du 1er août 2018 portant organisation de la Commission nationale pour la protection des données et du régime général sur la protection des données"
    url: "https://legilux.public.lu/eli/etat/leg/loi/2018/08/01/a686/jo"
    publisher: "Journal Officiel du Grand-Duché de Luxembourg (Legilux)"
    note: "Confirmed unreadable: legilux.public.lu is a JavaScript single-page application with no static content available to this environment's fetch tooling."
---

# Loi du 1er août 2018 (Luxembourg GDPR implementation)

> **Created 2026-09-05**, closing the gap `discovery/unresolved.md` and
> [[LU-CNPD]] itself had flagged: every other member state in the Atlas
> already carried a modelled national GDPR implementing act, and
> Luxembourg's was the one exception, sourced only to a date with no
> entity behind it.

## Description

Luxembourg's national implementation of the GDPR, dated **1 August
2018** and published as **Mémorial A No. 686**. Confirmed by reading
cnpd.public.lu's own "Droit luxembourgeois" legislation page directly:
the page lists this act by its full official title and distinguishes it
from a second, separate law of the same date (Mémorial A No. 689) that
implements the Law Enforcement Directive (2016/680) in criminal and
national-security matters — a different instrument, not modelled here or
anywhere else in the Atlas yet.

[[LU-CNPD]] previously sourced only the **date** (1 August 2018) via an
ELI URL fragment on its own "Législation" page, without a confirmed
official title — `legilux.public.lu` itself, which would carry the act's
full text, is a JavaScript single-page application returning no static
content to this environment's fetch tooling, on both this pass and the
2026-08-25 pass that first found the date. The official title above comes
from CNPD's own page, not from Legilux directly, and a WebSearch
cross-check independently returned the same title.

## The seventh national GDPR instrument

| Instrument | Country | Type |
|---|---|---|
| [[NL-UAVG]] | NL | `implements-requirement-from` |
| [[DE-BDSG]] | DE | `implements-requirement-from` |
| [[ES-LOPDGDD]] | ES | `implements-requirement-from` |
| [[PL-ODO]] | PL | `implements-requirement-from` |
| [[IE-DPA-2018]] | IE | `implements-requirement-from` |
| **LU-LOI-PROTECTION-DONNEES** | **LU** | `implements-requirement-from` |
| [[NO-PERSONOPPLYSNINGSLOVEN]] | NO | `implements-requirement-from` — via the EEA |
| [[GB-UK-GDPR]] | GB | `derived-from` |
| [[CH-REVDSG]] | CH | `aligned-with` |

## Not modelled

- The **Mémorial A No. 689** law of the same date, implementing the Law
  Enforcement Directive — a separate instrument CNPD's own page names but
  this pass did not otherwise research.
- The act's **section-level content**: what it says about the CNPD's
  powers, procedures, or Luxembourg-specific derogations. Neither
  Legilux page was readable.
- The **2002 predecessor act** the 2018 law repeals, per the WebSearch
  cross-check — not independently confirmed by a primary source read
  this pass, and not modelled.

## Relationships

- `implements-requirement-from` [[EU-GDPR]].
- `applies-to` [[LU-CNPD]], which it organises.

## Sources

Two sources, one read directly (CNPD's own legislation page). Legilux's
own text remains confirmed unreadable (JavaScript SPA, no static
content).
