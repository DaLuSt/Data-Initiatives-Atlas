---
id: CH-OPENDATA-SWISS
type: platform
name: opendata.swiss
description: >
  The central portal for open data of the Swiss public administration,
  operated by the Federal Statistical Office. It is the Swiss counterpart to
  the national open data portals of the other Atlas countries.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - CH-BFS
related_entities:
  - CH-BFS
  - CH-EMBAG
relationships:
  - type: maintained-by
    target: CH-BFS
    source: fact
    evidence: "opendata.swiss is the central portal for open data of the Swiss public administration, and the Federal Statistical Office operates opendata.swiss (bfs.admin.ch 'Das Portal opendata.swiss' and the English 'The opendata.swiss portal'; opendata.swiss). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "opendata.swiss"
    url: "https://opendata.swiss/de"
    publisher: "opendata.swiss / Bundesamt für Statistik"
  - title: "Das Portal opendata.swiss"
    url: "https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/portal.html"
    publisher: "Bundesamt für Statistik (BFS)"
  - title: "The opendata.swiss portal"
    url: "https://www.bfs.admin.ch/bfs/en/home/services/ogd/portal.html"
    publisher: "Federal Statistical Office (FSO)"
---

# opendata.swiss

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

opendata.swiss is the central open data portal of the Swiss public
administration, operated by [[CH-BFS]].

## A national portal with a custodian, unlike two of its peers

[[NL-DATA-OVERHEID]] and [[ES-DATOS-GOB-ES]] are both recorded in the Atlas
as national portals with **no custodian modelled** — a gap queued since the
France batch. opendata.swiss arrives with one, because the Federal
Statistical Office says in its own words that it operates the portal.

## No relationship to [[CH-EMBAG]] is asserted

The EMBAG creates the legal foundations for **open government data** in
Switzerland, and this is the federal open government data portal. The
connection is close to self-evident.

It is still not asserted, because no source read states it. The EMBAG
sources describe the act's purpose in general terms and never name the
portal; the portal's own pages describe what it holds and not the statute it
sits under.

`related_entities` records the adjacency so it is discoverable, and
`discovery/unresolved.md` records the question. An entity pair this obvious
is exactly where a repository starts inventing edges, and this one does not.

## Not modelled

- Whether opendata.swiss exposes **DCAT-AP** or a Swiss application profile,
  and whether the European data portal harvests it. Four countries in the
  Atlas have a DCAT profile entity; Switzerland's status is unknown.
- The **cantonal and communal** open data portals that publish through it.

## Relationships

- `maintained-by` [[CH-BFS]].

## Sources

Listed in frontmatter.
