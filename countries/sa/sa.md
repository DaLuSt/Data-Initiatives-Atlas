---
id: SA
type: country
name: "Saudi Arabia"
description: >
  Country anchor entity for Saudi Arabia. A base anchor: it exists because the Atlas models the sourced national entities
  listed in its index, and it carries no more than that.

level: national
country: SA
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - SA-NCA
  - SA-NCA-LEGAL-POWERS-2024
  - SA-NCA-ECC
  - SA-NCA-DCC
  - SA-NCSS
relationships: []

sources:
  - title: "Laws and Regulations — National Cybersecurity Authority"
    url: "https://nca.gov.sa/en/laws-and-regulations/"
    publisher: "National Cybersecurity Authority (NCA), Saudi Arabia"
    accessed: "2026-11-01"
---

# Saudi Arabia

## Description

Saudi Arabia (ISO 3166-1 alpha-2: **`SA`**) is a **base country anchor**. It carries the National Cybersecurity Authority ([[SA-NCA]]), the Royal Decree on its legal powers ([[SA-NCA-LEGAL-POWERS-2024]]), its Essential and Data Cybersecurity Controls ([[SA-NCA-ECC]], [[SA-NCA-DCC]]) and the National Cybersecurity Strategy ([[SA-NCSS]]), all from the Authority's own English site; no document's text was opened. The Personal Data Protection Law and the Saudi Data and Artificial Intelligence Authority (SDAIA) are not here: `sdaia.gov.sa` rejects the agent's requests.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). It is a first sourced slice, not a survey of the country's data governance: the Personal Data Protection Law, SDAIA and its National Data Management Office, the Communications, Space and Technology Commission and the Digital Government Authority are not in the Atlas yet (see `countries/README.md` on the participation model).
