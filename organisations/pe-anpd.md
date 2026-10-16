---
id: PE-ANPD
type: organisation
name: "Autoridad Nacional de Protección de Datos Personales"
name_en: "National Authority for Personal Data Protection (ANPD)"
alternative_names:
  - "National Authority for Personal Data Protection (ANPD)"
  - "ANPD"
description: >
  Peru's personal data protection authority. Law 29733 makes the Ministry of Justice and Human Rights the Authority; in practice
  the Ministry's directorate-general that exercises it issues regulations, runs the national registry of personal data and
  sanctions infringements.

level: national
country: PE
region: null

status: active
organisation_role: regulatory
confidence: medium
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
  - PE
  - PE-LEY-29733
  - PE-DS-016-2024-JUS
relationships:
  - type: part-of
    target: PE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Ministry's press note of 30 November 2024 (read 2026-10-16) describes it as exercised from the Ministry of Justice and Human Rights' 'Dirección General que ejerce la Autoridad Nacional de Protección de Datos Personales (ANPD)'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: PE-LEY-29733
    source: fact
    evidence: "Art. 32 of Law 29733 (read 2026-10-16): the Ministry of Justice, through its national directorate, 'es la Autoridad Nacional de Protección de Datos Personales'; it is governed by the law, its regulation and the Ministry's organisation rules."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Ley de Protección de Datos Personales, Ley N° 29733 (Editora Perú, normas legales actualizadas)"
    url: "https://cdn.www.gob.pe/uploads/document/file/272360/Ley%20N%C2%BA%2029733.pdf.pdf?v=1618338779"
    publisher: "Editora Perú, hosted on gob.pe"
    accessed: "2026-10-16"
    note: "Read as text. It is an older consolidated edition with the 2013 regulation; the 2024 regulation replaces that one."
  - title: "Ejecutivo aprueba nuevo reglamento de la ley de Protección de Datos Personales"
    url: "https://www.gob.pe/institucion/minjus/noticias/1067368-ejecutivo-aprueba-nuevo-reglamento-de-la-ley-de-proteccion-de-datos-personales"
    publisher: "Ministerio de Justicia y Derechos Humanos (Perú)"
    accessed: "2026-10-16"
---

# Autoridad Nacional de Protección de Datos Personales (Peru)

> **Created 2026-10-16** (roadmap #478, Peru). Known from the law and two Ministry press notes. The Authority is a function of the Ministry of Justice and Human Rights, not a separate legal person; its own page (on minjus.gob.pe) was not read. No founding date is recorded.

## What is sourced

Art. 32 of [[PE-LEY-29733]] names the Ministry of Justice as the Authority and lets it open offices nationwide. The Ministry's 2024 note names the director general who promoted the new regulation ([[PE-DS-016-2024-JUS]]) and the Authority's role in clarifying how it applies; the March 2025 note has the Ministry and the Authority clarifying the advertising-call consent rules.

## Relationships

Part of [[PE]]; `governed-by` [[PE-LEY-29733]].
