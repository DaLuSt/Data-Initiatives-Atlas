---
id: LI
type: country
name: Liechtenstein
alternative_names:
  - Principality of Liechtenstein
  - Liechtenstein
  - Fürstentum Liechtenstein
description: >
  Country anchor entity for Liechtenstein, a member of the European Free
  Trade Association and a party to the Agreement on the European Economic
  Area, and not a member of the European Union. It is a base anchor: it
  carries the country's position in the European legal and institutional
  frameworks so that entities scoped to it have somewhere to attach. Its
  first national entities are the data protection authority Datenschutzstelle
  and the Datenschutzgesetz.

level: national
country: LI
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-30"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - INTL-COE
relationships:
  - type: part-of
    target: INTL-COE
    source: fact
    evidence: "Confirmed 2026-09-30: coe.int itself remains genuinely bot-walled (403) even with an honest, identifying User-Agent, but Wikipedia's own dedicated 'Member states of the Council of Europe' article, read directly, gives a sourced per-country accession table: Liechtenstein joined 23 November 1978. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: high
    valid_from: "1978-11-23"
    valid_until: null

sources:
  - title: "The European Free Trade Association"
    url: "https://www.efta.int/about-efta/european-free-trade-association"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-22"
  - title: "LI — Liechtenstein (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:LI"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
    note: "coe.int itself remains genuinely bot-walled (403) and stays cited but unread; the accession date is sourced from Wikipedia below instead."
  - title: "Member states of the Council of Europe"
    url: "https://en.wikipedia.org/wiki/Member_states_of_the_Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-09-30"
---

# Liechtenstein

> **Verified 2026-08-22.** `efta.int` and `government.nl` were both read
> directly and confirm Liechtenstein's EFTA and EEA membership verbatim.
> `coe.int` and `iso.org` remain bot-walled (403) even with an honest,
> identifying User-Agent and stay cited but unread.
>
> **Confirmed 2026-09-30**: the Council of Europe membership claim below
> is now sourced with an accession date — 23 November 1978 — from
> Wikipedia's dedicated Council of Europe article, since `coe.int` itself
> remains bot-walled.

## Description

Liechtenstein (ISO 3166-1 alpha-2: **`LI`**) is a country anchor, created so
that entities scoped to it have somewhere to attach. Two Liechtenstein
entities are now modelled: [[LI-DATENSCHUTZSTELLE]] and [[LI-DSG]].

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | Member |
| Council of Europe | Member since 23 November 1978 |
| EFTA / EEA | Member of [[INTL-EFTA]]; party to [[INTL-EEA-AGREEMENT]] |

> The **EFTA/EEA row** is directly confirmed — see below. The **Council of
> Europe row** is now sourced too, from Wikipedia's dedicated member-states
> article (2026-09-30), since `coe.int` itself remains bot-walled.

## The third EEA EFTA state, and the smallest

Confirmed by reading efta.int's own "The European Free Trade
Association" page directly (2026-08-22, fetched with an honest,
identifying User-Agent — efta.int returns a bot-defense challenge to a
browser User-Agent but real content to one that names itself as a bot):
"The European Free Trade Association (EFTA) is the intergovernmental
organisation of Iceland, Liechtenstein, Norway and Switzerland," and
"three of the four EFTA States – Iceland, Liechtenstein and Norway – in
a single market" under the EEA Agreement. Corroborated by reading
government.nl's own "EU, EEA, EFTA and Schengen Area countries" page
directly: Liechtenstein is listed among both "The 30 EEA countries" and
"The 4 EFTA countries."

Liechtenstein completes the **EEA EFTA** trio with [[IS]] and
[[NO]]. EU acts reach it the same way: incorporation into
[[INTL-EEA-AGREEMENT]] by EEA Joint Committee decision, then national
implementation.

It is in the Schengen area and in a customs and currency union with [[CH]],
using the Swiss franc — so it is simultaneously inside the EEA and inside a
monetary arrangement with a state that is not.

One Joint Committee decision is modelled: [[INTL-EEA-JCD-154-2018]], which
incorporated [[EU-GDPR]]. Liechtenstein is the case where that mattered
least — the GDPR became **directly applicable** here on 20 July 2018, and
[[LI-DSG]] did not come into force until 1 January 2019, because the national
act supplements the regulation rather than giving it effect.

## What this anchor does not yet carry

The **data protection layer only**. [[LI-DATENSCHUTZSTELLE]] and [[LI-DSG]]
were added on 2026-08-21 alongside Iceland's, to test whether the Norwegian
EEA pattern generalises. It does, with Liechtenstein as the informative
exception — see [[LI-DSG]].

There is no open data portal, no statistics office, no interoperability
framework and no cyber authority.

## Sources

Listed in frontmatter. `efta.int` and `government.nl` were read directly
this pass; `coe.int` and `iso.org` remain bot-walled (403) even with an
honest User-Agent. Wikipedia's dedicated Council of Europe member-states
article, read directly 2026-09-30, supplies the accession date `coe.int`
itself could not.
