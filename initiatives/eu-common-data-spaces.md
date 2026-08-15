---
id: EU-COMMON-DATA-SPACES
type: initiative
name: Common European Data Spaces
alternative_names:
  - European data spaces
  - Common European data spaces
description: >
  EU initiative to establish interoperable, EU-wide data spaces in strategic
  sectors and domains of public interest, so that more data becomes
  available for use in the economy, society and research while the companies
  and individuals generating it remain in control. A January 2024 Commission
  staff working document identifies 14 areas.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DATA-STRATEGY
  - EU-EHDS
  - EU-EMDS
  - EU-GREEN-DEAL-DATA-SPACE
  - EU-AGRI-DATA-SPACE
  - EU-DSSC
relationships:
  - type: part-of
    target: EU-DATA-STRATEGY
    source: fact
    evidence: "Common European data spaces in strategic sectors and domains of public interest is the fourth pillar of the European strategy for data (COM(2020)66; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "A European strategy for data"
    url: "https://digital-strategy.ec.europa.eu/en/policies/strategy-data"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Data spaces — SEMIC Support Centre"
    url: "https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/data-spaces"
    publisher: "European Commission — Interoperable Europe Portal"
---

# Common European Data Spaces

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Common European data spaces are the fourth pillar of
[[EU-DATA-STRATEGY]]: EU-wide, interoperable data spaces which the
Commission intends to fund in strategic sectors and domains of public
interest. Their stated purpose is to make more data available for use in the
economy, society and research while keeping the companies and individuals
who generate the data in control.

## The fourteen areas

A Commission staff working document of January 2024 is reported to identify
14 areas: agriculture, cultural heritage, energy, finance, green deal,
health, industry, language, media, mobility, public administrations,
research and innovation, skills, and tourism.

**Batch 10 created four of the fourteen**, and deliberately not the rest:

| Data space | Status in the Atlas |
|---|---|
| Health | [[EU-EHDS]] — has its own regulation; best sourced |
| Mobility | [[EU-EMDS]] — purpose only |
| Green deal | [[EU-GREEN-DEAL-DATA-SPACE]] — purpose only |
| Agriculture | [[EU-AGRI-DATA-SPACE]] — purpose only |
| Cultural heritage, energy, finance, industry, language, media, public administrations, research and innovation, skills, tourism | **Not created** |

The ten not created are ones for which research returned **only their name
in the list of fourteen** — no purpose statement, governance, standards or
infrastructure. Batch 10's brief asks for exactly those attributes, and
creating ten entities whose entire content would be "this is one of the
fourteen" is the shallow-entity failure the brief warns against. They are
enumerated here and queued in `discovery/research-queue.md`.

Even the three created beyond EHDS are thin — one sourced purpose sentence
each — and say so in their own bodies.

## Horizontal support

[[EU-DSSC]] supports the formation of data spaces across sectors, and
publishes [[EU-DSSC-BLUEPRINT]], the shared reference architecture for
building and governing them.

## Anticipated national connections

Two Dutch entities are the obvious counterparts: [[NL-HEALTH-RI]] against
the health data space, and [[NL-NTM]] against mobility. **Neither
relationship is asserted** — no source connects them, and in both cases the
national body's designated role under the EU space is exactly what has not
been established.

## Relationships

- Part of [[EU-DATA-STRATEGY]].

## Sources

Listed in frontmatter.
