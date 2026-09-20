---
id: DE-BSIG
type: law
name: BSI-Gesetz
alternative_names:
  - BSIG
  - Gesetz über das Bundesamt für Sicherheit in der Informationstechnik
  - Act on the Federal Office for Information Security
description: >
  German federal act constituting the Bundesamt für Sicherheit in der
  Informationstechnik and defining the scope of its tasks, including its
  role under § 4 BSIG as the central reporting point for IT security. The
  current BSI-Gesetz entered into force on 20 August 2009, superseding the
  1991 BSI-Errichtungsgesetz that originally created the office. It was
  substantially expanded by the IT-Sicherheitsgesetz (2015) and
  IT-Sicherheitsgesetz 2.0 (2021), and comprehensively revised by the
  NIS-2-Umsetzungsgesetz with effect from 6 December 2025.

level: national
country: DE
region: EU

status: active
confidence: high
coverage: medium

verification: primary-source

start_date: 2009-08-20
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - DE-BSI
related_entities:
  - DE-NIS2UMSUCG
relationships: []

sources:
  - title: "Gesetz über das Bundesamt für Sicherheit in der Informationstechnik (BSI-Gesetz — BSIG)"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/Gesetze-und-Verordnungen/BSI-Gesetz/bsi-gesetz_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "BSI — Auftrag"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/auftrag_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "NIS2-Umsetzungsgesetz in Deutschland 2025"
    url: "https://www.openkritis.de/it-sicherheitsgesetz/nis2-umsetzung-gesetz-cybersicherheit.html"
    publisher: "OpenKRITIS"
    accessed: "2026-08-28"
  - title: "Umsetzung der EU-Direktive NIS2 in Deutschland (NIS2-Umsetzungsgesetz)"
    url: "https://www.deloitte.com/de/de/services/consulting-risk/perspectives/umsetzung-eu-direktive-nis2-nis2umsucg.html"
    publisher: "Deloitte Deutschland"
    accessed: "2026-08-28"
---

# BSI-Gesetz (BSIG)

> **Re-verified 2026-08-28.** All four cited pages read directly, including
> both `bsi.bund.de` pages, which between them supply the previously-missing
> enactment date. `verification: primary-source`; `confidence` raised to
> `high` and `coverage` to `medium`.
>
> **Ontology decision, 2026-09-20**: [[DE-NIS2UMSUCG]]'s edge to this entity
> moves from `supersedes` to `amends` (metadata/relationship-types.md §2.1),
> closing `discovery/unresolved.md` items #7 and #68. This entity's own
> `status: active` is no longer a deliberate inconsistency requiring
> explanation — see "Why this entity is active" below, rewritten
> accordingly.

## Description

The BSI's own "Auftrag" page, read directly this pass, gives the fuller
legislative history than the entity previously recorded: the office was
first created by the **BSI-Errichtungsgesetz**, in force from 1 January
1991 to 19 August 2009, superseded by the **current BSI-Gesetz (BSIG)**,
which **entered into force on 20 August 2009** — a date not previously
established and now recorded as `start_date`. The BSI's own dedicated
BSI-Gesetz page corroborates this and states the most recent consolidated
version became effective 2 December 2025 (BGBl. 2025 I Nr. 301, S. 2) — a
date that sits close to, but does not exactly match, the 5/6 December 2025
publication/entry-into-force dates recorded on [[DE-NIS2UMSUCG]]; this
pass could not resolve which date describes the Bundesgesetzblatt issue
versus the amending act's own commencement, and both are recorded rather
than one being silently dropped.

The BSIG constitutes [[DE-BSI]] and defines the scope of its tasks. Under
**§ 4 BSIG** the BSI acts as the central reporting point for IT security,
collecting and evaluating information on vulnerabilities, malware and
attack patterns — confirmed directly this pass on the BSI's own page.

Three expansions are now sourced, one more than before:

- The **IT-Sicherheitsgesetz**, in force from 2015, significantly widened
  the BSI's tasks and powers, particularly critical-infrastructure oversight
  and mandatory incident reporting.
- **IT-Sicherheitsgesetz 2.0**, in force from 2021, further broadened the
  mandate, including consumer-facing IT security labelling — newly
  confirmed this pass on the BSI's own "Auftrag" page and not previously
  recorded on this entity.
- [[DE-NIS2UMSUCG]] **comprehensively revised** the BSIG with effect from
  6 December 2025, in preference to enacting a separate NIS2 statute —
  confirmed directly this pass by Deloitte's own page ("kein eigenständiges
  NIS-2-Gesetz geschaffen, stattdessen erfolgte eine umfassende Revision des
  bestehenden BSI-Gesetzes") and by OpenKRITIS's page, which additionally
  states the regulated population grew to roughly 30,000 organisations
  across categories including "besonders wichtige" and "wichtige
  Einrichtungen," digital service providers, DNS operators,
  telecommunications operators and public administration bodies —
  consistent with the "roughly 29,500 entities across 18 sectors" figure
  already recorded on [[DE-NIS2UMSUCG]].

`coverage: medium` (raised from `low`): the act's enactment date, its
predecessor, and its amendment history are now recorded, though its
detailed internal structure (chapters, sections beyond § 4) still is not.

## Why this entity is `status: active` — resolved 2026-09-20

[[DE-NIS2UMSUCG]] carries an edge pointing here, and this entity is
`active` rather than `superseded`. Until 2026-09-20 that edge was
`supersedes` at `confidence: low`, which made the pairing a **deliberate
inconsistency** requiring explanation on both entities' files: `supersedes`
normally means the target retires, and the BSIG plainly had not.

The BSIG was **amended, not repealed**. OpenKRITIS's page, read directly,
does state that "[d]as bisherige BSI-Gesetz tritt in der alten Fassung
dann außer Kraft" (the BSI-Gesetz's previous wording ceases to have effect)
— language that could be misread as a repeal. Read alongside Deloitte's
explicit statement that no standalone NIS2 law was created and the BSIG was
instead comprehensively revised, the more accurate description is the
ordinary German legislative pattern for an Änderungsgesetz that restates a
law's text in full (Neufassung): the old wording lapses at the moment the
new wording takes effect, but the statute continues in force under its own
name and citation.

**Closed as an ontology decision, 2026-09-20**: [[DE-NIS2UMSUCG]]'s edge
now uses `amends` (metadata/relationship-types.md §2.1) instead of
`supersedes` — a type added later, for a different case, that turns out to
fit this one exactly, and was simply never checked against it until now.
`amends` carries no implication that the target retires, so `active` is now
the entity's plainly correct status rather than a flagged inconsistency.
See [[DE-NIS2UMSUCG]] for the full reasoning.

Where the Atlas has a genuine supersession it still says so on both sides —
[[NL-WBNI]] is `superseded` and [[NL-CBW]] `supersedes` it; [[DE-IWG]] is
`superseded` and [[DE-DNG]] `supersedes` it. This entity is the other
pattern: amended, continuing under its own name, and that is now what its
relationships say.

## Relationships

**None asserted from this entity.** It is reached from [[DE-BSI]]
(`governed-by`) and from [[DE-NIS2UMSUCG]] (`amends`, since 2026-09-20;
previously `supersedes`).

## Sources

Listed in frontmatter, all four read directly this pass.
