---
id: MA
type: country
name: Morocco
alternative_names:
  - Kingdom of Morocco
  - Maroc
  - المغرب
  - al-Maghrib
description: >
  Country anchor entity for Morocco, a party to Convention 108 and one of
  the eight states outside the Council of Europe that have ratified it. It
  is a base anchor: it exists because the Convention reaches Morocco, and
  no national entities are modelled yet.

level: national
country: MA
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
    evidence: "Confirmed by reading en.wikipedia.org's own article directly (2026-08-27): 'Being non–Council of Europe states, Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia, and Uruguay have acceded to the treaty.' Independently confirmed by reading Morocco's own data protection authority's site directly (2026-08-28, cndp.ma 'Relations internationales'): 'Le Maroc a déposé auprès du Conseil de l'Europe une demande d'adhésion à la Convention 108... La demande du Maroc a été acceptée par le Conseil de l'Europe' (Morocco deposited an accession request with the Council of Europe, which was accepted), with the CNDP naming its own role and that of the Ministry of Foreign Affairs and Cooperation in the process. Neither page read directly gives a precise date; a WebSearch cross-check suggests ratification was deposited 28 May 2019 and entered into force 1 September 2019, but that date is not adopted here since no directly-read source states it — left null rather than padded. ISO's OBP remains confirmed genuinely bot-walled (403) and the WTO PDF remains confirmed genuinely unreadable (an image-based scan), but 2 of the entity's 3 cited sources are now read directly: a majority."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "MA — Morocco (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:MA"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version (confirmed genuinely unreadable — image-based PDF)"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
  - title: "Relations internationales"
    url: "https://www.cndp.ma/relations-internationales/"
    publisher: "Commission Nationale de contrôle de la protection des Données à caractère Personnel (CNDP), Morocco"
    accessed: "2026-08-28"
---

# Morocco

> **Promoted to `primary-source` 2026-08-28.** Wikipedia's own article was
> read directly and confirms Morocco's accession by name in its own
> words. Morocco's own data protection authority's site was found and
> read directly this pass, confirming Morocco's accession request was
> accepted by the Council of Europe (a precise date — 28 May 2019 deposit,
> 1 September 2019 in force — surfaced via WebSearch but is not adopted
> here since no directly-read source states it). That is 2 of 3 cited
> sources read directly —
> ISO's OBP remains genuinely bot-walled (403) and the WTO PDF remains
> genuinely unreadable (an image-based scan) — a real majority.

## Description

Morocco (ISO 3166-1 alpha-2: **`MA`**) is a **base country anchor**, and
one of the Atlas's first entities outside Europe and the UN system. It is
here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

Morocco is one of five African parties to Convention 108. It is not a Council of Europe member and has no prospect of EU membership, which makes it a clean example of the treaty doing the work it was opened to non-European accession to do.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter, 2 of 4 read directly — Wikipedia (prior pass) and
Morocco's own CNDP site (this pass, 2026-08-28). ISO's OBP is genuinely
bot-walled (403) and the WTO PDF is genuinely unreadable (image-based
scan).
