---
id: INTL-EEA-JOINT-COMMITTEE
type: organisation
name: EEA Joint Committee
alternative_names: []
description: >
  The institution of the Agreement on the European Economic Area
  responsible for managing the Agreement and taking the decisions that
  incorporate new EU legislation into it, extending it to Iceland,
  Liechtenstein and Norway. It typically meets eight times a year, is
  composed of the ambassadors of the three EEA EFTA states and
  representatives of the Secretariat-General of the European Commission,
  and decides by consensus. Its presidency alternates every six months
  between the EU and an EEA EFTA state, and four subcommittees assist it.
  Decision of the EEA Joint Committee No 154/2018, which incorporated the
  General Data Protection Regulation, is one of its decisions and is
  already an Atlas entity.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 1994-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-EEA-AGREEMENT
  - INTL-EEA-JCD-154-2018
  - EU
  - "NO"
  - IS
  - LI
relationships:
  - type: part-of
    target: INTL-EEA-AGREEMENT
    source: fact
    evidence: "Confirmed verbatim by reading efta.int's own 'EEA Joint Committee' page directly (2026-08-22), fetched with an honest, identifying User-Agent rather than a browser-spoofing one — efta.int returns a bot-defense challenge (403) to a browser User-Agent, but 200s and serves real content to a UA that names itself as a bot, the same pattern tools/reverify.py's own UA gets, and the opposite of every other bot-walled host found this session: 'The EEA Joint Committee is responsible for the management of the EEA Agreement and typically meets eight times a year. It is a forum in which views are exchanged and decisions are taken by consensus to incorporate EU legislation into the EEA Agreement.' The page's own breadcrumb places it under 'EEA Institutions - Two Pillar Structure', confirming it is an institution of the Agreement itself. Corroborated independently by reading en.wikipedia.org/wiki/EEA_Joint_Committee and en.wikipedia.org/wiki/European_Free_Trade_Association directly. Anchor edge under metadata/relationship-types.md §2.3: this Committee is not merely scoped like the Agreement, it is the Agreement's own institution and the mechanism by which the Agreement is amended."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: produces
    target: INTL-EEA-JCD-154-2018
    source: fact
    evidence: "Confirmed by reading efta.int's own 'EEA Joint Committee' page directly (2026-08-22): 'The EEA Joint Committee agrees on the incorporation of a decision into the EEA Agreement, and therefore plays a key role in the EEA decision-making procedure' — and the eur-lex.europa.eu text of the decision itself (already cited on [[INTL-EEA-JCD-154-2018]]) styles itself 'Decision of the EEA Joint Committee No 154/2018 of 6 July 2018'."
    confidence: medium
    valid_from: 2018-07-06
    valid_until: null
  - type: related-to
    target: EU
    source: fact
    evidence: "Confirmed by reading efta.int's own 'EEA Joint Committee' page directly (2026-08-22): 'The EEA Joint Committee is composed of the ambassadors of the EEA EFTA States and representatives of the Secretariat-General of the European Commission. The Presidency of the Committee is held for six months on an alternating basis by the EU and an EEA EFTA State.' The Committee is a joint body of both sides rather than an EU institution, hence `related-to` rather than `part-of`."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EEA Joint Committee"
    url: "https://www.efta.int/eea-relations-eu/eea-institutions-two-pillar-structure/eea-joint-committee"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "EEA Institutions - Two Pillar Structure"
    url: "https://www.efta.int/eea-relations-eu/eea-institutions-two-pillar-structure"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "EEA Joint Committee"
    url: "https://en.wikipedia.org/wiki/EEA_Joint_Committee"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "European Free Trade Association"
    url: "https://en.wikipedia.org/wiki/European_Free_Trade_Association"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# EEA Joint Committee

> **Verified 2026-08-22, and a correction to standing guidance.**
> `efta.int` was treated as bot-walled (403) in every earlier pass this
> session, on the strength of a browser-spoofing User-Agent. Fetched
> instead with an honest, identifying User-Agent — the same kind
> `tools/reverify.py` sends — `efta.int` returns real content: 200, not
> 403. This is the reverse of the pattern found for `eur-lex.europa.eu`
> and `europarl.europa.eu` earlier this session (those were wrongly
> marked blocked full stop); here the block was specifically a
> browser-User-Agent challenge. `eftasurv.int` (a JavaScript
> single-page application) and `eftacourt.int` (which serves only a live
> case-docket regardless of path) were re-tested the same way and remain
> genuinely unreadable — that finding holds.

## Description

Confirmed verbatim by reading efta.int's own "EEA Joint Committee" page
directly (2026-08-22): "The EEA Joint Committee is responsible for the
management of the EEA Agreement and typically meets eight times a year.
It is a forum in which views are exchanged and decisions are taken by
consensus to incorporate EU legislation into the EEA Agreement. The EEA
Joint Committee is composed of the ambassadors of the EEA EFTA States
and representatives of the Secretariat-General of the European
Commission. The Presidency of the Committee is held for six months on an
alternating basis by the EU and an EEA EFTA State. Four subcommittees
assist the Joint Committee on the free movement of goods; the free
movement of capital and services, including company law; the free
movement of persons; and horizontal and flanking policies."

## The instrument this closes

[[INTL-EEA-AGREEMENT]]'s own entity has said, since it was created, that
its rules are "continuously updated by adding new EU legislation through
decisions of the EEA Joint Committee" — while the Committee itself was
listed as "not modelled". [[INTL-EEA-JCD-154-2018]], the decision that
incorporated [[EU-GDPR]], already existed as an Atlas entity describing
one output of this Committee, without the Committee itself being one. The
`produces` edge above closes that gap directly: the graph now shows the
body, not only what it made.

## Not modelled

- The **EEA Council**, the **Standing Committee of the EFTA States**, the
  **EEA Joint Parliamentary Committee** and the **EEA Consultative
  Committee** — the other four bodies efta.int itself lists alongside
  this Committee under "EEA Institutions - Two Pillar Structure".
- Individual **Joint Committee decisions** other than 154/2018, and the
  **four subcommittees** that prepare its work. Cataloguing the full set
  of decisions is a large undertaking already noted on
  [[INTL-EEA-AGREEMENT]].
- The **Rules of Procedure** (Decision No 1/94, as amended by Decision
  No 24/2005) that govern how the Committee itself operates.

## Sources

Listed in frontmatter. `efta.int`'s own page and the "Two Pillar
Structure" overview page were both read directly this pass with an
honest User-Agent; both Wikipedia articles corroborate independently.
