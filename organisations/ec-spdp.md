---
id: EC-SPDP
type: organisation
name: "Superintendencia de Protección de Datos Personales"
name_en: "Superintendency of Personal Data Protection (SPDP)"
alternative_names:
  - "Superintendency of Personal Data Protection (SPDP)"
  - "SPDP"
  - "Autoridad de Protección de Datos Personales (Ecuador)"
description: >
  Ecuador's data protection authority. Its own site says it guides, regulates and supervises compliance with the Organic Law on
  Personal Data Protection to guarantee people's rights and privacy. It publishes resolutions, answered consultations and draft
  rules for public comment, and has issued its first penalties for serious infringements.

level: national
country: EC
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EC
  - EC-LOPDP
relationships:
  - type: part-of
    target: EC
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Superintendency's home page (read 2026-10-16): 'La SPDP orienta, regula y supervisa el cumplimiento de la Ley Orgánica de Protección de Datos Personales para garantizar tus derechos y la privacidad'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EC-LOPDP
    source: fact
    evidence: "The same page (read 2026-10-16) names the Organic Law on Personal Data Protection as what it supervises, and arts. 75-77 of the law (read the same day) set up the authority and its Superintendent."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Superintendencia de Protección de Datos Personales — inicio"
    url: "https://spdp.gob.ec/"
    publisher: "Superintendencia de Protección de Datos Personales (Ecuador)"
    accessed: "2026-10-16"
  - title: "Ley Orgánica de Protección de Datos Personales, Registro Oficial Suplemento 459 de 26-may.-2021 (Lexis, on finanzaspopulares.gob.ec)"
    url: "https://www.finanzaspopulares.gob.ec/wp-content/uploads/2021/07/ley_organica_de_proteccion_de_datos_personales.pdf"
    publisher: "Asamblea Nacional / Registro Oficial (Ecuador), copy hosted by the Corporación Nacional de Finanzas Populares y Solidarias"
    accessed: "2026-10-16"
    note: "Read as text, 40+ pages; the copy carries the Registro Oficial header and the signatures."
---

# Superintendencia de Protección de Datos Personales (Ecuador)

> **Created 2026-10-16** (roadmap #478, Ecuador). Read on the Superintendency's own site, spdp.gob.ec, and in the law that sets up the authority ([[EC-LOPDP]], arts. 75-77). The home page does not give a founding date, so none is recorded.

## What the home page says

Quick-access sections for resolutions, answered consultations, draft rules ("Proyectos Normativos", for citizen participation), online services and a complaints form; a national plan; programmes approved for professional training; "Resoluciones de Procedimientos Administrativos Sancionadores: La SPDP emite sus primeras sanciones por infracciones graves a la Ley Orgánica de Protección de Datos Personales". A news item says the Superintendency works so that rules are "proporcional y de fácil aplicación" for small businesses.

## Relationships

Part of [[EC]]; `governed-by` [[EC-LOPDP]].
