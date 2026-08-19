---
id: PT-CNCS
type: organisation
name: Centro Nacional de Cibersegurança
alternative_names:
  - CNCS
  - Portuguese National Cybersecurity Centre
description: >
  Portugal's national cybersecurity centre and the supervisory authority for
  cybersecurity regulation in Portugal.

level: national
country: PT
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - PT
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "The Centro Nacional de Cibersegurança is the supervisory authority for Portugal regarding cybersecurity regulations, and is Portugal's national cybersecurity centre (cncs.gov.pt; ecs-org.eu 'NIS2 Directive Transposition Tracker'). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CNCS — Centro Nacional de Cibersegurança"
    url: "https://www.cncs.gov.pt/"
    publisher: "Centro Nacional de Cibersegurança (CNCS)"
  - title: "NIS2 Directive Transposition Tracker"
    url: "https://ecs-org.eu/policy/nis2-directive-transposition-tracker/"
    publisher: "European Cyber Security Organisation (ECSO)"
---

# Centro Nacional de Cibersegurança

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

CNCS is Portugal's national cybersecurity centre and, the sources say, the
**supervisory authority** for cybersecurity regulation in Portugal.

## ⚠ Portugal's NIS2 transposition is not modelled

Every other country in the Atlas with a cyber authority has the instrument
beside it: [[BE-CCB]] with [[BE-NIS2-WET]], [[DE-BSI]] with [[DE-BSIG]],
[[FR-ANSSI]] with [[FR-NIS2-LOI]], [[IE-NCSC]] with [[IE-NCS-BILL]].

**Portugal's transposing instrument was not identified**, so CNCS takes an
anchor edge to [[PT]] rather than a relationship to an act. The gap is
logged in `discovery/unresolved.md`.

## Relationships

- `part-of` [[PT]] — an anchor edge.

## Sources

Listed in frontmatter.
