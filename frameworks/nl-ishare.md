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
related_entities: []
relationships: []

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

None asserted. Topsector Logistiek, the DMI ecosystem and the IDSA are all
named in sources but none is an Atlas entity yet; all are queued in
`discovery/research-queue.md`. Asserting relationships to entities that do
not exist is not possible, and inventing approximations for them would be
worse than the gap.

## Sources

Listed in frontmatter. Note the third is a law-firm blog — a secondary
source, low in the README's preference order.
