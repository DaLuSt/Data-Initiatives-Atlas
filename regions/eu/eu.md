---
id: EU
type: region
name: European Union
alternative_names:
  - EU
description: >
  Region anchor entity for the European Union, the first regional scope
  covered by the Data Initiatives Atlas. Used as the target of `region`
  fields and as the level at which EU legislation, strategies and standards
  are recorded before being connected to national implementations.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: unverified

start_date: null
end_date: null
last_verified: "2026-08-14"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "European Union — official website"
    url: "https://european-union.europa.eu/"
    publisher: "European Union"
    accessed: "2026-08-14"
---

# European Union

## Description

The European Union (region code `EU`) is the first regional scope populated
in the Data Initiatives Atlas. EU-level legislation, strategies, standards
and data spaces reference this entity via `region: EU`, and their
applicability to specific member states (starting with the Netherlands) is
expressed through `applies-in` relationships rather than duplicating each EU
entity per country (see `metadata/ontology.md` §"Country-Neutral
Architecture").

`coverage: low` is deliberate — this Batch 0 commit only establishes the
anchor node. Substantive EU content is researched starting in Batch 7 (see
`progress/backlog.md`).

## ⚠ Verification note (added in Batch 6)

`verification: unverified` — see the identical note on [[NL]]. This entity
was written in Batch 0 with a source URL composed from background knowledge
rather than confirmed by search or fetch. Surfaced by the Batch 6 audit and
recorded in `discovery/unresolved.md`.

## Relationships

The **Batch 11 audit found this anchor fully disconnected** — nothing
pointed at it and it pointed at nothing, unlike [[UN]], which the UN-system
bodies reference via `part-of`.

That was an inconsistency rather than a deliberate choice: the UN layer
modelled institutional membership and the EU layer did not. Fixed by adding
`part-of` relationships from [[EU-COMMISSION]], [[EU-PARLIAMENT]] and
[[EU-COUNCIL]].

Note the asymmetry with [[NL]] is *not* a defect and remains: `NL` is the
target of `applies-in` relationships from supra-national instruments, while
`EU` is the scope those instruments are tagged with. A country is a place
law applies in; a region here is the level law comes from.

See `regions/eu/index.md` for the curated index of EU entities, built up
batch by batch.

## Sources

Listed in frontmatter.
