---
id: CZ-DATA-GOV
type: platform
name: data.gov.cz
alternative_names:
  - Národní katalog otevřených dat
  - Czech National Open Data Catalogue
description: >
  Czechia's national open data catalogue (Národní katalog otevřených
  dat, NKOD), publishing datasets from Czech public bodies and
  maintained by the Digital and Information Agency. Under the 2026 Act
  on data management and controlled access, it is being expanded into
  a broader National Data Catalogue covering non-public as well as
  open data.

level: national
country: CZ
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
organisations: []
related_entities:
  - CZ
  - CZ-DIA
  - CZ-ZAKON-60-2026
relationships:
  - type: part-of
    target: CZ
    source: fact
    evidence: "Confirmed by reading data.gov.cz's own homepage directly (2026-08-26), a government portal: anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: CZ-DIA
    source: fact
    evidence: "Confirmed by reading two DIA-published pages directly (2026-08-26). DIA's own project page for 'Rozvoj Národního katalogu otevřených dat (NKOD) a infrastruktury Veřejného datového fondu' (Development of the National Open Data Catalogue and Public Data Fund infrastructure) describes DIA's own work expanding NKOD — the alternative name this entity already carries for data.gov.cz. isvs.cz's report on the 2026 Act, read independently, states directly that the successor 'Národní katalog dat... vznikne rozšířením stávajícího Národního katalogu otevřených dat' (National Data Catalogue will be created by expanding the existing National Open Data Catalogue), 'jehož správcem bude DIA' (of which DIA will be the administrator). data.gov.cz's own homepage footer also lists a 'Národní koordinátor otevřených dat' (National Open Data Coordinator) with a `@dia.gov.cz` contact address, and links directly to dia.gov.cz and DIA's own social media accounts for the portal (LinkedIn, YouTube, X all branded to DIA/`otevrenadata`). This closes the custodian gap this entity previously flagged."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gov.cz — Národní katalog otevřených dat"
    url: "https://data.gov.cz/"
    publisher: "Digitální a informační agentura / Government of the Czech Republic"
    accessed: "2026-08-26"
  - title: "Rozvoj Národního katalogu otevřených dat (NKOD) a infrastruktury Veřejného datového fondu"
    url: "https://www.dia.gov.cz/cs/nase-cinnosti/projekty/projekty-fondy-eu/rozvoj-narodniho-katalogu-otevrenych-dat-nkod-a-infrastruktury-verejneho-datoveho-fondu"
    publisher: "Digitální a informační agentura (DIA)"
    accessed: "2026-08-26"
  - title: "DIA: Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.isvs.cz/dia-zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani/"
    publisher: "ISVS.CZ"
    accessed: "2026-08-26"
---

# data.gov.cz

> **Verified 2026-08-26.** All three cited pages were read directly.
> DIA's own project page and an independent trade-press report close
> the custodian gap this entity previously flagged: DIA both develops
> NKOD today and will formally administer its 2028–2029 successor.

## Description

data.gov.cz is Czechia's national open data catalogue, the Národní
katalog otevřených dat (NKOD).

## The custodian gap, closed

This entity previously flagged itself as "the seventh portal without a
sourced custodian" — [[CZ-DIA]] was the obvious operator, but
[[CZ-ZAKON-60-2026]] making DIA the node connecting Czech data sources
to the European data portal was adjacent to, not proof of, running the
catalogue itself. DIA's own project page, read directly, closes that
gap: it describes DIA's own work "rozšíření Národního katalogu
otevřených dat (NKOD)" (expanding the National Open Data Catalogue) —
DIA's own name for its own project, matching this entity's own
alternative name exactly.

## A bigger catalogue is coming, administered by DIA by name

isvs.cz's report on [[CZ-ZAKON-60-2026]], read directly, states this
catalogue "vznikne rozšířením stávajícího Národního katalogu
otevřených dat" — will be expanded into a **Národní katalog dat**
(National Data Catalogue) covering non-public as well as open data —
"jehož správcem bude DIA" (of which DIA will be the administrator).
The expanded catalogue takes on a controlled-access-intermediary role
from January 2028 and reaches mandatory, government-wide central
registration by January 2029; see [[CZ-ZAKON-60-2026]] for the full
timeline.

## Relationships

- `part-of` [[CZ]] — anchor edge.
- `maintained-by` [[CZ-DIA]].

## Sources

Listed in frontmatter, all three read directly this pass.
