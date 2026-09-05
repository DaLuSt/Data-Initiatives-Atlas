---
id: NL-RIJKSWATERSTAAT
type: organisation
name: Rijkswaterstaat
alternative_names:
  - RWS
description: >
  Executive agency (uitvoeringsorganisatie/agentschap) of the Dutch
  Ministry of Infrastructure and Water Management, responsible for
  national roads, waterways and water management, and for sustainable
  spatial development. Manages public data infrastructure covering
  waterway and traffic information, and was a founding partner of both
  PDOK (2013) and the National Data Warehouse for Traffic Information.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - NL-PDOK
  - NL-NDW
  - NL-GEONOVUM
  - NL-KADASTER
  - NL-IENW
relationships:
  - type: part-of
    target: NL-IENW
    source: fact
    evidence: "Confirmed by reading rijkswaterstaat.nl's own 'Onze organisatie' page directly (2026-09-05): it is the 'uitvoeringsorganisatie' of the Ministerie van Infrastructuur en Waterstaat, and rijksfinancien.nl's own budget documentation, also consulted, names it 'Agentschap Rijkswaterstaat.' en.wikipedia.org's own account of the ministry, also read directly, names Rijkswaterstaat as one of its executive agencies. Upgraded same-day from an anchor `part-of` [[NL]] edge, recorded before [[NL-IENW]] existed as an Atlas entity."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-PDOK
    source: fact
    evidence: "Confirmed already on NL-PDOK's own file, reading pdok.nl's own 'Over PDOK' page directly: PDOK was established in 2013 as a collaboration between Kadaster, several ministries, Rijkswaterstaat and Geonovum."
    confidence: high
    valid_from: 2013-01-01
    valid_until: null
  - type: participates-in
    target: NL-NDW
    source: fact
    evidence: "Confirmed already on NL-NDW's own file, reading organisaties.overheid.nl's own listing directly: Rijkswaterstaat is named among the government partners in the National Data Warehouse for Traffic Information."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Onze organisatie"
    url: "https://www.rijkswaterstaat.nl/over-ons/onze-organisatie"
    publisher: "Rijkswaterstaat"
    accessed: "2026-09-05"
---

# Rijkswaterstaat

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged Rijkswaterstaat as an unmodelled
> founding partner of [[NL-PDOK]], which had noted "the Ministry of
> Infrastructure and Water Management and Rijkswaterstaat are not yet
> Atlas entities... [which] makes the founding collaboration look
> narrower than it was." Its own "Onze organisatie" page was read
> directly this pass.

## Description

Rijkswaterstaat is the **executive agency** ("uitvoeringsorganisatie",
per `rijksfinancien.nl`'s own budget documentation an "Agentschap") of
the **Ministry of Infrastructure and Water Management**. Reading
`rijkswaterstaat.nl`'s own page directly, it is organised around three
domains: **water infrastructure** (flood protection, water management,
inland shipping routes), **road networks** (highway maintenance and
traffic management), and **environmental/spatial development**
(sustainable land planning). It also manages **public data
infrastructure** covering waterway and traffic information, accessible
to the public and businesses. `part-of` [[NL-IENW]] — created the same
pass, closing what was recorded first as an anchor `part-of` [[NL]] edge.

## Founding partner of PDOK and NDW

[[NL-PDOK]]'s own file, reading `pdok.nl` directly, already established
that Rijkswaterstaat was one of the founding partners when PDOK launched
in **2013**, alongside [[NL-KADASTER]], several ministries and
[[NL-GEONOVUM]]. [[NL-NDW]]'s own file, reading `organisaties.overheid.nl`
directly, separately names Rijkswaterstaat among the government partners
in the National Data Warehouse for Traffic Information. Both edges are
now recorded on this entity's own side, closing the gap PDOK's file had
flagged — its founding collaboration no longer looks narrower than it
actually was.

## Relationships

- `part-of` [[NL-IENW]] — its parent ministry.
- `participates-in` [[NL-PDOK]] — founding partner since 2013.
- `participates-in` [[NL-NDW]] — named government partner.

## Sources

Listed in frontmatter. `en.wikipedia.org`'s account of [[NL-IENW]], read
directly the same pass, is also cited above.
