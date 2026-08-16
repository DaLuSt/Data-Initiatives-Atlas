---
id: NL-RVIG
type: organisation
name: Rijksdienst voor Identiteitsgegevens
alternative_names:
  - RvIG
  - Netherlands Identity Data Agency
description: >
  Dutch government agency responsible for the system of identity data,
  including the Basisregistratie Personen. It is responsible for the secure
  storage and exchange of the personal data the BRP holds, and publishes the
  guidance connecting the BRP to other base registries — including the
  documented coupling between the BAG and the BRP through which municipal
  address data reaches the population register.

level: national
country: NL
region: null

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
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-BRP
  - NL-BAG
  - NL-BZK
relationships: []

sources:
  - title: "Basisregistratie Personen | RvIG"
    url: "https://www.rvig.nl/basisregistratie-personen"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
  - title: "Toelichting — Koppeling BAG-BRP"
    url: "https://www.rvig.nl/bag-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
  - title: "Koppeling BAG-GBA-BRP"
    url: "https://www.rvig.nl/hup/koppeling-bag-gba-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
  - title: "Basisregistratie Personen (BRP) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brp/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
---

# RvIG — Rijksdienst voor Identiteitsgegevens

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

RvIG is the Dutch agency for the system of identity data. Within the
`stelsel van basisregistraties` it is responsible for the **secure storage
and exchange** of the personal data held in [[NL-BRP]].

It also publishes the guidance describing how the BRP couples to other
registers — notably the **BAG–BRP coupling**, through which municipal
address data from [[NL-BAG]] reaches the population register. That coupling
is one of the clearest documented examples of the stelsel working as a
system rather than as ten separate databases.

## `coverage: low`

RvIG's legal form, its position within [[NL-BZK]], its founding date and its
wider identity-document responsibilities are unrecorded. Everything here
comes from its BRP-facing pages, because the BRP is why this batch needed
it.

## Relationships

None asserted from this entity. [[NL-BRP]] carries the `maintained-by` edge
pointing here — `metadata/relationship-types.md` §2.1 defines
`maintained-by` as *"the target organisation maintains this entity"*, so it
belongs on the register.

## Sources

Listed in frontmatter.
