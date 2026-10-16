---
id: CN
type: country
name: "China"
description: >
  Country anchor entity for China. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: CN
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
  - CN-DSL-2021
  - CN-PIPL-2021
relationships: []

sources:
  - title: "Data Security Law of the People's Republic of China (English translation)"
    url: "http://www.npc.gov.cn/englishnpc/c2759/c23934/202112/t20211209_385109.html"
    publisher: "National People's Congress of the PRC (English website)"
    accessed: "2026-10-16"
    note: "Read in full as text; an English translation, and only the Chinese text has legal effect."
---

# China

## Description

China (ISO 3166-1 alpha-2: **`CN`**) is a **base country anchor**. It carries the Data Security Law ([[CN-DSL-2021]]), read in full in the NPC's English translation, and the Personal Information Protection Law ([[CN-PIPL-2021]]), known from a Xinhua report on the NPC's English site; the PIPL's own text was not read.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). The authorities (the Cyberspace Administration of China and the sector regulators are named in the Data Security Law only by function), the Cybersecurity Law, the PIPL's text, the regulations on cross-border data transfers and the national data strategies were not read. Hong Kong, Macao and Taiwan are not covered by this anchor. It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
