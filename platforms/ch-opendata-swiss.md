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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed verbatim by reading bfs.admin.ch directly (2026-08-22): 'Die Geschäftsstelle OGD, die beim Bundesamt für Statistik angesiedelt ist ... betreibt ... das Portal opendata.swiss.' Independently confirmed on the English page: 'opendata.swiss is the Swiss public administration's centralised portal for open government data (OGD).'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CH-EMBAG
    source: fact
    evidence: "Confirmed by reading bfs.admin.ch's 'Open Government Data (OGD)' page directly (2026-08-22): 'Der Masterplan OGD 2024−2027 ... zielt darauf ab, die Daten der öffentlichen Verwaltung gemäss dem Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG) frei zugänglich zu machen.' The OGD office that operates opendata.swiss states directly that it does so pursuant to the EMBAG's open-government-data mandate — a connection no source read on either entity previously stated by name."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "opendata.swiss"
    url: "https://opendata.swiss/de"
    publisher: "opendata.swiss / Bundesamt für Statistik"
    accessed: "2026-08-22"
  - title: "Das Portal opendata.swiss"
    url: "https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/portal.html"
    publisher: "Bundesamt für Statistik (BFS)"
    accessed: "2026-08-22"
  - title: "The opendata.swiss portal"
    url: "https://www.bfs.admin.ch/bfs/en/home/services/ogd/portal.html"
    publisher: "Federal Statistical Office (FSO)"
    accessed: "2026-08-22"
  - title: "Open Government Data (OGD)"
    url: "https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html"
    publisher: "Bundesamt für Statistik (BFS)"
    accessed: "2026-08-22"
---

# opendata.swiss

> **Verified 2026-08-22.** All four cited pages were read directly and
> confirm the claims below, verbatim in places. A connection this entity
> previously said no source stated has now been found — see "A
> connection now sourced" below. A rebrand was also found and flagged:
> the portal itself advertises a successor, "opendata.swiss next."

## Description

Confirmed by reading opendata.swiss directly (2026-08-22): the portal
lists **16,441 datasets** at the time of reading. opendata.swiss is the central open data portal of the Swiss public
administration, operated by [[CH-BFS]].

A finding worth flagging: the portal's own homepage advertises
**"opendata.swiss next"** — a stated future replacement for the current
site — not otherwise recorded here and not chased further this pass.

## A national portal with a custodian, unlike two of its peers

[[NL-DATA-OVERHEID]] and [[ES-DATOS-GOB-ES]] are both recorded in the Atlas
as national portals with **no custodian modelled** — a gap queued since the
France batch. opendata.swiss arrives with one, because the Federal
Statistical Office says in its own words that it operates the portal.

## A connection now sourced: `governed-by` [[CH-EMBAG]]

The EMBAG creates the legal foundations for **open government data** in
Switzerland, and this is the federal open government data portal. Earlier
passes found the connection self-evident but unsourced: the EMBAG sources
described the act's purpose in general terms without naming the portal,
and the portal's own pages described what it holds without naming the
statute it sits under.

That gap is closed. Confirmed by reading bfs.admin.ch's own "Open
Government Data (OGD)" page directly (2026-08-22): "Der Masterplan OGD
2024−2027 ... zielt darauf ab, die Daten der öffentlichen Verwaltung
gemäss dem [EMBAG] frei zugänglich zu machen. Die Geschäftsstelle OGD ...
betreibt ... das Portal opendata.swiss." The office that runs opendata.swiss
states directly that it does so pursuant to the EMBAG's mandate.
`governed-by` is now asserted on that basis.

## Not modelled

- Whether opendata.swiss exposes **DCAT-AP** or a Swiss application profile,
  and whether the European data portal harvests it. Four countries in the
  Atlas have a DCAT profile entity; Switzerland's status is unknown.
- The **cantonal and communal** open data portals that publish through it.

## Relationships

- `maintained-by` [[CH-BFS]].
- `governed-by` [[CH-EMBAG]] — newly sourced this pass.

## Sources

Listed in frontmatter, all four read directly this pass.
