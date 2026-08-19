---
id: LU-CTIE
type: organisation
name: Centre des technologies de l'information de l'État
alternative_names:
  - CTIE
  - Government IT Centre
description: >
  Luxembourg's government IT centre — the main provider and host of IT
  services and solutions for the government of the Grand Duchy. It manages
  office automation and telephony for ministries and administrations, is
  responsible for implementing the State's IT infrastructure security, and is
  a central actor in eGovernment, operating the Guichet.lu portal.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU
  - LU-DATA-PUBLIC
relationships:
  - type: part-of
    target: LU
    source: fact
    evidence: "The Centre des technologies de l'information de l'État is the main provider and host of IT services and solutions for the government of the Grand Duchy of Luxembourg; it manages office automation and telephony for ministries and administrations, is responsible for implementing IT infrastructure security for the State, and acts as a central player in eGovernment, implementing the online portal Guichet.lu (ctie.gouvernement.lu 'Le CTIE' and the English 'Government IT Centre'; annuaire.public.lu; mindigital.gouvernement.lu). NOT READ — search-only. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Government IT Centre — CTIE"
    url: "https://ctie.gouvernement.lu/en.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
  - title: "Le CTIE — Centre des technologies de l'information de l'Etat"
    url: "https://ctie.gouvernement.lu/fr/l-administration.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
  - title: "Centre des technologies de l'information de l'Etat — Portail Open Data"
    url: "https://data.public.lu/en/organizations/centre-des-technologies-de-linformation-de-letat/"
    publisher: "data.public.lu"
---

# Centre des technologies de l'information de l'État

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

CTIE is Luxembourg's government IT centre — provider and host of IT services
for the whole of central government, operator of the **Guichet.lu** portal,
and **responsible for implementing the State's IT infrastructure security**.

## An operator that is also a security authority

That last function is why this entity carries [[DOMAIN-CYBERSECURITY]]
alongside [[DOMAIN-GOVERNMENT]].

Elsewhere the Atlas separates them: [[NL-LOGIUS]] operates and [[NL-NCSC]]
secures; [[FR-DINUM]] operates and [[FR-ANSSI]] secures. CTIE does both for
the State's own infrastructure — again the small-state pattern of
concentrating what larger administrations divide.

**This does not make CTIE Luxembourg's national cyber authority.** Securing
the State's own infrastructure and supervising a country's essential entities
under [[EU-NIS2]] are different jobs, and Luxembourg's NIS2 authority is
**not modelled** — see `discovery/unresolved.md`.

## Not modelled

- **Guichet.lu**, the citizen and business services portal CTIE operates.
- Luxembourg's **NIS2 competent authority and CSIRT** — GOVCERT.LU and the
  national cybersecurity bodies were not researched.
- The **"Digital Government 2026-2030" strategy**, which the sources name as
  the current programme, aiming at fully digital, inclusive public services
  built on the **Once Only** principle by 2030.

## Relationships

- `part-of` [[LU]] — an anchor edge.

## Sources

Listed in frontmatter.
