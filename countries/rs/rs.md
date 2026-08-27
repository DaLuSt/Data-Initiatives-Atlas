---
id: RS
type: country
name: Serbia
alternative_names:
  - Republic of Serbia
  - Србија
  - Republika Srbija
description: >
  Country anchor entity for Serbia, a candidate country for European Union
  membership since 2012. It is a base anchor: it carries the country's
  position in the European legal and institutional frameworks so that
  entities scoped to it have somewhere to attach, and no national entities
  are modelled yet.

level: national
country: RS
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
    evidence: "Confirmed by reading two Wikipedia articles directly (2026-08-27) after coe.int itself proved genuinely, domain-wide bot-walled (403) on every path tried: the 'Member states of the Council of Europe' article's own accession table gives Serbia's accession date as 3 April 2003; the general 'Council of Europe' article corroborates current membership. ISO's OBP is also confirmed blocked (403) — it is a JavaScript application, not a static page. The EU-candidacy year (2012) rests on enlargement.ec.europa.eu, read directly in the prior pass but not independently re-confirmed this pass to a specific month/day. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: high
    valid_from: 2003-04-03
    valid_until: null

sources:
  - title: "RS — Serbia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:RS"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states (confirmed genuinely bot-walled, 403)"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Candidate countries and potential candidates"
    url: "https://enlargement.ec.europa.eu/enlargement-policy/candidate-countries-and-potential-candidates_en"
    publisher: "European Commission — Enlargement and Eastern Neighbourhood"
    accessed: "2026-08-27"
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

# Serbia

> **Verified 2026-08-27.** `coe.int` and ISO's OBP are both confirmed
> genuinely bot-walled (403). Two Wikipedia articles were read directly
> instead and independently confirm Council of Europe membership with an
> exact accession date — a genuine majority (4 of 6 cited pages). The
> EU-candidacy year rests on enlargement.ec.europa.eu, read in the prior
> pass; its specific month/day was not independently re-confirmed.

## Description

Serbia (ISO 3166-1 alpha-2: **`RS`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Serbia
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | **Candidate country** since 2012 |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member since **3 April 2003** |

Confirmed by reading Wikipedia's "Member states of the Council of
Europe" article directly (2026-08-27): its own accession table gives
the exact date, replacing the bare year this entity previously carried
on general reference knowledge alone. The EU-candidacy year (2012) is
unchanged prior knowledge, not independently re-confirmed to a specific
date this pass.

## Candidate since 2012

Serbia has been an EU candidate since 2012 and has been negotiating
longer than [[UA]] and [[MD]], which are now reported to be ahead of it.

Serbia does not recognise [[XK]]'s declaration of independence, which is one
reason Kosovo's own accession path is a potential-candidate track rather than
a candidate one.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter, four of six read directly this pass — both
Wikipedia articles, government.nl and (from the prior pass)
enlargement.ec.europa.eu. `coe.int` and ISO's OBP are both genuinely
bot-walled (403).
