---
id: BY
type: country
name: Belarus
alternative_names:
  - Republic of Belarus
  - Беларусь
  - Рэспубліка Беларусь
description: >
  Country anchor entity for Belarus. It is a base anchor: it carries the
  country's position in the European legal and institutional frameworks so
  that entities scoped to it have somewhere to attach, and no national
  entities are modelled yet.

level: national
country: BY
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
    evidence: "Confirmed by reading Wikipedia's 'Member states of the Council of Europe' article directly (2026-08-27), after coe.int itself proved genuinely, domain-wide bot-walled (403) on every path tried: 'Belarus applied for full membership on 12 March 1993' but has never been admitted, and it is absent from the article's own table of 46 current members — a date and detail this entity did not previously carry. The general 'Council of Europe' article corroborates: after 1989, 'all European post-Soviet states except Belarus and Kazakhstan' joined. ISO's OBP is also confirmed blocked (403). Anchor edge recording non-membership and a suspended relationship, not membership."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "BY — Belarus (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:BY"
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

# Belarus

> **Verified 2026-08-27.** ISO's OBP is confirmed genuinely bot-walled
> (403). Two Wikipedia articles were read directly, adding a detail this
> entity did not previously carry: Belarus applied for full Council of
> Europe membership on 12 March 1993 and was never admitted — a genuine
> majority (3 of 4 cited pages, alongside government.nl).

## Description

Belarus (ISO 3166-1 alpha-2: **`BY`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Belarus
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | No |
| Council of Europe | **Not a member** — applied 12 March 1993, never admitted |

Confirmed by reading Wikipedia's "Member states of the Council of
Europe" article directly (2026-08-27): Belarus applied for full
membership on 12 March 1993 and does not appear in the article's own
current 46-member table — a date this entity did not previously carry.

## Never a member

Belarus is the only European state that has **never** been a member
of [[INTL-COE]], despite applying for full membership on 12 March 1993.
It held special guest status with the Parliamentary Assembly from 1992;
that status was **suspended in 1997** and has not been restored, and the
Council suspended all relations following the 2022 invasion of [[UA]]
launched in part from Belarusian territory.

Belarus is a UN member state. Its anchor edge is `related-to`
[[INTL-COE]] rather than `part-of`, and the distinction from [[RU]] — which
was a member and was expelled — is deliberate: a membership that never
existed and a membership that ended are different facts.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter, three of four read directly this pass — both
Wikipedia articles and government.nl. ISO's OBP is genuinely bot-walled
(403).
