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
coverage: medium
verification: primary-source

start_date: null
end_date: 2025-02-21
last_verified: "2026-08-26"
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
    accessed: "2026-08-26"
  - title: "La Secretaría General de la Administración Digital pone en marcha MiFacturae"
    url: "https://avance.digital.gob.es/es-es/notasprensa/Paginas/240320_miFacturae.aspx"
    publisher: "Ministerio para la Transformación Digital y de la Función Pública"
  - title: "Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22929"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
---

# SGAD — Secretaría General de Administración Digital

> **Verified 2026-08-26.** Two of three cited pages were read directly:
> the organisational-unit ficha and BOE's own text of Real Decreto
> 1118/2024. The MiFacturae press note was not re-fetched.

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

Confirmed by reading administracion.gob.es's own organisational-unit ficha
directly (2026-08-26): the SGAD reported to the Ministry through the
**State Secretariat for the Civil Service**, and comprised seven
subordinate divisions spanning cybersecurity planning, digitalisation
promotion, digital infrastructure, IT budgeting and procurement, and
digital governance — internal structure this entity did not previously
record, even though its coverage remains `low` overall.

## Why a superseded organisation is kept

The Atlas retains superseded entities rather than deleting them
(`metadata/ontology.md` — temporal integrity). Deleting this one would make
[[ES-AEAD]]'s `supersedes` relationship dangle, and would erase the fact
that Spain's digital-government function changed legal form in 2025 — a
fact a reader comparing five countries' institutional arrangements would
want.

`coverage: medium`, up from `low`. Previously everything recorded here was
what the successor's creation documents said about it; the SGAD's own
organisational-unit ficha, read directly this pass, now supplies its
ministry attachment and its seven subordinate divisions. **Its founding
date and full remit remain unrecorded**, so nothing about those is
asserted.

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

Listed in frontmatter, two of three read directly this pass: the
organisational-unit ficha (describing the body itself) and BOE's own text
of Real Decreto 1118/2024 (describing its replacement). The MiFacturae
press note was not re-fetched.
