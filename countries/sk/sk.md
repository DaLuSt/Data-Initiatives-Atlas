---
id: SK
type: country
name: Slovakia
alternative_names:
  - Slovak Republic
  - Slovensko
  - Slovenská republika
description: >
  Country anchor entity for Slovakia, a member state of the European Union
  since 1 May 2004. It is a base anchor: it carries the country's position
  in the European legal and institutional frameworks so that entities
  scoped to it have somewhere to attach, and no national entities are
  modelled yet.

level: national
country: SK
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
    evidence: "Slovakia is one of the 27 member states of the European Union, having acceded on 1 May 2004; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SK — Slovakia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:SK"
    publisher: "International Organization for Standardization (ISO)"
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Timeline — Joining the euro area"
    url: "https://www.consilium.europa.eu/en/policies/join-the-euro-area/timeline-joining-the-euro-area/"
    publisher: "Council of the European Union"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Slovakia

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Slovakia (ISO 3166-1 alpha-2: **`SK`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No
Slovakia entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1 May 2004** |
| Euro area | Since **1 January 2009** |
| Schengen area | Member |
| Council of Europe | Member since 1993 |
| EEA | Through EU membership |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## One half of a dissolution

Slovakia and [[CZ]] both joined [[INTL-COE]] in 1993 and the EU in
2004, having been one state until 1 January 1993.

Slovakia adopted the euro in 2009; Czechia has not. The Atlas holds a Czech
national layer and nothing Slovak, so the pair is currently asymmetric in the
graph in a way the history does not warrant.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

No EU instrument in the Atlas carries `applies-in` → [[SK]] yet.
That is a gap rather than a finding: as a member state, every
directly applicable EU regulation the Atlas holds does apply here.

## Sources

Listed in frontmatter.
