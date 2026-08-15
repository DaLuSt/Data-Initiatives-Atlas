---
id: DE-IT-PLANUNGSRAT
type: organisation
name: IT-Planungsrat
alternative_names:
  - IT Planning Council
description: >
  Central political steering body for the digitalisation of public
  administration in Germany. It coordinates cooperation between the
  federation and the Länder on information technology questions, adopts the
  federal IT architecture guidelines, and is supported operationally by the
  Föderale IT-Kooperation.

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
organisations: []
related_entities:
  - DE-FITKO
relationships:
  - type: produces
    target: DE-IT-ARCHITEKTURRICHTLINIEN
    source: fact
    evidence: "By decision 2025/17 the IT-Planungsrat adopted version 1.9.0 of the Föderale IT-Architekturrichtlinie; the federal IT architecture board, chaired by FITKO, defines and develops the guidelines (fitko.de/foederale-it-architektur; docs.fitko.de/fit/policies/foederale-it-architekturrichtlinien). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Föderale IT-Kooperation (FITKO) Fact sheet"
    url: "https://www.it-planungsrat.de/fileadmin/beschluesse/2018/Beschluss2018-04_02_I_FITKO_Factsheet.pdf"
    publisher: "IT-Planungsrat"
  - title: "Produkt 'GovData': Alle Länder und der Bund unterstützen das Open Data-Portal"
    url: "https://www.it-planungsrat.de/aktuelles/details/produkt-govdata-alle-laender-und-der-bund-unterstuetzen-das-open-data-portal"
    publisher: "IT-Planungsrat"
  - title: "IT-Planungsrat & FITKO"
    url: "https://digitales.hessen.de/moderne-verwaltung/it-planungsrat-fitko"
    publisher: "Hessisches Ministerium für Digitalisierung und Innovation"
  - title: "IT-Planungsrat und Föderale IT-Kooperation"
    url: "https://www.geodaten.niedersachsen.de/startseite/gdi_grundlagen/it_planungsrat_fitko/it-planungsrat-und-foderale-it-kooperation-207861.html"
    publisher: "Geodatenportal Niedersachsen"
  - title: "FITKO | Föderale IT-Architektur"
    url: "https://www.fitko.de/foederale-it-architektur"
    publisher: "Föderale IT-Kooperation (FITKO)"
---

# IT-Planungsrat

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The IT-Planungsrat coordinates cooperation between the Bund and the Länder
on questions of information technology and is described as the **central
political steering body** for the digitalisation of public administration
in Germany.

Its decisions are numbered and published (`Beschluss 2025/17`, for example,
adopted version 1.9.0 of the [[DE-IT-ARCHITEKTURRICHTLINIEN]]), and it
commissioned the [[DE-FITKO]] to develop a federal IT architecture in
cooperation with the Bund and the Länder. It is also the body under which
[[DE-GOVDATA]] is supported by all Länder and the Bund.

## The closest thing Germany has to a Forum Standaardisatie

In role, the IT-Planningsrat sits where the Dutch [[NL-FORUM-STANDAARDISATIE]]
and [[NL-OBDO]] sit: a standing multi-level governance body that adopts
binding-ish architecture and standards decisions for public administration.

**No relationship to either is asserted.** The comparison is an Atlas
observation and the mechanisms differ materially — the Dutch model rests on
the 'pas toe of leg uit' policy ([[NL-PAS-TOE-OF-LEG-UIT]]) applied to a
published list, while the German model rests on Bund-Länder decisions
binding on projects affecting the federal IT landscape. Recording a
`related-to` between them would flatten a real difference into a
resemblance.

## Relationships

- Produces [[DE-IT-ARCHITEKTURRICHTLINIEN]].

The link to [[DE-FITKO]] is recorded **on the FITKO entity**, as
`governed-by` → this one: the FITKO acts on the IT-Planungsrat's mandate,
so the council is the principal and the agency the dependent party.
Recording it in the other direction — "the IT-Planungsrat is governed by
the FITKO" — would have inverted the constitutional relationship because
the FITKO happens to do the operational work.

## Sources

Listed in frontmatter.
