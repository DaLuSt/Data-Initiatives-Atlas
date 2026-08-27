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
  - EU-EDPB
  - ES-LOPDGDD
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Confirmed by reading gdpr-info.eu's own text of Article 68(3) GDPR directly (2026-08-26): 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.' The AEPD is Spain's supervisory authority. `gdprhub.eu` was not read this pass."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: ES-LOPDGDD
    source: fact
    evidence: "Confirmed by reading boe.es's own text of Ley Orgánica 3/2018 directly (2026-08-26, BOE-A-2018-16673) and aepd.es's own press note on a modification to the law: the note describes new corrective powers, including 'el apercibimiento como una medida adecuada, de naturaleza no sancionadora, incluida dentro de los poderes correctivos' (a formal warning as an appropriate, non-sanctioning measure within the corrective powers), and expanded discretion for the Agency to create standardised, mandatory complaint procedures. The 'Novedades LOPD sector privado' PDF was attempted but returned only encoded, unreadable content."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-26"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
  - title: "Ley Orgánica 3/2018, de 5 de diciembre — novedades para el sector privado"
    url: "https://www.aepd.es/guias/novedades-lopd-sector-privado.pdf"
    publisher: "Agencia Española de Protección de Datos (AEPD)"
  - title: "Modificación de la Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales"
    url: "https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/modificacion-ley-organica-proteccion-datos-personales-y-garantia-derechos-digitales"
    publisher: "Agencia Española de Protección de Datos (AEPD)"
    accessed: "2026-08-26"
  - title: "BOE-A-2018-16673 Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
---

# AEPD — Agencia Española de Protección de Datos

> **Verified 2026-08-26.** Three of five cited pages were read directly:
> gdpr-info.eu's own text of Article 68(3) GDPR, boe.es's own consolidated
> text of Ley Orgánica 3/2018, and AEPD's own press note on a subsequent
> modification of that law. The "Novedades LOPD sector privado" PDF
> returned only garbled, unreadable content when fetched, and `gdprhub.eu`
> was not read this pass.

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

Confirmed by reading AEPD's own press note directly (2026-08-26): a
modification of the 2018 organic law gave the Agency the **apercibimiento**
(formal warning) as a new corrective, non-sanctioning measure, and expanded
its discretion to create standardised, mandatory complaint procedures —
detail this entity did not previously carry.

`coverage: medium`: its composition, appointment process, sanctioning
record and its relationship with the autonomous communities' own data
protection authorities remain unrecorded. Several autonomous communities
operate regional data protection authorities; none is representable, for
the reason set out in [[ES]].

## Five national DPAs, all five now on the record

| Country | Authority | `participates-in` [[EU-EDPB]]? |
|---|---|---|
| Netherlands | [[NL-AP]] | **yes** — sourced |
| Germany | [[DE-BFDI]] | **yes** — sourced (2026-08-22) |
| Belgium | [[BE-APD]] | **yes** — sourced |
| France | [[FR-CNIL]] | **yes** — sourced |
| Spain | **AEPD** | **yes** — sourced |

Confirmed by reading gdpr-info.eu's own text of Article 68(3) GDPR
directly: the Board "shall be composed of the head of one supervisory
authority of each Member State ... or their respective representatives" —
a general legal fact rather than a country-specific announcement, but a
direct textual basis all the same. The same one-article reasoning closed
this edge on all five national DPAs now in the Atlas, across four
separate re-verification passes. What began as "the Atlas's clearest
single example of a sourcing artefact masquerading as structure" is now
fully closed.

## Relationships

- `participates-in` [[EU-EDPB]] — confirmed this pass via Article 68(3)
  GDPR's own text; `confidence: medium`.
- `applies-to` [[ES-LOPDGDD]] — confirmed this pass via BOE's consolidated
  text and AEPD's own press note on a later modification; `confidence:
  medium`.

## Sources

Listed in frontmatter, three of five read directly this pass; the
"Novedades LOPD sector privado" PDF returned only garbled content and
`gdprhub.eu` was not read.
