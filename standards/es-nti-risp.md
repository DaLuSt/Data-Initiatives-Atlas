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
verification: primary-source

start_date: 2013-01-01
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading boe.es's own consolidated text of Real Decreto 4/2010 directly (2026-08-26, BOE-A-2010-1331): its first additional provision states the technical interoperability norms 'serán de obligado cumplimiento por parte de las Administraciones Públicas' (will be mandatory for compliance by Public Administrations), listing roughly twenty such norms including the one behind the NTI-RISP. anabad.org was not re-read this pass."
    confidence: high
    valid_from: null
    valid_until: null
  - type: based-on
    target: EU-DCAT-AP
    source: fact
    evidence: "Confirmed by reading datos.gob.es's own blog post and migration guide directly (2026-08-26): 'the future new version of the NTI-RISP incorporates DCAT-AP-ES as a reference model'; DCAT-AP-ES aligns with DCAT-AP 2.1.1, the DCAT-AP-HVD 2.2.0 extension, Directive (EU) 2019/1024 on open data and re-use of public sector information, and Implementing Regulation (EU) 2023/138 establishing the list of High-Value Datasets — all four citations confirmed directly in the migration guide's own text, more precisely than the previous search-only evidence. CAVEAT unchanged: the same pages state DCAT-AP-ES remains in administrative processing, and 'application will be mandatory once the modification text of the standard comes into force' — so this descent is not yet in force."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Real Decreto 4/2010, de 8 de enero, por el que se regula el Esquema Nacional de Interoperabilidad en el ámbito de la Administración Electrónica"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2010-1331"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "DCAT-AP y la Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información (NTI-RISP)"
    url: "https://datos.gob.es/es/conocimiento/dcat-ap-y-la-norma-tecnica-de-interoperabilidad-de-reutilizacion-de"
    publisher: "datos.gob.es"
  - title: "DCAT-AP-ES: A step forward in open data interoperability"
    url: "https://datos.gob.es/en/blog/dcat-ap-es-step-forward-open-data-interoperability"
    publisher: "datos.gob.es"
    accessed: "2026-08-26"
  - title: "Guide to migrating to DCAT-AP-ES"
    url: "https://datos.gob.es/en/conocimiento/guide-migrating-dcat-ap-es"
    publisher: "datos.gob.es"
    accessed: "2026-08-26"
  - title: "Guía de aplicación de la Norma Técnica de Interoperabilidad de Reutilización de Recursos de Información"
    url: "https://datos.gob.es/es/documentacion/guia-de-aplicacion-de-la-norma-tecnica-de-interoperabilidad-de-reutilizacion-de"
    publisher: "datos.gob.es"
  - title: "Nuevo impulso a la interoperabilidad de los datos abiertos en España"
    url: "http://espanadigital.gob.es/en/actualidad/nuevo-impulso-la-interoperabilidad-de-los-datos-abiertos-en-espana"
    publisher: "España Digital 2026"
---

# NTI-RISP / DCAT-AP-ES

> **Verified 2026-08-26.** Three of six cited pages were read directly:
> BOE's own consolidated text of Real Decreto 4/2010, datos.gob.es's blog
> post, and its DCAT-AP-ES migration guide — the last of which supplied
> direct citations for both European legal instruments this entity names.

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

- `derived-from` [[ES-ENI]] — confirmed this pass via BOE's own text of
  Real Decreto 4/2010; `confidence: high`.
- `based-on` [[EU-DCAT-AP]] — `confidence: low`, unchanged: the
  administrative-processing caveat still stands, see above.

## Sources

Listed in frontmatter, three of six read directly this pass: BOE's own
text of Real Decreto 4/2010 (newly added as a proper citation, previously
only named in evidence text), the datos.gob.es blog post, and the
migration guide. The application guide and the España Digital 2026
announcement were not re-fetched.
