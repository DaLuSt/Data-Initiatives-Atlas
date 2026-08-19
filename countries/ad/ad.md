---
id: AD
type: country
name: Andorra
alternative_names:
  - Principality of Andorra
  - Andorra
  - Principat d'Andorra
description: >
  Country anchor entity for Andorra. It is a base anchor: it carries the
  country's position in the European legal and institutional frameworks so
  that entities scoped to it have somewhere to attach, and no national
  entities are modelled yet.

level: national
country: AD
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
    evidence: "Andorra is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union (coe.int 'The Council of Europe's 46 member states'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "AD — Andorra (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:AD"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Andorra

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

## Description

Andorra (ISO 3166-1 alpha-2: **`AD`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Andorra
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member since 1994 |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## The euro without the euro area

Andorra uses the **euro as its official currency under a monetary
agreement with the European Union**, without being an EU member state or a
member of the euro area. [[MC]], [[SM]] and [[VA]] are in the same position.

These four are the cleanest demonstration in Europe that monetary
arrangements and legal applicability come apart: the currency is the EU's and
the law is not.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter.
