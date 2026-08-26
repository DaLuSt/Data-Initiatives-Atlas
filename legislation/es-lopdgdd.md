---
id: ES-LOPDGDD
type: law
name: Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales
alternative_names:
  - LOPDGDD
  - Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales
  - Spanish Organic Law on Data Protection and the Guarantee of Digital Rights
description: >
  Spanish organic law of 5 December 2018 that adapts national law to the
  GDPR and guarantees digital rights for citizens. It entered into force on
  7 December 2018 and supplements the GDPR with national provisions,
  establishing a catalogue of digital rights, with the Agencia Española de
  Protección de Datos overseeing enforcement. It is structured in 97
  articles across ten titles, plus 22 additional, 6 transitory, one
  repealing and 16 final provisions, and adds a Title X on digital rights —
  including disconnection from work, digital wills and the right to erasure
  — that the previous data protection law did not contemplate.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2018-12-07
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - ES-AEPD
related_entities:
  - EU-GDPR
  - NL-UAVG
  - DE-BDSG
  - BE-GDPR-WET
  - FR-LIL
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading boe.es's own preamble text directly (2026-08-26, BOE-A-2018-16673): the law 'consta de noventa y siete artículos estructurados en diez títulos, veintidós disposiciones adicionales, seis disposiciones transitorias, una disposición derogatoria y dieciséis disposiciones finales' (97 articles across ten titles, 22 additional provisions, SIX transitory provisions — not seven, correcting this entity's prior figure — one repealing and 16 final provisions). finreg360.com, also read directly, confirms the 7 December 2018 entry into force and Title X's catalogue of digital rights, including network neutrality, universal access, the right to be forgotten and digital wills. The aepd.es PDF returned only garbled content; protecciondatos-lopd.com is bot-walled behind a loading challenge."
    confidence: high
    valid_from: 2018-12-07
    valid_until: null

sources:
  - title: "BOE-A-2018-16673 Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673"
    publisher: "Boletín Oficial del Estado (BOE)"
    accessed: "2026-08-26"
  - title: "Ley Orgánica 3/2018, de 5 de diciembre — novedades para el sector privado"
    url: "https://www.aepd.es/guias/novedades-lopd-sector-privado.pdf"
    publisher: "Agencia Española de Protección de Datos (AEPD)"
  - title: "Entra en vigor la Ley Orgánica de Protección de Datos Personales y Garantía de Derechos Digitales"
    url: "https://finreg360.com/alerta/entra-en-vigor-la-ley-organica-de-proteccion-de-datos-personales-y-garantia-de-derechos-digitales/"
    publisher: "Finreg360"
    accessed: "2026-08-26"
  - title: "Ley Orgánica de Protección de Datos — LOPDGDD 3/2018"
    url: "https://protecciondatos-lopd.com/empresas/nueva-ley-proteccion-datos-2018/"
    publisher: "Grupo Ático34"
---

# LOPDGDD — Ley Orgánica 3/2018

> **Verified 2026-08-26.** Two of four cited pages were read directly:
> BOE's own preamble text and Finreg360's commentary — a genuine majority,
> and enough to catch and correct one wrong figure this entity carried.
> The AEPD PDF returned only garbled content, and protecciondatos-lopd.com
> is bot-walled behind a loading challenge.

## Description

The LOPDGDD adapts Spanish law to [[EU-GDPR]] and guarantees digital rights
for citizens. It entered into force on **7 December 2018**, two days after
publication.

It runs to **97 articles across ten titles**, plus 22 additional, **six**
transitory, one repealing and 16 final provisions — confirmed by reading
boe.es's own preamble directly, which corrects this entity's previous
figure of seven transitory provisions. [[ES-AEPD]] enforces it.

## The GDPR technique table, fifth entry

| Country | Instrument | Technique |
|---|---|---|
| Netherlands | [[NL-UAVG]] | new implementing act |
| Germany | [[DE-BDSG]] | new act, replacing the earlier one |
| Belgium | [[BE-GDPR-WET]] | new act, repealing the 1992 privacy law |
| France | [[FR-LIL]] | **amended a 1978 act in place** |
| **Spain** | **LOPDGDD** | **new act — carrying subject matter beyond data protection** |

Spain passed a new act, like three of the four before it. What is different
is **what else the act contains**.

Its **Title X on digital rights** — disconnection from work, digital wills,
the right to erasure — has no counterpart in the GDPR and is not data
protection law in the ordinary sense. The Spanish instrument is a GDPR
implementation *and* a general digital-rights statute in one text.

The Atlas records a single `implements-requirement-from` edge to
[[EU-GDPR]], which is accurate for the part of the act that implements the
GDPR and silent about Title X. **Nothing is asserted about Title X's
relationship to anything**, because it does not descend from an EU
instrument in the Atlas; it descends from Spanish policy.

This is the clearest case so far of a real property the Atlas's
relationship model does not carry: **an instrument can implement an EU
requirement with part of itself.** The edge is whole-entity to
whole-entity. No partial-implementation type is proposed on one example.

## The organic-law rank is not modelled

`Ley Orgánica` is a distinct rank in the Spanish constitutional hierarchy,
requiring an absolute majority of the Congress to pass or amend, and
reserved for matters touching fundamental rights. An ordinary Spanish law —
[[ES-LEY-37-2007]], for instance — cannot amend it.

The Atlas has no field for the rank of an instrument within a national legal
hierarchy. `type: law` is what both get. The same flattening already applies
to a German *Gesetz* versus *Verordnung*, a Belgian *wet* versus *koninklijk
besluit*, and a French *loi* versus *ordonnance*, so this is not a Spanish
problem — Spain is simply the case where the distinction carries the most
weight, because the rank is what allows Title X to bind at all.

Logged in `discovery/unresolved.md`. **No field was added**: five countries
have now been modelled without one, and adding it would require re-reading
every instrument in the Atlas to populate it consistently.

## Relationships

- `implements-requirement-from` [[EU-GDPR]] — confirmed this pass via
  BOE's own preamble text and Finreg360's commentary; `confidence: high`.

## Sources

Listed in frontmatter, two of four read directly this pass: the BOE
consolidated text and Finreg360's commentary. The AEPD PDF returned only
garbled content and protecciondatos-lopd.com is bot-walled.
