---
id: NL-KVK
type: organisation
name: Kamer van Koophandel
alternative_names:
  - KVK
  - Netherlands Chamber of Commerce
description: >
  Dutch chamber of commerce. Its principal statutory task within the Atlas's
  scope is operating the Handelsregister, the national business register,
  which forms one of the base registrations in the Stelsel van
  Basisregistraties.

level: national
country: NL
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-KADASTER
relationships:
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "KVK operates the Handelsregister, referenced as a base registration cross-linked from the BRK (kadaster.nl, digitaleoverheid.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Kamer van Koophandel"
    url: "https://en.wikipedia.org/wiki/Kamer_van_Koophandel"
    publisher: "Wikipedia"
  - title: "10 basisregistraties — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
---

# Kamer van Koophandel (KVK)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The KVK is the Dutch chamber of commerce. Its relevance to the Atlas is its
statutory operation of the Handelsregister, the national business register,
which is one of the registrations within the [[NL-BASISREGISTRATIES]].
Businesses must register with the KVK, and the register is cross-referenced
from other base registrations — the Kadaster relates the BRK to the
Handelsregister, and [[NL-RDW]] vehicle registration interacts with KVK
registration status.

`confidence: low` and `coverage: low`: sourcing for this entity is
noticeably weaker than for its peers. The only general-profile source
located was a Wikipedia article, which is a secondary source and sits low in
the preference order set out in the README. The KVK's own site and the
statutory basis of the Handelsregister (Handelsregisterwet, Batch 3) both
need to be consulted; recorded in `discovery/research-queue.md`.

## Relationships

- Participates in [[NL-BASISREGISTRATIES]] as operator of the
  Handelsregister.

## Sources

Listed in frontmatter.
