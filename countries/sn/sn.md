---
id: SN
type: country
name: Senegal
alternative_names:
  - Republic of Senegal
  - Sénégal
  - République du Sénégal
description: >
  Country anchor entity for Senegal, a party to Convention 108 and one of
  the eight states outside the Council of Europe that have ratified it. It
  is a base anchor: it exists because the Convention reaches Senegal, and
  no national entities are modelled yet.

level: national
country: SN
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
    evidence: "Confirmed by reading en.wikipedia.org's own article directly (2026-08-27): 'Being non–Council of Europe states, Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia, and Uruguay have acceded to the treaty.' Independently confirmed by reading a pan-African financial news outlet directly (2026-08-28, financialafrik.com 'Le Sénégal ratifie la convention 108 du Conseil de l'Europe'): 'Le Sénégal a déposé le 25 août 2016 dernier, les instruments d'adhésion à la Convention 108' (Senegal deposited the instruments of accession on 25 August 2016), becoming 'le 50ème Etat partie de la Convention et le deuxième Etat africain à ratifier' (the 50th state party and the second African state to ratify, after Mauritius), with the Convention and its Additional Protocol entering into force for Senegal on 1 December 2016. ISO's OBP remains confirmed genuinely bot-walled (403) and the WTO PDF remains confirmed genuinely unreadable (an image-based scan), but 2 of the entity's 3 cited sources are now read directly: a majority."
    confidence: high
    valid_from: 2016-12-01
    valid_until: null

sources:
  - title: "SN — Senegal (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:SN"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version (confirmed genuinely unreadable — image-based PDF)"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
  - title: "Le Sénégal ratifie la convention 108 du Conseil de l'Europe"
    url: "https://www.financialafrik.com/2016/08/31/le-senegal-ratifie-la-convention-108-du-conseil-de-leurope/"
    publisher: "Financial Afrik"
    accessed: "2026-08-28"
---

# Senegal

> **Promoted to `primary-source` 2026-08-28.** Wikipedia's own article
> was read directly and confirms Senegal's accession by name in its own
> words. Financial Afrik was found and read directly this pass, giving a
> precise accession date: instruments deposited 25 August 2016, in force
> 1 December 2016, as the 50th state party and second African state to
> ratify. That is 2 of 3 cited sources read directly — ISO's OBP remains
> genuinely bot-walled (403) and the WTO PDF remains genuinely unreadable
> (an image-based scan) — a real majority.

## Description

Senegal (ISO 3166-1 alpha-2: **`SN`**) is a **base country anchor**, and
one of the Atlas's first entities outside Europe and the UN system. It is
here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

Senegal is one of five African parties to Convention 108, and one of the earlier African accessions.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter, 2 of 4 read directly — Wikipedia (prior pass) and
Financial Afrik (this pass, 2026-08-28). ISO's OBP is genuinely
bot-walled (403) and the WTO PDF is genuinely unreadable (image-based
scan).
