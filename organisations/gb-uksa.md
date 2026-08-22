---
id: GB-UKSA
type: organisation
name: UK Statistics Authority
alternative_names:
  - UKSA
  - Statistics Authority
description: >
  Non-ministerial department of the United Kingdom, independent of
  government, which oversees the UK statistical system and reports directly
  to Parliament and the devolved legislatures rather than to ministers. The
  Office for National Statistics is its executive office. It carries the
  United Kingdom's multilateral statistical engagement, including membership
  of the Conference of European Statisticians and its Bureau.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - GB-ONS
  - UN-CES
  - INTL-OECD-CSSP
relationships:
  - type: participates-in
    target: UN-CES
    source: fact
    evidence: "NOT independently re-confirmed 2026-08-22: unece.org returns a bot-defense challenge (403), and the UKSA 'Multilateral Engagement' URL has moved — its replacement (uksa.statisticsauthority.gov.uk/about-the-authority/working-internationally/), read directly, lists UNECE among the bodies UKSA works with but does not name the Conference of European Statisticians or its Bureau specifically. The original claim is retained rather than removed. CAVEAT: the original sources establish that the UNITED KINGDOM is a CES and Bureau member; they do not settle whether the seat is held by the Authority or by the Office for National Statistics, so the same participation is recorded on both and neither claim is exclusive."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Working internationally — UK Statistics Authority"
    url: "https://uksa.statisticsauthority.gov.uk/about-the-authority/working-internationally/"
    publisher: "UK Statistics Authority"
    accessed: "2026-08-22"
  - title: "About us — Office for National Statistics"
    url: "https://www.ons.gov.uk/aboutus"
    publisher: "Office for National Statistics (UK)"
    accessed: "2026-08-22"
  - title: "Bureau of the Conference of European Statisticians (CES)"
    url: "https://unece.org/statistics/ces/bureau-conference-european-statisticians-ces"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
---

# UK Statistics Authority

> **Verified 2026-08-22.** ons.gov.uk's own "About us" page and the UKSA's
> (moved) international-engagement page were read directly. The
> CES/Bureau membership claim could not be re-confirmed this pass — see
> that relationship's evidence — because `unece.org` is bot-walled and the
> UKSA page that originally supported it no longer states it. The claim is
> retained, not removed.

## Description

Confirmed by reading ons.gov.uk's "About us" page (2026-08-22): "We are
independent of ministers and instead report through the UK Statistics
Authority to Parliament and the devolved governments of Scotland, Wales
and Northern Ireland." The UK Statistics Authority oversees
the UK statistical system and reports **to Parliament and the devolved
legislatures rather than to ministers**. [[GB-ONS]] is its executive office.

## Why this entity exists: to resolve a caveat, honestly, by not resolving it

[[GB-ONS]] asserts `participates-in` [[UN-CES]], and its evidence string
carries an explicit warning: *the sources establish that **the UK** is a CES
and Bureau member; whether the seat belongs to the ONS or to the UK
Statistics Authority is not distinguished.* `progress/backlog.md` listed the
Authority as the thing that would settle it.

**It does not settle it.** The sources found describe the Authority's
multilateral engagement and the UK's CES membership without saying which body
holds the seat, so this batch does the only defensible thing: records the
participation on **both**, at `confidence: low` here, with the ambiguity
stated in both evidence strings.

That is worse than a clean answer and better than a confident guess. A reader
following either edge is told the same thing: the UK is a member, and the
Atlas does not know through which body.

## What the structure does say

`part-of` runs from [[GB-ONS]] to here, and that edge **is** well founded —
the ONS's own pages describe it as the Authority's executive office. It is
the first `part-of` edge in the UK batch, and it gives the statistical layer
the two-tier shape the other countries' offices do not have in the Atlas:

| Country | Office | Parent modelled? |
|---|---|---|
| Netherlands | [[NL-CBS]] | no |
| Germany | [[DE-DESTATIS]] | no |
| Belgium | [[BE-STATBEL]] | no |
| Spain | [[ES-INE]] | no |
| Poland | [[PL-GUS]] | no |
| **United Kingdom** | [[GB-ONS]] | **yes — this entity** |

Whether the other five have an equivalent oversight body that the Atlas
simply has not researched is unknown, and is a fair question for a later
pass.

## `coverage: low`

The Authority's founding statute (the Statistics and Registration Service Act
2007 is named in general knowledge but was **not** established from the
sources found), its board, and its relationship to the Office for Statistics
Regulation are unrecorded. The OSR — the Authority's regulatory arm — remains
unmodelled.

## Relationships

- `participates-in` [[UN-CES]] at `confidence: low`, with the ambiguity in
  the evidence.

[[GB-ONS]] carries the `part-of` edge pointing here.

## Sources

Listed in frontmatter.
