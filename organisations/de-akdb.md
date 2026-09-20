---
id: DE-AKDB
type: organisation
name: Anstalt für Kommunale Datenverarbeitung in Bayern
alternative_names:
  - AKDB
description: >
  Bavarian municipal IT service provider, an Anstalt des öffentlichen
  Rechts (public-law institution) whose Träger (sponsoring bodies) are
  Bavaria's three municipal peak associations — the Bayerischer
  Landkreistag, Bayerischer Städtetag and Bayerischer Gemeindetag —
  rather than the Bavarian state government itself. Founded at a
  founding assembly on 12 May 1971 in Munich following the associations'
  decision of 2 April 1971, with operations commencing 1 October 1971.
  It supplies software, IT products and digitalisation services across
  the core functions of Bavarian municipal administration — finance,
  personnel, resident registration, building and property management —
  and operates as a knowledge centre for consulting, support, sales and
  training for municipalities.

level: subnational
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1971-05-12
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Confirmed by reading AKDB's own 'Historie' page directly (2026-09-20): the Bavarian municipal peak associations decided on 2 April 1971 to found an 'Anstalt für Kommunale Datenverarbeitung in Bayern,' held a founding assembly on 12 May 1971 in Munich, and commenced operations on 1 October 1971. The three Träger are named directly on that page as the Bayerischer Landkreistag, Bayerischer Städtetag and Bayerischer Gemeindetag — Bavaria's municipal associations, not the Land government itself, though AKDB holds the legal form of a public-law institution (Anstalt des öffentlichen Rechts) headquartered in Munich. Anchor edge under metadata/relationship-types.md §2.3, asserting Bavarian sub-federal scope via `level: subnational`; `confidence: medium` reflects that the Träger are municipal associations rather than the state itself, a nuance the anchor-edge rule does not have a sharper category for."
    confidence: medium
    valid_from: 1971-05-12
    valid_until: null

sources:
  - title: "Historie — AKDB"
    url: "https://www.akdb.de/ueber-die-akdb/historie/"
    publisher: "Anstalt für Kommunale Datenverarbeitung in Bayern (AKDB)"
    accessed: "2026-09-20"
  - title: "Anstalt für Kommunale Datenverarbeitung in Bayern — Wikipedia"
    url: "https://de.wikipedia.org/wiki/Anstalt_f%C3%BCr_Kommunale_Datenverarbeitung_in_Bayern"
    publisher: "Wikipedia (German)"
    accessed: "2026-09-20"
---

# AKDB — Anstalt für Kommunale Datenverarbeitung in Bayern

> **Created 2026-09-20**, closing part of `discovery/unresolved.md` item
> #5 alongside [[DE-DATAPORT]]. Sourced from AKDB's own "Historie" page,
> read directly, and corroborated by German Wikipedia.

## Description

AKDB is Bavaria's municipal IT service provider, founded as a
**public-law institution (Anstalt des öffentlichen Rechts)** at a founding
assembly on **12 May 1971** in Munich, following the Bavarian municipal
peak associations' decision on **2 April 1971** to create it. Operations
began **1 October 1971**.

## Municipality-owned, not state-owned

AKDB's own page names its Träger directly: the **Bayerischer
Landkreistag** (district association), **Bayerischer Städtetag** (cities
association) and **Bayerischer Gemeindetag** (communities association) —
Bavaria's three municipal peak associations, not the Land government
itself. This is a genuinely different ownership shape from
[[BE-DIGITAAL-VLAANDEREN]] (a Flemish government agency) and
[[BE-PARADIGM]] (a Brussels regional body): AKDB is a public-law
institution owned by municipalities collectively, for municipalities,
across an entire Land. `confidence: medium` on its `part-of` edge to
[[DE]] reflects that nuance — the anchor-edge rule's binary "part of the
state" / "not part of the state" test does not cleanly capture a body
that is public-law in form but municipally rather than state-owned.

## What it does

Confirmed directly: AKDB supplies **software, IT products and
digitalisation services** across the core functions of municipal
administration — finance and personnel, resident registration
(Einwohnermeldewesen), building and property management, and the
"Kommunales Steuerungsmodell." It describes itself as a knowledge centre
for consulting, support, sales and training.

## Not modelled

- AKDB's specific software products and IT platforms individually.
- Any relationship to [[DE-DATAPORT]] or other German multi-Land IT
  providers — no source read connects them.

## Relationships

- `part-of` [[DE]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
