---
id: CV
type: country
name: Cabo Verde
alternative_names:
  - Republic of Cabo Verde
  - Cabo Verde
  - República de Cabo Verde
description: >
  Country anchor entity for Cabo Verde, a party to Convention 108 and one
  of the eight states outside the Council of Europe that have ratified it.
  It is a base anchor: it exists because the Convention reaches Cabo
  Verde, and no national entities are modelled yet.

level: national
country: CV
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading en.wikipedia.org's own article directly (2026-08-27): 'Being non–Council of Europe states, Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia, and Uruguay have acceded to the treaty.' ISO's OBP is confirmed genuinely bot-walled (403) — a JavaScript application, not a static page — and the WTO PDF is confirmed genuinely unreadable (an image-based scan with no extractable text), so only 1 of 3 cited sources is read: not a majority. Anchor edge under metadata/relationship-types.md §2.3: this country is in the Atlas because the Convention reaches it, and the edge records nothing beyond being a party to that treaty."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CV — Cabo Verde (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:CV"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version (confirmed genuinely unreadable — image-based PDF)"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
---

# Cabo Verde

> **Re-checked 2026-08-27, still `search-only`.** Wikipedia's own article
> was read directly and confirms Cabo Verde's accession by name in its
> own words. ISO's OBP is confirmed genuinely bot-walled (403) and the
> WTO PDF is confirmed genuinely unreadable (an image-based scan). One of
> three is not a majority.

## Description

Cabo Verde (ISO 3166-1 alpha-2: **`CV`**) is a **base country anchor**,
and one of the Atlas's first entities outside Europe and the UN system. It
is here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

Cabo Verde is one of four African parties to Convention 108, with [[MU]], [[MA]], [[SN]] and [[TN]] — five of the eight non-European parties are African, which is not the distribution most descriptions of the treaty imply.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter, one of three read directly this pass — Wikipedia.
ISO's OBP is genuinely bot-walled (403) and the WTO PDF is genuinely
unreadable (image-based scan).
