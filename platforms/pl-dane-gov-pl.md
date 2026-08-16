---
id: PL-DANE-GOV-PL
type: platform
name: dane.gov.pl
alternative_names:
  - Portal Otwartych Danych
  - Polish Open Data Portal
description: >
  Polish national open data portal. The Act of 11 August 2021 on open data
  and the re-use of public sector information establishes a data portal as a
  database of public sector information resources, alongside the categories
  of high-value and dynamic data, access to dynamic data through APIs, and
  the opening of publicly funded research data for re-use.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PL-OTWARTE-DANE
  - NL-DATA-OVERHEID
  - DE-GOVDATA
  - ES-DATOS-GOB-ES
  - FR-DATA-GOUV
relationships:
  - type: governed-by
    target: PL-OTWARTE-DANE
    source: fact
    evidence: "The Act of 11 August 2021 on open data and re-use of public sector information establishes a data portal as a database of public sector information resources, alongside the high-value and dynamic data categories, API access to dynamic data and the opening of publicly funded research data (gov.pl/web/ia 'Nowa ustawa o otwartych danych'; nim.gov.pl; isap.sejm.gov.pl WDU20210001641). NOT READ — search-only. CAVEAT: the sources establish that the Act provides for a data portal; that dane.gov.pl is that portal is the Atlas connecting the provision to the operating site."
    confidence: low
    valid_from: 2021-12-08
    valid_until: null

sources:
  - title: "Nowa ustawa o otwartych danych — Portal Interoperacyjności i Architektury"
    url: "https://www.gov.pl/web/ia/nowa-ustawa-o-otwartych-danych"
    publisher: "Portal Gov.pl"
  - title: "Ustawa z dnia 11 sierpnia 2021 r. o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego (Dz.U. 2021 poz. 1641)"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20210001641"
    publisher: "Internetowy System Aktów Prawnych (ISAP) — Sejm RP"
  - title: "Nowa ustawa o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego"
    url: "https://nim.gov.pl/aktualnosci/nowa-ustawa-o-otwartych-danych-i-ponownym-wykorzystywaniu-informacji-sektora-publicznego.html"
    publisher: "Narodowy Instytut Muzealnictwa (NIM)"
---

# dane.gov.pl

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

dane.gov.pl is Poland's national open data portal. [[PL-OTWARTE-DANE]]
**establishes a data portal** as a database of public sector information
resources — one of the changes that act brought alongside the high-value and
dynamic data categories, API access, and the opening of publicly funded
research data.

## The `governed-by` edge is `confidence: low`, deliberately

The sources establish that the 2021 Act **provides for a data portal**. That
dane.gov.pl **is** that portal is the Atlas joining the statutory provision
to the operating site — a short step, and still a step the sources do not
take.

This is the same discipline applied to [[ES-DATOS-GOB-ES]], whose
`applies-to` edge is marked `source: interpretation` because the sources
show the portal publishing a norm's documentation rather than stating that
the norm governs it.

The difference is that here the *statutory* basis is direct, so the edge is
`source: fact` with the caveat in its evidence, rather than an
interpretation.

## Six national open data portals

| Country | Portal | Custodian modelled? |
|---|---|---|
| Netherlands | [[NL-DATA-OVERHEID]] | **no** |
| Germany | [[DE-GOVDATA]] | yes — [[DE-FITKO]] |
| France | [[FR-DATA-GOUV]] | yes — [[FR-DINUM]] |
| Spain | [[ES-DATOS-GOB-ES]] | **no** — Red.es not modelled |
| **Poland** | **dane.gov.pl** | **no** — see below |

Three of six national portals still have no custodian in the graph, for
three different reasons: the Dutch one was never researched, the Spanish
one's operator was too thinly sourced to create, and this one's operator
**was not identified at all**.

`coverage: low` reflects that: the portal's operator, launch date, dataset
count and relationship to [[PL-COI]]'s systems are all unrecorded. No source
found in this batch names who runs it.

## Not asserted

**No relationship to a Polish DCAT profile.** [[EU-DCAT-AP]] has four
national children in the Atlas; whether Poland has a fifth was not
researched. Queued.

**No relationship to the other five portals.** They are national solutions
to a shared problem, which is not a relationship.

## Relationships

- `governed-by` [[PL-OTWARTE-DANE]] — low confidence, see above.

## Sources

Listed in frontmatter. ⚠ **Not one is the portal's own site.** Everything
recorded here comes from descriptions of the Act that establishes it, which
is the direct cause of `coverage: low`.
