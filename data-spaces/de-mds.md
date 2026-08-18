---
id: DE-MDS
type: data-space
name: Mobility Data Space
alternative_names:
  - MDS
description: >
  Operating data space open to all actors in the mobility sector,
  describing itself as a fair data-sharing community. It connects those who
  offer mobility data with those who need it, functioning as a marketplace
  in which mobility-relevant data can be traded securely, fairly and
  transparently while preserving intellectual property rights, and promotes
  cross-sectoral data-driven collaboration between transport undertakings,
  the automotive industry, mobility service providers and municipalities.

level: sectoral
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - DE
  - DE-MOBILITHEK
  - EU-EMDS
relationships:
  - type: applies-in
    target: DE
    source: fact
    evidence: "The Mobility Data Space is a German data space for the mobility sector, promoting cross-sectoral data-driven collaboration between transport undertakings, the automotive industry, mobility service providers and municipalities (mobility-dataspace.eu; bmdv.bund.de). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Mobility Data Space"
    url: "https://www.mobility-data-space.de/"
    publisher: "Mobility Data Space"
  - title: "Mobility Data Space — Data Sharing Community"
    url: "https://mobility-dataspace.eu/"
    publisher: "Mobility Data Space"
  - title: "Der Mobility Data Space"
    url: "https://www.bmv.de/SharedDocs/DE/Artikel/DG/mobility-data-space.html"
    publisher: "Bundesministerium für Verkehr (BMV)"
  - title: "Mobility Data Space: Marktplatz für Mobilitätsdaten"
    url: "https://aftermarket-trends.de/mobility-data-space-marktplatz-fuer-mobilitaetsdaten/"
    publisher: "aftermarket-trends.de"
---

# Mobility Data Space (MDS)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Mobility Data Space is an operating data space available to all actors
in the mobility sector, describing itself as a **fair data sharing
community** for those who want to make tomorrow's mobility more
environmentally friendly, safer and more user-friendly.

It networks those who **offer** mobility data with those who **need** it to
develop new business models, and promotes cross-sectoral data-driven
collaboration between transport undertakings, the automotive industry,
mobility service providers and municipalities.

Its distinguishing feature against [[DE-MOBILITHEK]] is stated directly in
the sources: while the Mobilithek primarily makes **open and legally
published data** available, the MDS is a **data marketplace** where
mobility-relevant data can be traded securely, fairly and transparently
while preserving intellectual property rights. The full link between the
two was established in the first half of 2025.

## Open data and traded data as two entities

The Mobilithek/MDS pair is the cleanest illustration in the Atlas of a
distinction the Dutch layer does not draw explicitly: a **national access
point publishing open data** and a **commercial data space trading
proprietary data** are different things, serving overlapping communities
through different legal and economic arrangements.

The Netherlands has [[NL-NDW]] and [[NL-NTM]] on the open side and
[[NL-DSGO]] and [[NL-ISHARE]] in the agreement-system space, but no source
in the Dutch batches drew the line as sharply as the German sources do
here. **No relationship to any Dutch entity is asserted.**

## The EU mobility data space link is not asserted

[[EU-EMDS]] — the common European mobility data space — is the obvious
parent to look for, and this is exactly the pairing the Atlas already
refused once: Batch 10 examined [[EU-EMDS]] → [[NL-NTM]] and declined it
for want of a source.

The refusal is repeated here for the same reason. Every source read
describes the MDS in national and sectoral terms; **none names the European
mobility data space**. `related_entities` records the association for
navigation without asserting a relationship.

Two national mobility data spaces now sit unconnected to their apparent
European parent. That is a visible hole rather than a hidden one, and it is
logged in `discovery/unresolved.md`.

## Relationships

**None asserted.** This entity is currently reachable only through
`related_entities` and `countries/de/index.md`.

That makes it the **least-connected German entity in this batch**, and the
Atlas has treated that as a defect before: Batch 6 found [[NL-ISHARE]]
fully disconnected and fixed it with an explicitly-labelled interpretation
link. The same remedy was considered here — an interpretation-grade
`related-to` [[DE-MOBILITHEK]] — and **rejected**, because unlike the
iSHARE/DSGO case the sources actively distinguish these two platforms
rather than merely failing to connect them. Manufacturing a link between
two things a source contrasts would be worse than leaving the node thin.

## Sources

Listed in frontmatter, including the transport ministry's own page on the
MDS.
