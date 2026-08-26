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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading findata.fi's own pages directly (2026-08-26): its legislation page states 'Findata is the social and health data permit authority in Finland. It was established in 2019, and its operations are based on the Act on the Secondary Use of Health and Social Data.' Its own launch announcement, dated 30 December 2019, states 'Findata will start operating in early 2020' — so legal establishment (2019, when the Act took effect) and the start of actual operations (early 2020) are two distinct dates, neither of them 1 January 2019 as this entity previously guessed. Anchor edge under metadata/relationship-types.md §2.3: a permit authority established by statute is part of the state."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: FI-SECONDARY-USE-ACT
    source: fact
    evidence: "Confirmed by reading findata.fi's own legislation page directly (2026-08-26): 'Findata is based on the Act on the Secondary Use of Health and Social Data (552/2019) which entered into force in May 2019.' The same page names a 2025 amendment to that Act — see [[FI-SECONDARY-USE-ACT]] — that introduced a distributed permit model alongside Findata's centralised one."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Finnish Social and Health Data Permit Authority Findata"
    url: "https://findata.fi/en/"
    publisher: "Findata"
    accessed: "2026-08-26"
  - title: "Legislation — Findata"
    url: "https://findata.fi/en/services-and-instructions/legislation/"
    publisher: "Findata"
    accessed: "2026-08-26"
  - title: "A new authority to start operation: faster utilisation of social welfare and health care data resources"
    url: "https://findata.fi/en/news/a-new-authority-to-start-operation-faster-utilisation-of-social-welfare-and-health-care-data-resources/"
    publisher: "Findata"
    accessed: "2026-08-26"
  - title: "Secondary use of health and social data"
    url: "https://stm.fi/en/secondary-use-of-health-and-social-data"
    publisher: "Ministry of Social Affairs and Health (Finland)"
    accessed: "2026-08-26"
---

# Findata

> **Verified 2026-08-26.** All four cited pages were read directly.
> Findata's own launch announcement corrects this entity's founding
> date: it was legally established in 2019 but "will start operating in
> early 2020" — a genuine two-step founding this entity previously
> flattened into one fabricated date (2019-01-01). Its legislation page
> also surfaced a 2025 amendment to its governing Act — see
> [[FI-SECONDARY-USE-ACT]] — that introduces a distributed permit model
> this entity's design-rationale section below no longer states without
> qualification.

## Description

Finland's **social and health data permit authority**, legally
established in 2019 under [[FI-SECONDARY-USE-ACT]] and, per Findata's
own 30 December 2019 announcement, operational from **early 2020**. It
grants **data permits** for secondary use when the data is needed:

- from **multiple** public data controllers;
- from the **private sector**;
- from Findata's own **ready-made datasets**;
- from the **Kanta Services**.

## A 2025 amendment loosened the "crosses controllers" rule

Confirmed by reading findata.fi's own legislation page directly: before
a 2025 amendment (Act 1159/2025, effective 1 May 2026 for its
non-clinical-trial provisions), the moment an application needed data
from more than one controller, "the processing of data permits was
largely centralised under Findata." Since the amendment, applicants may
instead "apply for permits separately from each data controller," who
then "agree among themselves who is responsible for compiling the
dataset" — Findata or one of the other controllers. Findata's
centralised route still exists and is still the entity's core design;
what changed is that crossing controllers no longer makes Findata the
only path.

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

Listed in frontmatter, all four read directly this pass — three
Findata pages including its legislation page, and the Ministry of
Social Affairs and Health's own account of the regime.
