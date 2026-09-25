---
id: NL-IBDS
type: strategy
name: Interbestuurlijke Datastrategie
alternative_names:
  - IBDS
description: >
  Dutch inter-administrative data strategy, developed jointly by ministries,
  executive organisations and representatives of municipalities, provinces
  and water authorities. It aims for government to use the potential of data
  for societal challenges in a legally sound, ethically responsible and
  socially accountable way.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2021-11-18
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-FDS
  - NL-DATA-AGENDA-OVERHEID
relationships:
  - type: implemented-by
    target: NL-FDS
    source: fact
    evidence: "Confirmed 2026-08-21 on noraonline.nl's 'Federatief Datastelsel' wiki page: 'Samen met stakeholders ontwikkelt de IBDS daarom een Federatief Datastelsel (FDS)' — the IBDS is developing the FDS together with stakeholders. The Beleidsevaluatie Interbestuurlijke Datastrategie (Panteia, 7 January 2026) corroborates this, describing FDS building blocks and target architecture as deliverables of the IBDS's implementation programme (Realisatie IBDS) across 2022-2024."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: NL-DATA-AGENDA-OVERHEID
    source: fact
    evidence: "Confirmed by reading privacy-web.nl's own copy of the Kamerbrief directly (2026-09-25): State Secretary Knops (BZK) opens the IBDS's presentation to parliament by saying 'Twee jaar geleden heb ik de NL DIGITAAL: Data Agenda Overheid gelanceerd... De acties in deze data-agenda zijn grotendeels gerealiseerd' (two years ago I launched the Data Agenda Overheid... the actions in this data agenda have largely been realised), and closes by saying 'In navolging van de Data Agenda Overheid zal uw Kamer regelmatig worden geïnformeerd over de voortgang... van deze Interbestuurlijke Datastrategie' (following the Data Agenda Overheid's practice, parliament will be regularly informed about this strategy's progress). This is the government's own narrative link — the same office presenting IBDS as continuing a reporting practice the Data Agenda Overheid established — not a formal successor claim: the Data Agenda Overheid's own `successor` field already points through NL-DIGIBETER's chain to a different entity. `related-to` rather than a stronger type, since no source states IBDS extends or replaces the Data Agenda Overheid's substantive scope, only its parliamentary-reporting rhythm. Closes discovery/unresolved.md row #134."
    confidence: medium
    valid_from: 2021-11-18
    valid_until: null

sources:
  - title: "Interbestuurlijke Datastrategie (IBDS)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/data/interbestuurlijke-datastrategie/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Interbestuurlijke Datastrategie (IBDS)"
    url: "https://www.noraonline.nl/wiki/Interbestuurlijke_Datastrategie_(IBDS)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-22"
  - title: "Realisatie IBDS"
    url: "https://www.digitaleoverheid.nl/community/realisatie-ibds/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-22"
  - title: "Beleidsevaluatie Interbestuurlijke Datastrategie — Eindrapport"
    url: "https://open.overheid.nl/documenten/1edd5ed4-98e8-442e-bcd2-f6ec3f27a754/file"
    publisher: "Rijksoverheid (open.overheid.nl)"
    accessed: "2026-08-22"
  - title: "Federatief Datastelsel"
    url: "https://www.noraonline.nl/wiki/Federatief_Datastelsel"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-22"
  - title: "Kamerbrief over Interbestuurlijke Datastrategie Nederland"
    url: "https://privacy-web.nl/beleid/kamerbrief-over-interbestuurlijke-datastrategie-nederland/"
    publisher: "Privacy Web (reproducing State Secretary Knops's 18 November 2021 letter to the Tweede Kamer)"
    accessed: "2026-09-25"
---

# Interbestuurlijke Datastrategie (IBDS)

> **Verified 2026-08-20, deepened 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.
>
> **Narrowed 2026-09-25**, closing `discovery/unresolved.md` row #134:
> the Kamerbrief presenting the IBDS to parliament, read directly, gives
> the government's own narrative link to [[NL-DATA-AGENDA-OVERHEID]] —
> a continuation of reporting practice, not a stated succession or
> substantive extension.

## Description

The IBDS is the Netherlands' inter-administrative data strategy, covering
government as a whole rather than a single department. It was developed
through collaboration between ministries, executive organisations and
representatives of municipalities, provinces and water authorities, and was
presented to the Tweede Kamer on **18 November 2021** — confirmed on
digitaleoverheid.nl ("Op 18 november 2021 is de Interbestuurlijke
Datastrategie aan de Tweede Kamer aangeboden") and independently on
noraonline.nl's own metadata for the page ("Publicatiedatum: 2021-11-18").
`start_date` is now set to this date.

Its stated aim is for government to realise the potential of data for
societal challenges in a legally sound, ethically responsible and socially
accountable manner. It is described as working from four pillars —
rendered in search results as "what may, what can, what helps, what
inspires" — and as promoting cooperation across administrative tiers.

**Current status confirmed active.** The *Beleidsevaluatie Interbestuurlijke
Datastrategie* (Panteia, published 7 January 2026, "Definitief") covers
2021-2025 and describes 2025 as a phase of "opschaling en borging" (scaling
and consolidation) with recommendations for "een toekomstbestendiger IBDS" —
language describing an ongoing programme, not one that has concluded or been
absorbed. `confidence` raised from `low` to `medium` on this basis.

## Relationships

- Implemented by [[NL-FDS]] — now a sourced fact: "Samen met stakeholders
  ontwikkelt de IBDS daarom een Federatief Datastelsel (FDS)" (noraonline.nl).
- Coordinated within the [[NL-BZK]] digital-government policy remit.
- `related-to` [[NL-DATA-AGENDA-OVERHEID]] — the Kamerbrief presenting the
  IBDS, read directly, says its actions were "grotendeels gerealiseerd"
  (largely realised) and that parliamentary reporting on the IBDS
  continues "in navolging van" (following) that agenda's own practice.
  A narrative continuity in the government's own words, not a formal
  successor claim — see the note above.

## The programme, year by year

Per the 2026 evaluation report: 2021 design and coalition-building; 2022 the
implementation programme "Realisatie IBDS" launches, the advisory function
on responsible data use becomes operational, and the FDS's first outlines
are sketched; 2023 scaling with more projects and FDS building blocks;
2024 the FDS target architecture is completed and first facilities
piloted, and the *Interbestuurlijk Kenniscentrum* (IKC) becomes operational;
2025 the current phase, emphasising adoption and structural embedding.

## Sources

Listed in frontmatter, including the Kamerbrief read directly 2026-09-25.
