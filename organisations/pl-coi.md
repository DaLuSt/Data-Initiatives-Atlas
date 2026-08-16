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
verification: search-only

start_date: 2010-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PL-MC
related_entities:
  - PL-MC
  - PL-MOBYWATEL
relationships:
  - type: governed-by
    target: PL-MC
    source: fact
    evidence: "The Ministry of Digital Affairs is the supervisory body that designates the development directions for COI, and supervises COI in the scope of the tasks entrusted to this unit (gov.pl/web/cyfryzacja/centralny-osrodek-informatyki; coi.gov.pl/o-nas). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "O nas | COI"
    url: "https://coi.gov.pl/o-nas"
    publisher: "Centralny Ośrodek Informatyki (COI)"
  - title: "Centralny Ośrodek Informatyki — Ministerstwo Cyfryzacji"
    url: "https://www.gov.pl/web/cyfryzacja/centralny-osrodek-informatyki"
    publisher: "Ministerstwo Cyfryzacji"
  - title: "Centralny Ośrodek Informatyki przekształci się w Agencję Informatyzacji"
    url: "https://www.gov.pl/web/cyfryzacja/centralny-osrodek-informatyki-przeksztalci-sie-w-agencje-informatyzacji-co-usprawni-realizacje-zadan-w-obszarze-informatyzacji-panstwa"
    publisher: "Ministerstwo Cyfryzacji"
  - title: "Centralny Ośrodek Informatyki przekształci się w Agencję Informatyzacji (komunikat)"
    url: "https://pap-mediaroom.pl/polityka-i-spoleczenstwo/cyfryzacja-kprm-centralny-osrodek-informatyki-przeksztalci-sie-w-agencje"
    publisher: "PAP MediaRoom"
---

# COI — Centralny Ośrodek Informatyki

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

COI was established in **2010** as an institution of the public finance
sector, and employs around **1,800 IT and programming specialists**. Its
primary task is the protection, development and maintenance of the state's
most important IT systems:

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

## PESEL is not modelled

COI maintains the **PESEL** register — Poland's population register, the
direct counterpart of [[NL-BRP]] and the object the Dutch batch modelled in
detail.

**No entity was created for it.** It is named in a list of systems COI
maintains and nothing was researched about its legal basis, content or
governance. Creating it from that mention would produce exactly the thin
node the taxonomy threshold prevents — and would invite a false parallel
with the ten fully-described Dutch registers. Queued.

## Relationships

- `governed-by` [[PL-MC]].

**No `maintained-by` edge from [[PL-MOBYWATEL]] to this entity.** COI is
sourced as maintaining the application's *systems*; the mObywatel Act
regulates the application itself, and which body is its legal operator was
not established. See [[PL-MOBYWATEL]].

## Sources

Listed in frontmatter — COI's own about page, two ministry pages including
the transformation announcement, and the press-agency communiqué.
