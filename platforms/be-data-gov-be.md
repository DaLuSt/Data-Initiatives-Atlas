---
id: BE-DATA-GOV-BE
type: platform
name: data.gov.be
alternative_names:
  - Federaal open data portaal
  - Belgian federal open data portal
description: >
  Belgium's federal open data portal, managed by FOD BOSA. It collects
  metadata about open datasets — title, description, links to downloadable
  files — harvested automatically from government services so publishers do
  not have to re-enter it, and exposes a DCAT-AP feed. Because the
  participating portals follow common IT standards, one portal can retrieve
  another's content automatically, and European portals reproduce at least
  part of the federal and national portals' content.

level: national
country: BE
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
  - BE-BOSA
related_entities:
  - BE-DCAT-AP-BE
  - NL-DATA-OVERHEID
  - DE-GOVDATA
relationships:
  - type: maintained-by
    target: BE-BOSA
    source: fact
    evidence: "The DCAT-AP feed is uploaded via the federal open data portal, which is managed by FOD BOSA; BOSA publishes the portal as one of its applications and documents its metadata integration services (financien.belgium.be 'Open data: DCAT-AP feed'; bosa.belgium.be 'Federale open data portaal'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Federale open data portaal"
    url: "https://bosa.belgium.be/nl/applications/federale-open-data-portaal"
    publisher: "FOD Beleid en Ondersteuning (BOSA)"
  - title: "Presentaties | Data.gov.be"
    url: "https://data.gov.be/nl/presentaties"
    publisher: "data.gov.be"
  - title: "Open data best practices (Open Data Task Force, 04/2023)"
    url: "https://data.gov.be/sites/default/files/content/opendatabestpractices_202304_nl.pdf"
    publisher: "data.gov.be / FOD BOSA — Open Data Task Force"
  - title: "Open data: DCAT-AP feed"
    url: "https://financien.belgium.be/nl/Statistieken_en_analysen/operationele-cijfers/open-data-dcat-ap-feed"
    publisher: "FOD Financiën"
  - title: "Open Data Maturity 2025 — factsheet Belgium"
    url: "https://data.europa.eu/sites/default/files/2025-12/2025_odm_factsheet_belgium.pdf"
    publisher: "data.europa.eu (Publications Office of the European Union)"
---

# data.gov.be

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

data.gov.be is Belgium's **federal open data portal**, managed by
[[BE-BOSA]]. It collects **metadata** about open datasets — title, short
description, links to downloadable files — **harvested automatically from
government services**, so publishers are not asked to re-enter what they
have already published. It exposes a **DCAT-AP feed**, and applies
[[BE-DCAT-AP-BE]].

Because the participating portals follow common IT standards, one portal
can automatically retrieve another's content, and European portals
reproduce at least part of the federal and national portals' content. A new
version of the portal was launched alongside the publication of
**high-value datasets**, with metadata-quality work including **SHACL
validation** and the mapping of non-DCAT metadata to DCAT-AP.

## Three national open data portals

| Country | Portal | Institutional basis |
|---|---|---|
| Belgium | **data.gov.be** | managed by a federal support service ([[BE-BOSA]]) |
| Germany | [[DE-GOVDATA]] | a **Verwaltungsvereinbarung** acceded to by the federation and all sixteen Länder |
| Netherlands | [[NL-DATA-OVERHEID]] | an ordinary central government service |

The German entity notes that the same function needs an interstate
agreement in one country and a plain government service in another. Belgium
is the useful third data point, and it does **not** fall neatly on either
side: Belgium is federal like Germany, but its federal portal is run by a
federal service, with the Regions running their own portals that are
harvested rather than governed.

That is a real finding about federal states — federalism does not dictate
one architecture for shared infrastructure — and it is only visible with
three countries. **No relationship between the three portals is asserted.**

## What is not modelled

The **regional portals** that data.gov.be harvests from — Flemish, Walloon
and Brussels — are not Atlas entities, for the reason given in
`countries/be/be.md`: there is no level for a Belgian Region. A portal
described in its own sources as aggregating across levels is therefore
recorded with only one of those levels present.

## Relationships

- Maintained by [[BE-BOSA]].

Inbound: [[BE-DCAT-AP-BE]] `applies-to` this portal.

**No relationship to [[BE-HERGEBRUIK-WET]] is asserted**, the same call
made for [[DE-GOVDATA]] and [[DE-DNG]]: the open data act and the open data
portal are obviously related, and no source read states the relationship.

## Sources

Listed in frontmatter, including the European Open Data Maturity factsheet
for Belgium.
