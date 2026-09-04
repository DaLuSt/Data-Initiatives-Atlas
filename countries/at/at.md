---
id: AT
type: country
name: Austria
alternative_names:
  - Republic of Austria
  - Österreich
  - Republik Österreich
description: >
  Country anchor entity for Austria, a member state of the European Union
  since 1 January 1995. It is a base anchor: it carries the country's
  position in the European legal and institutional frameworks so that
  entities scoped to it have somewhere to attach, and no national entities
  are modelled yet.

level: national
country: AT
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Austria is one of the 27 member states of the European Union, having acceded on 1 January 1995; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "AT — Austria (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:AT"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-08-20"
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-20"
  - title: "The Council of Europe's 46 member states"
    url: "https://www.coe.int/en/web/portal/46-members-states"
    publisher: "Council of Europe"
    accessed: "2026-08-20"
  - title: "Timeline — Joining the euro area"
    url: "https://www.consilium.europa.eu/en/policies/join-the-euro-area/timeline-joining-the-euro-area/"
    publisher: "Council of the European Union"
    accessed: "2026-08-20"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
    accessed: "2026-08-20"
---

# Austria

> **Verified 2026-08-26.** EU-membership sourcing unchanged since
> 2026-08-20. This pass fixed a stale claim below: the anchor said no
> Austria entity was modelled, which stopped being true once
> [[AT-BRZ]], [[AT-DATA-GV-AT]], [[AT-DSB]], [[AT-ID-AUSTRIA]] and
> [[AT-STATISTIK]] were added, none of which had updated the anchor.

## Description

Austria (ISO 3166-1 alpha-2: **`AT`**) is a **base country anchor**. It
now anchors five entities: a federal IT provider, a national open data
portal, a national digital identity, a data protection authority and a
statistical office.

## Position in the European frameworks

| Framework | Status |
|---|---|
| European Union | Member state since **1 January 1995** |
| Euro area | Since **1 January 1999** |
| Schengen area | Member |
| Council of Europe | Member since 1956 |
| EEA | Through EU membership |

> Accession dates in this table were confirmed against the Union's own
> list of member states on 2026-08-20.

## A former EFTA state

Austria was one of the seven founding members of [[INTL-EFTA]]'s
predecessor arrangement in 1960 and left for the European Union in 1995,
alongside Finland and Sweden. That direction of travel is the norm: of
EFTA's original seven, only [[NO]] and [[CH]] are still outside the EU.

Austria is a **federal republic** of nine *Bundesländer*. It is therefore the
fourth Atlas country — after [[DE]], [[BE]] and [[ES]] — whose sub-national
tier the `level` vocabulary cannot represent.

## What this anchor does not yet carry

No interoperability framework attached to this entity. Its legislation
gap narrowed 2026-09-04: [[AT-EGOVG]], the E-Government-Gesetz behind
[[AT-ID-AUSTRIA]]'s E-ID function, is now modelled — see that entity for
how a claimed four-statute legal basis turned out, on direct reading, to
be one statute the other three merely cite.

No EU instrument in the Atlas carries `applies-in` → [[AT]] yet.
That is a gap rather than a finding: as a member state, every
directly applicable EU regulation the Atlas holds does apply here.

## Sources

Listed in frontmatter.
