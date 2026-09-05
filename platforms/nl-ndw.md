---
id: NL-NDW
type: platform
name: Nationaal Dataportaal Wegverkeer
alternative_names:
  - NDW
  - Nationale Databank Wegverkeersgegevens
  - National Road Traffic Data Portal
description: >
  Dutch national portal for road traffic data, covering national, provincial
  and municipal main roads. A partnership in which Dutch government bodies
  collect, combine, store and distribute mobility data used for traffic
  management, traffic information services and mobility policy. Opened in
  2009.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2009-07-06
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - NL-NTM
  - NL-RIJKSWATERSTAAT
relationships:
  - type: related-to
    target: NL-NTM
    source: fact
    evidence: "Confirmed by reading ndw.nu's own page directly (2026-08-27): NDW 'operates through three portfolios — NDW itself, NTM (a centralized mobility register), and NWB (a current and reliable network of public roads).' This makes explicit, from a page read directly this pass, what the prior text only asserted in prose without a corresponding relationship entry."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Samen sterker, samen goedkoper — NDW"
    url: "https://www.ndw.nu/"
    publisher: "Nationaal Dataportaal Wegverkeer (NDW)"
    accessed: "2026-08-27"
  - title: "Stronger together, cheaper together — National Road Traffic Data Portal"
    url: "https://english.ndw.nu/"
    publisher: "Nationaal Dataportaal Wegverkeer (NDW)"
    accessed: "2026-08-27"
  - title: "Nationaal Dataportaal Wegverkeer (NDW)"
    url: "https://organisaties.overheid.nl/28355859/Nationaal_Dataportaal_Wegverkeer"
    publisher: "Overheid.nl"
    accessed: "2026-08-27"
  - title: "Nationaal Dataportaal Wegverkeer"
    url: "https://nl.wikipedia.org/wiki/Nationaal_Dataportaal_Wegverkeer"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# NDW (Nationaal Dataportaal Wegverkeer)

> **Verified 2026-08-27.** All four cited pages read directly. The 6 July
> 2009 founding date is independently confirmed by both Wikipedia and
> organisaties.overheid.nl. Partner-count sources disagree slightly (18 vs
> 19 government bodies across the two pages read) and both figures are
> recorded rather than picking one silently.

## Description

The NDW is the Dutch national access point for road traffic data, covering
national motorways, provincial roads and municipal main roads. Dutch
government bodies work together in the NDW to collect, combine, store and
distribute mobility data. That data is used to manage traffic, feeds
numerous traffic information services, and provides a basis for mobility
policy. Reading organisaties.overheid.nl's own listing directly this pass
gives **18** government partners by name (the four largest municipalities,
all twelve provinces, [[NL-RIJKSWATERSTAAT]] — now a separate Atlas
entity, added 2026-09-05 — and regional bodies); ndw.nu's own
current page describes **19** governments working together. Both figures
are recorded here rather than silently reconciled, since the two primary
sources genuinely disagree by one and neither page names the discrepancy.

It was opened on 6 July 2009 under the name **Nationale Databank
Wegverkeersgegevens**, confirmed independently by both nl.wikipedia.org and
organisaties.overheid.nl, read directly this pass, and has since been
renamed to Nationaal Dataportaal Wegverkeer (per Wikipedia, on 1 October
2020) while keeping the NDW abbreviation. Both names are recorded in
`alternative_names` so that older documents referring to the databank
resolve to this entity.

The NDW now operates through **three portfolios** — confirmed by reading
ndw.nu's own current page directly this pass: NDW itself, [[NL-NTM]] (a
centralised mobility-data register), and the Nationaal Wegenbestand (NWB, a
current network of public roads).

**Typing note.** The NDW is recorded as a `platform`, but it is arguably as
much an organisation — it is a partnership of governments with its own
listing in the government organisation register. The `platform` typing
follows its primary function as a data portal. Flagged in
`discovery/unresolved.md`.

## Relationships

- `related-to` [[NL-NTM]] — one of NDW's three portfolios; confirmed this
  pass and now recorded as a structured relationship rather than prose only.

## Sources

Listed in frontmatter, all four read directly this pass — the Dutch and
English NDW homepages, the organisaties.overheid.nl government-organisation
listing, and the Wikipedia article.
