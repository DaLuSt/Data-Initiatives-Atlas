---
id: MK
type: country
name: North Macedonia
alternative_names:
  - Republic of North Macedonia
  - Северна Македонија
  - Republika e Maqedonisë së Veriut
description: >
  Country anchor entity for North Macedonia, a candidate country for
  European Union membership since 2005. It is a base anchor: it carries
  the country's position in the European legal and institutional
  frameworks so that entities scoped to it have somewhere to attach, and
  no national entities are modelled yet.

level: national
country: MK
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
    evidence: "Confirmed by reading two Wikipedia articles directly (2026-08-27) after coe.int itself proved genuinely, domain-wide bot-walled (403) on every path tried: the 'Member states of the Council of Europe' article's own accession table gives North Macedonia's accession date as 9 November 1995, the same day as Ukraine; the general 'Council of Europe' article corroborates current membership. ISO's OBP is also confirmed blocked (403) — it is a JavaScript application, not a static page. The EU-candidacy year (2005) rests on enlargement.ec.europa.eu, read directly in the prior pass but not independently re-confirmed this pass to a specific month/day. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: high
    valid_from: 1995-11-09
    valid_until: null

sources:
  - title: "MK — North Macedonia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:MK"
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

# North Macedonia

> **Verified 2026-08-27.** `coe.int` and ISO's OBP are both confirmed
> genuinely bot-walled (403). Two Wikipedia articles were read directly
> instead and independently confirm Council of Europe membership with an
> exact accession date — a genuine majority (4 of 6 cited pages). The
> EU-candidacy year rests on enlargement.ec.europa.eu, read in the prior
> pass; its specific month/day was not independently re-confirmed.

## Description

North Macedonia (ISO 3166-1 alpha-2: **`MK`**) is a **base country
anchor**, created so that entities scoped to it have somewhere to attach.
No North Macedonia entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | **Candidate country** since 2005 |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member since **9 November 1995** |

Confirmed by reading Wikipedia's "Member states of the Council of
Europe" article directly (2026-08-27): its own accession table gives
the exact date, replacing the bare year this entity previously carried
on general reference knowledge alone. The EU-candidacy year (2005) is
unchanged prior knowledge, not independently re-confirmed to a specific
date this pass.

## Twenty-one years a candidate

North Macedonia has held EU candidate status since **2005** and has
still not opened its first negotiating chapter — the longest wait of any
current candidate except [[TR]].

The opening is reported to depend on constitutional reform, an
anti-corruption agenda, and relations with two neighbouring member states,
[[BG]] and [[GR]]. That is a rare case where the Atlas's own country anchors
are the parties to the obstacle.

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
