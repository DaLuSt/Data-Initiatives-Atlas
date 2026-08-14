---
id: NL-FDS
type: framework
name: Federatief Datastelsel
alternative_names:
  - FDS
  - Afsprakenstelsel Federatief Datastelsel
description: >
  Dutch agreement system (afsprakenstelsel) enabling organisations with a
  public task to share and use data simply and responsibly. It focuses on
  standardisation and uniformity in how data is described and shared across
  domains, so that high-quality data from different sources can be found,
  shared and applied coherently for multiple uses.

level: national
country: NL
region: null

status: planned
confidence: low
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-IBDS
relationships:
  - type: implements
    target: NL-IBDS
    source: interpretation
    evidence: "Search results consistently present the FDS as the agreement system arising from the IBDS, but the formal relationship has not been read from an authoritative source."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Interbestuurlijke Datastrategie (IBDS) — Federatief Datastelsel (presentatie, Dag van de Interoperabiliteit)"
    url: "https://www.forumstandaardisatie.nl/sites/default/files/BFS/8-Bijeenkomsten/20241015-Dag-van-de-interoperabiliteit/presentaties/Presentatie-Federatief-Datastelsel-en-resultaten-Mentimeter.pdf"
    publisher: "Forum Standaardisatie"
  - title: "Interbestuurlijke Datastrategie (IBDS)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/data/interbestuurlijke-datastrategie/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
---

# Federatief Datastelsel (FDS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Federatief Datastelsel is an agreement system (afsprakenstelsel) for
organisations carrying out a public task, intended to make it possible for
them to share and use each other's data simply and responsibly. Rather than
centralising data, it is federative: it standardises *how* data is described
and exchanged across domains, so that high-quality data held in different
source systems can be found, shared and applied coherently for multiple
purposes.

`status: planned` is a deliberately conservative reading. Search results
asserted that the OBDO established the *Afsprakenstelsel Federatief
Datastelsel* in February 2026, which — if accurate — would justify a status
of `active` or `implemented`. That is a recent, specific and consequential
governance claim, and it has not been verified against a primary source. It
is recorded as an open question in `discovery/unresolved.md`; the status
should be revisited as the first item of any re-verification pass.

The typing of FDS as `framework` rather than `initiative` or `programme` is
an Atlas judgement based on its self-description as an *afsprakenstelsel* —
a body of agreements and standards — rather than a time-bound delivery
vehicle. This is flagged for review in `discovery/unresolved.md`.

## Relationships

- Implements / realises [[NL-IBDS]] (Atlas interpretation, unconfirmed).
- Sits within the [[NL-BZK]] digital-government policy remit.
- Governance decisions taken via the [[NL-OBDO]] (unconfirmed).

## Atlas interpretation

Both the FDS→IBDS relationship and the choice of `framework` as its entity
type are Atlas interpretations, not sourced facts.

## Sources

Listed in frontmatter.
