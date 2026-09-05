---
id: NL-EZK
type: organisation
name: Ministerie van Economische Zaken en Klimaat
alternative_names:
  - EZK
  - Ministry of Economic Affairs and Climate
  - Ministerie van Economische Zaken, Landbouw en Innovatie
description: >
  Dutch ministry responsible for the economy, including trade, industry,
  entrepreneurship, innovation, energy and climate policy, telecommunications
  and consumer affairs. Renamed to its current form on 26 October 2017, when
  the third Rutte cabinet took office; its Digitale Economie en Soevereiniteit
  portfolio holds oversight of the CBS and now co-leads the NDS.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2017-10-26
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-CBS
  - NL-NDS
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Anchor edge (metadata/relationship-types.md §2.3): EZK is a ministry of the Dutch state. Confirmed by reading rijksoverheid.nl's own ministry page directly (2026-09-05): it works 'toward a productive, resilient, and sustainable economy' across entrepreneurship, innovation, climate policy and digitalisation. nl.wikipedia.org, read directly the same pass, confirms the ministry was renamed 'Economische Zaken en Klimaat' in 2017 when the third Rutte cabinet took office, succeeding the 2010-2017 'Economische Zaken, Landbouw en Innovatie' ministry; the cabinet itself (and so the rename) is dated 26 October 2017 by a WebSearch cross-check of parlement.com and Rijksoverheid's own cabinet-history page."
    confidence: high
    valid_from: 2017-10-26
    valid_until: null
  - type: governed-by
    target: NL-WET-CBS
    source: interpretation
    evidence: "organisaties.overheid.nl's own CBS organisation profile, read directly by an earlier pass (2026-09-04, see [[NL-CBS]]), names EZK ('Economische Zaken en Klimaat') in its 'Relatie met ministerie' field. Recorded as an Atlas interpretation, not a `governed-by` edge from EZK's own side, since no page read describes EZK's oversight role in terms of the 2003 Wet CBS itself rather than a general organisational-relations field."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Ministerie van Economische Zaken en Klimaat"
    url: "https://www.rijksoverheid.nl/ministeries/ministerie-van-economische-zaken-en-klimaat"
    publisher: "Rijksoverheid"
    accessed: "2026-09-05"
  - title: "Ministerie van Economische Zaken en Klimaat"
    url: "https://nl.wikipedia.org/wiki/Ministerie_van_Economische_Zaken_en_Klimaat"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
  - title: "Contactgegevens Economische Zaken en Klimaat"
    url: "https://organisaties.overheid.nl/10621/Economische_Zaken_en_Klimaat"
    publisher: "Overheid.nl"
---

# Ministerie van Economische Zaken en Klimaat (EZK)

Picked up from `discovery/unresolved.md`, which asked which ministry
currently holds oversight of [[NL-CBS]] — a question [[NL-CBS]]'s own
2026-09-04 pass had already answered in prose but without an Atlas entity
to link to. Creating this entity also lets [[NL-NDS]]'s "EZK now
co-leading" finding point at something real.

## Description

EZK is the Dutch ministry responsible for the economy: trade, industry,
entrepreneurship, innovation, energy and climate policy, telecommunications
and consumer affairs. Reading `rijksoverheid.nl`'s own page directly, its
remit explicitly includes digitalisation, organised under a **Digitale
Economie en Soevereiniteit** (Digital Economy and Sovereignty) portfolio.

## History

Confirmed by reading `nl.wikipedia.org` directly: the ministry traces back
to a 1905 "Landbouw, Nijverheid en Handel" ministry, renamed "Economische
Zaken" in 1933. It took its current name on **26 October 2017**, when the
third Rutte cabinet was sworn in (date confirmed by a WebSearch cross-check
of parlement.com and Rijksoverheid's own cabinet-history page), succeeding
the 2010–2017 "Economische Zaken, Landbouw en Innovatie" ministry. None of
these predecessor ministries are modelled as separate Atlas entities —
consistent with how the Atlas treats ministry lineages elsewhere (e.g. the
unmodelled 1930 TNO-wet predecessor on [[NL-TNO-WET]]).

## Relationships

- `part-of` [[NL]] — anchor edge; a ministry of the Dutch state.
- Interpreted oversight relationship to [[NL-CBS]], via [[NL-WET-CBS]] —
  `organisaties.overheid.nl` names EZK as CBS's ministry, but no page read
  frames this in terms of the 2003 act itself, so it is recorded as an
  Atlas interpretation rather than a sourced `governed-by` fact.
- Related to [[NL-NDS]]: `nieuwe-kabinet-duidelijk-de-nds-gaat-door`
  (read directly by [[NL-NDS]]'s own 2026-08-27 pass) names an EZK state
  secretary for digital economy and sovereignty as now co-overseeing the
  NDS alongside [[NL-BZK]]. No typed edge is added from this side beyond
  the existing `related_entities` reference, since this entity's own
  sources do not themselves describe the NDS relationship.

## Sources

Listed in frontmatter, all three read directly this pass.
