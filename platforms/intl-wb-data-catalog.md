---
id: INTL-WB-DATA-CATALOG
type: platform
name: "World Bank Data Catalog"
alternative_names:
  - "datacatalog.worldbank.org"
  - "World Bank Data Catalog (open data catalog, microdata, finances and energy data)"
description: >
  The World Bank's catalog of its development data, made to be easy to find, download, use and share. It includes data
  from the Bank's microdata, finances and energy data platforms and datasets from the open data catalog. Known only
  from its home page.

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
  - INTL-WB-OPEN-DATA
relationships:
  - type: related-to
    target: INTL-WBG
    source: fact
    evidence: "The Catalog (read directly 2026-11-01) is the World Bank's: 'designed to make World Bank's development data easy to find, download, use, and share'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-WB-OPEN-DATA
    source: fact
    evidence: "The Catalog 'includes ... datasets from the open data catalog' (read directly)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "World Bank Data Catalog"
    url: "https://datacatalog.worldbank.org/"
    publisher: "World Bank Group"
    accessed: "2026-11-01"
---

# World Bank Data Catalog

> **Created 2026-11-01** (roadmap #511). Known **only** from the catalog's home page, read directly. Its access terms, its data licence and the sub-platforms it names (microdata, finances, energy) were not read.

## What the home page says

"The Data Catalog is designed to make World Bank's development data easy to find, download, use, and share. It includes data from the World Bank's microdata, finances and energy data platforms, as well as datasets from the open data catalog."

## Relationships

`related-to` [[INTL-WBG]] and [[INTL-WB-OPEN-DATA]] (medium).

## Sources

Listed in frontmatter, read directly.
