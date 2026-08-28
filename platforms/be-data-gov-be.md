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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "The DCAT-AP feed is uploaded via the federal open data portal, which is managed by FOD BOSA; BOSA publishes the portal as one of its applications and documents its metadata integration services (financien.belgium.be 'Open data: DCAT-AP feed'; bosa.belgium.be 'Federale open data portaal'). Confirmed by reading GitHub's own Fedict/dcat README directly (2026-08-28): the repository holds 'Metadata being used to update the Belgian data.gov.be portal' and is maintained by Fedict/FPS BOSA DG Digital Transformation, corroborating BOSA's maintainer role in the entity's own technical infrastructure rather than only in prose describing it. The five originally cited belgium.be/data.gov.be/data.europa.eu pages remain unreadable (CAPTCHA or unparseable binary) even on retry this pass."
    confidence: high
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
  - title: "Fedict/dcat — README (export of data.gov.be in DCAT-AP)"
    url: "https://github.com/Fedict/dcat"
    publisher: "GitHub (Fedict)"
    accessed: "2026-08-28"
  - title: "Europe and Belgium further expand possibilities for re-use of public sector information"
    url: "https://www.lexgo.be/en/news-and-articles/6385-europe-and-belgium-further-expand-possibilities-for-re-use-of-public-sector-information-open-data"
    publisher: "Lexgo.be"
    accessed: "2026-08-28"
  - title: "Fedict — FPS BOSA DG Digital Transformation (GitHub organisation profile and repository list)"
    url: "https://github.com/orgs/Fedict/repositories"
    publisher: "GitHub (Fedict / FPS BOSA)"
    accessed: "2026-08-28"
---

# data.gov.be

> **Promoted to `primary-source` 2026-08-28.** All five originally cited
> `belgium.be`/`data.gov.be`/`data.europa.eu` sources remain unreadable,
> confirmed again this pass (CAPTCHA or unparseable binary). Two
> previously-uncited pages were read in the prior pass — GitHub's own
> `Fedict/dcattools` README and a third-party API directory's description
> of data.gov.be. This pass found and read three more, all genuinely
> independent of the Belgian government's blocked web presence: a second
> Fedict GitHub repository, `Fedict/dcat`, whose own README states it
> holds "Metadata being used to update the Belgian data.gov.be portal, in
> DCAT-AP + HVD"; the Fedict GitHub organisation's repository listing,
> confirming the fuller set of open-data tooling repositories (`dcattools`,
> `dcat`, `lod-cbe`, `rdfvalidator`) under "FPS BOSA DG Digital
> Transformation"; and an independent Belgian legal-news article
> (lexgo.be) naming data.gov.be as "the federal data portal" and setting
> out the Belgian reuse-of-public-sector-information legal framework
> around it (the Act of 4 May 2016, amended 2019, and the Royal Decree of
> 2 June 2019 on model licences). That is 6 of 11 sources read directly —
> a genuine majority — so `verification` is promoted to `primary-source`.

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

**Confirmed by reading a second Fedict repository, `Fedict/dcat`, directly
(2026-08-28):** its README describes itself as the output side of that
same pipeline — "Metadata being used to update the Belgian data.gov.be
portal, in DCAT-AP + HVD. Available as N-Triples and RDF/XML file" — and
names a "pretty-print" RDF/XML serialisation (`datagovbe_edp.xml.gz`)
specifically harvested by the European Data Portal, closing the loop
`dcattools` describes from the input side. The Fedict GitHub organisation's
own repository listing, also read directly this pass, shows this is one of
several related tools (`lod-cbe`, `lod-sbmb`, `rdfvalidator`) built around
the same DCAT-AP infrastructure.

**Confirmed by reading an independent Belgian legal-news article directly
(2026-08-28, lexgo.be):** data.gov.be is named as "the federal data portal"
and sits inside a specific legal framework — the Act of 4 May 2016 on the
re-use of public sector information (amended by the Act of 7 April 2019)
and the Royal Decree of 2 June 2019, which set standardised model licences
and a "detailed rules" procedure for reuse requests, including a licensing
cascade from unrestricted CC0 down to conditional reuse agreements. The
article independently corroborates the portal's existence and federal
scope from a source with no connection to belgium.be.

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

Six of eleven read directly. From the prior pass: GitHub's `Fedict/dcattools`
README and publicapis.io's description. New this pass (2026-08-28):
`Fedict/dcat`'s own README, the Fedict GitHub organisation's repository
listing, and an independent lexgo.be legal-news article. All five
originally cited sources remain unreadable: three CAPTCHA-walled pages
(`bosa.belgium.be`, `data.gov.be` twice) and one bot-walled page
(`financien.belgium.be`), plus one PDF (`data.europa.eu`) whose content
could not be extracted as text — all retried this pass with the same
result, per the discipline's instruction not to re-spend effort on those
exact domains going forward.
