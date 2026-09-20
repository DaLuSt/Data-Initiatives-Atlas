---
id: DE-BITBW
type: organisation
name: IT Baden-Württemberg
alternative_names:
  - BITBW
description: >
  Baden-Württemberg's central IT service provider, established as a
  Landesoberbehörde (state upper authority) on 1 July 2015 in the
  Interior Ministry's business area, and operated as a Landesbetrieb
  (state enterprise). Created as the centrepiece of the state's IT
  reorganisation, simultaneously dissolving its predecessor, the
  Informatikzentrum Landesverwaltung Baden-Württemberg (IZLBW). It runs
  a service data centre for the offices of the Baden-Württemberg state
  administration from its seat in Stuttgart-Feuerbach.

level: subnational
country: DE
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2015-07-01
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
  - DE-HZD
  - DE-IT-NRW
  - DE-AKDB
  - DE-LDI
  - DE-IT-NIEDERSACHSEN
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading bitbw.de's own homepage directly (2026-09-20): 'Die Landesoberbehörde IT Baden-Württemberg (abgekürzt BITBW) ist seit dem 1. Juli 2015 der zentrale IT-Dienstleister des Landes Baden-Württemberg. Sie wurde als Landesoberbehörde im Geschäftsbereich des Innenministeriums errichtet und wird als Landesbetrieb geführt.' de.wikipedia.org, also read directly, independently confirms the same date and dual legal characterisation (established as a Landesoberbehörde, operated as a Landesbetrieb), and adds that its predecessor, the Informatikzentrum Landesverwaltung Baden-Württemberg (IZLBW), was 'gleichzeitig dadurch aufgelöst' (simultaneously dissolved). Fourth German sub-federal IT provider in this Atlas after [[DE-DATAPORT]], [[DE-AKDB]] and [[DE-IT-NRW]]/[[DE-HZD]]; unlike the multi-Land [[DE-DATAPORT]], BITBW serves a single Land. Anchor edge under metadata/relationship-types.md §2.3, asserting Baden-Württemberg sub-federal scope via `level: subnational`."
    confidence: high
    valid_from: 2015-07-01
    valid_until: null

sources:
  - title: "Über BITBW"
    url: "https://bitbw.de/"
    publisher: "IT Baden-Württemberg (BITBW)"
    accessed: "2026-09-20"
  - title: "IT Baden-Württemberg"
    url: "https://de.wikipedia.org/wiki/IT_Baden-W%C3%BCrttemberg"
    publisher: "Wikipedia (German)"
    accessed: "2026-09-20"
---

# IT Baden-Württemberg (BITBW)

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md`
> item #5 — Baden-Württemberg's own IT service provider, alongside
> Hesse's [[DE-HZD]], North Rhine-Westphalia's [[DE-IT-NRW]] and
> Bavaria's [[DE-AKDB]]. Sourced from BITBW's own homepage and German
> Wikipedia, both read directly.

## Description

BITBW is Baden-Württemberg's central IT service provider, confirmed
directly on its own homepage: established **1 July 2015** as a
**Landesoberbehörde** (state upper authority) in the business area of
the **Innenministerium** (Interior Ministry), and operated as a
**Landesbetrieb** (state enterprise) — the same dual "authority in legal
form, enterprise in operation" structure this Atlas has now seen across
several German Länder.

## A clean successor, not a merger

Unlike [[DE-IT-NRW]] (formed 2009 by merging the state statistical
office with three regional computing centres), BITBW's own Wikipedia
article, read directly, describes a **one-to-one succession**: BITBW's
creation "gleichzeitig" (simultaneously) dissolved its sole predecessor,
the **Informatikzentrum Landesverwaltung Baden-Württemberg (IZLBW)** —
not modelled here as a separate entity, since no source read this pass
gives it independent significance beyond being BITBW's direct
predecessor under a new legal form.

## The most exactly-dated of the Atlas's German sub-federal IT bodies

Unlike [[DE-HZD]] (year only, 1970) or [[DE-DATAPORT]] and [[DE-AKDB]]
(both dated to the day but decades earlier), BITBW's founding is
confirmed to the exact day — **1 July 2015** — independently by both its
own homepage and Wikipedia, giving this edge `confidence: high` without
qualification.

## Not modelled

- **IZLBW**, BITBW's dissolved predecessor — described here in prose
  only.
- BITBW's internal organisation and full service catalogue beyond
  "service data centre for the offices of the Land administration."

## Relationships

- `part-of` [[DE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
