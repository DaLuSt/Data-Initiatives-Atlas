---
id: AT-DATA-GV-AT
type: platform
name: data.gv.at
alternative_names:
  - Open Data Osterreich
  - Open Data Österreich
  - Austrian open data catalogue
description: >
  Austria's open data catalogue, operated by the Bundesrechenzentrum. It
  is a centralised repository aggregating over 20,700 datasets from
  federal, state and municipal sources.

level: national
country: AT
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
  - AT
  - AT-BRZ
relationships:
  - type: part-of
    target: AT
    source: fact
    evidence: "data.gv.at is a public body of AT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: AT-BRZ
    source: fact
    evidence: "BRZ operates the Austrian Open Data Catalogue at data.gv.at, a centralised repository aggregating over 20,700 datasets from federal, state and municipal sources (brz.gv.at; en.wikipedia.org 'Austrian Federal Computing Centre'). NOT READ - search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gv.at - Open Data Osterreich"
    url: "https://www.data.gv.at/"
    publisher: "Bundesrechenzentrum (BRZ)"
  - title: "Austrian Federal Computing Centre"
    url: "https://en.wikipedia.org/wiki/Austrian_Federal_Computing_Centre"
    publisher: "Wikipedia"
---

# data.gv.at

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Austria's national open data catalogue.

## Federal, Land and municipal in one catalogue

data.gv.at aggregates from **federal, state and municipal** sources -
which is notable because the Atlas cannot model two of those three
tiers. The `level` vocabulary has no term for an Austrian *Bundesland*,
the same gap recorded against the German Länder and the Belgian Regions.

So the portal is modelled and the governments feeding it are not. That
is the federal gap showing up in a second federal state, which is
precisely what the shortlist ranked Austria to test.

## Sources

Listed in frontmatter.
