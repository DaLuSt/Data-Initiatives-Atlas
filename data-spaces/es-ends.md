---
id: ES-ENDS
type: data-space
name: "Espacio Nacional de Datos de Salud"
alternative_names:
  - "ENDS"
  - "Spain's National Health Data Space"
  - "National Health Data Space (Spain)"
description: >
  Spain's national health data space, which the Ministry of Health says is under development, an initiative to favour a safer, more interoperable
  and more useful use of health data within the National Health System. Known only from the Ministry's Salud Digital page; its legal basis, its
  timetable and its relation to the European Health Data Space were not read.

level: national
country: ES
region: null

status: planned
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - ES-ODSNS

related_entities:
  - ES
  - EU-EHDS
  - ES-ODSNS
relationships:
  - type: related-to
    target: EU-EHDS
    source: fact
    evidence: "The Ministry's Salud Digital page (read directly 2026-11-01): 'la Unión Europea (UE) impulsa el Espacio Europeo de Datos de Salud ... En este marco, España participa en distintas iniciativas para seguir avanzando en interoperabilidad y en el intercambio seguro de información clínica.' It does not say the national space is built on the European one."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: ES-ODSNS
    source: fact
    evidence: "The same page: 'se ha creado la Oficina del Dato del SNS (ODSNS) como estructura de gobernanza, gestión y coordinación del dato sanitario'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "The page: the Ministry of Health and the autonomous communities work within the National Health System (SNS) so that health information can be shared; the national health data space is a national initiative."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Ministerio de Sanidad — Salud Digital: Quiénes somos"
    url: "https://www.sanidad.gob.es/areas/saludDigital/home.htm"
    publisher: "Ministerio de Sanidad (Spain)"
    accessed: "2026-11-01"
---

# Espacio Nacional de Datos de Salud (ENDS)

> **Created 2026-11-01** (roadmap #460, health data). Known **only** from the Ministry's Salud Digital page, read directly (Spanish): "también se está desarrollando el Espacio Nacional de Datos de Salud (ENDS), una iniciativa orientada a favorecer un uso más seguro, interoperable y útil de los datos sanitarios". Hence `status: planned`. The Ministry's strategy documents were not read.

## Relationships

`related-to` [[EU-EHDS]] (medium), [[ES-ODSNS]]; `applies-in` Spain (medium).

## Sources

Listed in frontmatter, read directly.
