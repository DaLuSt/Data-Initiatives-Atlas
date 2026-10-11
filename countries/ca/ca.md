---
id: CA
type: country
name: "Canada"
description: >
  Country anchor entity for Canada. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: CA
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
  - CA-OPC
  - CA-PIPEDA
  - CA-PRIVACY-ACT
  - CA-DIRECTIVE-OPEN-GOV
relationships: []

sources:
  - title: "Personal Information Protection and Electronic Documents Act (S.C. 2000, c. 5) — Justice Laws Website"
    url: "https://laws-lois.justice.gc.ca/eng/acts/P-8.6/"
    publisher: "Department of Justice Canada"
    accessed: "2026-10-11"
  - title: "Who we are — Office of the Privacy Commissioner of Canada"
    url: "https://www.priv.gc.ca/en/about-the-opc/who-we-are/"
    publisher: "Office of the Privacy Commissioner of Canada"
    accessed: "2026-10-11"
  - title: "Directive on Open Government — Treasury Board of Canada Secretariat"
    url: "https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=28108"
    publisher: "Treasury Board of Canada Secretariat"
    accessed: "2026-10-11"
---

# Canada

## Description

Canada (ISO 3166-1 alpha-2: **`CA`**) is a **base country anchor**. It carries the federal privacy regulator ([[CA-OPC]]) with the two Acts it oversees ([[CA-PIPEDA]], [[CA-PRIVACY-ACT]]) and the Treasury Board's [[CA-DIRECTIVE-OPEN-GOV]], all read on Government of Canada sites. Provincial privacy laws, Statistics Canada (its page returned HTTP 500) and the data strategy are not yet recorded.

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
