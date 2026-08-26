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
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - CZ
relationships:
  - type: part-of
    target: CZ
    source: fact
    evidence: "Confirmed verbatim by reading nukib.gov.cz's own 'Cyber Security' page directly (2026-08-26): 'The National Cyber Security Centre (NCSC – NCKB in Czech) and the Strategic Affairs and Engagement Division are the executive sections of the National Cyber and Information Security Agency (NÚKIB). The sections oversee: The activities of the Government CERT Czech Republic (GovCERT.CZ)...' NÚKIB's own 'NCSC' page, read independently, adds that NÚKIB 'manage[s] the Public Regulated Service of the Galileo navigation system in the Czech Republic' — a function this entity did not previously carry. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
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

## ⚠ Czechia's NIS2 transposition is not modelled

As for [[PT-CNCS]], the transposing instrument was not identified, so NÚKIB
carries an anchor edge to [[CZ]] rather than a relationship to an act.

Czechia's cyber security act (No 181/2014) and its NIS2 successor are both
absent. Logged in `discovery/unresolved.md`.

## Relationships

- `part-of` [[CZ]] — an anchor edge.

## Sources

Listed in frontmatter, both read directly this pass.
