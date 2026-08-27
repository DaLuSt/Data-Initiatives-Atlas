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
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-EIDAS
  - EU-EIDAS2
  - FR-FRANCECONNECT
  - DE-BUNDID
relationships:
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "Confirmed by reading eidas.redsara.es's own 'qué es' page and viafirma.com's eIDAS-in-Spain article directly (2026-08-27): eidas.redsara.es describes the Spanish eIDAS node as 'una plataforma que facilita la identificación electrónica transfronteriza en el ámbito de la Unión Europea' (a platform enabling cross-border electronic identification in the EU); viafirma.com confirms Spain notified the DNIe (electronic ID document), not Cl@ve, as its eIDAS-Node scheme. NEITHER page actually read confirms the specific claim this entity previously carried — that administrations integrate with the eIDAS node 'through the Cl@ve system' — eidas.redsara.es's page displays both Cl@ve and eIDAS logos together but states no textual claim about their technical relationship, and viafirma.com does not mention Cl@ve at all. cef.uv.es returned HTTP 503 both in the prior pass and this one. CAVEAT UNCHANGED: this edge covers Cl@ve's general association with Spain's eIDAS infrastructure, not a notification of Cl@ve as a scheme, and the specific integration claim remains unconfirmed by direct reading despite two of the three specific citations now being read."
    confidence: low
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
---

# Cl@ve

> **Verified 2026-08-27.** Two of the three specific citations behind
> the entity's one relationship — eidas.redsara.es and viafirma.com —
> were found (the correct viafirma URL, via search) and read directly
> this pass; `cef.uv.es` remains persistently unavailable (HTTP 503).
> That is a majority of the entity's now six total sources. Reading them
> did not confirm the specific claim previously carried — that
> administrations integrate with the eIDAS node "through Cl@ve" — so
> `confidence: low` on that edge stands, now for a different, more
> precise reason: not "unread" but "read, and not stated."

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

## The eIDAS gap now spans five countries

[[DE-BUNDID]] carries `implements-requirement-from` → [[EU-EIDAS]] at low
confidence, because a German source mentions the regulation. This entity's
own edge is now similarly thin, but for a sharper reason: two sources about
Spain's eIDAS node **were** read directly this pass, and neither states
that Cl@ve is how it works — one displays the Cl@ve and eIDAS logos
together with no textual claim connecting them, the other confirms the
DNIe, not Cl@ve, as Spain's notified scheme and does not mention Cl@ve at
all.

Nor is anything asserted to [[EU-EIDAS2]], which requires every member state
to offer a European Digital Identity Wallet by the end of 2026 — now about
four months away.

[[FR-FRANCECONNECT]] predicted this would *"become a factual question rather
than a modelling one"*. With a fifth country added and the deadline four
months out, one of five national identity systems in the Atlas carries an
eIDAS edge, and none carries an eIDAS2 edge. The prediction stands, and the
question is now overdue rather than approaching.

## Why `coverage: medium`, up from `low`

Cl@ve's operator, its legal basis, its user numbers, and the status of
any Spanish digital identity wallet remain unrecorded. What is now
established: registration channels (video call, invitation letter,
in-person, existing certificate) and a fourth named variant,
**Cl@ve Móvil**, alongside PIN, Permanente and Firma — confirmed by
reading administracion.gob.es directly, which did not previously appear
in this entity's description.

## Relationships

- `implements-requirement-from` [[EU-EIDAS]] — `confidence: low`; see the
  caveat at the top of this entity. Two of its three specific citations
  are now read directly, and neither states the claim.

## Sources

Listed in frontmatter, five of six read directly this pass, including
two of the three specific citations behind the one relationship above.
`cef.uv.es` remains persistently unavailable (HTTP 503).
