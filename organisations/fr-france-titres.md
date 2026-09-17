---
id: FR-FRANCE-TITRES
type: organisation
name: Agence nationale des titres sécurisés
alternative_names:
  - ANTS
  - France Titres
description: >
  French national public administrative establishment (établissement
  public national à caractère administratif) under the Interior
  Ministry's supervision, responsible for designing, managing and
  producing France's secure state-issued titles: passports, national
  identity cards, vehicle registration certificates, driving licences,
  residence permits, and travel documents for refugees and stateless
  persons. Created in 2007 as the Agence nationale des titres
  sécurisés (ANTS); authorised in 2024 to trade as "France Titres" and
  given expanded digital-identity missions, including operating the
  France Identité scheme.

level: national
country: FR
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: "2007-02-22"
end_date: null
last_verified: "2026-09-17"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR
  - FR-FRANCE-IDENTITE
relationships:
  - type: part-of
    target: FR
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Confirmed by reading the founding decree's own text directly at legifrance.gouv.fr (2026-09-17, Décret n° 2007-240 du 22 février 2007), Article 1: 'L'Agence nationale des titres sécurisés est un établissement public national à caractère administratif placé sous la tutelle du ministre de l'intérieur' (the Agency is a national public administrative establishment placed under the supervision of the Minister of the Interior)."
    confidence: high
    valid_from: "2007-02-22"
    valid_until: null

sources:
  - title: "Décret n° 2007-240 du 22 février 2007 portant création de l'Agence nationale des titres sécurisés"
    url: "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000615900"
    publisher: "Légifrance (République française)"
    accessed: "2026-09-17"
  - title: "Décret n° 2024-146 du 26 février 2024 relatif à l'Agence nationale des titres sécurisés"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000049205088"
    publisher: "Légifrance (République française)"
    accessed: "2026-09-17"
  - title: "L'ANTS devient France Titres"
    url: "https://www.interieur.gouv.fr/actualites/communiques-de-presse/lants-devient-france-titres"
    publisher: "Ministère de l'Intérieur"
    accessed: "2026-09-17"
---

# Agence nationale des titres sécurisés (France Titres)

> **Created 2026-09-17**, closing [[FR-FRANCE-IDENTITE]]'s own "not
> itself an Atlas entity" note on France Titres, the scheme's operator.
> Both the 2007 founding decree and the 2024 renaming decree were read
> directly at legifrance.gouv.fr.

## Description

Confirmed by reading the founding decree's own text directly: the
Agence nationale des titres sécurisés (ANTS) is a national public
administrative establishment (Article 1) created to meet state
administrations' needs for "conception, de gestion, de production de
titres sécurisés" — the design, management and production of secure
titles and their associated data transmissions (Article 2). It covers,
per the decree and its companion list-fixing decree, passports,
national identity cards, vehicle registration certificates, driving
licences, residence permits, and travel documents for refugees and
stateless persons.

## From ANTS to France Titres, in the decree's own words

Confirmed by reading Décret n° 2024-146 du 26 février 2024 directly:
Article 1 authorises the agency to trade under the name "France
Titres," while its legal identity as the ANTS is unchanged. Article 2
adds five new missions (numbered 7 through 11 in the amended list),
including defining digital-identity orientations for secure
identification documents, managing the digital systems and mobile
applications behind electronic identification services, processing
and preserving personal data for online services, contributing to
interoperability standards, and representing France in international
and European digital-identity work. Article 3 shortens the director's
term from five to three years; Article 4 expands the governing board
to add the Director General of Foreign Nationals in France, the
Delegate for Road Safety, and two departmental prefects.

These 2024 missions are the statutory basis for France Titres'
operational role behind [[FR-FRANCE-IDENTITE]] and its coordination of
the POTENTIAL and APTITUDE EUDI Wallet pilot consortia — both already
recorded on that entity's own file, which carries the `governed-by`
edge pointing here (the Atlas's convention: assert an operator
relationship once, on the operated entity, not on both sides).

## Relationships

- `part-of` [[FR]] — anchor edge.

[[FR-FRANCE-IDENTITE]] carries `governed-by` → this entity.

## Not modelled

- The vehicle-registration ("carte grise"), driving-licence and
  residence-permit title lines individually — the decree treats them
  as one undifferentiated mission, and no source distinguishes their
  governance.
- The governing board's full composition beyond the 2024 additions
  named in Article 4.

## Sources

Two of two decrees read directly at legifrance.gouv.fr; the Interior
Ministry's own press release corroborates the 2024 renaming.
