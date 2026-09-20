---
id: DE-IT-NRW
type: organisation
name: Landesbetrieb Information und Technik Nordrhein-Westfalen
alternative_names:
  - IT.NRW
  - IT NRW
description: >
  North Rhine-Westphalia's own IT service provider and statistical
  office, a Landesbetrieb (state enterprise — a legally dependent,
  organisationally separated part of the state administration) formed
  in 2009 by merging the Landesamt für Datenverarbeitung und Statistik
  (LDS NRW, itself descended from the state's 1948 Statistical Office)
  with the three shared regional computing centres (Gemeinsame
  Gebietsrechenzentren) in Hagen, Köln and Münster. Since 2011 it has
  progressively centralised over 200 specialised IT procedures of the
  state administration, and since 2018 has also carried the title
  Statistisches Landesamt (Statistical State Office).

level: subnational
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2009-01-01
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
  - DE-HZD
  - DE-BITBW
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading IT.NRW's own 'Geschichte' page directly (2026-09-20): the organisation was formed in 2009 by merging the Landesamt für Datenverarbeitung und Statistik (LDS NRW, which had itself evolved from the 1948 Statistical State Office and been converted to a Landesbetrieb in 2001) with the three Gemeinsame Gebietsrechenzentren (GGRZ) in Hagen, Köln and Münster. IT.NRW's legal form is explicitly stated as a Landesbetrieb — 'a legally dependent, organisationally separated part of the state administration' oriented toward cost recovery rather than a separate legal person — making it a more direct part of the North Rhine-Westphalian state than [[DE-DATAPORT]] (a multi-Land public-law institution) or [[DE-AKDB]] (owned by municipal associations). Anchor edge under metadata/relationship-types.md §2.3, asserting sub-federal scope via `level: subnational`."
    confidence: high
    valid_from: 2009-01-01
    valid_until: null

sources:
  - title: "Entwicklung des Landesbetriebs IT.NRW"
    url: "https://www.it.nrw/itnrw/geschichte"
    publisher: "Landesbetrieb IT.NRW"
    accessed: "2026-09-20"
  - title: "Landesbetrieb Information und Technik Nordrhein-Westfalen — Wikipedia"
    url: "https://de.wikipedia.org/wiki/Landesbetrieb_Information_und_Technik_Nordrhein-Westfalen"
    publisher: "Wikipedia (German)"
    accessed: "2026-09-20"
---

# IT.NRW — Landesbetrieb Information und Technik Nordrhein-Westfalen

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md`
> item #5 alongside [[DE-DATAPORT]] and [[DE-AKDB]]. Sourced from IT.NRW's
> own "Geschichte" page, read directly.

## Description

IT.NRW is North Rhine-Westphalia's own **IT service provider and
statistical office**, formed in **2009** by merging the **Landesamt für
Datenverarbeitung und Statistik (LDS NRW)** — itself descended from the
Land's Statistical Office of 1948 — with the **three shared regional
computing centres (Gemeinsame Gebietsrechenzentren, GGRZ)** in Hagen,
Köln and Münster.

## A Landesbetrieb, not a separate legal person

Unlike [[DE-DATAPORT]] (a multi-Land public-law institution created by
treaty) or [[DE-AKDB]] (a public-law institution owned by municipal
associations), IT.NRW's own page describes its legal form precisely as a
**Landesbetrieb**: "a legally dependent, organisationally separated part
of the state administration," oriented toward cost recovery rather than
constituted as an independent legal entity. This makes it the most
direct "part of the state" of the three German entities this Atlas now
records, and its `part-of` [[DE]] edge is recorded at `confidence: high`
accordingly.

## Two roles in one body

Confirmed directly: IT.NRW serves the state administration in two
distinct capacities — as **IT service provider** (e-government,
communication networks, software development and operations) and, since
adopting the title **Statistisches Landesamt** in 2018, as North
Rhine-Westphalia's own **statistical office**. Since 2011 it has
progressively centralised over 200 specialised IT procedures previously
run separately across the state administration.

## Not modelled

- The individual predecessor bodies (LDS NRW pre-2009, the three GGRZ)
  as separate entities — described here in prose only.
- IT.NRW's statistical-office role in detail, or any relationship to
  [[EU-EUROSTAT]] or the European Statistical System — no source read
  this pass connects them.
- Any relationship to [[DE-HZD]] (Hesse, 2026-09-20) or [[DE-BITBW]]
  (Baden-Württemberg, 2026-09-20), two more Landesbetrieb-style IT
  providers now modelled — no source connects them; recorded for
  navigation only.

## Relationships

- `part-of` [[DE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
