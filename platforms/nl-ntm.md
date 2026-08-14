---
id: NL-NTM
type: platform
name: Nationaal Toegangspunt Mobiliteitsdata
alternative_names:
  - NTM
  - National Access Point for Mobility Data
description: >
  The Netherlands' national access point for mobility data, operating within
  the NDW. Every European country is obliged to have a national access
  point; the NTM is the Dutch one, bringing mobility data together at a
  single central point for all involved parties.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - NL-NDW
relationships:
  - type: part-of
    target: NL-NDW
    source: fact
    evidence: "The NDW was expanded with the Nationaal Wegenbestand and the Nationaal Toegangspunt Mobiliteitsdata; all that data comes together in one central access point, the NTM (ndw.nu; ntm.ndw.nu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Nationaal Toegangspunt Mobiliteitsdata — standaarden"
    url: "https://ntm.ndw.nu/standaarden"
    publisher: "Nationaal Dataportaal Wegverkeer (NDW)"
  - title: "Nationaal Dataportaal Wegverkeer"
    url: "https://nl.wikipedia.org/wiki/Nationaal_Dataportaal_Wegverkeer"
    publisher: "Wikipedia"
---

# NTM (Nationaal Toegangspunt Mobiliteitsdata)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The NTM is the Netherlands' national access point for mobility data. All
mobility data gathered through [[NL-NDW]] ultimately comes together at this
single central access point for all involved parties.

## An EU obligation without an EU entity yet

The NTM exists because **every European country is obliged to have a
national access point** — the Dutch one is the NTM. This is a textbook
instance of the EU→national chain the Atlas is built to show, and it is the
reason `region: EU` is set on a national entity here.

The obligation is understood to derive from EU intelligent transport
systems (ITS) legislation, but **no source located in this batch named the
instrument**, so no `implements-requirement-from` relationship is asserted —
only the `region: EU` marker and this note. Identifying the instrument and
completing the chain is queued in `discovery/research-queue.md` for Batch 8.

Recording the obligation's existence while refusing to name its source is
the honest position: the fact that an EU requirement exists is sourced;
which instrument imposes it is not.

## Relationships

- Part of [[NL-NDW]].
- Awaiting an `implements-requirement-from` link to the EU ITS instrument
  (Batch 8).

## Sources

Listed in frontmatter.
