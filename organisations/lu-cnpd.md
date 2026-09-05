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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - EU-GDPR
  - LU-LOI-PROTECTION-DONNEES
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Confirmed by reading cnpd.public.lu directly (2026-08-25): its own news feed reports 'La CNPD a participé au High-Level Meeting de l'EDPB à Dublin' (the CNPD participated in the EDPB's High-Level Meeting in Dublin), 21/07/2026 — direct evidence of participation, not only the Article 68(3) GDPR composition rule (that the Board is composed of the head of one supervisory authority per member state) this edge previously rested on alone. That rule, confirmed independently by reading gdpr-info.eu's and gdprhub.eu's texts of Article 68 GDPR directly, still explains why every member state's authority holds a seat."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CNPD — Commission nationale pour la protection des données"
    url: "https://cnpd.public.lu/"
    publisher: "Commission nationale pour la protection des données (CNPD)"
    accessed: "2026-08-25"
  - title: "Législation — CNPD"
    url: "https://cnpd.public.lu/fr/legislation.html"
    publisher: "Commission nationale pour la protection des données (CNPD)"
    accessed: "2026-08-25"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-25"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
    accessed: "2026-08-25"
  - title: "Droit luxembourgeois — CNPD"
    url: "https://cnpd.public.lu/fr/legislation/droit-lux.html"
    publisher: "Commission nationale pour la protection des données (CNPD)"
    accessed: "2026-09-05"
---

# Commission nationale pour la protection des données

> **Verified 2026-08-25.** All four cited pages were read directly. A
> stronger confirmation for [[EU-EDPB]] participation replaces the
> composition-rule-only reasoning this edge previously carried, and the
> exact date of Luxembourg's GDPR implementation act is now sourced —
> see below.
>
> **Updated 2026-09-05**: the act's official title was found and it is
> now modelled as [[LU-LOI-PROTECTION-DONNEES]].

## Description

Confirmed by reading cnpd.public.lu directly (2026-08-25): the CNPD is
Luxembourg's data protection supervisory authority, headquartered at 15
Boulevard du Jazz, L-4370 Belvaux.

## ⚠ Two CNPDs

Portugal's authority is **also** CNPD — [[PT-CNPD]], the Comissão Nacional de
Proteção de Dados. Two member states, two supervisory authorities, the same
three letters, and both added in the same batch.

The scoped IDs keep them apart. As with the two INEs ([[PT-INE]] and
[[ES-INE]]), the collision is real and in the world, not an Atlas artefact.

## Luxembourg's GDPR implementation act, modelled 2026-09-05

Every other member state in the Atlas has a modelled implementing act —
[[NL-UAVG]], [[DE-BDSG]], [[ES-LOPDGDD]], [[PL-ODO]], [[IE-DPA-2018]],
[[PT-LEI-58-2019]] and [[CZ-ZAKON-110-2019]]. The 2026-08-25 pass found
CNPD's own "Législation" page linking to the law under the colloquial
label "Loi 'Protection des données'" at
`legilux.public.lu/eli/etat/leg/loi/2018/08/01/a686/jo`, confirming the
**1 August 2018** date but not an official title — asserting one the
Atlas had not read would have been exactly the kind of guess this
project's discipline exists to prevent.

This pass found the title: CNPD's own "Droit luxembourgeois" legislation
page, read directly, names it in full — "Loi du 1er août 2018 portant
organisation de la Commission nationale pour la protection des données
et du régime général sur la protection des données" — and, usefully,
distinguishes it from a **second, separate law of the same date**
(Mémorial A No. 689) implementing the Law Enforcement Directive in
criminal and national-security matters, which is not this act and is not
modelled. `legilux.public.lu` itself remains unreadable (JavaScript
single-page application, no static content). The act is now modelled as
[[LU-LOI-PROTECTION-DONNEES]].

## Relationships

- `participates-in` [[EU-EDPB]].
- Inbound: `applies-to` from [[LU-LOI-PROTECTION-DONNEES]], the act that
  organises this authority.

## Sources

Listed in frontmatter. The original four read directly in the 2026-08-25
pass; CNPD's "Droit luxembourgeois" page added and read directly
2026-09-05. `legilux.public.lu` was tried on both passes and found to be
a JavaScript single-page application with no static content.
