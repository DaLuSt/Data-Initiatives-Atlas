---
id: ES-AEPD
type: organisation
name: Agencia Española de Protección de Datos
alternative_names:
  - AEPD
  - Spanish Data Protection Agency
description: >
  Spanish data protection supervisory authority, responsible for overseeing
  compliance with the GDPR and with Ley Orgánica 3/2018. It is configured as
  an independent administrative authority under the 2015 law on the legal
  regime of the public sector, and relates to the Government through the
  Ministry of Justice. It publishes guidance for controllers and for the
  private sector on the obligations introduced by the 2018 organic law.

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
organisations: []
related_entities:
  - EU-EDPB
  - ES-LOPDGDD
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Article 68(3) GDPR provides that the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives; the Agencia Española de Protección de Datos is Spain's supervisory authority (gdpr-info.eu 'Art. 68 GDPR — European Data Protection Board'; gdprhub.eu 'Article 68 GDPR'; edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: ES-LOPDGDD
    source: fact
    evidence: "Organic Law 3/2018 supplements the EU GDPR with national provisions and establishes a catalogue of digital rights, with the Agencia Española de Protección de Datos overseeing enforcement; the AEPD publishes and maintains guidance on the changes the LOPDGDD introduces for the private sector, and announces modifications to the law (aepd.es 'Novedades LOPD sector privado'; aepd.es press note on the modification of the LOPDGDD). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
  - title: "Ley Orgánica 3/2018, de 5 de diciembre — novedades para el sector privado"
    url: "https://www.aepd.es/guias/novedades-lopd-sector-privado.pdf"
    publisher: "Agencia Española de Protección de Datos (AEPD)"
  - title: "Modificación de la Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales"
    url: "https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/modificacion-ley-organica-proteccion-datos-personales-y-garantia-derechos-digitales"
    publisher: "Agencia Española de Protección de Datos (AEPD)"
  - title: "BOE-A-2018-16673 Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"
    publisher: "Boletín Oficial del Estado (BOE)"
---

# AEPD — Agencia Española de Protección de Datos

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The AEPD is Spain's data protection supervisory authority. It oversees
compliance with [[EU-GDPR]] and [[ES-LOPDGDD]], and publishes guidance for
controllers — including a dedicated guide to what the 2018 organic law
changed for the private sector.

Institutionally it is an **independent administrative authority** under the
2015 law on the legal regime of the public sector, relating to the
Government **through the Ministry of Justice** rather than through the
digital-transformation ministry that most other entities in this batch sit
under.

`coverage: low`: its composition, appointment process, sanctioning record
and its relationship with the autonomous communities' own data protection
authorities are not recorded. Several autonomous communities operate
regional data protection authorities; none is representable, for the reason
set out in [[ES]].

## Five national DPAs, one European link

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — sourced |
| Germany | [[DE-BFDI]] | no — refused |
| Belgium | [[BE-APD]] | no — refused |
| France | [[FR-CNIL]] | no — refused |
| Spain | **AEPD** | no — refused |

The count moves from four to five and the sourced-link count stays at one.

[[FR-CNIL]] described this as *"the Atlas's clearest single example of a
sourcing artefact masquerading as structure"*. A fifth instance does not
make it clearer — it makes it **more expensive to leave open**. A reader
taking the graph at face value would now conclude that the European Data
Protection Board has one member out of five modelled candidates, all of
which certainly sit on it.

Nothing has been asserted to close it, because no source read for the
Spanish, French, Belgian or German authority mentions the EDPB. Five page
reads would fix four edges. It is logged in `discovery/unresolved.md` and
remains among the cheapest items in the re-verification pass.

## Relationships

- `applies-to` [[ES-LOPDGDD]].

## Sources

Listed in frontmatter — two AEPD publications and the BOE consolidated text
of the law it enforces.
