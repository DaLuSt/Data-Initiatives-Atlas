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
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-19"
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
    evidence: "Liechtenstein is one of the 46 member states of the Council of Europe, an intergovernmental organisation separate from the European Union (coe.int 'The Council of Europe's 46 member states'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "LI — Liechtenstein (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:LI"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "The European Free Trade Association"
    url: "https://www.efta.int/about-efta/european-free-trade-association"
    publisher: "European Free Trade Association (EFTA)"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# Liechtenstein

> **Sourcing caveat.** Compiled from search-engine results only; the
> cited pages were confirmed to exist but were not read, because the
> working environment blocks page retrieval. `verification: search-only`.

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
| Council of Europe | Member since 1978 |
| EFTA / EEA | Member of [[INTL-EFTA]]; party to [[INTL-EEA-AGREEMENT]] |

> Accession **years** in this table come from general reference
> knowledge rather than from the cited pages, which were not read.
> They are flagged for the re-verification pass along with everything
> else marked `search-only`.

## The third EEA EFTA state, and the smallest

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

Listed in frontmatter.
