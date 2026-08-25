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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-25"
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
    evidence: "Confirmed by reading ctie.gouvernement.lu directly (2026-08-25): 'The Government IT Centre (CTIE) is the administrative body responsible for IT services for Luxembourg's government, ministries and public administrations.' Its 'Attributions' (Remit) page, read the same pass, gives the exact legal basis: 'The remit of the Government IT Centre (CTIE) is set out in the law of 24 November 2015 amending the amended law of 20 April 2009,' and confirms verbatim that CTIE's mission includes to 'ensure IT security and respect for the legal provisions regarding the protection of persons in respect of the processing of personal data, within the limits of its attributions.' The French-language 'Le CTIE' page, also read directly, confirms the same description in French, last modified 12.03.2025. 'Guichet.lu' was not named on either page read this pass and is retained from the original sourcing rather than removed. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Government IT Centre — CTIE"
    url: "https://ctie.gouvernement.lu/en.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-08-25"
  - title: "Remit — CTIE"
    url: "https://ctie.gouvernement.lu/en/l-administration/Attributions.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-08-25"
  - title: "Le CTIE — Centre des technologies de l'information de l'État"
    url: "https://ctie.gouvernement.lu/fr/l-administration.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-08-25"
  - title: "Centre des technologies de l'information de l'État — Portail Open Data"
    url: "https://data.public.lu/en/organizations/centre-des-technologies-de-linformation-de-letat/"
    publisher: "data.public.lu"
    accessed: "2026-08-25"
---

# Centre des technologies de l'information de l'État

> **Verified 2026-08-25.** All four cited pages were read directly. A
> finding: the "Attributions" (Remit) page gives an exact legal basis —
> "the law of 24 November 2015 amending the amended law of 20 April
> 2009" — that no earlier version of this entity carried. "Guichet.lu"
> was not named on any page read this pass and is retained from the
> original sourcing rather than removed.

## Description

Confirmed by reading ctie.gouvernement.lu directly (2026-08-25): "The
Government IT Centre (CTIE) is the administrative body responsible for
IT services for Luxembourg's government, ministries and public
administrations." Its own "Remit" page, read the same pass, states its
legal basis directly — "the law of 24 November 2015 amending the
amended law of 20 April 2009" — and confirms verbatim that its mission
includes to "ensure IT security and respect for the legal provisions
regarding the protection of persons in respect of the processing of
personal data." "Guichet.lu" itself was not named on either page read
this pass and is retained from the original sourcing.

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

- **Guichet.lu**, the citizen and business services portal CTIE operates —
  named in the original sourcing but not found on either page read this
  pass.
- Luxembourg's **NIS2 competent authority and CSIRT** — GOVCERT.LU and the
  national cybersecurity bodies were not researched.
- The **"law of 24 November 2015 amending the amended law of 20 April
  2009"** as a separate law entity — named and dated by CTIE's own page,
  but not created here, matching the threshold this Atlas applies
  elsewhere (e.g. [[PL-GUS]]'s Act on Public Statistics).

## Confirmed directly: the "Digital Government Strategy 2026-2030"

Confirmed by reading ctie.gouvernement.lu directly (2026-08-25): "The
Digital Government Strategy 2026-2030 marks a new milestone in
Luxembourg's digital transformation. By 2030, the Luxembourg government
aims to make its public services fully digital, inclusive and based on
the 'Once Only' principle." A detail this entity previously carried as
unconfirmed is now read directly, word for word.

## Relationships

- `part-of` [[LU]] — an anchor edge.

## Sources

Listed in frontmatter, all four read directly this pass.
