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
    evidence: "Russia was a member state of the Council of Europe from 1996 until its membership was terminated on 16 March 2022 under Article 8 of the Statute, with immediate effect (coe.int 'The Russian Federation is excluded from the Council of Europe'; commonslibrary.parliament.uk CBP-9570). NOT READ — search-only. The edge carries a closed validity interval: a membership that ended is a different fact from one that never existed."
    confidence: medium
    valid_from: 1996-02-28
    valid_until: 2022-03-16

sources:
  - title: "RU — Russia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:RU"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Russia

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

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
| Council of Europe | Member 1996 – **16 March 2022** (expelled) |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

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

Listed in frontmatter.
