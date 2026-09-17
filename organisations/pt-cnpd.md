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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-17"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PT
  - PT-LEI-58-2019
  - PT-LEI-43-2004
  - EU-EDPB
  - EU-GDPR
relationships:
  - type: part-of
    target: PT
    source: fact
    evidence: "Confirmed by reading cnpd.pt's own 'o que somos e quem somos' page directly (2026-08-26): the CNPD is 'uma entidade administrativa independente, com personalidade jurídica de direito público e com poderes de autoridade' (an independent administrative entity with public-law personality and authority powers), organised under Lei n.º 43/2004 of 18 August. Anchor edge under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: PT-LEI-43-2004
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (this entity's own 'not itself an Atlas entity' note). Confirmed by reading the Diário da República's own text of Lei n.º 43/2004 directly (2026-09-17, files.dre.pt, Série I-A, N.º 194, 18 August 2004, pp. 5251-5253): Article 1 states the law regulates the CNPD's organisation and functioning and the personal statute of its members; Article 2 defines the CNPD as 'uma entidade administrativa independente, com poderes de autoridade, que funciona junto da Assembleia da República' (an independent administrative entity, with authority powers, functioning alongside the Assembly of the Republic)."
    confidence: high
    valid_from: "2004-08-18"
    valid_until: null
  - type: participates-in
    target: EU-EDPB
    source: fact
    evidence: "Confirmed by reading gdpr-info.eu's own text of Article 68(3) GDPR directly (2026-08-26): 'The Board shall be composed of the head of one supervisory authority of each Member State and of the European Data Protection Supervisor, or their respective representatives.' cnpd.pt's own page, also read directly, confirms the CNPD is Portugal's national supervisory authority for GDPR compliance."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: PT-LEI-58-2019
    source: fact
    evidence: "Confirmed by reading cnpd.pt's own 'o que somos e quem somos' page directly (2026-08-26): the CNPD's organisational framework derives from Lei n.º 43/2004, and its powers derive from both the RGPD (Articles 57-58) and Lei n.º 58/2019, which 'empowers the CNPD to defend direitos, liberdades e garantias das pessoas singulares' (rights, freedoms and guarantees of individuals) in personal-data-processing contexts — read together, as [[PT-LEI-58-2019]] itself also states."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CNPD — o que somos e quem somos"
    url: "https://www.cnpd.pt/cnpd/o-que-somos-e-quem-somos/"
    publisher: "Comissão Nacional de Proteção de Dados (CNPD)"
    accessed: "2026-08-26"
  - title: "Lei de Proteção de Dados Pessoais — Lei n.º 58/2019, de 8 de agosto (texto consolidado)"
    url: "https://www.stcpservicos.pt/storage/app/media/Documentos%20Gerais/Lei%20Prote%C3%A7%C3%A3o%20Dados%20-%20Lei%2058-2019.pdf"
    publisher: "LegiX / Priberam Informática (consolidated-text mirror; not the Diário da República itself)"
    accessed: "2026-08-26"
  - title: "Art. 68 GDPR — European Data Protection Board"
    url: "https://gdpr-info.eu/art-68-gdpr/"
    publisher: "gdpr-info.eu (Intersoft Consulting)"
    accessed: "2026-08-26"
---

# Comissão Nacional de Proteção de Dados

> **Verified 2026-08-26.** All three cited pages were read directly.
> cnpd.pt's own page names the CNPD's organisational statute (Lei n.º
> 43/2004) — a fact this entity did not previously carry — and confirms
> the "read together with" formulation in its own words.
>
> **Closed 2026-09-17.** Lei n.º 43/2004 is now [[PT-LEI-43-2004]],
> closing this entity's own "not itself an Atlas entity" note. Its own
> text, read directly, confirms the CNPD's legal nature and adds a
> `governed-by` edge.

## Description

The CNPD is Portugal's data protection supervisory authority: an
**independent administrative authority** whose control powers come from the
GDPR **read together with** [[PT-LEI-58-2019]]. Confirmed by reading
cnpd.pt directly, its own organisation and functioning are set out in
**Lei n.º 43/2004, of 18 August** — a separate statute from either of
those two, and now its own Atlas entity, [[PT-LEI-43-2004]], read
directly at the Diário da República on 2026-09-17.

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

- `part-of` [[PT]] — anchor edge, confirmed this pass.
- `participates-in` [[EU-EDPB]].
- `applies-to` [[PT-LEI-58-2019]].
- `governed-by` [[PT-LEI-43-2004]] — added 2026-09-17, closing this
  entity's own previous "not itself an Atlas entity" note.

## Sources

Listed in frontmatter, all three read directly on 2026-08-26.
[[PT-LEI-43-2004]]'s own text read directly on 2026-09-17.
