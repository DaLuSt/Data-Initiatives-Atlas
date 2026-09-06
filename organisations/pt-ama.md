---
id: PT-AMA
type: organisation
name: Agência para a Modernização Administrativa
alternative_names:
  - AMA
  - AMA, I.P.
  - Administrative Modernisation Agency
description: >
  Former Portuguese public institute within the indirect administration of
  the State, with a mission to develop, coordinate and evaluate measures,
  programmes and projects in administrative and regulatory modernisation and
  simplification, electronic administration and the distribution of public
  services. Restructured in August 2025 into the Agência para a Reforma
  Tecnológica do Estado (ARTE), which now uses AMA's former domain.

level: national
country: PT
region: EU

status: superseded
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: 2025-08-22
last_verified: "2026-08-26"
previous_version: null
successor: PT-ARTE

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PT
  - PT-DADOS-GOV
  - PT-ARTE
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "The Agência para a Modernização Administrativa, I.P. was a public institute integrated into the indirect administration of the State, with a mission to develop, coordinate and evaluate measures, programmes and projects in administrative and regulatory modernisation and simplification, electronic administration and the distribution of public services (eportugal.gov.pt 'Agência para a Modernização Administrativa', historical). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Agência para a Modernização Administrativa (historical — page now redirects)"
    url: "https://eportugal.gov.pt/entidades/agencia-para-a-modernizacao-administrativa"
    publisher: "ePortugal / Governo de Portugal"
    accessed: "2026-08-26"
  - title: "AMA passa a chamar-se Agência para a Reforma Tecnológica do Estado"
    url: "https://eco.sapo.pt/2025/08/21/ama-passa-chamar-se-agencia-para-a-reforma-tecnologica-do-estado/"
    publisher: "ECO / Grupo Impresa"
    accessed: "2026-08-26"
  - title: "Agência para a Reforma Tecnológica do Estado, IP"
    url: "https://www.gov.pt/entidades/agencia-para-a-reforma-tecnologica-do-estado-ip"
    publisher: "Governo de Portugal"
    accessed: "2026-08-26"
---

# Agência para a Modernização Administrativa (AMA)

> **Superseded — re-verified 2026-08-26.** AMA no longer exists under
> this name: `ama.gov.pt` now redirects (via a loop) to `arte.gov.pt`.
> gov.pt's own entity registry and independent Portuguese trade press
> (ECO), both read directly, confirm AMA was restructured into
> [[PT-ARTE]] by decree-law n.º 96/2025, in force from 22 August 2025.
> `status: superseded`, `successor: PT-ARTE`, promoted to
> `verification: primary-source` on the strength of that confirmation.

## Description

AMA **was** a **public institute within the indirect administration of the
State** — a Portuguese administrative form with no exact counterpart
elsewhere in the Atlas, sitting between a ministry department and an
independent agency. It no longer exists under this name; see [[PT-ARTE]].

Its mission spans four things that other countries usually separate:
administrative **and regulatory** modernisation and simplification,
**electronic administration**, and the **distribution of public services**.

## Regulatory simplification is the unusual half

Every country in the Atlas has a body doing e-government and service
delivery. AMA's remit also covers **regulatory** simplification — reducing
the burden of rules themselves, not only of the processes implementing them.

[[GB-GDS]], [[NO-DIGDIR]] and [[FR-DINUM]] are the closest comparators on
the digital side and none of their Atlas entities records a regulatory
mandate. Whether that reflects Portuguese practice or the Atlas's sourcing
is not established.

## The `maintained-by` edge to [[PT-DADOS-GOV]], closed on the successor

AMA was widely understood to run Portugal's open data portal, but no
source read while AMA still existed stated it. dados.gov.pt's own
homepage footer, read directly this pass, credits ARTE by name — so the
`maintained-by` edge is now sourced and lives on [[PT-DADOS-GOV]],
pointing to [[PT-ARTE]], not to this (superseded) entity.

## Not modelled

- **ePortugal**, the citizen services portal AMA operated.
- The **iAP**, Portugal's public administration interoperability platform.

**Closed 2026-09-06**: Portugal's digital identity means are now modelled
as [[PT-CMD]] (Chave Móvel Digital) and [[PT-CARTAO-CIDADAO]] (Cartão de
Cidadão), both `implements-requirement-from` [[EU-EIDAS]] at High
assurance and `maintained-by` [[PT-ARTE]], sourced directly from the
European Commission's own eID notification table.

## Relationships

- `part-of` [[PT]] — anchor edge.
- `successor`: [[PT-ARTE]].

## Sources

Listed in frontmatter. The ePortugal page is kept for historical record
even though it now redirects; ECO's report and gov.pt's own ARTE entry
were read directly this pass and are what justify `primary-source`.
