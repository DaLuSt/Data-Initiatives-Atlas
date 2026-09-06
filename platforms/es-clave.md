---
id: ES-CLAVE
type: platform
name: Cl@ve
alternative_names:
  - Cl@ve PIN
  - Cl@ve Permanente
  - Cl@ve Firma
description: >
  Spanish common electronic identification system, allowing citizens to
  authenticate securely in their dealings with public administrations. It is
  described as the most widespread such system in Spanish public
  administrations. Agreed-key systems are based on a username and password
  and require prior registration that guarantees the person's identity;
  registration can be completed remotely or in person at offices performing
  registration functions for the platform. Cl@ve identifies but does not
  sign; a separate Cl@ve Firma allows document signing and is available for
  a small number of procedures.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - ES
  - EU-EIDAS
  - EU-EIDAS2
  - FR-FRANCECONNECT
  - DE-BUNDID
  - ES-DNIE
relationships:
  - type: applies-in
    target: ES
    source: fact
    evidence: "Confirmed by reading administracion.gob.es directly (2026-08-27): 'El sistema más extendido en las Administraciones Públicas es Cl@ve' (the most widespread system in Spanish public administrations is Cl@ve). Anchor edge under metadata/relationship-types.md §2.3, added 2026-09-06 to replace the removed implements-requirement-from edge to EU-EIDAS — see 'The eIDAS edge is removed, not weakened' below."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Cl@ve — Sistema Cl@ve: qué es y cómo funciona"
    url: "https://clave.gob.es/en"
    publisher: "Cl@ve — Gobierno de España"
    accessed: "2026-08-27"
  - title: "Identificación Electrónica — Trámites y Servicios Electrónicos"
    url: "https://administracion.gob.es/pag_Home/Tramites/Identificacion-electronica.html"
    publisher: "Punto de Acceso General (administracion.gob.es)"
    accessed: "2026-08-27"
  - title: "Identidad digital en las AA.PP. — Ciudadanos"
    url: "https://firmaelectronica.gob.es/en/ciudadanos/cosas-deberias-saber/identidad-digital-aapp"
    publisher: "Portal de Firma Electrónica — Gobierno de España"
    accessed: "2026-08-27"
  - title: "Información general sobre el sistema de identificación Cl@ve"
    url: "https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/informacion-general-sobre-sistema-identificacion-pin.html"
    publisher: "Agencia Tributaria"
  - title: "¿Que es eIDAS? — Red SARA"
    url: "https://eidas.redsara.es/EidasHome/queEs.jsp"
    publisher: "Red SARA"
    accessed: "2026-08-27"
  - title: "The eIDAS Regulation in Spain"
    url: "https://www.viafirma.com/en/eidas-spain/"
    publisher: "Viafirma"
    accessed: "2026-08-27"
  - title: "eID4Spain2020 — Scope and objectives (currently HTTP 503)"
    url: "https://cef.uv.es/eid4spain2020/"
    publisher: "Universitat de València"
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/EIDCOMMUNITY/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community, Digital Building Blocks"
    accessed: "2026-09-06"
---

# Cl@ve

> **Verified 2026-08-27.** Two of the three specific citations behind
> the entity's one relationship — eidas.redsara.es and viafirma.com —
> were found (the correct viafirma URL, via search) and read directly
> this pass; `cef.uv.es` remains persistently unavailable (HTTP 503).
> That is a majority of the entity's now six total sources. Reading them
> did not confirm the specific claim previously carried — that
> administrations integrate with the eIDAS node "through Cl@ve" — so
> `confidence: low` on that edge stood, at the time, for a different,
> more precise reason: not "unread" but "read, and not stated."
>
> **Updated 2026-09-06: the eIDAS edge is removed, not weakened.** The
> European Commission's own eID notification table, read directly,
> settles the question this entity had left open — Spain's eIDAS-notified
> scheme is the DNIe, now its own entity, [[ES-DNIE]], and Cl@ve does not
> appear in the Commission's table at all. See "The eIDAS edge is
> removed, not weakened" below.

