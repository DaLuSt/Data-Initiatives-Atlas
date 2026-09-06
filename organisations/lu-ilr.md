---
id: LU-ILR
type: organisation
name: Institut Luxembourgeois de Régulation
alternative_names:
  - ILR
  - Luxembourg Institute of Regulation
  - Luxembourg Regulatory Institute
description: >
  Luxembourg's independent multi-sector regulator, established in 1997
  during telecommunications liberalisation and expanded to its current
  form in 2000. It regulates electronic communications, electricity, gas,
  postal services, rail transport, airport charges and radio frequencies,
  and since 2019 has been Luxembourg's single point of contact for network
  and information system security in several sectors. Since 2026 it is
  the NIS2 competent authority for the vast majority of sectors under
  Luxembourg's NIS2 transposition act.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 1997-01-01
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU
  - LU-LOI-NIS2
relationships:
  - type: part-of
    target: LU
    source: fact
    evidence: "Confirmed by reading myilr.lu's own 'What is the ILR' page directly (2026-09-06): 'The ILR guarantees and supervises, in the consumer's interests, the smooth running of the markets on the basis of effective and sustainable competition, while guaranteeing a basic universal service' — an independent Luxembourg public authority regulating electronic communications, electricity, gas, postal services, rail, airport charges and radio frequencies, established 1997 and expanded to its current scope in 2000. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 1997-01-01
    valid_until: null
  - type: governed-by
    target: LU-LOI-NIS2
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (LU-CTIE, 2026-09-05). Confirmed by reading ILR's own NIS2 page and FAQ page directly (2026-09-05/2026-09-06): the Loi du 5 mai 2026 'assigns to the ILR the function of competent authority for the security of networks and information systems for the vast majority of sectors.' ILR had already held an adjacent, narrower role since 2019 (network and information system security point of contact for energy, transport, health, drinking water, digital infrastructure and digital services, per myilr.lu, read directly 2026-09-06) — the 2026 Act extends rather than creates this function."
    confidence: high
    valid_from: 2026-05-10
    valid_until: null

sources:
  - title: "What is the ILR"
    url: "https://www.myilr.lu/en/what-is-the-ilr/"
    publisher: "Institut Luxembourgeois de Régulation (ILR)"
    accessed: "2026-09-06"
  - title: "NIS 2"
    url: "https://www.ilr.lu/en/sectors/niss/nis-2/"
    publisher: "Institut Luxembourgeois de Régulation (ILR)"
    accessed: "2026-09-06"
  - title: "Frequently asked questions about NIS2 (FAQ)"
    url: "https://www.ilr.lu/en/sectors/niss/nis-2/frequently-asked-questions-about-nis2-faq/"
    publisher: "Institut Luxembourgeois de Régulation (ILR)"
    accessed: "2026-09-05"
  - title: "Cybersécurité: l'ILR présente la nouvelle loi NIS 2"
    url: "https://gouvernement.lu/fr/actualites/toutes_actualites/communiques/2026/07-juillet/06-cybersecurite-nis-2.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-09-06"
---

# Institut Luxembourgeois de Régulation

> **Created 2026-09-06**, closing a gap flagged on [[LU-CTIE]] the
> previous day: Luxembourg's NIS2 competent authority was named there but
> not modelled as its own entity. ILR's own site was read directly for
> both its general regulatory mandate and its NIS2 role.

## Description

Confirmed by reading myilr.lu's own "What is the ILR" page directly
(2026-09-06): the ILR is Luxembourg's **independent multi-sector
regulator**, established in **1997** during telecommunications
liberalisation and expanded to its present form in **2000** when
electricity and postal services were added. Its stated mission, quoted
verbatim: "The ILR guarantees and supervises, in the consumer's interests,
the smooth running of the markets on the basis of effective and
sustainable competition, while guaranteeing a basic universal service."

It regulates **electronic communications, electricity, gas, postal
services, the rail network, airport charges** and manages **radio
frequencies**. Since **2019** it has additionally served as Luxembourg's
single point of contact for network and information system security in
energy, transport, health, drinking-water supply, digital infrastructure
and digital services.

## The NIS2 role, closing a previously-flagged gap

[[LU-CTIE]] found and named ILR as Luxembourg's NIS2 competent authority on
2026-09-05 but left it and the transposing act unmodelled, calling that "at
least four new nodes, beyond what a single-question check should add."
This entity and [[LU-LOI-NIS2]] close two of those four. Confirmed by
reading ILR's own pages directly: the **Loi du 5 mai 2026** "assigns to
the ILR the function of competent authority for the security of networks
and information systems for the vast majority of sectors" — extending the
narrower 2019 role to the full NIS2 remit, with the **Commission de
Surveillance du Secteur Financier (CSSF)** holding the equivalent role for
banking and financial-market infrastructure.

## Not modelled

- **CSSF**, ILR's counterpart competent authority for the financial
  sector — see [[LU-LOI-NIS2]].
- **GOVCERT.LU** and **CIRCL**, Luxembourg's two CSIRTs per secondary
  sourcing — see [[LU-LOI-NIS2]] for why they remain unmodelled.
- The **1997/2000 founding instrument(s)** by which ILR itself was
  established — myilr.lu names the years but not an exact law title or
  number, so no `governed-by` edge for ILR's own creation is asserted,
  only for the NIS2 mandate.

## Relationships

- `part-of` [[LU]] — an anchor edge.
- `governed-by` [[LU-LOI-NIS2]] — the Act assigning ILR its NIS2
  competent-authority function.

## Sources

Listed in frontmatter, all four read directly (three on 2026-09-06, ILR's
FAQ page carried over from the 2026-09-05 pass on [[LU-CTIE]]).
