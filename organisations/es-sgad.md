---
id: ES-SGAD
type: organisation
name: Secretaría General de Administración Digital
alternative_names:
  - SGAD
  - General Secretariat for Digital Administration
description: >
  Former Spanish central digital-government body, dependent on the Ministry
  for Digital Transformation and the Civil Service, responsible for
  promoting the use of information and communication technologies in the
  General State Administration and its public bodies. Its main task was the
  coordination and deployment of the Plan for the Digitalisation of Public
  Administrations, part of Component 11 of the Recovery Plan and aligned
  with the España Digital 2026 agenda. Transformed into the Agencia Estatal
  de Administración Digital by Real Decreto 1118/2024.

level: national
country: ES
region: EU

status: superseded
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: 2025-02-21
last_verified: null
previous_version: null
successor: ES-AEAD

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES-AEAD
  - ES-ESPANA-DIGITAL-2026
relationships: []

sources:
  - title: "Secretaría General de Administración Digital — ficha de unidad orgánica"
    url: "https://administracion.gob.es/pagFront/espanaAdmon/directorioOrganigrama/fichaUnidadOrganica.htm?codigoUnidad=E04995903"
    publisher: "Punto de Acceso General (administracion.gob.es)"
  - title: "La Secretaría General de la Administración Digital pone en marcha MiFacturae"
    url: "https://avance.digital.gob.es/es-es/notasprensa/Paginas/240320_miFacturae.aspx"
    publisher: "Ministerio para la Transformación Digital y de la Función Pública"
  - title: "Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22929"
    publisher: "Boletín Oficial del Estado (BOE)"
---

# SGAD — Secretaría General de Administración Digital

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The SGAD was the body responsible for promoting the use of ICT across the
General State Administration and its public bodies, dependent on the
Ministry for Digital Transformation and the Civil Service.

Its principal objective was the **coordination and deployment of the Plan
for the Digitalisation of Public Administrations**, the Spanish
government's roadmap for digitalising the country, forming Component 11 of
the Recovery Plan and aligned with [[ES-ESPANA-DIGITAL-2026]].

It was transformed into [[ES-AEAD]] by Real Decreto 1118/2024, the successor
being formally constituted on **21 February 2025**.

## Why a superseded organisation is kept

The Atlas retains superseded entities rather than deleting them
(`metadata/ontology.md` — temporal integrity). Deleting this one would make
[[ES-AEAD]]'s `supersedes` relationship dangle, and would erase the fact
that Spain's digital-government function changed legal form in 2025 — a
fact a reader comparing five countries' institutional arrangements would
want.

`coverage: low` is deliberate. Everything recorded here is what the
successor's creation documents say about it. **No source read describes the
SGAD's own founding, its internal structure or its full remit**, so nothing
about those is asserted.

## The direction of the succession edge

The `supersedes` relationship lives on [[ES-AEAD]], not here — the newer
entity points back at the older one, matching how the Atlas records
[[NL-RORA]] → [[NL-EAR]] and [[DE-NIS2UMSUCG]] → [[DE-BSIG]].

This entity carries the succession only through the scalar fields
`status: superseded`, `end_date` and `successor`, which is what the schema
provides for the passive side. Adding a mirror relationship here would
double-count the edge in the generated graph.

## Relationships

None asserted. The succession is recorded on [[ES-AEAD]] and through this
entity's `successor` field.

## Sources

Listed in frontmatter. Note the asymmetry: two of the three describe the
body's *replacement* rather than the body itself, which is why coverage is
low.
