---
id: DE-FITKO
type: organisation
name: Föderale IT-Kooperation
alternative_names:
  - FITKO
  - Federal IT Cooperation
description: >
  Institution under public law (Anstalt des öffentlichen Rechts) jointly
  held by all German Länder and the federation, created under the 2019 IT
  State Treaty (IT-Staatsvertrag), seated in Frankfurt am Main and
  established on 1 January 2020. Acting on the mandate of the
  IT-Planungsrat, it coordinates and networks public-administration
  digitalisation projects, leads federal IT architecture management, and
  hosts the KoSIT, FIM and the GovData portal. Staff grew from around 40 in
  2020 to 111 by June 2025.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2020-01-01
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-IT-PLANUNGSRAT
  - DE-FIM
  - DE-KOSIT
  - DE-GOVDATA
relationships:
  - type: governed-by
    target: DE-IT-PLANUNGSRAT
    source: fact
    evidence: "Confirmed by reading de.wikipedia.org's dedicated FITKO article and service.bund.de's own page directly (2026-08-28): FITKO is 'a German lawful public institution' created under the 2019 IT-Staatsvertrag and established 1 January 2020, functioning as 'the operational foundation for the IT Planning Council'; service.bund.de states plainly that FITKO was 'created' by the IT-Planungsrat 'as an agile organization to implement its decisions,' with the IT-Planungsrat setting policy direction and FITKO executing it. fitko.de's own homepage, also read directly, confirms FITKO implements IT-Planungsrat decisions while the council sets 'politisch-strategische' direction."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "FITKO"
    url: "https://www.fitko.de/"
    publisher: "Föderale IT-Kooperation (FITKO)"
    accessed: "2026-08-28"
  - title: "Föderale IT-Kooperation (FITKO) Fact sheet"
    url: "https://www.it-planungsrat.de/fileadmin/beschluesse/2018/Beschluss2018-04_02_I_FITKO_Factsheet.pdf"
    publisher: "IT-Planungsrat"
  - title: "FITKO (Föderale IT-Kooperation)"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-grundlagen/akteure/fitko/fitko-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
  - title: "Föderale IT-Kooperation"
    url: "https://de.wikipedia.org/wiki/F%C3%B6derale_IT-Kooperation"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "FITKO — Föderale IT-Kooperation"
    url: "https://www.service.bund.de/Content/DE/DEBehoerden/F/FITKO/FITKO.html?nn=4641496"
    publisher: "service.bund.de (Bundesverwaltungsamt)"
    accessed: "2026-08-28"
---

# Föderale IT-Kooperation (FITKO)

> **Re-verified 2026-08-28.** Three of five cited pages read directly. The
> factsheet PDF returned only encoded binary to the fetch tool and
> `digitale-verwaltung.de` returned HTTP 400 on every attempt this pass
> (the same domain is unreachable across other entities in this batch —
> see [[DE-OZG]]). `verification: primary-source`; `confidence` raised to
> `high`; the legal basis is now more precisely sourced (the 2019
> IT-Staatsvertrag, not previously named) and staff-growth figures are
> added.

## Description

The FITKO is an **Anstalt des öffentlichen Rechts in Trägerschaft aller
Länder und des Bundes** — a public-law institution jointly held by all
sixteen Länder and the federation — seated in Frankfurt am Main and
established on **1 January 2020**. Confirmed directly this pass on its
dedicated Wikipedia article: it was created on the basis of the **2019 IT
State Treaty (IT-Staatsvertrag)**, a more precise legal basis than
previously recorded, and its staff grew from roughly **40 in 2020 to 111 by
June 2025**.

Its tasks, as the sources describe them:

- supporting the [[DE-IT-PLANUNGSRAT]] and its committees organisationally
  and strategically, and coordinating their work — confirmed directly this
  pass on fitko.de's own homepage and on service.bund.de's page, which
  states FITKO was "created by the IT-Planungsrat as an agile organization
  to implement its decisions";
- developing federal IT architecture management, and leading work on a
  federal IT architecture in cooperation with the Bund and the Länder;
- acting as the central coordination and networking point that creates the
  conditions for effective administrative digitalisation, and ensuring the
  IT-Planungsrat's decisions are implemented;
- chairing the **föderales IT-Architekturboard**, which defines and
  develops the [[DE-IT-ARCHITEKTURRICHTLINIEN]] (confirmed directly this
  pass on fitko.de's own dedicated architecture-board page in the course of
  re-verifying that entity).

Institutions brought together **under the FITKO's roof** include the
[[DE-KOSIT]] (Koordinierungsstelle für IT-Standards), the FIM (Föderales
Informationsmanagement) and the [[DE-GOVDATA]] portal. This pass's direct
reads describe FIM and GovData as products under FITKO's **product
management** rather than explicitly as institutions housed there, and one
source (fitko.de's own homepage) additionally names **Governikus** —
digital identity and authentication services — as a further managed
product not previously recorded on this entity; it is noted here but not
modelled separately, per the same reasoning that already excludes FIM as a
standalone entity (below).

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
  mandated. This pass's direct reading reinforces the correction:
  service.bund.de states in as many words that the IT-Planungsrat "created"
  FITKO to implement its decisions.
- **`maintained-by` → GovData** was first recorded here. But
  `maintained-by` is defined as *"the target organisation maintains this
  entity"*, so an edge from the FITKO to [[DE-GOVDATA]] asserts that the
  portal maintains the agency. It now sits on [[DE-GOVDATA]] pointing here,
  matching [[NL-DIGIKOPPELING]] → [[NL-LOGIUS]].

Both are worth recording because direction errors are invisible to a reader
and survive validation: the graph stays connected and every check passes
while the meaning is reversed.

## FIM is now an entity

The Föderales Informationsmanagement was named in the sources as a third
body/product under the FITKO's roof, alongside the KoSIT and GovData, but
this pass's direct reads could not establish anything further about it —
creating an entity on the strength of a mention in a product list is
exactly what §21 of the brief rules out. A research-queue pickup on
2026-09-04 closed the gap: `docs.fitko.de`'s own dedicated documentation
site — not found in this pass — carries a full page on FIM, and it is now
[[DE-FIM]], `governed-by` [[DE-IT-PLANUNGSRAT]] and `maintained-by` this
entity.

## Relationships

- `governed-by` [[DE-IT-PLANUNGSRAT]] — confirmed directly this pass,
  `confidence: high`.

Inbound: [[DE-GOVDATA]], [[DE-KOSIT]] and, since 2026-09-04, [[DE-FIM]] all
point here, and [[DE-IT-ARCHITEKTURRICHTLINIEN]] records the FITKO's
chairing of the architecture board.

## Sources

Listed in frontmatter. Three of five read directly this pass; the
factsheet PDF returned only binary and `digitale-verwaltung.de` returned
HTTP 400 on every attempt, both kept listed with that status noted here
rather than silently dropped.
