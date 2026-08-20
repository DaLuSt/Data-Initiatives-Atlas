---
id: ES-AEAD
type: organisation
name: Agencia Estatal de Administración Digital
alternative_names:
  - AEAD
  - State Agency for Digital Administration
description: >
  Spanish state agency responsible for leading the digitalisation and
  modernisation of public services. A public-law body attached to the
  Ministry for Digital Transformation and the Civil Service, with its own
  legal personality, management autonomy and full competences. Created by
  Real Decreto 1118/2024 of 5 November 2024, which approved its statute, and
  formally constituted on 21 February 2025, replacing the Secretaría General
  de Administración Digital and assuming its functions. It coordinates and
  supervises the ICT services of the General State Administration and
  functionally coordinates the ICT units of state public-sector bodies.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2025-02-21
end_date: null
last_verified: null
previous_version: ES-SGAD
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES-SGAD
  - ES-DATOS-GOB-ES
  - ES-CLAVE
relationships:
  - type: supersedes
    target: ES-SGAD
    source: fact
    evidence: "The Secretaría General de Administración Digital was transformed into the Agencia Estatal de Administración Digital by Real Decreto 1118/2024 of 5 November, which approved its statute; the Agency will replace the current General Secretariat of Digital Administration and assume its functions, and was formally constituted on 21 February 2025 (BOE-A-2024-22929; espanadigital.gob.es 'El Gobierno aprueba la creación de la Agencia Estatal de Administración Digital'). NOT READ — search-only."
    confidence: medium
    valid_from: 2025-02-21
    valid_until: null

sources:
  - title: "Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22929"
    publisher: "Boletín Oficial del Estado (BOE)"
  - title: "Real Decreto 1125/2024, de 5 de noviembre, por el que se regulan la organización y los instrumentos operativos para la Administración Digital de la Administración del Estado"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22935"
    publisher: "Boletín Oficial del Estado (BOE)"
  - title: "El Gobierno aprueba la creación de la Agencia Estatal de Administración Digital para acelerar la transformación tecnológica de las Administraciones Públicas"
    url: "https://espanadigital.gob.es/en/actualidad/el-gobierno-aprueba-la-creacion-de-la-agencia-estatal-de-administracion-digital-para"
    publisher: "España Digital 2026"
---

# AEAD — Agencia Estatal de Administración Digital

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The AEAD is Spain's central digital-government body. It is a **public-law
body attached to the Ministry for Digital Transformation and the Civil
Service**, holding its own legal personality, management autonomy and full
competences to lead the digitalisation of public services.

Its functions include coordinating and supervising the ICT services of the
General State Administration, developing digital services, and
**functionally coordinating the ICT units** of the public-law bodies
attached to or dependent on the state public sector.

Two royal decrees of the same day, 5 November 2024, define it:

- **RD 1118/2024** approves its statute — the instrument that creates it;
- **RD 1125/2024** regulates the organisation and operational instruments
  for the digital administration of the State.

It was **formally constituted on 21 February 2025**.

## The Atlas's first organisational succession

The Atlas already models succession between *documents* — [[NL-EAR]] to
[[NL-RORA]] is an architecture superseding an architecture, and several acts
supersede other acts. This is the first case of **one organisation
superseding another**, and it is worth recording as a modelling result
rather than a Spanish detail.

The pattern is the same one the ontology already provides:

- `ES-SGAD` carries `status: superseded` and `successor: ES-AEAD`;
- this entity carries `previous_version: ES-SGAD` and one `supersedes`
  relationship with `valid_from: 2025-02-21`.

No new relationship type was needed. That is a genuine reusability result:
`supersedes` was introduced for legislation, and it carried an
organisational transformation without modification.

**What the model does not capture** is that this was a *transformation*
rather than an abolition and replacement — the same functions, staff and
remit continued under a new legal form with greater autonomy. `supersedes`
says only that one entity took over from another. The distinction between
succession and transformation is not expressible, and it is not worth a new
relationship type on one sourced example.

## Relationships

- `supersedes` [[ES-SGAD]].

## Sources

Listed in frontmatter — two BOE entries for the constituting decrees and
the government's own announcement.
