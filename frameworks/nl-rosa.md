---
id: NL-ROSA
type: framework
name: Referentie Onderwijs Sector Architectuur
alternative_names:
  - ROSA
  - Ketenreferentiearchitectuur ROSA
description: >
  Chain reference architecture for the entire Dutch education sector,
  covering formal and non-formal education. It aims to promote cooperation
  between chain partners on information provision across all education
  domains. Maintained in the Edustandaard context.

level: sectoral
country: NL
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - NL-NORA
relationships: []

sources:
  - title: "Ketenreferentie-architectuur ROSA"
    url: "https://www.edustandaard.nl/standaard_architecturen/referentie-onderwijs-sector-architectuur-rosa/"
    publisher: "Edustandaard"
  - title: "Relevante architecturen binnen het onderwijs"
    url: "https://www.edustandaard.nl/rosa/onderwijsarchitecturen/"
    publisher: "Edustandaard"
---

# ROSA (Referentie Onderwijs Sector Architectuur)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

ROSA is the chain reference architecture (ketenreferentiearchitectuur) for
the Dutch education sector as a whole, spanning both formal and non-formal
education. Its purpose is to promote cooperation between chain partners on
information provision across all education domains.

It is published in the Edustandaard context. **Edustandaard itself is not
yet an Atlas entity** and is queued in `discovery/research-queue.md`; the
`maintained-by` relationship this framework should carry is therefore left
unasserted rather than pointed at an approximation.

`level: sectoral` rather than `national`, following the same reasoning
applied to [[NL-NICTIZ]]: national in reach, but bounded to one sector.

`domains:` is empty for the same reason it is empty on [[NL-NICTIZ]] —
`DOMAIN-EDUCATION` would now connect ROSA and [[NL-SURF]], which does meet
the two-entity threshold in `metadata/taxonomy.md` §1. It is **not** created
in this batch because Batch 4 is standards and frameworks, not domains;
Batch 5 should create it and tag both entities. Recorded in the research
queue.

## Relationships

None asserted. ROSA's relationship to [[NL-NORA]] is likely (the Dutch
reference architectures generally descend from NORA) but was not sourced.

## Sources

Listed in frontmatter.
