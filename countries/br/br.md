---
id: BR
type: country
name: "Brazil"
description: >
  Country anchor entity for Brazil. A base anchor: it exists because the
  Atlas models the sourced national entities listed in its index, and it
  carries no more than that.

level: national
country: BR
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-10-16"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - BR-ANPD
  - BR-LGPD
  - BR-ECA-DIGITAL
  - BR-LEI-15352-2026
relationships: []

sources:
  - title: "Institucional — ANPD"
    url: "https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional"
    publisher: "Agência Nacional de Proteção de Dados (Brasil)"
    accessed: "2026-10-16"
    note: "Page modified 5 October 2026."
---

# Brazil

## Description

Brazil (ISO 3166-1 alpha-2: **`BR`**) is a **base country anchor**. It carries the National Data Protection Agency ([[BR-ANPD]]) and three laws, all read on the Agency's own site: the General Data Protection Law ([[BR-LGPD]]), the Digital Statute of Children and Adolescents ([[BR-ECA-DIGITAL]]) and the law that turned the Agency into a regulatory agency ([[BR-LEI-15352-2026]]). The laws' own texts were not read (planalto.gov.br did not answer).

## What this anchor does not yet carry

Only the entities listed in [the country index](index.md). The laws' texts, the Agency's regulations, the decrees of May 2026 on the Marco Civil da Internet, the Brazilian digital government strategy and the open data policy were not read. It is a first sourced slice, not a survey of the country's data governance (see `countries/README.md` on the participation model).
