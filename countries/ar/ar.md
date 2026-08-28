---
id: AR
type: country
name: Argentina
alternative_names:
  - Argentine Republic
  - República Argentina
description: >
  Country anchor entity for Argentina, a party to Convention 108 and one
  of the eight states outside the Council of Europe that have ratified it.
  It is a base anchor: it exists because the Convention reaches Argentina,
  and no national entities are modelled yet.

level: national
country: AR
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
    evidence: "Confirmed by reading en.wikipedia.org's own article directly (2026-08-27): 'Being non–Council of Europe states, Argentina, Cabo Verde, Mauritius, Mexico, Morocco, Senegal, Tunisia, and Uruguay have acceded to the treaty.' Independently confirmed by reading Argentina's own government's press release directly (2026-08-28, argentina.gob.ar 'Argentina, Estado Parte del Convenio 108'): Argentina became the 54th state to join Convention 108, with President Mauricio Macri and Foreign Minister Jorge Faurie depositing the instruments of accession with the Council of Europe's Secretary General on 25 February 2019, and the Convention and its Additional Protocol entering into force for Argentina on 1 June 2019 — a more precise date than this entity previously carried. ISO's OBP remains confirmed genuinely bot-walled (403) and the WTO PDF remains confirmed genuinely unreadable (an image-based scan), but 2 of the entity's 3 cited sources are now read directly: a majority. Anchor edge under metadata/relationship-types.md §2.3: this country is in the Atlas because the Convention reaches it, and the edge records nothing beyond being a party to that treaty."
    confidence: high
    valid_from: 2019-06-01
    valid_until: null

sources:
  - title: "AR — Argentina (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:AR"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Convention for the Protection of Individuals with Regard to Automatic Processing of Personal Data"
    url: "https://en.wikipedia.org/wiki/Convention_for_the_Protection_of_Individuals_with_Regard_to_Automatic_Processing_of_Personal_Data"
    publisher: "Wikipedia"
  - title: "Facilitating transborder data flows: Convention 108 and its modernised version (confirmed genuinely unreadable — image-based PDF)"
    url: "https://www.wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf"
    publisher: "World Trade Organization"
  - title: "Argentina, Estado Parte del Convenio 108"
    url: "https://www.argentina.gob.ar/noticias/argentina-estado-parte-del-convenio-108"
    publisher: "Argentina.gob.ar (Ministerio de Relaciones Exteriores)"
    accessed: "2026-08-28"
---

# Argentina

> **Promoted to `primary-source` 2026-08-28.** Wikipedia's own article was
> read directly and confirms Argentina's accession by name in its own
> words. Argentina's own government press release was found and read
> directly this pass, giving a precise accession date: instruments
> deposited 25 February 2019, in force 1 June 2019, as the 54th state
> party. That is 2 of 3 cited sources read directly — ISO's OBP remains
> genuinely bot-walled (403) and the WTO PDF remains genuinely unreadable
> (an image-based scan) — a real majority.

## Description

Argentina (ISO 3166-1 alpha-2: **`AR`**) is a **base country anchor**, and
one of the Atlas's first entities outside Europe and the UN system. It is
here because it is a party to [[INTL-CONVENTION-108]].

## Why this country is in a European data atlas

Convention 108 is the only binding international treaty on data protection
and it is open to accession by any state. Eight non-European states have
acceded, and modelling the treaty without them would have modelled it as
the regional instrument it is not.

Argentina holds an EU adequacy decision, granted in 2003 and one of the earliest, and acceded to Convention 108 in 2019. The two facts are connected: [[EU-GDPR]] Recital 105 makes accession a factor in adequacy assessment.

## What this anchor does not yet carry

Nothing beyond treaty membership. There is no national data protection
authority, no legislation, no portal and no statistics office attached to
this entity. The Atlas's scope is European data governance; these eight
anchors are the reach of one treaty, not the start of a global country
layer.

## Sources

Listed in frontmatter, 2 of 4 read directly — Wikipedia (prior pass) and
Argentina's own government press release (this pass, 2026-08-28). ISO's
OBP is genuinely bot-walled (403) and the WTO PDF is genuinely unreadable
(image-based scan).
