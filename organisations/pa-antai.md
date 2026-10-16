---
id: PA-ANTAI
type: organisation
name: "Autoridad Nacional de Transparencia y Acceso a la Información"
name_en: "National Authority for Transparency and Access to Information (ANTAI)"
alternative_names:
  - "National Authority for Transparency and Access to Information (ANTAI)"
  - "ANTAI"
description: >
  Panama's authority for transparency and access to public information,
  created by Law 33 of 25 April 2013. Its Directorate of Personal Data
  Protection is the body that regulates and supervises personal data
  processing under Law 81 of 2019, and it runs the national open data
  policy.

level: national
country: PA
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: 2013-04-25
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PA
  - PA-LEY-81-2019
  - PA-DE-285-2021
  - PA-OPEN-DATA-POLICY
relationships:
  - type: part-of
    target: PA
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. ANTAI's open data policy page (read 2026-10-16) cites 'la Ley 33 de 25 de abril de 2013, que crea la Autoridad Nacional de Transparencia y Acceso a la Información'."
    confidence: high
    valid_from: 2013-04-25
    valid_until: null
  - type: governed-by
    target: PA-LEY-81-2019
    source: fact
    evidence: "The Directorate of Personal Data Protection page (read 2026-10-16) lists as its function to 'garantizar el cumplimiento de las disposiciones legales establecidas en la Ley Protección de Datos Personales' and to regulate public and private bodies that process personal data, citing art. 33 of Ley 81 de 2019."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Dirección Protección de Datos Personales"
    url: "https://antai.gob.pa/direccion-de-proteccion-de-datos-personales/"
    publisher: "Autoridad Nacional de Transparencia y Acceso a la Información (Panama)"
    accessed: "2026-10-16"
  - title: "Política Pública de Datos Abiertos de Gobierno"
    url: "https://antai.gob.pa/politica-publica-de-datos-abiertos-de-gobierno/"
    publisher: "Autoridad Nacional de Transparencia y Acceso a la Información (Panama)"
    accessed: "2026-10-16"
  - title: "ANTAI — home page"
    url: "https://www.antai.gob.pa/"
    publisher: "Autoridad Nacional de Transparencia y Acceso a la Información (Panama)"
    accessed: "2026-10-16"
---

# ANTAI (Panama)

> **Created 2026-10-16** (roadmap #479, Panama). Read on ANTAI's own site. `start_date` is the date of Law 33, the law that created it; when ANTAI began operating was not read.

## What the pages say

The **Directorate of Personal Data Protection** has as its objective to promote respect for and protection of the right to privacy; its functions include assessments and reports on personal data processing (it may require documentation and certifications from controllers through their data protection officers), adopting model contractual clauses for intra- and cross-border transfers (art. 33 of Law 81 of 2019), regulating and supervising public and private bodies that process or hold personal data, and handling complaints. Its **Directorate of Transparency** and its open data working group run the open data side ([[PA-OPEN-DATA-POLICY]]). The FAQ page publishes ANTAI's binding opinions, for example Opinion No. 02-2022 of 27 May 2022 on photographing identity documents without consent.

## Relationships

Part of [[PA]]; `governed-by` [[PA-LEY-81-2019]]; its personal-data complaint procedure refers to [[PA-DE-285-2021]].
