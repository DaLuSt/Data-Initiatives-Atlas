---
id: CZ-UOOU
type: organisation
name: Úřad pro ochranu osobních údajů
alternative_names:
  - ÚOOÚ
  - UOOU
  - Czech Office for Personal Data Protection
description: >
  Czechia's data protection supervisory authority, established in 2000.

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - CZ-ZAKON-110-2019
  - EU-GDPR
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Article 68(3) GDPR, read directly on gdpr-info.eu (2026-08-26), provides that the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives; the Úřad pro ochranu osobních údajů is Czechia's supervisory authority. No page read (including ÚOOÚ's own site and its Wikipedia article) names EDPB membership in ÚOOÚ's own words, so this stays on the composition-rule tier rather than a direct statement."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: CZ-ZAKON-110-2019
    source: fact
    evidence: "Confirmed by reading cs.wikipedia.org's ÚOOÚ article directly (2026-08-26): 'Činnost úřadu vymezuje zákon č. 110/2019 Sb., o zpracování osobních údajů' (the office's activity is defined by Act No. 110/2019 Sb., on the processing of personal data). The same article confirms in its own words: 'Zákon č. 110/2019 Sb. ... již funkci inspektorů neuvádí, stávající inspektoři ale dokončili své funkční období podle původních právních předpisů' (Act No. 110/2019 no longer includes the position of inspectors, but the existing inspectors completed their term under the original rules), naming all seven inspectors and their appointment dates: they were appointed by the President of the Republic on the Senate's proposal for ten-year terms."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Úřad pro ochranu osobních údajů"
    url: "https://www.uoou.gov.cz/"
    publisher: "Úřad pro ochranu osobních údajů (ÚOOÚ)"
    accessed: "2026-08-26"
  - title: "Úřad pro ochranu osobních údajů"
    url: "https://cs.wikipedia.org/wiki/%C3%9A%C5%99ad_pro_ochranu_osobn%C3%ADch_%C3%BAdaj%C5%AF"
    publisher: "Wikipedie"
    accessed: "2026-08-26"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-26"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
    accessed: "2026-08-26"
---

# Úřad pro ochranu osobních údajů

> **Verified 2026-08-26.** All four cited pages were read directly.
> Wikipedia's own ÚOOÚ article confirms the office was established in
> **2000**, a founding date this entity did not previously carry, and
> confirms the inspector-abolition claim with unusual specificity: all
> seven former inspectors, named, appointed by the President on the
> Senate's proposal for ten-year terms.

## Description

ÚOOÚ is Czechia's data protection supervisory authority, established
in **2000**.

## A structural change recorded in what the act removed

The sources note that [[CZ-ZAKON-110-2019]] **no longer includes the position
of inspectors** that existed under the previous Czech data protection act.
Confirmed by reading cs.wikipedia.org directly: the office previously had
**seven inspectors**, each appointed by the President of the Republic on
the proposal of the Senate for a ten-year term; the 2019 Act removed the
position going forward, while letting sitting inspectors finish their
terms under the old rules.

That is a small detail and an unusually concrete one: most national GDPR
instruments are described by what they add, and this one is described by an
office it abolished.

## The eleventh authority on the Board

[[EU-EDPB]] now reaches eleven national supervisory authorities plus the
[[EU-EDPS]] — from two, before the structural-fixes batch found Article
68(3).

## Relationships

- `participates-in` [[EU-EDPB]].
- `applies-to` [[CZ-ZAKON-110-2019]].

## Sources

Listed in frontmatter, all four read directly this pass.
