---
id: PT-CARTAO-CIDADAO
type: platform
name: Cartão de Cidadão
alternative_names:
  - CC
  - Citizen Card
  - Portuguese Citizen Card
description: >
  Portugal's national multi-purpose smart identity card, doubling as a
  digital identification, authentication and electronic-signature means.
  Card-based authentication requires a smartcard reader and a PIN code,
  and works through public and private portals that have adopted the
  Autenticação.gov service.

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
  - PT-CMD
relationships:
  - type: implements-requirement-from
    target: EU-EIDAS
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP ([[PT-AMA]]'s 'Not modelled' section). Confirmed by reading the European Commission's own eID User Community page directly (2026-09-06), 'Overview of pre-notified and notified eID schemes under eIDAS': its table lists Portugal's 'Cartão de Cidadão' with eID means 'Portuguese national identity card (eID card)', assurance level 'High', status 'NOTIFIED', notification date '28 Feb 2019', Official Journal reference '2019/C 75/04'. A formal notification under eIDAS's Article 9 mutual-recognition mechanism, not an inference from subject matter."
    confidence: high
    valid_from: 2019-02-28
    valid_until: null
  - type: maintained-by
    target: PT-ARTE
    source: fact
    evidence: "Confirmed by reading autenticacao.gov.pt's own 'Autenticação com Cartão de Cidadão' page directly (2026-09-06): the page's footer identifies ARTE — Agência para a Reforma Tecnológica do Estado — as the operator of the autenticacao.gov.pt portal through which Cartão de Cidadão authentication is delivered."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Autenticação com Cartão de Cidadão"
    url: "https://www.autenticacao.gov.pt/cartao-cidadao/autenticacao"
    publisher: "Autenticação.gov / ARTE"
    accessed: "2026-09-06"
  - title: "Overview of pre-notified and notified eID schemes under eIDAS"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/EIDCOMMUNITY/Overview+of+pre-notified+and+notified+eID+schemes+under+eIDAS"
    publisher: "European Commission — eID User Community"
    accessed: "2026-09-06"
---

# Cartão de Cidadão (CC)

> **Created 2026-09-06**, closing part of a gap [[PT-AMA]]'s own entity
> flagged: "the... Cartão de Cidadão, Portugal's digital identity means,
> which would be the [[EU-EIDAS]] counterpart[]." Sourced directly from
> autenticacao.gov.pt and the European Commission's own eID notification
> table.

## Description

Confirmed by reading autenticacao.gov.pt's own page directly: "A
autenticação com Cartão de Cidadão permite-lhe fazer login, realizar
serviços e registar-se de forma segura em diferentes portais públicos ou
privados" — authentication with the Citizen Card lets users securely log
in, use services and register on public or private portals that have
adopted the Autenticação.gov service. Card-based authentication requires a
smartcard reader and the card's own authentication PIN.

## Notified under eIDAS at High assurance

Confirmed by reading the European Commission's own eID User Community page
directly: Portugal's "Cartão de Cidadão" is listed with eID means
"Portuguese national identity card (eID card)," assurance level "High,"
status "NOTIFIED," notification date **28 Feb 2019**, Official Journal
reference **2019/C 75/04** — Portugal's earlier and card-based
eIDAS-notified scheme, alongside the later, mobile-based [[PT-CMD]].

## Relationships

- `implements-requirement-from` [[EU-EIDAS]], valid from 28 February 2019.
- `maintained-by` [[PT-ARTE]].

## Sources

Listed in frontmatter, read directly 2026-09-06.
