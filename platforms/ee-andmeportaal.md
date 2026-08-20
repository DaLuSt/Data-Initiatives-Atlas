---
id: EE-ANDMEPORTAAL
type: platform
name: Estonian data portal
alternative_names:
  - avaandmed.eesti.ee
  - Eesti andmeportaal
description: >
  Estonia's national data portal, established in 2025 on the basis of the
  previous open data portal, giving an overview of government-held data as
  a single information point for public and third sector data grouped by
  dataset. It consolidates what were previously two environments: open
  data in the former portal and database descriptions in RIHA.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2025-01-01
end_date: null
last_verified: "2026-08-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EE
  - EE-RIA
  - EE-RIHA
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: maintained-by
    target: EE-RIA
    source: fact
    evidence: "The Estonian data portal is published by the Information System Authority (RIA) and described by it as providing an overview of government-held data; the Data Portal was established in 2025, building on the previous open data portal, to support the reuse of data and promote the data economy (ria.ee 'Estonian data portal'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: replaces
    target: EE-RIHA
    source: fact
    evidence: "Prior to the Estonian data portal, data collected by the state and its related descriptions were published in two environments: open data in the former open data portal, and data descriptions for databases in RIHA, the administration system for the state information system; the Data Portal was established in 2025 building on the previous portal (ria.ee 'Estonian data portal'). NOT READ — search-only. Recorded as replacing RIHA's data-description role only — RIHA continues as the administration system."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Estonian data portal | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-based-governance-and-reuse-data/estonian-data-portal"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
  - title: "Administration system for the state information system RIHA"
    url: "https://en.wikipedia.org/wiki/Administration_system_for_the_state_information_system_RIHA"
    publisher: "Wikipedia"
---

# Estonian data portal

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Estonia's national data portal, **established in 2025**, and the newest
national open data portal in the Atlas by several years.

## It replaced a split the other countries still have

Before it, Estonian state data lived in two places: **open data** in the
previous open data portal, and **descriptions of the databases** in
[[EE-RIHA]]. The new portal consolidates both — "an overview of
government-held data … the single information point where anyone can find
public and third sector data".

That split is not an Estonian peculiarity. It is the ordinary arrangement
everywhere else in the Atlas: [[NL-DATA-OVERHEID]] and
[[NL-BASISREGISTRATIES]] are separate things, as are
[[ES-DATOS-GOB-ES]]/[[ES-NTI-RISP]] and [[FR-DATA-GOUV]]. Estonia merging
the catalogue of *datasets* with the catalogue of *systems* is a design
choice the Atlas can now show, because it holds both halves.

## Sources

Listed in frontmatter.

