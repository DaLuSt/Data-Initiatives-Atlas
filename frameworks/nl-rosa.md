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

domains:
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - NL-NORA
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "NORA has daughter architectures (NORA dochters) from government domains, including EAR for central government, GEMMA for municipalities, PETRA for the provinces and WILMA for the water boards, alongside domain and chain architectures such as ROSA for education, KARWEI for work and income and SRK for the criminal justice chain (noraonline.nl/wiki/NORA_dochters; noraonline.nl/wiki/Visie_op_dochters; nl.wikipedia.org 'Nederlandse Overheid Referentie Architectuur'). NOT READ — search-only. This entity is ROSA, the education chain architecture, named in that list."
    confidence: medium
    valid_from: null
    valid_until: null

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

Tagged [[DOMAIN-EDUCATION]], created in Batch 5 — ROSA's own creation in
Batch 4 is what brought that domain to the two-entity threshold in
`metadata/taxonomy.md` §1, alongside [[NL-SURF]].

## Relationships

- `based-on` [[NL-NORA]] — **now sourced.** An earlier version of this entity
  said the NORA relationship was "likely… but was not sourced". NORA's own
  wiki enumerates its *dochters*: EAR for central government, GEMMA for
  municipalities, PETRA for the provinces, WILMA for the water boards, and
  domain and chain architectures including **ROSA for education**. The same
  page sources [[NL-PETRA]] and [[NL-EAR]].

The `maintained-by` edge to Edustandaard is still unasserted — that body is
still not an Atlas entity.

## Sources

Listed in frontmatter.
