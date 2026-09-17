---
id: BE-AGG
type: organisation
name: Antiterroristische Gemengde Groep
alternative_names:
  - AGG
  - Groupe interforces antiterroriste
  - GIA
  - Anti-Terrorist Joint Group
description: >
  Belgium's anti-terrorism threat-analysis body from 1991 to 2006,
  established by royal decree of 17 October 1991 and superseded by the
  Coördinatieorgaan voor de Dreigingsanalyse (OCAD) on 1 December 2006,
  which assumed its rights and obligations under the act of 10 July 2006.

level: national
country: BE
region: null

status: superseded
confidence: high
coverage: low
verification: primary-source

start_date: "1991-10-17"
end_date: "2006-12-01"
last_verified: "2026-09-17"
previous_version: null
successor: BE-OCAD

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - BE-OCAD
  - BE-WET-DREIGINGSANALYSE-2006
relationships:
  - type: part-of
    target: BE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading etaamb.openjustice.be's own text of the Royal Decree of 28 November 2006 directly (2026-09-17), which names the AGG's own founding instrument as the Royal Decree of 17 October 1991."
    confidence: high
    valid_from: "1991-10-17"
    valid_until: "2006-12-01"

sources:
  - title: "28 NOVEMBER 2006. — Koninklijk besluit tot uitvoering van de wet van 10 juli 2006 betreffende de analyse van de dreiging"
    url: "https://etaamb.openjustice.be/nl/koninklijk-besluit-van-28-november-2006_n2006009957.html"
    publisher: "etaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-09-17"
---

# Antiterroristische Gemengde Groep (AGG)

> **Created 2026-09-17**, closing [[BE-OCAD]]'s own "not itself an Atlas
> entity" note. etaamb.openjustice.be's own text of the Royal Decree of 28
> November 2006 — already the instrument [[BE-OCAD]]'s file separately
> flagged as unread — closes two gaps at once: it names the AGG's own
> founding decree and gives OCAD's operational start date, both read
> directly this pass.

## Description

Confirmed by reading the Royal Decree of 28 November 2006's own text
directly: the Antiterroristische Gemengde Groep was established by
**Royal Decree of 17 October 1991**, and operated continuously — the
Decree's own preamble notes it "is immers een orgaan dat 24 uur op de 24
werkt" (is a body that operates 24 hours a day), which the drafters cite
as the reason continuity with its successor mattered.

## Succeeded by OCAD, in the underlying Act's own words

Confirmed by reading the same Royal Decree directly: it implements
Article 17 of [[BE-WET-DREIGINGSANALYSE-2006]] (the Act of 10 July 2006),
which states, in its own words, "het OCAD in de rechten en de
verplichtingen treedt van de Antiterroristische Gemengde Groep" (OCAD
succeeds to the rights and obligations of the AGG) — explicit statutory
succession, including inherited access rights to the AGG's information
systems, framed as necessary to avoid interrupting a body that worked
around the clock.

**Closes a second gap on [[BE-OCAD]]'s own file**: that entity's own
`start_date` (1 December 2006) rested on WebSearch corroboration only,
"not independently confirmed by a directly-read page." This Decree's own
provisions take effect **1 December 2006**, now a directly-read primary
source for the same date.

## Relationships

- `part-of` [[BE]] — scope anchor.

[[BE-OCAD]] now carries `supersedes` → this entity and
`previous_version: BE-AGG`, matching the Atlas's succession convention.

## Not modelled

- The AGG's own internal organisation and history across its 1991–2006
  existence, beyond its founding and succession dates.
- Any acts amending the 1991 founding decree during that period.

## Sources

One of one read directly: etaamb.openjustice.be's own text of the 28
November 2006 Royal Decree.
