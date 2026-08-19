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

**All fourteen now exist.** Batch 10 created four and deliberately left the
rest, because research had returned only their names; the data-spaces batch
of 2026-08-18 created the other ten.

| Data space | Entity | Note |
|---|---|---|
| Health | [[EU-EHDS]] | Reg. (EU) 2025/327 — **the only one with its own regulation** |
| Mobility | [[EU-EMDS]] | |
| Green deal | [[EU-GREEN-DEAL-DATA-SPACE]] | |
| Agriculture | [[EU-AGRI-DATA-SPACE]] | |
| Energy | [[EU-CEEDS]] | Digital Europe Programme deployment; 15+ member-state pilots |
| Cultural heritage | [[EU-CULTURAL-HERITAGE-DATA-SPACE]] | built on Europeana, 60M+ items |
| Industry | [[EU-MANUFACTURING-DATA-SPACE]] | UNDERPIN and SM4RTENANCE deployments |
| Research and innovation | [[EU-EOSC]] | **the most operational** — EU Node live since Oct 2024 |
| Finance | [[EU-FINANCIAL-DATA-SPACE]] | FIDA is one of three components |
| Language | [[EU-LANGUAGE-DATA-SPACE]] | the one that names **monetisation** |
| Public administrations | [[EU-PUBLIC-ADMIN-DATA-SPACE]] | ⚠ `coverage: low` |
| Skills | [[EU-SKILLS-DATA-SPACE]] | ⚠ `coverage: low` |
| Tourism | [[EU-TOURISM-DATA-SPACE]] | ⚠ `coverage: low` |
| Media | [[EU-MEDIA-DATA-SPACE]] | ⚠ `coverage: low` |

**Four of the ten are still thin**, and say so in their own bodies. Batch 10
declined to create shallow entities and was right to at the time; what
changed is that six of the ten turned out to have real content — deployment
programmes, operators, funding instruments, live infrastructure — once
searched for individually rather than as a list.

The four that remain thin are created anyway, because **holding thirteen of
fourteen would misrepresent the set**. Completeness is the claim the table
above makes; depth is claimed only where `coverage` says so.

## Not uniform, and now visible

Having all fourteen makes the differences legible in a way four could not:

- **One has a Regulation** ([[EU-EHDS]]). One has a named legislative
  component in progress ([[EU-FINANCIAL-DATA-SPACE]], via FIDA). The rest
  rest on funding programmes and governance.
- **One already runs** ([[EU-EOSC]]), with a federation of thirteen
  candidate nodes.
- **One inverts the usual order** ([[EU-CULTURAL-HERITAGE-DATA-SPACE]]),
  designating a data space over infrastructure that had existed for a decade.
- **Their participants differ**: health systems, energy operators, public
  administrations, and — in the language data space — publishers and the
  press, whose stated purpose includes **monetising** their data.

Only [[EU-EHDS]] carries `applies-in` edges to countries. The others are
programmes and initiatives, not instruments, and do not apply in a member
state in the sense that relationship carries here.

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
