---
id: FR-RGS
type: standard
name: Référentiel Général de Sécurité
alternative_names:
  - RGS
  - General Security Framework (France)
description: >
  French general security framework, setting mandatory rules for the
  functions of administrative information systems that contribute to
  the security of electronically exchanged information — identification,
  electronic signature, confidentiality and timestamping — and offering
  optional best practices beyond those minimums. Established by Décret
  n° 2010-112 of 2 February 2010, implementing Articles 9, 10 and 12 of
  [[FR-ORDONNANCE-2005-1516]]. ANSSI, in co-construction with DINUM, is
  responsible for keeping the framework's requirements up to date; the
  framework and any updates require Prime Ministerial approval before
  publication in the Official Journal. It defines three graduated
  security levels — RGS*, RGS** and RGS*** — matched to the sensitivity
  of the data and exchanges concerned.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2010-02-02
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
  - DOMAIN-GOVERNMENT
organisations:
  - FR-DINUM
  - FR-ANSSI
related_entities:
  - FR-ORDONNANCE-2005-1516
  - FR-RGI
relationships:
  - type: maintained-by
    target: FR-DINUM
    source: fact
    evidence: "Confirmed by reading numerique.gouv.fr's own RGS page directly (2026-09-04), which lists DINUM as the page's owner and states the RGS derives from Article 9 of ordonnance n° 2005-1516, providing administrations the guidance needed to implement that ordinance's requirements."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: FR-ANSSI
    source: fact
    evidence: "Confirmed by reading cyber.gouv.fr's own RGS regulation page directly (2026-09-04) — ANSSI's own site, in the state's own words: 'L'ANSSI, en co-construction avec la Direction interministérielle du numérique, est responsable du maintien à jour des exigences du référentiel général de sécurité' (ANSSI, in co-construction with DINUM, is responsible for keeping the RGS's requirements up to date)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: FR-ORDONNANCE-2005-1516
    source: fact
    evidence: "Confirmed by reading legifrance.gouv.fr's own text of Décret n° 2010-112 du 2 février 2010 directly (2026-09-04): the decree implements Articles 9, 10 and 12 of ordonnance n° 2005-1516, establishing rules to which information-system functions contributing to the security of electronically exchanged information must conform, and providing that the RGS and its updates require Prime Ministerial approval and Official Journal publication, with ANSSI participating in its development and updating."
    confidence: high
    valid_from: 2010-02-02
    valid_until: null

sources:
  - title: "Décret n° 2010-112 du 2 février 2010 pris pour l'application des articles 9, 10 et 12 de l'ordonnance n° 2005-1516"
    url: "https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000021779444"
    publisher: "Légifrance"
    accessed: "2026-09-04"
  - title: "Référentiel général de sécurité (RGS)"
    url: "https://www.numerique.gouv.fr/offre-accompagnement/reference-securite-rgs/"
    publisher: "DINUM — numerique.gouv.fr"
    accessed: "2026-09-04"
  - title: "Le référentiel général de sécurité (RGS)"
    url: "https://cyber.gouv.fr/reglementation/reglementation-identite-confiance-numerique/securite-echanges-voie-electronique/referentiel-general-de-securite/"
    publisher: "ANSSI — cyber.gouv.fr"
    accessed: "2026-09-04"
---

# Référentiel Général de Sécurité (RGS)

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged the RGS as a sibling of
> [[FR-RGI]], not yet modelled. All three cited pages were read
> directly this pass, including both institutions the RGS names as its
> joint stewards.

## Description

The RGS sets mandatory rules for administrative information systems'
security functions — identification, electronic signature,
confidentiality and timestamping — and offers optional best practices
beyond the mandatory minimum. It defines three graduated certification
levels, **RGS\*, RGS\*\* and RGS\*\*\***, matched to data sensitivity.

## Established by decree, five years after its parent ordinance

Reading `legifrance.gouv.fr`'s own text of **Décret n° 2010-112 du 2
février 2010** directly: it implements **Articles 9, 10 and 12** of
[[FR-ORDONNANCE-2005-1516]] — the same 2005 ordinance whose **Article
11** separately founds [[FR-RGI]]. The decree provides that the RGS and
any updates require **Prime Ministerial approval** before publication
in the Official Journal.

## Co-constructed by two institutions, not one

Unlike [[FR-RGI]] and the RGAA, both maintained solely by [[FR-DINUM]],
the RGS names **two** joint stewards. Reading ANSSI's own site
(`cyber.gouv.fr`) directly, in the state's own words: **"L'ANSSI, en
co-construction avec la Direction interministérielle du numérique, est
responsable du maintien à jour des exigences du référentiel général de
sécurité"** (ANSSI, in co-construction with DINUM, is responsible for
keeping the RGS's requirements up to date). DINUM's own page
independently confirms its role, without mentioning ANSSI directly —
each institution's own site names itself and, in ANSSI's case, its
co-steward.

## Not modelled

- **RGAA** (Référentiel Général d'Amélioration de l'Accessibilité), the
  third référentiel in this family, resting on a different legal basis
  (the 2005 disability-rights law, not this ordinance) — queued
  separately.

## Relationships

- `maintained-by` [[FR-DINUM]].
- `maintained-by` [[FR-ANSSI]].
- `governed-by` [[FR-ORDONNANCE-2005-1516]].

## Sources

Listed in frontmatter, all three read directly this pass.
