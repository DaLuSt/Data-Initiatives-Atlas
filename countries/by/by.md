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
    evidence: "Belarus is not a member state of the Council of Europe and has never been one; it held special guest status with the Parliamentary Assembly from 1992, suspended in 1997, and the Council suspended all relations with Belarus following the 2022 invasion of Ukraine (coe.int 'The Russian Federation is excluded from the Council of Europe', which records the suspension of relations with Belarus in the same decision; coe.int portal '46 member states', on which Belarus does not appear). NOT READ — search-only. Anchor edge recording non-membership and a suspended relationship, not membership."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BY — Belarus (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:BY"
    publisher: "International Organization for Standardization (ISO)"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Belarus

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

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
| Council of Europe | **Not a member** |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## Never a member

Belarus is the only European state that has **never** been a member
of [[INTL-COE]]. It held special guest status with the Parliamentary
Assembly from 1992; that status was **suspended in 1997** and has not been
restored, and the Council suspended all relations following the 2022
invasion of [[UA]] launched in part from Belarusian territory.

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

Listed in frontmatter.
