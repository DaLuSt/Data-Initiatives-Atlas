---
id: ES-ENI
type: framework
name: Esquema Nacional de Interoperabilidad
alternative_names:
  - ENI
  - Spanish National Interoperability Framework
description: >
  Spanish national interoperability framework for electronic administration,
  regulated by Real Decreto 4/2010 of 8 January. Its purpose is to create
  the conditions needed to guarantee an adequate level of technical,
  semantic and organisational interoperability of the systems and
  applications used by public administrations, so that rights can be
  exercised and duties fulfilled through electronic access to public
  services. It covers organisational, semantic and technical
  interoperability, common infrastructures and services, communications,
  electronic signatures and document preservation, and its first additional
  provision provides for the development of Technical Interoperability
  Standards that are mandatory for public administrations.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2010-01-08
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - ES-NTI-RISP
  - ES-ENS
  - NL-PAS-TOE-OF-LEG-UIT
  - FR-RGI
  - BE-BELGIF
relationships:
  - type: applies-in
    target: ES
    source: fact
    evidence: "Confirmed by reading Real Decreto 4/2010's own text at boe.es directly (2026-08-26): its first additional provision mandates a catalogue of mandatory Technical Interoperability Standards covering electronic documents, electronic files, electronic signature policies, data intermediation, document preservation, network connectivity, authentication registers and information re-use — approved by the competent ministry through sectoral committees and published by official resolution. One of three cited sources read this pass (noticias.juridicas.com returned HTTP 503; anabad.org not attempted) — not enough alone for `verification: primary-source` under this Atlas's majority-read rule, though the one read is the decree's own primary text. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BOE-A-2010-1331 Real Decreto 4/2010, de 8 de enero, por el que se regula el Esquema Nacional de Interoperabilidad en el ámbito de la Administración Electrónica"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2010-1331"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "Normas Técnicas de Interoperabilidad — Real Decreto 4/2010, de 8 de enero"
    url: "https://www.anabad.org/normas-tecnicas-de-interoperabilidadreal-decreto-42010-de-8-de-enero/"
    publisher: "ANABAD"
  - title: "Real Decreto 4/2010, de 8 de enero, por el que se regula el Esquema Nacional de Interoperabilidad"
    url: "https://noticias.juridicas.com/base_datos/Admin/rd4-2010.html"
    publisher: "Noticias Jurídicas"
---

# ENI — Esquema Nacional de Interoperabilidad

> **Re-checked 2026-08-26, still `search-only`.** The decree's own text
> was read directly at boe.es and confirms the first-additional-provision
> claim. Only one of three cited sources was read this pass
> (`noticias.juridicas.com` returned a transient HTTP 503; `anabad.org`
> was not attempted), short of the majority this Atlas requires for
> `primary-source`.

## Description

The ENI is Spain's national interoperability framework for electronic
administration, regulated by **Real Decreto 4/2010 of 8 January**.

Its purpose is to create the conditions guaranteeing an adequate level of
**technical, semantic and organisational** interoperability of the systems
and applications used by public administrations. It covers common
infrastructures and services, communications, electronic signatures and
document preservation.

Its **first additional provision** provides for the development of **Normas
Técnicas de Interoperabilidad** — technical standards, **mandatory for
public administrations**, that develop the operational detail. [[ES-NTI-RISP]]
is one of them.

## Five national interoperability frameworks, five binding models

This is where the fifth country pays off. The Atlas now holds a national
interoperability instrument for every country it covers, and no two work the
same way:

| Country | Instrument | How it binds |
|---|---|---|
| Netherlands | [[NL-PAS-TOE-OF-LEG-UIT]] | **comply or explain** — a list, with a justification duty |
| Germany | (IT-Planungsrat resolutions) | **Bund–Länder political agreement** |
| Belgium | [[BE-BELGIF]] | **federal framework**, descending from [[EU-EIF]] |
| France | [[FR-RGI]] | **legal obligation** under an ordonnance |
| **Spain** | **ENI** | **royal decree, with mandatory implementing technical norms beneath it** |

Spain and France are both binding, but differently: France's RGI is an
obligation stated in an instrument, whereas Spain's ENI is a *framework
decree that delegates* to a layer of separately-issued mandatory technical
norms. That two-level structure — decree plus NTIs — has no counterpart in
the other four, and it is the reason [[ES-NTI-RISP]] can exist as its own
entity with its own descent from [[EU-DCAT-AP]].

The Atlas models both levels with existing types (`framework` and
`standard`) and an existing relationship (`derived-from`). Nothing was
added.

## No link to the European Interoperability Framework

**[[EU-EIF]] → ENI is not asserted**, and the refusal is deliberate.

A national interoperability framework descending from the EIF is exactly
what a reader would expect, and [[BE-BELGIF]] does carry that edge. But the
Atlas has now refused it three times — for Germany, for France
([[FR-RGI]]), and here — because **no source read says it**. [[FR-RGI]]
recorded that the refusal was made *precisely because* the surrounding
pattern made the link look expected.

The same reasoning applies unchanged. One country in five has a sourced EIF
descent. That is a statement about what has been read, not about European
interoperability policy, and the `verification: search-only` marking on all
of them is what keeps it readable as such.

## Not recorded

The relationship between the ENI and [[ES-ENS]] — the two schemes are
consistently presented together in Spanish practice — is not asserted. RD
4/2010 regulates one and RD 311/2022 the other; no source read establishes a
relationship between the instruments themselves.

The ENI's legal base is also not modelled. Sources state it was established
by article 42 of Ley 11/2007, an act since replaced by the 2015
administrative-procedure legislation; the chain from the current legal base
to this decree was not established well enough to record, and asserting the
repealed act as its parent would be worse than leaving the gap.

## Relationships

None asserted. [[ES-NTI-RISP]] carries the `derived-from` edge pointing
here, which is the direction that keeps the descent on the derived thing.

## Sources

Listed in frontmatter — the BOE consolidated text and two secondary
summaries of the decree and its technical standards.
