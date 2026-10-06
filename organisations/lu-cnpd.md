---
id: LU-CNPD
type: organisation
name: Commission nationale pour la protection des données
name_en: "Luxembourg Data Protection Authority"
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
coverage: medium
verification: primary-source

start_date: 2002-08-02
end_date: null
last_verified: "2026-09-30"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EDPB
  - EU-GDPR
  - LU-LOI-PROTECTION-DONNEES
  - LU-LOI-DONNEES-PENAL-2018
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
  - title: "Mémorial A N° 686 du 16 août 2018 (PDF, full text)"
    url: "https://data.legilux.public.lu/filestore/eli/etat/leg/loi/2018/08/01/a686/jo/fr/pdfa/eli-etat-leg-loi-2018-08-01-a686-jo-fr-pdfa.pdf"
    publisher: "Journal Officiel du Grand-Duché de Luxembourg (Legilux)"
    accessed: "2026-09-30"
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
>
> **Closed 2026-09-30**: `legilux.public.lu`'s main site is still an
> unreadable JavaScript shell, but its `data.legilux.public.lu` filestore
> mirror now serves the founding act's own text directly, confirming the
> CNPD's legal form in its own words — see below.

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

**Narrowed 2026-09-13**: the second law is now [[LU-LOI-DONNEES-PENAL-2018]],
sourced directly this time — its own Article 2(1)(15°), read via Legilux's
static filestore subdomain (a working alternate to the unreadable main
site), names the CNPD as one of its two supervisory authorities, giving
this entity a second statutory basis alongside the GDPR one.

**Closed 2026-09-30**: [[LU-LOI-PROTECTION-DONNEES]]'s own text is now
read directly the same way, via `data.legilux.public.lu`'s filestore
mirror of Mémorial A No. 686. Article 3 states in so many words: "La
Commission nationale pour la protection des données, désignée ci-après
par le terme «CNPD», est un établissement public indépendant doté de la
personnalité juridique" (an independent public institution with legal
personality). Article 73 additionally confirms this CNPD continues the
legal personality, staff and commitments of the body first created by the
repealed 2 August 2002 act — the CNPD is a continuous institution rather
than a 2018 creation, even though its current statutory basis dates from
that year. `start_date` is set to **2 August 2002** on this basis rather
than left `null` or dated to 2018; the 2002 act itself (not read directly,
named only by its repeal date in Article 72 of the 2018 law) is not
independently modelled as a separate Atlas entity.

## Relationships

- `participates-in` [[EU-EDPB]].
- Inbound: `applies-to` from [[LU-LOI-PROTECTION-DONNEES]], the act that
  organises this authority, and from [[LU-LOI-DONNEES-PENAL-2018]], its
  companion act for criminal and national-security data processing.

## Sources

Listed in frontmatter. The original four read directly in the 2026-08-25
pass; CNPD's "Droit luxembourgeois" page added and read directly
2026-09-05. `legilux.public.lu`'s main site was tried on both passes and
found to be a JavaScript single-page application with no static content;
its `data.legilux.public.lu` filestore mirror, found 2026-09-30, serves
the founding act's own PDF text directly instead.
