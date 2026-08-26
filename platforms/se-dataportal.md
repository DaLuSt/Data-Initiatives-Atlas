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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
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
    evidence: "Sveriges dataportal is a public body of SE; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: SE-DIGG
    source: fact
    evidence: "Confirmed verbatim by reading dataportal.se's own 'Om oss' page directly (2026-08-25): '(Digg) ansvarar för Sveriges dataportal. Sveriges dataportal gör det möjligt för allmänheten att söka bland data som tillhandahålls av offentliga och privata organisationer... Målet är att data ska bli en strategisk samhällsresurs' (DIGG is responsible for Sweden's data portal, which lets the public search data provided by public and private organisations... the goal is for data to become a strategic societal resource) — matching this entity's description almost word for word."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Om Sveriges dataportal"
    url: "https://www.dataportal.se/om-oss"
    publisher: "Myndigheten for digital forvaltning (DIGG)"
    accessed: "2026-08-25"
  - title: "DIGG lanserar Sveriges nya dataportal"
    url: "https://www.mynewsdesk.com/se/digg-myndigheten-foer-digital-foervaltning/pressreleases/digg-lanserar-sveriges-nya-dataportal-3035515"
    publisher: "DIGG via Mynewsdesk"
    accessed: "2026-08-25"
---

# Sveriges dataportal

> **Verified 2026-08-25.** Both cited pages were read directly.
> dataportal.se's own page states DIGG's custodianship in almost the
> same words this entity already used.

## Description

Confirmed by reading dataportal.se directly (2026-08-25): Sweden's
national data portal.

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

Listed in frontmatter, both read directly this pass.
