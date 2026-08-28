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
verification: primary-source

start_date: 2019-06-20
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU
  - UN-LOCODE
  - UN-CEFACT
  - EU-EFTI-REGULATION
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "Confirmed by reading the European Parliament's own Legislative Observatory (OEIL) procedure file directly (2026-08-28): the legislative proposal was published 17 May 2018, Parliament approved at first reading 18 April 2019, the Council adopted 13 June 2019, the final act was signed 20 June 2019, and it was published in OJ L 198 of 25 July 2019. transport.ec.europa.eu's own EMSWe page, also read directly, confirms the regulation 'harmonise[s] and simplify[ies] reporting requirements for ships arriving at, staying in, and departing from EU ports' and states explicitly that 'EMSWe becomes applicable on 15 August 2025' — an application date this entity had not previously recorded."
    confidence: high
    valid_from: 2019-06-20
    valid_until: null
  - type: references
    target: UN-LOCODE
    source: fact
    evidence: "Confirmed by reading EMSA's (European Maritime Safety Agency) own EMSWe page directly (2026-08-28): the Regulation requires a harmonised Reporting Interface Module and a common location database; transport.ec.europa.eu's own page, also read directly, names the Common Location Database as one of three databases supporting the system. The specific UN/LOCODE, SafeSeaNet-code and GISIS composition of that database was confirmed via the legislation.gov.uk retained-text mirror, also read directly."
    confidence: high
    valid_from: 2019-06-20
    valid_until: null

sources:
  - title: "European maritime single window environment — OEIL procedure file"
    url: "https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2018/0139(COD)"
    publisher: "European Parliament — Legislative Observatory"
    accessed: "2026-08-28"
  - title: "European Maritime Single Window Environment (EMSWe)"
    url: "https://transport.ec.europa.eu/transport-modes/maritime/eu-wide-digital-maritime-system-and-services/european-maritime-single-window-environment_en"
    publisher: "European Commission — Mobility and Transport"
    accessed: "2026-08-28"
  - title: "EMSWe Message Implementation Guide"
    url: "https://emsa.europa.eu/emswe-mig/"
    publisher: "European Maritime Safety Agency (EMSA)"
    accessed: "2026-08-28"
  - title: "Regulation (EU) 2019/1239 of the European Parliament and of the Council of 20 June 2019 establishing a European Maritime Single Window environment"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019R1239"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "Regulation (EU) 2019/1239 — retained EU legislation text"
    url: "https://www.legislation.gov.uk/eur/2019/1239/data.xht?view=snippet&wrap=true"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-28"
---

# EMSWe — Regulation (EU) 2019/1239

> **Re-verified 2026-08-28.** `eur-lex.europa.eu` remains unreadable to
> this pass's fetch tooling. Three new sources were found and read
> directly instead — the European Parliament's own procedure file, the
> Commission's DG MOVE EMSWe page, and EMSA's own Message Implementation
> Guide page — which together confirm the full legislative timeline and
> surface a previously-unrecorded fact: EMSWe's actual **application
> date is 15 August 2025**, six years after adoption. `verification`
> moves from `search-only` to `primary-source`.

## Description

The regulation of **20 June 2019** (signed; the OEIL procedure file, read
directly, gives Parliament approval 18 April 2019, Council adoption 13 June
2019, and Official Journal publication 25 July 2019) establishes the
**European Maritime Single Window environment** and repeals Directive
2010/65/EU. It harmonises the reporting obligations a ship faces on
arrival at and departure from a Union port: a **common EMSWe data set**,
national maritime single windows through which declarants submit it once,
and a **mapping between customs data requirements and the corresponding
EMSWe data elements** so that what is submitted can be processed by
customs IT systems.

**EMSWe did not become applicable until 15 August 2025** — confirmed by
reading the Commission's own DG MOVE page directly, six years after
adoption. This entity previously carried only the 2019 adoption date; the
application date is a genuine, previously-missing fact and is recorded
here rather than in `start_date` (which stays at the regulation's own
dating, following this Atlas's convention of dating an instrument by its
own text rather than by whichever milestone a later pass discovers).

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
- ~~The **eFTI Regulation (EU) 2020/1056**~~ — now [[EU-EFTI-REGULATION]].
  Its full text was read directly and searched for "UN/CEFACT", "CEFACT",
  "MMT" and "UNECE": none appears. The secondary-source claim that it
  builds its data set on the UN/CEFACT MMT-RDM model is not supported by
  the instrument itself — the actual data set is left to a future
  delegated act the Regulation does not yet identify. [[UN-LOCODE]] in
  EMSWe remains the only sourced EU→UN/CEFACT connection.

## Relationships

- `applies-in` [[EU]].
- `references` [[UN-LOCODE]] — the citing party carries the edge.

## Sources

Listed in frontmatter, four of five read directly this pass — the European
Parliament's own OEIL procedure file, the Commission's DG MOVE EMSWe page,
EMSA's own Message Implementation Guide page, and the National Archives'
retained-EU-law text (which surfaced the location-database provision).
`eur-lex.europa.eu` returned empty content, consistent with every other
EUR-Lex attempt made across this batch, and was not read.
