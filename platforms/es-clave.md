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
  - EU-EIDAS
  - EU-EIDAS2
  - FR-FRANCECONNECT
  - DE-BUNDID
relationships:
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "Cl@ve 2.0 is the main Spanish eGovernment solution used by local, regional and national public electronic services to authenticate citizens, and includes the eIDAS node service; the Spanish eIDAS node facilitates cross-border identification both for Spanish citizens accessing services in other European countries and for citizens of other European countries accessing Spanish public services (eidas.redsara.es; cef.uv.es eID4Spain2020 'Scope and objectives'; viafirma.com 'The eIDAS Regulation in Spain'). NOT READ — search-only. CAVEAT: the sources establish that Cl@ve incorporates the eIDAS node; they indicate the notified electronic identification MEANS for Spain is the DNIe rather than Cl@ve itself, so this edge covers the eIDAS infrastructure role and not a notification of Cl@ve as a scheme."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Cl@ve — Sistema Cl@ve: qué es y cómo funciona"
    url: "https://clave.gob.es/en"
    publisher: "Cl@ve — Gobierno de España"
  - title: "Identificación Electrónica — Trámites y Servicios Electrónicos"
    url: "https://administracion.gob.es/pag_Home/Tramites/Identificacion-electronica.html"
    publisher: "Punto de Acceso General (administracion.gob.es)"
  - title: "Identidad digital en las AA.PP. — Ciudadanos"
    url: "https://firmaelectronica.gob.es/en/ciudadanos/cosas-deberias-saber/identidad-digital-aapp"
    publisher: "Portal de Firma Electrónica — Gobierno de España"
  - title: "Información general sobre el sistema de identificación Cl@ve"
    url: "https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/informacion-general-sobre-sistema-identificacion-pin.html"
    publisher: "Agencia Tributaria"
---

# Cl@ve

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Cl@ve is Spain's **common electronic identification system** for citizens
dealing with public administrations, and is described as the most widespread
such system in Spanish public administrations.

It works on **agreed keys** — username and password — with **prior
registration** that must guarantee the person's identity, completed either
remotely or in person at an office performing registration functions.

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
confidence, because a German source mentions the regulation. Nothing
equivalent is asserted here: **no source read about Cl@ve mentions eIDAS,
cross-border recognition, or acceptance of other member states' eIDs** —
even though a national identification scheme is precisely what eIDAS
governs.

Nor is anything asserted to [[EU-EIDAS2]], which requires every member state
to offer a European Digital Identity Wallet by the end of 2026 — now about
four months away.

[[FR-FRANCECONNECT]] predicted this would *"become a factual question rather
than a modelling one"*. With a fifth country added and the deadline four
months out, one of five national identity systems in the Atlas carries an
eIDAS edge, and none carries an eIDAS2 edge. The prediction stands, and the
question is now overdue rather than approaching.

## Why `coverage: low`

Cl@ve's operator, its legal basis, the relationship between Cl@ve PIN and
Cl@ve Permanente, its user numbers, and the status of any Spanish digital
identity wallet are all unrecorded. Two of the four sources cited are tax
agency and signature-portal help pages rather than descriptions of the
system's governance.

## Relationships

None asserted — see above.

## Sources

Listed in frontmatter.
