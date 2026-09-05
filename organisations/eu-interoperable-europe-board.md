---
id: EU-INTEROPERABLE-EUROPE-BOARD
type: organisation
name: Interoperable Europe Board
alternative_names: []
description: >
  Governance body established under the Interoperable Europe Act to steer
  EU cross-border interoperability cooperation. Composed of high-level
  representatives from every member state and the European Commission,
  which chairs it and runs its Secretariat. Meets twice a year, adopts an
  annual work programme, and among other tasks is charged with shaping the
  next revision of the European Interoperability Framework (EIF).

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-INTEROPERABLE-EUROPE-ACT
  - EU-EIF
  - EU-ENISA
relationships:
  - type: governed-by
    target: EU-INTEROPERABLE-EUROPE-ACT
    source: fact
    evidence: "Confirmed by reading interoperable-europe.ec.europa.eu's own 'The Board' page directly (2026-09-05), which names the Interoperable Europe Act as its establishing legal instrument and describes its composition (member-state and Commission representatives, Commission chairing and running the Secretariat), meeting cadence (twice a year), and governance structure (a Steering Board; working groups, including a permanent one succeeding the former Expert Group on interoperability of European public services)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: influences
    target: EU-EIF
    source: fact
    evidence: "Confirmed by reading interoperable-europe.ec.europa.eu's own Board page directly (2026-09-05): the Board's tasks include work 'to shape the next European Interoperability Framework (EIF).' A WebSearch-surfaced news summary (not independently verified by direct fetch this pass) reports the Board's fourth meeting, 19 May 2026, reviewed progress on the EIF revision — consistent with, but not itself the basis for, this relationship. `influences` is used deliberately rather than a stronger governance claim: no source read states that the Board's decisions are binding on the EIF's content, only that shaping its next revision is among the Board's tasks."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The Board"
    url: "https://interoperable-europe.ec.europa.eu/collection/governance-board/board"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-09-05"
---

# Interoperable Europe Board

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged this body as needed to resolve
> the [[EU-INTEROPERABLE-EUROPE-ACT]] / [[EU-EIF]] relationship, and both
> of those entities' own files explicitly named the Board as uncreated.
> Its own governance page was read directly this pass.

## Description

The Interoperable Europe Board is the governance body the
[[EU-INTEROPERABLE-EUROPE-ACT]] establishes to steer EU cross-border
interoperability cooperation. Reading `interoperable-europe.ec.europa.eu`'s
own page directly: it brings together **high-level representatives from
every member state and the European Commission**, with the Commission
**chairing** the Board and running its **Secretariat**. Observers include
the Committee of the Regions, ENISA and the European Cybersecurity
Competence Centre.

The Board **meets twice a year** and **adopts an annual work programme**.
A **Steering Board** — the Chair, up to two elected member-state
representatives, and the current Council Trio Presidency — prepares its
agendas. The Board may set up **working groups**; the former Expert Group
on interoperability of European public services has been transformed into
one of its permanent working groups.

## The EIF/Act relationship, partially resolved

[[EU-INTEROPERABLE-EUROPE-ACT]]'s own file and [[EU-EIF]]'s own file both
explicitly flagged the same open question: how does the Act relate to the
EIF, and does the Interoperable Europe Board — reported second-hand to
adopt new EIF versions — actually do so? Reading the Board's own page
directly confirms **one piece of this directly**: among the Board's tasks
is work "to shape the next European Interoperability Framework (EIF)."

This is deliberately recorded as `influences`, not a stronger governance
or supersession claim. The page read this pass states that shaping the
EIF's next revision is one of the Board's tasks — it does not state that
the Board's adoption is what gives a new EIF version legal or normative
force, nor does it resolve whether the Interoperable Europe Act itself
supersedes, governs, or merely sits alongside the EIF as a framework. That
narrower legal question remains open and is not force-closed here.

## Relationships

- `governed-by` [[EU-INTEROPERABLE-EUROPE-ACT]] — its establishing
  instrument.
- `influences` [[EU-EIF]] — tasked with shaping the framework's next
  revision.

## Sources

Listed in frontmatter, read directly this pass.
