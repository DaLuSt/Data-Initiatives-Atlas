---
id: IE-DATA-GOV-IE
type: platform
name: data.gov.ie
alternative_names:
  - Ireland's Open Data Portal
description: >
  Ireland's national open data portal, publishing datasets from Irish public
  bodies. It is the Irish counterpart to the national open data portals of
  the other Atlas countries.

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IE
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: part-of
    target: IE
    source: fact
    evidence: "Confirmed by reading data.gov.ie directly (2026-08-22): 'IRELAND'S OPEN DATA PORTAL — Promoting innovation and transparency through the publication of Irish Public Sector data,' with 22,623 datasets and 143 publishers listed at the time of reading. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gov.ie — Ireland's Open Data Portal"
    url: "https://data.gov.ie/"
    publisher: "Government of Ireland"
    accessed: "2026-08-22"
  - title: "Open Data Directive"
    url: "https://digital-strategy.ec.europa.eu/en/policies/open-data"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-22"
---

# data.gov.ie

> **Verified 2026-08-22.** Both cited pages were read directly and
> confirmed the claims below verbatim.

## Description

Confirmed by reading data.gov.ie directly (2026-08-22): "IRELAND'S OPEN
DATA PORTAL — Promoting innovation and transparency through the
publication of Irish Public Sector data," listing 22,623 datasets from
143 publishers at the time of reading. data.gov.ie is Ireland's national
open data portal.

## The third portal in the Atlas with no custodian modelled

[[NL-DATA-OVERHEID]] and [[ES-DATOS-GOB-ES]] already carry this gap, queued
since the France batch. data.gov.ie joins them: no source read names the
body that operates it.

[[CH-OPENDATA-SWISS]], added in the same batch as this entity, **does** have
one — [[CH-BFS]] says in its own words that it operates the portal. Two
portals written on the same day, one with a custodian and one without, on
exactly the difference in what the sources say.

## Ireland's Open Data Directive transposition — now identified

An earlier version of this entity recorded the transposing instrument as
**not identified**, noting only that it would be an S.I. rather than an Act.

It is **[[IE-PSI-REGULATIONS-2021]]** — S.I. No. 376/2021, made **22 July
2021**, five days after the Directive's 17 July deadline. Ireland is the one
member state in the Atlas that transposed by a **standalone** instrument
rather than by amending an existing act.

Belgium, France and Spain remain unidentified; Portugal's turned out to be
[[PT-LEI-26-2016]], an amendment.

## Sources

Listed in frontmatter, both read directly this pass. The Commission's
open-data policy page confirms [[EU-OPEN-DATA-DIRECTIVE]] "entered into
force on 16 July 2019, replacing the 2003 PSI Directive" — a detail not
previously recorded on this entity.
