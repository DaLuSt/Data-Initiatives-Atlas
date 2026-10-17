---
id: CI-ARTCI
type: organisation
name: "Autorité de Régulation des Télécommunications/TIC de Côte d'Ivoire"
name_en: "Telecommunications/ICT Regulatory Authority of Côte d'Ivoire (ARTCI)"
alternative_names:
  - "Telecommunications/ICT Regulatory Authority of Côte d'Ivoire (ARTCI)"
  - "ARTCI"
description: >
  Côte d'Ivoire's telecommunications and ICT regulator, created in 2012 as an independent administrative authority with legal personality
  and financial autonomy, with a Regulatory Council of seven members and a Director General. It also presents itself as the personal data
  protection authority under the law of 19 June 2013.

level: national
country: CI
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
  - CI
  - CI-LOI-2013-450
  - CI-LOI-2013-451
  - CI-LOI-2024-352
relationships:
  - type: part-of
    target: CI
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. 'A propos de l'ARTCI' (read 2026-10-17): 'Créée en 2012 sous la forme d'une Autorité Administrative Indépendante dotée de la personnalité juridique et de l'autonomie financière, l'Autorité de Régulation des Télécommunications/TIC de Côte d'Ivoire (ARTCI)'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CI-LOI-2013-450
    source: fact
    evidence: "The data protection page (read 2026-10-17): 'En Côte d'Ivoire, cette protection est encadrée par la loi n°2013-450 du 19 juin 2013 portant protection des données à caractère personnel', and a news item of 3 August 2026 signs 'L'ARTCI, Autorité de Protection des Données Personnelles'."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "A propos de l'ARTCI"
    url: "https://artci.ci/a-propos-de-lartci/"
    publisher: "Autorité de Régulation des Télécommunications/TIC de Côte d'Ivoire"
    accessed: "2026-10-16"
  - title: "Protection des Données — ARTCI"
    url: "https://artci.ci/protection-des-donnees/"
    publisher: "Autorité de Régulation des Télécommunications/TIC de Côte d'Ivoire"
    accessed: "2026-10-16"
  - title: "Lois — ARTCI"
    url: "https://artci.ci/textes-juridiques/lois/"
    publisher: "Autorité de Régulation des Télécommunications/TIC de Côte d'Ivoire"
    accessed: "2026-10-16"
    note: "A list of laws to download; the texts were not opened."
---

# ARTCI (Côte d'Ivoire)

> **Created 2026-10-17** (roadmap #480, Côte d'Ivoire). Read on the regulator's own site (in French). **No `start_date`**: the page says "créée en 2012", a year only. The page's menu also links a separate "Autorité de protection" site (autoritedeprotection.ci), not read.

## What the pages say

- **Organs:** a Regulatory Council of seven members, one of whom is the chair, which carries out the regulatory missions; a Director General, who manages technical, administrative and financial affairs.
- **Powers:** normative; control of legal and regulatory compliance; search and seizure of equipment or installations; investigation; administrative and financial sanctions; first-instance dispute settlement between operators, or between operators and consumers of telecommunications services.
- **Data protection:** the data protection page lists the usual principles (consent and transparency, limited purpose, minimisation, accuracy, security, individuals' rights, restricted international transfer, sanctions) under law 2013-450 and carries the regulator's DCP (personal data) orders and forms. A 2026 communiqué invites controllers to use the CERTINUM platform and signs as "Autorité de Protection des Données Personnelles".

## Relationships

Part of [[CI]]; `governed-by` [[CI-LOI-2013-450]] (medium confidence: the page says the law frames protection and does not itself name the regulator as authority in a quoted sentence).
