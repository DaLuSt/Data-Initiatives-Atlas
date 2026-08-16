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
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - FR-LIL
relationships:
  - type: applies-to
    target: FR-LIL
    source: fact
    evidence: "The CNIL publishes and maintains guidance on the entry into force of the new loi Informatique et Libertés and its implementing decree; the 2018 ordinance moved the CNIL from prior control to posterior control based on accountability, and specifies that its corrective measures and sanctions also apply to processors (cnil.fr 'Entrée en vigueur de la nouvelle loi Informatique et Libertés'; moirouxavocats.com). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Entrée en vigueur de la nouvelle loi Informatique et Libertés"
    url: "https://www.cnil.fr/fr/entree-en-vigueur-de-la-nouvelle-loi-informatique-et-libertes"
    publisher: "Commission nationale de l'informatique et des libertés (CNIL)"
  - title: "Entrée en vigueur de la nouvelle loi Informatique et Libertés et de son décret d'application"
    url: "https://www.cnil.fr/fr/entree-en-vigueur-de-la-nouvelle-loi-informatique-et-libertes-et-de-son-decret-dapplication"
    publisher: "Commission nationale de l'informatique et des libertés (CNIL)"
  - title: "Les modifications apportées par l'ordonnance n° 2018-1125 du 12 décembre 2018 à la loi n° 78-17 du 6 janvier 1978"
    url: "https://moirouxavocats.com/actualites/les-modifications-apportees-par-lordonnance-n-2018-1125-du-12-decembre-2018-a-la-loi-n-78-17-du-6-janvier-1978-relative-a-linformatique-aux-fichiers-et-aux-libertes/"
    publisher: "Moiroux Avocats"
  - title: "Cybersécurité : le rôle central de la CNIL et des autorités compétentes dans l'application de DORA et NIS2"
    url: "https://cloix-mendesgil.com/eclairages-juridiques/droit-du-numerique-donnees-et-conformite/cybersecurite-le-role-central-de-la-cnil-et-des-autorites-competentes-dans-lapplication-de-dora-et-nis2/"
    publisher: "Cloix & Mendès-Gil"
---

# CNIL — Commission nationale de l'informatique et des libertés

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The CNIL is France's data protection supervisory authority. It supervises
[[EU-GDPR]] and [[FR-LIL]], and publishes guidance for citizens and
controllers.

The **2018 reform changed its operating model**: the ordinance of
12 December 2018 moved the CNIL **from prior control to posterior control**,
based on the accountability of organisations, and specified that its
corrective measures and sanctions apply to **processors** as well as
controllers.

`coverage: low`: its composition, appointment process, powers in detail and
its relationship with [[FR-ANSSI]] under the cybersecurity regime are not
recorded. Sources describe the CNIL as strengthening collaboration with
ANSSI, but the arrangement was not established well enough to model.

## Four national DPAs, one European link

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — sourced |
| Germany | [[DE-BFDI]] | no — refused |
| Belgium | [[BE-APD]] | no — refused |
| France | **CNIL** | no — refused |

Four national data protection authorities now sit in the Atlas, and **only
one connects to the European Data Protection Board.** No source read for
the German, Belgian or French authority mentions the EDPB at all.

This is now the Atlas's clearest single example of a **sourcing artefact
masquerading as structure**. Every one of these authorities sits on the
Board; the graph shows one of them doing so, purely because one Dutch page
happened to say it. A reader taking the graph at face value would conclude
the EDPB has one member.

The `verification: search-only` marking on all four is what keeps that
readable as an artefact rather than a finding. It is logged in
`discovery/unresolved.md` and is among the cheapest items in the
re-verification pass — four pages.

## Relationships

- `applies-to` [[FR-LIL]].

## Sources

Listed in frontmatter — two CNIL pages and two law-firm commentaries.
