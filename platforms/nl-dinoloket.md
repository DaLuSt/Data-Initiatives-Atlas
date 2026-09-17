---
id: NL-DINOLOKET
type: platform
name: DINOloket
alternative_names:
  - DINO
  - Data en Informatie van de Nederlandse Ondergrond
description: >
  Dutch web portal providing access to subsurface (geological) data and
  models of the Netherlands, developed and managed by TNO Geologische
  Dienst Nederland (the Geological Survey of the Netherlands) on behalf
  of the Ministry of the Interior and Kingdom Relations. It serves data
  from both the historical DINO databank — a repository TNO has
  maintained since before the Basisregistratie Ondergrond (BRO) existed
  — and the BRO itself, making it the modern point of access for
  subsurface data that predates and now sits alongside the basisregistratie.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-17"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-TNO
related_entities:
  - NL-TNO
  - NL-BRO
relationships:
  - type: maintained-by
    target: NL-TNO
    source: fact
    evidence: "Confirmed by reading dinoloket.nl's own 'About us' page and its own homepage/footer directly (2026-09-17): 'DINOloket is developed and managed by TNO Geological Survey of The Netherlands on behalf of the Ministry of the Interior and Kingdom Relations.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: depends-on
    target: NL-BRO
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #140, NL-BRO's own 'predecessors DINO and BIS... neither modelled' finding). Confirmed by reading dinoloket.nl's own pages directly: 'the data originates from both TNO's DINO repository and the BRO (Basisregistratie Ondergrond)' — the portal's current data delivery depends on both sources, one of which (BRO) is a separate Atlas entity. This is a data-delivery dependency, not a claim that DINOloket implements or is governed by BRO."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Welkom op DINOloket"
    url: "https://www.dinoloket.nl/node"
    publisher: "DINOloket (TNO Geologische Dienst Nederland)"
    accessed: "2026-09-17"
  - title: "About us"
    url: "https://www.dinoloket.nl/en/about-us"
    publisher: "DINOloket (TNO Geologische Dienst Nederland)"
    accessed: "2026-09-17"
  - title: "Introduction"
    url: "https://www.dinoloket.nl/en/introduction"
    publisher: "DINOloket (TNO Geologische Dienst Nederland)"
    accessed: "2026-09-17"
---

# DINOloket

> **Created 2026-09-17**, narrowing `discovery/unresolved.md` row #140.
> [[NL-BRO]]'s own file names DINO as a predecessor registration "not
> modelled," noting that "DINO in particular appears to continue to
> exist." Three of DINOloket's own pages, read directly, confirm that
> continuation: DINO is still a live databank, delivered today through
> this portal alongside BRO's own data. BIS, the Alterra soil-information
> system NL-BRO also names, remains genuinely unresearched — see "Not
> modelled" below.

## Description

DINOloket ("Data en Informatie van de Nederlandse Ondergrond") is the
Dutch government's public web portal for subsurface data and geological
models. Confirmed by reading its own "About us" page and homepage
directly: it "is developed and managed by TNO Geological Survey of The
Netherlands on behalf of the Ministry of the Interior and Kingdom
Relations." Its databank comprises "borehole data, groundwater data, cone
penetration test data, vertical electrical soundings, the results of
geological, chemical and mechanical sample analyses, borehole logs and
seismic data."

Its own pages state plainly that its data "originates from both TNO's
DINO repository and the BRO" — meaning the historical DINO databank named
on [[NL-BRO]]'s own file as one of two things the newer basisregistratie
"builds on" has a continuing, documented existence, reachable through this
portal rather than absorbed or discontinued. `depends-on` [[NL-BRO]]
records this data-delivery relationship, not a governance or
implementation claim.

## What is not confirmed

No page read gives an exact founding date for DINOloket or for the DINO
databank itself. A secondary source (geografie.nl, not read directly)
describes the service as having "existed for approximately fifteen years"
as of a 2013 relaunch, implying an original date around 1998 — an
inference, not a sourced fact, so `start_date` stays `null` rather than
being set from arithmetic on an unread source. DINOloket's own
"Introduction" page, read directly, discusses Dutch stratigraphic
nomenclature dating to 1980 and names the **Rijks Geologische Dienst
(RGD)** — TNO's own institutional predecessor for this function, before
TNO absorbed it — but gives no founding date for DINOloket or DINO
themselves.

## Not modelled

- **BIS**, the soil information system from Alterra at Wageningen UR,
  which [[NL-BRO]]'s own file names as the second predecessor
  registration. No source was found or read this pass describing BIS's
  current status, operator page, or whether it continues to exist the
  way DINO does. Left genuinely unresearched rather than assumed
  discontinued or folded into DINOloket.
- **The Rijks Geologische Dienst (RGD)**, TNO's own institutional
  predecessor for the geological-survey function, named on DINOloket's
  own "Introduction" page but not independently researched.

## Relationships

- `maintained-by` [[NL-TNO]].
- `depends-on` [[NL-BRO]] — DINOloket's current data delivery draws on
  both the DINO databank and the BRO register.

## Sources

Three of three read directly: DINOloket's own homepage, "About us" page,
and "Introduction" page.
