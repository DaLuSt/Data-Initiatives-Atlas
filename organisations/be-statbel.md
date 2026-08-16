---
id: BE-STATBEL
type: organisation
name: Statbel
alternative_names:
  - Algemene Directie Statistiek
  - Statistics Belgium
  - Direction générale Statistique
description: >
  Belgian national statistical office, the Algemene Directie Statistiek
  within the FOD Economie. It opened an open data portal in October 2015,
  publishes its statistics under a Creative Commons Attribution 4.0 licence
  and maintains a DCAT catalogue of its open data.

level: national
country: BE
region: null

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
  - BE-DCAT-AP-BE
relationships:
  - type: aligned-with
    target: BE-DCAT-AP-BE
    source: fact
    evidence: "Statbel publishes a DCAT catalogue for its open data (statbel.fgov.be 'DCAT catalogue for Statbel's open data'). NOT READ — search-only. Recorded as aligned-with rather than based-on: the sources establish that Statbel publishes a DCAT catalogue, not that it conforms to the Belgian federal DCAT profile specifically."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Open Data | Statbel"
    url: "https://statbel.fgov.be/nl/open-data?category=214"
    publisher: "Statbel (Algemene Directie Statistiek)"
  - title: "DCAT catalogue for Statbel's open data"
    url: "https://statbel.fgov.be/en/open-data/dcat-catalogue-statbels-open-data"
    publisher: "Statbel (Algemene Directie Statistiek)"
  - title: "De Algemene Directie Statistiek van de FOD Economie gaat voor Open Data"
    url: "https://news.belgium.be/nl/de-algemene-directie-statistiek-van-de-fod-economie-gaat-voor-open-data"
    publisher: "news.belgium.be (Belgian federal government)"
  - title: "Statistics Belgium"
    url: "https://en.wikipedia.org/wiki/Statistics_Belgium"
    publisher: "Wikipedia"
---

# Statbel (Algemene Directie Statistiek)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Statbel is Belgium's national statistical office — the Algemene Directie
Statistiek within the FOD Economie.

Its open data portal opened on **22 October 2015**, carrying datasets on
population, income, land use and other subjects in freely reusable formats
under a **Creative Commons Attribution 4.0** licence. It maintains a
**DCAT catalogue** of that open data.

`coverage: low`: unlike [[DE-DESTATIS]] and [[NL-CBS]], no statutory basis
for Statbel was established — no Belgian equivalent of [[DE-BSTATG]] or
[[NL-WET-CBS]] was found by search, so none is recorded and no
`governed-by` relationship is asserted.

## The statistics cluster, now with a third member

The Atlas has recorded the same refused link three times:

| Candidate | Refused because |
|---|---|
| [[UN-UNSD]] → [[EU-EUROSTAT]] | no source read connects the levels |
| [[UN-FPOS]] → [[NL-WET-CBS]] | no source connects the Dutch act to the Fundamental Principles |
| [[DE-DESTATIS]] → [[EU-EUROSTAT]] | Destatis's remit names "the European Union", not Eurostat |
| [[DE-BSTATG]] → [[UN-FPOS]] | the act's principles restate the FPOS without citing them |

Statbel adds nothing to this list, and that is worth saying explicitly:
**no source read connects Statbel to Eurostat, to the European Statistical
System or to the UN statistical system either.** Three national statistical
offices now sit in the Atlas and none of them connects upward.

This is the single most persistent structural hole in the graph. It has
survived three countries, and each country has made it more conspicuous
without making it closable. It is not a hard research problem — it is a
page-reading problem, and page reading is what this environment cannot do.

## Relationships

- `aligned-with` [[BE-DCAT-AP-BE]] — at `confidence: low`. What is sourced
  is that Statbel publishes *a* DCAT catalogue; that it conforms to the
  Belgian federal profile is the obvious reading and is not stated. The
  weaker relationship type and the low confidence carry that distinction.

## Sources

Listed in frontmatter.
