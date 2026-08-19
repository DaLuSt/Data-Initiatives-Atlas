---
id: VA
type: country
name: Holy See
alternative_names:
  - Holy See (Vatican City State)
  - Santa Sede
  - Stato della Città del Vaticano
description: >
  Country anchor entity for Holy See. It is a base anchor: it carries the
  country's position in the European legal and institutional frameworks so
  that entities scoped to it have somewhere to attach, and no national
  entities are modelled yet.

level: national
country: VA
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-19"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-COE
relationships:
  - type: related-to
    target: INTL-COE
    source: fact
    evidence: "The Holy See holds observer status with the Council of Europe rather than membership; it does not appear among the organisation's 46 member states (coe.int portal '46 member states'). NOT READ — search-only. Anchor edge recording observer status, not membership."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "VA — Holy See (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:VA"
    publisher: "International Organization for Standardization (ISO)"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Holy See

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Holy See (ISO 3166-1 alpha-2: **`VA`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Holy
See entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | No |
| Council of Europe | **Observer state**, not a member |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## An observer, not a member, of almost everything

The Holy See is a **Council of Europe observer state**, not a
member, and a **UN observer state**, not a member — one of only two, with the
State of Palestine.

It uses the **euro under a monetary agreement** with the EU, like [[AD]],
[[MC]] and [[SM]], and mints its own euro coins.

Its anchor edge is `related-to` [[INTL-COE]], recording observer status.
Vatican City is an enclave within [[IT]] and the smallest state in the world
by both area and population.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter.
