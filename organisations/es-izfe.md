---
id: ES-IZFE
type: organisation
name: Informatika Zerbitzuen Foru Elkartea
alternative_names:
  - IZFE
  - Sociedad Foral de Servicios Informáticos
description: >
  Provincial (foral) IT services company for Gipuzkoa, in the Basque
  Country, constituted by Decreto Foral 55/1993 of 29 June 1993
  (published in the Boletín Oficial de Gipuzkoa on 9 July 1993) as
  "Informatika Zerbitzuen Foru Elkartea - Sociedad Foral de Servicios
  Informáticos, S.A." Its sole shareholder, from constitution to the
  present, is the Diputación Foral de Gipuzkoa (the provincial
  government). It is the technical instrument through which the
  Diputación Foral pursues its information-systems and technology
  objectives, providing ICT services to the provincial government,
  the wider Gipuzkoan public sector and local administrations across
  the territory, including two data-processing centres and the
  province's corporate network.

level: subnational
country: ES
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 1993-06-29
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-EJIE
  - ES-CCASA
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Confirmed by reading IZFE's own official 2025 budget introduction directly (2026-09-20, published under IZFE's own letterhead): 'Por Decreto Foral 55/1993 de 29 de junio, publicado en el Boletín Oficial de Gipuzkoa de 9 de Julio de 1993, se constituyó la entidad \"Informatika Zerbitzuen Foru Elkartea - Sociedad Foral de Servicios Informáticos, S.A.\", en anagrama Izfe, S.A., cuyo único socio en el momento de la constitución, y a la fecha de hoy, es la Diputación Foral de Gipuzkoa.' The same document states the company is registered in the Registro Mercantil de Gipuzkoa (folio 98, tomo 1374, hoja 7316-1ª) and describes it as 'el instrumento del que se dota la organización de la Diputación Foral' for its information-systems objectives. Anchor edge under metadata/relationship-types.md §2.3, asserting Gipuzkoan (provincial/foral) sub-federal scope via `level: subnational` — a narrower unit than an Autonomous Community, since Gipuzkoa is one of the Basque Country's three historical territories."
    confidence: high
    valid_from: 1993-06-29
    valid_until: null

sources:
  - title: "Presupuesto 2025 — Introducción"
    url: "https://www7.gipuzkoa.net/presupuestos/2025/Ppto2025/pdfs/3/IZFE/I1.pdf"
    publisher: "IZFE, S.A."
    accessed: "2026-09-20"
  - title: "Quiénes somos — IZFE"
    url: "https://www.izfe.eus/es/sobre-izfe/quienes-somos"
    publisher: "IZFE, S.A."
    accessed: "2026-09-20"
---

# IZFE — Informatika Zerbitzuen Foru Elkartea

> **Created 2026-09-20**, further narrowing `discovery/unresolved.md`
> item #5 alongside [[ES-AOC]] and [[ES-EJIE]]. Sourced from IZFE's own
> official 2025 budget document, read directly as a local PDF after
> WebFetch returned only binary content — the same workaround used
> elsewhere in the Atlas for unreadable PDFs.

## Description

IZFE is **Gipuzkoa's** own provincial (foral) IT services company,
constituted by **Decreto Foral 55/1993 of 29 June 1993** (published in
the Boletín Oficial de Gipuzkoa on 9 July 1993). Its own budget document,
read directly, states plainly that its **sole shareholder, from
constitution to the present, is the Diputación Foral de Gipuzkoa** — the
provincial government.

## A third level below the Autonomous Community

[[ES-EJIE]] is wholly owned by the **Basque Government** (the Autonomous
Community level). IZFE sits one level below: Gipuzkoa is one of the
Basque Country's **three historical territories** (alongside Álava and
Bizkaia), each with its own Diputación Foral. Confirmed directly on
euskadi.eus's own NISAE page (already cited on [[ES-EJIE]]): IZFE is one
of the four public IT companies — with EJIE, CCASA and LANTIK — that
jointly constitute the Interoperability and Security Node of the
Administrations of Euskadi, serving the Basque Government and the three
Provincial Councils.

## What it does

IZFE's own page, read directly, describes it as "the technological ally
of the Provincial and Local Administration of Gipuzkoa," providing
services in tax and economic management, social services, e-government
and infrastructure/cybersecurity. Its own budget document adds technical
detail: two data-processing centres and a dual-star-topology corporate
network connecting all provincial sites, interconnected with the rest of
the Basque Country's and Spain's administrations.

## Not modelled

- **LANTIK**, IZFE's and EJIE's last NISAE co-member — attempted
  2026-09-20 but not created; `bizkaia.eus`/`lantik.bizkaia.eus` returned
  HTTP 503 on every attempt. **CCASA, the other, is now [[ES-CCASA]]**
  (Álava's own provincial IT company, added 2026-09-20).

## Relationships

- `part-of` [[ES]] (anchor edge, `level: subnational`).

## Sources

Listed in frontmatter, both read directly — the budget document as a
local PDF via the Read-tool workaround, IZFE's own "Quiénes somos" page
directly via WebFetch.
