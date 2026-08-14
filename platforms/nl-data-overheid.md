---
id: NL-DATA-OVERHEID
type: platform
name: data.overheid.nl
alternative_names:
  - Dataregister van de Nederlandse Overheid
  - Nationaal Dataportaal
description: >
  The Dutch national open data portal, where data made available by
  government bodies can be found. More than 180 government organisations
  publish data through it. Datasets are described using the DCAT metadata
  standard.

level: national
country: NL
region: null

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
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-WHO
relationships:
  - type: depends-on
    target: NL-DCAT-AP-NL
    source: fact
    evidence: "Datasets on data.overheid.nl are described with metadata using DCAT; DCAT is used by data.overheid.nl among other platforms (data.overheid.nl; geonovum.nl DCAT-AP-NL pages). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Dataregister van de Nederlandse Overheid"
    url: "https://data.overheid.nl/"
    publisher: "Overheid.nl"
  - title: "Data.overheid.nl"
    url: "https://www.opennederland.nl/platforms/data-overheid/"
    publisher: "Vereniging Open Nederland"
---

# data.overheid.nl

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

data.overheid.nl is the national data portal of the Dutch government, where
data made available by government bodies can be found. More than 180
government organisations publish data through it.

Its datasets are described with metadata so they can be presented clearly
and searched in a targeted way, using DCAT — which is where this platform
connects to the standards layer: the Dutch profile [[NL-DCAT-AP-NL]] is what
makes those descriptions interoperable with other Dutch catalogues and with
European data catalogues.

It is also the operational counterpart to [[NL-WHO]]: the re-use obligations
in that act, including the designation of high-value datasets, are what this
portal exists to serve. The precise legal relationship was not sourced, so
no relationship is asserted beyond the association.

The portal's operator was not established from the sources located. The
`organisations: [NL-BZK]` entry reflects BZK's general open-data policy
responsibility and is an **Atlas association, not a sourced operator
claim**; it should be corrected on re-verification.

## Relationships

- Depends on [[NL-DCAT-AP-NL]] for dataset metadata.
- Serves the re-use regime established by [[NL-WHO]].

## Sources

Listed in frontmatter.
