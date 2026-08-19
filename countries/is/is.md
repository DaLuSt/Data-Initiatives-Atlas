---
id: IS
type: country
name: Iceland
alternative_names:
  - Iceland
  - Ísland
  - Lýðveldið Ísland
description: >
  Country anchor entity for Iceland, a member of the European Free Trade
  Association and a party to the Agreement on the European Economic Area,
  and not a member of the European Union. It is a base anchor: it carries
  the country's position in the European legal and institutional
  frameworks so that entities scoped to it have somewhere to attach, and
  no national entities are modelled yet.

level: national
country: IS
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
    evidence: "Iceland is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union (coe.int 'The Council of Europe's 46 member states'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "IS — Iceland (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:IS"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "The European Free Trade Association"
    url: "https://www.efta.int/about-efta/european-free-trade-association"
    publisher: "European Free Trade Association (EFTA)"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Iceland

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Iceland (ISO 3166-1 alpha-2: **`IS`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Iceland
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | Member |
| Council of Europe | Member since 1950 |
| EFTA / EEA | Member of [[INTL-EFTA]]; party to [[INTL-EEA-AGREEMENT]] |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## The second EEA EFTA state in the Atlas

Iceland is a party to [[INTL-EEA-AGREEMENT]] and a member of
[[INTL-EFTA]], not of the European Union — the same position as [[NO]], and
described at length on that entity.

EU acts do not apply in Iceland by force of Union law. They take effect only
once incorporated into the EEA Agreement by a decision of the **EEA Joint
Committee** and then implemented in Icelandic law, which is why no
`applies-in` edge from an EU instrument points here.

Iceland, [[LI]] and [[NO]] are the three **EEA EFTA states**; [[CH]] is the
fourth EFTA member and is in neither the EU nor the EEA.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter.
