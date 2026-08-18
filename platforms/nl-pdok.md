---
id: NL-PDOK
type: platform
name: Publieke Dienstverlening Op de Kaart
alternative_names:
  - PDOK
description: >
  Dutch platform providing geodatasets from government authorities as data
  services and files. PDOK services are based on open data and are freely
  available. Established in 2013 as a collaboration between the Kadaster,
  several ministries, Rijkswaterstaat and Geonovum.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2013-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-KADASTER
  - NL-GEONOVUM
  - NL-BZK
related_entities: []
relationships:
  - type: aligned-with
    target: EU-INSPIRE
    source: fact
    evidence: "PDOK services comply with national and international standards, including the European INSPIRE standard, HVD and Dutch e-government standards; PDOK is the platform providing geodatasets from Dutch government authorities via geo-webservices and OGC APIs, and Kadaster has independently operated the portal since 2018 (pdok.nl/over-pdok; kadaster.nl 'PDOK - platform voor open data'; opennederland.nl 'PDOK'). NOT READ — search-only. CAVEAT: the sources establish standards compliance, not that PDOK is the designated INSPIRE network-service infrastructure for the Netherlands under the Implementatiewet."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: interpretation
    evidence: "PDOK publishes geodata including base-registration content; no source directly states a formal relationship between PDOK and the stelsel van basisregistraties. Atlas interpretation."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Over PDOK"
    url: "https://www.pdok.nl/over-pdok"
    publisher: "PDOK"
  - title: "Home — PDOK"
    url: "https://www.pdok.nl/"
    publisher: "PDOK"
  - title: "Publieke Dienstverlening op de Kaart"
    url: "https://data.overheid.nl/community/organization/pdok"
    publisher: "Overheid.nl"
---

# PDOK (Publieke Dienstverlening Op de Kaart)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

PDOK is the Dutch platform for making geodatasets from government
authorities available, serving both public and private sector users. It
publishes digital geo-information as data services and as files. PDOK
services are based on open data and are therefore freely available to
everyone, and any government organisation wanting to make its geodata
reusable can approach PDOK.

It was established in 2013 as a collaboration between [[NL-KADASTER]], the
ministries of Infrastructure and Water Management, the Interior and Kingdom
Relations, and Economic Affairs and Climate, together with Rijkswaterstaat
and [[NL-GEONOVUM]].

Two of the named founding partners — the Ministry of Infrastructure and
Water Management and Rijkswaterstaat — are not yet Atlas entities and are
queued in `discovery/research-queue.md`. `organisations:` therefore lists
only the partners that exist, which makes the founding collaboration look
narrower than it was; the full list is recorded in this prose.

`start_date: 2013-01-01` is a **placeholder for "in 2013"** — no precise
establishment date was located.

## Relationships

- Founded and supported by [[NL-KADASTER]], [[NL-GEONOVUM]] and [[NL-BZK]]
  among others.
- Publishes geo-data related to [[NL-BASISREGISTRATIES]] (Atlas
  interpretation, `confidence: low`).

## Atlas interpretation

The link to the base-registry system is an Atlas reading, not a sourced
arrangement.

## Sources

Listed in frontmatter.
