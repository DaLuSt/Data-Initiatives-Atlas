---
id: ES-LOCALRET
type: organisation
name: Consorci Localret
alternative_names:
  - Localret
description: >
  Consortium formed in 1997 by Catalonia's two municipalist
  associations — the Federació de Municipis de Catalunya (FMC) and the
  Associació Catalana de Municipis i Comarques (ACM) — to foster the
  development of telecommunications networks and services and the
  application of ICT to improve local government action in Catalonia.
  At its founding it integrated 784 municipalities, representing 99% of
  Catalonia's population. Headquartered in Barcelona, it represented
  Catalan local governments in the 2001-2002 pact and resolution that
  created the AOC Consortium, alongside the Generalitat de Catalunya.

level: subnational
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1997-01-01
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES-AOC
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Closes a gap ES-AOC's own file had flagged ('Localret ... not independently researched') -- graph completion, not a numbered discovery/unresolved.md row. Confirmed by reading localret.cat's own 'Who We Are' page directly (2026-09-26): 'the local consortium formed by the local administrations of Catalonia to support municipalities in their digital transformation,' headquartered in Barcelona. ca.wikipedia.org's own 'Localret' article, also read directly, independently gives the 1997 founding year, names FMC and ACM as founders, states it integrated 784 municipalities (99% of Catalonia's population) at founding, and confirms it co-founded the AOC Consortium in 2002 -- matching ES-AOC's own already-sourced account of Localret representing local governments in the 2001 pact. Anchor edge under metadata/relationship-types.md §2.3, asserting Catalan sub-federal scope via `level: subnational`, matching ES-AOC's own treatment."
    confidence: medium
    valid_from: "1997-01-01"
    valid_until: null
  - type: participates-in
    target: ES-AOC
    source: fact
    evidence: "Confirmed on both ES-AOC's own page (aoc.cat, already cited on ES-AOC) and ca.wikipedia.org's Localret article, both stating Localret represented local governments in the 23 July 2001 pact and 27 March 2002 resolution that created the AOC Consortium -- Localret co-founded AOC, it does not merely relate to it."
    confidence: high
    valid_from: "2002-03-27"
    valid_until: null

sources:
  - title: "Who We Are — Localret"
    url: "https://www.localret.cat/en/qui-som/"
    publisher: "Consorci Localret"
    accessed: "2026-09-26"
  - title: "Localret"
    url: "https://ca.wikipedia.org/wiki/Localret"
    publisher: "Viquipèdia (Catalan Wikipedia)"
    accessed: "2026-09-26"
---

# Consorci Localret

> **Created 2026-09-26**, closing a gap [[ES-AOC]]'s own file had
> flagged (graph completion, not a numbered `discovery/unresolved.md`
> row). Sourced from Localret's own official page and its Catalan
> Wikipedia article, both read directly.

## Description

Localret is a **consortium** formed in **1997** by Catalonia's two
municipalist associations — the **Federació de Municipis de Catalunya
(FMC)** and the **Associació Catalana de Municipis i Comarques (ACM)** —
to foster telecommunications and ICT development for local government in
Catalonia. Confirmed on its own official page: it exists "to support
municipalities in their digital transformation." Confirmed independently
on Catalan Wikipedia: at founding it integrated **784 municipalities**,
representing **99%** of Catalonia's population.

## Co-founder of [[ES-AOC]]

[[ES-AOC]]'s own file already records that its creation traces to a
**23 July 2001 pact** in the Parliament of Catalonia and a **27 March
2002 resolution**, with local governments represented by Localret
alongside the Generalitat de Catalunya. This entity's own sources
independently confirm the same account from Localret's side —
Localret **co-founded** AOC, recorded here as `participates-in` rather
than a looser association.

## Not modelled

- The **Federació de Municipis de Catalunya (FMC)** and **Associació
  Catalana de Municipis i Comarques (ACM)**, Localret's own founding
  associations — not independently researched this pass.
- The **Fundació Observatori per a la Societat de la Informació de
  Catalunya**, which Localret co-founded with the Open University of
  Catalonia and the Generalitat — not independently researched.

## Relationships

- `part-of` [[ES]] (anchor edge, `level: subnational`).
- `participates-in` [[ES-AOC]] — `confidence: high`, co-founder.

## Sources

Listed in frontmatter, both read directly.
