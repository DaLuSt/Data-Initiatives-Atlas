---
id: UN-GGIM
type: programme
name: United Nations Committee of Experts on Global Geospatial Information Management
alternative_names:
  - UN-GGIM
description: >
  United Nations programme on global geospatial information management,
  established in July 2011 by a resolution of the United Nations Economic
  and Social Council. It works through regional committees, each of which
  liaises with the UN-GGIM Secretariat on topics of interest and major
  developments between meetings of the Committee of Experts, facilitates
  regional development and discussion, and formally feeds into the Committee
  of Experts.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: 2011-07-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - UN
  - UN-GGIM-EUROPE
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "UN-GGIM was established in July 2011 through a resolution by the United Nations Economic and Social Council (ECOSOC); the UN-GGIM Secretariat coordinates the Committee of Experts and its regional committees (ggim.un.org; un.org/globalgeospatial regional committees page; un-ggim-europe.org 'About Us'). NOT READ — search-only."
    confidence: medium
    valid_from: 2011-07-01
    valid_until: null

sources:
  - title: "UN-GGIM — Global Geospatial Information Management"
    url: "https://ggim.un.org/"
    publisher: "United Nations Statistics Division (UNSD)"
  - title: "Regional Committees | Global Geospatial Information Management"
    url: "https://www.un.org/globalgeospatial/en/regional-committees"
    publisher: "United Nations"
  - title: "Fifteenth Session of the United Nations Committee of Experts on Global Geospatial Information Management (UN-GGIM)"
    url: "https://un-ggim-europe.org/news/fifteenth-session-of-the-united-nations-committee-of-experts-on-global-geospatial-information-management-un-ggim/"
    publisher: "UN-GGIM: Europe"
---

# UN-GGIM — Committee of Experts on Global Geospatial Information Management

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

UN-GGIM is the United Nations programme on global geospatial information
management, **established in July 2011 by an ECOSOC resolution**.

It works through **regional committees**, each of which liaises with the
UN-GGIM Secretariat between meetings of the Committee of Experts,
facilitates regional discussion, and formally feeds into the Committee.
[[UN-GGIM-EUROPE]] is the European one.

## The geospatial cluster finally has an international parent

The Atlas has held a geospatial cluster since Batch 5 — [[EU-INSPIRE]],
[[DOMAIN-GEOSPATIAL]], [[NL-GEONOVUM]], [[DE-GEOZG]] — with **nothing above
the EU level**. It is the same shape as the statistics cluster: a
well-developed European and national layer with no international parent,
which is why `discovery/candidates.md` grouped them together.

The parent now exists. **What does not yet exist is the edge from
[[EU-INSPIRE]] to it** — see [[UN-GGIM-EUROPE]] for why.

## Sources are thin, and one is the child

`coverage: low` is honest: the ECOSOC resolution is not cited by number, the
Committee's mandate, membership and outputs are unrecorded, and one of the
three sources is [[UN-GGIM-EUROPE]]'s own news page reporting on a session
of its parent.

That last point matters for a re-verification pass — a regional committee
reporting on the global committee is not an independent source for the
global committee's existence or remit, though it is good evidence of the
relationship between them.

## Relationships

- `part-of` [[UN]].

[[UN-GGIM-EUROPE]] carries the `part-of` edge pointing here.

## Sources

Listed in frontmatter.
