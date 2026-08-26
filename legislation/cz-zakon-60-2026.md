---
id: CZ-ZAKON-60-2026
type: law
name: Zákon o správě dat a řízeném přístupu
alternative_names:
  - Zákon č. 60/2026 Sb.
  - Act on data management and controlled access
description: >
  Czech act on data management and controlled access to data (No 60/2026
  Sb.), implementing the EU Data Governance Act in Czech law and
  substantially extending it with specific tools. Under it the Digital
  and Information Agency serves as Czechia's single information point
  and the node for communication with European structures, connecting
  Czech data sources to the European data portal.

level: national
country: CZ
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2026-05-27
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ
  - CZ-DIA
  - EU-DGA
relationships:
  - type: applies-in
    target: CZ
    source: fact
    evidence: "Confirmed by reading zakonyprolidi.cz's own legal-text record directly (2026-08-26): 'Zákon č. 60/2026 Sb. ... 60 ZÁKON ze dne 15. dubna 2026 o správě dat, o řízeném přístupu k datům a o změně některých souvisejících zákonů' (Act No. 60 of 15 April 2026 on data management, controlled access to data, and amending certain related acts). The same record gives 'Platnost od 12.05.2026' (published/valid from 12 May 2026) and 'Účinnost od 27.05.2026' (in effect from 27 May 2026), noting 'Předpis má dělenou účinnost' (the act has staggered effectiveness). data.gov.cz's own homepage, read independently, corroborates the 12 May 2026 publication date: 'Dne 12. května 2026 vyšel ve Sbírce zákonů dlouho očekávaný Zákon o správě dat a řízeném přístupu k datům pod č. 60/2026 Sb.'"
    confidence: medium
    valid_from: "2026-05-27"
    valid_until: null
  - type: implements-requirement-from
    target: EU-DGA
    source: fact
    evidence: "Confirmed in the Act's own statutory text, read directly on zakonyprolidi.cz (2026-08-26): § 1(1) states 'Tento zákon upravuje v návaznosti na přímo použitelný předpis Evropské unie upravující správu dat (dále jen „nařízení o evropské správě dat“)...' (This Act regulates, in connection with the directly applicable European Union regulation governing data governance (hereinafter the 'European Data Governance Regulation')...) — the Act's own first section names the Data Governance Act as what it implements. isvs.cz's report, read independently, states the same thing in plainer terms: 'V českém prostředí implementuje evropské nařízení Digital Governance Act (Akt o správě dat), a výrazně jej rozšiřuje o specifické nástroje' (In the Czech context it implements the European Digital Governance Act (Data Governance Act), and substantially extends it with specific tools)."
    confidence: medium
    valid_from: "2026-05-27"
    valid_until: null

sources:
  - title: "Zákon č. 60/2026 Sb. — Zákon o správě dat, o řízeném přístupu k datům a o změně některých souvisejících zákonů"
    url: "https://www.zakonyprolidi.cz/cs/2026-60"
    publisher: "Zákony pro lidi (AION CS)"
    accessed: "2026-08-26"
  - title: "Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.dia.gov.cz/cs/aktuality/zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani"
    publisher: "Digitální a informační agentura (DIA)"
    accessed: "2026-08-26"
  - title: "DIA: Zákon o správě dat a řízeném přístupu otevírá cestu státu k efektivnímu rozhodování"
    url: "https://www.isvs.cz/dia-zakon-o-sprave-dat-a-rizenem-pristupu-otevira-cestu-statu-k-efektivnimu-rozhodovani/"
    publisher: "ISVS.CZ"
    accessed: "2026-08-26"
---

# Zákon o správě dat a řízeném přístupu

> **Verified 2026-08-26.** All three cited pages were read directly.
> The Act's own text on zakonyprolidi.cz supplied precise dates this
> entity previously had none of (enacted 15 April 2026, published 12
> May, in effect 27 May) and, in its own § 1, names the EU Data
> Governance Act as what it implements — a relationship this entity
> did not previously carry at all.

## Description

The Czech act on **data management and controlled access to data**, No
60/2026 Sb. — enacted **15 April 2026**, published in the Sbírka
zákonů (Collection of Laws) on **12 May 2026**, and in effect from
**27 May 2026** for most provisions, with staggered effectiveness for
the rest (see below).

## It implements the EU Data Governance Act — in its own words

The Act's own § 1(1), read directly, states it regulates matters "v
návaznosti na přímo použitelný předpis Evropské unie upravující správu
dat" — in connection with the directly applicable EU regulation on
data governance, i.e. [[EU-DGA]]. isvs.cz's independent report puts it
plainly: the Act "implements the European Digital Governance Act...
and substantially extends it with specific tools." No source read
states what those extensions are beyond the National Data Catalogue
described below, so nothing further is asserted.

## The entity Czechia was added for

The Atlas holds a great deal of law *about* data: data protection acts, open
data transpositions, cyber security acts, statistics acts. What it has almost
none of is law about **how a state manages its own data and lets others reach
it**.

This act does that, and names a body to do it: [[CZ-DIA]] becomes the
**single information point** and the node connecting Czech data sources to
the **European data portal**.

The nearest things elsewhere in the Atlas are Dutch and are not statutes —
[[NL-IBDS]], an interadministrative data strategy, and [[NL-FDS]], a
federative data system. A comparison the Atlas can now make: **the
Netherlands built the arrangement, Czechia legislated it.**

## A four-year rollout, not a single effective date

isvs.cz's report, read directly, describes a phased implementation
that "staggered effectiveness" understates: the Act expands the
existing National Open Data Catalogue — [[CZ-DATA-GOV]] — into a
broader **Národní katalog dat** (National Data Catalogue) covering both
open and non-public data, administered by DIA ("jehož správcem bude
DIA"). From **January 2028** the catalogue begins acting as the
intermediary for controlled-access requests to non-public data; full
operation, with every public authority obliged to register its data
centrally, begins **1 January 2029**. DIA's own director, Bohdan Urban,
is quoted in the same article, and DIA is named as the bill's own
proposer ("Předkladatelem zákona byla DIA").

## Relationships

- `applies-in` [[CZ]].
- `implements-requirement-from` [[EU-DGA]].

## Sources

Listed in frontmatter, all three read directly this pass.
