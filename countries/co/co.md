---
id: CO
type: country
name: "Colombia"
description: >
  Country anchor entity for Colombia. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: CO
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - CO-LEY-1581-2012
  - CO-SIC
  - CO-DECRETO-767-2022
  - CO-MINTIC
relationships: []

sources:
  - title: "Ley Estatutaria 1581 de 2012 (Secretaría del Senado, base de datos de leyes)"
    url: "http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html"
    publisher: "Secretaría del Senado de la República (Colombia)"
    accessed: "2026-10-16"
    note: "Read as text; the page was last updated 30 September 2026 and carries the Constitutional Court's conditional-constitutionality notes."
---

# Colombia

## Description

Colombia (ISO 3166-1 alpha-2: **`CO`**) is a **base country anchor**. It carries the statutory law on personal data protection ([[CO-LEY-1581-2012]]) and the authority it designates ([[CO-SIC]]), and the Digital Government Policy decree ([[CO-DECRETO-767-2022]]) with the ministry that leads it ([[CO-MINTIC]]); the two texts were read in the official legal databases.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). The Superintendency's own site did not answer. The financial habeas data law (Ley 1266 de 2008), the unified ICT-sector decree (Decreto 1078 de 2015), the open data policy and the national data strategy were not read. It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
