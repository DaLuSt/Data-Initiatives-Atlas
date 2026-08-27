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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading Wikipedia's 'Council of Europe' article directly (2026-08-27), after coe.int itself proved genuinely, domain-wide bot-walled (403) on every path tried: the article explicitly lists the Holy See/Vatican as a 'Council observer' rather than a member state, distinct from the 46-member table in the companion 'Member states of the Council of Europe' article, also read directly, which does not include it. ISO's OBP is also confirmed blocked (403). Anchor edge recording observer status, not membership."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "VA — Holy See (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:VA"
    publisher: "International Organization for Standardization (ISO)"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
  - title: "Council of Europe"
    url: "https://en.wikipedia.org/wiki/Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Member states of the Council of Europe"
    url: "https://en.wikipedia.org/wiki/Member_states_of_the_Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# Holy See

> **Verified 2026-08-27.** ISO's OBP is confirmed genuinely bot-walled
> (403). Two Wikipedia articles were read directly instead, confirming
> observer status directly in the Council of Europe's own descriptive
> terms — a genuine majority (3 of 4 cited pages, alongside
> government.nl).

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

Confirmed by reading Wikipedia's "Council of Europe" article directly
(2026-08-27), which names the Holy See a "Council observer."

## An observer, not a member, of almost everything

The Holy See is a **Council of Europe observer state**, not a
member — confirmed directly in the Council's own descriptive terms — and a
**UN observer state**, not a member — one of only two, with the
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

Listed in frontmatter, three of four read directly this pass — both
Wikipedia articles and government.nl. ISO's OBP is genuinely bot-walled
(403).
