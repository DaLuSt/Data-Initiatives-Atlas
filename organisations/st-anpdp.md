---
id: ST-ANPDP
type: organisation
name: "Agência Nacional de Protecção de Dados Pessoais"
name_en: "National Personal Data Protection Agency"
alternative_names:
  - "ANPDP"
  - "National Personal Data Protection Agency"
description: >
  São Tomé and Príncipe's national personal-data protection agency, provided
  for by Article 44 of Lei 03/2016. Whether it is operating was not
  established.

level: national
country: ST
region: null

status: active
organisation_role: regulatory
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ST
  - ST-LEI-03-2016
relationships:
  - type: part-of
    target: ST
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Article 44 of the law, in the text read (2026-10-11), names the 'Agence Nationale de Protection des Données Personnelles (ANPDP)'."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: ST-LEI-03-2016
    source: fact
    evidence: "Article 44, 'Agence Nationale de Protection des Données Personnelles', in the text read (2026-10-11): its organic law and staff are approved by a law of the National Assembly; its members' status guarantees independence; it has its own technical and administrative support. Article 3 refers to a communication 'avec l'Agence Nationale de Protection des Données Personnelles (ANPDP)' for designating a representative."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Loi n° 03/2016 — Protection des Données Personnelles (French translation hosted by the AFAPDP)"
    url: "https://www.afapdp.org/wp-content/uploads/2022/02/Loi-de-Protection-des-Donnes-Personnlles-03_2016.pdf"
    publisher: "Assembleia Nacional de São Tomé e Príncipe (copy hosted by the Association francophone des autorités de protection des données personnelles)"
    accessed: "2026-10-11"
---

# Agência Nacional de Protecção de Dados Pessoais (ANPDP), São Tomé and Príncipe

> **Created 2026-10-11** (roadmap #472, São Tomé and Príncipe). Known from the law that provides for it, in a French rendering; whether it is operating and its own site were not established.

## Description

The national data-protection agency provided for by Article 44 of [[ST-LEI-03-2016]], with independent members, its own support staff and an organic law to be passed by the National Assembly. Per the same text, controllers outside the country designate a local representative by communicating with it.

## Relationships

`part-of` [[ST]] (anchor edge); `governed-by` [[ST-LEI-03-2016]].
