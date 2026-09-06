---
id: PT-CMD
type: platform
name: Chave Móvel Digital
alternative_names:
  - CMD
  - Digital Mobile Key
description: >
  Portugal's mobile digital identification and signature scheme, certified
  by the Portuguese State. It associates a mobile phone number with a
  person's identification document, enabling two-factor authentication
  (a mobile app or SMS code plus a PIN) to public and private portals and
  digital document signing, without requiring a physical card reader.

level: national
country: PT
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PT-ARTE
related_entities:
  - EU-EIDAS
  - PT-ARTE
  - PT-CARTAO-CIDADAO
relationships:
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP ([[PT-AMA]]'s 'Not modelled' section). Confirmed by reading the European Commission's own eID User Community page directly (2026-09-06), 'Overview of pre-notified and notified eID schemes under eIDAS': its table lists Portugal's 'Chave Móvel Digital' with eID means 'Digital Mobile Key', assurance level 'High', status 'NOTIFIED', notification date '08 Apr 2020', Official Journal reference '2020/C 116/05'. A formal notification under eIDAS's Article 9 mutual-recognition mechanism, not an inference from subject matter."
    confidence: high
    valid_from: 2020-04-08
    valid_until: null
  - type: maintained-by
    target: PT-ARTE
    source: fact
    evidence: "Confirmed by reading autenticacao.gov.pt's own 'A Chave Móvel Digital' page directly (2026-09-06): the page's footer identifies ARTE — Agência para a Reforma Tecnológica do Estado — as the operator of the autenticacao.gov.pt portal through which CMD is delivered."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "A Chave Móvel Digital"
    url: "https://www.autenticacao.gov.pt/a-chave-movel-digital"
    publisher: "Autenticação.gov / ARTE"
    accessed: "2026-09-06"
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/EIDCOMMUNITY/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community"
    accessed: "2026-09-06"
---

# Chave Móvel Digital (CMD)

> **Created 2026-09-06**, closing part of a gap [[PT-AMA]]'s own entity
> flagged: "the Chave Móvel Digital... Portugal's digital identity means,
> which would be the [[EU-EIDAS]] counterpart[]." Sourced directly from
> autenticacao.gov.pt and the European Commission's own eID notification
> table.

## Description

Confirmed by reading autenticacao.gov.pt's own page directly: CMD is "um
meio de autenticação e assinatura digital certificado pelo Estado
português" — a means of authentication and digital signature certified by
the Portuguese State. It associates a mobile phone number with a person's
identification document, letting them authenticate to public and private
portals and sign documents digitally via a mobile app or SMS code plus a
PIN, without a physical smartcard reader — Portugal's mobile-first
counterpart to [[PT-CARTAO-CIDADAO]].

## Notified under eIDAS at High assurance

Confirmed by reading the European Commission's own eID User Community page
directly: Portugal's "Chave Móvel Digital" ("Digital Mobile Key") is
listed with assurance level "High," status "NOTIFIED," notification date
**08 Apr 2020**, Official Journal reference **2020/C 116/05**. The same
table lists [[PT-CARTAO-CIDADAO]] separately, notified earlier (28 Feb
2019) — Portugal runs two independently eIDAS-notified schemes, unlike
Spain, where only the DNIe card is notified and Cl@ve is not (see
[[ES-DNIE]]).

## Relationships

- `implements-requirement-from` [[EU-EIDAS]], valid from 8 April 2020.
- `maintained-by` [[PT-ARTE]].

## Sources

Listed in frontmatter, read directly 2026-09-06.
