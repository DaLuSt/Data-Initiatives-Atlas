---
id: EU-DATA-EUROPA-EU
type: platform
name: data.europa.eu
alternative_names:
  - The official portal for European data
  - European Data Portal
description: >
  The portal that gives access to open data from international, EU, national, regional, local and geo data portals. Its
  own "About" page says it replaces the EU Open Data Portal and the European Data Portal, collects the metadata of
  public data made available across Europe, and reports metadata errors back to the owners of the catalogues it
  harvests. Its footer names the Publications Office of the European Union as the manager of the site.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-14"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - EU-PUBLICATIONS-OFFICE
related_entities:
  - EU-DCAT-AP
  - EU-OPEN-DATA-DIRECTIVE
relationships:
  - type: maintained-by
    target: EU-PUBLICATIONS-OFFICE
    source: fact
    evidence: "The portal's page 'About data.europa.eu' (data.europa.eu/en/about/about-dataeuropaeu, HTML downloaded and read directly 2026-11-14): the footer reads 'This website is managed by:' followed by the logo and name 'Publications Office of the European Union'. The page does not say which legal act gives the Office that task."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: part-of
    target: EU
    source: fact
    evidence: "The same page, read directly 2026-11-14: 'The portal provides access to open data from international, EU, national, regional, local and geo data portals. It replaces the EU Open Data Portal and the European Data Portal.' and 'The portal collects the metadata of public data made available across Europe.'"
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About data.europa.eu"
    url: "https://data.europa.eu/en/about/about-dataeuropaeu"
    publisher: "data.europa.eu (Publications Office of the European Union)"
    accessed: "2026-11-14"
---

# data.europa.eu

> **Created 2026-11-14** (roadmap #771). Sourced from the portal's own "About" page, whose HTML was downloaded and read
> directly. Only that page was read: no launch date, no dataset count and no metadata standard is stated on it, so none
> is recorded here.

## What the page says

- **What it is.** "The portal provides access to open data from international, EU, national, regional, local and geo data
  portals. It replaces the EU Open Data Portal and the European Data Portal."
- **Its aim.** "Going beyond collecting metadata (data about data), the strategic objective of the portal is to improve
  accessibility and increase the value of open data."
- **Metadata quality.** "The portal collects the metadata of public data made available across Europe. The data
  catalogues of origin may contain datasets with errors. The service will assess these errors and communicate them back
  to the owners of the catalogues."
- **Who runs it.** The footer: "This website is managed by:" the Publications Office of the European Union
  ([[EU-PUBLICATIONS-OFFICE]]).

## Not established

- **Its links to the national portals.** The Atlas holds many of the portals it harvests ([[DE-GOVDATA]],
  [[FR-DATA-GOUV]], [[ES-DATOS-GOB-ES]], [[NL-DATA-OVERHEID]] and others), but the page read names none, so no edge is
  drawn from them. A harvesting list read from the portal would support `uses-data-from` or `participates-in` edges.
- **[[EU-DCAT-AP]].** The profile is described in the Atlas as enabling cross-portal dataset search; the page read does
  not mention it, so it is under `related_entities` only.
- **Legal basis.** Which act founds the portal was not read; [[EU-OPEN-DATA-DIRECTIVE]] is listed as related, not linked.

## Sources

Listed in frontmatter, read directly.
