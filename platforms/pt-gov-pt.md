---
id: PT-GOV-PT
type: platform
name: gov.pt
alternative_names:
  - Portal gov.pt
description: >
  Portugal's single aggregating portal for public services, launched in
  October 2024 to replace ePortugal, itself the successor (since 2019) to
  the earlier Portal do Cidadão. Provides information on more than 2,500
  public services for citizens and businesses, online access to digital
  services, and a Reserved Area for tracking submitted requests. Operated
  by the Agência para a Reforma Tecnológica do Estado.

level: national
country: PT
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2024-10-01
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
  - PT-IAP
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP ([[PT-AMA]]'s own 'Not modelled' section: 'ePortugal, the citizen services portal AMA operated'). Confirmed by reading gov.pt's own 'Sobre' (About) page directly (2026-09-13): the portal provides 'informações sobre mais de 2.500 serviços públicos para cidadãos e empresas' (information on more than 2,500 public services for citizens and businesses). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: PT-ARTE
    source: fact
    evidence: "Confirmed by reading gov.pt's own 'Sobre' page directly (2026-09-13): 'A Agência para a Reforma Tecnológica do Estado, IP (ARTE) é responsável por desenvolver, gerir e manter o portal' (the Agência para a Reforma Tecnológica do Estado is responsible for developing, managing and maintaining the portal), coordinating with public administration entities to gather, edit and publish service content."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Sobre — gov.pt"
    url: "https://www.gov.pt/sobre"
    publisher: "Governo de Portugal / ARTE"
    accessed: "2026-09-13"
  - title: "Já viu o novo portal gov.pt? ePortugal.gov.pt acabou"
    url: "https://pplware.sapo.pt/internet/ja-viu-o-novo-portal-gov-pt-eportugal-gov-pt-acabou/"
    publisher: "Pplware"
    accessed: "2026-09-13"
---

# gov.pt

> **Created 2026-09-13**, closing part of [[PT-AMA]]'s own flagged gap —
> "ePortugal, the citizen services portal AMA operated" was not modelled
> because the portal itself no longer exists under that name. `gov.pt`'s
> own "Sobre" page and independent Portuguese tech press were both read
> directly.

## Description

Confirmed by reading gov.pt's own "Sobre" page directly: gov.pt is
Portugal's **single aggregating portal for public services**, providing
information on **more than 2,500 public services** for citizens and
businesses, online access to digital services, location information,
practical guides, and a **Reserved Area** for tracking submitted
requests.

## ePortugal did not add a new entity — like AMA, it changed name

The page states directly: "**O gov.pt veio substituir o ePortugal**, como
o portal agregador dos serviços públicos em Portugal" (gov.pt replaced
ePortugal as the aggregating portal for public services in Portugal).
Independent Portuguese tech press (Pplware), read directly, corroborates
the same transition, dating it to **early October 2024**. `eportugal.gov.pt`
itself now redirects to `gov.pt` — the same domain-collapse pattern
already recorded for [[PT-AMA]] → [[PT-ARTE]].

ePortugal was itself, per the same page, the successor (since 2019) to an
earlier "Portal do Cidadão" — a second layer of lineage, recorded here in
prose only. Neither ePortugal nor the Portal do Cidadão is modelled as its
own entity: both are superseded portals with no further sourced content
of their own, the same treatment the Atlas gives other renamed-not-split
predecessors (e.g. [[NL-TNO-WET]]'s 1930 act).

## Operated by ARTE, under the same decree-law as iAP

Confirmed directly: **ARTE** — [[PT-ARTE]], the same body created in 2025
by restructuring [[PT-AMA]] — "é responsável por desenvolver, gerir e
manter o portal" (is responsible for developing, managing and maintaining
the portal). The page cites **Decree-Laws 73/2014 and 74/2014**, and more
recently **Decree-Law 49/2024**, which establishes rules for digital
service delivery through a centralised omnichannel system — the same
Decree-Law 49/2024 that governs [[PT-IAP]], Portugal's interoperability
platform, also operated by ARTE.

## Not modelled

- **Decree-Laws 73/2014, 74/2014 and 49/2024** themselves, as legislation
  entities — named here in prose only.
- **ePortugal** and the earlier **Portal do Cidadão**, both superseded
  and carrying no sourced content beyond the lineage recorded above.

## Relationships

- `part-of` [[PT]] — anchor edge.
- `maintained-by` [[PT-ARTE]].

## Sources

Listed in frontmatter, both read directly 2026-09-13.
