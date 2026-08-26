---
id: BE-VL-BESTUURSDECREET-2021
type: law
name: Decreet van 2 juli 2021 tot wijziging van het Bestuursdecreet van 7 december 2018
alternative_names:
  - Vlaams open data-decreet
  - Flemish Open Data Decree
description: >
  Decree of the Flemish Parliament of 2 July 2021 amending the Bestuursdecreet
  of 7 December 2018, published in the Belgian Official Gazette on 8 July 2021
  at pages 68914-68923. It transposes Directive (EU) 2019/1024 on open data
  and the re-use of public sector information for the Flemish Community and
  Region, rewriting Chapter 4 of the Bestuursdecreet on open data and the
  re-use of public sector information and inserting a new Section 2/1 on
  research data. The amended provisions entered into force on 17 July 2021,
  the directive's transposition deadline.

level: subnational
country: BE
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2021-07-17
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE
  - EU-OPEN-DATA-DIRECTIVE
  - BE-HERGEBRUIK-WET-2023
  - BE-BRU-ORDONNANCE-2021
  - BE-WAL-DECRET-2022
relationships:
  - type: implements-requirement-from
    target: EU-OPEN-DATA-DIRECTIVE
    source: fact
    evidence: "Confirmed by reading the annotated Codex Vlaanderen text directly (2026-08-26): the table of contents shows 'HOOFDSTUK 4. Open data en hergebruik van overheidsinformatie (verv. decr. 2 juli 2021, art. 14, I: 17 juli 2021)', and Article I.2 explicitly states the decree transposes 'richtlijn (EU) 2019/1024'. The amendments were published in the Belgisch Staatsblad on 8 July 2021 and entered into force 17 July 2021. The EUR-Lex national-implementing-measures register, also read directly, independently lists a '2 July 2021 decree amending the Administrative Decree of 7 December 2018' among Belgium's measures for this Directive."
    confidence: high
    valid_from: 2021-07-17
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "Confirmed by reading the annotated Codex Vlaanderen text directly (2026-08-26): the decree is an act of the Flemish Parliament amending the Bestuursdecreet, which applies within the Flemish Community and Region, constituent units of Belgium. Anchor edge under metadata/relationship-types.md §2.3; the Atlas has no sub-national anchor entities, so a subnational instrument anchors to its state."
    confidence: medium
    valid_from: 2021-07-17
    valid_until: null

sources:
  - title: "Bestuursdecreet van 7 december 2018 — geannoteerde tekst (Codex Vlaanderen)"
    url: "https://codex.vlaanderen.be/PrintDocument.ashx?id=1030009&geannoteerd=true"
    publisher: "Vlaamse overheid — Codex Vlaanderen"
    accessed: "2026-08-26"
  - title: "Bestuursdecreet — Codex Vlaanderen (document 1030009)"
    url: "https://codex.vlaanderen.be/PrintDocument.ashx?id=1030009"
    publisher: "Vlaamse overheid — Codex Vlaanderen"
  - title: "Directive (EU) 2019/1024 — national implementing measures"
    url: "https://eur-lex.europa.eu/legal-content/nl/NIM/?uri=oj:JOL_2019_172_R_0003"
    publisher: "EUR-Lex — Publications Office of the European Union"
    accessed: "2026-08-26"
---

# Flemish Open Data Decree (2 July 2021)

> **Verified 2026-08-26.** Both the annotated Codex Vlaanderen text and the
> EUR-Lex national implementing measures register were read directly, and
> both independently confirm the transposition, the article-level detail,
> and the entry-into-force date. `verification: primary-source`.

## Description

A decree of the **Flemish Parliament** of **2 July 2021**, published in the
*Belgisch Staatsblad* on 8 July 2021 at pages 68914–68923. It amends the
**Bestuursdecreet of 7 December 2018** to transpose
[[EU-OPEN-DATA-DIRECTIVE]] for the Flemish Community and Region:

| Change | Article | In force |
|---|---|---|
| Chapter 4 — open data and the re-use of public sector information | Art. 14 | 17 July 2021 |
| New Section 2/1 — research data | Art. 26 | 17 July 2021 |

## The first `level: subnational` entity in the Atlas

This entity exists because the `level` vocabulary changed on 2026-08-21.

`level: regional` in this Atlas means **supra**-national — it is what all 68
EU-scoped entities carry — so there was no value for a Belgian Region or
Community, and [[BE-HERGEBRUIK-WET-2023]] recorded all three sub-federal
instruments in prose while modelling none of them. The gap had blocked four
queued items across three countries since the Belgium batch.

`level: local` was the tempting shortcut and would have been wrong: this is
**primary legislation of a constituent state with its own parliament**, not a
municipal by-law. `subnational` was added for exactly this tier. See
`metadata/controlled-vocabularies.md` §`level`.

## Adopted a fortnight early, in force exactly on the deadline

[[BE-HERGEBRUIK-WET-2023]] says Flanders *"met the deadline"* because the
decree of 2 July 2021 *"preceded 17 July 2021 by a fortnight"*. The
annotated Codex text sharpens that: the decree was **adopted** on 2 July, and
its open-data provisions **entered into force on 17 July 2021** — the
transposition deadline itself, to the day.

So Flanders did not transpose early. It transposed exactly on time, having
legislated a fortnight before, which is a different and more deliberate thing.

## Belgium answered for the whole territory anyway

Flanders being on time did not help. Belgium was referred to the Court of
Justice in February 2023 because the **federal** legislator had not acted, and
a member state answers for all of its territory. [[BE-HERGEBRUIK-WET-2023]],
the federal act, was not published until **23 January 2024** — roughly
**thirty months** after this decree was already in force.

That gap is the whole reason the sub-federal instruments were worth modelling:
the Atlas showed Belgium as twenty-nine months late, and three quarters of the
country was not.

## Relationships

- `implements-requirement-from` [[EU-OPEN-DATA-DIRECTIVE]] — the same type the
  federal act and the other two sub-federal instruments carry.
- `applies-in` [[BE]]. The Atlas has no entity for the Flemish Region itself,
  so a subnational instrument anchors to its state. What the edge asserts is
  scope, not that the decree applies throughout Belgium — the body above says
  precisely where it applies.

## Sources

Both read directly this pass — the annotated Bestuursdecreet on Codex
Vlaanderen and the EUR-Lex register of national implementing measures,
which corroborate each other.
