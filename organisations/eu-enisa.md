---
id: EU-ENISA
type: organisation
name: European Union Agency for Cybersecurity
alternative_names:
  - ENISA
description: >
  EU agency for cybersecurity, contributing to EU network and information
  security since 2004 and given a reinforced role and permanent mandate by
  the Cybersecurity Act. It supports the European cybersecurity
  certification framework. Based in Athens with a branch in Heraklion.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-CYBERSECURITY-ACT
  - EU-EDPB
  - EU-INTEROPERABLE-EUROPE-BOARD
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "ENISA is the European Union Agency for Cybersecurity, established under Regulation (EU) 2019/881 (EUR-Lex summary of the Cybersecurity Act). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EU-CYBERSECURITY-ACT
    source: fact
    evidence: "Regulation (EU) 2019/881 is on ENISA and on ICT cybersecurity certification; ENISA has a reinforced role to strengthen EU cybersecurity and facilitate uptake of certification (EUR-Lex summary of the EU Cybersecurity Act). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-INTEROPERABLE-EUROPE-BOARD
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (this entity's own file: 'the Interoperable Europe Board, which is not yet an Atlas entity' — it now is, created 2026-09-05). Confirmed by reading interoperable-europe.ec.europa.eu's own 'The Board' page directly (already cited on [[EU-INTEROPERABLE-EUROPE-BOARD]]'s own file, cross-applied here 2026-09-13): observers include the Committee of the Regions, ENISA and the European Cybersecurity Competence Centre. `participates-in` rather than `part-of`, matching the weaker observer role."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The EU Cybersecurity Act — summary"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/the-eu-cybersecurity-act.html"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "Cybersecurity / network and information security (Rolling Plan 2024)"
    url: "https://interoperable-europe.ec.europa.eu/collection/rolling-plan-ict-standardisation/cybersecurity-network-and-information-security-rp-2024"
    publisher: "European Commission — Interoperable Europe Portal"
  - title: "The Board"
    url: "https://interoperable-europe.ec.europa.eu/collection/governance-board/board"
    publisher: "European Commission — Interoperable Europe Portal"
    accessed: "2026-09-13"
---

# ENISA (European Union Agency for Cybersecurity)

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

ENISA has contributed to EU network and information security since 2004.
[[EU-CYBERSECURITY-ACT]] (Regulation (EU) 2019/881) concerns the agency and
ICT cybersecurity certification, giving it a reinforced role in
strengthening EU cybersecurity and driving uptake of certification. It is
based in Athens with a branch office in Heraklion.

ENISA is invited to participate as an observer in the [[EU-INTEROPERABLE-EUROPE-BOARD]]
— **stale as of 2026-09-13, now fixed**: the Board has been an Atlas
entity since 2026-09-05; this file's own "not yet an Atlas entity" line
was simply never updated. Independently confirmed by reading
interoperable-europe.ec.europa.eu's own Board page directly this pass:
its observers are "the Committee of the Regions, the EU Cybersecurity
Agency and the European Cybersecurity Competence Centre" — ENISA by its
full institutional name.

## Coordination with the data protection authorities

Where certification touches the security of processing personal data, ENISA
is reported to consult [[EU-EDPB]] before adopting a scheme, and ENISA's
advice is issued on prior request from the EDPB — an arrangement the EDPB
and [[EU-EDPS]] have welcomed as giving a clear division of
responsibilities. No relationship is asserted for this: the sourced
statements describe an evolving arrangement in a joint opinion rather than a
settled structural fact.

`coverage: low`: the agency's mandate, structure and certification schemes
were not researched.

## What this closes

[[EU-CYBERSECURITY-ACT]] was created in Batch 8 with its ENISA relationship
explicitly pending. That gap is now closed.

## Relationships

- Governed by / established under [[EU-CYBERSECURITY-ACT]].

## Sources

Listed in frontmatter.
