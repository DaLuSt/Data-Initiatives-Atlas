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
last_verified: null
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
    evidence: "The Conference of European Statisticians is organised by UNECE; some 65 countries come together at the CES to drive statistical work in the UNECE region and beyond, and its objectives include developing and adopting statistical standards in the UNECE region (unece.org/statistics/ces; unece.org 'About the Conference of European Statisticians'; ec.europa.eu/eurostat Statistics Explained 'Statistical cooperation – introduction'). NOT READ — search-only."
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
---

# CES — Conference of European Statisticians

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

Listed in frontmatter — three UNECE pages and the Eurostat cooperation page
that names the CES as a forum Eurostat sits in.
