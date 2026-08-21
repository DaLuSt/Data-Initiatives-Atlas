---
id: FI-SECONDARY-USE-ACT
type: law
name: Act on the Secondary Use of Health and Social Data (552/2019)
alternative_names:
  - Secondary Use Act
  - Laki sosiaali- ja terveystietojen toissijaisesta käytöstä
  - "552/2019"
description: >
  Finnish act of 2019 regulating how health and social data may be used
  outside the purpose for which it was collected — in scientific research,
  statistics, innovation and development, knowledge management, teaching, and
  authority planning and reporting. Its stated purpose is to establish
  conditions for the effective and secure processing of and access to personal
  health and social data for those secondary purposes. It is the basis for the
  social and health data permit authority Findata, established the same year.
  The act is not applied to clinical trials.

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
organisations:
  - FI-FINDATA
related_entities:
  - FI
  - FI-FINDATA
  - EU-EHDS
relationships:
  - type: applies-in
    target: FI
    source: fact
    evidence: "The Secondary Use Act (Act on the Secondary Use of Health and Social Data, 552/2019) regulates how health and social data may be used outside their original purpose, for example in scientific research, statistics, and the planning and reporting duty of an authority; its purpose is to establish conditions for the effective and secure processing of and access to personal health and social data for certain secondary purposes such as research and statistics, innovation and development, knowledge management, teaching and authority planning (findata.fi/en/services-and-instructions/legislation/; stm.fi 'Secondary use of health and social data'; uef.fi library page). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-01-01
    valid_until: null

sources:
  - title: "Legislation — Findata"
    url: "https://findata.fi/en/services-and-instructions/legislation/"
    publisher: "Findata"
  - title: "Secondary use of health and social data"
    url: "https://stm.fi/en/secondary-use-of-health-and-social-data"
    publisher: "Ministry of Social Affairs and Health (Finland)"
  - title: "Act on the Secondary Use of Health and Social Data"
    url: "https://www.uef.fi/en/library/act-on-the-secondary-use-of-health-and-social-data"
    publisher: "University of Eastern Finland Library"
  - title: "Act on Secondary Use of Health and Social Data will not be applied to clinical trials"
    url: "https://findata.fi/en/news/act-on-secondary-use-of-health-and-social-data-will-not-be-applied-to-clinical-trials/"
    publisher: "Findata"
---

# Finnish Secondary Use Act (552/2019)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

The act that governs **secondary use** of Finnish health and social data —
use outside the purpose for which the data was collected. The listed
secondary purposes are:

| |
|---|
| scientific research |
| statistics |
| innovation and development |
| knowledge management |
| teaching |
| authority planning and reporting |

It is the statutory basis for [[FI-FINDATA]], established the same year.

## An exclusion that defines the boundary

The act is **not applied to clinical trials**. That is worth recording rather
than passing over: it marks where the secondary-use regime stops and the
clinical-research regime begins. A trial collects data *for* research, so it
is not secondary use at all — and the Atlas's other health entities do not
draw that line anywhere.

## The first Finnish health entities, and the fourth country in the domain

[[FI]] gained a national layer in the country-expansion batch and had no
health entity. This act and [[FI-FINDATA]] are its first two.

Counting from [[DOMAIN-HEALTH]]'s position before 2026-08-21 — **one country,
the Netherlands** — the domain now reaches five: [[NL]], [[DE]], [[FR]],
[[FI]] and [[DK]], in that order of addition.

## What the date is, and is not

`start_date` is **2019-01-01**, and that is a placeholder for a year rather
than a sourced day. The sources give the act's number — **552/2019** — and
its year, and none of them gives the date of adoption or entry into force.
The identifier is exact; the date is not, and is flagged here rather than
presented as precise.

## Relationships

- `applies-in` [[FI]] — anchor edge.
- The `governed-by` edge lives on [[FI-FINDATA]], the authority the act
  establishes.

## Sources

Listed in frontmatter — Findata's legislation page, the ministry's account of
the regime, a university library guide, and Findata's own notice on the
clinical-trials exclusion.
