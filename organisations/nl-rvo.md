---
id: NL-RVO
type: organisation
name: Rijksdienst voor Ondernemend Nederland
name_en: "Netherlands Enterprise Agency"
alternative_names:
  - RVO
  - Netherlands Enterprise Agency
description: >
  Dutch executive agency of the Ministry of Economic Affairs and Climate,
  as its own site puts it, working for almost all ministries (Wikipedia
  also names the agriculture ministry as a parent), established 1 January
  2014 (the day from Wikipedia; RVO's own history page gives the year) from the merger of
  Dienst Regelingen and Agentschap NL. Administers subsidies, permits
  and international-business support for entrepreneurs, and represents
  the agricultural bronhouder interest on the board of the Stichting
  Samenwerkingsverband Bronhouders BGT.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2014-01-01
end_date: null
last_verified: "2026-11-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - NL
  - NL-EZK
  - NL-BGT
  - NL-SVB-BGT
relationships:
  - type: part-of
    target: NL-EZK
    source: fact
    evidence: "RVO's own 'Organisatie' page, read directly 2026-11-19 (page checked by RVO on 4 November 2026): 'We zijn een agentschap van het ministerie van Economische Zaken en Klimaat maar voeren opdrachten uit voor bijna alle ministeries, decentrale overheden en de EU.' Upgraded 2026-11-19 from an anchor `part-of` [[NL]], recorded from Wikipedia on 2026-09-13 with the remark that neither ministry was an Atlas entity; [[NL-EZK]] is one, and reaches [[NL]] itself, as [[NL-RIJKSWATERSTAAT]] reaches it through [[NL-IENW]]. Wikipedia also named the Ministry of Agriculture as a second parent ministry; RVO's page names only EZK, and says it works for almost all ministries. `valid_from` is empty: RVO's history page gives 'RVO bestaat sinds 2014' without a day, and when the agency came under the ministry in its present name was not read (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-BGT
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #150: 'Rijkswaterstaat/ProRail/Defence/RVO as BGT bronhouders... remain unmodelled'). Confirmed by reading svb-bgt.nl's own 'Bestuursleden' page directly (already cited on [[NL-SVB-BGT]]): the SVB-BGT board named a representative from RVO among the bronhouder categories' representatives, alongside the Unie van Waterschappen, Defensie, Rijkswaterstaat and IPO."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Onze geschiedenis"
    url: "https://www.rvo.nl/onderwerpen/over-ons/onze-geschiedenis"
    publisher: "Rijksdienst voor Ondernemend Nederland (rvo.nl)"
    accessed: "2026-11-19"
  - title: "Organisatie"
    url: "https://www.rvo.nl/over-ons/organisatie"
    publisher: "Rijksdienst voor Ondernemend Nederland (rvo.nl)"
    accessed: "2026-11-19"
  - title: "Rijksdienst voor Ondernemend Nederland"
    url: "https://nl.wikipedia.org/wiki/Rijksdienst_voor_Ondernemend_Nederland"
    publisher: "Wikipedia"
    accessed: "2026-09-13"
  - title: "Bestuursleden"
    url: "https://www.svb-bgt.nl/bestuursleden/"
    publisher: "SVB-BGT"
    accessed: "2026-09-06"
---

# Rijksdienst voor Ondernemend Nederland (RVO)

> **Created 2026-09-13**, closing part of `discovery/unresolved.md` row
> #150. A dedicated Wikipedia article and SVB-BGT's own "Bestuursleden"
> page (already cited on [[NL-SVB-BGT]]) were both read directly.
> `rvo.nl` returned only a page title with no substantive content to
> WebFetch — a JavaScript application, not a domain-wide block.

## Description

Confirmed by reading the Dutch Wikipedia article directly: RVO is an
executive agency ("baten-lastenagentschap") of the **Ministry of
Economic Affairs** and the **Ministry of Agriculture, Nature and Food
Quality**, established **1 January 2014** from the merger of Dienst
Regelingen and Agentschap NL. It administers subsidies, permits, patent
services and international-business support for entrepreneurs — as of
2023, over 6,000 civil servants across six locations and an annual
budget exceeding €825 million.

## A named BGT bronhouder representative

SVB-BGT's own "Bestuursleden" page, read directly (already cited on
[[NL-SVB-BGT]]'s own file), names RVO among the representatives sitting
on the board of the Stichting Samenwerkingsverband Bronhouders BGT — the
foundation coordinating the bronhouders (data-source holders) of
[[NL-BGT]]. Given RVO's affiliation with the Ministry of Agriculture,
Fisheries, Food Security and Nature — one of the register's named
bronhouder categories per svb-bgt.nl's own homepage — RVO functions as
that ministry's operational representative on the board, though no
source read states this division of labour explicitly.

## Not modelled

- Dienst Regelingen and Agentschap NL, RVO's two 2014 predecessor
  organisations.
- The Ministry of Economic Affairs and the Ministry of Agriculture,
  Nature and Food Quality themselves, matching the Atlas's convention
  of not modelling ministries as their own entities.

## Relationships

- `part-of` [[NL-EZK]] — "een agentschap van het ministerie van Economische Zaken en Klimaat", on RVO's own
  page (read 2026-11-19); upgraded from an anchor `part-of` [[NL]], as [[NL-RIJKSWATERSTAAT]] was.
- `participates-in` [[NL-BGT]] — named board representative, via
  [[NL-SVB-BGT]].

## Sources

Listed in frontmatter, both read directly 2026-09-13.
