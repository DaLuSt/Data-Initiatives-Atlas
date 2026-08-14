---
id: NL-BASISREGISTRATIES
type: framework
name: Stelsel van Basisregistraties
alternative_names:
  - Stelsel van basisregistraties
  - System of Base Registries
description: >
  The Dutch system of base registries: ten designated national registrations
  plus supporting system services, established so that core data of each
  kind is collected and managed in one authoritative place and reused across
  government rather than re-collected.

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
organisations:
  - NL-BZK
related_entities:
  - NL-KADASTER
  - NL-KVK
  - NL-RDW
  - NL-WET-BRP
relationships:
  - type: governed-by
    target: NL-WET-BRP
    source: fact
    evidence: "The Wet BRP governs the Basisregistratie Personen, one of the registrations within the stelsel (rvig.nl; digitaleoverheid.nl BRP page). This governs one registration, not the stelsel as a whole. NOT READ — search-only."
    confidence: low
    valid_from: 2014-01-06
    valid_until: null

sources:
  - title: "10 basisregistraties — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistraties — Kadaster"
    url: "https://www.kadaster.nl/zakelijk/registraties/basisregistraties"
    publisher: "Kadaster"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
---

# Stelsel van Basisregistraties

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Stelsel van Basisregistraties is the Dutch system of base registries.
Ten designated basisregistraties, together with a set of supporting system
services, form the stelsel. The organising principle is single-point
collection and management: central government decided to introduce the
system so that the core data of each type is collected and maintained in one
authoritative place, then reused across government rather than repeatedly
re-collected.

Registrations named in Batch 2 research include the BRK (Basisregistratie
Kadaster, held by [[NL-KADASTER]]), the BAG (Basisregistratie Adressen en
Gebouwen), the Handelsregister (held by [[NL-KVK]]), the BRV
(Basisregistratie Voertuigen, held by [[NL-RDW]] since 1 July 2008) and the
BRP (Basisregistratie Personen). The registrations cross-reference one
another — the Kadaster relates the BRK to the BAG, the Handelsregister and
the BRP.

`coverage: low`: the individual registrations are not yet Atlas entities,
and the full list of ten has not been enumerated from a source. The
governance of the stelsel as a whole — who owns it, and how it relates to
[[NL-FDS]], which addresses overlapping federated-data-sharing ground — has
not been established and is recorded in `discovery/unresolved.md`.

## Scope note

This is a `framework`, not an organisation, and so sits outside Batch 2's
nominal scope. It was added here because without it the register-holding
organisations added in this batch would be disconnected nodes: it is the
structure that makes [[NL-KADASTER]], [[NL-KVK]] and [[NL-RDW]] cohere as
part of one data system rather than three unrelated agencies.

## Relationships

- Registrations held by [[NL-KADASTER]], [[NL-KVK]] and [[NL-RDW]].
- [[NL-WET-BRP]] governs the BRP registration within the stelsel. Note this
  relationship is recorded at `confidence: low`: the Wet BRP governs *one*
  registration, not the stelsel as a whole, and each registration has its
  own statutory basis. Once the individual registrations become entities,
  this link should move down to the BRP entity.
- Policy responsibility within [[NL-BZK]]'s digital-government remit
  (asserted by the digitaleoverheid.nl placement of the topic, not by a
  read source).

## Sources

Listed in frontmatter.
