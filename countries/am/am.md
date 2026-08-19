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
  - type: part-of
    target: INTL-COE
    source: fact
    evidence: "Armenia is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union (coe.int 'The Council of Europe's 46 member states'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "AM — Armenia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:AM"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Armenia

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

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
| Council of Europe | Member since 2001 |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

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

Listed in frontmatter.
