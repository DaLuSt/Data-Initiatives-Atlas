---
id: NZ
type: country
name: "New Zealand"
description: >
  Country anchor entity for New Zealand. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: NZ
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
  - NZ-OPC
  - NZ-PRIVACY-ACT-2020
  - NZ-PRIVACY-AMENDMENT-ACT-2025
relationships: []

sources:
  - title: "Who we are — Office of the Privacy Commissioner"
    url: "https://www.privacy.org.nz/about-us/who-we-are/"
    publisher: "Office of the Privacy Commissioner (New Zealand)"
    accessed: "2026-10-16"
---

# New Zealand

## Description

New Zealand (ISO 3166-1 alpha-2: **`NZ`**) is a **base country anchor**. It carries the Office of the Privacy Commissioner ([[NZ-OPC]]), the Privacy Act 2020 ([[NZ-PRIVACY-ACT-2020]]) and the Privacy Amendment Act 2025 ([[NZ-PRIVACY-AMENDMENT-ACT-2025]]), all read on the Commissioner's own site; the Acts' texts were not read (legislation.govt.nz answers with a challenge page).

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). The Government Chief Data Steward and Stats NZ, the Government Data Strategy and the Statistics Act 2022 were not read: data.govt.nz and stats.govt.nz are JavaScript pages that return no text to the agent. It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
