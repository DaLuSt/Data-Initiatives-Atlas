---
id: UN-CEFACT
type: organisation
name: United Nations Centre for Trade Facilitation and Electronic Business
alternative_names:
  - UN/CEFACT
description: >
  Subsidiary intergovernmental body of the United Nations Economic
  Commission for Europe, serving as the focal point within the United
  Nations Economic and Social Council for trade facilitation recommendations
  and electronic business standards. Its stated goal is "Simple, Transparent
  and Effective Processes for Global Commerce", and it aims to help business,
  trade and administrative organisations from developed, developing and
  transition economies to exchange products and services effectively. It
  works on trade facilitation — simplifying trade procedures, including
  standardising and harmonising the core information used in trade documents
  — and on electronic business. Its approved recommendations and standards
  are described as contributing to the implementation of the WTO Trade
  Facilitation Agreement, regional paperless-trade initiatives and the 2030
  Sustainable Development Agenda.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations:
  - UN-UNECE
related_entities:
  - UN-UNECE
relationships:
  - type: part-of
    target: UN-UNECE
    source: fact
    evidence: "All four originally-cited unece.org pages returned HTTP 403 on every attempt this pass, including a bare-root-domain test — `unece.org` is blocked domain-wide this session. Per this batch's source-substitution instruction, three alternates were fetched directly and corroborate the claim: Wikipedia's UN/CEFACT article states it is 'created in 1996 as part of the United Nations Economic Commission for Europe (UNECE)... an intergovernmental body within UNECE's framework, with UNECE providing secretarial support'; service-architecture.com states UN/CEFACT 'is situated in the Economic Commission for Europe (UN/ECE)... and reports to ECOSOC'; and Nigeria's NEPC page (a national trade-promotion agency reporting on its own UN/CEFACT Bureau seat) independently describes it as 'an intergovernmental body...within the framework of...ECOSOC', without naming UNECE specifically. Two of the three name UNECE explicitly; the third corroborates the ECOSOC half of the claim."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Trade Facilitation and E-business (UN/CEFACT)"
    url: "https://unece.org/trade/uncefact"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "UN/CEFACT — Introduction"
    url: "https://unece.org/trade/uncefact/introduction"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "UN/CEFACT"
    url: "https://en.wikipedia.org/wiki/UN/CEFACT"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "United Nations Centre for Trade Facilitation and Electronic Business (UN/CEFACT)"
    url: "https://www.service-architecture.com/articles/web-services/united-nations-centre-for-trade-facilitation-and-electronic-business-un-cefact.html"
    publisher: "Service-Architecture.com"
    accessed: "2026-08-28"
  - title: "UN/CEFACT Initiative"
    url: "https://nepc.gov.ng/trade-facilitation/un-cefact-initiative/"
    publisher: "Nigerian Export Promotion Council (NEPC)"
    accessed: "2026-08-28"
---

# UN/CEFACT — UN Centre for Trade Facilitation and Electronic Business

> **Verified 2026-08-28, via source substitution.** `unece.org` is blocked
> domain-wide this session — all four originally-cited pages, and the bare
> domain itself, return HTTP 403. Three alternates were fetched directly
> per this batch's instruction and corroborate the entity's core claims:
> Wikipedia, a service-architecture.com profile, and Nigeria's NEPC trade
> agency's own page (reporting on its seat on the UN/CEFACT Bureau). Two of
> the four sources in the revised list below are original UNECE pages kept
> on record as unread/blocked; the other three are the newly-read
> alternates — a genuine majority (3 of 5).

## Description

UN/CEFACT is a **subsidiary intergovernmental body of [[UN-UNECE]]** and the
focal point within ECOSOC for **trade facilitation recommendations and
electronic business standards**.

Its goal is *"Simple, Transparent and Effective Processes for Global
Commerce"*. It works on two things: **trade facilitation** — standardising
and harmonising the core information used in trade documents — and
**electronic business**.

## Recorded with no European link, and that is the finding

`discovery/candidates.md` listed UN/CEFACT with an explicit warning:

> *Produces standards of exactly the kind the Atlas models (UN/EDIFACT,
> UN/LOCODE, Core Components). **EU adoption is not sourced yet** — that is
> the gap to close.*

It was not closed for UN/CEFACT **as a body** — nothing found this pass or
before establishes that any EU instrument or member state adopts UN/CEFACT
recommendations in general. But it is worth flagging that this is no longer
true at the level of one specific output: [[UN-LOCODE]], one of UN/CEFACT's
own code lists, is named directly in Regulation (EU) 2019/1239 (the European
Maritime Single Window regulation) — a fact already recorded on [[UN-LOCODE]]
and [[EU-EMSWE]] themselves, not new this pass. So the entity is here,
attached to its parent, and while UN/CEFACT the *body* connects to the
European layer not at all, one of its *outputs* now genuinely does — a
distinction worth holding precisely rather than letting either overstate the
other.

That is a deliberate outcome rather than a failure to finish. Of the four
clusters in `discovery/candidates.md`, three produced European↔UN edges and
this one did not. Recording it with the missing edge visible is more useful
than leaving it out: it marks a specific, narrow question — *does any EU or
national instrument in this Atlas reference a UN/CEFACT standard?* — that
someone with page access can answer quickly.

**No UN/CEFACT standard is modelled either.** UN/EDIFACT, UN/LOCODE and the
Core Component Library are named in the description as what the body
produces; none has an entity, because none was researched.

## `coverage: low`

Its governance, plenary structure and relationship to ECOSOC beyond "focal
point" remain unrecorded. One new fact did surface this pass, from Wikipedia
rather than UNECE: UN/CEFACT was **created in 1996**, building on UNECE trade
facilitation work dating to 1957. Per this batch's date-fabrication
discipline, `start_date` is left `null` rather than set to a padded
`1996-01-01` — a year is not a day — but the year itself is now recorded in
prose here.

## Relationships

- `part-of` [[UN-UNECE]].

## Sources

Listed in frontmatter, three of five read directly this pass. Both original
`unece.org` pages are kept on record but are 403-blocked this session; three
alternates (Wikipedia, service-architecture.com, NEPC) were read directly in
their place, per this batch's source-substitution instruction.
