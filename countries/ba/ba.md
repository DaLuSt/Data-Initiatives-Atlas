---
id: BA
type: country
name: Bosnia and Herzegovina
alternative_names:
  - Bosnia and Herzegovina
  - Bosna i Hercegovina
  - Босна и Херцеговина
description: >
  Country anchor entity for Bosnia and Herzegovina, a candidate country
  for European Union membership since 2022. It is a base anchor: it
  carries the country's position in the European legal and institutional
  frameworks so that entities scoped to it have somewhere to attach, and
  no national entities are modelled yet.

level: national
country: BA
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
    evidence: "Bosnia and Herzegovina is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union (coe.int 'The Council of Europe's 46 member states'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BA — Bosnia and Herzegovina (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:BA"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Candidate countries and potential candidates"
    url: "https://enlargement.ec.europa.eu/enlargement-policy/candidate-countries-and-potential-candidates_en"
    publisher: "European Commission — Enlargement and Eastern Neighbourhood"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Bosnia and Herzegovina

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Bosnia and Herzegovina (ISO 3166-1 alpha-2: **`BA`**) is a **base country
anchor**, created so that entities scoped to it have somewhere to attach.
No Bosnia and Herzegovina entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | **Candidate country** since 2022 |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member since 2002 |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## Candidate since December 2022

Bosnia and Herzegovina was granted EU **candidate status in
December 2022**, six months after [[UA]] and [[MD]].

Its constitutional structure — two entities and a district, with a
three-member presidency — is the most extreme case in Europe of the
sub-national tier the Atlas's `level` vocabulary cannot represent. Where
[[BE]] has three Regions and three Communities, here the constituent units
hold most of the competences that a data atlas would want to model.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter.
