---
id: PL-COI
type: organisation
name: Centralny Ośrodek Informatyki
alternative_names:
  - COI
  - Central IT Centre
description: >
  Polish public-finance-sector institution established in 2010 to deliver
  services and tools contributing to the country's digital transformation,
  employing around 1,800 IT and programming specialists. Its primary task is
  the protection, development and maintenance of the state's most important
  IT systems, including the Profil Zaufany trusted profile, the mObywatel
  application, the PESEL register, the passport document register, the
  e-services platform and ePUAP. It is supervised by the Ministry of Digital
  Affairs, which designates its development directions. A draft law would
  convert it into an Agencja Informatyzacji.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PL-MC
related_entities:
  - PL-MC
  - PL-MOBYWATEL
  - PL-PESEL
relationships:
  - type: governed-by
    target: PL-MC
    source: fact
    evidence: "Confirmed by reading gov.pl's own COI page directly (2026-08-26): 'Organ nadrzędny: Ministerstwo Cyfryzacji — jednostka nadzorowana' (superior body: Ministry of Digital Affairs — supervised unit). coi.gov.pl's own 'O nas' page, also read directly, confirms COI 'realizuje zadania wyznaczane przez Ministerstwo Cyfryzacji' (carries out tasks designated by the Ministry of Digital Affairs), though it names the Minister of Internal Affairs and Administration (MSWiA), not the Ministry of Digital Affairs, as the body that established COI in 2010 — a founding detail this entity did not previously carry, and a different ministry from its current supervisor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "O nas | COI"
    url: "https://coi.gov.pl/o-nas"
    publisher: "Centralny Ośrodek Informatyki (COI)"
    accessed: "2026-08-26"
  - title: "Centralny Ośrodek Informatyki — Ministerstwo Cyfryzacji"
    url: "https://www.gov.pl/web/cyfryzacja/centralny-osrodek-informatyki"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Centralny Ośrodek Informatyki przekształci się w Agencję Informatyzacji"
    url: "https://www.gov.pl/web/cyfryzacja/centralny-osrodek-informatyki-przeksztalci-sie-w-agencje-informatyzacji-co-usprawni-realizacje-zadan-w-obszarze-informatyzacji-panstwa"
    publisher: "Ministerstwo Cyfryzacji"
    accessed: "2026-08-26"
  - title: "Centralny Ośrodek Informatyki przekształci się w Agencję Informatyzacji (komunikat)"
    url: "https://pap-mediaroom.pl/polityka-i-spoleczenstwo/cyfryzacja-kprm-centralny-osrodek-informatyki-przeksztalci-sie-w-agencje"
    publisher: "PAP MediaRoom"
---

# COI — Centralny Ośrodek Informatyki

> **Verified 2026-08-26, with one date fixed.** Three of four cited pages
> were read directly. `start_date` was previously padded to `2010-01-01`;
> COI's own page gives only the bare year, "powołano w 2010 roku", so it
> is now `null` with the year kept in prose.

## Description

COI was established in **2010** — confirmed by reading coi.gov.pl's own
"O nas" page directly, though only as a bare year, by the **Minister of
Internal Affairs and Administration (MSWiA)**, not by the Ministry of
Digital Affairs that supervises it today — as an institution of the
public finance sector, and employs around **1,800 IT and programming
specialists**. Its primary task is the protection, development and
maintenance of the state's most important IT systems:

- **Profil Zaufany** — the trusted profile;
- **[[PL-MOBYWATEL]]** — the citizen application;
- the **PESEL** register;
- the **passport document** register;
- the e-services platform and **ePUAP**.

## A pending organisational transformation, caught earlier than Spain's

A draft law would convert COI into an **Agencja Informatyzacji**, described
as improving the unit's operations and allowing faster performance of its
tasks. Consultations have begun.

This is the same shape as Spain's [[ES-SGAD]] → [[ES-AEAD]], which the Atlas
recorded as its **first organisational succession** — a body converted into
an agency with greater autonomy. The difference is timing:

| | Spain | Poland |
|---|---|---|
| Change | directorate → **state agency** | centre → **agency** |
| Instrument | RD 1118/2024 | **draft law, in consultation** |
| Status | **completed** 21 Feb 2025 | **not enacted** |
| Modelled | `supersedes` edge, two entities | **no successor entity** |

**No `successor` and no Agencja Informatyzacji entity was created.** The
agency does not exist. This is the same refusal made for the Centro Nacional
de Ciberseguridad that [[ES-LCGC]] would create: a node for a body a draft
law proposes would be indistinguishable in the graph from one that exists.

That the Atlas now holds the *same* institutional change at two different
stages, in two countries, is a genuine benefit of covering six of them.

## PESEL is now modelled

COI maintains the **PESEL** register — Poland's population register, the
direct counterpart of [[NL-BRP]]. It is now [[PL-PESEL]], `maintained-by`
this entity via the State Registers System launched 1 March 2015, and
`governed-by` [[PL-EWIDENCJA-LUDNOSCI]], the 2010 act that is its legal
basis.

## Relationships

- `governed-by` [[PL-MC]].

**Still no `maintained-by` edge from [[PL-MOBYWATEL]] to this entity.**
COI remains sourced as maintaining the application's *systems* only. The
mObywatel Act's own text, read this pass, names [[PL-MC]] — not COI — as
the application's legal operator; that edge is recorded there instead.
See [[PL-MOBYWATEL]].

## Sources

Listed in frontmatter, three of four read directly this pass.
