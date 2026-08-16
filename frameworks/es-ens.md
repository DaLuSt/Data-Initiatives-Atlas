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
verification: search-only

start_date: 2022-05-03
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - ES-CCN
related_entities:
  - ES-CCN
  - ES-ENI
  - NL-BIO
relationships:
  - type: maintained-by
    target: ES-CCN
    source: fact
    evidence: "Real Decreto 311/2022 assigns the Centro Criptológico Nacional the role of state-level public coordinator for the technical response of incident response teams through CCN-CERT and the development of awareness, training and sensitisation programmes for public-sector personnel; the CCN is the technical authority that publishes the CCN-STIC guides and the INES measurement tool, and has published the changes and updates to the scheme on the ENS portal (ccn.cni.es 'Actualizadas las preguntas frecuentes del nuevo ENS'; BOE-A-2022-7191; inqnable.es). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191"
    publisher: "Boletín Oficial del Estado (BOE)"
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

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

Listed in frontmatter — the BOE text, the CCN's own notice, a ministry page
and a technical commentary.
