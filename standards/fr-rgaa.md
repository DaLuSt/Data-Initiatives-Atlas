---
id: FR-RGAA
type: standard
name: Référentiel Général d'Amélioration de l'Accessibilité
alternative_names:
  - RGAA
  - General Accessibility Improvement Framework (France)
description: >
  French general framework of digital accessibility requirements,
  applying to the online public communication services of the state,
  territorial authorities and their affiliated public bodies, and to
  certain private-sector services, across web, television and telephony
  channels. It stems from Article 47 of the law of 11 February 2005 on
  equal rights and opportunities for persons with disabilities, with an
  implementing decree published 16 May 2009 and web-channel approval
  following in October 2009. The Direction interministérielle du
  numérique (DINUM) has created and maintained it since October 2019;
  the current version, 4.1, was released 16 February 2021. It connects
  to the European EN 301 549 accessibility standard, though it does not
  translate that standard's full scope — native mobile applications and
  non-Web documents remain outside its historical coverage.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2009-05-16
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - FR-DINUM
related_entities:
  - FR-RGI
  - FR-RGS
relationships:
  - type: maintained-by
    target: FR-DINUM
    source: fact
    evidence: "Confirmed by reading numerique.gouv.fr's own RGAA page directly (2026-09-04): 'La Direction interministérielle du numérique (DINUM) crée et maintient le RGAA' (DINUM creates and maintains the RGAA), alongside associated resources and tools. Corroborated by reading the French Wikipedia RGAA article directly (2026-09-04), which independently states DINUM has overseen the RGAA's evolution since October 2019, with the latest version, 4.1, released 16 February 2021."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "RGAA — Rendre les sites et services numériques accessibles"
    url: "https://www.numerique.gouv.fr/publications/rgaa-accessibilite/"
    publisher: "DINUM — numerique.gouv.fr"
    accessed: "2026-09-04"
  - title: "RGAA"
    url: "https://fr.wikipedia.org/wiki/RGAA"
    publisher: "Wikipédia"
    accessed: "2026-09-04"
---

# Référentiel Général d'Amélioration de l'Accessibilité (RGAA)

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged the RGAA as a sibling of
> [[FR-RGI]] and [[FR-RGS]], not yet modelled. Both cited pages were
> read directly this pass.

## Description

The RGAA is France's general digital-accessibility framework, applying
to public-sector online services and, more recently, certain
private-sector ones, across web, television and telephony channels.

## A different legal parent than its siblings

Unlike [[FR-RGI]] and [[FR-RGS]], both founded on
[[FR-ORDONNANCE-2005-1516]], the RGAA stems from **Article 47 of the
law of 11 February 2005 on equal rights and opportunities for persons
with disabilities** — confirmed by reading the French Wikipedia RGAA
article directly, which describes an implementing decree published
**16 May 2009**, with web-channel approval following in October 2009.
No entity is created for the 2005 disability-rights law itself: it is a
broad statute of which digital accessibility is one article among many,
the same treatment the Atlas gives statutes that merely reference a
narrower instrument (see [[AT-EGOVG]]'s Meldegesetz/Passgesetz
citations).

## Maintained by DINUM since 2019

Reading `numerique.gouv.fr`'s own RGAA page directly: **"La Direction
interministérielle du numérique (DINUM) crée et maintient le RGAA."**
The French Wikipedia article, independently read, dates DINUM's
stewardship to **October 2019** and names the current version, **4.1**,
released **16 February 2021** — the same body that maintains
[[FR-RGI]], but (unlike [[FR-RGS]]) with no named co-steward.

## A partial European connection

Wikipedia's own account, read directly, states the RGAA connects to the
European **EN 301 549** accessibility standard, but does not translate
that standard's full scope: **"native mobile applications and non-Web
documents... remain outside its historical scope."** No relationship to
an EN 301 549 entity is asserted, because none exists in the Atlas.

## Relationships

- `maintained-by` [[FR-DINUM]].

## Sources

Listed in frontmatter, both read directly this pass.
