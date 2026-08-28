---
id: DE-GOVDATA
type: platform
name: GovData
alternative_names:
  - "GovData — Das Datenportal für Deutschland"
description: >
  Germany's central open data portal, bringing together freely available
  data from public administrations at federal, Land and municipal level
  (plus utilities, universities and research institutions) and making it
  findable through a single search — over 157,000 datasets, roughly 10,600
  high-value datasets and 35 applications as of this pass. Its operational
  basis is an administrative agreement (Verwaltungsvereinbarung) acceded to
  by the federation and all sixteen Länder, completed when Saarland joined.
  Product management sits at the FITKO in Frankfurt am Main, which took
  GovData into its product management as an IT-Planungsrat product on
  1 January 2023; SEITENBAU GmbH provides technical implementation and
  hosting.

level: national
country: DE
region: null

status: active
confidence: high
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
  - DE-FITKO
related_entities:
  - DE-DCAT-AP-DE
  - DE-DNG
  - NL-DATA-OVERHEID
relationships:
  - type: maintained-by
    target: DE-FITKO
    source: fact
    evidence: "Confirmed by reading fitko.de's own product-management page and press release directly (2026-08-28): 'GovData is managed by FITKO as an IT Planning Council product, operational since January 1, 2023.' govdata.de's own help page, also read directly, independently confirms 'product management based at FITKO in Frankfurt' and names SEITENBAU GmbH as the technical operator/host — a fact not previously recorded on this entity."
    confidence: high
    valid_from: 2023-01-01
    valid_until: null

sources:
  - title: "GovData — Das Datenportal für Deutschland"
    url: "https://www.govdata.de/"
    publisher: "GovData"
    accessed: "2026-08-28"
  - title: "GovData | FITKO"
    url: "https://www.fitko.de/produktmanagement/govdata"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "GovData: Alle Länder und der Bund unterstützen das Open Data-Portal"
    url: "https://www.fitko.de/presse/pressedetail/govdata-alle-laender-und-der-bund-unterstuetzen-das-open-data-portal"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "Produkt 'GovData': Alle Länder und der Bund unterstützen das Open Data-Portal"
    url: "https://www.it-planungsrat.de/aktuelles/details/produkt-govdata-alle-laender-und-der-bund-unterstuetzen-das-open-data-portal"
    publisher: "IT-Planungsrat"
    accessed: "2026-08-28"
  - title: "Das Portal — GovData"
    url: "https://www.govdata.de/informationen/hilfe"
    publisher: "GovData"
    accessed: "2026-08-28"
---

# GovData

> **Re-verified 2026-08-28.** All five cited pages read directly.
> `verification: primary-source`; `confidence` raised to `high`.

## Description

GovData is Germany's central data portal. It brings together freely
available data from public administrations at **federal, Land and
municipal level** — and, per govdata.de's own help page (read directly),
also from utilities, universities and research institutions — making it
findable through a single search. Confirmed directly this pass on
govdata.de's own homepage: it currently hosts **over 157,000 datasets**,
roughly **10,600 high-value datasets**, and **35 applications**; FITKO's
own product page gives a slightly earlier snapshot of "over 150,000
datasets" including "19,000 building plans."

Its operational basis is a **Verwaltungsvereinbarung**, an administrative
agreement. All sixteen Länder and the federation have acceded to it;
confirmed directly this pass on the FITKO press release, **Saarland's
accession completed the set**, with IT-Planungsrat chair Patrick Burghardt
quoted directly: "wir ziehen Bund und Länder an einem Strang."

Product management sits at [[DE-FITKO]] in Frankfurt am Main, which took
GovData into its product management as a **product of the
[[DE-IT-PLANUNGSRAT]] on 1 January 2023** — confirmed directly this pass.
govdata.de's own help page, also read directly, names **SEITENBAU GmbH**
as the company providing technical implementation and hosting — a fact not
previously recorded here.

GovData established [[DE-DCAT-AP-DE]] as the recognised data exchange
standard for open government data, confirmed directly this pass on FITKO's
own product page, which also describes planned expansion toward
**protected public-sector data** (e.g. registry information) accessible
through **NOOTS** — a system not previously recorded on this entity and not
otherwise modelled here.

## The federal model made visible

Most German entities in this batch lose information at the Bund-Länder
boundary. GovData is the one where the federal structure is **the point**
rather than an obstacle: a portal that only works because sixteen Länder
and the federation separately signed an agreement to feed it, run as a
shared product by a jointly-owned institution.

The Dutch counterpart [[NL-DATA-OVERHEID]] needs no such construction.
**No relationship between them is asserted**, and the contrast is the
useful part: the same function requires an interstate treaty-like
instrument in one country and an ordinary government service in the other.

## Relationships

- Maintained by [[DE-FITKO]] — confirmed directly this pass, `confidence:
  high`.

Inbound: [[DE-DCAT-AP-DE]] `applies-to` this portal.

**No relationship to [[DE-DNG]] is asserted**, though the connection is
tempting: the DNG is the federal open-data act and GovData is the federal
open-data portal. No source read this pass links them either, and the
portal predates the 2021 act. `related_entities` records the association
for navigation only.

## Sources

Listed in frontmatter, all five read directly this pass.
