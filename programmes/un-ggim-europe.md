---
id: UN-GGIM-EUROPE
type: programme
name: "UN-GGIM: Europe"
alternative_names:
  - UN-GGIM Europe
  - European Regional Committee of UN-GGIM
description: >
  European regional committee of the United Nations Committee of Experts on
  Global Geospatial Information Management, formally established on 1 October
  2014 in Chișinău, Moldova. Its aim is to contribute to the more effective
  management and availability of geospatial information in Europe and to
  ensure that the Regional Committee's work is aligned to the global UN-GGIM
  programme, with a stated mission of maximising the use of geospatial
  information in Europe for a safer and more sustainable world. It operates
  through working groups.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2014-10-01
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - UN-GGIM
  - EU-INSPIRE
relationships:
  - type: part-of
    target: UN-GGIM
    source: fact
    evidence: "Confirmed by reading un-ggim-europe.org's own 'About Us' and 'Working Groups' pages, and un.org's regional-committees page, all directly (2026-08-28). The About Us page states UN-GGIM: Europe is a regional entity of the Committee of Experts, formally established 1 October 2014, aiming to 'ensure that the national mapping and cadastral authorities and national statistical institutes in the European UN Member States...work together', and notes it 'is supported by EuroGeographics' with headquarters in Brussels — a previously-unconfirmed detail. un.org's regional-committees page confirms each committee 'liaises with the UN-GGIM Secretariat' and 'formally feeds into the Committee of Experts.' The EuroGeographics PDF returned HTTP 404 this pass and was not read."
    confidence: high
    valid_from: 2014-10-01
    valid_until: null

sources:
  - title: "About Us | UN-GGIM: Europe"
    url: "https://un-ggim-europe.org/about-us/"
    publisher: "UN-GGIM: Europe"
    accessed: "2026-08-28"
  - title: "Working Groups | UN-GGIM: Europe"
    url: "https://un-ggim-europe.org/working-groups/"
    publisher: "UN-GGIM: Europe"
    accessed: "2026-08-28"
  - title: "Regional Committees | Global Geospatial Information Management"
    url: "https://www.un.org/globalgeospatial/en/regional-committees"
    publisher: "United Nations"
    accessed: "2026-08-28"
  - title: "UN-GGIM: An Overview — INSPIRE KEN Webinar, December 2016"
    url: "https://eurogeographics.org/app/uploads/2018/04/20161213_GGIM_OverView_INSPIREKEN_0.pdf"
    publisher: "EuroGeographics"
---

# UN-GGIM: Europe

> **Verified 2026-08-28.** Three of four cited pages were read directly.
> The EuroGeographics PDF now 404s (it may have been moved or removed since
> the original search) and was not read, but the two un-ggim-europe.org
> pages and the un.org regional-committees page were, giving a genuine
> majority. A useful bonus fact surfaced: UN-GGIM: Europe's own page states
> it "is supported by EuroGeographics" and is headquartered in Brussels —
> the clearest confirmation yet of the EuroGeographics connection this
> entity's body previously flagged only as a plausible missing node.

## Description

UN-GGIM: Europe is the **European regional committee** of [[UN-GGIM]],
formally established on **1 October 2014 in Chișinău, Moldova**.

Its aim is to contribute to more effective management and availability of
geospatial information in Europe and to keep the Regional Committee's work
aligned to the global UN-GGIM programme. It operates through working groups.

## The INSPIRE link was looked for and not found

`discovery/candidates.md` set this up precisely:

> *INSPIRE is discussed in its context, though **no source read states a
> relationship** — that is the thing to verify.*

It was searched for and **it is still not established.** What the searches
returned is real but insufficient: a 2016 EuroGeographics presentation
titled *"UN-GGIM: An Overview"* delivered to an **INSPIRE Knowledge Exchange
Network webinar**, and general discussion of INSPIRE data harmonisation in
UN-GGIM: Europe's working-group context.

A presentation given by a third party to an INSPIRE audience about UN-GGIM
is evidence that the two communities talk to each other. **It is not
evidence that [[EU-INSPIRE]] is derived from, governed by, aligned with or
part of anything in the UN-GGIM structure**, and no such edge is asserted.

So this batch closed three of the four clusters in `candidates.md` and left
the geospatial one **structurally incomplete on purpose**: the UN parent
exists, the European regional committee exists, and the edge to the European
instrument does not, because nothing read supports one.

## The missing European node is probably EuroGeographics

The same shape that blocked the statistics cluster appears here. In
statistics the missing node was [[EU-ESS]], the partnership Eurostat and the
national offices both belong to. In geospatial it is plausibly
**EuroGeographics**, the European association of national mapping, cadastral
and land registry authorities, which appears throughout this material and
authored the cited presentation.

It is **not created here**, but this pass strengthens the case for it:
UN-GGIM: Europe's own "About Us" page, read directly, now states in its own
words that the committee "is supported by EuroGeographics" and gives a
Brussels headquarters address — the clearest first-party statement of the
relationship found so far, stronger than the previously-cited third-party
presentation. Creating a full `EuroGeographics` entity is still outside this
pass's scope (it is not a UN body and this batch is the UN cluster), but the
research-queue item is now better evidenced than before. Queued in
`discovery/research-queue.md`.

## Relationships

- `part-of` [[UN-GGIM]].

## Sources

Listed in frontmatter, three of four read directly this pass — both
UN-GGIM: Europe pages and the UN regional committees page. The
EuroGeographics presentation, the closest thing found to an INSPIRE
connection, now 404s and was not read.
