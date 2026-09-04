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
verification: primary-source

start_date: 2025-02-21
end_date: null
last_verified: "2026-09-04"
previous_version: ES-SGAD
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES-SGAD
  - ES-DATOS-GOB-ES
  - ES-CLAVE
  - ES-LEY-40-2015
relationships:
  - type: supersedes
    target: ES-SGAD
    source: fact
    evidence: "Confirmed by reading boe.es's own text of Real Decreto 1118/2024 directly (2026-08-26, BOE-A-2024-22929): the Agency was created by Ley 22/2021 (the 2022 General Budget Law), and upon its effective constitution the Secretaría General de Administración Digital and its dependent organs are suppressed, with the Agency 'quedará subrogada en la totalidad de los derechos y obligaciones' (subrogated into the totality of the rights and obligations) of the SGAD, assuming all its contracts and legal relationships — a more precise legal mechanism than the previous search-only evidence captured."
    confidence: high
    valid_from: 2025-02-21
    valid_until: null
  - type: governed-by
    target: ES-LEY-40-2015
    source: fact
    evidence: "A research-queue pickup (2026-09-04) closed the 'no legal-basis entity' gap this file's own Ley 22/2021 citation had left open. Reading Real Decreto 1118/2024's own Article 1.1 directly: 'La Agencia Estatal de Administración Digital... es una entidad de Derecho público regulada en la sección 4.ª del capítulo III del título II de la Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público' (the Agency is a public-law entity regulated under section 4 of chapter III of title II of Ley 40/2015). This is distinct from Ley 22/2021, which created the Agency; Ley 40/2015 supplies the legal form ('agencia estatal') and its operating rules, which is what `governed-by` records here."
    confidence: medium
    valid_from: 2025-02-21
    valid_until: null

sources:
  - title: "Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22929"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "Real Decreto 1125/2024, de 5 de noviembre, por el que se regulan la organización y los instrumentos operativos para la Administración Digital de la Administración del Estado"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2024-22935"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "El Gobierno aprueba la creación de la Agencia Estatal de Administración Digital para acelerar la transformación tecnológica de las Administraciones Públicas"
    url: "http://espanadigital.gob.es/en/actualidad/el-gobierno-aprueba-la-creacion-de-la-agencia-estatal-de-administracion-digital-para"
    publisher: "España Digital 2026"
---

# AEAD — Agencia Estatal de Administración Digital

> **Verified 2026-08-26; legal basis closed 2026-09-04.** boe.es's own
> text of Real Decreto 1118/2024 (BOE-A-2024-22929) was read directly,
> confirming the Agency's legal mechanism for absorbing the SGAD in more
> precise terms than the search-only evidence carried. A research-queue
> pickup then read the same decree's Article 1.1 for a second purpose —
> closing the "no legal-basis entity" gap by creating [[ES-LEY-40-2015]],
> the law that supplies the Agency's legal form.

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

- **RD 1118/2024** approves its statute;
- **RD 1125/2024** regulates the organisation and operational instruments
  for the digital administration of the State.

Confirmed by reading boe.es directly: the Agency itself was created
earlier, by **Ley 22/2021** (the 2022 General Budget Law) — RD 1118/2024
approves the statute that a body created by that law needed before it
could operate, rather than creating the Agency outright. It reports to the
Ministry for Digital Transformation and the Civil Service through the
**State Secretary for the Civil Service**, who serves as its President.

RD 1125/2024, also read directly, names the Agency as the pillar of the
new ICT governance model: it "coordinará funcionalmente las unidades de
Tecnologías de la Información y Comunicaciones" (Art. 4.3), and each
ministerial department must set up its own ICT coordination division
reporting functionally to the Agency (Art. 4.4) — the mechanism behind
the "functionally coordinates the ICT units" line in this entity's
description, previously unsourced to a specific article.

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

- `supersedes` [[ES-SGAD]] — confirmed 2026-08-26 via BOE's own text of RD
  1118/2024, naming the subrogation mechanism directly; `confidence: high`.
- `governed-by` [[ES-LEY-40-2015]] — closed 2026-09-04, via the same
  decree's Article 1.1.

## Sources

Listed in frontmatter. BOE's own text of Real Decreto 1118/2024 and of
Real Decreto 1125/2024 were read directly in the 2026-08-26 pass; the
España Digital 2026 announcement was not re-fetched. RD 1118/2024's
Article 1.1 was read again in the 2026-09-04 pass that closed the
legal-basis gap.
