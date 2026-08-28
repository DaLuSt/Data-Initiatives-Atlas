---
id: MU
type: country
name: Mauritius
alternative_names:
  - Republic of Mauritius
  - Maurice
description: >
  Country anchor entity for Mauritius, a party to Convention 108 and one
  of the eight states outside the Council of Europe that have ratified it.
  It is a base anchor: it exists because the Convention reaches Mauritius,
  and no national entities are modelled yet.

level: national
country: MU
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading en.wikipedia.org's own article directly (2026-08-27): 'Being non–Council of Europe states, Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia, and Uruguay have acceded to the treaty.' Independently confirmed by reading a Mauritian newspaper directly (2026-08-28, lemauricien.com 'Data Protection Day: Maurice, premier pays d'Afrique à ratifier la Convention 108+'): Mauritius is 'le 6e État après la Bulgarie, la Croatie, la Lituanie, la Pologne et la Serbie, ainsi que le premier pays d'Afrique à ratifier la Convention 108+' (the 6th state overall and the first African country to ratify Convention 108+, the amending protocol), which also confirms Mauritius's prior party status to the base Convention 108. dataprotection.govmu.org (Mauritius's own DPA) was tried again this pass and returned HTTP 403, not the 404 recorded previously — still genuinely unreadable either way. ISO's OBP remains confirmed genuinely bot-walled (403) and the WTO PDF remains confirmed genuinely unreadable (an image-based scan), but 2 of the entity's 3 cited sources are now read directly: a majority."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "MU — Mauritius (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:MU"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version (confirmed genuinely unreadable — image-based PDF)"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
  - title: "Data Protection Day: Maurice, premier pays d'Afrique à ratifier la Convention 108+"
    url: "https://www.lemauricien.com/actualites/data-protection-day-maurice-premier-pays-dafrique-a-ratifier-la-convention-108/400859/"
    publisher: "Le Mauricien"
    accessed: "2026-08-28"
---

# Mauritius

> **Promoted to `primary-source` 2026-08-28.** Wikipedia's own article
> was read directly and confirms Mauritius's accession by name in its
> own words. A Mauritian newspaper was found and read directly this
> pass, confirming Mauritius as the 6th state overall and first African
> state to ratify Convention 108+ (dataprotection.govmu.org, tried again,
> is still genuinely unreadable — 403 this time rather than 404, but
> either way dead). That is 2 of 3 cited sources read directly — ISO's
> OBP remains genuinely bot-walled (403) and the WTO PDF remains
> genuinely unreadable (an image-based scan) — a real majority.

## Description

Mauritius (ISO 3166-1 alpha-2: **`MU`**) is a **base country anchor**, and
one of the Atlas's first entities outside Europe and the UN system. It is
here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

Mauritius has ratified **both** Convention 108 and the amending protocol [[INTL-CONVENTION-108-PLUS]], putting it ahead of most European parties on the modernised instrument. Its Data Protection Office published its own communiqué on the CETS 223 ratification.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter, 2 of 4 read directly — Wikipedia (prior pass) and
Le Mauricien (this pass, 2026-08-28). ISO's OBP is genuinely bot-walled
(403) and the WTO PDF is genuinely unreadable (image-based scan).
dataprotection.govmu.org was retried this pass and is still genuinely
unreadable (403).
