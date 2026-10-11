---
id: NL-DEFENSIE
type: organisation
name: Ministerie van Defensie
name_en: "Ministry of Defence"
alternative_names:
  - Defensie
  - Ministry of Defence
description: >
  Dutch ministry of defence. The Atlas records it only for its role as one of
  the seven bronhouder (source holder) categories of the Basisregistratie
  Grootschalige Topografie, the national large-scale topographic map.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-GEOSPATIAL
organisations: []
related_entities:
  - NL-BGT
  - NL-SVB-BGT
relationships:
  - type: part-of
    target: NL
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. svb-bgt.nl's own homepage, read directly (2026-10-11), names 'het Ministerie van Defensie' among the Dutch government bodies that work together on the BGT."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-BGT
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #150, the last of the seven BGT bronhouder categories to be modelled. svb-bgt.nl's own homepage, read directly (2026-10-11): 'Alle gemeenten, waterschappen, provincies, het Ministerie van Defensie, het Ministerie van Landbouw, Visserij, Voedselzekerheid en Natuur, ProRail en Rijkswaterstaat werken samen aan de BGT'; the page describes them as bronhouders working through the SVB-BGT partnership. It gives the Ministry no more specific role."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Homepage"
    url: "https://www.svb-bgt.nl/homepage/"
    publisher: "SVB-BGT"
    accessed: "2026-10-11"
    note: "Read directly; the only source for this entity's role."
---

# Ministerie van Defensie

> **Created 2026-10-11** (roadmap #536, `discovery/unresolved.md` row #150).
> The row said the Ministry was left out because the Atlas does not model
> ministries in their own right. It does: [[NL-BZK]], [[NL-EZK]] and
> [[NL-IENW]] are entities, so that convention did not exist and is lifted.

## Description

One of the seven categories of bronhouder of [[NL-BGT]], alongside the
municipalities, provinces, water boards, [[NL-RIJKSWATERSTAAT]],
[[NL-PRORAIL]] and the agricultural bronhouder, represented by [[NL-RVO]].
They coordinate through [[NL-SVB-BGT]].

This entity is deliberately thin. The only source read says the Ministry is a
bronhouder and gives no detail of which part of the map it holds; the
Ministry's own site (`defensie.nl`) answered with a redirect page only.

## Relationships

- `part-of` NL (anchor edge).
- `participates-in` [[NL-BGT]].
