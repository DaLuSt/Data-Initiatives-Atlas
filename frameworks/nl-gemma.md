---
id: NL-GEMMA
type: framework
name: Gemeentelijke Model Architectuur
alternative_names:
  - GEMMA
  - Gemeentelijke ModelArchitectuur
description: >
  Reference architecture for Dutch municipalities. A coherent collection of
  architecture products that builds further on international standards and
  the Nederlandse Overheid Referentie Architectuur, developed and managed by
  the Kenniscentrum Architectuur of VNG Realisatie together with
  municipalities, suppliers and chain partners.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-VNG-REALISATIE
related_entities:
  - NL-NORA
  - NL-COMMON-GROUND
  - NL-VNG
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "Confirmed by reading vng.nl's own GEMMA page directly (2026-08-27): GEMMA 'builds further on international standards and the Dutch Government Reference Architecture (NORA)'. noraonline.nl's own GEMMA wiki page, also read directly, confirms GEMMA is part of the 'NORA Familie' spanning domains including governance, subsidies, health, safety, environment, housing, taxes and finance."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-VNG-REALISATIE
    source: fact
    evidence: "Confirmed by reading both vng.nl's own GEMMA page and noraonline.nl's GEMMA wiki page directly (2026-08-27): the Kenniscentrum Architectuur, part of VNG Realisatie, 'develops and manages the GEMMA together with municipalities, suppliers and chain partners.' The NORA wiki page names a specific contact (Theo Peters) for GEMMA, corroborating VNG Realisatie as the operating body rather than VNG generally. A research-queue pickup (2026-09-04) created NL-VNG-REALISATIE as its own Atlas entity and re-points this edge to it from the NL-VNG simplification this file previously carried."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Gemeentelijke Model Architectuur (GEMMA)"
    url: "https://vng.nl/projecten/gemeentelijke-model-architectuur-gemma"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-27"
  - title: "GEMMA (Gemeentelijke ModelArchitectuur)"
    url: "https://www.noraonline.nl/wiki/GEMMA_(Gemeentelijke_ModelArchitectuur)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
  - title: "GEMMA Online — Gemeentelijke modelarchitectuur"
    url: "https://vng.nl/kennisbank-grip-op-informatie/gemma-online-gemeentelijke-modelarchitectuur"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
---

# GEMMA (Gemeentelijke Model Architectuur)

> **Verified 2026-08-27.** Two of three cited pages were read directly this
> pass, closing the previous `search-only` status (never previously
> `last_verified`). The second `vng.nl` page was not re-fetched.

## Description

GEMMA is the reference architecture for all Dutch municipalities. Reading
vng.nl's own page directly confirms, in the organisation's own words, it
"builds further on international standards and... NORA" — making it the
municipal domain-specific extension of the government-wide reference
architecture, now a directly-confirmed fact rather than a search-only
claim.

Its purpose is to give municipalities overview and insight for steering
developments in which business operations and IT interact, to help
municipalities collaborate, and to keep solutions aligned with one another.
The NORA wiki page, read directly, adds that GEMMA spans domains including
governance, subsidies, health, safety, environment, housing, taxes and
finance — a broader domain list than previously recorded.

GEMMA includes theme architectures covering subjects such as Security and
Privacy, Case Management (zaakgericht werken) and [[NL-COMMON-GROUND]], plus
supporting products including the GEMMA Concept Framework and the GEMMA
Standards List. It is published at gemmaonline.nl and the ArchiMate model is
maintained openly on GitHub.

**[[NL-VNG-REALISATIE]]**, whose Kenniscentrum Architectuur develops and
manages GEMMA, is confirmed directly (both vng.nl and the NORA wiki,
which names a specific contact, Theo Peters). A research-queue pickup
(2026-09-04) created it as its own Atlas entity and re-pointed the
`maintained-by` edge to it from the [[NL-VNG]] simplification this file
previously carried.

## Relationships

- Based on [[NL-NORA]] — now `source: fact`.
- Maintained by [[NL-VNG-REALISATIE]] — re-pointed 2026-09-04 from the
  [[NL-VNG]] simplification this entity previously carried.
- Includes a theme architecture for [[NL-COMMON-GROUND]], connecting the
  municipal architecture to the municipal information-management programme.

## Sources

Two of three read directly this pass: `vng.nl`'s main GEMMA page and the
NORA Online wiki entry. The second `vng.nl` "GEMMA Online" page was not
re-fetched.
