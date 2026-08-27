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
verification: primary-source

start_date: 2018-01-01
end_date: null
last_verified: "2026-08-27"
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
  - type: aligned-with
    target: INTL-IDS-RAM
    source: fact
    evidence: "CORRECTED this pass. Confirmed by reading internationaldataspaces.org's own article directly (2026-08-27): the relationship is a collaboration between two distinct, separately-governed frameworks, not an incorporation of iSHARE into the IDS-RAM as the entity previously stated. The article's own words: 'IDSA reference architecture model for data spaces and iSHARE as trust framework for data spaces complete each other,' and specific iSHARE components ('iSHARE satellites combined with the iSHARE standards-based authorization registry role') 'are based on IDSA's RAM.' IDSA and iSHARE Foundation each retain distinct roles under a 2022 collaboration agreement: IDSA covers 'the technical foundation for data spaces (IDSA Rulebook, IDS Reference Architecture Model, Dataspace Protocol, IDS Certification)' while iSHARE covers 'the Trust Framework, Trust Protocol and Governance Components.' `type` changed from `references` to `aligned-with` (two entities deliberately kept consistent without one implementing the other) as the better fit per `metadata/relationship-types.md` §2.1, since neither 'incorporation' nor a one-way 'references' matches what the source describes."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: NL-DSGO
    source: interpretation
    evidence: "Both are Dutch afsprakenstelsels governing sectoral data sharing through uniform agreements. No source read this pass or previously connects them; recorded as an Atlas observation to stop this entity sitting fully disconnected from the graph, which the Batch 6 audit flagged."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Data spaces — iSHARE"
    url: "https://ishare.eu/nl/deelnemen/data-spaces-2/"
    publisher: "iSHARE"
    accessed: "2026-08-27"
  - title: "DMI — iSHARE in data spaces"
    url: "https://ishare.eu/nl/ecosysteem/ishare-in-data-spaces/dmi/"
    publisher: "iSHARE"
    accessed: "2026-08-27"
  - title: "Afsprakenstelsel iSHARE: hoe zit dat juridisch in elkaar?"
    url: "https://www.sva.nl/blog/weg-wagen-6/afsprakenstelsel-ishare-hoe-zit-dat-juridisch-in-elkaar-128"
    publisher: "SVA"
    accessed: "2026-08-27"
  - title: "IDSA and iSHARE Foundation intensify collaboration to speed up industrial adoption of data spaces"
    url: "https://internationaldataspaces.org/idsa-and-ishare-foundation-intensify-collaboration-to-speed-up-industrial-adoption-of-data-spaces/"
    publisher: "International Data Spaces Association (IDSA)"
    accessed: "2026-08-27"
---

# iSHARE

> **Verified 2026-08-27, one relationship corrected.** All three originally
> cited pages were read directly, none of which mention IDSA or
> INTL-IDS-RAM by name. A fourth source — IDSA's own article — was read
> directly to check the `references` relationship the entity carried, and
> found it materially mischaracterised: the sources describe a
> **collaboration between two separately-governed frameworks**, not IDSA
> "incorporating" iSHARE. The relationship `type` is corrected to
> `aligned-with` and its evidence rewritten. `verification` moves from
> `search-only` to `primary-source`.

## Description

iSHARE is an agreement system (afsprakenstelsel) and trust framework for
data sharing, introduced in 2018 as an initiative of Topsector Logistiek.
None of the three pages read directly this pass mention Topsector Logistiek
by name; that origin claim is carried over from the prior text rather than
independently re-confirmed. Its purpose, confirmed by reading sva.nl
directly, is "a system of agreements" establishing uniform rules across
parties sharing data — standardised protocols for identification,
authentication and authorisation in place of bilateral contracts.

Its design goal is a specific and unusual one: enabling parties to share
data with **counterparties they do not know**, while retaining control over
the data and over access to it. Confirmed by reading sva.nl directly:
iSHARE "stimulates trust and control" and lets participants gain "a
reusable and trusted (e)identity to log in" across the network, with
authorisations that can be modified as needed.

iSHARE is used to establish data spaces. Confirmed by reading ishare.eu
directly: the DMI ecosystem "works as a federated data space, using the
iSHARE Trust Framework," with iSHARE providing "a robust mechanism for
determining data access rights." **The claim that "the IDSA has
incorporated the iSHARE agreement system into the IDS architecture" is
corrected this pass** — see below.

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

- `aligned-with` [[INTL-IDS-RAM]] — **corrected this pass**. IDSA's own
  article, read directly, describes a 2022 collaboration in which "IDSA
  reference architecture model for data spaces and iSHARE as trust
  framework for data spaces complete each other" — two separately-governed
  frameworks kept deliberately consistent, each retaining distinct roles
  (IDSA: reference architecture, rulebook, certification; iSHARE: trust
  framework, trust protocol, governance components). The prior text's
  claim that "the IDSA has incorporated iSHARE into the IDS architecture"
  overstated a collaboration as an absorption, and `type` is corrected
  from `references` to `aligned-with` accordingly.

Topsector Logistiek and the DMI ecosystem are named in sources but neither
is an Atlas entity yet; both are queued in `discovery/research-queue.md`.
[[INTL-IDSA]] is now a proper Atlas entity and the relationship above
connects to its reference architecture, closing the gap queued since
Batch 5 — with a corrected, rather than merely confirmed, characterisation.

The **Batch 6 audit found this entity fully disconnected** before that
gap closed — no inbound or outbound edges at all, the only such case in the
Netherlands layer. That is a defect in a knowledge graph even when every
individual omission was justified: an entity nothing reaches is effectively
invisible.

The additional fix from that audit is an explicit `related-to` [[NL-DSGO]]
marked `source: interpretation` at `confidence: low`. Both are Dutch
afsprakenstelsels governing sectoral data sharing through uniform
agreements — the same family observation already recorded on
[[EU-DSSC-BLUEPRINT]]. It is an Atlas reading, not a sourced link, and it is
labelled as one.

## Sources

Listed in frontmatter, all four read directly this pass. Note the third
(sva.nl) is a law-firm blog — a secondary source, low in the README's
preference order.
