---
id: ES-CNI
type: organisation
name: Centro Nacional de Inteligencia
alternative_names:
  - CNI
  - National Intelligence Centre
description: >
  Spain's national intelligence service, integrated within the structure of
  the Ministry of Defence as a public body with functional autonomy and its
  own legal personality, and reporting to the President of the Government.
  It was created by Ley 11/2002, whose Article 12 provides for prior
  judicial control of activities affecting fundamental rights, exercised
  under Ley Orgánica 2/2002.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2002-05-06
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - ES-LEY-11-2002
  - ES-LO-2-2002
  - ES-CCN
relationships:
  - type: governed-by
    target: ES-LEY-11-2002
    source: fact
    evidence: "The CNI was created by Ley 11/2002, de 6 de mayo, reguladora del Centro Nacional de Inteligencia; the CNI is ascribed to the Ministry of Defence as a public organisation with functional autonomy and its own legal personality, and reports to the President of the Government (defensa.gob.es 'Centro Nacional de Inteligencia'; boe.es BOE-A-2002-8628; es.wikipedia.org 'Centro Nacional de Inteligencia (España)'). NOT READ — search-only."
    confidence: medium
    valid_from: 2002-05-06
    valid_until: null
  - type: governed-by
    target: ES-LO-2-2002
    source: fact
    evidence: "Article 12 of Ley 11/2002 establishes that an organic law would prescribe the form of prior judicial control of CNI activities; Ley Orgánica 2/2002, de 6 de mayo, is complementary to Ley 11/2002 and modifies the Ley Orgánica del Poder Judicial to establish judicial control of CNI activities affecting the fundamental rights recognised in Articles 18.2 and 18.3 of the Spanish Constitution (boe.es BOE-A-2002-8627; catedrapsyd.unizar.es 'Los controles judiciales de la actividad del Centro Nacional de Inteligencia'; iberley.es). NOT READ — search-only."
    confidence: medium
    valid_from: 2002-05-06
    valid_until: null

sources:
  - title: "Centro Nacional de Inteligencia — organigrama"
    url: "https://www.defensa.gob.es/ministerio/organigrama/cni/"
    publisher: "Ministerio de Defensa de España"
  - title: "Organización del CNI"
    url: "https://www.cni.es/sobre-el-cni/organizacion"
    publisher: "Centro Nacional de Inteligencia (CNI)"
  - title: "Ley Orgánica 2/2002, de 6 de mayo, reguladora del control judicial previo del Centro Nacional de Inteligencia"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2002-8627"
    publisher: "Agencia Estatal Boletín Oficial del Estado (BOE)"
  - title: "Centro Nacional de Inteligencia (España)"
    url: "https://es.wikipedia.org/wiki/Centro_Nacional_de_Inteligencia_(Espa%C3%B1a)"
    publisher: "Wikipedia"
---

# Centro Nacional de Inteligencia (CNI)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The CNI is Spain's national intelligence service. Its position in the state
is unusual and the sources are precise about it: it is **integrated within
the structure of the Ministry of Defence** as a public body with *functional
autonomy and its own legal personality*, while **reporting to the President
of the Government**.

Its head is the *Secretario de Estado Director*, appointed by royal decree.

## Spain is the one-service country

Every other country in this batch splits the function at least two ways —
civilian and military, or domestic and foreign. Spain does not: the CNI is a
**single** service covering both, which is why this is the only country in
the batch with one service entity rather than two, three or four.

## Prior judicial control, and why it needed a second act

Spain's authorisation model is the third distinct answer in this batch, and
the cleanest constitutionally:

| Country | Who authorises intrusive measures |
|---|---|
| Netherlands | Minister, then **binding** review by [[NL-TIB]] |
| France | **Prime Minister**, after an opinion from [[FR-CNCTR]] |
| **Spain** | **A judge**, in advance |

Article 12 of [[ES-LEY-11-2002]] provides for prior judicial control but
could not itself create it: establishing it meant amending the *Ley Orgánica
del Poder Judicial*, which requires an **organic law**. Hence
[[ES-LO-2-2002]], passed the **same day**, 6 May 2002, doing nothing but
that.

Two acts of identical date, one ordinary and one organic, is not
administrative duplication — it is Spanish constitutional law working as
designed, and it is the reason this entity carries two `governed-by` edges
where [[BE-VSSE]] carries one.

The control covers activities affecting the rights in **Articles 18.2 and
18.3** of the Constitution: inviolability of the home, and secrecy of
communications.

## The bridge to the existing Atlas

[[ES-CCN]], the Centro Criptológico Nacional, was already an Atlas entity —
Spain's authority for information-systems security and the body behind
[[ES-ENS]]. It is `part-of` the CNI: created by Real Decreto 421/2004, *adscrito
al Centro Nacional de Inteligencia*, sharing the CNI's means, procedures,
rules and resources, and governed by Ley 11/2002.

That edge is asserted on [[ES-CCN]] rather than here, and it is the single
most load-bearing connection in this batch: it joins the entire
national-security cluster to the Atlas's existing cyber-security layer
through a body that was already present.

## Not modelled

- **CIFAS**, the armed forces' intelligence centre, and the information
  services of the National Police and Guardia Civil. The sources mention a
  common inspection regime covering them; none was researched.
- The **Comisión Delegada del Gobierno para Asuntos de Inteligencia**, the
  government committee that sets the CNI's annual objectives.
- The CNI's predecessor, **CESID**, and the 2002 reform that replaced it.

## Relationships

- `governed-by` [[ES-LEY-11-2002]] and [[ES-LO-2-2002]].

## Sources

Listed in frontmatter.
