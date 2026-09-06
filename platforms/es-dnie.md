---
id: ES-DNIE
type: platform
name: Documento Nacional de Identidad electrónico
alternative_names:
  - DNIe
  - electronic National Identity Document
description: >
  Spain's electronic national identity card, issued by the Dirección
  General de la Policía (Ministry of the Interior) through the Cuerpo
  Nacional de Policía. It carries an integrated chip that stores identity
  data securely and enables electronic signature with legal validity
  equivalent to a handwritten one. Notified to the European Commission as
  Spain's eIDAS electronic identification scheme at the "High" assurance
  level, distinct from Cl@ve.

level: national
country: ES
region: EU

status: active
confidence: medium
coverage: low
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
  - ES-CLAVE
relationships:
  - type: applies-in
    target: ES
    source: fact
    evidence: "Confirmed by reading dnielectronico.es (the DNIe's own official portal) directly (2026-09-06): the document is 'emitido por la Dirección General de la Policía (Ministerio del Interior)' (issued by the Directorate-General of Police, Ministry of the Interior) and administered by the Cuerpo Nacional de Policía. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "CLOSES A GAP FLAGGED ON [[ES-CLAVE]]. Confirmed by reading the European Commission's own eID User Community page directly (2026-09-06), 'Overview of pre-notified and notified eID schemes under eIDAS' (ec.europa.eu/digital-building-blocks, maintained by the eID User Community, last updated 2 February 2026): its table lists 'The Kingdom of Spain' / 'Documento Nacional de Identidad electrónico (DNIe)' with assurance level 'High', eID means 'Spanish ID card (DNIe)', status 'NOTIFIED', notification date '07 Nov 2018', Official Journal reference 2018/C 401/08. The same table lists only this one Spanish entry — Cl@ve does not appear in it at all, corroborating [[ES-CLAVE]]'s own already-recorded finding (viafirma.com, read 2026-08-27) that Spain notified the DNIe, not Cl@ve, as its eIDAS-Node scheme. This is a formal notification under eIDAS's Article 9 mutual-recognition mechanism, not an inference from subject matter."
    confidence: high
    valid_from: 2018-11-07
    valid_until: null

sources:
  - title: "Portal del DNI electrónico"
    url: "https://www.dnielectronico.es/PortalDNIe/"
    publisher: "Cuerpo Nacional de Policía — Ministerio del Interior"
    accessed: "2026-09-06"
  - title: "¿Qué es el DNIe? — Portal del DNI electrónico"
    url: "https://www.dnielectronico.es/PortalDNIe/PRF1_Cons02.action?pag=REF_100"
    publisher: "Cuerpo Nacional de Policía — Ministerio del Interior"
    accessed: "2026-09-06"
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/EIDCOMMUNITY/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community, Digital Building Blocks"
    accessed: "2026-09-06"
---

# Documento Nacional de Identidad electrónico (DNIe)

> **Added 2026-09-06.** [[ES-CLAVE]]'s own entity had already found, via
> viafirma.com, that Spain notified the DNIe — not Cl@ve — as its eIDAS
> scheme, but left the DNIe unmodelled and the claim resting on a single
> vendor source. The European Commission's own eID User Community page,
> read directly this pass, both corroborates that finding independently
> and supplies a clean primary-source notification date, assurance
> level and Official Journal reference — enough to model the DNIe as its
> own entity and give it the edge [[ES-CLAVE]] could not sourcedly carry.

## Description

The DNIe is Spain's electronic national identity card, issued by the
**Dirección General de la Policía** (Ministry of the Interior) through
the **Cuerpo Nacional de Policía**. Confirmed by reading
dnielectronico.es directly: it carries "un pequeño circuito integrado
(chip), capaz de guardar de forma segura información y de procesarla
internamente" (a small integrated chip, able to securely store
information and process it internally), enabling an electronic
signature with "una validez jurídica equivalente a la que les
proporciona la firma manuscrita" (legal validity equivalent to a
handwritten signature). The same portal states that from 2 April 2026 a
**digital DNI on mobile** can be used for legal identification, and
both public and private entities are obliged to accept it.

## The eIDAS-notified scheme is the card, not Cl@ve

[[ES-CLAVE]]'s own entity records, at `confidence: low`, that Spain's
eIDAS node is associated with Cl@ve without any source stating the
technical relationship, and that viafirma.com names the DNIe as the
actual notified scheme. The European Commission's own notification
table, read directly here, settles it in the Commission's own words:
the table's **only Spanish entry** is "Documento Nacional de Identidad
electrónico (DNIe)," assurance level **High**, notified **7 November
2018**, Official Journal reference **2018/C 401/08**. Cl@ve does not
appear in the table at all. `implements-requirement-from` →
[[EU-EIDAS]] is recorded here at `confidence: high` — a direct
Commission notification — rather than on Cl@ve, which carries no such
edge in the Commission's own registry.

## Relationships

- `applies-in` [[ES]] — anchor edge.
- `implements-requirement-from` [[EU-EIDAS]], `confidence: high` — a
  direct Commission notification, 7 November 2018.

`related_entities` also carries [[ES-CLAVE]], Spain's separate
identification credential, which this entity's own notification status
corrects rather than supersedes.

## Sources

Listed in frontmatter, all three read directly this pass.
