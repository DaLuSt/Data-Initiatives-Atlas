---
id: EU-PUBLIC-ADMIN-DATA-SPACE
type: data-space
name: Common European data space for public administration
alternative_names:
  - Public administration data space
  - Public administrations data space
description: >
  One of the fourteen common European data spaces, covering public
  administrations. It is named among the strategic sectors of the European
  Data Strategy and sits closest of the fourteen to the Atlas's own
  subject matter.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains: 
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-COMMON-DATA-SPACES
  - EU-INTEROPERABLE-EUROPE-ACT
  - EU-SDG
  - EU-TOURISM-DATA-SPACE
  - EU-MEDIA-DATA-SPACE
relationships:
  - type: part-of
    target: EU-COMMON-DATA-SPACES
    source: fact
    evidence: "Public administration is one of the fourteen common European data spaces identified in the Commission's January 2024 staff working document (SWD(2024) 21 final of 24.1.2024; digital-strategy.ec.europa.eu 'Common European data spaces'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: EU-INTEROPERABLE-EUROPE-ACT
    source: interpretation
    evidence: "PARTIALLY NARROWS discovery/unresolved.md row #121. data.europa.eu's own article 'Interoperability in data spaces: Building Europe's digital future' (read directly, 2026-09-18) states, of common European data spaces generally: 'Initiatives such as the SEMIC Support Centre and Interoperable Europe Act provide tools and frameworks to support compatibility.' This is a general statement about data spaces collectively, not one naming the public administration data space specifically, so it is recorded as `source: interpretation` (this data space is one of the fourteen the statement describes) rather than `fact`. The EIF and EU-SDG halves of the row's question remain unanswered: no source read connects either to this entity, specifically or generally."
    confidence: low
    valid_from: null
    valid_until: null
  - type: governed-by
    target: EU-SDG
    source: fact
    evidence: "CLOSES THE EU-SDG HALF of discovery/unresolved.md row #121. The Commission's own 'Common European data spaces' overview page (already cited above), read directly, lists 'OOTS - Once Only Technical System' under the 'Public administration' data space heading — naming OOTS as one of the entries constituting this data space. The Commission's own news article 'Once-Only Technical System: key for the creation of the first European data space' (read directly, already cited on [[EU-SDG]]) states OOTS was 'Established by the Single Digital Gateway Regulation (SDGR)' and that 'The SDGR provides the legal framework for the creation of a European data space for public administrations.' Together these name the SDGR as the legal basis for the component the Commission itself lists under this data space — a fact-level connection, not an inference."
    confidence: high
    valid_from: "2020-12-12"
    valid_until: null

sources:
  - title: "SWD(2024) 21 final — Staff working document on common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/library/staff-working-document-data-spaces"
    publisher: "European Commission"
  - title: "Common European data spaces"
    url: "https://digital-strategy.ec.europa.eu/en/policies/data-spaces"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "Interoperability in data spaces: Building Europe's digital future"
    url: "https://data.europa.eu/en/news-events/news/interoperability-data-spaces-building-europes-digital-future"
    publisher: "data.europa.eu — Publications Office of the European Union"
    accessed: "2026-09-18"
  - title: "Once-Only Technical System: key for the creation of the first European data space"
    url: "https://commission.europa.eu/news-and-media/news/once-only-technical-system-key-creation-first-european-data-space-2022-07-20_en"
    publisher: "European Commission"
    accessed: "2026-09-19"
  - title: "Public Procurement Data Space (PPDS)"
    url: "https://www.public-procurement-data-space.europa.eu/en"
    publisher: "European Commission — DG GROW"
    accessed: "2026-09-19"
  - title: "Webinar: European data spaces for public administrations and the role of data.europa.eu (7 June 2023)"
    url: "https://data.europa.eu/sites/default/files/course/European%20data%20spaces%20for%20public%20administrations%20and%20data.europa.eu_.pdf"
    publisher: "data.europa.eu Academy (European Commission DG CNECT, DG GROW, Data Spaces Support Centre)"
    accessed: "2026-09-20"
---

