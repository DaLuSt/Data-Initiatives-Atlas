---
id: PT-IAP
type: platform
name: Plataforma de Interoperabilidade da Administração Pública
alternative_names:
  - iAP
  - iAP — Interoperabilidade da AP
description: >
  Portugal's reference technological infrastructure for exchanging
  information between public services and bodies, operating since 2007
  and offering four independent services — Integration, Messages,
  Payments and Authentication. Its use as the preferred means of
  interoperability across the public administration was made mandatory
  by Resolution of the Council of Ministers 42/2015, later reinforced by
  Decree-Law 49/2024. Operated by the Agência para a Reforma Tecnológica
  do Estado.

level: national
country: PT
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - PT-ARTE
related_entities:
  - PT
  - PT-ARTE
  - PT-AMA
  - PT-GOV-PT
  - EU-EIF
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP ([[PT-AMA]]'s own 'Not modelled' section: 'the iAP, Portugal's public administration interoperability platform'). Confirmed by reading digital.gov.pt's own article directly (2026-09-13): the iAP is described as 'a infraestrutura tecnológica de referência para a troca de informação entre serviços e organismos públicos em Portugal' (the reference technological infrastructure for exchanging information between public services and bodies in Portugal), with over 6.3 billion interactions processed and 124 entities integrated. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: PT-ARTE
    source: fact
    evidence: "Confirmed by reading iap.gov.pt's own 'Sobre a iAP' page directly (2026-09-13): the portal's footer branding and organisational affiliation identify ARTE — Agência para a Reforma Tecnológica do Estado — as the operator. Independently corroborated by digital.gov.pt's own article, read directly, naming the same legal basis (Resolução do Conselho de Ministros 42/2015 and Decreto-Lei 49/2024) that gov.pt's own 'Sobre' page cites for [[PT-GOV-PT]], another ARTE-operated portal."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Sobre a iAP"
    url: "https://www.iap.gov.pt/web/iap/sobre-a-iap"
    publisher: "iAP / Agência para a Reforma Tecnológica do Estado"
    accessed: "2026-09-13"
  - title: "iAP: a plataforma de interoperabilidade que liga a Administração Pública portuguesa"
    url: "https://digital.gov.pt/pt/noticias/iap-a-plataforma-de-interoperabilidade-que-liga-a-administracao-publica-portuguesa"
    publisher: "Digital.gov.pt"
    accessed: "2026-09-13"
---

# Plataforma de Interoperabilidade da Administração Pública (iAP)

> **Created 2026-09-13**, closing part of [[PT-AMA]]'s own flagged gap —
> "the iAP, Portugal's public administration interoperability platform."
> `iap.gov.pt`'s own page and a `digital.gov.pt` ministry article were
> both read directly.

## Description

Confirmed by reading digital.gov.pt's own article directly: the iAP is
**"a infraestrutura tecnológica de referência para a troca de informação
entre serviços e organismos públicos"** (the reference technological
infrastructure for exchanging information between public services and
bodies) in Portugal, offering four independent services: **Integration**,
**Messages**, **Payments** and **Authentication**.

## Scale, confirmed directly

The same article, read directly, gives the platform's own reported
figures: operating **since 2007**, it has processed **over 6.3 billion
interactions**, integrates **124 entities**, and is credited with
estimated savings of **€21.5 billion** — including enabling Portugal's
Social Energy Tariff programme to expand from 100,000 to 800,000 families
through automated data verification. `start_date` is left `null`: the
bare year 2007 is confirmed, but no source read gives a specific day or
month.

## Mandatory by resolution, then by decree-law

Confirmed by reading digital.gov.pt's own article directly: the iAP's use
as the **preferred means of interoperability** across the public
administration was established by **Resolução do Conselho de Ministros
n.º 42/2015**, and more recently reinforced by **Decreto-Lei n.º
49/2024** — the same decree-law that establishes the rules for digital
service delivery through [[PT-GOV-PT]], gov.pt's aggregating portal.

## Operated by ARTE, alongside gov.pt

Confirmed by reading iap.gov.pt's own page directly: **ARTE** —
[[PT-ARTE]] — is identified via the portal's footer branding and
organisational affiliation as its operator, the same body responsible
for [[PT-GOV-PT]], [[PT-DADOS-GOV]], [[PT-CMD]] and [[PT-CARTAO-CIDADAO]].

## Not modelled

- **Resolução do Conselho de Ministros n.º 42/2015** and **Decreto-Lei
  n.º 49/2024** as legislation entities — named here in prose only.
- A sourced relationship to [[EU-EIF]] (the European Interoperability
  Framework) — no source read this pass states one; the resemblance in
  subject matter is not evidence of a stated connection, matching the
  Atlas's treatment of every other national interoperability framework
  refused an unsourced [[EU-EIF]] edge (Germany's, France's, Spain's —
  see `discovery/unresolved.md` rows #71, #84).
- The **Interoperabilidade Documental** service, launched June 2025
  alongside a new institutional portal — named by the digital.gov.pt
  article but not independently detailed this pass.

## Relationships

- `part-of` [[PT]] — anchor edge.
- `maintained-by` [[PT-ARTE]].

## Sources

Listed in frontmatter, both read directly 2026-09-13.
