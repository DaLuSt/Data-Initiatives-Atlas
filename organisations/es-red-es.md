---
id: ES-RED-ES
type: organisation
name: Entidad Pública Empresarial Red.es, M.P.
alternative_names:
  - Red.es
  - red.es
description: >
  Spanish public business entity (entidad pública empresarial) attached to
  the Ministry for Digital Transformation and the Civil Service through the
  State Secretariat for Digitalisation and Artificial Intelligence. It
  executes and deploys national digitalisation plans, designs and operates
  digital public services, and acts as a connector between ministries,
  public bodies, autonomous communities, local entities and international
  organisations. Alongside datos.gob.es it operates the ONTSI observatory,
  holds the national authority for ".es" domain name registration, and
  manages RedIRIS, the advanced communications network for Spanish
  universities and public research centres.

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
  - ES
  - ES-DATOS-GOB-ES
  - ES-AEAD
  - ES-ESPANA-DIGITAL-2026
relationships:
  - type: part-of
    target: ES
    source: fact
    evidence: "Confirmed by reading administracion.gob.es's own ficha de unidad orgánica directly (2026-08-26): Red.es is attached to 'Ministerio para la Transformación Digital y de la Función Pública' through the 'Secretaria de Estado de Digitalización e Inteligencia Artificial', organic unit code EA0044367-v4. red.es's own 'About us' and 'What we do' pages, also read directly, confirm Red.es as 'la entidad impulsora de la Agenda Digital en España' (the driving entity behind Spain's Digital Agenda) and its connector role between ministries, public bodies, autonomous communities, local entities and international organisations."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "About us | Red.es"
    url: "https://www.red.es/en/about-us/about-us"
    publisher: "Entidad Pública Empresarial Red.es, M.P."
    accessed: "2026-08-26"
  - title: "What we do | Red.es"
    url: "https://www.red.es/en/about-us/what-we-do"
    publisher: "Entidad Pública Empresarial Red.es, M.P."
    accessed: "2026-08-26"
  - title: "Aporta - datos.gob.es | Red.es"
    url: "https://www.red.es/es/iniciativas/aporta-datosgobes"
    publisher: "Entidad Pública Empresarial Red.es, M.P."
  - title: "Entidad Pública Empresarial Red.Es — ficha de unidad orgánica"
    url: "https://administracion.gob.es/pagFront/espanaAdmon/directorioOrganigrama/fichaUnidadOrganica.htm?codigoUnidad=EA0044367"
    publisher: "Punto de Acceso General (administracion.gob.es)"
    accessed: "2026-08-26"
  - title: "Organigrama del Ministerio para la Transformación Digital y de la Función Pública"
    url: "https://transparencia.gob.es/content/dam/transparencia_home/publicidadactiva/organizacionyempleo/03estructura/legislaturaxv/mtdf/MTDF_LXV.pdf"
    publisher: "Portal de la Transparencia — Gobierno de España"
---

# Red.es

> **Verified 2026-08-26.** Three of five cited pages were read directly,
> confirming Red.es's legal attachment and connector role in its own and
> the government's words.

## Description

The Spanish public business entity through which the Ministry for Digital
Transformation and the Civil Service operates [[ES-DATOS-GOB-ES]], the
national open data portal, under the **Iniciativa Aporta**.

## Why this entity exists

`discovery/research-queue.md` recorded, from the Spain batch:

> *"**Red.es** — public business entity operating [[ES-DATOS-GOB-ES]]. Cited
> but too thinly sourced to create, which is why that portal is the only
> national open data portal in the Atlas besides the Dutch one with no
> `maintained-by` edge."*

The portal entity's own `description` has said all along that it "is
promoted by the Ministry for Digital Transformation and the Civil Service
**through the public business entity Red.es**". The fact was in the Atlas;
what was missing was a node to hang it on.

## Not a ministry, not an agency

`entidad pública empresarial` is a specific Spanish legal form — a public
body operating under private law for its ordinary activity while remaining
attached to a ministry. Red.es is attached to the Ministry for Digital
Transformation and the Civil Service through the **Secretaría de Estado de
Digitalización e Inteligencia Artificial**.

The Atlas's `type` vocabulary flattens this to `organisation`, the same
value carried by [[ES-AEAD]] (a state agency) and [[ES-INE]] (an autonomous
body). Only this paragraph records that the three are different creatures
under Spanish administrative law.

## More than the portal

Red.es is not a data body that happens to run other things. Its remit spans:

- **datos.gob.es** and the Iniciativa Aporta
- **ONTSI** — the national observatory of technology and society
- the **`.es` domain registry** — national naming authority
- **RedIRIS** — the research and education network for Spanish universities
  and public research centres

Three of those four are unmodelled. RedIRIS in particular is the Spanish
counterpart of [[NL-SURF]], and its absence is now a named gap rather than
an unnoticed one.

## Relationships

- `part-of` [[ES]] (anchor edge, and a factual attachment: Red.es is a
  public body of the Spanish state).
- [[ES-DATOS-GOB-ES]] carries the `maintained-by` edge to this entity.

## Sources

Listed in frontmatter, three of five read directly this pass.
