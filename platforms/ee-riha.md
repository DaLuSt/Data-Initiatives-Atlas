---
id: EE-RIHA
type: platform
name: RIHA — administration system for the state information system
alternative_names:
  - RIHA
  - Riigi infosüsteemi haldussüsteem
description: >
  Estonian administration system in which the databases of the state
  information system are described and registered, regulated by the Public
  Information Act and a special regulation. Before the Estonian data
  portal was established, data descriptions for state databases were
  published here while open data was published in the separate open data
  portal.

level: national
country: EE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
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
  - EE-ATS
  - NL-BASISREGISTRATIES
relationships:
  - type: governed-by
    target: EE-ATS
    source: fact
    evidence: "RIHA, the administration system for the state information system, is regulated by the Public Information Act and a special regulation (en.wikipedia.org 'Administration system for the state information system RIHA', citing the Public Information Act, Riigikogu, RT I 2000, 92, 597). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: EE-RIA
    source: fact
    evidence: "RIA is the national competence centre responsible for managing the technological infrastructure underpinning Estonia's e-government system; data descriptions for state databases were published in RIHA before the Estonian data portal consolidated them (ria.ee 'Estonian data portal'; en.wikipedia.org 'RIHA'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Administration system for the state information system RIHA"
    url: "https://en.wikipedia.org/wiki/Administration_system_for_the_state_information_system_RIHA"
    publisher: "Wikipedia"
  - title: "Estonian data portal | RIA"
    url: "https://www.ria.ee/en/state-information-system/data-based-governance-and-reuse-data/estonian-data-portal"
    publisher: "Riigi Infosüsteemi Amet (RIA)"
---

# RIHA — administration system for the state information system

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

The **administration system for the state information system** — Estonia's
catalogue of the databases the state runs, and the closest thing in the
Atlas to a register *of registers*.

## The Dutch comparison it invites, and does not quite fit

[[NL-BASISREGISTRATIES]] is a *stelsel* of ten authentic registrations with
a legal duty to use them. RIHA is not that: it is the administration system
in which state databases are described and registered. One is a set of
authoritative data sources; the other is the index that says which systems
exist.

**No relationship between them is asserted.** They are the same shape at a
distance and different things up close, which is exactly the case where the
Atlas records the comparison in prose rather than inventing an edge.

## Legal basis

The **[[EE-ATS]]** (Public Information Act) and a special regulation. That
is the one clear statutory anchor found for any part of the Estonian data
infrastructure, which is why the `governed-by` edge sits here rather than on
[[EE-X-TEE]].

## Sources

Listed in frontmatter.

