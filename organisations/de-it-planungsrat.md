---
id: DE-IT-PLANUNGSRAT
type: organisation
name: IT-Planungsrat
alternative_names:
  - IT Planning Council
description: >
  Central political, cross-departmental steering committee of the federal
  government and the Länder in Germany. It coordinates cooperation between
  the federation and the Länder on information technology questions,
  establishes IT interoperability and security standards, adopts the
  federal IT architecture guidelines, manages the shared federal-Länder
  digitalisation budget, and is supported operationally by the Föderale
  IT-Kooperation, which it created to implement its decisions.

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
organisations: []
related_entities:
  - DE-FITKO
relationships:
  - type: produces
    target: DE-IT-ARCHITEKTURRICHTLINIEN
    source: fact
    evidence: "Confirmed by reading fitko.de's own 'Föderale IT-Architektur' page directly (2026-08-28): by decision 2025/17 the IT-Planungsrat adopted version 1.9.0 of the Föderale IT-Architekturrichtlinie, with the föderales IT-Architekturboard — chaired by FITKO and established by IT-Planungsrat decision on 22 February 2021 — defining and developing the guidelines, whose binding application was separately made mandatory by decision 2021/37."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Föderale IT-Kooperation (FITKO) Fact sheet"
    url: "https://www.it-planungsrat.de/fileadmin/beschluesse/2018/Beschluss2018-04_02_I_FITKO_Factsheet.pdf"
    publisher: "IT-Planungsrat"
  - title: "Produkt 'GovData': Alle Länder und der Bund unterstützen das Open Data-Portal"
    url: "https://www.it-planungsrat.de/aktuelles/details/produkt-govdata-alle-laender-und-der-bund-unterstuetzen-das-open-data-portal"
    publisher: "IT-Planungsrat"
    accessed: "2026-08-28"
  - title: "IT-Planungsrat & FITKO"
    url: "https://digitales.hessen.de/moderne-verwaltung/it-planungsrat-fitko"
    publisher: "Hessisches Ministerium für Digitalisierung und Innovation"
    accessed: "2026-08-28"
  - title: "IT-Planungsrat und Föderale IT-Kooperation"
    url: "https://www.geodaten.niedersachsen.de/startseite/gdi_grundlagen/it_planungsrat_fitko/it-planungsrat-und-foderale-it-kooperation-207861.html"
    publisher: "Geodatenportal Niedersachsen"
    accessed: "2026-08-28"
  - title: "FITKO | Föderale IT-Architektur"
    url: "https://www.fitko.de/foederale-it-architektur"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
---

# IT-Planungsrat

> **Re-verified 2026-08-28.** All five cited sources read directly (the
> factsheet PDF returned only binary and could not be read as text; the
> other four loaded as readable HTML). `verification: primary-source`;
> `confidence` raised to `high`.

## Description

The IT-Planungsrat coordinates cooperation between the Bund and the Länder
on questions of information technology and is described, confirmed
directly this pass on two independent Land-government pages, as the
**central political, cross-departmental steering committee** of the
federal government and the Länder — establishing IT interoperability and
security standards, managing e-government initiatives, overseeing federal
network infrastructure, and managing the **shared federal-Länder
digitalisation budget** (a function not previously recorded on this
entity).

Its decisions are numbered and published (`Beschluss 2025/17`, for example,
adopted version 1.9.0 of the [[DE-IT-ARCHITEKTURRICHTLINIEN]], confirmed
directly this pass, alongside a separately-confirmed `Beschluss 2021/37`
that made the guidelines' application binding), and it created
[[DE-FITKO]] specifically **to implement its decisions** — confirmed
directly this pass on digitales.hessen.de, which calls FITKO the council's
"implementation muscle." It is also the body under which [[DE-GOVDATA]] is
supported by all Länder and the Bund, confirmed directly this pass on the
IT-Planungsrat's own page announcing Saarland's accession completed the
set of all sixteen Länder plus the federation as members of the
administrative agreement underpinning the portal.

geodaten.niedersachsen.de, read directly, adds that FITKO **consolidated
previously independent organisations** including [[DE-KOSIT]], FIM and
[[DE-GOVDATA]] under one roof, and now operates **FIT-Store** (software
reuse across administrations) and **FIT-Connect** (a service gateway) —
neither previously recorded on this entity or on [[DE-FITKO]].

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

- Produces [[DE-IT-ARCHITEKTURRICHTLINIEN]] — confirmed directly this
  pass, `confidence: high`.

The link to [[DE-FITKO]] is recorded **on the FITKO entity**, as
`governed-by` → this one: the FITKO acts on the IT-Planungsrat's mandate,
so the council is the principal and the agency the dependent party.
Recording it in the other direction — "the IT-Planungsrat is governed by
the FITKO" — would have inverted the constitutional relationship because
the FITKO happens to do the operational work. This pass's direct reads
(digitales.hessen.de calling FITKO the council's "implementation muscle")
reinforce that direction.

## Sources

Listed in frontmatter, four of five read directly as HTML text this pass;
the factsheet PDF returned only binary to the fetch tool.
