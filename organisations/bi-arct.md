---
id: BI-ARCT
type: organisation
name: "Telecommunications Regulatory and Control Agency (ARCT, Burundi)"
alternative_names:
  - "ARCT"
  - "Agence de Régulation et de Contrôle des Télécommunications"
description: >
  Burundi's telecommunications regulator. Its site lists certification, spectrum (frequency table and assignment), licences, authorisations, numbering and regulations as its services. Its Décrets et Lois page lists Décret n° 100/112 of 5 April 2012 'portant réorganisation et fonctionnement de l'agence de régulation et de contrôle des télécommunications (ARCT)' and decrees on the universal service fund (100/186 of 16 October 2017), the national internet exchange point (100/122 of 13 May 2014) and the digital migration.
  The home page states no founding law and no mandate text; none of the decrees was opened.

level: national
country: BI
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - BI
  - BI-DECRET-LOI-1-011-1997
relationships:
  - type: part-of
    target: BI
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. ARCT's home page and Décrets et Lois page (read 2026-11-06 through a summarising fetch tool): a statutory agency reorganised by Décret n° 100/112 of 5 April 2012."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: BI-DECRET-LOI-1-011-1997
    source: fact
    evidence: "ARCT's Décrets et Lois page lists the Décret-Loi N° 1/011 of 4 September 1997 'portant dispositions organiques sur les télécommunications' as the sector's organic law."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ARCT (Agence de Régulation et de Contrôle des Télécommunications), Burundi, page d'accueil"
    url: "https://www.arct.gov.bi"
    publisher: "ARCT, Burundi"
    accessed: "2026-11-06"
  - title: "ARCT, Décrets et Lois"
    url: "https://arct.gov.bi/decret-et-lois/"
    publisher: "ARCT, Burundi"
    accessed: "2026-11-06"
---

# Telecommunications Regulatory and Control Agency (ARCT, Burundi)

> **Created 2026-11-06** (roadmap #476). From the regulator's own pages through a summarising fetch tool. `start_date` empty: only the 2012 reorganisation decree's date was read.

## Relationships

Part of [[BI]]; governed by [[BI-DECRET-LOI-1-011-1997]].
