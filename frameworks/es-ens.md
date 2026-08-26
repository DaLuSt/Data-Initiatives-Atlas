---
id: ES-ENS
type: framework
name: Esquema Nacional de Seguridad
alternative_names:
  - ENS
  - Spanish National Security Framework
description: >
  Spanish national security framework for the public sector and the entities
  that supply it with technology and services, regulated by Real Decreto
  311/2022 of 3 May, which updated the earlier scheme as part of urgent
  measures to strengthen defences against cyber threats. Its content runs to
  seven chapters, transitory and three additional provisions, and four
  annexes covering security categories, security measures, security audit
  and a glossary. Its 2022 innovations include compliance profiles, a
  protocol for acting on cyber incidents and a new coding system for
  security measure requirements. The Centro Criptológico Nacional is its
  technical authority, publishing the CCN-STIC guides and operating the INES
  measurement tool.

level: national
country: ES
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2022-05-03
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - ES-CCN
related_entities:
  - ES-CCN
  - INTL-ISO-IEC-27001
  - ES-ENI
  - NL-BIO
relationships:
  - type: aligned-with
    target: INTL-ISO-IEC-27001
    source: interpretation
    evidence: "Real Decreto 311/2022's own text, read directly at boe.es (2026-08-26), was searched for an explicit ISO/IEC 27001 reference; none was found in the articles read. The ISO alignment claim rests on secondary commentary (pmg-ssi.com, not read this pass) describing the PDCA continuous-improvement model as ISO-27001-inspired. Downgraded from `source: fact` to `interpretation` pending a direct textual confirmation."
    confidence: low
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: ES-CCN
    source: fact
    evidence: "Confirmed by reading Real Decreto 311/2022's own text at boe.es directly (2026-08-26): Article 33 has the CCN 'articula la respuesta a los incidentes de seguridad' through CCN-CERT structure, exercising 'coordinación nacional de la respuesta técnica de los equipos de respuesta a incidentes de seguridad informática (CSIRT)' for public-sector network and information-system security. Additional Provision One requires the CCN, jointly with the National Institute of Public Administration, to develop awareness, sensitisation and training programmes for public-sector personnel — a joint role this entity did not previously carry precisely."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "Actualizadas las preguntas frecuentes del nuevo ENS"
    url: "https://www.ccn.cni.es/index.php/es/actualidad-ccn/931-actualizadas-las-preguntas-frecuentes-del-nuevo-ens"
    publisher: "Centro Criptológico Nacional (CCN) — CNI"
  - title: "Esquema Nacional de Seguridad"
    url: "https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx"
    publisher: "Ministerio de Economía, Comercio y Empresa"
  - title: "El nuevo ENS 2022 y sus principales cambios"
    url: "https://ciberseguridad.blog/el-nuevo-ens-2022-y-sus-principales-cambios/"
    publisher: "Ciberseguridad.blog"
---

# ENS — Esquema Nacional de Seguridad

> **Verified 2026-08-26.** The decree's own text was read directly at
> boe.es, confirming CCN's coordination role in detail. The ISO/IEC 27001
> alignment claim could not be confirmed directly in the articles read,
> so it is downgraded to an Atlas interpretation at low confidence rather
> than repeated as a stated fact — see below.

## Description

The ENS is Spain's national security framework for the public sector **and
for the entities that supply technology and services to it** — a supply
chain scope that is the feature most worth noting.

**Real Decreto 311/2022 of 3 May** updated the earlier scheme, within a
package of urgent measures to strengthen defences against cyber threats.

Its structure: seven chapters, transitory and three additional provisions,
and four annexes — **security categories, security measures, security audit,
and a glossary**. The 2022 innovations are **compliance profiles**, a
**protocol for acting on cyber incidents**, and a new **coding system for
security-measure requirements**.

[[ES-CCN]] is its technical authority: it publishes the **CCN-STIC guides**
and operates **INES**, the measurement tool.

## A binding baseline, unlike the Dutch one

The nearest comparator in the Atlas is [[NL-BIO]], the Dutch government
information security baseline. Both are national public-sector security
baselines; the resemblance stops at the enforcement model.

The ENS is a **royal decree** with an audit annex and a designated technical
authority operating a measurement tool. It reaches suppliers as well as
administrations. Nothing equivalent to INES — a state-run instrument that
measures compliance across the sector — is modelled for any other country
in the Atlas.

**No relationship between the two is asserted.** They are national answers
to a shared problem, which is not a relationship — the same position taken
for [[FR-FRANCECONNECT]] and [[DE-BUNDID]].

## Its relationship to NIS2 is not modelled, and that is a real gap

The ENS predates [[EU-NIS2]]'s transposition deadline and covers much of the
same ground for the public sector, while [[ES-LCGC]] — the actual
transposition — is still a draft. How the two will fit together is
precisely the question the Spanish institutional dispute described on
[[ES-INCIBE]] is about.

No source read answers it, so nothing is asserted. This is one of the
clearer cases in the Atlas where the *absence* of an edge carries
information: a reader can see that Spain has a mature public-sector security
regime and an unfinished NIS2 transposition, and that the Atlas does not
claim to know how they relate.

## Relationships

- `maintained-by` [[ES-CCN]] — the target organisation maintains this
  entity, per `metadata/relationship-types.md` §2.1.

## Sources

Listed in frontmatter, the BOE text read directly this pass. The CCN's
own notice, the ministry page and the technical commentary were not
attempted.

## `aligned-with` [[INTL-ISO-IEC-27001]], now at reduced confidence

Added with the intelligence-services batch, which made this entity's
isolation visible: [[ES-ENS]] and [[ES-CCN]] were a two-node island in the
graph, reachable from nothing else in the Atlas.

The claim — that the ENS follows a **PDCA continuous-improvement model
inspired by ISO 27001**, and that certification to ISO/IEC 27001 can meet
the ENS's **LOW** security level — was originally sourced to secondary
commentary (pmg-ssi.com) rather than the decree itself. Reading Real
Decreto 311/2022's own text directly this pass did not turn up an
explicit ISO/IEC 27001 reference in the articles read, so the edge is
downgraded to `source: interpretation`, `confidence: low` rather than
repeated as a stated fact on secondary authority alone.

`aligned-with` remains the right type if the claim holds — "two entities
are deliberately kept consistent without one implementing the other" —
but a future pass should search the decree's full text (all its chapters
and annexes, not just the articles read this pass) for the ISO reference
before restoring `source: fact`.

[[GB-CAF]] carries the same relationship to the same standard at full
confidence; that comparison stands regardless of this downgrade.
