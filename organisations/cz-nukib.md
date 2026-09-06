---
id: CZ-NUKIB
type: organisation
name: Národní úřad pro kybernetickou a informační bezpečnost
alternative_names:
  - NÚKIB
  - NUKIB
  - National Cyber and Information Security Agency
description: >
  Czechia's national cyber and information security agency and the country's
  cybersecurity supervisory authority. Its executive sections include the
  National Cyber Security Centre (NCKB), which oversees the activities of the
  government CERT, GovCERT.CZ.

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - CZ
  - CZ-ZAKON-264-2025
relationships:
  - type: part-of
    target: CZ
    source: fact
    evidence: "Confirmed verbatim by reading nukib.gov.cz's own 'Cyber Security' page directly (2026-08-26): 'The National Cyber Security Centre (NCSC – NCKB in Czech) and the Strategic Affairs and Engagement Division are the executive sections of the National Cyber and Information Security Agency (NÚKIB). The sections oversee: The activities of the Government CERT Czech Republic (GovCERT.CZ)...' NÚKIB's own 'NCSC' page, read independently, adds that NÚKIB 'manage[s] the Public Regulated Service of the Galileo navigation system in the Czech Republic' — a function this entity did not previously carry. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: CZ-ZAKON-264-2025
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading the Act's own text directly (NÚKIB's hosted unofficial English translation, v3): the Act establishes NÚKIB ('the Agency') as the supervisory and enforcement authority under Czechia's transposition of the NIS2 Directive — Title VI (§§55-63) sets out NÚKIB's inspection, corrective-measure and penalty powers. See CZ-ZAKON-264-2025 for the full transposition sourcing."
    confidence: high
    valid_from: 2025-11-01
    valid_until: null

sources:
  - title: "National Cyber and Information Security Agency — Cyber Security"
    url: "https://nukib.gov.cz/en/cyber-security/"
    publisher: "NÚKIB"
    accessed: "2026-08-26"
  - title: "National Cyber and Information Security Agency — NCSC"
    url: "https://nukib.gov.cz/en/252-ncsc/"
    publisher: "NÚKIB"
    accessed: "2026-08-26"
---

# Národní úřad pro kybernetickou a informační bezpečnost

> **Verified 2026-08-26.** Both cited pages were read directly and
> confirm this entity's description of NÚKIB's structure in NÚKIB's
> own words. Its NCSC page also names a function this entity did not
> previously carry: managing the Galileo Public Regulated Service for
> Czechia.
>
> **Closed 2026-09-06**: the long-flagged NIS2 transposition gap is
> resolved — [[CZ-ZAKON-264-2025]], read directly, names NÚKIB as the
> enforcement authority.

## Description

NÚKIB is Czechia's national cyber **and information** security agency, and
the country's cybersecurity supervisory authority.

Inside it sit the **National Cyber Security Centre (NCKB)** and the Strategic
Affairs and Engagement Division, and those sections oversee **GovCERT.CZ**,
the government CERT. NÚKIB also manages the **Galileo Public Regulated
Service** in Czechia, confirmed by reading its own NCSC page directly.

## The fourth "NCSC" in the Atlas, and the second one nested inside something else

| Body | Country | Where it sits |
|---|---|---|
| [[GB-NCSC]] | GB | inside [[GB-GCHQ]], a signals intelligence agency |
| **NCKB** | **CZ** | **inside NÚKIB** — not modelled separately |
| [[IE-NCSC]] | IE | standalone; will be the NIS2 authority |
| [[NL-NCSC]] | NL | standalone since the DTC merger |
| [[CH-BACS]] | CH | renamed *from* NCSC |

The Czech NCKB is **not a separate entity** here: the sources present it as a
section of NÚKIB rather than as a body, and creating a node for an internal
division would imply a standing it does not have.

## Czechia's NIS2 transposition, closed 2026-09-06

As for [[PT-CNCS]], this was previously an open gap: no transposing
instrument had been identified for NÚKIB. It is now closed —
**[[CZ-ZAKON-264-2025]]**, Czechia's new Cybersecurity Act (264/2025 Sb.,
in effect from 1 November 2025), transposes [[EU-NIS2]] and names NÚKIB
("the Agency") as the supervisory and enforcement authority, confirmed by
reading the Act's own text directly. The predecessor Act No. 181/2014 Sb.
is repealed by the new Act's own §72 but is not itself modelled as a
separate Atlas entity — see CZ-ZAKON-264-2025 for the full sourcing and
reasoning.

## Relationships

- `part-of` [[CZ]] — an anchor edge.
- `governed-by` [[CZ-ZAKON-264-2025]] — the Act establishing NÚKIB's
  supervisory and enforcement powers under Czechia's NIS2 transposition.

## Sources

Listed in frontmatter. The two 2026-08-26 sources were read directly that
pass; the NIS2 transposition finding cites CZ-ZAKON-264-2025's own
sources, read directly 2026-09-06.
