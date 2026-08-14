---
id: NL-COMMON-GROUND
type: initiative
name: Common Ground
alternative_names:
  - Programma Common Ground
description: >
  Dutch municipal information-management vision and programme, coordinated
  by the VNG, under which municipalities jointly restructure their
  information provision. Its central principle is that data are queried from
  source systems rather than repeatedly copied into applications, enabling
  exchange of current data without duplication.

level: national
country: NL
region: null

status: active
confidence: low
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-VNG
related_entities: []
relationships:
  - type: maintained-by
    target: NL-VNG
    source: fact
    evidence: "Common Ground is presented as a VNG programme on vng.nl/onderwerpen/common-ground and vng.nl/projecten/programma-common-ground. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Common Ground"
    url: "https://vng.nl/onderwerpen/common-ground"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
  - title: "Programma Common Ground"
    url: "https://vng.nl/projecten/programma-common-ground"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
  - title: "Realisatiekoers Common Ground Informatiesamenleving, 21 mei 2025"
    url: "https://vng.nl/sites/default/files/2025-05/20250521-08b-realisatiekoers-common-ground.pdf"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
---

# Common Ground

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Common Ground is the information-science vision through which Dutch
municipalities collectively reorganise their information management, aiming
for a simpler, more flexible and smarter arrangement that improves service
delivery and business operations.

Its defining principle concerns where data lives and how it moves: data
should not be recorded repeatedly across applications, but queried from
source systems, so that current data can be exchanged without copying and
storing it each time. A stated corollary is that data are owned by
government and by citizens themselves rather than by ICT suppliers. The VNG
describes the resulting architecture as ICT "building blocks" that can be
clicked together, providing a base layer carrying generic processes on which
municipalities implement only local customisations.

A *Realisatiekoers Common Ground Informatiesamenleving* dated 21 May 2025
exists, indicating the programme was being actively re-planned at that date.
`status: active` is recorded with `confidence: low` because the current
programme status has not been read from a source.

Common Ground's typing as `initiative` rather than `framework` or
`programme` is an Atlas judgement: it is described as both a vision and a
programme, and both readings are defensible. Flagged in
`discovery/unresolved.md`.

## Relationships

- Run by [[NL-VNG]].
- Municipal counterpart to the government-wide architecture work in
  [[NL-NORA]]; the formal relationship to GEMMA (Batch 4 scope) is not yet
  recorded.

## Atlas interpretation

The choice of entity type, and the positioning of Common Ground relative to
NORA, are Atlas interpretations rather than sourced facts.

## Sources

Listed in frontmatter.
