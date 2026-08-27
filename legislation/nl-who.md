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
confidence: medium
coverage: medium
verification: primary-source

start_date: 2024-06-19
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading rijksoverheid.nl's own announcement directly (2026-08-27): 'Op 19 juni 2024 is de Wet implementatie Open data richtlijn inwerking getreden. Met deze wijziging is de Europese Open data richtlijn geïmplementeerd in de Nederlandse Wet hergebruik van overheidsinformatie.' eerstekamer.nl, also read directly, confirms the bill amends the Who to implement EU Directive 2019/1024, was adopted by the Eerste Kamer without amendment on 4 June 2024 following Tweede Kamer approval on 12 March 2024, and was published in Staatsblad nr. 164 on 18 June 2024, entering into force the following day. minbzk.github.io's own hWho guidance, read directly, confirms the same 19 June 2024 date and the mechanism (a European list of high-value datasets, six categories, machine-readable via free APIs)."
    confidence: high
    valid_from: 2024-06-19
    valid_until: null

sources:
  - title: "Inwerkingtreding Wet implementatie Open data richtlijn"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2024/08/02/inwerkingtreding-wet-implementatie-open-data-richtlijn"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "Wet implementatie Open data richtlijn (36.382)"
    url: "https://www.eerstekamer.nl/wetsvoorstel/36382_wet_implementatie_open_data"
    publisher: "Eerste Kamer der Staten-Generaal"
    accessed: "2026-08-27"
  - title: "Handleiding Herziene Who n.a.v. de Wet implementatie open data richtlijn"
    url: "https://minbzk.github.io/publicatie/hl/hwho/"
    publisher: "Ministerie van BZK"
    accessed: "2026-08-27"
  - title: "Wet hergebruik van overheidsinformatie"
    url: "https://vng.nl/projecten/wet-hergebruik-van-overheidsinformatie"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-27"
---

# Wet hergebruik van overheidsinformatie (Who)

> **Verified 2026-08-27.** All four cited pages were read directly, closing
> both the "not read" gap and the previously-unresolved entry-into-force
> date. `verification` moves from `search-only` to `primary-source`,
> `confidence` from `low` to `medium`.

## Description

The Who governs the re-use of public sector information in the Netherlands.
On **19 June 2024** it was amended by the *Wet implementatie Open data
richtlijn*, which transposed [[EU-OPEN-DATA-DIRECTIVE]] (Directive (EU)
2019/1024) into Dutch law; the amended act is often referred to as the
herziene Who (hWho). Confirmed by reading eerstekamer.nl directly: the
Tweede Kamer approved the bill on 12 March 2024, the Eerste Kamer adopted it
without amendment on 4 June 2024, it was published as Staatsblad 2024, 164
on 18 June 2024, and — per the bill's own commencement rule, "the day after
publication" — entered into force on 19 June 2024.

Under the revised regime, confirmed by reading minbzk.github.io's own hWho
guidance directly: government organisations and public undertakings (now
including publicly-funded research organisations, an expanded scope) must
proactively make more data available for re-use; dynamic data must in
principle become available via APIs immediately after collection; and only
marginal distribution costs may be charged in most cases. A European list of
high-value datasets spans six categories — geospatial, earth observation,
meteorological, statistics, business registers and mobility — which must be
provided free of charge in machine-readable form via APIs. vng.nl's own
impact analysis, also read directly, states that Dutch **municipalities
carry no additional obligations** under this list for five of the six
themes, as they are "geen dataprovider" (not a data provider) for those; the
sixth (environmental data) required further investigation per that page.

**The previously-unresolved date is now resolved.** The rijksoverheid.nl
page cited was itself dated 2 August 2024 but, read directly, states the
law's own entry into force as 19 June 2024 — the two dates concern different
things (a later news announcement vs. the actual commencement date), not a
genuine conflict. `start_date` now records 19 June 2024.

## Modelling note

The Who and the Wet implementatie Open data richtlijn are modelled as **one
entity**, not two: the implementing act is an amending statute whose effect
is carried by the Who. This pass confirms that model is defensible under
`metadata/relationship-types.md` §2.1's `amends` type — the implementing act
amends the Who "which continues to exist under its own name and date" — but
leaves the existing single-entity choice unchanged rather than splitting it,
since no source read this pass gave the amending act independent standing
beyond its effect on the Who.

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

Listed in frontmatter, all four read directly this pass.
