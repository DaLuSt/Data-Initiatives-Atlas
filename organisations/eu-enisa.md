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
last_verified: "2026-11-17"
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
    evidence: "Regulation (EU) 2019/881, read directly 2026-11-17 from the Official Journal text (Publications Office, CELEX 32019R0881): Article 1(1)(a) names ENISA 'the European Union Agency for Cybersecurity', and Article 3(1) gives it its tasks 'across the Union', including supporting 'Member States, Union institutions, bodies, offices and agencies'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EU-CYBERSECURITY-ACT
    source: fact
    evidence: "Regulation (EU) 2019/881, read directly 2026-11-17 from the Official Journal text (Publications Office, CELEX 32019R0881): Article 1(1), the Regulation lays down '(a) objectives, tasks and organisational matters relating to ENISA (the European Union Agency for Cybersecurity)'; Article 3(1), 'ENISA shall carry out the tasks assigned to it under this Regulation for the purpose of achieving a high common level of cybersecurity across the Union'."
    confidence: high
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
  - title: "Official Journal text (CELEX 32019R0881)"
    url: "https://publications.europa.eu/resource/celex/32019R0881"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-17"
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
