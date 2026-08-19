---
id: PT-CNPD
type: organisation
name: Comissão Nacional de Proteção de Dados
alternative_names:
  - CNPD
  - Portuguese Data Protection Authority
description: >
  Portugal's data protection supervisory authority — an independent
  administrative authority with powers of control over the processing of
  personal data, conferred by the GDPR read together with Lei n.º 58/2019.

level: national
country: PT
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PT-LEI-58-2019
  - EU-EDPB
  - EU-GDPR
relationships:
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Article 68(3) GDPR provides that the European Data Protection Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives; the CNPD is Portugal's supervisory authority (gdpr-info.eu 'Art. 68 GDPR — European Data Protection Board'; gdprhub.eu 'Article 68 GDPR'; edpb.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PT-LEI-58-2019
    source: fact
    evidence: "The CNPD acts as an independent administrative authority with powers of control over personal data processing, as conferred by the RGPD in conjunction with Lei n.º 58/2019 (cnpd.pt; Lei n.º 58/2019 de 8 de agosto). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CNPD — Comissão Nacional de Proteção de Dados"
    url: "https://www.cnpd.pt/"
    publisher: "Comissão Nacional de Proteção de Dados (CNPD)"
  - title: "Lei n.º 58/2019, de 8 de agosto — Lei de Proteção de Dados Pessoais"
    url: "https://www.stcpservicos.pt/storage/app/media/Documentos%20Gerais/Lei%20Prote%C3%A7%C3%A3o%20Dados%20-%20Lei%2058-2019.pdf"
    publisher: "Diário da República (reproduction)"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
  - title: "Article 68 GDPR"
    url: "https://gdprhub.eu/Article_68_GDPR"
    publisher: "GDPRhub (noyb)"
---

# Comissão Nacional de Proteção de Dados

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The CNPD is Portugal's data protection supervisory authority: an
**independent administrative authority** whose control powers come from the
GDPR **read together with** [[PT-LEI-58-2019]].

That formulation is worth keeping. The Portuguese sources describe the
authority's powers as conferred by the Regulation *in conjunction with* the
national act — not by one or the other. It is the clearest statement in the
Atlas of how a national GDPR instrument and the Regulation operate together.

## The ninth authority on the Board

[[EU-EDPB]] had two incoming edges before the structural-fixes batch and
eight after it. The CNPD makes nine, on the same basis: **Article 68(3)**
composes the Board of one supervisory-authority head per member state plus
the [[EU-EDPS]].

## Relationships

- `participates-in` [[EU-EDPB]].
- `applies-to` [[PT-LEI-58-2019]].

## Sources

Listed in frontmatter.
