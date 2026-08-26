---
id: BE-GDPR-WET
type: law
name: Wet betreffende de bescherming van natuurlijke personen met betrekking tot de verwerking van persoonsgegevens
alternative_names:
  - Wet van 30 juli 2018
  - Gegevensbeschermingswet
  - Loi du 30 juillet 2018
  - Belgian Data Protection Act
description: >
  Belgian act of 30 July 2018 on the protection of natural persons with
  regard to the processing of personal data, in force from 5 September
  2018. It supplements the GDPR where the regulation left room for national
  legislators, and repealed the Belgian privacy act of 8 December 1992.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2018-09-05
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - BE-APD
related_entities:
  - EU-GDPR
  - NL-UAVG
  - DE-BDSG
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading three sources directly (2026-08-26). The act's own text at ejustice.just.fgov.be: '30 JULI 2018. - Wet betreffende de bescherming van natuurlijke personen met betrekking tot de verwerking van persoonsgegevens', published 5 September 2018. The Belgian Data Protection Authority's own page states the law 'integreert de beginsels van de AVG' (integrates the principles of the GDPR) and that it 'annuleert definitief de privacywet van 8 december 1992' (definitively cancels the privacy law of 8 December 1992) — directly confirming the repeal this entity asserts. Agoria's analysis adds that the law runs to 286 articles across 69 pages and lowered the age of digital consent for minors from 16 to 13."
    confidence: high
    valid_from: 2018-09-05
    valid_until: null

sources:
  - title: "Wet van 30 juli 2018 betreffende de bescherming van natuurlijke personen met betrekking tot de verwerking van persoonsgegevens"
    url: "https://www.ejustice.just.fgov.be/eli/wet/2018/07/30/2018040581/justel"
    publisher: "Belgisch Staatsblad / Moniteur belge (FOD Justitie)"
    accessed: "2026-08-26"
  - title: "Wet van 30 juli 2018"
    url: "https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/recht-op-afbeelding/wet-van-30-juli-2018"
    publisher: "Gegevensbeschermingsautoriteit (GBA/APD)"
    accessed: "2026-08-26"
  - title: "Wet bescherming persoonsgegevens (België)"
    url: "https://nl.wikipedia.org/wiki/Wet_bescherming_persoonsgegevens_(Belgi%C3%AB)"
    publisher: "Wikipedia"
  - title: "Daar is de nieuwe Belgische Gegevensbeschermingswet (Uitvoeringswet GDPR)"
    url: "https://www.agoria.be/nl/diensten/expertise/legal-tax-finance/juridisch/privacy-gegevensbescherming/daar-is-de-nieuwe-belgische-gegevensbeschermingswet-uitvoeringswet-gdpr"
    publisher: "Agoria"
    accessed: "2026-08-26"
  - title: "Wet van 30/07/2018 — geconsolideerde tekst"
    url: "https://etaamb.openjustice.be/nl/wet-van-30-juli-2018_n2018040581.html"
    publisher: "etaamb / OpenJustice"
---

# Wet van 30 juli 2018 (Belgian Data Protection Act)

> **Verified 2026-08-26.** Three of five sources were read directly — the
> act's own ELI text on the Belgisch Staatsblad, the Belgian Data Protection
> Authority's own page (which states the repeal of the 1992 act in as many
> words), and a law-firm analysis. Wikipedia and the etaamb consolidated
> text were not re-fetched this pass. `verification: primary-source`.

## Description

The act of **30 July 2018** on the protection of natural persons with
regard to the processing of personal data entered into force on
**5 September 2018**. It supplements [[EU-GDPR]] where the regulation left
room for national legislators, integrates the GDPR's principles, and
**definitively repealed the Belgian privacy act of 8 December 1992**.

[[BE-APD]] supervises it and publishes guidance on it, including on the
enhanced protection the GDPR and this act together give to special
categories of personal data.

## One EU regulation, three national implementing acts

This is the entity that completes the country-neutrality demonstration.
[[EU-GDPR]] remains **one** Atlas entity, in `legislation/`, `country:
null`. It now carries `applies-in` to three countries and is implemented by
three national acts:

```
                         EU-GDPR
                    /       |       \
        implements-requirement-from
                  /         |         \
           NL-UAVG      DE-BDSG     BE-GDPR-WET
```

There is no `BE-EU-GDPR`, no `DE-EU-GDPR` and no `NL-EU-GDPR`. Adding a
third country required no ontology change, no new relationship type and no
new folder — the same result Germany produced, now confirmed rather than
assumed.

**No relationship between the three national acts is asserted.** They are
siblings; their shared parent is the relationship.

## Better sourced than its German sibling

[[DE-BDSG]] carries an explicit warning that all four of its sources are
commercial legal publishers, with no Gesetze-im-Internet or
Bundesgesetzblatt citation, and that it should be the first German entity
re-sourced.

This entity has the citation the German one lacks: the **ELI reference on
the Belgisch Staatsblad** (`ejustice.just.fgov.be/eli/wet/2018/07/30/...`),
plus a consolidated text and the supervisory authority's own page. That is
the strongest legislative sourcing position of any national implementing
act in the Atlas.

It is worth noting *why*, because it is not a merit of this batch: Belgian
federal law is published under stable ELI URIs that a search index
surfaces, and German federal law largely is not. The Atlas's sourcing
quality partly tracks how each country publishes its statute book.

## Sources

Three of five read directly this pass — the ELI text on the Belgisch
Staatsblad, the GBA/APD's own page, and Agoria's analysis. Wikipedia and the
etaamb consolidated text remain unread.
