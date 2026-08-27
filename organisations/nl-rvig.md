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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    accessed: "2026-08-27"
  - title: "Toelichting — Koppeling BAG-BRP"
    url: "https://www.rvig.nl/bag-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
  - title: "Koppeling BAG-GBA-BRP"
    url: "https://www.rvig.nl/hup/koppeling-bag-gba-brp"
    publisher: "Rijksdienst voor Identiteitsgegevens (RvIG)"
    accessed: "2026-08-27"
  - title: "Basisregistratie Personen (BRP) — Stelsel van basisregistraties"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/stelsel-van-basisregistraties/10-basisregistraties/brp/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
---

# RvIG — Rijksdienst voor Identiteitsgegevens

> **Verified 2026-08-27.** All four cited pages read directly. The
> BAG–BRP coupling is confirmed to have hardened into a mandatory,
> ongoing requirement since January 2024 — not just the one-time technical
> link the entity's prior text implied — with a monthly compliance report
> (Kwaliteitsmonitor) for municipalities.

## Description

RvIG is the Dutch agency for the system of identity data. Within the
`stelsel van basisregistraties` it is responsible for the **secure storage
and exchange** of the personal data held in [[NL-BRP]].

It also publishes the guidance describing how the BRP couples to other
registers — notably the **BAG–BRP coupling**, through which municipal
address data from [[NL-BAG]] reaches the population register. That coupling
is one of the clearest documented examples of the stelsel working as a
system rather than as ten separate databases. Reading both of RvIG's own
coupling pages directly this pass shows it happened in two stages: a
one-time technical link in 2011–2012, and a **mandatory, ongoing**
requirement in force since January 2024 that bans point addresses, location
descriptions and reference addresses outright and is monitored through a
monthly Kwaliteitsmonitor (KWM) report to municipalities.

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

Listed in frontmatter, all four read directly this pass — RvIG's own BRP
page and both its coupling-guidance pages, plus the digitaleoverheid.nl BRP
page.
