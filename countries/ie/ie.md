---
id: IE
type: country
name: Ireland
alternative_names:
  - Éire
  - Republic of Ireland
description: >
  Country anchor entity for Ireland, the tenth national scope covered by the
  Data Initiatives Atlas and its eighth European Union member state. Ireland
  is the only common-law member state in the Atlas, and its Data Protection
  Commission acts as lead supervisory authority under the GDPR's one-stop-shop
  mechanism for a large share of the technology sector established in the
  Union.

level: national
country: IE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-20"
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
    evidence: "Ireland is one of the 27 member states of the European Union, having acceded on 1 January 1973; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
    accessed: "2026-08-20"
  - title: "IE — Ireland (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:IE"
    publisher: "International Organization for Standardization (ISO)"
    accessed: "2026-08-20"
  - title: "Irish Supervisory Authority fines TikTok €530 million and orders corrective measures"
    url: "https://www.edpb.europa.eu/news/irish-supervisory-authority-fines-tiktok-eu530-million-and-orders-corrective-measures_en"
    publisher: "European Data Protection Board (EDPB)"
    accessed: "2026-08-20"
  - title: "NIS2 Directive implementation in Ireland"
    url: "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-ireland"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-20"
---

# Ireland

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says, including its accession date.
> `verification: primary-source`.

## Description

Ireland (ISO 3166-1 alpha-2: **`IE`**) is the **tenth country** in the
Atlas and its **eighth EU member state**, after [[NL]], [[DE]], [[BE]],
[[FR]], [[ES]] and [[PL]] — and alongside [[GB]], [[NO]] and [[CH]], which
are not member states.

## Why Ireland, ahead of larger member states

Two reasons, and neither is size.

**1. The one-stop-shop has a centre, and it is Dublin.**

[[IE-DPC]] is lead supervisory authority under [[EU-GDPR]] Article 56 for a
large share of the technology sector with its main EU establishment in
Ireland. Before this batch the Atlas held **eight** national data protection
authorities and modelled no mechanism connecting any of them — the
one-stop-shop existed nowhere in the graph, even though it is how most
consequential GDPR enforcement in the Union actually happens.

**2. The only common-law member state.**

Every other member state in the Atlas is a civil-law jurisdiction. [[GB]]
brought common law into the Atlas, but as a *former* member. Ireland is the
case where common-law drafting and EU membership coexist — which is why
[[IE-DPA-2018]] gives effect to the GDPR through an Act of the Oireachtas
that reads nothing like [[NL-UAVG]] or [[DE-BDSG]].

## A transposition that has not happened

Ireland missed the **17 October 2024** deadline for [[EU-NIS2]]. It intends
to transpose through the **National Cyber Security Bill**, which was still
not enacted as at the date of this batch — see [[IE-NCS-BILL]], carried as
`status: proposed`.

That makes Ireland the second country in the Atlas with a *pending* cyber
instrument, after [[GB-CSRB]], and the first where the pending instrument is
a **transposition already overdue**. The two are not the same thing:
[[GB-CSRB]] is a sovereign choice about a directive that no longer binds the
UK; [[IE-NCS-BILL]] is a member state late on an obligation.

## EU instruments that apply in Ireland

Recorded as `applies-in` edges on the instruments themselves, in the pattern
established by the Germany batch. See the country index at
`countries/ie/index.md`.

## Not modelled

- **Northern Ireland**, which is in [[GB]] and where the interaction between
  the two jurisdictions after Brexit is substantial and unresearched.
- The **Oireachtas** and the Irish legislative process.
- Any **sub-national** level.

## Sources

Listed in frontmatter.
