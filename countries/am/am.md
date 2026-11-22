---
id: AM
type: country
name: Armenia
alternative_names:
  - Republic of Armenia
  - Հայաստան
  - Հայաստանի Հանրապետություն
description: >
  Country anchor entity for Armenia. It is a base anchor: it carries the
  country's position in the European legal and institutional frameworks so
  that entities scoped to it have somewhere to attach, and no national
  entities are modelled yet.

level: national
country: AM
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-COE
relationships:
  - type: part-of
    target: INTL-COE
    source: fact
    evidence: "The Council of Europe's own poster 'Map of the Council of Europe 46 member states' (edoc.coe.int, designed February 2024), read directly 2026-11-22 as a PDF, lists Armenia among the 46 member states. The accession date in `valid_from` (2001-01-25) is from an encyclopedia's accession table, read earlier, because the Council's own chart of signatures on coe.int cannot be read from here; it is not in the poster. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that. Replaces encyclopedia evidence for the membership itself (roadmap #767)."
    confidence: high
    valid_from: 2001-01-25
    valid_until: null

sources:
  - title: "Map of the Council of Europe 46 member states (2024)"
    url: "https://edoc.coe.int/en/map-of-the-member-states/5332-map-of-the-council-of-europe-46-member-states.html"
    publisher: "Council of Europe (edoc.coe.int)"
    accessed: "2026-11-22"
  - title: "AM — Armenia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:AM"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states (confirmed genuinely bot-walled, 403)"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
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

# Armenia

> **Verified 2026-08-27.** `coe.int` and ISO's OBP are both confirmed
> genuinely bot-walled (403) — the OBP is a JavaScript application with
> no static content to fetch. Two Wikipedia articles were read directly
> instead and independently confirm Council of Europe membership with an
> exact accession date, a genuine majority (3 of 5 cited pages).

## Description

Armenia (ISO 3166-1 alpha-2: **`AM`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Armenia
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member since **25 January 2001** |

Confirmed by reading Wikipedia's "Member states of the Council of
Europe" article directly (2026-08-27): its own accession table gives
the exact date, replacing the bare year this entity previously carried
on general reference knowledge alone.

## At the eastern edge of the definition

Armenia is a member of [[INTL-COE]] and a participant in the EU's
Eastern Partnership. The UN M49 geoscheme places it in **Western Asia**, not
Europe.

It is in the Atlas because the scope rule this batch adopted is a **union**
of four criteria rather than a geographic line — see the note on
`countries/README.md`. Recording the ambiguity is the point; drawing a
boundary and hiding it would not be.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter, three of five read directly this pass — both
Wikipedia articles and government.nl. `coe.int` and ISO's OBP are both
genuinely bot-walled (403).