## Description

Cl@ve is Spain's **common electronic identification system** for citizens
dealing with public administrations, confirmed by reading
administracion.gob.es directly: "El sistema más extendido en las
Administraciones Públicas es Cl@ve" (the most widespread system in
Spanish public administrations).

It works on **agreed keys** — username and password — with **prior
registration** that must guarantee the person's identity. Confirmed by
reading clave.gob.es directly, registration can be completed via **video
call, invitation letter, in person, or with an existing electronic
certificate** — more specific than "remotely or in person," this
entity's previous description.

**Cl@ve identifies; it does not sign.** A separate **Cl@ve Firma** allows
document signing, and the sources say it can be used in only a small number
of procedures at present. For signing generally, an electronic certificate
or the electronic DNI is used, and a certificate-based signature has the
same validity as a handwritten one.

## Three countries, three national identity architectures

The Atlas now holds three national digital identity systems, and the third
does not fit the axis the first two defined:

| | Spain | France | Germany |
|---|---|---|---|
| Entity | **Cl@ve** | [[FR-FRANCECONNECT]] | [[DE-BUNDID]] |
| Model | **agreed keys issued by the state**, plus certificates and the electronic DNI | identity **federation** — reuse an existing account | a **central citizen account** |
| Providers | the state | multiple, including private | the state |
| Signing | **separate** — Cl@ve Firma, few procedures | — | — |

[[FR-FRANCECONNECT]] recorded France and Germany as *"opposite means to the
same goal"* — brokering versus issuing. Spain does neither: it operates a
**credential scheme** alongside a certificate infrastructure, and treats
identification and signature as **separate problems with separate systems**.

That separation is the distinctive part. Neither the French nor the German
entity records signature capability as a distinct question at all.

**No relationship between the three is asserted.** Three national solutions
to a shared problem is still not a relationship.

## The eIDAS edge is removed, not weakened

The prior pass left `implements-requirement-from` → [[EU-EIDAS]] on this
entity at `confidence: low`, with two sources read directly that neither
confirmed nor denied the specific claim. The European Commission's own
eID User Community page, read directly this pass (2026-09-06),
'Overview of pre-notified and notified eID schemes under eIDAS'
(ec.europa.eu/digital-building-blocks), settles it: its **only Spanish
entry** is "Documento Nacional de Identidad electrónico (DNIe)," at
assurance level **High**, notified **7 November 2018** (OJEU 2018/C
401/08). **Cl@ve does not appear in the table at all.**

That is no longer "read, and not stated" — it is read, and stated
otherwise. The edge is removed from this entity rather than kept at a
still-lower confidence, and recorded instead on a new entity,
[[ES-DNIE]], which carries it at `confidence: high`. This is the same
call [[FR-LOI-VALTER]] makes for France's Open Data Directive question:
a documented negative is the finding, not a gap to keep flagging at
diminishing confidence.

Nor is anything asserted to [[EU-EIDAS2]] or [[EU-EUDI-WALLET]], which
require every member state to offer a European Digital Identity Wallet
by the end of 2026 — a separate, still-unsourced obligation.

## Why `coverage: medium`, up from `low`

Cl@ve's operator, its legal basis, its user numbers, and the status of
any Spanish digital identity wallet remain unrecorded. What is now
established: registration channels (video call, invitation letter,
in-person, existing certificate) and a fourth named variant,
**Cl@ve Móvil**, alongside PIN, Permanente and Firma — confirmed by
reading administracion.gob.es directly, which did not previously appear
in this entity's description.

## Relationships

- `applies-in` [[ES]] — anchor edge, added 2026-09-06 to replace the
  removed `implements-requirement-from` edge.

No relationship to [[EU-EIDAS]] is asserted — see "The eIDAS edge is
removed, not weakened" above.

## Sources

Listed in frontmatter. Five of the original six were read directly in
the 2026-08-27 pass; `cef.uv.es` remains persistently unavailable (HTTP
503). The European Commission's own eID notification table was read
directly in the 2026-09-06 pass.
