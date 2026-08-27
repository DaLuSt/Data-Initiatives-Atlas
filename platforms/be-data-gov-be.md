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
last_verified: "2026-08-27"
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
    evidence: "The DCAT-AP feed is uploaded via the federal open data portal, which is managed by FOD BOSA; BOSA publishes the portal as one of its applications and documents its metadata integration services (financien.belgium.be 'Open data: DCAT-AP feed'; bosa.belgium.be 'Federale open data portaal'). Not confirmed this pass — every one of the five cited pages, including a re-attempt at the data.europa.eu factsheet as a PDF, returned either a CAPTCHA challenge or an unreadable binary stream."
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
  - title: "Fedict/dcattools — README"
    url: "https://github.com/Fedict/dcattools/blob/master/README.md"
    publisher: "GitHub (Fedict)"
    accessed: "2026-08-27"
  - title: "Open Government, Belgium API"
    url: "https://publicapis.io/open-government-belgium-api"
    publisher: "Public APIs Directory"
    accessed: "2026-08-27"
---

# data.gov.be

> **Re-checked 2026-08-27, still `search-only`.** All five originally
> cited sources remain unreadable, confirmed again this pass. Two
> previously-uncited pages were found via search and read directly this
> pass — GitHub's own `Fedict/dcattools` README (GitHub is not part of
> the Belgian government's blocked web presence) and a third-party API
> directory's description of data.gov.be — giving genuine new technical
> and descriptive detail. That is 2 of 7 sources, still short of a
> majority: the block across the Belgian federal open-data web presence
> remains near-total, the same class of finding as bot-walled `.gouv.fr`
> domains in the France batch.

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

Confirmed by reading GitHub's own `Fedict/dcattools` README directly
(2026-08-27) — genuinely readable, unlike every `belgium.be` and
`data.gov.be` page tried for this entity — the harvesting pipeline works
by scraping Belgian open data portals, running SPARQL scripts to enrich
raw DCAT into DCAT-AP, uploading the enriched files to data.gov.be, then
consolidating everything into N-Triples and XML for weekly transmission
to the European Data Portal. This is the mechanical detail behind the
"DCAT-AP feed" this entity's description already named.

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

Two of seven readable this pass — GitHub's `Fedict/dcattools` README and
publicapis.io's description. All five originally cited sources remain
unreadable: three CAPTCHA-walled pages (`bosa.belgium.be`, `data.gov.be`
twice) and one bot-walled page (`financien.belgium.be`), plus one PDF
(`data.europa.eu`) whose content could not be extracted as text.
