---
id: NL-NHR
type: platform
name: Handelsregister
alternative_names:
  - NHR
  - Nieuw Handelsregister
  - HR
  - Dutch Business Register
description: >
  The Dutch trade register: a public register containing information about
  businesses and legal entities active in the Netherlands, held by the Kamer
  van Koophandel, and one of the ten registrations in the stelsel van
  basisregistraties. Its identifier, the KvK number, is increasingly carried
  in products of the cadastral base registry for organisations, which is one
  of the documented links between the two registers.

level: national
country: NL
region: null

status: active
confidence: medium
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
  - NL-KVK
related_entities:
  - NL-BASISREGISTRATIES
  - NL-KVK
  - NL-BRK
relationships:
  - type: part-of
    target: NL-BASISREGISTRATIES
    source: fact
    evidence: "The ten base registrations are the BRP, HR (Handelsregister), BAG, BRT, BRK, BRV, BRI, WOZ, BGT and BRO (digitaleoverheid.nl '10 basisregistraties'; data.overheid.nl; noraonline.nl 'Het huidige Stelsel van Basisregistraties'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-KVK
    source: fact
    evidence: "The handelsregister is a public register containing information about businesses and legal entities active in the Netherlands, managed by the Kamer van Koophandel (catalogus.kadaster.nl/brk 'Handelsregister'; digitaleoverheid.nl). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Handelsregister | Basisregistratie Kadaster (BRK)"
    url: "https://catalogus.kadaster.nl/brk/nl/page/Handelsregister"
    publisher: "Kadaster"
  - title: "Handelsregister (HR) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/hr/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Basisregistraties: de 10 basisregistraties"
    url: "https://data.overheid.nl/community/group/basisregistraties_10"
    publisher: "data.overheid.nl"
---

# NHR — Handelsregister

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Handelsregister is the public Dutch register of businesses and legal
entities, held by [[NL-KVK]]. It is one of the ten registrations in
[[NL-BASISREGISTRATIES]].

The **KvK number** is its identifier, and the Kadaster's own BRK catalogue
records that KvK numbers are increasingly carried in BRK products for
organisations — a concrete, sourced instance of two base registries sharing
a key.

## The one register whose statutory basis is not modelled at all

Nine of the ten registers in this batch have at least a named statute in
their description. This one does not: **no source read names the
Handelsregisterwet or gives its year**, so nothing is asserted, not even in
prose beyond this paragraph.

That is a narrower gap than it looks. The Atlas has a `governed-by` edge for
[[NL-BRP]] because [[NL-WET-BRP]] already existed as an entity from Batch 3.
For the other nine registers the statutes are named in descriptions where
sourced and **no law entity was created for any of them** — see
[[NL-BASISREGISTRATIES]] for why that was a deliberate scope limit rather
than an omission.

## Relationships

- `part-of` [[NL-BASISREGISTRATIES]].
- `maintained-by` [[NL-KVK]].

**No relationship to [[NL-BRK]] is asserted**, despite the shared KvK
number, for the reason set out on [[NL-BRP]]: the Atlas has no relationship
type for a key-sharing coupling between two registers.

## Sources

Listed in frontmatter.
