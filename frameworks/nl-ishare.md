---
id: NL-ISHARE
type: framework
name: iSHARE
alternative_names:
  - iSHARE Trust Framework
  - Afsprakenstelsel iSHARE
description: >
  Agreement system and trust framework for data sharing, introduced in 2018
  as an initiative of Topsector Logistiek. It establishes uniform agreements
  on identification, authentication and authorisation so that parties can
  share data with counterparties they do not know, while retaining control
  over the data and access to it.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2018-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-IDS-RAM
  - INTL-IDSA
  - NL-FDS
  - NL-DSGO
relationships:
  - type: references
    target: INTL-IDS-RAM
    source: fact
    evidence: "iSHARE records the International Data Spaces Association incorporating iSHARE into the IDS Reference Architecture Model, the conceptual basis of IDS-compliant data exchange between organisations (internationaldataspaces.org 'IDS Reference Architecture Model'; ishare.eu; the IDSA reference already recorded on this entity). NOT READ — search-only. `references` and not `based-on`: the direction the sources describe is the IDSA incorporating iSHARE, not iSHARE deriving from the IDS-RAM. This closes a gap queued in discovery/research-queue.md since Batch 5."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: NL-DSGO
    source: interpretation
    evidence: "Both are Dutch afsprakenstelsels governing sectoral data sharing through uniform agreements. No source connects them; recorded as an Atlas observation to stop this entity sitting fully disconnected from the graph, which the Batch 6 audit flagged."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Data spaces — iSHARE"
    url: "https://ishare.eu/nl/deelnemen/data-spaces-2/"
    publisher: "iSHARE"
  - title: "DMI — iSHARE in data spaces"
    url: "https://ishare.eu/nl/ecosysteem/ishare-in-data-spaces/dmi/"
    publisher: "iSHARE"
  - title: "Afsprakenstelsel iSHARE: hoe zit dat juridisch in elkaar?"
    url: "https://www.sva.nl/blog/weg-wagen-6/afsprakenstelsel-ishare-hoe-zit-dat-juridisch-in-elkaar-128"
    publisher: "SVA"
---

# iSHARE

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

iSHARE is an agreement system (afsprakenstelsel) and trust framework for
data sharing, introduced in 2018 as an initiative of Topsector Logistiek.
Its purpose is uniform agreements on identification, authentication and
authorisation.

Its design goal is a specific and unusual one: enabling parties to share
data with **counterparties they do not know**, while retaining control over
the data and over access to it. Because every party joins the agreement
system in the same way and is bound by the same conditions, a controlled and
accessible environment results in which data can be exchanged safely.

iSHARE is used to establish data spaces, providing the governance, trust and
interoperability between participants that a data space requires. The DMI
ecosystem is cited as a federated data space using the iSHARE Trust
Framework, and the IDSA has incorporated the iSHARE agreement system into
the IDS architecture.

## A Dutch entity that outgrew the Netherlands

iSHARE is recorded as `country: NL` on the basis of its Dutch origin
(Topsector Logistiek), but it now presents itself at **ishare.eu** and
operates in a European data-space context. This sits awkwardly with the
country-neutral model: an initiative that began national and became
cross-border is exactly the case the `country` field handles least well.

The current recording is provisional and flagged in
`discovery/unresolved.md`. If iSHARE is now genuinely governed at European
level it may warrant `country: null` with `region: EU`, or a successor
entity. That should be settled in Batch 10, when European data spaces are
researched, rather than guessed now.

`start_date: 2018-01-01` is a **placeholder for "in 2018"**.

## Relationships

Topsector Logistiek, the DMI ecosystem and the IDSA are all named in sources
but none is an Atlas entity yet; all are queued in
`discovery/research-queue.md`.

The **Batch 6 audit found this entity fully disconnected** — no inbound or
outbound edges at all, the only such case in the Netherlands layer. That is
a defect in a knowledge graph even when every individual omission was
justified: an entity nothing reaches is effectively invisible.

The fix is an explicit `related-to` [[NL-DSGO]] marked
`source: interpretation` at `confidence: low`. Both are Dutch
afsprakenstelsels governing sectoral data sharing through uniform
agreements — the same family observation already recorded on
[[EU-DSSC-BLUEPRINT]]. It is an Atlas reading, not a sourced link, and it is
labelled as one. The alternative — leaving the entity unreachable — was
judged worse than a clearly-marked interpretation.

## Sources

Listed in frontmatter. Note the third is a law-firm blog — a secondary
source, low in the README's preference order.
