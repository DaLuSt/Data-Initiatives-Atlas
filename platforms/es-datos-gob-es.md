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
verification: search-only

start_date: null
end_date: null
last_verified: null
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
relationships:
  - type: applies-to
    target: ES-NTI-RISP
    source: interpretation
    evidence: "datos.gob.es organises and manages the Catálogo de Información Pública of the public sector, and publishes the NTI-RISP application guide, the DCAT-AP-ES migration guide and the explanation of how DCAT-AP relates to the NTI-RISP on its own knowledge pages (datos.gob.es 'Qué hacemos'; datos.gob.es NTI-RISP and DCAT-AP-ES documentation). ATLAS INTERPRETATION: the sources show the portal publishing and stewarding the norm's documentation, not a stated rule that the norm governs the portal. NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Datos abiertos del Gobierno de España | datos.gob.es"
    url: "https://datos.gob.es/en/"
    publisher: "datos.gob.es"
  - title: "Qué hacemos | datos.gob.es"
    url: "https://datos.gob.es/en/what-we-do"
    publisher: "datos.gob.es"
  - title: "Aporta — datos.gob.es | Red.es"
    url: "https://www.red.es/es/iniciativas/aporta-datosgobes"
    publisher: "Red.es"
  - title: "Datos abiertos — Transparencia y Datos Abiertos"
    url: "https://administracion.gob.es/pag_Home/espanaAdmon/Transparencia-y-datos-abiertos-2/datos_abiertos.html"
    publisher: "Punto de Acceso General (administracion.gob.es)"
---

# datos.gob.es

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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
fifth worldwide.

## Red.es is cited but not modelled

The portal's operator, **Red.es**, is named in the sources and is not an
entity in the Atlas. Creating it from a single mention of its role as the
promoting body would produce an organisation node whose entire content is
"it promotes this portal" — the kind of thin node the taxonomy's threshold
rule exists to prevent.

The consequence is recorded rather than papered over: **this platform has no
`maintained-by` edge**, unlike [[NL-DATA-OVERHEID]] and [[DE-GOVDATA]].
Red.es is queued in `discovery/research-queue.md`.

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

- `applies-to` [[ES-NTI-RISP]] — Atlas interpretation, low confidence.

## Sources

Listed in frontmatter — the portal's own pages, the Red.es initiative page,
and the government's open data hub.
