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
coverage: medium
verification: primary-source

start_date: 2004-03-12
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading Real Decreto 421/2004's own text at boe.es directly (2026-08-26, BOE-A-2004-5051): 'El Centro Criptológico Nacional queda adscrito al Centro Nacional de Inteligencia y comparte con éste medios, procedimientos, normativa y recursos' (the CCN is attached to the CNI and shares with it means, procedures, regulations and resources), dated **12 March 2004** — the decree's own date, which this entity did not previously carry precisely. CCN personnel become organically and functionally integrated within the CNI, subject to Ley 11/2002's own statutes."
    confidence: medium
    valid_from: 2004-03-12
    valid_until: null
  - type: governed-by
    target: ES-LEY-11-2002
    source: fact
    evidence: "Confirmed by reading Real Decreto 421/2004's own text directly (2026-08-26): CCN personnel are subject to the statutes and personnel provisions established by Ley 11/2002. Real Decreto 311/2022, also read directly for [[ES-ENS]]'s file, confirms CCN's operational role: Article 33 has it 'articula la respuesta a los incidentes de seguridad' through CCN-CERT and exercises 'coordinación nacional de la respuesta técnica de los equipos de respuesta a incidentes de seguridad informática (CSIRT)', with Additional Provision One requiring CCN and the National Institute of Public Administration to jointly develop awareness and training programmes."
    confidence: medium
    valid_from: 2004-03-12
    valid_until: null

sources:
  - title: "Actualizadas las preguntas frecuentes del nuevo ENS"
    url: "https://www.ccn.cni.es/index.php/es/actualidad-ccn/931-actualizadas-las-preguntas-frecuentes-del-nuevo-ens"
    publisher: "Centro Criptológico Nacional (CCN) — CNI"
    accessed: "2026-08-26"
  - title: "BOE-A-2022-7191 Real Decreto 311/2022, de 3 de mayo, por el que se regula el Esquema Nacional de Seguridad"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "Esquema Nacional de Seguridad"
    url: "https://portal.mineco.gob.es/es-es/ministerio/estrategias/Paginas/Esquema_Nacional_de_Seguridad.aspx"
    publisher: "Ministerio de Economía, Comercio y Empresa"
    accessed: "2026-08-26"
  - title: "BOE-A-2004-5051 Real Decreto 421/2004, de 12 de marzo, por el que se regula el Centro Criptológico Nacional"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2004-5051"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
---

# CCN — Centro Criptológico Nacional

> **Verified 2026-08-26.** All four cited pages were read directly. The
> founding decree's exact date, 12 March 2004, is now precisely dated
> rather than left as a bare year, and mineco.gob.es independently
> confirms CCN's operational role in its own words.

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

Listed in frontmatter, all four read directly this pass: both
constituting BOE texts, the CCN's own ENS FAQ notice (updated with 43
questions, and a transition deadline of 5 May 2024 for RD 3/2010
certifications) and the ministry's own ENS page, which independently
states in its own words that "El Centro Criptológico Nacional (CCN)...
articulará la respuesta a los incidentes de seguridad de entidades del
sector público."

## The CCN is part of the CNI

Added with the intelligence-services batch. The CCN was created on
**12 March 2004** by **Real Decreto 421/2004**, confirmed by reading the
decree's own text directly this pass, and is *adscrito al* [[ES-CNI]] —
Spain's national intelligence service — sharing the CNI's means,
procedures, rules and resources.

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
