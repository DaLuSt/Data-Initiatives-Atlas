---
id: IT-CIE
type: platform
name: Carta d'Identità Elettronica
alternative_names:
  - CIE
  - CIE ID
  - Electronic Identity Card
description: >
  Italy's electronic identity card, described by the Ministry of the
  Interior's own site as "the only physical and digital identity
  certified by the Italian State." Alongside its physical function as
  an identity document, the companion CieID app lets holders use it as
  a digital-identity credential for public-administration services
  online — one of three authentication tools [[IT-CAD]] Article 66
  provides for, alongside [[IT-SPID]] and the Carta Nazionale dei
  Servizi (CNS). The Ministry of the Interior administers the
  programme; the Istituto Poligrafico e Zecca dello Stato (IPZS)
  produces the physical cards — neither is an Atlas entity.

level: national
country: IT
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IT
  - IT-CAD
  - IT-SPID
relationships:
  - type: governed-by
    target: IT-CAD
    source: fact
    evidence: "Confirmed by reading docs.italia.it's own text of CAD Article 66 directly (2026-09-04): the article establishes that the electronic identity card's characteristics and issuance procedures are defined by presidential decree, that it must carry personal identification data and fiscal code, and may optionally carry blood type, health preferences, biometric data (excluding DNA) and electronic-signature-supporting information. The same article, in the same breath, establishes the Carta Nazionale dei Servizi (CNS) as a second authentication credential public administrations may issue on request — CIE and CNS share this one legal basis, which is why no separate CNS entity is created; see the entity body."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Carta di Identità Elettronica (CIE)"
    url: "https://www.cartaidentita.interno.gov.it/"
    publisher: "Ministero dell'Interno"
    accessed: "2026-09-04"
  - title: "Codice dell'amministrazione digitale | Art. 66. Carta d'identità elettronica e carta nazionale dei servizi"
    url: "https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2018-09-28/_rst/capo5_sezione3_art66.html"
    publisher: "Team Digitale / docs.italia.it"
    accessed: "2026-09-04"
---

# Carta d'Identità Elettronica (CIE)

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had recorded since the country-expansion
> pass that [[IT-CAD]] names three authentication credentials — SPID,
> CIE and CNS — while only SPID was modelled. Two pages were read
> directly this pass: the Ministry of the Interior's own CIE site, and
> the CAD's own Article 66 text.

## Description

The CIE is Italy's electronic identity card. The Ministry of the
Interior's own site states it directly: **"l'unica identità fisica e
digitale certificata dallo Stato italiano"** (the only physical and
digital identity certified by the Italian State). Beyond its physical
function, the companion **CieID** app — promoted extensively on the same
official page — lets holders use the card as a digital-identity
credential for public-administration services online, the same role
[[IT-SPID]] plays through a different mechanism.

The **Ministry of the Interior** administers the programme; the
**Istituto Poligrafico e Zecca dello Stato (IPZS)**, shown in the
official site's own footer, produces the physical cards. Neither body
is an Atlas entity, so no `maintained-by` edge is asserted — the same
honest gap [[PL-MOBYWATEL]] records for bodies named only in passing.

## One article, two credentials — why CNS is not a separate entity

[[IT-CAD]]'s own **Article 66**, read directly, is titled "Carta
d'identità elettronica e carta nazionale dei servizi" and establishes
**both** the CIE and the **Carta Nazionale dei Servizi (CNS)** in the
same provision: the CIE's characteristics are set by presidential
decree and it must carry identification data and a fiscal code; the
CNS is a second credential public administrations may issue "su
richiesta del soggetto interessato" (on the interested party's
request), valid for online access "regardless of issuer," and each
issuing administration bears its own production cost.

The CNS is narrower in practice — commonly issued as a regional health
card or a chamber-of-commerce credential rather than a general national
identity document — and no source read names an operator distinct from
the many public bodies Article 66 permits to issue one. Rather than
model a credential with no single custodian, this entity records CNS
here, on its statutory sibling, exactly as [[AT-EGOVG]] recorded three
consuming statutes on its own page instead of creating an entity for
each.

## Three credentials, one code

[[IT-CAD]] Article 64 creates [[IT-SPID]]; Article 66 creates the CIE
and the CNS. All three are named in the CAD's own text as
authentication tools for accessing Italian public-administration
services online, and Article 71 sets the technical rules common to all
of them. This is the same "codified act" shape [[IT-CAD]]'s own entity
already describes: one instrument amended in place, rather than one
statute per credential.

## Relationships

- `governed-by` [[IT-CAD]] — Article 66.

## Sources

Listed in frontmatter, both read directly this pass.
