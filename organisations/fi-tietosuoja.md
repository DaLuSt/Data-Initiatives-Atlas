---
id: FI-TIETOSUOJA
type: organisation
name: Office of the Data Protection Ombudsman
alternative_names:
  - Tietosuojavaltuutetun toimisto
  - Dataombudsmannens byrå
description: >
  Finland's national supervisory authority for data protection, and the
  Finnish member of the European Data Protection Board.

level: national
country: FI
region: EU

status: active
confidence: medium
coverage: low
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
  - FI
  - EU-EDPB
relationships:
  - type: part-of
    target: FI
    source: fact
    evidence: "The Office of the Data Protection Ombudsman is a public body of FI; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "The Office of the Data Protection Ombudsman is the national supervisory authority for data protection and as such sits on the European Data Protection Board, which is composed of the head of one supervisory authority from each member state and the European Data Protection Supervisor, confirmed 2026-08-21 on edpb.europa.eu's members page. Article 68 of the GDPR (eur-lex.europa.eu) was not itself read — see docs/re-verification.md on eur-lex's bot-defense wall."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Office of the Data Protection Ombudsman"
    url: "https://tietosuoja.fi/en/home"
    publisher: "Tietosuojavaltuutetun toimisto"
    accessed: "2026-08-21"
  - title: "European Data Protection Board - Members"
    url: "https://www.edpb.europa.eu/about-edpb/about-edpb/members_en"
    publisher: "European Data Protection Board"
    accessed: "2026-08-21"
  - title: "Tietosuojavaltuutetun toimisto — Etusivu"
    url: "https://tietosuoja.fi/etusivu"
    publisher: "Tietosuojavaltuutetun toimisto"
    accessed: "2026-08-21"
  - title: "Dataombudsmannens byrå — Framsida"
    url: "https://tietosuoja.fi/sv/framsida"
    publisher: "Tietosuojavaltuutetun toimisto"
    accessed: "2026-08-21"
---

# Office of the Data Protection Ombudsman

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

Finland's data protection authority - the **fourteenth** on [[EU-EDPB]].

## Correction

`Dataombudsmannens byra` was missing its ring diacritic — the Swedish-language
site spells it **Dataombudsmannens byrå**, now fixed. The unattested English
gloss "Finnish Data Protection Ombudsman" — no Wikipedia page exists under
that title — has been dropped rather than carried forward unread. Both the
Finnish- and Swedish-language front pages have been added as sources to
corroborate the two local-language names.

## An ombudsman, not an agency

Finland supervises data protection through an **ombudsman**, a form
distinct from the agencies and commissions the Atlas holds elsewhere.
The Atlas's `type: organisation` flattens that difference.

## Sources

Listed in frontmatter.
