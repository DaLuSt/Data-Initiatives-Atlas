---
id: LU
type: country
name: Luxembourg
alternative_names:
  - Grand Duchy of Luxembourg
  - Grand-Duché de Luxembourg
  - Lëtzebuerg
description: >
  Country anchor entity for Luxembourg, the twelfth national scope covered by
  the Data Initiatives Atlas and its tenth European Union member state. It is
  the smallest country in the Atlas by population and, through ILNAS, one of
  only two whose standards body belongs to all five European and
  international standardisation organisations the Atlas holds.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources:
  - title: "LU — Luxembourg (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:LU"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Government IT Centre — CTIE"
    url: "https://ctie.gouvernement.lu/en.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
  - title: "ISO — ILNAS"
    url: "https://www.iso.org/member/1776.html"
    publisher: "International Organization for Standardization (ISO)"
---

# Luxembourg

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Luxembourg (ISO 3166-1 alpha-2: **`LU`**) is the **twelfth country** in the
Atlas and its **tenth EU member state**.

## The smallest country, and the case against reading size into the graph

Luxembourg is by a wide margin the smallest country the Atlas holds. It is
also, through [[LU-ILNAS]], one of **only two** countries whose national
standards body belongs to all five standardisation organisations the Atlas
holds — [[INTL-ISO]], [[INTL-IEC]], [[EU-CEN]], [[EU-CENELEC]] and
[[EU-ETSI]].

The other is the **United Kingdom**, through [[GB-BSI]], which the Atlas
records as "the most connective UK entity".

A reader inferring institutional reach from population would get that
backwards. Luxembourg matches the UK on standards connectivity and beats
eight larger member states, several of which have no standards body in the
Atlas at all.

## One body does three jobs

[[LU-ILNAS]] is the **normalisation, accreditation and product-safety**
authority in one institute. Everywhere else in the Atlas these functions sit
in separate bodies, and mostly the Atlas holds only the standardisation one.
Small-state administration concentrates functions that larger states split,
and Luxembourg is where that shows.

## EU instruments that apply in Luxembourg

Recorded as `applies-in` edges on the instruments themselves. See
`countries/lu/index.md`.

## Not modelled

- **Luxembourg's role as an EU institutional seat.** The Court of Justice,
  the Court of Auditors, the EIB and the **Publications Office of the
  European Union** are based there. The Publications Office is an Atlas
  entity ([[EU-PUBLICATIONS-OFFICE]]) and **carries no relationship to
  [[LU]]** — being headquartered in a member state is not a relationship the
  Atlas models, and treating it as one would make every host state look like
  a participant in what it hosts.
- **LuxProvide** and the **MeluXina** supercomputer, Luxembourg's EuroHPC
  presence.
- The **financial sector** and the CSSF, which dominate Luxembourg's data
  economy and are outside the Atlas's public-sector scope.

## Sources

Listed in frontmatter.
