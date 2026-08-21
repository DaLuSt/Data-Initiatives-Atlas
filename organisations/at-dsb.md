---
id: AT-DSB
type: organisation
name: Datenschutzbehörde
alternative_names:
  - DSB
description: >
  Austria's national supervisory authority for data protection, and the
  Austrian member of the European Data Protection Board.

level: national
country: AT
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
  - AT
  - EU-EDPB
relationships:
  - type: part-of
    target: AT
    source: fact
    evidence: "The Datenschutzbehörde is a public body of AT; this anchor edge records national scope under metadata/relationship-types.md §2.3 and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "The Datenschutzbehörde is the national supervisory authority for data protection and as such sits on the European Data Protection Board, which is composed of the head of one supervisory authority from each member state and the European Data Protection Supervisor, confirmed 2026-08-21 on edpb.europa.eu's members page. Article 68 of the GDPR (eur-lex.europa.eu) was not itself read — see docs/re-verification.md on eur-lex's bot-defense wall."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Datenschutzbehörde"
    url: "https://www.dsb.gv.at/"
    publisher: "Datenschutzbehörde"
    accessed: "2026-08-21"
  - title: "European Data Protection Board - Members"
    url: "https://www.edpb.europa.eu/about-edpb/about-edpb/members_en"
    publisher: "European Data Protection Board"
    accessed: "2026-08-21"
---

# Datenschutzbehörde

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.

## Description

Austria's data protection authority - the **seventeenth** on
[[EU-EDPB]].

## Correction

`name` was previously spelled **"Datenschutzbehorde"**, missing the umlaut.
The authority's own site spells it **Datenschutzbehörde**; the entity's own
`alternative_names` already had the correct spelling, so the two disagreed
with each other. Fixed, and the unattested English gloss "Austrian Data
Protection Authority" — not found on the authority's own site, and no
Wikipedia page exists under that title — has been dropped rather than
carried forward unread.

## One authority for a federal state

Unlike [[DE-BFDI]], which sits alongside sixteen Land authorities,
Austria supervises data protection through a **single federal**
authority. That is a real difference between two federal states, and
one the Atlas can now show - it could not, with Germany alone.

## Sources

Listed in frontmatter.
