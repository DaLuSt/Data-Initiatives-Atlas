---
id: SE-DATAPORTAL
type: platform
name: Sveriges dataportal
alternative_names:
  - dataportal.se
  - Sweden's data portal
description: >
  Sweden's national data portal, where public agencies' open data is
  collected and made available to public actors, businesses and civil
  society. It lets the public search for data provided by public and
  private organisations, with the aim of making data a strategic societal
  resource and enabling collaboration and innovation around shared data.

level: national
country: SE
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
  - SE
  - SE-DIGG
relationships:
  - type: part-of
    target: SE
    source: fact
    evidence: "Sveriges dataportal is a public body of SE; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: SE-DIGG
    source: fact
    evidence: "DIGG is responsible for Sweden's data portal, which operates at dataportal.se, where government agencies' open data is collected and made available to public actors, businesses and civil society (digg.se; dataportal.se 'Om oss'; mynewsdesk 'DIGG lanserar Sveriges nya dataportal'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Om Sveriges dataportal"
    url: "https://www.dataportal.se/om-oss"
    publisher: "Myndigheten for digital forvaltning (DIGG)"
  - title: "DIGG lanserar Sveriges nya dataportal"
    url: "https://www.mynewsdesk.com/se/digg-myndigheten-foer-digital-foervaltning/pressreleases/digg-lanserar-sveriges-nya-dataportal-3035515"
    publisher: "DIGG via Mynewsdesk"
---

# Sveriges dataportal

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Sweden's national data portal.

## Public *and* private data

Most national portals in the Atlas catalogue government data. Sweden's
is described as carrying data provided by **public and private**
organisations, which is a wider remit than [[NL-DATA-OVERHEID]],
[[ES-DATOS-GOB-ES]] or [[FR-DATA-GOUV]] claim.

It also closes a gap the queue has tracked: Sweden arrives with its
portal custodian already known, unlike the six national portals still
listed there without one.

## Relationships

- `maintained-by` [[SE-DIGG]].

## Sources

Listed in frontmatter.
