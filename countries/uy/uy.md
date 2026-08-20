---
id: UY
type: country
name: Uruguay
alternative_names:
  - Oriental Republic of Uruguay
  - República Oriental del Uruguay
description: >
  Country anchor entity for Uruguay, a party to Convention 108 and one of
  the eight states outside the Council of Europe that have ratified it. It
  is a base anchor: it exists because the Convention reaches Uruguay, and
  no national entities are modelled yet.

level: national
country: UY
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
  - INTL-CONVENTION-108
relationships:
  - type: related-to
    target: INTL-CONVENTION-108
    source: fact
    evidence: "Eight non-Council of Europe countries from Africa and Latin America have ratified Convention 108: Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia and Uruguay (en.wikipedia.org 'Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data', citing the Council of Europe chart of signatures and ratifications; wto.org 'Facilitating transborder data flows: Convention 108'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: this country is in the Atlas because the Convention reaches it, and the edge records nothing beyond being a party to that treaty."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UY — Uruguay (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:UY"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
---

# Uruguay

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Uruguay (ISO 3166-1 alpha-2: **`UY`**) is a **base country anchor**, and
one of the Atlas's first entities outside Europe and the UN system. It is
here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

**Uruguay was the first non-European state to accede** to Convention 108, which is the moment the treaty stopped being a regional instrument. It also holds an EU adequacy decision, granted in 2012.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter.
