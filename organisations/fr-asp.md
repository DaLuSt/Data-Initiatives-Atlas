---
id: FR-ASP
type: organisation
name: "Autorité de la statistique publique"
name_en: "Public Statistics Authority"
alternative_names:
  - "ASP"
  - "Public Statistics Authority"
description: >
  French independent authority that oversees the professional independence
  and quality of public statistics, created by article 144 of the 2008 law
  on the modernisation of the economy and with missions set by decree n°
  2009-250 of 3 March 2009. It has nine members.

level: national
country: FR
region: null

status: active
organisation_role: regulatory
confidence: medium
coverage: low
verification: primary-source
start_date: 2008-08-04
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR
  - FR-INSEE
  - EU-ESGAB
relationships:
  - type: part-of
    target: FR
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Insee's own page, read directly (2026-10-11): 'La création de l'Autorité résulte de l'article 144 de la loi de modernisation de l'économie du 4 août 2008' and 'Les missions de l'Autorité de la statistique publique sont définies par le décret n°2009-250 du 3 mars 2009 modifié'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: FR-INSEE
    source: fact
    evidence: "The Autorité oversees the professional independence of public statistics produced within the French public statistical system, to which Insee belongs. The two pages read (Insee's and the Cnis's, 2026-10-11) say the Autorité 'veille au principe d'indépendance professionnelle' and 'se réfère au code des bonnes pratiques de la statistique européenne'; neither describes a formal link between the Autorité and Insee, so this is an association only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "L'Autorité de la statistique publique (ASP)"
    url: "https://insee.fr/fr/information/2012500"
    publisher: "Insee"
    accessed: "2026-10-11"
  - title: "L'Autorité de la statistique publique (ASP)"
    url: "https://www.cnis.fr/lautorite-de-la-statistique-publique-asp/"
    publisher: "Cnis — Conseil national de l'information statistique"
    accessed: "2026-10-11"
---

# Autorité de la statistique publique (ASP)

> **Created 2026-10-11** (roadmap #459). Insee's page and the Cnis's page on the Autorité were read directly. Its own site (`autorite-statistique-publique.fr`) was not read. The article of the 1951 statistics law that holds its membership rules was not checked on Légifrance.

## Description

The Autorité de la statistique publique oversees the professional independence of public statistics in France, and watches over their quality and methodological rigour, by reference to the European Statistics Code of Practice. Its creation results from article 144 of the *loi de modernisation de l'économie* of 4 August 2008 (Insee's page), and its missions are set by décret n° 2009-250 of 3 March 2009, as amended. Per the Cnis's page it has nine members: a president appointed in the Council of Ministers, members named by the presidents of the Senate and the National Assembly, the Conseil économique, social et environnemental, the Cour des comptes and the Inspections générales, and the minister for the economy, and one *conseiller d'État* who also chairs the statistical secrecy committee. It can issue general opinions, make observations to those who do not comply, and act when asked or on its own initiative.

It is one of three pillars of the French statistical system, alongside the Cnis (the consultation body) and the public statistical service; the Cnis handles consultation upstream and the Autorité oversees quality and independence.

## Relationships

`part-of` [[FR]] (anchor edge); `related-to` [[FR-INSEE]] (association only).
