---
id: LU-CNPD
type: organisation
name: Commission nationale pour la protection des données
alternative_names:
  - CNPD
  - CNPD Luxembourg
  - Luxembourg Data Protection Authority
description: >
  Luxembourg's data protection supervisory authority.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - EU-GDPR
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Article 68(3) GDPR provides that the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives; the Commission nationale pour la protection des données is Luxembourg's supervisory authority (gdpr-info.eu 'Art. 68 GDPR — European Data Protection Board'; gdprhub.eu 'Article 68 GDPR'; edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CNPD — Commission nationale pour la protection des données"
    url: "https://cnpd.public.lu/"
    publisher: "Commission nationale pour la protection des données (CNPD)"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
---

# Commission nationale pour la protection des données

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

The CNPD is Luxembourg's data protection supervisory authority.

## ⚠ Two CNPDs

Portugal's authority is **also** CNPD — [[PT-CNPD]], the Comissão Nacional de
Proteção de Dados. Two member states, two supervisory authorities, the same
three letters, and both added in the same batch.

The scoped IDs keep them apart. As with the two INEs ([[PT-INE]] and
[[ES-INE]]), the collision is real and in the world, not an Atlas artefact.

## ⚠ Luxembourg's GDPR implementation act is not modelled

Every other member state in the Atlas has one — [[NL-UAVG]], [[DE-BDSG]],
[[ES-LOPDGDD]], [[PL-ODO]], [[IE-DPA-2018]], [[PT-LEI-58-2019]] and
[[CZ-ZAKON-110-2019]]. Luxembourg's (the law of 1 August 2018) was **not
identified from a citable source**, so this authority carries no
`applies-to` edge to a national act. Logged in `discovery/unresolved.md`.

## Relationships

- `participates-in` [[EU-EDPB]].

## Sources

Listed in frontmatter.
