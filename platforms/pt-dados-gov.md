---
id: PT-DADOS-GOV
type: platform
name: dados.gov.pt
alternative_names:
  - dados.gov
  - Portal de Dados Abertos
  - Portuguese open data portal
description: >
  Portugal's national open data portal, publishing datasets from Portuguese
  public bodies, maintained by the Agência para a Reforma Tecnológica do
  Estado (ARTE) and running on the open-source udata platform.

level: national
country: PT
region: EU

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
  - PT
  - PT-ARTE
  - EU-OPEN-DATA-DIRECTIVE
  - PT-LEI-26-2016
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "Confirmed by reading dados.gov.pt's own homepage directly (2026-08-26): 'Aceda, explore e reutilize dados públicos de forma transparente e acessível' (Access, explore and reuse public data transparently and accessibly), footer-credited to 'República Portuguesa'. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: PT-ARTE
    source: fact
    evidence: "Confirmed by reading dados.gov.pt's own homepage directly (2026-08-26): the footer names the 'Agência para a Reforma Tecnológica do Estado' alongside 'República Portuguesa'. This closes the custodian gap this entity previously flagged ('the fifth portal without a custodian') — see [[PT-ARTE]], created in 2025 by restructuring [[PT-AMA]], the body previously suspected but unsourced as the operator."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: interpretation
    evidence: "dados.gov.pt is Portugal's national open data portal; [[PT-LEI-26-2016]]'s third amendment is the instrument that transposes the Open Data Directive into Portuguese law, read directly this pass (mosaico.gov.pt names dados.gov as the platform this framework operates through). This entity is the technical implementation the legal transposition applies to, rather than itself being an instrument that implements the Directive — recorded as `interpretation` rather than `fact` for that reason."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "dados.gov.pt — Portal de Dados Abertos"
    url: "https://dados.gov.pt/"
    publisher: "Governo de Portugal"
    accessed: "2026-08-26"
  - title: "Dados.GOV"
    url: "https://mosaico.gov.pt/plataformas-comuns/dados-gov"
    publisher: "Mosaico / Governo de Portugal"
    accessed: "2026-08-26"
---

# dados.gov.pt

> **Verified 2026-08-26.** Both cited pages were read directly. The
> portal's own footer names its custodian — closing a gap this entity
> had flagged since its creation — and dados.gov.pt turns out to be more
> than a single portal: it aggregates and indexes sectoral and local open
> data catalogues too.

## Description

dados.gov.pt is Portugal's national open data catalogue: a central hub
that hosts open datasets directly and also indexes sectoral (health,
justice, environment) and local data portals. Confirmed by reading its
own homepage directly: "qualquer utilizador pode, em nome próprio ou em
representação de uma organização, criar uma conta e carregar dados" (any
user may, personally or on behalf of an organisation, create an account
and upload data) under open licences — it is a publishing platform, not
only a read-only listing.

## The custodian gap, closed via AMA's successor

This entity previously flagged itself as "the fifth portal without a
custodian" — [[PT-AMA]] was the obvious operator and no source read said
so. dados.gov.pt's own homepage footer, read directly this pass, credits
the **Agência para a Reforma Tecnológica do Estado** — [[PT-ARTE]],
created in August 2025 by restructuring [[PT-AMA]]. AMA's successor is
this portal's sourced custodian.

## Portugal's Open Data Directive transposition — identified, weakly linked

[[PT-LEI-26-2016]], the LADA, whose **third amendment** approved general
principles on open data and transposed the Directive, is the transposing
instrument — confirmed by mosaico.gov.pt naming dados.gov as the platform
this legal framework operates through. The edge is recorded at
`confidence: low` and `source: interpretation`: the law transposes the
Directive into Portuguese law, but nothing read states that this
*portal specifically* is what implements the Directive's requirements,
only that it is the platform the framework runs on.

Portugal did not pass a standalone open data act. It folded open data into
the statute that already governed **access to administrative and
environmental information** — one act where Germany has three.

## Relationships

- `part-of` [[PT]] — anchor edge.
- `maintained-by` [[PT-ARTE]] — confirmed this pass.
- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]] —
  `confidence: low`, `source: interpretation`, via [[PT-LEI-26-2016]].

## Sources

Listed in frontmatter.
