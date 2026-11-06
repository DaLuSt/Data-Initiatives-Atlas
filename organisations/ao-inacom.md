---
id: AO-INACOM
type: organisation
name: "Angolan Institute of Communications (INACOM)"
alternative_names:
  - "INACOM"
  - "Instituto Angolano das Comunicações"
description: >
  Angola's regulator of electronic communications and postal services. Its site gives its mission as 'Regular, Supervisionar, e Fiscalizar o Mercado das Comunicações Electrónicas e serviços Postais'.
  Its legislation pages list the Estatuto Orgânico do INACOM (Decreto Presidencial n.º 243/14 of 9 September 2014), the Regulamento Geral das Comunicações Electrónicas (Decreto Presidencial 108/16 of 25 May 2016, republished by Decreto Presidencial n.º 271/25 of 29 December 2025), the national numbering and frequency plans, and the Lei n.º 23/11 of 20 June 2011. A page on data protection lists a data protection agency's organic statute (Decreto Presidencial n.º 214/16) and the 2025 national cybersecurity decrees (leads, not modelled; none opened).

level: national
country: AO
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - AO
  - AO-LEI-23-11
relationships:
  - type: part-of
    target: AO
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. INACOM's home page and legislation page (read 2026-11-06 through a summarising fetch tool): the regulator of electronic communications and postal services, with its organic statute Decreto Presidencial n.º 243/14 of 9 September 2014."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: AO-LEI-23-11
    source: fact
    evidence: "INACOM's legislation page lists 'Lei n.º 23/11 de 20 de Junho, Das Comunicações Electrónicas e dos Serviços da Sociedade da Informação' among its electronic communications legislation."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "INACOM (Instituto Angolano das Comunicações), página inicial"
    url: "https://www.inacom.gov.ao"
    publisher: "INACOM, Angola"
    accessed: "2026-11-06"
  - title: "INACOM, Legislação — Comunicações Electrónicas"
    url: "https://inacom.gov.ao/legislacao-comunicacoes-electronicas/"
    publisher: "INACOM, Angola"
    accessed: "2026-11-06"
---

# Angolan Institute of Communications (INACOM)

> **Created 2026-11-06** (roadmap #479). From the regulator's own pages through a summarising fetch tool. `start_date` empty: the date of the organic statute (9 September 2014) is the statute's, not necessarily the body's start.

## Relationships

Part of [[AO]]; governed by [[AO-LEI-23-11]].
