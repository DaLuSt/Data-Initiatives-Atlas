---
id: NL-AWR
type: act
name: Algemene wet inzake rijksbelastingen
name_en: "General State Taxes Act"
alternative_names:
  - AWR
  - General State Taxes Act
description: >
  Dutch general act on state taxes, originally the act of 2 July 1959 laying
  down the rules common to a number of state taxes. The Atlas records it for
  one chapter, Hoofdstuk IVA "Basisregistratie inkomen" (articles 21 to 22i),
  which is the statutory basis of the income base registry.

level: national
country: NL
region: EU

status: active
rank: ordinary
confidence: medium
coverage: low
verification: primary-source

start_date: 1959-07-02
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-BRI
  - NL-BASISREGISTRATIES
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "The Algemene wet inzake rijksbelastingen is a Dutch act, published on wetten.overheid.nl under identifier BWBR0002320 (read directly 2026-10-11; its page gives the original act as 'Wet van 2 juli 1959, houdende regelen, welke aan een aantal rijksbelastingen gemeen zijn'). Anchor edge under metadata/relationship-types.md §2.3; it asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Algemene wet inzake rijksbelastingen — BWBR0002320"
    url: "https://wetten.overheid.nl/BWBR0002320/"
    publisher: "Overheid.nl (wetten.nl)"
    accessed: "2026-10-11"
    note: "Read directly; the table of contents lists Hoofdstuk IVA 'Basisregistratie inkomen (Artikelen 21-22i)'. The page gives the act's date but not the Staatsblad citation or the date Hoofdstuk IVA entered into force."
---

# Algemene wet inzake rijksbelastingen (AWR)

## Description

A general tax act that applies across several Dutch state taxes. **This entity
covers one chapter of it.** Hoofdstuk IVA, "Basisregistratie inkomen"
(articles 21 to 22i), sets up the income base registry, [[NL-BRI]]: Article
21 defines a basisregistratie as a collection of data that a law provides
contains authentic data, and Article 21a states that there is a base registry
of income. The rest of the act is out of scope here.

This is why it was not created with the other register statutes: the
earlier rule was not to give a general act its own entity to carry a single
chapter. Roadmap #458 lifted that for the one case where the base registry has
no other statute behind it, and [[NL-KADASTERWET]] and [[NL-WET-WOZ]], which
are also general acts, already had entities.

## What was not read

The Staatsblad citation of the 1959 act and the date Hoofdstuk IVA entered into
force. [[NL-BRI]] carries a start date of 2009-01-01 from its own sources; this
entity does not repeat it.

## Relationships

- `applies-in` NL (anchor edge).

Inbound: [[NL-BRI]] is `governed-by` this entity.
