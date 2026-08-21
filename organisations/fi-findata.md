---
id: FI-FINDATA
type: organisation
name: Findata
alternative_names:
  - Sosiaali- ja terveysalan tietolupaviranomainen
  - Finnish Social and Health Data Permit Authority
description: >
  Finland's social and health data permit authority, established in 2019 on
  the basis of the Act on the Secondary Use of Health and Social Data. It
  grants data permits for the secondary use of health and social data when
  the data is needed from multiple public data controllers, from the private
  sector, from Findata's own ready-made datasets, or from the Kanta Services.

level: national
country: FI
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-01-01
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - FI
  - FI-SECONDARY-USE-ACT
  - EU-EHDS
relationships:
  - type: part-of
    target: FI
    source: fact
    evidence: "Findata is the social and health data permit authority in Finland, established in 2019 and based on the Act on the Secondary Use of Health and Social Data; it grants data permits for the secondary use of health and social data when data is needed from multiple public data controllers, from the private sector, from Findata's ready-made datasets, or from the Kanta Services (findata.fi; stm.fi 'Secondary use of health and social data'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: a permit authority established by statute is part of the state."
    confidence: medium
    valid_from: 2019-01-01
    valid_until: null
  - type: governed-by
    target: FI-SECONDARY-USE-ACT
    source: fact
    evidence: "Findata is the social and health data permit authority in Finland, established in 2019 and based on the Act on the Secondary Use of Health and Social Data (552/2019) (findata.fi/en/services-and-instructions/legislation/; findata.fi 'A new authority to start operation'). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-01-01
    valid_until: null

sources:
  - title: "Finnish Social and Health Data Permit Authority Findata"
    url: "https://findata.fi/en/"
    publisher: "Findata"
  - title: "Legislation — Findata"
    url: "https://findata.fi/en/services-and-instructions/legislation/"
    publisher: "Findata"
  - title: "A new authority to start operation: faster utilisation of social welfare and health care data resources"
    url: "https://findata.fi/en/news/a-new-authority-to-start-operation-faster-utilisation-of-social-welfare-and-health-care-data-resources/"
    publisher: "Findata"
  - title: "Secondary use of health and social data"
    url: "https://stm.fi/en/secondary-use-of-health-and-social-data"
    publisher: "Ministry of Social Affairs and Health (Finland)"
---

# Findata

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Finland's **social and health data permit authority**, established in 2019
under [[FI-SECONDARY-USE-ACT]]. It grants **data permits** for secondary use
when the data is needed:

- from **multiple** public data controllers;
- from the **private sector**;
- from Findata's own **ready-made datasets**;
- from the **Kanta Services**.

The first of those conditions is the design: a single controller can license
its own data, and the moment a request crosses controllers it becomes
Findata's.

## A permit authority is a different answer from a platform

[[FR-HEALTH-DATA-HUB]] pools 56 members and holds a platform.
[[DK-SUNDHEDSDATASTYRELSEN]] holds the registers itself. Findata holds
comparatively little and **licenses access to what others hold** — a
regulator rather than a custodian.

That distinction is why the Atlas is worth building for this domain. All three
countries have "a national health data body"; the bodies do materially
different jobs, and only putting them side by side shows it.

## Relationships

- `part-of` [[FI]] — anchor edge.
- `governed-by` [[FI-SECONDARY-USE-ACT]], the act it was established under.

## What is not modelled

The **Kanta Services** — Finland's national health record system — are named
in Findata's own description of its remit and have no entity. So does
[[FI]]'s wider social-welfare data layer.

## Sources

Listed in frontmatter — three Findata pages including its legislation page,
and the Ministry of Social Affairs and Health's own account of the regime.
