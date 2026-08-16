---
id: FR-ANSSI
type: organisation
name: Agence nationale de la sécurité des systèmes d'information
alternative_names:
  - ANSSI
  - French National Cybersecurity Agency
description: >
  French national authority for cybersecurity and cyberdefence, a component
  of the Secrétariat général de la défense et de la sécurité nationale. Its
  five stated missions are to defend, know, share, support and regulate,
  building and organising interministerially the nation's protection
  against cyberattacks and contributing to the stability of cyberspace.

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
  - FR-NIS2-LOI
relationships:
  - type: applies-to
    target: FR-NIS2-LOI
    source: fact
    evidence: "The law transposing NIS2 designates ANSSI as the competent national authority for cybersecurity, and since 17 March 2026 ANSSI has made available the Cyber France reference framework (aventris.fr; legiscope.com; nis-2-directive.com France page). NOT READ — search-only. Note the transposing instrument's own status is contested — see FR-NIS2-LOI."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Au cœur d'un collectif, pour une nation cyber-résiliente — ANSSI"
    url: "https://cyber.gouv.fr/"
    publisher: "Agence nationale de la sécurité des systèmes d'information (ANSSI)"
  - title: "Missions — ANSSI"
    url: "https://cyber.gouv.fr/nous-connaitre/lagence/missions/"
    publisher: "Agence nationale de la sécurité des systèmes d'information (ANSSI)"
  - title: "Agence nationale de la sécurité des systèmes d'information | SGDSN"
    url: "https://www.sgdsn.gouv.fr/notre-organisation/composantes/agence-nationale-de-la-securite-des-systemes-dinformation"
    publisher: "Secrétariat général de la défense et de la sécurité nationale (SGDSN)"
  - title: "Avancement de la transposition de la directive NIS 2"
    url: "https://aide.monespacenis2.cyber.gouv.fr/fr/article/avancement-de-la-transposition-de-la-directive-nis-2-1b3j1da/"
    publisher: "MonEspaceNIS2 (ANSSI)"
---

# ANSSI — Agence nationale de la sécurité des systèmes d'information

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

ANSSI is France's national authority for cybersecurity and cyberdefence, a
component of the **Secrétariat général de la défense et de la sécurité
nationale (SGDSN)**. Its stated purpose is to build and organise, in an
interministerial way, the nation's protection against cyberattacks and to
contribute to the stability of cyberspace.

It describes **five missions**: defend, know, share, support and regulate.

It is designated the competent national authority under France's NIS2
transposition, and since **17 March 2026** has made available the *Cyber
France* reference framework. It also runs **MonEspaceNIS2**, the
registration and guidance service for entities in scope.

`coverage: low`: the agency's founding instrument, size, and the boundary
between its remit and the CNIL's are not recorded.

## Four national cybersecurity authorities — and a Dutch gap that persists

| Country | Authority | Under |
|---|---|---|
| France | **ANSSI** | [[FR-NIS2-LOI]] *(status contested)* |
| Belgium | [[BE-CCB]] | [[BE-NIS2-WET]] |
| Germany | [[DE-BSI]] | [[DE-BSIG]] as revised by [[DE-NIS2UMSUCG]] |
| Netherlands | *not modelled* | [[NL-CBW]] |

The Belgian batch noted that the Netherlands has a NIS2 act with no
authority attached, because the NCSC has never been an Atlas entity. A
fourth country has now been added without closing it — three of four
countries have their authority modelled and the Netherlands still does not.

That is the second time a Dutch gap has been made more conspicuous by
adding another country rather than by anyone examining the Dutch layer.
The other is [[EU-INSPIRE]] → [[NL]]. Both are logged.

## Relationships

- `applies-to` [[FR-NIS2-LOI]] — at **`confidence: low`**, because the
  designation is sourced but the instrument doing the designating has a
  contested status. If the transposing law turns out not to be in force,
  this relationship describes a designation that has not yet taken effect.

## Sources

Listed in frontmatter.
