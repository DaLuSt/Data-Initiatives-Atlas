---
id: CL
type: country
name: "Chile"
alternative_names:
  - "Republic of Chile"
  - "República de Chile"
description: >
  Country anchor entity for Chile. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: CL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - CL-LEY-21719
  - CL-AGENCIA-PDP
relationships: []

sources:
  - title: "Diario Oficial de la República de Chile, n° 44.176, 17 de junio de 2025 — decreto n° 12 que crea la Comisión Asesora Ministerial para la implementación de la ley n° 21.719"
    url: "https://www.diariooficial.interior.gob.cl/publicaciones/2025/06/17/44176/01/2660255.pdf"
    publisher: "Diario Oficial de la República de Chile (Ministerio del Interior)"
    accessed: "2026-10-11"
  - title: "Ley 21.719 que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales"
    url: "https://academiajudicial.cl/recursos/actualizaciones-normativas/ley-21-719-que-regula-la-proteccion-y-el-tratamiento-de-los-datos-personales-y-crea-la-agencia-de-proteccion-de-datos-personales/"
    publisher: "Academia Judicial de Chile"
    accessed: "2026-10-11"
---

# Chile

## Description

Chile (ISO 3166-1 alpha-2: **`CL`**) is a **base country anchor**. It carries the 2024 personal-data law ([[CL-LEY-21719]]) and the Agency it creates ([[CL-AGENCIA-PDP]]), known from the Diario Oficial and the Academia Judicial; the law's own text was not readable (`bcn.cl` challenge). Ley 19.628 of 1999 is not recorded as an entity.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
