---
id: FR-CNIL
type: organisation
name: Commission nationale de l'informatique et des libertés
alternative_names:
  - CNIL
  - French Data Protection Authority
description: >
  French data protection supervisory authority. It supervises compliance
  with the GDPR and the loi Informatique et Libertés, and publishes
  guidance for citizens and controllers. The 2018 reform moved it from a
  model of prior control to posterior control based on the accountability
  of organisations, and extended its corrective measures and sanctions to
  processors.

level: national
country: FR
region: null

status: active
confidence: medium
coverage: low
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
  - EU-EDPB
  - FR-LIL
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Confirmed by reading gdpr-info.eu's own text of Article 68(3) GDPR directly (2026-08-26 and re-confirmed 2026-08-27): 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.' The CNIL is France's supervisory authority under the GDPR — a fact this entity's own description states without qualification. This is the same evidentiary basis on which ES-AEPD's and BE-APD's identical edges were confirmed as `source: fact` in the Spain and Belgium re-verification passes; this entity's prior text applied a stricter, inconsistent standard (requiring a source to name the CNIL specifically, rather than accepting the general composition rule as dispositive) and is corrected here for consistency."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-LIL
    source: fact
    evidence: "Confirmed by reading cnil.fr's own pages directly (2026-08-26): 'La loi n° 2018-493 du 20 juin 2018 ... a modifié la loi Informatique et Libertés afin de mettre en conformité le droit national avec le cadre juridique européen' and moirouxavocats.com's confirmation of ordonnance n° 2018-1125 du 12 décembre 2018's exact title. cloix-mendesgil.com, read independently, confirms current CNIL/ANSSI collaboration: 'la CNIL renforce sa collaboration avec l'ANSSI, l'ACPR et la Banque de France' (the CNIL is strengthening its collaboration with ANSSI, the ACPR and the Banque de France)."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Entrée en vigueur de la nouvelle loi Informatique et Libertés"
    url: "https://www.cnil.fr/fr/entree-en-vigueur-de-la-nouvelle-loi-informatique-et-libertes"
    publisher: "Commission nationale de l'informatique et des libertés (CNIL)"
    accessed: "2026-08-26"
  - title: "Les modifications apportées par l'ordonnance n° 2018-1125 du 12 décembre 2018 à la loi n° 78-17 du 6 janvier 1978"
    url: "https://moirouxavocats.com/actualites/les-modifications-apportees-par-lordonnance-n-2018-1125-du-12-decembre-2018-a-la-loi-n-78-17-du-6-janvier-1978-relative-a-linformatique-aux-fichiers-et-aux-libertes/"
    publisher: "Moiroux Avocats"
    accessed: "2026-08-26"
  - title: "Cybersécurité : le rôle central de la CNIL et des autorités compétentes dans l'application de DORA et NIS2"
    url: "https://cloix-mendesgil.com/eclairages-juridiques/droit-du-numerique-donnees-et-conformite/cybersecurite-le-role-central-de-la-cnil-et-des-autorites-competentes-dans-lapplication-de-dora-et-nis2/"
    publisher: "Cloix & Mendès-Gil"
    accessed: "2026-08-26"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-26"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
    accessed: "2026-08-26"
  - title: "Entrée en vigueur de la nouvelle loi Informatique et Libertés et de son décret d'application"
    url: "https://www.cnil.fr/fr/entree-en-vigueur-de-la-nouvelle-loi-informatique-et-libertes-et-de-son-decret-dapplication"
    publisher: "Commission nationale de l'informatique et des libertés (CNIL)"
    accessed: "2026-08-26"
---

# CNIL — Commission nationale de l'informatique et des libertés

> **Re-verified 2026-08-27, one correction.** All six cited pages were
> read directly in the prior pass. CNIL's own page confirms the 2018
> reform verbatim, and a 2025-2028 strategy article confirms current
> CNIL/ANSSI collaboration. The `participates-in` [[EU-EDPB]] edge was
> previously kept at "refused" because no page names the CNIL
> specifically — a stricter standard than this Atlas applied to the
> identical Article 68(3) evidence for [[ES-AEPD]] and [[BE-APD]] in
> later passes. Corrected here for consistency: the edge now stands
> confirmed, `source: fact`.

## Description

Confirmed by reading cnil.fr directly (2026-08-26): the CNIL is
France's data protection supervisory authority. It supervises
[[EU-GDPR]] and [[FR-LIL]], and publishes guidance for citizens and
controllers.

The **2018 reform changed its operating model**: the ordinance of
12 December 2018 moved the CNIL **from prior control to posterior control**,
based on the accountability of organisations, and specified that its
corrective measures and sanctions apply to **processors** as well as
controllers.

`coverage: low`: its composition, appointment process and powers in detail
are not recorded. Its relationship with [[FR-ANSSI]] under the
cybersecurity regime is now confirmed to exist — cloix-mendesgil.com,
read directly this pass, states "la CNIL renforce sa collaboration avec
l'ANSSI" — but not established well enough to model as a relationship.

## Four national DPAs, all four now connected to the Board

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — sourced |
| Germany | [[DE-BFDI]] | **yes** — sourced (2026-08-22) |
| Belgium | [[BE-APD]] | **yes** — sourced (2026-08-26) |
| France | **CNIL** | **yes** — sourced (corrected 2026-08-27) |

All four now connect to the European Data Protection Board. This
entity's own edge was the last of the four to close: gdpr-info.eu's
text of Article 68(3) GDPR — read directly in the prior pass and again
this pass — states plainly that the Board is composed of one
supervisory authority per Member State, and the CNIL is undisputedly
France's. That is a general rule stated directly, not an inference from
something adjacent; the same reasoning closed [[DE-BFDI]]'s gap in an
earlier pass and [[BE-APD]]'s and [[ES-AEPD]]'s in later ones.

Logged in `discovery/unresolved.md`.

## Relationships

- `participates-in` [[EU-EDPB]] — confirmed this pass via Article 68(3)
  GDPR's own text, correcting a previously inconsistent refusal;
  `confidence: medium`.
- `applies-to` [[FR-LIL]].

## Sources

Listed in frontmatter, all six read directly (five in the prior pass,
gdpr-info.eu re-confirmed this pass).
