---
id: ES-EJIE
type: organisation
name: Eusko Jaurlaritzaren Informatika Elkartea
alternative_names:
  - EJIE
  - Sociedad Informática del Gobierno Vasco
  - Basque Government IT Company
description: >
  Basque Government's own information-technology company, established
  by Decreto 60/1982, of 1 February, as a commercial entity wholly
  owned by the Basque Government (Gobierno Vasco / Eusko Jaurlaritza),
  operating under the Department of Governance, Digital Administration
  and Self-Government. It manages information technology and digital
  administration services across the Basque public sector, including
  the euskadi.eus government portal, web content management systems,
  digital accessibility standards, and IT infrastructure for Basque
  Government bodies. EJIE is one of four public IT companies — with
  CCASA, IZFE and LANTIK — that jointly constitute the Interoperability
  and Security Node of the Administrations of Euskadi (NISAE), serving
  the Basque Government and the Provincial Councils of Álava, Bizkaia
  and Gipuzkoa.

level: subnational
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1982-02-01
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-IZFE
  - ES-CCASA
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Confirmed by reading euskadi.eus's own EJIE page directly (2026-09-20): EJIE (Eusko Jaurlaritzaren Informatika Elkartea, Sociedad Informática del Gobierno Vasco) was established by 'DECRETO 60/1982, de 1 de Febrero' as a commercial entity created and wholly owned by the Basque Government, operating under the Department of Governance, Digital Administration and Self-Government. A separate euskadi.eus page on the NISAE interoperability node, also read directly, names EJIE alongside CCASA, IZFE and LANTIK as the four public IT companies constituting the Interoperability and Security Node of the Administrations of Euskadi, serving the Basque Government and the Provincial Councils of Álava, Bizkaia and Gipuzkoa. Anchor edge under metadata/relationship-types.md §2.3, asserting Basque sub-federal scope via `level: subnational`. Wholly government-owned, unlike [[DE-AKDB]] (municipal-association-owned) or [[ES-AOC]] (a multi-party consortium), so `part-of` is a closer fit here than for either."
    confidence: high
    valid_from: 1982-02-01
    valid_until: null

sources:
  - title: "EJIE - Sociedad Informática del Gobierno Vasco"
    url: "https://www.euskadi.eus/ejie-sociedad-informatica-del-gobierno-vasco/web01-a2wz/es/"
    publisher: "Gobierno Vasco — Euskadi.eus"
    accessed: "2026-09-20"
  - title: "NISAE - Nodo de Interoperabilidad y Seguridad de las Administraciones de Euskadi"
    url: "https://www.euskadi.eus/gobierno-vasco/-/documentacion/nisae-nodo-de-interoperabilidad-y-seguridad-de-las-administraciones-de-euskadi-p-class-migasestandar-grupo-a-href-informacionservicios-interoperabilidadweb01-a4ogainfes-servicios-de-interoperabilidad-a-p/"
    publisher: "Gobierno Vasco — Euskadi.eus"
    accessed: "2026-09-20"
---

# EJIE — Basque Government IT Company

> **Created 2026-09-20**, closing part of `discovery/unresolved.md` item
> #5 alongside [[ES-AOC]] and Germany's [[DE-DATAPORT]] / [[DE-AKDB]].
> Sourced from the Basque Government's own euskadi.eus portal, read
> directly.

## Description

EJIE is the **Basque Government's own IT company**, established by
**Decreto 60/1982, de 1 de Febrero** (Decree 60/1982 of 1 February 1982)
as a commercial entity wholly owned and created by the **Gobierno
Vasco / Eusko Jaurlaritza**. It sits under the Department of Governance,
Digital Administration and Self-Government, and manages information
technology and digital administration services across the Basque public
sector, including the **euskadi.eus** government portal itself, web
content management, accessibility standards and IT infrastructure.

## One of four in the Basque interoperability node

Confirmed directly on euskadi.eus's own NISAE page: EJIE is one of **four
public IT companies** — alongside **CCASA, IZFE and LANTIK** — that
jointly constitute the **Nodo de Interoperabilidad y Seguridad de las
Administraciones de Euskadi (NISAE)**, serving the Basque Government and
the three Provincial Councils (Álava, Bizkaia, Gipuzkoa). This is a
four-way structure comparable to how several Belgian and German bodies
this Atlas records split responsibility by level of government, though
here all four sit within one Autonomous Community rather than across
separate ones.

## Wholly government-owned, unlike its Atlas siblings

[[DE-AKDB]] is owned by Bavaria's municipal associations, and [[ES-AOC]]
is a multi-party consortium of the Generalitat de Catalunya and a
local-government association. EJIE is simpler: wholly created and owned
by the Basque Government itself, which is why its `part-of` edge carries
`confidence: high` rather than the `medium` the other two carry for their
more layered ownership.

## Not modelled

- **LANTIK**, the last of EJIE's three NISAE co-members — attempted
  2026-09-20 but not created; `bizkaia.eus`/`lantik.bizkaia.eus` returned
  HTTP 503 on every attempt. **IZFE and CCASA, the other two, are now
  [[ES-IZFE]]** (Gipuzkoa) and **[[ES-CCASA]]** (Álava, added 2026-09-20).
- The **NISAE** interoperability node itself as a separate entity —
  described here in prose as a joint function of the four companies.

## Relationships

- `part-of` [[ES]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly.
