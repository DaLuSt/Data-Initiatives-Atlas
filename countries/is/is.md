---
id: IS
type: country
name: Iceland
alternative_names:
  - Iceland
  - Ísland
  - Lýðveldið Ísland
description: >
  Country anchor entity for Iceland, a member of the European Free Trade
  Association and a party to the Agreement on the European Economic Area,
  and not a member of the European Union. It is a base anchor: it carries
  the country's position in the European legal and institutional
  frameworks so that entities scoped to it have somewhere to attach. Its
  first national entities are the data protection authority Persónuvernd
  and Act No. 90/2018 on data protection and the processing of personal
  data.

level: national
country: IS
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
    evidence: "Confirmed 2026-09-30: coe.int itself remains genuinely bot-walled (403) even with an honest, identifying User-Agent, but Wikipedia's own dedicated 'Member states of the Council of Europe' article, read directly, gives a sourced per-country accession table: Iceland joined 7 March 1950. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: high
    valid_from: "1950-03-07"
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
  - title: "IS — Iceland (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:IS"
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

# Iceland

> **Verified 2026-08-22.** `efta.int` and `government.nl` were both read
> directly and confirm Iceland's EFTA and EEA membership verbatim.
> `coe.int` and `iso.org` remain bot-walled (403) even with an honest,
> identifying User-Agent — unlike `efta.int`, whose apparent block
> earlier this session turned out to be User-Agent-specific, these two
> are genuinely closed and stay cited but unread.
>
> **Confirmed 2026-09-30**: the Council of Europe membership claim below
> is now sourced with an accession date — 7 March 1950 — from
> Wikipedia's dedicated Council of Europe article, since `coe.int` itself
> remains bot-walled.

## Description

Iceland (ISO 3166-1 alpha-2: **`IS`**) is a country anchor, created so
that entities scoped to it have somewhere to attach. Two Icelandic entities
are now modelled: [[IS-PERSONUVERND]] and [[IS-PERSONUVERNDARLOG]].

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Not a member, not a candidate |
| Euro area | No |
| Schengen area | Member |
| Council of Europe | Member since 7 March 1950 |
| EFTA / EEA | Member of [[INTL-EFTA]]; party to [[INTL-EEA-AGREEMENT]] |

> The **EFTA/EEA row** is directly confirmed — see below. The **Council of
> Europe row** is now sourced too, from Wikipedia's dedicated member-states
> article (2026-09-30), since `coe.int` itself remains bot-walled.

## The second EEA EFTA state in the Atlas

Confirmed by reading efta.int's own "The European Free Trade
Association" page directly (2026-08-22, fetched with an honest,
identifying User-Agent — efta.int returns a bot-defense challenge to a
browser User-Agent but real content to one that names itself as a bot):
"The European Free Trade Association (EFTA) is the intergovernmental
organisation of Iceland, Liechtenstein, Norway and Switzerland," and
"three of the four EFTA States – Iceland, Liechtenstein and Norway – in
a single market" under the EEA Agreement. Corroborated by reading
government.nl's own "EU, EEA, EFTA and Schengen Area countries" page
directly: Iceland is listed among both "The 30 EEA countries" and "The
4 EFTA countries."

Iceland is a party to [[INTL-EEA-AGREEMENT]] and a member of
[[INTL-EFTA]], not of the European Union — the same position as [[NO]], and
described at length on that entity.

EU acts do not apply in Iceland by force of Union law. They take effect only
once incorporated into the EEA Agreement by a decision of the **EEA Joint
Committee** and then implemented in Icelandic law, which is why no
`applies-in` edge from an EU instrument points here.

One such decision is now modelled: [[INTL-EEA-JCD-154-2018]], which
incorporated [[EU-GDPR]] and carries `applies-in` to [[IS]], [[LI]] and
[[NO]].

Iceland, [[LI]] and [[NO]] are the three **EEA EFTA states**; [[CH]] is the
fourth EFTA member and is in neither the EU nor the EEA.

## What this anchor does not yet carry

The **data protection layer only**. [[IS-PERSONUVERND]] and
[[IS-PERSONUVERNDARLOG]] were added on 2026-08-21 to test whether the
Norwegian EEA pattern generalises — see [[IS-PERSONUVERNDARLOG]] for the
three-way comparison, and `discovery/research-queue.md` for what is still
missing.

There is no open data portal, no statistics office, no interoperability
framework and no cyber authority. Iceland is also the only member of
[[INTL-NIIS]] with no X-Road deployment modelled.

## Sources

Listed in frontmatter. `efta.int` and `government.nl` were read directly
this pass; `coe.int` and `iso.org` remain bot-walled (403) even with an
honest User-Agent. Wikipedia's dedicated Council of Europe member-states
article, read directly 2026-09-30, supplies the accession date `coe.int`
itself could not.
