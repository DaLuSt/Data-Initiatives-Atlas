---
id: ES-ODSNS
type: organisation
name: "Oficina del Dato del Sistema Nacional de Salud"
alternative_names:
  - "ODSNS"
  - "SNS Data Office"
  - "Oficina del Dato del SNS"
description: >
  The governance, management and coordination structure for health data that the Spanish Ministry of Health says has been created for the National Health
  System. Known only from one sentence on the Ministry's Salud Digital page; its creating act and date were not read.

level: national
country: ES
region: null

status: active
organisation_role: advisory
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
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-ENDS
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "The Ministry of Health's page (read directly 2026-11-01) presents the Oficina del Dato del SNS as part of the National Health System's data governance: 'se ha creado la Oficina del Dato del SNS (ODSNS) como estructura de gobernanza, gestión y coordinación del dato sanitario'. Which body it sits in was not stated, so medium confidence."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: ES-ENDS
    source: fact
    evidence: "The same sentence follows the one on the National Health Data Space under development."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Ministerio de Sanidad — Salud Digital: Quiénes somos"
    url: "https://www.sanidad.gob.es/areas/saludDigital/home.htm"
    publisher: "Ministerio de Sanidad (Spain)"
    accessed: "2026-11-01"
---

# Oficina del Dato del SNS (ODSNS)

> **Created 2026-11-01** (roadmap #460). Known **only** from one sentence of the Ministry's page; the act that created it, its date, its members and its place in the Ministry were not read, so none is recorded.

## What the page says

"se ha creado la Oficina del Dato del SNS (ODSNS) como estructura de gobernanza, gestión y coordinación del dato sanitario." The page also names the SNS Digital Health Strategy, the SNS Artificial Intelligence Strategy and the SNS Cybersecurity Strategy as the common framework, and the Individual Health Card, the SNS Digital Clinical Record and the SNS e-prescription as the shared tools; none of those is modelled.

## Relationships

`part-of` Spain (medium); `related-to` [[ES-ENDS]] (medium).

## Sources

Listed in frontmatter, read directly.
