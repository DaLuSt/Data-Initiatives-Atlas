---
id: UN-CES
type: programme
name: Conference of European Statisticians
alternative_names:
  - CES
description: >
  Intergovernmental statistical body organised by the United Nations
  Economic Commission for Europe, bringing together national and
  international statistical experts from some 65 countries to drive
  statistical work in the UNECE region and beyond. Its main objectives are
  to improve official statistics and their comparability, to promote close
  coordination of international statistical activities, to respond to
  emerging needs for international statistical cooperation, and to develop
  and adopt statistical standards in the UNECE region. It holds annual
  plenary sessions with high-level talks for chief statisticians, along with
  seminars and expert meetings, and publishes the Conference of European
  Statisticians Statistical Standards and Studies series.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations:
  - UN-UNECE
related_entities:
  - UN-UNECE
  - EU-EUROSTAT
  - UN-UNSC
relationships:
  - type: part-of
    target: UN-UNECE
    source: fact
    evidence: "Confirmed by reading the Eurostat 'Statistical cooperation — introduction' page directly (2026-08-28): 'Eurostat represents the EU in the Conference of European Statisticians (CES), which is organised by the UNECE,' describing the CES as one of the 'key international forums' Eurostat uses. All three unece.org pages (the CES home page, its about page, and its bureau page) returned HTTP 403 on every attempt this pass — `unece.org` is blocked domain-wide this session, confirmed by testing the bare root domain. A WebSearch cross-check surfaced text that reads as a near-verbatim match to this entity's existing description (65 countries, the same four objectives, annual plenary sessions), suggesting it is drawing on the same unece.org page's cached/indexed text rather than an independent source — corroborating without counting as a page genuinely fetched and read this pass. One of four cited sources read directly is not a majority."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "About the Conference of European Statisticians (CES)"
    url: "https://unece.org/statistics/ces/about-conference-european-statisticians-ces"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "Conference of European Statisticians (CES)"
    url: "https://unece.org/statistics/ces"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "Bureau of the Conference of European Statisticians (CES)"
    url: "https://unece.org/statistics/ces/bureau-conference-european-statisticians-ces"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "Statistical cooperation — introduction"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
    accessed: "2026-08-28"
---

# CES — Conference of European Statisticians

> **Still `search-only` after this pass.** All three `unece.org` sources
> are blocked domain-wide this session (confirmed via the bare root
> domain). Only the Eurostat cooperation page was read directly — it
> confirms the specific claim that matters most to this entity's role in
> the Atlas (Eurostat sits in the CES, which UNECE organises), but one of
> four cited sources is not a majority, and no independent alternate for
> the UNECE-side facts (65 countries, the CES's own objectives) was found
> and genuinely read this pass, so `verification` is not promoted.

## Description

The CES is an intergovernmental statistical body organised by [[UN-UNECE]].
Some **65 countries** take part, driving statistical work in the UNECE
region and beyond.

Its objectives are to improve official statistics and their comparability,
coordinate international statistical activities, respond to emerging needs
for statistical cooperation, and **develop and adopt statistical standards**
in the UNECE region. It runs annual plenary sessions with high-level talks
for chief statisticians, plus seminars and expert meetings, and publishes
the *CES Statistical Standards and Studies* series.

## The forum where the European and UN statistical layers actually meet

[[EU-EUROSTAT]] `participates-in` this Conference. That edge, together with
the one to [[UN-UNSC]], is what ends the Atlas's UN-layer isolation.

It is worth being precise about why this entity is the right attachment
point rather than a convenience. The Atlas refused [[UN-UNSD]] →
[[EU-EUROSTAT]] three times, and the refusals were correct: **the two
organisations are not related to each other directly.** They meet in
forums. The CES is one of those forums, it is named as such by Eurostat's
own cooperation page, and it belongs to UNECE rather than to either party.

That is a genuinely different claim from "Eurostat is connected to the UN
statistical system", and it is the one the sources support.

## `programme`, not `organisation`

The CES is a standing intergovernmental conference with a Bureau, which
makes `organisation` arguable. It is typed `programme` because
`metadata/taxonomy.md` reserves `organisation` for bodies with their own
institutional identity, and the CES is convened *by* UNECE rather than
existing beside it — the same reading that types [[UN-GGIM]] a programme.

Logged in `discovery/unresolved.md` as a typing question rather than
presented as settled.

## Relationships

- `part-of` [[UN-UNECE]].

## Sources

Listed in frontmatter, one of four read directly this pass: the Eurostat
cooperation page, which names the CES as a forum Eurostat sits in. All
three UNECE pages remain 403-blocked this session.
