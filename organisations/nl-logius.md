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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading logius.nl's own 'Afdeling standaarden' page directly (2026-08-27): Logius operates under the Ministry of the Interior and Kingdom Relations (BZK), which 'serves as its policy client' overseeing Dutch digitalisation efforts. rijksfinancien.nl's BZK 2022 budget memorandum, also read directly, lists Logius as one of eight 'baten-lastenagentschappen' (income-expense agencies) under BZK's authority, alongside RvIG and P-Direkt, though the detailed Logius budget section itself was truncated in what could be retrieved."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-GDI
    source: interpretation
    evidence: "Recorded from the Logius side: logius.nl's own standards page, read directly, frames standardisation as 'the foundation of digital service delivery' for the GDI, and the facturatie-gdi-diensten news item, also read directly, confirms Logius manages invoicing/funding arrangements for named GDI services (DigiD, DigiD Machtigen, MijnOverheid). Direction is expressed here as Logius→GDI for navigability; the authoritative framing belongs on the GDI entity."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Afdeling standaarden"
    url: "https://www.logius.nl/onze-dienstverlening/standaarden/afdeling-standaarden"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "Facturatie GDI-diensten 2023 is veranderd"
    url: "https://www.logius.nl/actueel/facturatie-gdi-diensten-2023-veranderd"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "5.2 Logius — Memorie van toelichting"
    url: "https://www.rijksfinancien.nl/memorie-van-toelichting/2022/owb/vii/onderdeel/1060049"
    publisher: "Ministerie van Financiën"
    accessed: "2026-08-27"
---

# Logius

> **Verified 2026-08-27.** All three cited pages were read directly this
> pass, closing the previous `search-only` status (this entity had never
> been assigned a `last_verified` date before).

## Description

Logius is the digital government service organisation of the Netherlands
and forms part of [[NL-BZK]], which — per logius.nl's own page, read
directly — acts as its policy client ("beleidsopdrachtgever") overseeing
Dutch digitalisation efforts. It manages and develops products and services
used across government and by organisations carrying out public tasks, so
that citizens and businesses can transact digitally with them.

Logius operates services that form part of the [[NL-GDI]], including
identity and messaging services. Its standards department — confirmed
directly to number **around forty employees** — manages open standards,
applies quality cycles to them, aligns with national and international
developments, advises on standardisation and implementation, and publishes
and maintains specifications. logius.nl's own page frames this work as "the
foundation of digital service delivery" for the GDI, and names
collaboration with [[NL-FORUM-STANDAARDISATIE]] specifically, placing
Logius alongside it in the Dutch standardisation landscape in an
operational rather than advisory role.

From 2023 the funding model for several GDI services changed. Reading
logius.nl's own news item directly confirms, in its own words: "Vanaf 2023
stuurt Logius geen facturen meer naar afnemers van GDI-diensten" — Logius
stopped invoicing users of services such as DigiD, DigiD Machtigen and
MijnOverheid, with those services moving to central budget managed by BZK.
The individual GDI services named here are not yet separate Atlas entities.

## Relationships

- `owned-by` [[NL-BZK]] — Logius is one of BZK's income-expense agencies
  ("baten-lastenagentschappen"), per the ministry's own 2022 budget
  memorandum.
- `maintained-by` [[NL-GDI]] (Atlas interpretation, direction expressed for
  navigability — see above).

## Sources

All three read directly this pass. The BZK budget memorandum's detailed
Logius-specific budget section was truncated in retrieval; the document's
confirmation that Logius is a BZK agency was legible regardless.
