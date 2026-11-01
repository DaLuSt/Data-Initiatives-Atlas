---
id: INTL-WBG
type: organisation
name: "World Bank Group"
alternative_names:
  - "World Bank"
  - "The World Bank"
  - "WBG"
description: >
  The multilateral development institution whose stated purpose is "to create a world free of poverty on a livable
  planet". In the Atlas for its published data programmes: the World Bank Open Data portal, the Data Catalog and the
  World Development Report 2021 on data. Whether its institutions count as UN specialised agencies is not asserted
  (metadata/ontology.md, decision of 2026-11-01).

level: international
country: null
region: null

status: active
organisation_role: executive
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
organisations: []
related_entities:
  - INTL-WB-OPEN-DATA
  - INTL-WB-DATA-CATALOG
  - INTL-WDR-2021
relationships:
  - type: related-to
    target: INTL-WB-OPEN-DATA
    source: fact
    evidence: "The World Bank's Open Data site (read directly 2026-11-01) is the Bank's own data portal; it 'is expanding to Data360, a newly curated collection of data, analytics, and tools to foster development'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-WB-DATA-CATALOG
    source: fact
    evidence: "The Data Catalog (read directly 2026-11-01) 'is designed to make World Bank's development data easy to find, download, use, and share'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-WDR-2021
    source: fact
    evidence: "The Bank's WDR 2021 page (read directly 2026-11-01) is its report 'Data for Better Lives'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Who we are"
    url: "https://www.worldbank.org/en/who-we-are"
    publisher: "World Bank Group"
    accessed: "2026-11-01"
  - title: "World Bank Open Data"
    url: "https://data.worldbank.org/"
    publisher: "World Bank Group"
    accessed: "2026-11-01"
---

# World Bank Group

> **Created 2026-11-01** (roadmap #511). From the Bank's own pages, read directly: its "Who we are" page and its data portals. The institution's founding (1944), its five member institutions, its membership and its Articles were not read, so none is recorded; this is a first, deliberately narrow entry for its data programmes. It is the first body added under the multilateral-bodies rule in `metadata/ontology.md` (section 6, decided 2026-11-01 as a default the owner can change).

## What is sourced

"We exist to create a world free of poverty on a livable planet." "The World Bank Group tackles the world's biggest problems with job creation." The Open Data site's home page names World Development Indicators ("a compilation of relevant, high-quality, internationally comparable statistics about global development and the fight against poverty"), the Atlas of Global Development 2026 and the expansion to Data360. The page on its own headline reports are not otherwise read.

## Relationships

`related-to` [[INTL-WB-OPEN-DATA]], [[INTL-WB-DATA-CATALOG]] and [[INTL-WDR-2021]].

## Sources

Listed in frontmatter, read directly.
