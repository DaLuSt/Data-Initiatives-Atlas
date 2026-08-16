---
id: ES-NTI-RISP
type: standard
name: Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información
alternative_names:
  - NTI-RISP
  - DCAT-AP-ES
description: >
  Spanish technical interoperability standard for selecting, identifying,
  describing and making datasets available for re-use, and the regulatory
  framework in Spain for managing and opening public data since 2013. It is
  one of the Technical Interoperability Standards provided for by the first
  additional provision of Real Decreto 4/2010, which are mandatory for
  public administrations. It has been updated to incorporate the DCAT-AP-ES
  metadata model, the Spanish adaptation of the European DCAT-AP metadata
  exchange scheme, aligned with DCAT-AP 2.1.1 and DCAT-AP-HVD 2.2.0 and with
  Directive (EU) 2019/1024 and Implementing Regulation (EU) 2023/138 on
  high-value datasets. The DCAT-AP-ES model is in administrative processing.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2013-01-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DCAT-AP
  - ES-ENI
  - ES-DATOS-GOB-ES
  - NL-DCAT-AP-NL
  - DE-DCAT-AP-DE
  - BE-DCAT-AP-BE
relationships:
  - type: derived-from
    target: ES-ENI
    source: fact
    evidence: "Real Decreto 4/2010, which regulates the Esquema Nacional de Interoperabilidad, establishes in its first additional provision the development of a series of Technical Interoperability Standards that are mandatory for public administrations, and those standards develop specific aspects of the matters needed to ensure the practical and operational aspects of interoperability between public administrations and with citizens (anabad.org 'Normas Técnicas de Interoperabilidad — Real Decreto 4/2010'; BOE-A-2010-1331). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-DCAT-AP
    source: fact
    evidence: "The NTI-RISP has been updated to incorporate the DCAT-AP-ES metadata model; DCAT-AP-ES is the Spanish adaptation of the European DCAT-AP metadata exchange scheme, adopts the guidelines of the European DCAT-AP schema and is aligned with the European profiles DCAT-AP 2.1.1 and DCAT-AP-HVD 2.2.0, promoting interoperability between national and European catalogues (datos.gob.es 'DCAT-AP y la Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información'; datos.gob.es 'DCAT-AP-ES: A step forward in open data interoperability'). CAVEAT: the same sources state the DCAT-AP-ES model is in administrative processing, so this descent may not yet be in force. NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "DCAT-AP y la Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información (NTI-RISP)"
    url: "https://datos.gob.es/es/conocimiento/dcat-ap-y-la-norma-tecnica-de-interoperabilidad-de-reutilizacion-de"
    publisher: "datos.gob.es"
  - title: "DCAT-AP-ES: A step forward in open data interoperability"
    url: "https://datos.gob.es/en/blog/dcat-ap-es-step-forward-open-data-interoperability"
    publisher: "datos.gob.es"
  - title: "Guide to migrating to DCAT-AP-ES"
    url: "https://datos.gob.es/en/conocimiento/guide-migrating-dcat-ap-es"
    publisher: "datos.gob.es"
  - title: "Guía de aplicación de la Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información"
    url: "https://datos.gob.es/es/documentacion/guia-de-aplicacion-de-la-norma-tecnica-de-interoperabilidad-de-reutilizacion-de"
    publisher: "datos.gob.es"
  - title: "Nuevo impulso a la interoperabilidad de los datos abiertos en España"
    url: "http://espanadigital.gob.es/en/actualidad/nuevo-impulso-la-interoperabilidad-de-los-datos-abiertos-en-espana"
    publisher: "España Digital 2026"
---

# NTI-RISP / DCAT-AP-ES

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The NTI-RISP is Spain's technical standard for selecting, identifying,
describing and publishing datasets for re-use. It has been **the regulatory
framework for opening public data in Spain since 2013**.

It is one of the **Normas Técnicas de Interoperabilidad** provided for by the
first additional provision of Real Decreto 4/2010 — see [[ES-ENI]] — and
those norms are **mandatory for public administrations**.

It has been updated to incorporate **DCAT-AP-ES**, the Spanish adaptation of
[[EU-DCAT-AP]], aligned with DCAT-AP 2.1.1 and DCAT-AP-HVD 2.2.0, and with
Directive (EU) 2019/1024 and Implementing Regulation (EU) 2023/138 on
high-value datasets.

## The DCAT chain now forks four ways

```
                       INTL-DCAT (W3C)
                             │ based-on
                             ▼
                      EU-DCAT-AP (SEMIC)
            ┌───────────┬────┴──────┬───────────┐
       based-on     based-on    based-on    based-on
            ▼           ▼           ▼           ▼
   NL-DCAT-AP-NL  DE-DCAT-AP-DE  BE-DCAT-AP-BE  ES-NTI-RISP
     (Geonovum)  (IT-Planungsrat)   (federal)   (mandatory NTI)
```

Batch 15 called the DCAT descent *"the template for what the UN layer
lacks"*. It is now a five-level structure branching across four countries,
with every layer above the national one recorded exactly once.

**Spain's branch is the odd one, and usefully so.** The other three national
profiles are profiles: documents that a portal network agrees to follow.
Spain's is a **norm with legal force**, issued under a royal decree and
mandatory for public administrations, into which a DCAT profile has been
placed as content.

So the four siblings are not four instances of one institutional pattern —
they are a foundation-custodied profile (Netherlands), a Bund–Länder
resolution (Germany), a federal profile (Belgium), and a binding technical
norm (Spain). That range is only visible because the Atlas keeps them as
four entities under one parent instead of collapsing them into a single
"national DCAT profile" concept.

**No relationships are asserted between the four siblings.** Their shared
parent is the relationship.

## Why the `based-on` edge is `confidence: low`

The descent from [[EU-DCAT-AP]] arrives through the DCAT-AP-ES update, and
the same sources that describe the alignment also say the DCAT-AP-ES model
is **in administrative processing**. The Atlas therefore records the edge —
the sources are clear that this is what the norm is being aligned to — at
low confidence and with `valid_from: null`, and states the caveat inside the
`evidence` string rather than only in this prose.

This is a different situation from [[ES-LCGC]], which is `status: proposed`
because the whole instrument is a draft. The NTI-RISP is in force; it is the
*European alignment* that is mid-flight. The entity is `active` and the
relationship is uncertain, which is exactly the split the provenance fields
exist to express.

## Relationships

- `derived-from` [[ES-ENI]].
- `based-on` [[EU-DCAT-AP]] — low confidence, see above.

## Sources

Listed in frontmatter — four datos.gob.es pages, including the migration
guide and the NTI-RISP application guide, plus the government announcement
of the update.
