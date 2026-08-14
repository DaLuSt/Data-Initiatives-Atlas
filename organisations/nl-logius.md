---
id: NL-LOGIUS
type: organisation
name: Logius
alternative_names: []
description: >
  Dutch government's digital services organisation, part of the Ministry of
  the Interior and Kingdom Relations. Logius manages and develops shared
  products and services for government and public-task organisations, and
  operates services forming part of the Generieke Digitale Infrastructuur.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-BZK
relationships:
  - type: owned-by
    target: NL-BZK
    source: fact
    evidence: "Logius is part of the Ministry of BZK, which is its policy commissioner (beleidsopdrachtgever), per logius.nl and rijksfinancien.nl. NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-GDI
    source: interpretation
    evidence: "Recorded from the Logius side: search results state GDI services are managed by Logius. Direction is expressed here as Logius→GDI for navigability; the authoritative framing belongs on the GDI entity."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Afdeling standaarden"
    url: "https://www.logius.nl/onze-dienstverlening/standaarden/afdeling-standaarden"
    publisher: "Logius"
  - title: "Facturatie GDI-diensten 2023 is veranderd"
    url: "https://www.logius.nl/actueel/facturatie-gdi-diensten-2023-veranderd"
    publisher: "Logius"
  - title: "5.2 Logius — Memorie van toelichting"
    url: "https://www.rijksfinancien.nl/memorie-van-toelichting/2022/owb/vii/onderdeel/1060049"
    publisher: "Ministerie van Financiën"
---

# Logius

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Logius is the digital government service organisation of the Netherlands and
forms part of [[NL-BZK]], which acts as its policy commissioner. It manages
and develops products and services used across government and by
organisations carrying out public tasks, so that citizens and businesses can
transact digitally with them.

Logius operates services that form part of the [[NL-GDI]], including
identity and messaging services. It also runs a standards department: it
manages standards, contributes to the quality of that management, and
promotes standardisation and the correct application of open standards —
placing it alongside [[NL-FORUM-STANDAARDISATIE]] in the Dutch
standardisation landscape, though in an operational rather than advisory
role.

From 2023 the funding model for several GDI services changed: Logius stopped
invoicing users of services such as DigiD, DigiD Machtigen and MijnOverheid,
with those services moving to central budget managed by BZK. The individual
GDI services named here are not yet separate Atlas entities.

## Relationships

- Part of / owned by [[NL-BZK]].
- Operates services within [[NL-GDI]].

## Sources

Listed in frontmatter.
