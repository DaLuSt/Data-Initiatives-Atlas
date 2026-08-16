---
id: PL-OTWARTE-DANE
type: law
name: Ustawa z dnia 11 sierpnia 2021 r. o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego
alternative_names:
  - Ustawa o otwartych danych
  - Polish Open Data Act 2021
description: >
  Polish act of 11 August 2021 on open data and the re-use of public sector
  information, published as Dz.U. 2021 poz. 1641 and effective from 8
  December 2021. It implements Directive (EU) 2019/1024 of 20 June 2019 on
  open data and the re-use of public sector information, and fully repeals
  the Act of 25 February 2016 on the re-use of public sector information. It
  introduces high-value data and dynamic data categories, requires dynamic
  data to be made available through APIs, opens research data produced by
  publicly funded scientific activity to re-use, and establishes a data
  portal as a database of public sector information resources. It is
  described as implementing solutions going beyond the directive's minimum
  standards.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2021-12-08
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-OPEN-DATA-DIRECTIVE
  - PL-DANE-GOV-PL
  - NL-WHO
  - DE-DNG
  - ES-LEY-37-2007
relationships:
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "The Act of 11 August 2021 on open data and re-use of public sector information aims to implement Directive (EU) 2019/1024 of 20 June 2019 on open data and the re-use of public sector information; it is effective from 8 December 2021 and fully repeals the Act of 25 February 2016 on the re-use of public sector information. It introduces high-value data and dynamic data categories, access to dynamic data through APIs, re-use of publicly funded research data, and establishes a data portal as a database of public sector information resources (isap.sejm.gov.pl WDU20210001641; gov.pl/web/ia 'Nowa ustawa o otwartych danych'; nist.gov.pl; nim.gov.pl). NOT READ — search-only."
    confidence: medium
    valid_from: 2021-12-08
    valid_until: null

sources:
  - title: "Ustawa z dnia 11 sierpnia 2021 r. o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego (Dz.U. 2021 poz. 1641)"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20210001641"
    publisher: "Internetowy System Aktów Prawnych (ISAP) — Sejm RP"
  - title: "Nowa ustawa o otwartych danych — Portal Interoperacyjności i Architektury"
    url: "https://www.gov.pl/web/ia/nowa-ustawa-o-otwartych-danych"
    publisher: "Portal Gov.pl"
  - title: "Nowa ustawa o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego"
    url: "https://nim.gov.pl/aktualnosci/nowa-ustawa-o-otwartych-danych-i-ponownym-wykorzystywaniu-informacji-sektora-publicznego.html"
    publisher: "Narodowy Instytut Muzealnictwa (NIM)"
  - title: "Ustawa z dnia 11 sierpnia 2021 r. — Narodowy Instytut Samorządu Terytorialnego"
    url: "https://archiwum.nist.gov.pl/prawo/ustawa-z-dnia-11-sierpnia-2021-r-o-otwartych-danych-i-ponownym-wykorzystywaniu-informacji-sektora-publicznego-dz-u-2021-poz-1641,3464.html"
    publisher: "Narodowy Instytut Samorządu Terytorialnego"
---

# Ustawa o otwartych danych (2021)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Act of **11 August 2021** (Dz.U. 2021 poz. 1641), effective **8 December
2021**, implements [[EU-OPEN-DATA-DIRECTIVE]] and **fully repeals the Act of
25 February 2016** on the re-use of public sector information.

What it introduces:

- **high-value data** and **dynamic data** categories;
- dynamic data **through APIs**;
- re-use of **research data** produced by publicly funded scientific
  activity;
- a **data portal** as a database of public sector information resources —
  see [[PL-DANE-GOV-PL]].

It is described as going **beyond the directive's minimum standards**.

## This resolves the 2016-act trap

`progress/backlog.md` has carried this since the Belgium batch, and the
Spain batch sharpened it:

> *The Open Data Directive transpositions for Belgium and France. Neither
> identified. Both countries have a well-known **earlier** open data act
> (2016 in both cases) that looks like the answer and chronologically cannot
> be it.*

**Poland had the identical 2016 act** — the *ustawa z dnia 25 lutego 2016 r.
o ponownym wykorzystywaniu informacji sektora publicznego* — and this act
**explicitly and fully repeals it**.

| Country | Transposition of [[EU-OPEN-DATA-DIRECTIVE]] | Earlier act |
|---|---|---|
| Netherlands | [[NL-WHO]] | — |
| Germany | [[DE-DNG]] | — |
| Spain | [[ES-LEY-37-2007]], amended 2021 | **2007**, amended in place |
| **Poland** | **this act** | **2016, fully repealed** |
| Belgium | *not identified* | 2016 ([[BE-HERGEBRUIK-WET]]) |
| France | *not identified* | 2016 ([[FR-LRN]]) |

**Four of six countries are now closed**, and the trap has appeared in four
of six — 2016 in Belgium, France and Poland, 2007 in Spain.

The Polish case is the most useful of the four, because it shows **what the
answer looks like**: a later act that names the earlier one and repeals it.
Spain's amends its earlier act in place; Poland's replaces it outright. The
Belgian and French answers, when found, will take one of those two shapes —
which is a materially better starting point than "an act exists somewhere".

## Relationships

- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]], valid from
  8 December 2021.

**No `supersedes` edge to the 2016 act**, because that act is not an Atlas
entity. It is named and dated in the evidence string. Creating a repealed
Polish act solely to carry one edge would be inconsistent with how the
Spanish, Belgian and French earlier acts are handled — of which only two
exist as entities, and both for independent reasons.

## Sources

Listed in frontmatter — the ISAP record with the Dziennik Ustaw citation,
the government interoperability portal, and two institute summaries. This is
the **best-cited Polish instrument in the batch**, and the only one with a
Dz.U. reference.
