---
id: LI-DATENSCHUTZSTELLE
type: organisation
name: Datenschutzstelle
alternative_names:
  - DSS
  - Data Protection Authority (Liechtenstein)
description: >
  Liechtenstein's independent data protection supervisory authority. Its
  Commissioner is appointed by the Landtag for a five-year renewable term.
  It supervises the General Data Protection Regulation, which applies in
  Liechtenstein through the EEA Agreement, and the national Datenschutzgesetz
  that supplements it. As the supervisory authority of an EEA EFTA state it
  participates in the activities of the European Data Protection Board under
  Decision of the EEA Joint Committee No 154/2018.

level: national
country: LI
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - LI
  - LI-DSG
  - EU-EDPB
  - INTL-EEA-JCD-154-2018
relationships:
  - type: part-of
    target: LI
    source: fact
    evidence: "The Datenschutzstelle (DSS) is Liechtenstein's independent supervisory authority, with its Commissioner appointed by Parliament (Landtag) for a five-year renewable term (datenschutzstelle.li; gdprhub.eu 'Data Protection in Liechtenstein'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: a national supervisory authority whose head is appointed by the legislature is part of the state."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 provides that the supervisory authorities of the EFTA States shall participate in the activities of the European Data Protection Board (eur-lex.europa.eu ELI dec/2018/1022/oj; efta.int 154-2018). NOT READ — search-only. Membership follows from the sourced rule rather than from a source naming the Datenschutzstelle."
    confidence: medium
    valid_from: 2018-07-06
    valid_until: null

sources:
  - title: "Datenschutzstelle Liechtenstein"
    url: "https://www.datenschutzstelle.li/"
    publisher: "Datenschutzstelle Liechtenstein"
  - title: "Data Protection in Liechtenstein"
    url: "https://gdprhub.eu/index.php?title=Data_Protection_in_Liechtenstein"
    publisher: "GDPRhub — noyb"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# Datenschutzstelle

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Liechtenstein's data protection supervisory authority, and Liechtenstein's
**first modelled national entity**. Its Commissioner is appointed by the
**Landtag** for a five-year renewable term.

It supervises [[EU-GDPR]] — directly applicable in Liechtenstein through the
EEA Agreement — and [[LI-DSG]], the national act that supplements it.

## Relationships

- `part-of` [[LI]] — anchor edge under `metadata/relationship-types.md` §2.3.
- `participates-in` [[EU-EDPB]], on the composition rule in
  [[INTL-EEA-JCD-154-2018]]: the supervisory authorities of the EFTA States
  participate in the Board's activities. As with [[IS-PERSONUVERND]], this is
  participation in activities and **not** membership with a vote under
  Article 68(3) GDPR.

## Sources

Listed in frontmatter — the authority's own site, GDPRhub, and the EUR-Lex
record of the Joint Committee decision.
