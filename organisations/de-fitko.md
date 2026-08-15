---
id: DE-FITKO
type: organisation
name: Föderale IT-Kooperation
alternative_names:
  - FITKO
  - Federal IT Cooperation
description: >
  Institution under public law (Anstalt des öffentlichen Rechts) jointly
  held by all German Länder and the federation, seated in Frankfurt am Main
  and established on 1 January 2020. Acting on the mandate of the
  IT-Planungsrat, it coordinates and networks public-administration
  digitalisation projects, leads federal IT architecture management, and
  hosts the KoSIT, FIM and the GovData portal.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2020-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-IT-PLANUNGSRAT
relationships:
  - type: governed-by
    target: DE-IT-PLANUNGSRAT
    source: fact
    evidence: "The FITKO coordinates and networks public administration digitalisation projects on the mandate of the IT-Planungsrat (im Auftrag des IT-Planungsrats); it bundles the IT-Planungsrat's former business and coordination offices and took over their operational planning, steering and coordination tasks, and ensures implementation of the IT-Planungsrat's decisions (de.wikipedia.org 'Föderale IT-Kooperation'; digitale-verwaltung.de; it-planungsrat.de FITKO factsheet). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "FITKO"
    url: "https://www.fitko.de/"
    publisher: "Föderale IT-Kooperation (FITKO)"
  - title: "Föderale IT-Kooperation (FITKO) Fact sheet"
    url: "https://www.it-planungsrat.de/fileadmin/beschluesse/2018/Beschluss2018-04_02_I_FITKO_Factsheet.pdf"
    publisher: "IT-Planungsrat"
  - title: "FITKO (Föderale IT-Kooperation)"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-grundlagen/akteure/fitko/fitko-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "Föderale IT-Kooperation"
    url: "https://de.wikipedia.org/wiki/F%C3%B6derale_IT-Kooperation"
    publisher: "Wikipedia"
  - title: "FITKO — Föderale IT-Kooperation"
    url: "https://www.service.bund.de/Content/DE/DEBehoerden/F/FITKO/FITKO.html?nn=4641496"
    publisher: "service.bund.de (Bundesverwaltungsamt)"
---

# Föderale IT-Kooperation (FITKO)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The FITKO is an **Anstalt des öffentlichen Rechts in Trägerschaft aller
Länder und des Bundes** — a public-law institution jointly held by all
sixteen Länder and the federation — seated in Frankfurt am Main and
established on **1 January 2020**.

Its tasks, as the sources describe them:

- supporting the [[DE-IT-PLANUNGSRAT]] and its committees organisationally
  and strategically, and coordinating their work;
- developing federal IT architecture management, and leading work on a
  federal IT architecture in cooperation with the Bund and the Länder;
- acting as the central coordination and networking point that creates the
  conditions for effective administrative digitalisation, and ensuring the
  IT-Planungsrat's decisions are implemented;
- chairing the **föderales IT-Architekturboard**, which defines and
  develops the [[DE-IT-ARCHITEKTURRICHTLINIEN]].

Institutions brought together **under the FITKO's roof** include the
[[DE-KOSIT]] (Koordinierungsstelle für IT-Standards), the FIM (Föderales
Informationsmanagement) and the [[DE-GOVDATA]] portal.

## The most structurally important German organisation in the Atlas

The FITKO is the hinge of the German layer. It is downstream of the
[[DE-IT-PLANUNGSRAT]] politically and upstream of the standards, the
architecture guidelines and the open-data portal operationally, which makes
it the single node through which most of the German public-sector graph
connects.

It has no Dutch counterpart with the same shape. [[NL-LOGIUS]] runs
services, [[NL-ICTU]] runs programmes and [[NL-FORUM-STANDAARDISATIE]]
governs standards; the FITKO does versions of all three under a Bund-Länder
ownership structure the Dutch layer has no equivalent of. **No relationship
to any of them is asserted.**

## Note on relationship direction

Two edges here were written in the wrong direction on the first pass and
corrected against `metadata/relationship-types.md` §2.1 before validation:

- **`governed-by` → [[DE-IT-PLANUNGSRAT]]** was first recorded on the
  council pointing at the FITKO. That inverted the constitutional
  relationship because the FITKO does the operational work. The FITKO acts
  *im Auftrag des* IT-Planungsrats: the council mandates, the agency is
  mandated.
- **`maintained-by` → GovData** was first recorded here. But
  `maintained-by` is defined as *"the target organisation maintains this
  entity"*, so an edge from the FITKO to [[DE-GOVDATA]] asserts that the
  portal maintains the agency. It now sits on [[DE-GOVDATA]] pointing here,
  matching [[NL-DIGIKOPPELING]] → [[NL-LOGIUS]].

Both are worth recording because direction errors are invisible to a reader
and survive validation: the graph stays connected and every check passes
while the meaning is reversed.

## FIM is not an entity

The Föderales Informationsmanagement is named in the sources as a third
body under the FITKO's roof, alongside the KoSIT and GovData, but nothing
further about it was established. Creating an entity on the strength of a
single mention in a list is exactly what §21 of the brief rules out.
Queued in `discovery/research-queue.md`.

## Relationships

- `governed-by` [[DE-IT-PLANUNGSRAT]].

Inbound: [[DE-GOVDATA]] and [[DE-KOSIT]] both point here, and
[[DE-IT-ARCHITEKTURRICHTLINIEN]] records the FITKO's chairing of the
architecture board.

## Sources

Listed in frontmatter.
