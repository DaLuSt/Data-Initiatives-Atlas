---
id: UN-FPOS
type: framework
name: Fundamental Principles of Official Statistics
alternative_names:
  - FPOS
  - UN Fundamental Principles of Official Statistics
description: >
  Global principles setting the foundation for values guiding the production
  and dissemination of official statistics and related metadata that are
  professionally sound, transparent and impartial. Adopted by the UN
  Statistical Commission in 1994 and endorsed by the General Assembly in
  resolution 68/261 (2014).

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2014-01-01
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - UN-UNSD
related_entities: []
relationships:
  - type: maintained-by
    target: UN-UNSD
    source: fact
    evidence: "Confirmed by reading unstats.un.org/fpos/ and its principles_stat_activities.asp page directly (2026-08-28), both published by the United Nations Statistics Division. The main FPOS page states the ten principles' history directly: the Conference of European Statisticians first developed and adopted them in 1991, the UN Statistical Commission adopted them in 1994, and the General Assembly formally endorsed them via resolution 68/261 in 2014, calling them 'a global standard for official statistics.' The methods page corroborates the April 1994 Statistical Commission adoption. The publications sub-page (unstats.un.org/fpos/publications/) returned HTTP 404 this pass and was not read."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Fundamental Principles of Official Statistics"
    url: "https://unstats.un.org/fpos/"
    publisher: "United Nations Statistics Division"
    accessed: "2026-08-28"
  - title: "UNSD — Fundamental Principles of National Official Statistics — publications"
    url: "https://unstats.un.org/fpos/publications/"
    publisher: "United Nations Statistics Division"
  - title: "Principles governing international statistical activities"
    url: "https://unstats.un.org/unsd/methods/statorg/principles_stat_activities/principles_stat_activities.asp"
    publisher: "United Nations Statistics Division"
    accessed: "2026-08-28"
---

# Fundamental Principles of Official Statistics (FPOS)

> **Verified 2026-08-28.** Two of three cited unstats.un.org pages were read
> directly, closing the prior search-only gap. The main FPOS page confirms
> the full 1991 → 1994 → 2014 lineage in its own words, including the exact
> General Assembly resolution number. The publications sub-page returned a
> 404 this pass and was not read.

## Description

The FPOS set the global foundation for the values guiding production and
dissemination of official statistics and related metadata — professionally
sound, transparent and impartial.

Their lineage is unusually well documented and worth recording precisely,
because it runs *upward* from the regional to the global level, which is the
opposite of most chains in this Atlas:

| Year | Step |
|---|---|
| 1991 | Developed and adopted by the Conference of European Statisticians |
| 1994 | Adopted by the UN Statistical Commission |
| 2014 | Formally endorsed by the General Assembly, resolution 68/261 |

`start_date: 2014-01-01` records the General Assembly endorsement year and
is a **placeholder** — the resolution's date was not established. The 1994
and 1991 steps are recorded here in prose rather than as separate entities.

The principles also govern SDG indicator practice: SDG indicators are to be
disaggregated "in accordance with the Fundamental Principles of Official
Statistics".

## A national chain that could be completed

Countries are tracked on whether their statistical legislation aligns with
the FPOS. That makes [[NL-WET-CBS]] — the Dutch statistics act, which the
Atlas records as guaranteeing [[NL-CBS]]'s independence — a candidate
downstream node.

**No relationship is asserted.** No source read states that the Dutch act
implements or aligns with the FPOS. Establishing it would give the Atlas an
international → national chain in the statistics domain, parallel to the
DCAT chain in metadata. Queued.

## Relationships

- Maintained by [[UN-UNSD]].

## Sources

Listed in frontmatter, two of three read directly this pass: unstats.un.org's
own FPOS page (which states the 1991/1994/2014 lineage verbatim) and its
principles-governing-international-statistical-activities page. The
publications sub-page 404'd and was not read.
