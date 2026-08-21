---
id: EU-EMSWE
type: regulation
name: Regulation (EU) 2019/1239 establishing a European Maritime Single Window environment
alternative_names:
  - EMSWe Regulation
  - European Maritime Single Window environment
description: >
  Regulation of the European Parliament and of the Council of 20 June 2019
  establishing a European Maritime Single Window environment and repealing
  Directive 2010/65/EU. It harmonises the reporting obligations ships face on
  arrival at and departure from Union ports by establishing a common EMSWe
  data set and national maritime single windows. It provides for a common
  location database holding a reference list of location codes, including the
  United Nations Code for Trade and Transport Locations (UN/LOCODE), the
  SafeSeaNet-specific codes and the port facility codes registered in the
  International Maritime Organization's Global Integrated Shipping
  Information System, and includes a mapping between customs data
  requirements and the corresponding EMSWe data elements.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2019-06-20
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU
  - UN-LOCODE
  - UN-CEFACT
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "Regulation (EU) 2019/1239 of the European Parliament and of the Council of 20 June 2019 establishing a European Maritime Single Window environment and repealing Directive 2010/65/EU (eur-lex.europa.eu CELEX 32019R1239; eur-lex.europa.eu legislative summary 'European maritime single window environment'). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-06-20
    valid_until: null
  - type: references
    target: UN-LOCODE
    source: fact
    evidence: "The Regulation provides for a common location database holding a reference list of location codes, including the United Nations Code for Trade and Transport Locations (UN/LOCODE), the SafeSeaNet-specific codes and the port facility codes as registered in the Global Integrated Shipping Information System (GISIS) of the International Maritime Organization, designed to facilitate the submission of information by declarants in the European Maritime Single Window environment (eur-lex.europa.eu CELEX 32019R1239; legislation.gov.uk eur/2019/1239 retained text). NOT READ — search-only."
    confidence: medium
    valid_from: 2019-06-20
    valid_until: null

sources:
  - title: "Regulation (EU) 2019/1239 of the European Parliament and of the Council of 20 June 2019 establishing a European Maritime Single Window environment"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019R1239"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "European maritime single window environment — legislative summary"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/european-maritime-single-window-environment.html"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "Regulation (EU) 2019/1239 — retained EU legislation text"
    url: "https://www.legislation.gov.uk/eur/2019/1239/data.xht?view=snippet&wrap=true"
    publisher: "The National Archives (legislation.gov.uk)"
---

# EMSWe — Regulation (EU) 2019/1239

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval of
> `eur-lex.europa.eu` is blocked by the network egress proxy.
> `verification: search-only`.

## Description

The regulation of **20 June 2019** establishing the **European Maritime
Single Window environment** and repealing Directive 2010/65/EU. It harmonises
the reporting obligations a ship faces on arrival at and departure from a
Union port: a **common EMSWe data set**, national maritime single windows
through which declarants submit it once, and a **mapping between customs data
requirements and the corresponding EMSWe data elements** so that what is
submitted can be processed by customs IT systems.

## Why a shipping regulation is in a data atlas

Because it is a data regulation. Its subject is a harmonised data set, a
submission-once obligation, and a shared reference database — the same
apparatus [[EU-SDG]] and the Single Digital Gateway apply to other domains.

It also carries the **common location database**: a reference list of
location codes holding [[UN-LOCODE]], the SafeSeaNet-specific codes, and the
IMO port facility codes registered in GISIS.

## The instrument the trade cluster was missing

`discovery/candidates.md` §2 asked whether *"any instrument already in this
Atlas reference[s] a UN/CEFACT standard"*, calling it *"the narrow question
that would connect the trade/e-business cluster"*. Nothing already in the
Atlas did. This regulation does, and adding it connects [[UN-CEFACT]] to the
European layer for the first time.

It also does something for the domain layer. `discovery/candidates.md`
measured [[DOMAIN-MOBILITY]] at **2 of 7 countries** and called the domain
coverage lopsided. This is a regional instrument rather than a national one,
so it does not move that count — but it is the first EU-level mobility
instrument in the Atlas, and [[UN-LOCODE]] is the second mobility entity
added with it.

## What is not modelled

- **Directive 2010/65/EU**, which this regulation repealed, is not an entity,
  so no `supersedes` edge is asserted.
- The **SafeSeaNet codes** and the IMO **GISIS** port facility codes are named
  in the same provision as UN/LOCODE. Neither is modelled: the IMO is not in
  the Atlas at all, and creating it to carry one code list would be the thin
  entity the taxonomy threshold prevents. Recorded in
  `discovery/unresolved.md`.
- The **eFTI Regulation (EU) 2020/1056** was found in the same research and
  is described in secondary sources as building its data set on the UN/CEFACT
  MMT-RDM model. It is **not** created: the claim was found in a UNECE
  presentation and a project website, not in the regulation, and UN/LOCODE in
  EMSWe is the better-sourced instance of the same connection. Queued in
  `discovery/research-queue.md`.

## Relationships

- `applies-in` [[EU]].
- `references` [[UN-LOCODE]] — the citing party carries the edge.

## Sources

Listed in frontmatter — the EUR-Lex full record and legislative summary, and
the National Archives' retained-EU-law text, which was the source that
surfaced the location-database provision.
