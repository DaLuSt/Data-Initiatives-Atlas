---
id: INTL-OECD-CSSP
type: programme
name: OECD Committee on Statistics and Statistical Policy
alternative_names:
  - CSSP
  - OECD statistics committee
  - CSTAT
description: >
  The OECD's committee on statistics and statistical policy, named by
  Eurostat as one of the key international forums in which it represents the
  European Union, alongside the United Nations Statistical Commission and
  the Conference of European Statisticians. Eurostat describes these
  international statistical agencies as cooperating to set up international
  standards for statistics, improve the comparability of statistical
  information, improve the coordination of international statistics-related
  activities, and support national statistical systems financially or
  technically.

level: international
country: null
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations:
  - INTL-OECD
related_entities:
  - INTL-OECD
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: INTL-OECD
    source: fact
    evidence: "Eurostat states that it represents the EU in key international forums such as the United Nations Statistical Commission, the Conference of European Statisticians organised by the UNECE, and the OECD's committee on statistics and statistical policy (CSSP); a parallel passage on the same Eurostat page describes Eurostat as representing the European Commission in the OECD's statistics committee (CSTAT) (ec.europa.eu/eurostat Statistics Explained 'Statistical cooperation – introduction'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Statistical cooperation — introduction"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
  - title: "Statistical cooperation — introduction (alternate path)"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php/Statistical_cooperation_-_introduction"
    publisher: "Eurostat — European Commission"
---

# OECD Committee on Statistics and Statistical Policy

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The CSSP is the OECD's committee on statistics and statistical policy. It is
recorded here because [[EU-EUROSTAT]]'s own cooperation page names it as one
of three forums in which Eurostat represents the European Union — with the
[[UN-UNSC]] and the [[UN-CES]].

## Why a non-UN body is in a UN-layer batch

`discovery/candidates.md` predicted this and it held:

> *The same Eurostat page reportedly names the CSSP alongside the UNSC and
> CES — so **one page read may close the OECD gap and the UN gap
> together**.*

[[INTL-OECD]] had sat in the Atlas since Batch 13 **with no instrument
beneath it and no relationship to anything**. It was as isolated as the UN
layer and attracted less attention because it is one node rather than nine.
The same sentence that connects Eurostat to the UN statistical system
connects it here.

## The name is unsettled, and both versions are recorded

The sources give **two different names and acronyms** for what appears to be
the same body:

| Rendering | Where |
|---|---|
| *committee on statistics and statistical policy* (**CSSP**) | the passage naming the EU's three forums |
| *statistics committee* (**CSTAT**) | a parallel passage on the same Eurostat page describing what Eurostat represents the Commission in |

Both are in `alternative_names`, and the entity is `confidence: low`
because of it. The two passages also differ on **who is represented** — "the
EU" in one and "the European Commission" in the other — which is not a
distinction the Atlas can resolve without reading the page.

`coverage: low` is likewise deliberate: the committee's mandate,
composition, meeting cadence and outputs are all unrecorded. Everything here
comes from one Eurostat page, and **no OECD source is cited at all** — the
committee is described only from the outside, by a participant. That is the
first thing a re-verification pass should fix.

## Relationships

- `part-of` [[INTL-OECD]].

[[EU-EUROSTAT]] carries the `participates-in` edge pointing here.

## Sources

Listed in frontmatter. Both entries are the same Eurostat page under its two
URL forms, which is unusual and is recorded honestly rather than padded out:
this entity rests on **one document**.
