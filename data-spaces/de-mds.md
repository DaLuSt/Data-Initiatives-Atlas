---
id: DE-MDS
type: data-space
name: Mobility Data Space
alternative_names:
  - MDS
description: >
  Operating data space open to all actors in the mobility sector, run by
  DRM Datenraum Mobilität GmbH (evolved from an acatech Foundation project)
  and describing itself as a fair data-sharing community. It connects those
  who offer mobility data with those who need it, functioning as a
  marketplace in which mobility-relevant data can be traded securely,
  fairly and transparently while preserving intellectual property rights,
  and promotes cross-sectoral data-driven collaboration between transport
  undertakings, the automotive industry, mobility service providers and
  municipalities. Its infrastructure is compatible with the IDSA and
  Gaia-X.

level: sectoral
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading mobility-dataspace.eu and mobility-data-space.de directly (2026-08-28): the Mobility Data Space is a German data space for the mobility sector, run by DRM Datenraum Mobilität GmbH and funded by Germany's Federal Ministry for Transport, connecting organisations seeking mobility data with those wanting to license their data assets and promoting cross-sectoral data-driven collaboration between transport undertakings, the automotive industry, mobility service providers and municipalities. aftermarket-trends.de, also read directly, confirms it is 'supported by Germany's Federal Ministry for Digital Affairs and Transport.' The originally-cited bmv.de URL 404s on direct fetch (retried once) despite appearing in search results, and is treated as dead rather than silently dropped. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Mobility Data Space"
    url: "https://www.mobility-data-space.de/"
    publisher: "Mobility Data Space"
    accessed: "2026-08-28"
  - title: "Mobility Data Space — Data Sharing Community"
    url: "https://mobility-dataspace.eu/"
    publisher: "Mobility Data Space"
    accessed: "2026-08-28"
  - title: "Der Mobility Data Space"
    url: "https://www.bmv.de/SharedDocs/DE/Artikel/DG/mobility-data-space.html"
    publisher: "Bundesministerium für Verkehr (BMV)"
  - title: "Mobility Data Space: Marktplatz für Mobilitätsdaten"
    url: "https://aftermarket-trends.de/mobility-data-space-marktplatz-fuer-mobilitaetsdaten/"
    publisher: "aftermarket-trends.de"
    accessed: "2026-08-28"
---

# Mobility Data Space (MDS)

> **Re-verified 2026-08-28.** Three of four cited pages loaded directly.
> The fourth — `bmv.de`'s own MDS article — returned a genuine HTTP 404 on
> two separate attempts despite the URL appearing indexed in search
> results, and is treated as dead rather than silently dropped (no working
> BMV replacement URL for this specific article was found; other BMV pages
> on related MDS/mobility-data topics do resolve, so the ministry's domain
> is not wholesale blocked, just this one path). Three of four is a
> genuine majority. `verification: primary-source`.

## Description

The Mobility Data Space is an operating data space available to all actors
in the mobility sector, run by **DRM Datenraum Mobilität GmbH** — confirmed
directly this pass on mobility-dataspace.eu, which describes DRM as a
non-profit holding company that evolved from an acatech Foundation project,
with three managing directors overseeing technology, market/community and
governance. It describes itself as a **fair data sharing community** for
those who want to make tomorrow's mobility more environmentally friendly,
safer and more user-friendly.

It networks those who **offer** mobility data with those who **need** it to
develop new business models. aftermarket-trends.de, read directly, quotes
MDS CEO Michael Schäfer: trading partners negotiate data-sharing terms
among themselves ("Wer wem welche Daten zu welchen Konditionen zur
Verfügung stellt, machen die jeweiligen Handelspartner untereinander aus")
— the MDS itself acts as a **neutral intermediary**, providing a dataset
catalogue and a protected exchange environment rather than owning the data
traded on it. Its infrastructure is confirmed as compatible with **IDSA**
and **Gaia-X** standards.

Its distinguishing feature against [[DE-MOBILITHEK]] is confirmed directly
by aftermarket-trends.de: Mobilithek (which it dates to launch in July
2022) focuses on **open, publicly mandated data**, while the MDS handles
**proprietary mobility data** traded commercially. mobility-dataspace.eu,
also read directly, confirms the full link between the two platforms was
established in early 2025.

## Open data and traded data as two entities

The Mobilithek/MDS pair is the cleanest illustration in the Atlas of a
distinction the Dutch layer does not draw explicitly: a **national access
point publishing open data** and a **commercial data space trading
proprietary data** are different things, serving overlapping communities
through different legal and economic arrangements. This pass's direct
reading of aftermarket-trends.de sharpens that distinction with an
on-record CEO quote rather than search-snippet paraphrase.

The Netherlands has [[NL-NDW]] and [[NL-NTM]] on the open side and
[[NL-DSGO]] and [[NL-ISHARE]] in the agreement-system space, but no source
in the Dutch batches drew the line as sharply as the German sources do
here. **No relationship to any Dutch entity is asserted.**

## The EU mobility data space link is not asserted

[[EU-EMDS]] — the common European mobility data space — is the obvious
parent to look for, and this is exactly the pairing the Atlas already
refused once: Batch 10 examined [[EU-EMDS]] → [[NL-NTM]] and declined it
for want of a source.

The refusal is repeated here for the same reason, and this pass's direct
reads do not change it: mobility-dataspace.eu and mobility-data-space.de,
both read this pass, describe the MDS in national and sectoral terms;
**neither names the European mobility data space**. `related_entities`
records the association for navigation without asserting a relationship.

Two national mobility data spaces now sit unconnected to their apparent
European parent. That is a visible hole rather than a hidden one, and it is
logged in `discovery/unresolved.md`.

## Relationships

- `applies-in` [[DE]] — confirmed directly this pass, `confidence: high`.

That makes it, as before, one of the least-connected German entities in
this batch, and the Atlas has treated that as a defect elsewhere: Batch 6
found [[NL-ISHARE]] fully disconnected and fixed it with an
explicitly-labelled interpretation link. The same remedy was considered
here — an interpretation-grade `related-to` [[DE-MOBILITHEK]] — and
**rejected**, because unlike the iSHARE/DSGO case the sources actively
distinguish these two platforms rather than merely failing to connect
them. Manufacturing a link between two things a source contrasts would be
worse than leaving the node thin.

## Sources

Listed in frontmatter. Three of four read directly this pass; `bmv.de`'s
specific MDS article is confirmed dead (404 on two attempts) and is kept in
the list with that status noted here rather than silently removed, since no
equivalent replacement URL on the ministry's own domain was found.