# Common European data space for public administration

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Narrowed 2026-09-18** (`discovery/unresolved.md` row #121): one of the
> temptations recorded below now has a thin, general source. See "One
> connection, thinly sourced" below — the row is narrowed, not closed.
>
> **Narrowed further 2026-09-19**: the [[EU-SDG]] question is now answered
> — see "The Single Digital Gateway, found" below. Only the [[EU-EIF]]
> question remains fully open.
>
> **Deployment project found 2026-09-19** (`discovery/unresolved.md` row
> #125): the Public Procurement Data Space (PPDS), live since 24 September
> 2024. See "PPDS, found" below. `coverage` promoted to `medium`.
>
> **Closed 2026-09-20** (`discovery/unresolved.md` row #121): the EIF
> question, the row's last open piece, is now a confirmed documented
> negative rather than an unresearched gap. A 38-slide EU webinar deck
> dedicated specifically to this data space and PPDS — covering the Data
> Governance Act, Data Act, PPDS's own architecture and the Data Spaces
> Support Centre's role in detail — was read in full and never mentions
> EIF once. See "The EIF question, closed as a documented negative"
> below.

## Description

One of the fourteen common European data spaces, covering public administrations.
It is named among the strategic sectors of the European Data Strategy and sits closest of the fourteen to the Atlas's own subject matter.

## The one closest to the rest of this Atlas

Public administration is the sector the Atlas covers most densely: 232 of its
entities carry [[DOMAIN-GOVERNMENT]], making it by a wide margin the largest
node in the association layer.

So this data space is the natural meeting point between the data-space layer
and everything else the Atlas holds — [[EU-INTEROPERABLE-EUROPE-ACT]],
[[EU-EIF]], the national interoperability frameworks, the open data portals.

**Most of those connections remain unasserted**, and this is exactly the
entity where a repository would be most tempted to draw them. All three
temptations recorded here are now resolved, two positively and one as a
documented negative:

- [x] How does the public administration data space relate to [[EU-EIF]]
  specifically? **Closed 2026-09-20 as a documented negative** — see below.
- [x] Does it build on [[EU-SDG]], the Single Digital Gateway? **Answered
  2026-09-19** — see below.

## One connection, thinly sourced — 2026-09-18

The third — [[EU-INTEROPERABLE-EUROPE-ACT]] — now has a source, though a
thin one. data.europa.eu's own article "Interoperability in data spaces:
Building Europe's digital future," read directly, states of common
European data spaces generally: *"Initiatives such as the SEMIC Support
Centre and Interoperable Europe Act provide tools and frameworks to
support compatibility."*

This names the Act specifically, but describes data spaces **collectively**
rather than this one by name — the Commission's own dedicated page for
this data space (fetched earlier and cited above) says nothing about the
Act. The edge is recorded at `source: interpretation`, `confidence: low`:
this entity is one of the fourteen the general statement describes, but
the statement itself does not single it out. The EIF and SDG questions
above remain fully open — no source read connects either to data spaces
in general or to this one specifically.

The remaining question is in `discovery/unresolved.md`.

## The Single Digital Gateway, found — 2026-09-19

The Commission's own "Common European data spaces" overview page (already
cited above, read directly) lists three things under the "Public
administration" heading, one of which is **OOTS — Once Only Technical
System**. The Commission's own account of OOTS, read directly (already
cited on [[EU-SDG]]), states OOTS was "Established by the Single Digital
Gateway Regulation (SDGR)" and that "The SDGR provides the legal framework
for the creation of a European data space for public administrations."

That names [[EU-SDG]] as the legal basis for a component the Commission's
own page lists under this data space — recorded as `governed-by`,
`confidence: high`, since both statements are read directly rather than
inferred from proximity. OOTS itself is not modelled as a separate Atlas
entity (see "Not modelled" below).

## The EIF question, closed as a documented negative — 2026-09-20

The [[EU-EIF]] question was checked twice from independent angles and
found negative both times. First, a search (2026-09-19) of the
Interoperable Europe Portal's own "Data Spaces" page found no mention of
EIF in its data-spaces content. Second, and more thoroughly this pass: a
38-slide European Commission / Data Spaces Support Centre webinar deck
titled "European data spaces for public administrations and the role of
data.europa.eu" (7 June 2023), read in full page by page, is dedicated
specifically to this data space and its flagship deployment, PPDS. It
covers the European Data Strategy, the Data Governance Act's four
pillars, the Data Act's scope, the "data spaces are fish markets, not
data lakes" framing, PPDS's own architecture and roadmap, and the Data
Spaces Support Centre's goals, assets and 17-70 engaged initiatives —
never once naming the European Interoperability Framework.

This is now recorded as a genuine, checked-and-negative finding rather
than an unresearched gap: two independent Commission-published sources,
one general (the Interoperable Europe Portal) and one specific
(a dedicated deep-dive on this exact data space), both omit EIF entirely.
No relationship is asserted, and none should be inferred from proximity —
this is the same discipline the Atlas applies to the
Plattform-Industrie-4.0↔Manufacturing-X and INSPIRE↔UN-GGIM refusals.

## PPDS, found — 2026-09-19

`discovery/unresolved.md` row #125 asked for a deployment project for
this data space. One is now sourced: the Commission's own "Common
European data spaces" overview page, re-read directly, lists three items
under the "Public administration" heading — OOTS (above), the **European
Legal Data Space**, and the **Public Procurement Data Space (PPDS)**. PPDS's
own official site, read directly, describes it as a service letting
"policy makers, public buyers, companies, and other stakeholders access
public procurement information ... unprecedented at the European level,"
covering roughly **250,000 public authorities** whose procurement spend
totals **€2.5 trillion** (about 15% of EU GDP) annually. It went live on
**24 September 2024**, launched at a "PPDS Day 2024" event organised by
DG GROW (Internal Market, Industry, Entrepreneurship and SMEs), which
operates it.

The **European Legal Data Space**, the third item named on the same
Commission page, was not independently researched this pass.

## ⚠ `coverage`, promoted to medium

Governance and operator detail beyond OOTS's SDGR basis and PPDS's own
DG GROW role remain unestablished, so `coverage` moves from `low` to
`medium` rather than `high`.

## Not modelled

- **OOTS (Once Only Technical System)** as its own entity — it is the
  component the Commission's own page lists under this data space,
  described in prose here rather than as a separate node.
- **PPDS (Public Procurement Data Space)** as its own entity, for the same
  reason, matching the DEPLOYTOUR/TEMS precedent set on
  [[EU-TOURISM-DATA-SPACE]] and [[EU-MEDIA-DATA-SPACE]].
- The **European Legal Data Space**, the third item named on the
  Commission's overview page — not independently researched this pass.

## Sources

Listed in frontmatter. The data.europa.eu article was added and read
directly 2026-09-18; the Commission's OOTS article was added 2026-09-19
(already read directly on [[EU-SDG]] since 2026-08-28); PPDS's own site
added and read directly 2026-09-19.
