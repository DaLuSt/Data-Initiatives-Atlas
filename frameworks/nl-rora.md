---
id: NL-RORA
type: framework
name: RijksOverheid Referentie Architectuur
alternative_names:
  - RORA
description: >
  Reference architecture for the Dutch central government, successor since
  2024 to the Enterprise Architectuur Rijksdienst (EAR).

level: national
country: NL
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: 2024-01-01
end_date: null
last_verified: null
previous_version: NL-EAR
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-EAR
  - NL-NORA
relationships:
  - type: supersedes
    target: NL-EAR
    source: fact
    evidence: "Since 2024 RORA (RijksOverheid Referentie Architectuur) has become the successor to the Enterprise Architectuur Rijksdienst (EAR) (roraonline.nl; earonline.nl). NOT READ — search-only."
    confidence: low
    valid_from: 2024-01-01
    valid_until: null

sources:
  - title: "Welkom op de kennisbank van de Enterprise Architectuur Rijksdienst — RORA Online"
    url: "https://www.roraonline.nl/index.php/Welkom_op_de_kennisbank_van_de_Enterprise_Architectuur_Rijksdienst"
    publisher: "RORA Online"
  - title: "Rijksregister standaarden — RORA Online"
    url: "https://www.roraonline.nl/index.php/Rijksregister_standaarden"
    publisher: "RORA Online"
---

# RORA (RijksOverheid Referentie Architectuur)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

RORA is the reference architecture for the Dutch central government and,
since 2024, the successor to [[NL-EAR]].

`confidence: low` and `coverage: low` throughout. This entity rests on a
single reported statement of succession. Almost nothing else about RORA was
established: not its scope, its maintainer, its relationship to [[NL-NORA]],
nor the precise date within 2024 (the `start_date` of 1 January 2024 is a
**placeholder for "during 2024"**, not a sourced commencement date, and
should be corrected or nulled on re-verification).

Adding a thinly-evidenced entity is justified here because the alternative
is worse: leaving [[NL-EAR]] marked `superseded` with a dangling
`successor` pointing at nothing, or silently omitting a succession that
sources do assert. The gaps are recorded rather than papered over.

## Relationships

- Supersedes [[NL-EAR]] from 2024.

## Sources

Listed in frontmatter. Note that roraonline.nl presents itself as "the
knowledge base of the Enterprise Architectuur Rijksdienst", which sits
oddly with RORA being EAR's successor; the naming and the site relationship
need checking.
