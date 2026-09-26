---
id: EU-EDM
type: standard
name: Europeana Data Model
alternative_names:
  - EDM
description: >
  RDF-based semantic data model created in 2010 and maintained by the
  Europeana Foundation, used to aggregate and harmonise cultural
  heritage metadata contributed to Europeana by thousands of
  institutions across Europe. It replaced an earlier, Dublin
  Core-based approach (Europeana Semantic Elements) that proved
  inadequate for representing complex cultural-heritage relationships.
  EDM reuses many Dublin Core Terms properties for basic descriptive
  metadata while adding richer semantic-web relationships between
  cultural heritage objects and contextual resources (persons, places,
  concepts, events), and is designed to accommodate established
  domain-specific standards such as LIDO (museums), EAD (archives) and
  METS (digital libraries) rather than replacing them.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2010-01-01
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-EUROPEANA-FOUNDATION
related_entities:
  - EU-CULTURAL-HERITAGE-DATA-SPACE
  - INTL-DCAT
relationships:
  - type: maintained-by
    target: EU-EUROPEANA-FOUNDATION
    source: fact
    evidence: "Closes a gap EU-CULTURAL-HERITAGE-DATA-SPACE's own file had flagged (not a numbered discovery/unresolved.md row: EDM 'would connect to the Atlas's metadata-standards layer around INTL-DCAT' but was not independently researched). Confirmed by reading europeana.atlassian.net's own Europeana Knowledge Base page on EDM directly (2026-09-26, pro.europeana.eu itself remains 403-blocked as already recorded on EU-CULTURAL-HERITAGE-DATA-SPACE): EDM is 'developed collaboratively with technical experts, especially from the EuropeanaTech community' and 'continues to evolve through community-driven processes coordinated by Europeana.' The Dublin Core Metadata Initiative's own Metadata Standards Index, also read directly, independently states 'EDM is maintained by the Europeana Foundation, based in The Hague, Netherlands,' gives its creation year (2010) and version history (5.2.8 in October 2017), and confirms it is RDF-based and 'reuses many Dublin Core Terms properties.'"
    confidence: high
    valid_from: "2010-01-01"
    valid_until: null
  - type: related-to
    target: INTL-DCAT
    source: interpretation
    evidence: "Neither source read this pass states a direct relationship between EDM and DCAT specifically -- the Dublin Core Metadata Initiative's own page notes EDM's Dublin Core Terms reuse but 'doesn't mention DCAT.' Both are RDF-based, semantic-web metadata frameworks reusing Dublin Core vocabulary for cultural/dataset description respectively, which is why this entity sits in the same metadata-standards family the Atlas already models around INTL-DCAT -- but recorded as `source: interpretation`, `confidence: low` rather than a stated fact, since no source connects them directly."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Europeana Data Model"
    url: "https://europeana.atlassian.net/wiki/spaces/EF/pages/2916974597/Europeana+Data+Model"
    publisher: "Europeana Foundation — Europeana Knowledge Base"
    accessed: "2026-09-26"
  - title: "Europeana Data Model (EDM)"
    url: "https://msi.dublincore.org/standards/europeana-data-model/"
    publisher: "Dublin Core Metadata Initiative — Metadata Standards Index"
    accessed: "2026-09-26"
---

# Europeana Data Model (EDM)

> **Created 2026-09-26**, closing a gap [[EU-CULTURAL-HERITAGE-DATA-SPACE]]'s
> own file had flagged (graph completion, not a numbered
> `discovery/unresolved.md` row). Sourced from the Europeana Foundation's
> own knowledge base and the Dublin Core Metadata Initiative's Metadata
> Standards Index, both read directly — `pro.europeana.eu` itself
> remains 403-blocked, as already recorded on
> [[EU-CULTURAL-HERITAGE-DATA-SPACE]].

## Description

EDM is an **RDF-based semantic data model**, **created in 2010**, used to
**aggregate and harmonise cultural heritage metadata** contributed to
Europeana by thousands of institutions across Europe. Confirmed
independently on the Dublin Core Metadata Initiative's own Metadata
Standards Index: EDM **replaced an earlier, Dublin Core-based approach**
(Europeana Semantic Elements) that proved inadequate for representing
complex cultural-heritage relationships, and reached **version 5.2.8 in
October 2017**.

It **reuses many Dublin Core Terms properties** for basic descriptive
metadata, while adding richer semantic-web relationships linking
cultural heritage objects to contextual resources — persons, places,
concepts, events. Confirmed on Europeana's own knowledge base: it is
designed to accommodate established domain-specific standards — **LIDO**
(museums), **EAD** (archives), **METS** (digital libraries) — rather than
replacing them.

## Maintained by the Europeana Foundation

Confirmed directly on the Dublin Core Metadata Initiative's page: "EDM is
maintained by the [[EU-EUROPEANA-FOUNDATION]], based in The Hague,
Netherlands." Europeana's own knowledge base independently confirms it
"continues to evolve through community-driven processes coordinated by
Europeana," developed with "technical experts, especially from the
EuropeanaTech community."

## No stated link to DCAT, and none inferred

Neither source read states a direct connection to [[INTL-DCAT]]
specifically — the Dublin Core Metadata Initiative's page notes EDM's
Dublin Core Terms reuse but does not mention DCAT. Both frameworks sit in
the same RDF/Dublin-Core-derived metadata-standards family, which is why
this entity is placed near [[INTL-DCAT]] in the graph, but the edge is
recorded at `source: interpretation`, `confidence: low` rather than
asserted as fact.

## Not modelled

- **Dublin Core** / the **Dublin Core Metadata Initiative (DCMI)** as a
  separate Atlas entity — referenced here only as EDM's own source
  vocabulary and as this entity's independent secondary source.
- **LIDO**, **EAD** and **METS**, the domain-specific standards EDM
  accommodates — not independently researched this pass.

## Relationships

- `maintained-by` [[EU-EUROPEANA-FOUNDATION]] — `confidence: high`.
- `related-to` [[INTL-DCAT]] — `confidence: low`, no direct source
  connects them.

## Sources

Listed in frontmatter, both read directly.
