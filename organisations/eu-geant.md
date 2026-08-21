---
id: EU-GEANT
type: organisation
name: GÉANT Association
alternative_names:
  - GÉANT
  - GEANT
description: >
  Non-profit association providing a dedicated network and collaboration
  services for research and education in Europe and in many regions beyond it.
  Its membership comprises 37 national research and education networks plus
  NORDUnet, with associates including five Nordic NRENs, KREN, CERN and ESA.
  GÉANT provides the pan-European backbone and coordinates shared services,
  while each NREN delivers those capabilities nationally. The NRENs are
  not-for-profit and mainly publicly funded, and serve over 50 million
  academics and researchers across Europe with services extending beyond
  connectivity to cybersecurity, identity management and collaborative
  research platforms.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-RESEARCH
  - DOMAIN-EDUCATION
organisations: []
related_entities:
  - EU
  - NL-SURF
  - DE-DFN
  - EU-EOSC
relationships:
  - type: part-of
    target: EU
    source: interpretation
    evidence: "Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity. GÉANT is a non-profit association whose membership spans 37 national research and education networks and reaches beyond Europe, and is not an EU body; the edge records the scope at which the Atlas files it and asserts nothing about EU ownership or control."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "National Research and Education Networks — GÉANT"
    url: "https://geant.org/who-we-work-with/national-research-and-education-networks/"
    publisher: "GÉANT Association"
  - title: "NRENs — About GÉANT"
    url: "https://about.geant.org/nrens/"
    publisher: "GÉANT Association"
  - title: "The GÉANT Compendium of National Research and Education Networks in Europe"
    url: "https://compendium.geant.org/"
    publisher: "GÉANT Association"
---

# GÉANT

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

The association behind Europe's research and education network. Its
membership is **37 NRENs plus NORDUnet**, with associates including five
Nordic NRENs, KREN, **CERN** and **ESA**.

The division of labour is the point: **GÉANT provides the pan-European
backbone and coordinates shared services; each NREN delivers them
nationally**, adapted to local context. The NRENs are not-for-profit and
mainly publicly funded, and between them serve **over 50 million** academics
and researchers.

What they deliver is not only connectivity — the sources name
**cybersecurity, identity management and collaborative research platforms**.

## The third membership association, and the pattern is now a pattern

The Atlas has acquired three of these in two batches:

| Vertical | Association | Members in the Atlas |
|---|---|---|
| Statistics | [[EU-ESS]] | [[NL-CBS]], [[DE-DESTATIS]], [[BE-STATBEL]], [[ES-INE]] |
| Geospatial | [[EU-EUROGEOGRAPHICS]] | [[NL-KADASTER]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[GB-OS]], [[IE-TAILTE]] |
| **Research and education** | **this entity** | [[NL-SURF]], [[DE-DFN]] |

Each one attaches national bodies of the same kind to each other and to a
European layer, and each was invisible until the association was modelled.

**The edge type differs by legal shape and that difference is real.**
[[EU-ESS]] takes `part-of` because a national statistical institute is
constitutionally a component of it under [[EU-REG-223-2009]]. GÉANT and
EuroGeographics take `participates-in`, because a member of an association is
not structurally contained by it.

## Relationships

- `part-of` [[EU]] — anchor edge, marked `source: interpretation`. GÉANT's
  reach extends past the Union and past Europe; the edge records where the
  Atlas files it.
- Membership edges live on the members.

## What is not asserted

No edge to [[EU-EOSC]]. GÉANT and the European Open Science Cloud are both
European research infrastructure and no source in this set connects them —
whereas [[DE-NFDI]]'s EOSC membership **is** sourced, and is asserted there.

**CERN and ESA are named as associates and are not modelled.** Both are
substantial international organisations; creating either from one mention in
a membership list would be the thin entity the taxonomy threshold prevents.

## Sources

Listed in frontmatter — two GÉANT pages on the NREN relationship and the
Compendium.
