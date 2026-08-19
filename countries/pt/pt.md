---
id: PT
type: country
name: Portugal
alternative_names:
  - Portuguese Republic
  - República Portuguesa
description: >
  Country anchor entity for Portugal, the eleventh national scope covered by
  the Data Initiatives Atlas and its ninth European Union member state. Used
  as the target of `country` fields for Portugal-scoped entities and of
  `applies-in` relationships from EU instruments.

level: national
country: PT
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
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
    evidence: "Portugal is one of the 27 member states of the European Union, having acceded on 1 January 1986; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "PT — Portugal (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:PT"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Agência para a Modernização Administrativa"
    url: "https://eportugal.gov.pt/entidades/agencia-para-a-modernizacao-administrativa"
    publisher: "ePortugal / Governo de Portugal"
---

# Portugal

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Portugal (ISO 3166-1 alpha-2: **`PT`**) is the **eleventh country** in the
Atlas and its **ninth EU member state**.

It was named in the structural review recorded in
`discovery/candidates.md` as the southern-European counterweight to
[[ES]] — the Iberian peninsula had one country in the Atlas and now has
two.

## What Portugal adds

- **A one-stop administrative modernisation agency.** [[PT-AMA]] combines
  administrative and regulatory simplification, e-government and public
  service delivery in a single public institute — a scope closer to
  [[GB-GDS]] and [[NO-DIGDIR]] than to the Dutch split between policy and
  [[NL-LOGIUS]].
- **A GDPR execution law with a name that says what it does.**
  [[PT-LEI-58-2019]] *executes* the Regulation in the domestic legal order.
- The **eleventh** country, and the **ninth** member state, against which the
  country-neutrality claim in README §16 holds.

## EU instruments that apply in Portugal

Recorded as `applies-in` edges on the instruments themselves, in the pattern
established by the Germany batch. See `countries/pt/index.md`.

## Not modelled

- The **Azores and Madeira**, Portugal's autonomous regions, which have their
  own administrations. The Atlas has no sub-national level — the same limit
  recorded for the Spanish Comunidades Autónomas and the German Länder.
- **ePortugal**, the citizen services portal, and the **Chave Móvel Digital**
  and **Cartão de Cidadão** identity means.

## Sources

Listed in frontmatter.
