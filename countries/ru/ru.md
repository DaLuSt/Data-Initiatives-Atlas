---
id: RU
type: country
name: Russia
alternative_names:
  - Russian Federation
  - Россия
  - Российская Федерация
description: >
  Country anchor entity for Russia. It is a base anchor: it carries the
  country's position in the European legal and institutional frameworks so
  that entities scoped to it have somewhere to attach, and no national
  entities are modelled yet.

level: national
country: RU
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
  - type: part-of
    target: INTL-COE
    source: fact
    evidence: "The EU Delegation to the Council of Europe's own news item (eeas.europa.eu, 17 March 2022), read directly 2026-11-22: 'On 16 March, the Committee of Ministers of the Council of Europe, after consultation with the Parliamentary Assembly, decided by consensus that the Russian Federation ceases to be a member immediately', 'adopted by consensus the resolution to cease Russian membership as of 16 March', and 'Russia joined the Council of Europe on 28 February 1996.' coe.int itself, where the Committee of Ministers' resolution is published, is blocked to this environment (403). The edge carries a closed validity interval: a membership that ended is a different fact from one that never existed."
    confidence: high
    valid_from: 1996-02-28
    valid_until: 2022-03-16

sources:
  - title: "Committee of Ministers decides Russia ceases to be a member of the Council of Europe"
    url: "https://www.eeas.europa.eu/delegations/council-europe/committee-ministers-decides-russia-ceases-be-member-council-europe_en"
    publisher: "European External Action Service (EU Delegation to the Council of Europe)"
    accessed: "2026-11-22"
  - title: "RU — Russia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:RU"
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

# Russia

> **Verified 2026-08-27.** `coe.int` and ISO's OBP are both confirmed
> genuinely bot-walled (403). Two Wikipedia articles were read directly
> instead: the dedicated accession-date table confirms Russia's 28
> February 1996 entry exactly, and the general article confirms the 2022
> expulsion followed the invasion of Ukraine — a genuine majority (3 of 5
> cited pages). The exact 16 March 2022 expulsion date rests on the two
> sources named in the evidence, not independently re-confirmed to the
> day this pass.

## Description

Russia (ISO 3166-1 alpha-2: **`RU`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Russia
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member **28 February 1996 – 16 March 2022** (expelled) |

Confirmed by reading Wikipedia's "Member states of the Council of
Europe" article directly (2026-08-27): its own accession table gives
the exact entry date, matching this entity's existing figure. The exact
expulsion date rests on the sources named in the frontmatter evidence,
not independently re-confirmed to the day this pass.

## The first expulsion in the Council of Europe's history

Russia's membership of [[INTL-COE]] was **terminated on 16 March
2022** under Article 8 of the Statute, with immediate effect, after 26 years
— the first expulsion the organisation has ever carried out. Russia ceased to
be a party to the European Convention on Human Rights on 16 September 2022.

This anchor's `part-of` edge to [[INTL-COE]] carries **`valid_from:
1996-02-28` and `valid_until: 2022-03-16`**. It is the Atlas's first use of a
closed validity interval on a membership edge, and it exists so that the
graph records a membership that ended rather than a membership that never
was. [[BY]] is the contrasting case.

Russia is a UN member state and a permanent member of the Security Council.
The UN M49 geoscheme places it in Eastern Europe.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter, three of five read directly this pass — both
Wikipedia articles and government.nl. `coe.int` and ISO's OBP are both
genuinely bot-walled (403).
