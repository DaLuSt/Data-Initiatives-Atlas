---
id: NL-RIVM
type: organisation
name: Rijksinstituut voor Volksgezondheid en Milieu
alternative_names:
  - RIVM
  - National Institute for Public Health and the Environment
description: >
  Dutch national institute for public health and the environment, an
  agency (zelfstandig onderdeel) of the Ministry of Health, Welfare and
  Sport (VWS) since 1 January 2004. Its own site marks 110 years of
  history, placing its origin around 1915-1916. It conducts research,
  identifies emerging issues and advises government, professionals and
  citizens on public health, safety and environmental matters, working
  primarily for VWS and also for the ministries responsible for
  infrastructure and water management, agriculture, public governance
  and social affairs, as well as international bodies including the
  European Commission and WHO.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - NL
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Confirmed by reading rivm.nl's own page directly (2026-09-04), in the institute's own words: 'Het RIVM is een zelfstandig onderdeel (agentschap) van het ministerie van Volksgezondheid, Welzijn en Sport (VWS)' (RIVM is an independent part (agency) of the Ministry of Health, Welfare and Sport). The same page references '110 jaar RIVM' (110 years of RIVM) without stating the exact founding date. VWS is not an Atlas entity, so the anchor edge is asserted at country scope. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 2004-01-01
    valid_until: null

sources:
  - title: "RIVM"
    url: "https://www.rivm.nl/over-het-rivm/rivm"
    publisher: "Rijksinstituut voor Volksgezondheid en Milieu (RIVM)"
    accessed: "2026-09-04"
---

# RIVM — Rijksinstituut voor Volksgezondheid en Milieu

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged RIVM, DANS and NWO together
> as unresearched since Batch 2. RIVM's own page was read directly this
> pass.

## Description

RIVM is the Dutch national institute for public health and the
environment. Reading `rivm.nl`'s own page directly, in the institute's
own words: **"Het RIVM is een zelfstandig onderdeel (agentschap) van het
ministerie van Volksgezondheid, Welzijn en Sport (VWS)"** (RIVM is an
independent part (agency) of the Ministry of Health, Welfare and
Sport) — an agency status held since **1 January 2004**, per secondary
reporting not independently fetched this pass.

It conducts research, identifies emerging issues and advises
government, professionals and citizens, working primarily for **VWS**
and also for the ministries responsible for infrastructure and water
management, agriculture, public governance and social affairs, plus
international bodies including the European Commission and WHO.

## A 110-year institution, exact founding date not confirmed

The same page references **"110 jaar RIVM"** (110 years of RIVM)
without stating the founding year explicitly in the content read this
pass — placing its origin around 1915-1916, but `start_date` is left
`null` rather than calculated from an approximate reference.

## Relationships

- `part-of` [[NL]] (anchor edge). VWS is not an Atlas entity, so no
  edge is asserted to it directly.

## Sources

Listed in frontmatter, read directly this pass.
