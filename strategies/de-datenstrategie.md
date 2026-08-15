---
id: DE-DATENSTRATEGIE
type: strategy
name: Nationale Datenstrategie
alternative_names:
  - Datenstrategie der Bundesregierung
  - "Fortschritt durch Datennutzung"
  - German National Data Strategy
description: >
  Federal government data strategy adopted by the German cabinet in 2023
  under the title "Fortschritt durch Datennutzung — Strategie für mehr und
  bessere Daten für eine neue, wirksame und zukunftsgerichtete
  Datennutzung". It develops the earlier national data strategy further,
  aiming at more and better data availability and a new culture of data use
  and data sharing, and carries a roadmap of concrete measures.

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
  - DE-BMI
related_entities:
  - DE-DIGITALSTRATEGIE
relationships: []

sources:
  - title: "Bundeskabinett beschließt Nationale Datenstrategie"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2023/08/nationale-datenstrategie.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Bundeskabinett beschließt Nationale Datenstrategie"
    url: "https://bmdv.bund.de/SharedDocs/DE/Pressemitteilungen/2023/084-neue-datenstrategie-der-bundesregierung.html"
    publisher: "Bundesministerium für Digitales und Verkehr (BMDV)"
  - title: "Nationale Datenstrategie der Bundesregierung (Drucksache 20/8260)"
    url: "https://dserver.bundestag.de/btd/20/082/2008260.pdf"
    publisher: "Deutscher Bundestag"
  - title: "Disput über die Weiterentwicklung der nationalen Datenstrategie"
    url: "https://www.bundestag.de/dokumente/textarchiv/2023/kw39-de-datenstrategie-967338"
    publisher: "Deutscher Bundestag"
---

# Nationale Datenstrategie

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Nationale Datenstrategie is the German federal government's data
strategy, titled *Fortschritt durch Datennutzung — Strategie für mehr und
bessere Daten für eine neue, wirksame und zukunftsgerichtete Datennutzung*.
It was developed and presented jointly by three ministries: the then
Bundesministerium für Digitales und Verkehr (BMDV), the Bundesministerium
für Wirtschaft und Klimaschutz (BMWK) and the Bundesministerium des Innern
und für Heimat ([[DE-BMI]]).

It builds on and develops an existing earlier national data strategy. Its
stated emphasis is on providing more and better data and on a new culture
of data use and data sharing, and it carries a roadmap setting out the
concrete new measures. Search results describe its subject areas as
spanning the European legal framework, open data, data protection,
competitive standards and data spaces.

This is Germany's counterpart to the Dutch [[NL-IBDS]] and
[[NL-DATA-AGENDA-OVERHEID]] in role, though **no source connects them** and
no relationship between them is asserted.

## ⚠ Unresolved: the adoption date

Sources returned by search disagree, and the disagreement is not resolvable
without reading them:

| Source | Implied date |
|---|---|
| BMI press release (URL path `/2023/08/`) | August 2023 |
| Behörden Spiegel article | 12 September 2023 |
| digitale-technologien.de news item (URL path `2023_09_14_`) | 14 September 2023 |

`start_date` is therefore **null**, not a guess. One reading that would
reconcile them is a cabinet decision in late August followed by press
coverage in September, but that is an inference and the Atlas does not
record inferences as dates. Logged in `discovery/unresolved.md`.

## Status caveat

`status: active` reflects that this is the most recent national data
strategy found. It was adopted under the previous federal government;
Germany has since created [[DE-BMDS]] as a dedicated digital ministry and
adopted the [[DE-MODERNISIERUNGSAGENDA-BUND]]. **No source read states
whether the 2023 data strategy remains in force, has been absorbed into the
newer agenda, or has been superseded.** Treat the status as the weakest
claim in this entity.

## Relationships

**This entity asserts none of its own.** It is reached from [[DE-BMI]],
which `produces` it — the sourced statement is that BMI was one of three
ministries that jointly developed and presented the strategy.

A `produces` link to [[DE-DNG]] was considered and **refused**. The strategy
covers open data and the DNG is the federal open-data instrument, but no
source read connects them, and the chronology runs the wrong way: the DNG
(2021) predates the strategy (2023). A thematic resemblance is not a
relationship.

The strategy's three authoring ministries are only partly modelled: BMWK is
not an Atlas entity, and BMDV has since been reorganised (see
[[DE-BMDS]]). Queued in `discovery/research-queue.md`.

## Sources

Listed in frontmatter.
