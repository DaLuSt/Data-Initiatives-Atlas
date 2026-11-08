---
id: GW-ARN-TIC
type: organisation
name: "National ICT Regulatory Authority (ARN-TIC, Guinea-Bissau)"
alternative_names:
  - "ARN"
  - "ARN-TIC"
  - "Autoridade Reguladora Nacional das Tecnologias de Informação e Comunicações"
description: >
  Guinea-Bissau's regulator of information and communication technologies. Its site says it succeeds the ICGB in its legal personality, keeping all its legal and contractual rights and obligations, and lists regulation and supervision, market analysis, spectrum management and the Universal Access Fund among its tasks, with a Conselho de Administração as its collegial body. The page names no founding instrument.
  Its national legislation page lists the Lei de Base das TIC (Lei n.º 5/2010 of 27 May), Decreto n.º 3/2021 on the radiocommunications regime, a 2022 quality-of-service despacho and short-number decision, and two 2021 Boletim Oficial regulations (network offer and services; communications networks).

level: national
country: GW
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-09"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - GW
  - GW-LEI-5-2010
relationships:
  - type: part-of
    target: GW
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. ARN-TIC's home page (read 2026-11-09 through a summarising fetch tool): the national ICT regulator, successor to the ICGB, with a Conselho de Administração."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GW-LEI-5-2010
    source: fact
    evidence: "ARN-TIC's national legislation page: 'LEI DE BASE – BOLETIM – Lei n. 5-2010, de 27 de Maio' heads its list."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ARN-TIC (Autoridade Reguladora Nacional das Tecnologias de Informação e Comunicações da Guiné-Bissau), página inicial"
    url: "https://arn.gw"
    publisher: "ARN-TIC, Guinea-Bissau"
    accessed: "2026-11-09"
  - title: "ARN-TIC, Legislação nacional"
    url: "https://arn.gw/nacionais/"
    publisher: "ARN-TIC, Guinea-Bissau"
    accessed: "2026-11-09"
---

# National ICT Regulatory Authority (ARN-TIC, Guinea-Bissau)

> **Created 2026-11-09** (roadmap #477). From the regulator's own pages through a summarising fetch tool. `start_date` empty: no founding instrument was named.

## Relationships

Part of [[GW]]; governed by [[GW-LEI-5-2010]].
