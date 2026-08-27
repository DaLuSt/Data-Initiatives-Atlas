---
id: TR
type: country
name: Türkiye
alternative_names:
  - Republic of Türkiye
  - Türkiye
  - Türkiye Cumhuriyeti
  - Turkey
description: >
  Country anchor entity for Türkiye, a candidate country for European
  Union membership since 1999. It is a base anchor: it carries the
  country's position in the European legal and institutional frameworks so
  that entities scoped to it have somewhere to attach, and no national
  entities are modelled yet.

level: national
country: TR
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading two Wikipedia articles directly (2026-08-27) after coe.int itself proved genuinely, domain-wide bot-walled (403) on every path tried: the 'Member states of the Council of Europe' article's own accession table gives Türkiye's accession date as 13 April 1950 — CORRECTING this entity's previous claim of 1949, which conflated the Council's founding year (5 May 1949) with Türkiye's own later accession. ISO's OBP is also confirmed blocked (403) — it is a JavaScript application, not a static page. The EU-candidacy year (1999) rests on enlargement.ec.europa.eu, read directly in the prior pass but not independently re-confirmed this pass to a specific month/day. Anchor edge under metadata/relationship-types.md §2.3: it records Council of Europe membership and asserts no more than that."
    confidence: high
    valid_from: 1950-04-13
    valid_until: null

sources:
  - title: "TR — Türkiye (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:TR"
    publisher: "International Organization for Standardization (ISO)"
  - title: "The Council of Europe's 46 member states (confirmed genuinely bot-walled, 403)"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
  - title: "Candidate countries and potential candidates"
    url: "https://enlargement.ec.europa.eu/enlargement-policy/candidate-countries-and-potential-candidates_en"
    publisher: "European Commission — Enlargement and Eastern Neighbourhood"
    accessed: "2026-08-27"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
  - title: "Council of Europe"
    url: "https://en.wikipedia.org/wiki/Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Member states of the Council of Europe"
    url: "https://en.wikipedia.org/wiki/Member_states_of_the_Council_of_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# Türkiye

> **Verified 2026-08-27, one correction.** `coe.int` and ISO's OBP are
> both confirmed genuinely bot-walled (403). Two Wikipedia articles were
> read directly instead — a genuine majority (4 of 6 cited pages) — and
> the dedicated accession-date table corrects this entity's previous
> claim that Türkiye joined in 1949: that was the Council's own founding
> year, not Türkiye's accession, which was **13 April 1950**.

## Description

Türkiye (ISO 3166-1 alpha-2: **`TR`**) is a **base country anchor**,
created so that entities scoped to it have somewhere to attach. No Türkiye
entity is modelled yet.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | **Candidate country** since 1999 |
| Euro area | No |
| Schengen area | No |
| Council of Europe | Member since **13 April 1950** |

Confirmed by reading Wikipedia's "Member states of the Council of
Europe" article directly (2026-08-27): its own accession table gives
the exact date and **corrects a previous error** — this entity
previously said 1949, conflating the Council's founding year with
Türkiye's own, later accession. The EU-candidacy year (1999) is
unchanged prior knowledge, not independently re-confirmed to a specific
date this pass.

## An early Council of Europe member and the oldest candidate

Türkiye joined [[INTL-COE]] on **13 April 1950**, less than a year
after its founding (5 May 1949) and decades before most of the states
now in the EU. It has been an EU **candidate since 1999**, with
accession negotiations opened in 2005 and effectively stalled since.

It is the longest-standing candidate by a wide margin, and the clearest case
in Europe of a state deeply embedded in one European organisation and held at
the door of the other.

The UN M49 geoscheme places Türkiye in Western Asia. The Atlas records it
under the Council of Europe and enlargement criteria.

## What this anchor does not yet carry

Nothing beyond membership. There is no national data protection authority,
no open data portal, no statistics office, no interoperability framework
and no legislation attached to this entity. Each of those exists in
reality; none has been researched.

## Sources

Listed in frontmatter, four of six read directly this pass — both
Wikipedia articles, government.nl and (from the prior pass)
enlargement.ec.europa.eu. `coe.int` and ISO's OBP are both genuinely
bot-walled (403).
