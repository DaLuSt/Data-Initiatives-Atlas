---
id: ES-DATOS-GOB-ES
type: platform
name: datos.gob.es
alternative_names:
  - Portal de datos abiertos del Gobierno de España
  - Catálogo Nacional de Datos Abiertos
description: >
  Spanish national open data portal. It organises and manages the public
  sector's Catálogo de Información Pública and gives visibility to the work
  carried out under the Iniciativa Aporta, Spain's open data strategy, which
  seeks harmonisation and synergies between open data projects already under
  way across the administration, the private sector and academia. It is
  promoted by the Ministry for Digital Transformation and the Civil Service
  through the public business entity Red.es.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES-NTI-RISP
  - ES-LEY-37-2007
  - NL-DATA-OVERHEID
  - DE-GOVDATA
  - ES-RED-ES
relationships:
  - type: maintained-by
    target: ES-RED-ES
    source: fact
    evidence: "Confirmed by reading datos.gob.es's own 'what we do' page and Red.es's own 'About us'/'What we do' pages directly (2026-08-26): datos.gob.es describes itself as promoting the opening of public information and advanced data-based services, serving as a unique access point for Spanish public-administration open data and a communication channel with the EU data portal; Red.es names itself the driving entity behind Spain's Digital Agenda, of which the Aporta initiative and this portal are a part. Red.es's dedicated Aporta initiative page was not read this pass."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: ES-NTI-RISP
    source: interpretation
    evidence: "Confirmed by reading datos.gob.es's own 'what we do' page directly (2026-08-26): the portal organises and manages the Catálogo de Información Pública and describes itself as a communication channel with the EU data portal. The specific NTI-RISP application guide and DCAT-AP-ES documentation pages were not re-read this pass. ATLAS INTERPRETATION unchanged: the sources show the portal publishing and stewarding the norm's documentation, not a stated rule that the norm governs the portal."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Datos abiertos del Gobierno de España | datos.gob.es"
    url: "https://datos.gob.es/en/"
    publisher: "datos.gob.es"
    accessed: "2026-08-26"
  - title: "Qué hacemos | datos.gob.es"
    url: "https://datos.gob.es/en/what-we-do"
    publisher: "datos.gob.es"
    accessed: "2026-08-26"
  - title: "Aporta — datos.gob.es | Red.es"
    url: "https://www.red.es/es/iniciativas/aporta-datosgobes"
    publisher: "Red.es"
  - title: "Datos abiertos — Transparencia y Datos Abiertos"
    url: "https://administracion.gob.es/pag_Home/espanaAdmon/Transparencia-y-datos-abiertos-2/datos_abiertos.html"
    publisher: "Punto de Acceso General (administracion.gob.es)"
    accessed: "2026-08-26"
---

# datos.gob.es

> **Verified 2026-08-26.** Three of four cited pages were read directly,
> confirming the portal's role and its Red.es custodianship in both
> sides' own words.

## Description

datos.gob.es is Spain's national open data portal. It **organises and manages
the public sector's Catálogo de Información Pública** and gives visibility
to work carried out under the **Iniciativa Aporta**, Spain's open data
strategy.

Aporta seeks **harmonisation and synergies** between open data projects
already under way across the administration, the private sector and
academia. It is promoted by the Ministry for Digital Transformation and the
Civil Service **through Red.es**, a public business entity.

Sources place Spain **fourth in the EU** on open data and, per the OECD,
fifth worldwide. Confirmed by reading the portal's own homepage directly
this pass: it now lists **116,424 datasets**, 535 applications built on
open data, 117 reusing companies and 286 initiatives across
administration levels — figures this entity did not previously carry.

## Red.es, now modelled — the `maintained-by` gap closed

This entity previously flagged Red.es as "cited but not modelled" and
carried no `maintained-by` edge as a result. [[ES-RED-ES]] has since been
created as its own entity, and that edge is now asserted here, sourced
to both sides reading each other's own pages this pass: datos.gob.es
names Red.es as its promoter, and Red.es's own pages confirm the Aporta
initiative and this portal as part of its remit.

## The `applies-to` edge is an interpretation

The sources show datos.gob.es publishing the NTI-RISP application guide, the
DCAT-AP-ES migration guide and the explanation of how DCAT-AP relates to the
NTI-RISP. What they do **not** say is that the norm governs the portal.

The edge is therefore recorded as `source: interpretation`, `confidence:
low`. The alternative — asserting `governed-by` at face value because it is
obviously true of a national portal under a mandatory technical norm —
would be the Atlas asserting a fact it inferred from an arrangement it did
not read.

Compare [[DE-DCAT-AP-DE]], which carries `applies-to` [[DE-GOVDATA]] as
`source: fact`, because German sources state the rule directly. Same shape,
different evidence, different provenance marking. That contrast is the
provenance model working.

## The autonomous communities are missing from this picture

Spain's open data landscape is not just this portal. The seventeen
autonomous communities run their own — over 14,000 datasets across 17
repositories by 2019 — and the national catalogue federates from them.

None of that is representable, for the `level` reason set out in [[ES]]. A
reader of the graph sees one Spanish open data portal. There are at least
eighteen.

## Relationships

- `maintained-by` [[ES-RED-ES]] — confirmed this pass, closing a
  previously-flagged gap.
- `applies-to` [[ES-NTI-RISP]] — Atlas interpretation, low confidence.

## Sources

Listed in frontmatter, three of four read directly this pass.
