---
id: ES-CCN
type: organisation
name: Centro Criptológico Nacional
alternative_names:
  - CCN
  - CCN-CERT
  - National Cryptologic Centre
description: >
  Spanish public-sector cybersecurity body attached to the national
  intelligence centre, and the technical authority for the Esquema Nacional
  de Seguridad. Real Decreto 311/2022 assigns it the role of state-level
  public coordinator for the technical response of incident response teams
  through CCN-CERT, and the development of awareness, training and
  sensitisation programmes for public-sector personnel. It publishes the
  CCN-STIC guides and operates the INES measurement tool, and its
  certification body determines functional security and assurance
  requirements for the national evaluation and certification scheme.

level: national
country: ES
region: null

status: active
confidence: medium
coverage: low
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
  - ES-ENS
  - ES-INCIBE
relationships: []

sources:
  - title: "Actualizadas las preguntas frecuentes del nuevo ENS"
    url: "https://www.ccn.cni.es/index.php/es/actualidad-ccn/931-actualizadas-las-preguntas-frecuentes-del-nuevo-ens"
    publisher: "Centro Criptológico Nacional (CCN) — CNI"
  - title: "BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191"
    publisher: "Boletín Oficial del Estado (BOE)"
  - title: "Esquema Nacional de Seguridad"
    url: "https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx"
    publisher: "Ministerio de Economía, Comercio y Empresa"
---

# CCN — Centro Criptológico Nacional

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The CCN is Spain's public-sector cybersecurity body, attached to the
national intelligence centre (CNI), and the **technical authority for
[[ES-ENS]]**.

Real Decreto 311/2022 assigns it two named roles:

1. **state-level public coordinator** for the technical response of incident
   response teams, through **CCN-CERT**;
2. development of **awareness, training and sensitisation** programmes for
   public-sector personnel.

It publishes the **CCN-STIC guides** and operates **INES**, the compliance
measurement tool, and its certification body determines functional security
and assurance requirements under the national evaluation and certification
scheme for information technologies.

## Relationships

The `maintained-by` edge for [[ES-ENS]] lives **on [[ES-ENS]]**, pointing
here — `metadata/relationship-types.md` §2.1 defines `maintained-by` as
*"the target organisation maintains this entity"*, so it belongs on the
maintained thing.

## Sources

Listed in frontmatter — the CCN's own ENS FAQ notice, the BOE text of the
decree that assigns it these roles, and a ministry page.
