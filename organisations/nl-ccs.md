---
id: NL-CCS
type: organisation
name: Centrale Commissie voor de Statistiek
alternative_names:
  - CCS
description: >
  Former independent supervisory body (zelfstandig bestuursorgaan) for
  Statistics Netherlands, established under the Wet op het CBS of 2003
  alongside the Director-General of Statistics, with which it shared
  independent governance of the newly autonomous CBS. It independently
  approved the CBS's multi-year and annual work programme, supervised
  its operations, was involved in preparing its budget and annual
  accounts (which the Director-General set "in agreement with the
  CCS"), and had special oversight of limiting administrative burden,
  avoiding unwanted market competition, and microdata access. A 2015
  legislative proposal abolished the CCS as a separate independent
  body, on the grounds that one zbo supervising another was an
  unnecessarily heavy governance structure; its powers transferred to
  the Director-General or the Minister. The change took effect 1
  January 2017, alongside the creation of a narrower Raad van advies
  (Advisory Board) with a purely advisory role.

level: national
country: NL
region: EU

status: superseded
confidence: medium
coverage: low
verification: primary-source

start_date: 2003-01-01
end_date: 2017-01-01
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-WET-CBS
  - NL-CBS
relationships:
  - type: governed-by
    target: NL-WET-CBS
    source: fact
    evidence: "Confirmed by reading eerstekamer.nl's own bill page for the Wet op het CBS directly (2026-08-27, carried on NL-WET-CBS's own entity): the 2003 act establishing CBS as a zelfstandig bestuursorgaan gave the CCS independent governance of the work programme alongside the Director-General. Confirmed independently by reading zoek.officielebekendmakingen.nl's own text of Kamerstuk 34248, nr. 3 directly (2026-09-04), the 2015 legislative proposal to abolish the CCS: it describes the CCS's original role as approving the DG CBS's multi-year programmes, annual reports and budgets, calling the two-zbo structure 'een onnodig zware inrichting' (an unnecessarily heavy governance structure)."
    confidence: high
    valid_from: 2003-01-01
    valid_until: 2017-01-01

sources:
  - title: "Kamerstuk 34248, nr. 3 — Herpositionering zelfstandige bestuursorganen CBS"
    url: "https://zoek.officielebekendmakingen.nl/kst-34248-3.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
    accessed: "2026-09-04"
  - title: "Raad van advies"
    url: "https://www.cbs.nl/nl-nl/over-ons/organisatie/raad-van-advies"
    publisher: "Centraal Bureau voor de Statistiek (CBS)"
    accessed: "2026-09-04"
---

# Centrale Commissie voor de Statistiek (CCS)

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged the CCS as [[NL-CBS]]'s
> statutory supervisor, unmodelled — and [[NL-WET-CBS]]'s own file had
> already flagged the same gap. Reading the actual 2015 legislative
> proposal directly this pass found the CCS was **abolished**, not
> merely unmodelled — this entity records a historical body, `status:
> superseded`, not a current one.

## Description

The CCS was CBS's independent supervisory body, established alongside
the Director-General of Statistics under the **Wet op het CBS of
2003**, which gave CBS its status as a zelfstandig bestuursorgaan
(independent administrative body, zbo). Reading the 2015 legislative
proposal to abolish it directly: the CCS independently approved the
CBS's multi-year and annual work programmes, supervised its
operations, took part in setting its budget and annual accounts —
which the Director-General fixed **"in overeenstemming met de CCS"**
(in agreement with the CCS) — and held special oversight of
administrative-burden limits, unwanted market competition, and
microdata access.

## Abolished, not renamed

Reading `zoek.officielebekendmakingen.nl`'s own text of **Kamerstuk
34248, nr. 3** directly: the government concluded that having one zbo
(the CCS) supervise another (CBS itself) was **"een onnodig zware
inrichting"** (an unnecessarily heavy governance structure), and
proposed abolishing the CCS outright, transferring its powers to the
Director-General or the Minister. This is a genuine abolition, not the
kind of rename-in-place the Atlas records for bodies like [[DE-BMV]] or
[[BE-DIGITAAL-VLAANDEREN]] — the CCS's oversight function did not
continue under a new name with the same powers.

The change took effect **1 January 2017**, per corroborating secondary
reporting not independently fetched this pass. A narrower **Raad van
advies** (Advisory Board) now exists at CBS — confirmed by reading
`cbs.nl`'s own current page directly, which describes it advising the
Director-General on request or on its own initiative, and recommending
candidates when the Director-General position is vacant — but that
page does not itself state the CCS connection or a founding date, so
no relationship or succession is asserted between the CCS and the
Raad van advies. The Raad van advies is not separately modelled: its
role is materially narrower than the CCS's own supervisory powers.

## Relationships

- `governed-by` [[NL-WET-CBS]] — historical, `valid_until: 2017-01-01`.

## Sources

Listed in frontmatter, both read directly this pass.
