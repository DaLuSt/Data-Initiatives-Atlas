---
id: PT-ARTE
type: organisation
name: Agência para a Reforma Tecnológica do Estado
alternative_names:
  - ARTE
  - ARTE, I.P.
  - Agency for the Technological Reform of the State
description: >
  Portuguese public institute responsible for directing, coordinating and
  executing the State's technological transformation and digitalisation
  strategy, created in August 2025 by restructuring the Agência para a
  Modernização Administrativa (AMA), which ceased to exist under that name.

level: national
country: PT
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2025-08-22
end_date: null
last_verified: "2026-08-26"
previous_version: PT-AMA
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PT
  - PT-AMA
  - PT-DADOS-GOV
  - PT-CMD
  - PT-CARTAO-CIDADAO
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "Confirmed by reading gov.pt's own entity page for ARTE directly (2026-08-26): 'A ARTE foi criada em 2025, no âmbito da reestruturação da Agência para a Modernização Administrativa (AMA)' (ARTE was created in 2025, as part of the restructuring of the Agência para a Modernização Administrativa). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Agência para a Reforma Tecnológica do Estado, IP"
    url: "https://www.gov.pt/entidades/agencia-para-a-reforma-tecnologica-do-estado-ip"
    publisher: "Governo de Portugal"
    accessed: "2026-08-26"
  - title: "ARTE — Agência para a Reforma Tecnológica do Estado"
    url: "https://www.arte.gov.pt/"
    publisher: "Agência para a Reforma Tecnológica do Estado (ARTE)"
    accessed: "2026-08-26"
  - title: "AMA passa a chamar-se Agência para a Reforma Tecnológica do Estado"
    url: "https://eco.sapo.pt/2025/08/21/ama-passa-chamar-se-agencia-para-a-reforma-tecnologica-do-estado/"
    publisher: "ECO / Grupo Impresa"
    accessed: "2026-08-26"
---

# Agência para a Reforma Tecnológica do Estado (ARTE)

> **Verified 2026-08-26.** All three cited pages were read directly. This
> is a newly created entity: [[PT-AMA]]'s own domain (`ama.gov.pt`) now
> redirects to `arte.gov.pt`, and both gov.pt's own entity registry and
> independent Portuguese trade press confirm ARTE is AMA's successor
> rather than a new, unrelated body.

## Description

ARTE is Portugal's public institute for directing, coordinating and
executing the State's technological transformation and digitalisation
strategy, created by restructuring [[PT-AMA]]. Confirmed by reading
eco.sapo.pt directly: the restructuring was enacted by decree-law
n.º 96/2025, published in the Diário da República on 21 August 2025 and
in force from **22 August 2025**, the day after publication.

## AMA did not add a new entity — it changed name

This entity exists because [[PT-AMA]], read again this pass for the
France/Portugal/Poland/Spain/Belgium re-verification push, turned out to
no longer exist under that name: `ama.gov.pt` now redirects (via a loop)
to `arte.gov.pt`. gov.pt's own entity page for ARTE states directly that
it "foi criada em 2025, no âmbito da reestruturação da Agência para a
Modernização Administrativa (AMA)" (was created in 2025, as part of the
restructuring of AMA) — confirmed independently by ECO's report naming
the decree-law. [[PT-AMA]] is recorded as `status: superseded` with this
entity as its `successor`, following the same pattern as
[[NL-WOB]]/[[NL-WOO]].

## The custodian gap on dados.gov.pt, closed

[[PT-DADOS-GOV]] previously flagged itself as "the fifth portal without a
custodian" — [[PT-AMA]] was the obvious operator but no source read said
so. dados.gov.pt's own homepage footer, read directly this pass, credits
ARTE by name — AMA's successor is the custodian AMA itself was never
sourced as having.

## Digital identity, added 2026-09-06

ARTE also operates Portugal's two eIDAS-notified digital identity means,
via the autenticacao.gov.pt portal: [[PT-CMD]] (Chave Móvel Digital) and
[[PT-CARTAO-CIDADAO]] (Cartão de Cidadão). Both closed a gap [[PT-AMA]]'s
own entity had flagged as unmodelled.

## Relationships

- `part-of` [[PT]] — anchor edge.
- Operates [[PT-DADOS-GOV]], [[PT-CMD]] and [[PT-CARTAO-CIDADAO]] — the
  `maintained-by` edges live on those entities, pointing here.

## Sources

Listed in frontmatter, all three read directly this pass.
