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
verification: primary-source

start_date: 2013-01-01
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GEOSPATIAL
organisations:
  - NL-KADASTER
  - NL-GEONOVUM
  - NL-BZK
  - NL-RIJKSWATERSTAAT
  - NL-IENW
related_entities: []
relationships:
  - type: aligned-with
    target: EU-INSPIRE
    source: fact
    evidence: "Confirmed by reading pdok.nl's own pages directly (2026-08-27): 'PDOK diensten voldoen aan nationale en internationale standaarden, waaronder de Europese INSPIRE standaard, HVD en de Nederlandse e-overheidstandaarden,' and separately, PDOK positions itself as 'expert op het gebied van INSPIRE-eisen.' data.overheid.nl's own PDOK organisation page, also read directly, describes PDOK's Nationaal Georegister as 'dé vindplaats van geo-informatie van Nederland.' CAVEAT unchanged: the sources establish standards compliance and expertise, not that PDOK is formally designated as the INSPIRE network-service infrastructure for the Netherlands under the Implementatiewet — that designation was not found in any page read."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-BASISREGISTRATIES
    source: interpretation
    evidence: "PDOK publishes geodata including base-registration content; no page read this pass states a formal relationship between PDOK and the stelsel van basisregistraties. Atlas interpretation, unchanged this pass."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Over PDOK"
    url: "https://www.pdok.nl/over-pdok"
    publisher: "PDOK"
    accessed: "2026-08-27"
  - title: "Home — PDOK"
    url: "https://www.pdok.nl/"
    publisher: "PDOK"
    accessed: "2026-08-27"
  - title: "Publieke Dienstverlening op de Kaart"
    url: "https://data.overheid.nl/community/organization/pdok"
    publisher: "Overheid.nl"
    accessed: "2026-08-27"
---

# PDOK (Publieke Dienstverlening Op de Kaart)

> **Verified 2026-08-27.** All three cited pages read directly. Founding
> partners and the 2013 establishment are confirmed; PDOK's own pages also
> reveal it became independently operated by the Kadaster from 2018, a
> detail the prior text did not carry.

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
and [[NL-GEONOVUM]] — confirmed by reading pdok.nl's own "Over PDOK" page
directly this pass, which names the same partners. That page also states
that since 2018 "het Kadaster zelfstandig het dataportaal PDOK" operates —
the Kadaster took over independent operation of the platform, a detail not
previously recorded here.

**All named founding partners now modelled, 2026-09-05.**
[[NL-RIJKSWATERSTAAT]] and [[NL-IENW]] (the Ministry of Infrastructure
and Water Management) are both now separate Atlas entities, closing the
gap this section used to flag. [[NL-RIJKSWATERSTAAT]] carries its own
`participates-in` edge back to this platform, and is itself `part-of`
[[NL-IENW]].

`start_date: 2013-01-01` is a **placeholder for "in 2013"** — no precise
establishment date was located, and nothing read this pass supplied one.

## Relationships

- Founded and supported by [[NL-KADASTER]], [[NL-GEONOVUM]], [[NL-BZK]],
  [[NL-RIJKSWATERSTAAT]] and [[NL-IENW]] among others.
- Publishes geo-data related to [[NL-BASISREGISTRATIES]] (Atlas
  interpretation, `confidence: low`).

## Atlas interpretation

The link to the base-registry system is an Atlas reading, not a sourced
arrangement.

## Sources

Listed in frontmatter, all three read directly this pass — PDOK's own
"Over PDOK" and home pages, and its data.overheid.nl organisation listing.
