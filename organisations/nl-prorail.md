---
id: NL-PRORAIL
type: organisation
name: ProRail
alternative_names:
  - ProRail B.V.
description: >
  Dutch railway infrastructure manager, responsible for constructing,
  maintaining, managing and ensuring the safety of the entire Dutch
  railway network. Established 1 January 2005 from the merger of three
  predecessor rail organisations. A private limited company (besloten
  vennootschap) wholly owned, via the holding company Railinfratrust
  B.V., by the Dutch State. One of the bronhouders (data-source holders)
  of the Basisregistratie Grootschalige Topografie.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2005-01-01
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - NL
  - NL-BGT
  - NL-SVB-BGT
  - NL-RIJKSWATERSTAAT
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading nl.wikipedia.org's own article directly (2026-09-13): ProRail B.V. is wholly owned, via the holding company Railinfratrust B.V., by the Dutch State ('volledig eigendom van de Nederlandse Staat')."
    confidence: medium
    valid_from: 2005-01-01
    valid_until: null
  - type: participates-in
    target: NL-BGT
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #150: 'Rijkswaterstaat/ProRail/Defence/RVO as BGT bronhouders... remain unmodelled'). Confirmed by reading svb-bgt.nl's own homepage directly (already cited on [[NL-RIJKSWATERSTAAT]] and [[NL-SVB-BGT]]): 'Alle gemeenten, waterschappen, provincies, het Ministerie van Defensie, het Ministerie van Landbouw, Visserij, Voedselzekerheid en Natuur, ProRail en Rijkswaterstaat werken samen aan de BGT' — naming ProRail directly as one of the bronhouders (data-source holders) of the register."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "ProRail"
    url: "https://nl.wikipedia.org/wiki/ProRail"
    publisher: "Wikipedia"
    accessed: "2026-09-13"
  - title: "Homepage"
    url: "https://www.svb-bgt.nl/homepage/"
    publisher: "SVB-BGT"
    accessed: "2026-09-06"
---

# ProRail

> **Created 2026-09-13**, closing part of `discovery/unresolved.md` row
> #150. A dedicated Wikipedia article and SVB-BGT's own homepage (already
> cited on [[NL-RIJKSWATERSTAAT]] and [[NL-SVB-BGT]]) were both read
> directly. `prorail.nl` itself returned HTTP 403 on every path tried —
> a domain-wide block, not a one-off failure.

## Description

Confirmed by reading the Dutch Wikipedia article directly: ProRail is
the **rail infrastructure manager** for the Netherlands, responsible for
constructing, maintaining, managing and ensuring safety across the
entire Dutch railway network — 7,002 km of track, 2,305 level crossings,
6,078 switches and 399 stations, as well as capacity distribution among
freight and passenger operators and traffic control through twelve
traffic management centres.

## Legal form and ownership

ProRail B.V. is a **besloten vennootschap** (private limited company),
**formally established on 1 January 2005** from the merger of three
separate rail organisations that had operated under the holding company
Railinfratrust since 2000. It is wholly owned, via Railinfratrust B.V.,
by the **Dutch State** — a state-owned company rather than a ministry
department, matching the organisational type of [[NL-RIJKSWATERSTAAT]]
more than a government office.

## A named BGT bronhouder

Confirmed by reading svb-bgt.nl's own homepage directly: ProRail is
named directly, alongside Rijkswaterstaat, the Ministry of Defence and
others, as one of the seven bronhouder categories that jointly maintain
[[NL-BGT]], coordinated by [[NL-SVB-BGT]].

## Not modelled

- Railinfratrust B.V., the holding company through which the State's
  ownership is structured.
- The 2023 cabinet decision to convert ProRail into a *privaatrechtelijk
  zelfstandig bestuursorgaan* (private-law independent administrative
  body) — reported by trade press, not independently confirmed by a
  directly-read primary source this pass.

## Relationships

- `part-of` [[NL]] — anchor edge.
- `participates-in` [[NL-BGT]] — named bronhouder.

## Sources

Listed in frontmatter, both read directly 2026-09-13.
