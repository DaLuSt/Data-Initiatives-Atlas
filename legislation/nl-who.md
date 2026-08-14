---
id: NL-WHO
type: law
name: Wet hergebruik van overheidsinformatie
alternative_names:
  - Who
  - hWho
  - Herziene Wet hergebruik van overheidsinformatie
description: >
  Dutch act on the re-use of public sector information. Amended in 2024 by
  the Wet implementatie Open data richtlijn, which transposed EU Directive
  2019/1024 into Dutch law and obliges public bodies and public undertakings
  to make more data proactively available for re-use, including designated
  high-value datasets.

level: national
country: NL
region: EU

status: active
confidence: low
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "The Wet implementatie Open data richtlijn implements EU directive 2019/1024 into Dutch law by amending the Who (rijksoverheid.nl; Eerste Kamer dossier 36.382; BZK Handleiding Herziene Who). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Inwerkingtreding Wet implementatie Open data richtlijn"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2024/08/02/inwerkingtreding-wet-implementatie-open-data-richtlijn"
    publisher: "Rijksoverheid"
  - title: "Wet implementatie Open data richtlijn (36.382)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/36382_wet_implementatie_open_data"
    publisher: "Eerste Kamer der Staten-Generaal"
  - title: "Handleiding Herziene Who n.a.v. de Wet implementatie open data richtlijn"
    url: "https://minbzk.github.io/publicatie/hl/hwho/"
    publisher: "Ministerie van BZK"
  - title: "Wet hergebruik van overheidsinformatie"
    url: "https://vng.nl/projecten/wet-hergebruik-van-overheidsinformatie"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
---

# Wet hergebruik van overheidsinformatie (Who)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Who governs the re-use of public sector information in the Netherlands.
In 2024 it was amended by the *Wet implementatie Open data richtlijn*, which
transposed [[EU-OPEN-DATA-DIRECTIVE]] (Directive (EU) 2019/1024) into Dutch
law; the amended act is often referred to as the herziene Who (hWho).

Under the revised regime, government organisations and government
undertakings must make greater efforts to proactively make as much data as
possible available for re-use. High-value datasets have been designated in
the Netherlands, and municipal and provincial high-value dataset lists exist
to support decentralised governments in opening data.

**Unresolved date.** Search results gave two different entry-into-force
dates for the implementing act: 19 June 2024 in one result, while the
rijksoverheid announcement of entry into force is dated 2 August 2024. The
discrepancy is unresolved and `start_date` is therefore left null rather
than guessed. Recorded in `discovery/unresolved.md`.

## Modelling note

The Who and the Wet implementatie Open data richtlijn are modelled as **one
entity**, not two: the implementing act is an amending statute whose effect
is carried by the Who. If Batch 3's re-verification finds the amending act
has independent significance, it should be split out — recorded in
`discovery/unresolved.md`.

## Classification

Dutch implementation legislation per `metadata/taxonomy.md` §2:
`type: law`, `level: national`, `country: NL`, `region: EU`.

## Relationships

- Implements requirements from [[EU-OPEN-DATA-DIRECTIVE]].
- Policy responsibility within [[NL-BZK]].
- Closely related to [[NL-WOO]] (active disclosure of government
  information) — the two concern overlapping but distinct regimes
  (openness vs. re-use). No relationship asserted, as none was sourced.

## Sources

Listed in frontmatter.
