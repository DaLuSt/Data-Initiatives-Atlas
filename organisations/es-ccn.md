---
id: ES-CCN
type: organisation
name: Centro Criptológico Nacional
alternative_names:
  - CCN
  - CCN-CERT
  - National Cryptologic Centre
description: >
  Spanish public-sector cybersecurity body attached to the national
  intelligence centre, and the technical authority for the Esquema Nacional
  de Seguridad. Real Decreto 311/2022 assigns it the role of state-level
  public coordinator for the technical response of incident response teams
  through CCN-CERT, and the development of awareness, training and
  sensitisation programmes for public-sector personnel. It publishes the
  CCN-STIC guides and operates the INES measurement tool, and its
  certification body determines functional security and assurance
  requirements for the national evaluation and certification scheme.

level: national
country: ES
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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - ES-ENS
  - ES-INCIBE
  - ES-CNI
  - ES-LEY-11-2002
relationships:
  - type: part-of
    target: ES-CNI
    source: fact
    evidence: "The Centro Criptológico Nacional was created in 2004 by Real Decreto 421/2004 and is adscrito al Centro Nacional de Inteligencia, sharing with it means, procedures, rules and resources, and is governed by Ley 11/2002, de 6 de mayo, reguladora del Centro Nacional de Inteligencia, which entrusts to the CNI the functions relating to the security of information technologies (ccn.cni.es; ccn-cert.cni.es 'Centro Criptológico Nacional'; boe.es BOE-A-2004-5051 Real Decreto 421/2004). NOT READ — search-only."
    confidence: medium
    valid_from: 2004-03-12
    valid_until: null
  - type: governed-by
    target: ES-LEY-11-2002
    source: fact
    evidence: "The Centro Criptológico Nacional shares with the Centro Nacional de Inteligencia its means, procedures, rules and resources and is governed by Ley 11/2002, de 6 de mayo, reguladora del Centro Nacional de Inteligencia; that act entrusts to the CNI the exercise of the functions relating to the security of information technologies, and Real Decreto 421/2004 regulates and defines the CCN's scope and functions (ccn.cni.es; ccn-cert.cni.es 'Centro Criptológico Nacional'; oc.ccn.cni.es 'Normativa'). NOT READ — search-only."
    confidence: medium
    valid_from: 2004-03-12
    valid_until: null

sources:
  - title: "Actualizadas las preguntas frecuentes del nuevo ENS"
    url: "https://www.ccn.cni.es/index.php/es/actualidad-ccn/931-actualizadas-las-preguntas-frecuentes-del-nuevo-ens"
    publisher: "Centro Criptológico Nacional (CCN) — CNI"
  - title: "BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191"
    publisher: "Boletín Oficial del Estado (BOE)"
  - title: "Esquema Nacional de Seguridad"
    url: "https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx"
    publisher: "Ministerio de Economía, Comercio y Empresa"
---

# CCN — Centro Criptológico Nacional

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The CCN is Spain's public-sector cybersecurity body, attached to the
national intelligence centre (CNI), and the **technical authority for
[[ES-ENS]]**.

Real Decreto 311/2022 assigns it two named roles:

1. **state-level public coordinator** for the technical response of incident
   response teams, through **CCN-CERT**;
2. development of **awareness, training and sensitisation** programmes for
   public-sector personnel.

It publishes the **CCN-STIC guides** and operates **INES**, the compliance
measurement tool, and its certification body determines functional security
and assurance requirements under the national evaluation and certification
scheme for information technologies.

## Relationships

The `maintained-by` edge for [[ES-ENS]] lives **on [[ES-ENS]]**, pointing
here — `metadata/relationship-types.md` §2.1 defines `maintained-by` as
*"the target organisation maintains this entity"*, so it belongs on the
maintained thing.

## Sources

Listed in frontmatter — the CCN's own ENS FAQ notice, the BOE text of the
decree that assigns it these roles, and a ministry page.

## The CCN is part of the CNI

Added with the intelligence-services batch. The CCN was created in 2004 by
**Real Decreto 421/2004** and is *adscrito al* [[ES-CNI]] — Spain's national
intelligence service — sharing the CNI's means, procedures, rules and
resources.

It is governed by [[ES-LEY-11-2002]], the act regulating the CNI, which
entrusts to the CNI the functions relating to the security of information
technologies. The CCN is how the CNI discharges that part of its statutory
mandate.

So the authority behind [[ES-ENS]], Spain's national security framework for
public-sector information systems, is a component of the intelligence
service. The United Kingdom is the only other country in the Atlas arranged
this way, with [[GB-NCSC]] inside [[GB-GCHQ]]; [[ES-INCIBE]], by contrast,
sits outside that structure entirely.

Real Decreto 421/2004 is **not** modelled as an entity. It is a royal decree
rather than an act, and the Atlas holds the statute it implements.
