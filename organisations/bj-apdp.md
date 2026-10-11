---
id: BJ-APDP
type: organisation
name: "Autorité de Protection des Données à caractère Personnel"
name_en: "Personal Data Protection Authority"
alternative_names:
  - "APDP"
  - "Personal Data Protection Authority"
description: >
  Benin's data-protection authority, to which the government declares its
  website and where individuals can complain, under the Digital Code of
  2018. Its own site is apdp.bj.

level: national
country: BJ
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
  - BJ
  - BJ-CODE-NUMERIQUE
relationships:
  - type: part-of
    target: BJ
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. gouv.bj, read directly (2026-10-11), calls it the 'Autorité de Protection des Données à caractère Personnel' of Benin and gives its address as apdp.bj."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: BJ-CODE-NUMERIQUE
    source: fact
    evidence: "gouv.bj, read directly (2026-10-11): declarations are made to the Authority 'conformément à la loi n° 2017-20 du 20 avril 2018 portant code du numérique en République du Bénin', and a person who thinks their data are not respected may complain to the Authority 'conformément à la procédure légale'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Politique de confidentialité — Présidence de la République du Bénin"
    url: "https://www.gouv.bj/pages/politique-confidentialite/"
    publisher: "Gouvernement du Bénin (gouv.bj)"
    accessed: "2026-10-11"
---

# Autorité de Protection des Données à caractère Personnel (APDP), Benin

> **Created 2026-10-11** (roadmap #471, Benin). Known from the Presidency's privacy page only; the Authority's own site could not be read.

## Description

Benin's data-protection authority. The Presidency's page says its site was declared to the Authority under the Digital Code ([[BJ-CODE-NUMERIQUE]]) and that a person can lodge a complaint or request with it. Its composition, powers and date of creation are not stated on that page and are not asserted; secondary sources describe it as an independent administrative authority created by the Code's personal-data book, which would make it date from the Code, but that was not read.

## Relationships

`part-of` [[BJ]] (anchor edge); `governed-by` [[BJ-CODE-NUMERIQUE]].
