---
id: DK
type: country
name: Denmark
alternative_names:
  - Kingdom of Denmark
  - Danmark
  - Kongeriget Danmark
description: >
  Country anchor entity for Denmark, a member state of the European Union
  since 1 January 1973. It is a base anchor: it carries the country's
  position in the European legal and institutional frameworks so that
  entities scoped to it have somewhere to attach, and no national entities
  are modelled yet.

level: national
country: DK
region: EU

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
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Denmark is one of the 27 member states of the European Union, having acceded on 1 January 1973; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "DK — Denmark (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:DK"
    publisher: "International Organization for Standardization (ISO)"
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Denmark

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Denmark (ISO 3166-1 alpha-2: **`DK`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Denmark
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1 January 1973** |
| Euro area | No |
| Schengen area | Member |
| Council of Europe | Member since 1949 |
| EEA | Through EU membership |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## Opt-outs, and a founding member of the Council of Europe

Denmark holds a **Treaty opt-out from the euro** — one of only two
ever granted, and the only one still in force since the United Kingdom left.
It is therefore an EU member state that will not adopt the single currency
without a further decision, unlike [[SE]], [[PL]], [[CZ]], [[HU]] and [[RO]],
which are obliged to join once they meet the criteria.

Denmark is one of the **ten founding members of [[INTL-COE]]** in 1949.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

No EU instrument in the Atlas carries `applies-in` → [[DK]] yet.
That is a gap rather than a finding: as a member state, every
directly applicable EU regulation the Atlas holds does apply here.

## Sources

Listed in frontmatter.
