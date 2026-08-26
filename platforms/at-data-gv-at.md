---
id: AT-DATA-GV-AT
type: platform
name: data.gv.at
alternative_names:
  - Open Data Osterreich
  - Open Data Österreich
  - Austrian open data catalogue
description: >
  Austria's open data catalogue, operated by the Bundesrechenzentrum since
  its 2014 launch. It is a centralised repository aggregating over 27,000
  datasets from federal, state and municipal sources.

level: national
country: AT
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading brz.gv.at's own Open Data page directly (2026-08-26), which describes data.gv.at as the platform through which citizens and businesses obtain the Austrian administration's public-sector datasets: anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: AT-BRZ
    source: fact
    evidence: "Confirmed verbatim by reading brz.gv.at's own Open Data page directly (2026-08-26): 'Das BRZ betreibt den zentralen österreichischen Datenkatalog (data.gv.at) für den österreichischen Bund sowie die nationalen und internationalen Schnittstellen (EU-Datenportal) zu diesem Datenkatalog' (the BRZ operates the central Austrian data catalogue for the federal government, as well as the national and international interfaces — the EU data portal — to it). The same page dates the launch to 2014 and gives an updated dataset count: 'aktuell sind über 27.000 veröffentlichten Datensätze verfügbar' (currently over 27,000 published datasets are available) — higher than the 20,700 this entity previously carried, unread, from a Wikipedia mention with no figure of its own."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "data.gv.at - Open Data Osterreich"
    url: "https://www.data.gv.at/"
    publisher: "Bundesrechenzentrum (BRZ)"
  - title: "Open Data - data.gv.at - BRZ"
    url: "https://www.brz.gv.at/was-wir-tun/services-produkte/open-data.html"
    publisher: "Bundesrechenzentrum (BRZ)"
    accessed: "2026-08-26"
  - title: "Austrian Federal Computing Centre"
    url: "https://en.wikipedia.org/wiki/Austrian_Federal_Computing_Centre"
    publisher: "Wikipedia"
    accessed: "2026-08-26"
---

# data.gv.at

> **Verified 2026-08-26.** `data.gv.at` itself is a genuine JavaScript
> single-page application — its homepage, robots.txt and every path
> tried return the same empty app shell with no static content, checked
> directly this pass (not a bot-wall: the same shell comes back on a
> `404` as on a `200`). BRZ's own Open Data product page, read directly,
> supplies everything this entity needs instead: the `maintained-by`
> edge stated in BRZ's own words, the 2014 launch date, and an updated
> dataset count.

## Description

Austria's national open data catalogue, run by [[AT-BRZ]] since its
launch in **2014**.

## An updated count, and where the old one came from

The dataset count in this entity's original sourcing — 20,700 — traced
to a bare mention on Wikipedia's BRZ article with no figure attached;
the actual number was never sourced to begin with. BRZ's own Open Data
page, read directly this pass, gives one in its own words: **over
27,000** published datasets, current as of this reading, up from 500
registered applications and roughly 25,000 monthly visits at an earlier
point the same page describes. data.gv.at won first place at the United
Nations Public Service Award in 2014, the year it launched.

## Federal, Land and municipal in one catalogue

data.gv.at aggregates from **federal, state and municipal** sources -
which is notable because the Atlas cannot model two of those three
tiers. The `level` vocabulary has no term for an Austrian *Bundesland*,
the same gap recorded against the German Länder and the Belgian Regions.
BRZ's own page adds a detail the entity did not have: municipalities and
Länder publish "auf freiwilliger oder gesetzlicher Basis" (on a
voluntary or statutory basis) — so unlike the federal layer, their
participation is not uniformly a legal duty.

So the portal is modelled and the governments feeding it are not. That
is the federal gap showing up in a second federal state, which is
precisely what the shortlist ranked Austria to test.

## Sources

Listed in frontmatter. `data.gv.at`'s own homepage was confirmed to be
a content-free JavaScript shell this pass; BRZ's Open Data product page
and Wikipedia were read directly.
