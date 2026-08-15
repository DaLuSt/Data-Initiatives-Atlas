---
id: DE-GOVDATA
type: platform
name: GovData
alternative_names:
  - "GovData — Das Datenportal für Deutschland"
description: >
  Germany's central open data portal, bringing together freely available
  data from public administrations at federal, Land and municipal level and
  making it findable through a single search. Its operational basis is an
  administrative agreement (Verwaltungsvereinbarung) acceded to by the
  federation and all sixteen Länder. Product management sits at the FITKO
  in Frankfurt am Main, which took GovData into its product management as
  an IT-Planungsrat product on 1 January 2023.

level: national
country: DE
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
  - DE-FITKO
related_entities:
  - DE-DCAT-AP-DE
  - DE-DNG
  - NL-DATA-OVERHEID
relationships:
  - type: maintained-by
    target: DE-FITKO
    source: fact
    evidence: "Product management for the GovData portal is located at the FITKO in Frankfurt am Main; the FITKO took GovData into its product management as a product of the IT-Planungsrat on 1 January 2023 (fitko.de/produktmanagement/govdata; de.wikipedia.org 'Föderale IT-Kooperation'). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-01-01
    valid_until: null

sources:
  - title: "GovData — Das Datenportal für Deutschland"
    url: "https://www.govdata.de/"
    publisher: "GovData"
  - title: "GovData | FITKO"
    url: "https://www.fitko.de/produktmanagement/govdata"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "GovData: Alle Länder und der Bund unterstützen das Open Data-Portal"
    url: "https://www.fitko.de/presse/pressedetail/govdata-alle-laender-und-der-bund-unterstuetzen-das-open-data-portal"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Produkt 'GovData': Alle Länder und der Bund unterstützen das Open Data-Portal"
    url: "https://www.it-planungsrat.de/aktuelles/details/produkt-govdata-alle-laender-und-der-bund-unterstuetzen-das-open-data-portal"
    publisher: "IT-Planungsrat"
  - title: "Das Portal — GovData"
    url: "https://www.govdata.de/informationen/hilfe"
    publisher: "GovData"
---

# GovData

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

GovData is Germany's central data portal. It brings together freely
available data from public administrations at **federal, Land and municipal
level** and makes it findable through a single search — the nationwide
portal through which Bund, Länder and Kommunen make their open
administrative data systematically discoverable and accessible.

Its operational basis is a **Verwaltungsvereinbarung**, an administrative
agreement. All sixteen Länder and the federation have acceded to it;
Saarland's accession completed the set.

Product management sits at [[DE-FITKO]] in Frankfurt am Main, which took
GovData into its product management as a **product of the
[[DE-IT-PLANUNGSRAT]] on 1 January 2023**.

GovData established [[DE-DCAT-AP-DE]] as the recognised data exchange
standard for open government data.

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

- Maintained by [[DE-FITKO]].

Inbound: [[DE-DCAT-AP-DE]] `applies-to` this portal.

**No relationship to [[DE-DNG]] is asserted**, though the connection is
tempting: the DNG is the federal open-data act and GovData is the federal
open-data portal. No source read links them, and the portal predates the
2021 act. `related_entities` records the association for navigation only.

## Sources

Listed in frontmatter.
