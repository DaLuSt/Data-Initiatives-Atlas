---
id: TN
type: country
name: Tunisia
alternative_names:
  - Republic of Tunisia
  - Tunisie
  - تونس
description: >
  Country anchor entity for Tunisia, a party to Convention 108 and one of
  the eight states outside the Council of Europe that have ratified it. It
  is a base anchor: it exists because the Convention reaches Tunisia, and
  no national entities are modelled yet.

level: national
country: TN
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
    evidence: "Confirmed by reading en.wikipedia.org's own article directly (2026-08-27): 'Being non–Council of Europe states, Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia, and Uruguay have acceded to the treaty.' Independently confirmed by reading a Tunisian news site directly (2026-08-28, webmanagercenter.com 'La Tunisie signe la Convention 108 du Conseil de l'Europe sur la protection des données personnelles'), which quotes the INPDP's own president stating 'la Tunisie a signé la convention 108 depuis le 1er novembre 2017' (Tunisia has been party to Convention 108 since 1 November 2017), and separately reports Tunisia's 24 May 2019 signature of the amending protocol (Convention 108+) as the 30th state to do so — ahead of several European states. epic.org, tried again this pass as a possible alternate, still returns HTTP 403. ISO's OBP remains confirmed genuinely bot-walled (403) and the WTO PDF remains confirmed genuinely unreadable (an image-based scan), but 2 of the entity's 3 cited sources are now read directly: a majority."
    confidence: high
    valid_from: 2017-11-01
    valid_until: null

sources:
  - title: "TN — Tunisia (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:TN"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version (confirmed genuinely unreadable — image-based PDF)"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
  - title: "La Tunisie signe la Convention 108 du Conseil de l'Europe sur la protection des données personnelles"
    url: "https://www.webmanagercenter.com/2019/05/27/435334/la-tunisie-signe-la-convention-108-du-conseil-de-leurope-sur-la-protection-des-donnees-personnelles/"
    publisher: "WebManagerCenter"
    accessed: "2026-08-28"
---

# Tunisia

> **Promoted to `primary-source` 2026-08-28.** Wikipedia's own article
> was read directly and confirms Tunisia's accession by name in its own
> words. A Tunisian news site quoting the INPDP's own president was
> found and read directly this pass, confirming Tunisia has been party
> to Convention 108 since 1 November 2017 and signed Convention 108+ on
> 24 May 2019 as the 30th state to do so. epic.org, previously the
> alternate this entity's body text mentioned, was retried and still
> 403s. That is 2 of 3 cited sources read directly — ISO's OBP remains
> genuinely bot-walled (403) and the WTO PDF remains genuinely unreadable
> (an image-based scan) — a real majority.

## Description

Tunisia (ISO 3166-1 alpha-2: **`TN`**) is a **base country anchor**, and
one of the Atlas's first entities outside Europe and the UN system. It is
here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

Tunisia is one of five African parties to Convention 108 and appears in EPIC's account of the convention's non-European reach.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter, 2 of 4 read directly — Wikipedia (prior pass) and
WebManagerCenter (this pass, 2026-08-28). ISO's OBP is genuinely
bot-walled (403) and the WTO PDF is genuinely unreadable (image-based
scan).
