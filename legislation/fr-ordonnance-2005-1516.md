---
id: FR-ORDONNANCE-2005-1516
type: law
name: Ordonnance n° 2005-1516 du 8 décembre 2005 relative aux échanges électroniques entre les usagers et les autorités administratives et entre les autorités administratives
alternative_names:
  - Ordonnance n° 2005-1516
description: >
  French ordinance of 8 December 2005 on electronic exchanges between
  users and administrative authorities, and between administrative
  authorities themselves. Article 11 requires administrative
  authorities, including local authorities, to comply with technical
  interoperability rules — the legal foundation for the Référentiel
  général d'interopérabilité (RGI). Articles 9, 10 and 12 provide for
  the Référentiel Général de Sécurité (RGS), implemented by Décret n°
  2010-112 of 2 February 2010.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2005-12-08
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR
  - FR-RGI
  - FR-RGS
relationships:
  - type: applies-in
    target: FR
    source: fact
    evidence: "Confirmed by reading numerique.gouv.fr's own RGI page directly (2026-08-26, carried forward from FR-RGI's own sourcing): 'Le RGI est défini dans l'ordonnance n° 2005-1516 du 8 décembre 2005... Dans l'article 11 de cette ordonnance, le RGI fixe les règles techniques permettant d'assurer l'interopérabilité des systèmes d'information' (the RGI is defined in ordonnance n° 2005-1516 of 8 December 2005... under Article 11, the RGI sets the technical rules ensuring interoperability of information systems). Confirmed independently by reading legifrance.gouv.fr's own text of Décret n° 2010-112 directly (2026-09-04), which implements the ordinance's Articles 9, 10 and 12 to establish the Référentiel Général de Sécurité. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 2005-12-08
    valid_until: null

sources:
  - title: "Décret n° 2010-112 du 2 février 2010 pris pour l'application des articles 9, 10 et 12 de l'ordonnance n° 2005-1516"
    url: "https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000021779444"
    publisher: "Légifrance"
    accessed: "2026-09-04"
  - title: "Référentiel général d'interopérabilité (RGI)"
    url: "https://www.numerique.gouv.fr/offre-accompagnement/reference-interoperabilite-rgi/"
    publisher: "DINUM — numerique.gouv.fr"
    accessed: "2026-08-26"
---

# Ordonnance n° 2005-1516

> **Added 2026-09-04, `verification: primary-source` from creation.**
> [[FR-RGI]]'s own file had already quoted this ordinance's Article 11
> verbatim but declined to create an entity for it. This entity closes
> that gap, and reading `legifrance.gouv.fr`'s own text of the
> implementing Décret n° 2010-112 directly this pass finds the same
> ordinance is also the legal basis for the Référentiel Général de
> Sécurité ([[FR-RGS]]), a connection [[FR-RGI]]'s own file did not
> record.

## Description

France's foundational law on electronic administration, in force since
**8 December 2005**. Reading `legifrance.gouv.fr`'s own text of its
implementing decree directly: **Article 11** requires administrative
authorities, including local authorities, to comply with technical
interoperability rules, establishing [[FR-RGI]]. **Articles 9, 10 and
12** provide for a security framework, implemented five years later by
**Décret n° 2010-112 du 2 février 2010** as the [[FR-RGS]].

## One ordinance, two référentiels

[[FR-RGI]]'s own entity records this ordinance as its sole legal
foundation, at Article 11. Reading the RGS's own implementing decree
directly this pass finds the **same ordinance**, at different articles,
is also the RGS's foundation — the two flagship "référentiels" of
French e-government law share one parent instrument, cited by different
article numbers for different subject matter, the same shape
[[AT-EGOVG]] and [[IT-CAD]] each show for their own multiple
descendants.

## Relationships

- `applies-in` [[FR]] (anchor edge).

## Sources

Listed in frontmatter, both read directly.
