---
id: INTL-WB-OPEN-DATA
type: platform
name: "World Bank Open Data"
alternative_names:
  - "World Bank Open Data site"
  - "data.worldbank.org"
  - "Data360"
description: >
  The World Bank's open data portal: World Development Indicators and other World Bank time series, economy profiles,
  and, from 2026, the Atlas of Global Development. Its home page says the site "is expanding to Data360, a newly
  curated collection of data, analytics, and tools to foster development". Known only from its home page.

level: international
country: null
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

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - INTL-WBG
related_entities:
  - INTL-WBG
  - INTL-WB-DATA-CATALOG
relationships:
  - type: related-to
    target: INTL-WBG
    source: fact
    evidence: "The portal is on the World Bank's own domain, data.worldbank.org, and is introduced as 'the World Bank open data site' (read directly 2026-11-01)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-WB-DATA-CATALOG
    source: fact
    evidence: "The Open Data home page and the Data Catalog both belong to the Bank; the catalog 'includes data from the World Bank's microdata, finances and energy data platforms, as well as datasets from the open data catalog' (read directly)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "World Bank Open Data"
    url: "https://data.worldbank.org/"
    publisher: "World Bank Group"
    accessed: "2026-11-01"
---

# World Bank Open Data

> **Created 2026-11-01** (roadmap #511). Known **only** from the portal's home page, read directly. The terms of use, the licence and the Data360 pages were not read, so no licence is recorded.

## What the home page says

World Development Indicators: "a compilation of relevant, high-quality, internationally comparable statistics about global development and the fight against poverty". "The Atlas of Global Development 2026 presents interactive storytelling and data visualizations on key global trends related to people, prosperity, our planet, infrastructure, and digital transformation." Theme areas include people (education, health, social protection, gender), the planet's natural resources, and clean energy, transport and cities. An economy can be selected on a map to see its data and profile.

## Relationships

`related-to` [[INTL-WBG]] and, at medium confidence, [[INTL-WB-DATA-CATALOG]].

## Sources

Listed in frontmatter, read directly.
