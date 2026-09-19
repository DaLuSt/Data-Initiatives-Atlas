---
id: ES-JEFATURA-DE-INFORMACION
type: organisation
name: Jefatura de Información
alternative_names:
  - Servicio de Información de la Guardia Civil
  - SIGC
description: >
  The Guardia Civil's information and intelligence directorate, commanded
  by a General Officer of the Guardia Civil in active service and
  reporting to the Mando de Operaciones. It organises, directs and manages
  the acquisition, reception, processing, analysis and dissemination of
  information of interest for public order and citizen security within
  the Guardia Civil's jurisdictional scope. It was created by Orden
  PRE/422/2013, which simultaneously suppressed the previously separate
  "Servicio de Información."

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2013-03-15
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - ES-CNI
  - ES
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "PARTIALLY CLOSES discovery/unresolved.md row #193. Confirmed by reading the BOE's own text of Orden PRE/422/2013 directly (boe.es/buscar/act.php?id=BOE-A-2013-2906, 2026-09-19), Article 9: 'A la Jefatura de Información, al mando de un Oficial General de la Guardia Civil en situación de servicio activo, le corresponde organizar, dirigir y gestionar la obtención, recepción, tratamiento, análisis y difusión de la información de interés para el orden público' — it organises, directs and manages the acquisition, reception, processing, analysis and dissemination of information of interest for public order, reporting to the Mando de Operaciones. Scope anchor under metadata/relationship-types.md §2.3: the Guardia Civil itself is not an Atlas entity, so the edge targets the country."
    confidence: medium
    valid_from: "2013-03-15"
    valid_until: null

sources:
  - title: "Orden PRE/422/2013, de 15 de marzo, por la que se desarrolla la estructura orgánica de los Servicios Centrales de la Dirección General de la Guardia Civil"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2013-2906"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
    accessed: "2026-09-19"
---

# Jefatura de Información (Guardia Civil)

> **Created 2026-09-19**, partially closing `discovery/unresolved.md` row
> #193 (the National Police's and Guardia Civil's information services,
> flagged as unresearched on both [[ES-CNI]] and [[ES-CIFAS]]). Sourced
> from the BOE's own text of Orden PRE/422/2013, read directly.

## Description

The Jefatura de Información is the Guardia Civil's own information and
intelligence directorate. Confirmed by reading the BOE's own text of
**Orden PRE/422/2013** directly, its Article 9: it is commanded by a
General Officer of the Guardia Civil in active service, and "corresponds
to organise, direct and manage the acquisition, reception, processing,
analysis and dissemination of information of interest for public order"
within the Guardia Civil's own jurisdictional scope, reporting to the
**Mando de Operaciones**.

## A renamed successor, not a new creation

The same order's Disposición adicional segunda, read directly, **suppresses
the previously separate "Servicio de Información"** and replaces it with
this restructured Jefatura — a rename-with-restructuring rather than an
entirely new body. No `previous_version`/`successor` pair is recorded: the
order does not describe the transition in terms that distinguish "this is
the same body renamed" from "this is a new body absorbing the old one's
functions," and the Atlas's provenance rules do not let that distinction be
assumed either way.

## Not modelled

- The **common inspection regime** [[ES-CNI]]'s own entity says covers
  Spain's intelligence bodies generally — not researched this pass.
- The **Mando de Operaciones**, the Guardia Civil's operational command
  this entity reports to.
- The **Guardia Civil** itself as an organisation entity.

## Relationships

- `part-of` [[ES]] — anchor; the Guardia Civil itself is not an Atlas
  entity.

## Sources

Listed in frontmatter — a single source, read directly.
