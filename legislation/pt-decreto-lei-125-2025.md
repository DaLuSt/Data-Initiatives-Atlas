---
id: PT-DECRETO-LEI-125-2025
type: law
name: Decreto-Lei n.º 125/2025
alternative_names:
  - Regime Jurídico da Cibersegurança
  - Portuguese Cybersecurity Legal Regime
description: >
  Portuguese decree-law of 4 December 2025 approving the legal regime for
  cybersecurity and transposing Directive (EU) 2022/2555 (NIS2) into
  Portuguese law, consolidating the Centro Nacional de Cibersegurança
  (CNCS) as the national cybersecurity authority.

level: national
country: PT
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2026-04-03
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - PT
  - PT-CNCS
  - EU-NIS2
relationships:
  - type: applies-in
    target: PT
    source: fact
    evidence: "Confirmed by reading the Diário da República's own gazette index directly (2026-08-26, files.dre.pt, Série I, n.º 234, 4 December 2025): 'Decreto-Lei n.º 125/2025 — Transpõe a Diretiva (UE) 2022/2555, relativa a medidas destinadas a garantir um elevado nível comum de cibersegurança na União' (Transposes Directive (EU) 2022/2555, on measures to ensure a high common level of cybersecurity in the Union). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading the Diário da República's own gazette index directly (2026-08-26): the decree-law's own summary states it transposes 'a Diretiva (UE) 2022/2555' — the NIS2 Directive's own number. Independent Portuguese press (RTP, read directly) corroborates: 'O decreto-Lei n.º 125/2025 aprova o regime jurídico da cibersegurança, transpondo a Diretiva (UE), do Parlamento Europeu e do Conselho, de 14 de dezembro de 2022' and states it enters into force 120 days after publication — RTP's report of an April 2026 entry into force matches the 4 December 2025 publication date plus 120 days."
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
---

# Decreto-Lei n.º 125/2025

> **Verified 2026-08-26.** The Diário da República's own gazette index
> and an independent press report (RTP) were both read directly. This is
> a newly created entity, closing a gap [[PT-CNCS]] had flagged since its
> own creation: "Portugal's NIS2 transposition was not identified."

## Description

Decreto-Lei n.º 125/2025, published **4 December 2025** and in force
from **3 April 2026** (120 days after publication, per RTP's report),
approves Portugal's legal regime for cybersecurity and transposes
**Directive (EU) 2022/2555** — NIS2 — into Portuguese law. RTP reports
it "reinforces CNCS's role as the national cybersecurity authority
while establishing sectoral and specialised supervisory bodies."

## The gap this closes

[[PT-CNCS]]'s own entity file, read again this pass, noted that every
other country in the Atlas with a cyber authority had its transposing
instrument modelled beside it — [[BE-CCB]] with [[BE-NIS2-WET]],
[[DE-BSI]] with [[DE-BSIG]], [[FR-ANSSI]] with [[FR-NIS2-LOI]],
[[IE-NCSC]] with [[IE-NCS-BILL]] — while Portugal's was "not identified."
It now is.

## Not modelled

- The decree-law's own text beyond its gazette-index summary — the
  articles establishing CNCS's specific powers, the sectoral/special
  supervisory authorities it creates, and its full transposition table
  were not read this pass, only reported on by RTP and the official
  index.
- The **Conselho Superior de Segurança do Ciberespaço (CSSC)**, an
  advisory body to the Prime Minister that press reporting says this
  decree-law also establishes.

## Relationships

- `applies-in` [[PT]] — anchor edge.
- `implements-requirement-from` [[EU-NIS2]].

## Sources

Listed in frontmatter, both read directly this pass.
