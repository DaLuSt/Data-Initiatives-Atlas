---
id: PT-CNCS
type: organisation
name: Centro Nacional de Cibersegurança
alternative_names:
  - CNCS
  - Portuguese National Cybersecurity Centre
description: >
  Portugal's national cybersecurity centre and the supervisory authority for
  cybersecurity regulation in Portugal.

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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - PT
  - PT-DECRETO-LEI-125-2025
  - EU-NIS2
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "Confirmed by reading the Diário da República's own gazette index directly (2026-08-26, files.dre.pt, Série I, n.º 234, 4 December 2025): Decreto-Lei n.º 125/2025's own summary describes it as reinforcing CNCS's role, and independent press (RTP, read directly) states the decree-law establishes CNCS as 'a autoridade nacional de cibersegurança' (the national cybersecurity authority). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading RTP's report directly (2026-08-26): [[PT-DECRETO-LEI-125-2025]], Portugal's NIS2 transposition, 'reinforces CNCS's role as the national cybersecurity authority while establishing sectoral and specialised supervisory bodies.' This is CNCS's own transposing instrument, previously unidentified for this entity — see [[PT-DECRETO-LEI-125-2025]] for the full account."
    confidence: medium
    valid_from: 2026-04-03
    valid_until: null

sources:
  - title: "Diário da República, 1.ª série, n.º 234, 4 de dezembro de 2025"
    url: "https://files.dre.pt/gratuitos/1s/2025/12/23400.pdf"
    publisher: "Diário da República / Imprensa Nacional-Casa da Moeda"
    accessed: "2026-08-26"
  - title: "Regime que reforça Centro Nacional de Cibersegurança publicado em Diário da República"
    url: "https://www.rtp.pt/noticias/economia/regime-que-reforca-centro-nacional-de-ciberseguranca-publicado-em-diario-da-republica_n1702457"
    publisher: "RTP (Rádio e Televisão de Portugal)"
    accessed: "2026-08-26"
  - title: "CNCS — Centro Nacional de Cibersegurança (currently unreachable)"
    url: "https://www.cncs.gov.pt/"
    publisher: "Centro Nacional de Cibersegurança (CNCS)"
---

# Centro Nacional de Cibersegurança

> **Verified 2026-08-26.** The Diário da República's own gazette index
> and an independent press report (RTP) were read directly. Portugal's
> NIS2 transposition — flagged as unidentified when this entity was
> created — is now identified: [[PT-DECRETO-LEI-125-2025]], in force
> since 3 April 2026.

## Description

CNCS is Portugal's national cybersecurity centre and, confirmed this
pass, its statutory **national cybersecurity authority** under
[[PT-DECRETO-LEI-125-2025]].

## Portugal's NIS2 transposition, identified

Every other country in the Atlas with a cyber authority has the
instrument beside it: [[BE-CCB]] with [[BE-NIS2-WET]], [[DE-BSI]] with
[[DE-BSIG]], [[FR-ANSSI]] with [[FR-NIS2-LOI]], [[IE-NCSC]] with
[[IE-NCS-BILL]]. Portugal's was flagged as unidentified when this entity
was created; it is [[PT-DECRETO-LEI-125-2025]], published 4 December
2025 and in force from 3 April 2026 — recent enough that it postdates
this Atlas's last full Portugal pass.

## Relationships

- `part-of` [[PT]] — anchor edge.
- `implements-requirement-from` [[EU-NIS2]] — via
  [[PT-DECRETO-LEI-125-2025]].

## Sources

Listed in frontmatter. `cncs.gov.pt` itself currently returns a
redirect loop under automated fetch; the gazette index and RTP's report
were read instead.
