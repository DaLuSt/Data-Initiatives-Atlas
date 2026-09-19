---
id: EU-INSIEME
type: initiative
name: INSIEME
alternative_names:
  - INSIEME - European Energy Data Space
description: >
  A Digital Europe Programme co-funded flagship project piloting and
  operationalising the Common European Energy Data Space (CEEDS), bringing
  together more than 50 European partners for 15+ pan-European deployments
  across EU member states. It is coordinated by the Department of Smart
  and Interconnected Living (SAIL) at FH OÖ, the University of Applied
  Sciences Upper Austria.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU-CEEDS
relationships:
  - type: part-of
    target: EU-CEEDS
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #132. Confirmed by reading insieme.energy's own homepage directly (2026-09-19): INSIEME 'pioneers the Common European Energy Data Space (CEEDS), creating the digital backbone' and 'connects and streamlines' national and partial data-space solutions 'into a Common European Energy Data Space (CEEDS),' describing itself as the European flagship initiative for CEEDS. This is the same project [[EU-CEEDS]]'s own entity already named in prose (as 'INSIEME, a flagship initiative under the Digital Europe Programme with more than 50 European partners, piloting the building blocks for operationalising CEEDS through 15+ deployments across member states') without its own entity or a typed edge."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "INSIEME - European Energy Data Space"
    url: "https://insieme.energy/"
    publisher: "INSIEME (Digital Europe Programme, grant agreement No. 101194952)"
    accessed: "2026-09-19"
---

# INSIEME

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #132 ("INSIEME, six Horizon Europe energy data-space projects, and
> Germany's ENDA not modelled"). Sourced from the project's own site,
> read directly. The six Horizon Europe predecessor projects and ENDA
> remain unmodelled — see "Not modelled" below.

## Description

INSIEME is a **Digital Europe Programme** co-funded project — confirmed by
reading insieme.energy's own homepage directly, which cites grant
agreement No. 101194952 — that **pilots and operationalises**
[[EU-CEEDS]]. In the project's own words, it "connects and streamlines"
national and partial energy-data solutions "into a Common European Energy
Data Space (CEEDS)," positioning itself as CEEDS's European flagship
initiative.

The consortium brings together **more than 50 European partners** for
**15+ pan-European deployments** across EU member states — the same scale
[[EU-CEEDS]]'s own entity already described in prose before this pass.

## Coordination

INSIEME is led by the **Department of Smart and Interconnected Living
(SAIL)** at **FH OÖ**, the University of Applied Sciences Upper Austria —
confirmed by reading the project's own site directly, which lists
`coordination.insieme@fh-ooe.at` as the project's contact address.

## Not modelled

- The **six Horizon Europe energy data space projects** that [[EU-CEEDS]]'s
  own description says INSIEME and CEEDS build on — not individually named
  by any source read this pass.
- Germany's **ENDA** reference architecture project, named on [[EU-CEEDS]]
  as a national contribution tested on the Redispatch 3.0 use case —
  unresearched this pass.
- INSIEME's **individual partner organisations** and the **specific
  countries** its deployments cover — not itemised on the page read.
- The project's **budget, start date and end date** — not stated on the
  homepage read; a search-only figure (co-funding "more than €16 million",
  running 2025–2028) exists but was not confirmed by a direct read this
  pass, so is not recorded here per the Atlas's no-fabrication convention.

## Relationships

- `part-of` [[EU-CEEDS]] — `confidence: high`.

## Sources

Listed in frontmatter — a single source, read directly. Two further
project pages (`smarten.eu`, `edsoforsmartgrids.eu`) were attempted this
pass; the first returned an HTTP 522 gateway error and the second lacked
the project details sought, so neither is cited.
