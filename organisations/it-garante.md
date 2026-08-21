---
id: IT-GARANTE
type: organisation
name: Garante per la protezione dei dati personali
alternative_names:
  - Garante privacy
  - GPDP
description: >
  Italy's independent supervisory authority for the protection of personal
  data, and the Italian member of the European Data Protection Board.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IT
  - EU-EDPB
relationships:
  - type: part-of
    target: IT
    source: fact
    evidence: "The Garante is a public body of IT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "The Garante per la protezione dei dati personali is the national supervisory authority for data protection and as such sits on the European Data Protection Board, which is composed of the head of one supervisory authority from each member state and the European Data Protection Supervisor, confirmed 2026-08-21 on edpb.europa.eu's members page. Article 68 of the GDPR (eur-lex.europa.eu) was not itself read — see docs/re-verification.md on eur-lex's bot-defense wall."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Garante per la protezione dei dati personali"
    url: "https://www.garanteprivacy.it/"
    publisher: "Garante per la protezione dei dati personali"
    accessed: "2026-08-21"
  - title: "European Data Protection Board - Members"
    url: "https://www.edpb.europa.eu/about-edpb/about-edpb/members_en"
    publisher: "European Data Protection Board"
    accessed: "2026-08-21"
---

# Garante per la protezione dei dati personali

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

Italy's data protection authority, and the **thirteenth** national DPA
on [[EU-EDPB]]. The unattested English gloss "Italian Data Protection
Authority" — not found on the Garante's own site and with no Wikipedia page
under that title — has been dropped rather than carried forward unread.

## Relationships

- `participates-in` [[EU-EDPB]].
- `part-of` [[IT]] (anchor edge).

## Sources

Listed in frontmatter.
