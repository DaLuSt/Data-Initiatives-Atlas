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
verification: search-only

start_date: 2018-09-05
end_date: null
last_verified: null
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
    evidence: "The wet van 30 juli 2018 is the Belgian law enacted to implement the European General Data Protection Regulation (2016/679); it supplements the GDPR where the GDPR left room for national member states, integrates the GDPR's principles and definitively repeals the privacy law of 8 December 1992 (nl.wikipedia.org 'Wet bescherming persoonsgegevens (België)'; agoria.be; siriuslegaladvocaten.be). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-09-05
    valid_until: null

sources:
  - title: "Wet van 30 juli 2018 betreffende de bescherming van natuurlijke personen met betrekking tot de verwerking van persoonsgegevens"
    url: "https://www.ejustice.just.fgov.be/eli/wet/2018/07/30/2018040581/justel"
    publisher: "Belgisch Staatsblad / Moniteur belge (FOD Justitie)"
  - title: "Wet van 30 juli 2018"
    url: "https://www.gegevensbeschermingsautoriteit.be/burger/thema-s/recht-op-afbeelding/wet-van-30-juli-2018"
    publisher: "Gegevensbeschermingsautoriteit (GBA/APD)"
  - title: "Wet bescherming persoonsgegevens (België)"
    url: "https://nl.wikipedia.org/wiki/Wet_bescherming_persoonsgegevens_(Belgi%C3%AB)"
    publisher: "Wikipedia"
  - title: "Daar is de nieuwe Belgische Gegevensbeschermingswet (Uitvoeringswet GDPR)"
    url: "https://www.agoria.be/nl/diensten/expertise/legal-tax-finance/juridisch/privacy-gegevensbescherming/daar-is-de-nieuwe-belgische-gegevensbeschermingswet-uitvoeringswet-gdpr"
    publisher: "Agoria"
  - title: "Wet van 30/07/2018 — geconsolideerde tekst"
    url: "https://etaamb.openjustice.be/nl/wet-van-30-juli-2018_n2018040581.html"
    publisher: "etaamb / OpenJustice"
---

# Wet van 30 juli 2018 (Belgian Data Protection Act)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

Listed in frontmatter.
