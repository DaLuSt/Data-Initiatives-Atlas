---
id: LU-LHC
type: organisation
name: Luxembourg House of Cybersecurity
alternative_names:
  - LHC
  - SECURITYMADEIN.LU
description: >
  Luxembourg economic interest grouping (groupement d'intérêt économique,
  g.i.e.) established 5 May 2010 as SECURITYMADEIN.LU and renamed
  Luxembourg House of Cybersecurity in October 2022, overseen by the
  Ministry of the Economy. It operates two centres: CIRCL, the CSIRT for
  the private sector, municipalities and non-governmental entities, and
  the National Cybersecurity Competence Center (NC3), formed from the
  consolidation of CASES and C3.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2010-05-05
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU
  - LU-CIRCL
relationships:
  - type: part-of
    target: LU
    source: fact
    evidence: "Anchor edge under metadata/relationship-types.md §2.3, since no specific ministry entity (Ministère de l'Économie) is yet modelled in the Atlas. Confirmed by reading securitymadein.lu's own 'The Cybersecurity Agency' page directly (2026-09-12): LHC is 'an Economic Interest Group' established '5 May 2010,' formerly known as SECURITYMADEIN.LU, renamed following the October 2022 inauguration per the Luxembourg government's own press release (gouvernement.lu), also read directly, which names the Ministry of the Economy as overseeing body and quotes its cybersecurity director as president of the management structure."
    confidence: medium
    valid_from: 2010-05-05
    valid_until: null

sources:
  - title: "The Cybersecurity Agency"
    url: "https://www.securitymadein.lu/agency/"
    publisher: "Luxembourg House of Cybersecurity (LHC) / SECURITYMADEIN.LU"
    accessed: "2026-09-12"
  - title: "En présence de S.A.R. le Grand-Duc héritier, Franz Fayot a inauguré la Luxembourg House of Cybersecurity"
    url: "https://gouvernement.lu/fr/actualites/toutes_actualites/communiques/2022/10-octobre/18-fayot-sar-cybersecurite.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-09-12"
---

# Luxembourg House of Cybersecurity

> **Created 2026-09-12**, closing part of `discovery/unresolved.md` row
> #181: CIRCL's operator was unmodelled. LHC's own agency page and the
> Luxembourg government's own inauguration press release were read
> directly.

## Description

Confirmed by reading `securitymadein.lu`'s own "The Cybersecurity Agency"
page directly: Luxembourg House of Cybersecurity (LHC) is "an Economic
Interest Group" (groupement d'intérêt économique, g.i.e.) established
**5 May 2010**, "formerly known as SECURITYMADEIN.LU." The Luxembourg
government's own 2022 press release, read directly, confirms the
renaming followed an October 2022 inauguration attended by the Hereditary
Grand Duke, names the **Ministry of the Economy** as the overseeing
body — "the ministry of the Economy has played the role of catalyst for a
cybersecurity ecosystem for over 20 years" — and names its cybersecurity
director as president of LHC's management structure.

## Two operating centres

Per the same LHC page: it operates through **CIRCL** ([[LU-CIRCL]]),
handling incident management and cyber threat intelligence exchange, and
the **National Cybersecurity Competence Center (NC3)**, created by
consolidating two predecessor bodies, CASES and C3. NC3 is outside this
Atlas's immediate scope (competence-centre/training function rather than
a CSIRT or regulator) and is not modelled separately here.

## Relationships

- `part-of` [[LU]] — anchor edge; no Ministry of the Economy entity is
  yet modelled to anchor to instead.

[[LU-CIRCL]] carries the inverse `maintained-by` edge pointing here,
recorded on its own file rather than duplicated on this one.

## Not modelled

- **NC3** (National Cybersecurity Competence Center), LHC's second
  centre, and its predecessors **CASES** and **C3**.
- A **Ministère de l'Économie** entity, which would be a more precise
  `part-of` target than the country-level anchor used here.

## Sources

Listed in frontmatter, both read directly 2026-09-12.
