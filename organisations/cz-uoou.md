---
id: CZ-UOOU
type: organisation
name: Úřad pro ochranu osobních údajů
name_en: "Czech Office for Personal Data Protection"
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
last_verified: "2026-11-22"
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
    evidence: "The EDPB's own members page (edpb.europa.eu, About EDPB > Members), read directly 2026-11-22, lists for the Czech Republic the 'Office for Personal Data Protection', Pplk. Sochora 27, Prague 7, uoou.gov.cz. Article 68(3) GDPR, read directly on gdpr-info.eu (2026-08-26), provides that the Board is composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their representatives."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: CZ-ZAKON-110-2019
    source: fact
    evidence: "Act No. 110/2019 Sb., read directly 2026-11-22 on zakonyprolidi.cz: § 1(e), the Act governs 'postavení a pravomoc Úřadu pro ochranu osobních údajů (dále jen „Úřad“)', and § 50(1), 'Úřad je ústředním správním úřadem pro oblast ochrany osobních údajů v rozsahu stanoveném tímto zákonem, jinými právními předpisy, mezinárodními smlouvami ... a přímo použitelnými předpisy Evropské unie.' The history of the office's inspectors, which an encyclopedia article supplied, is in the prose and not needed here (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "EDPB — Members"
    url: "https://www.edpb.europa.eu/about-edpb/about-edpb/members_en"
    publisher: "European Data Protection Board"
    accessed: "2026-11-22"
  - title: "Zákon č. 110/2019 Sb., o zpracování osobních údajů (zakonyprolidi.cz)"
    url: "https://www.zakonyprolidi.cz/cs/2019-110"
    publisher: "zakonyprolidi.cz (AION CS), text of the Sbírka zákonů"
    accessed: "2026-11-22"
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
