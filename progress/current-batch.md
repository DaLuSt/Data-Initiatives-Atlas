# Current Batch

**Status:** No batch in progress. The **candidate-clearing batch** was
completed on 2026-08-21 and `discovery/candidates.md` now carries only what
is genuinely still open.

## Candidate clearing — the remaining leads worked

**Date:** 2026-08-21

`discovery/candidates.md` was the last discovery file still carrying leads
nobody had gone back to. This batch worked every one of them, created
**sixteen** entities, closed **eleven** rows, and emptied three whole
sections of the page.

### What was created

| Layer | Entities |
|---|---|
| Statutory bases | [[EU-REG-223-2009]], [[EU-REG-1025-2012]] |
| The EEA route | [[INTL-EEA-JCD-154-2018]], [[IS-PERSONUVERNDARLOG]], [[IS-PERSONUVERND]], [[LI-DSG]], [[LI-DATENSCHUTZSTELLE]] |
| Switzerland | [[EU-CH-ADEQUACY]] |
| Geospatial | [[EU-EUROGEOGRAPHICS]] |
| Trade / mobility | [[UN-LOCODE]], [[UN-EDIFACT]], [[EU-EMSWE]] |
| Sustainable development | [[UN-2030-AGENDA]], [[EU-VOLUNTARY-REVIEW-2023]] |
| Measurement | [[EU-DESI]], [[EU-EGOV-BENCHMARK]] |

**All 17 entity types are now in use.** `publication` was the last unused
one; [[EU-DESI]], [[EU-EGOV-BENCHMARK]] and [[EU-VOLUNTARY-REVIEW-2023]] are
its first instances, and they give the Atlas its first
comparative-measurement layer. Everything else it holds prescribes; these
measure.

### The deferred pair was closed by creating both halves

[[EU-ESS]] carried a section headed *"Regulation (EC) No 223/2009 is cited,
not modelled"* and [[EU-CEN]] carried one headed *"Regulation 1025/2012 not
modelled"*. Both deferrals gave the **same** reason: modelling one statutory
base and not the other would make the Atlas inconsistent about statutory
bases in general.

The answer was to create both in one batch, not neither. `EU-ESS` now has the
`governed-by` edge its own body said it lacked, and the three European
standardisation organisations are covered by `applies-to` edges from
`EU-REG-1025-2012`. Both "not modelled" sections were rewritten to say what
happened rather than deleted.

### The EEA route is now drawable end to end

[[INTL-EEA-AGREEMENT]] carried a section headed *"⚠ The individual Joint
Committee decisions are not modelled"*. **JCD No 154/2018 was cited four
times across the Atlas** — in the Agreement's sources, and in
[[NO-PERSONOPPLYSNINGSLOVEN]]'s description, evidence string and sources —
without existing.

```
EU-GDPR ◀─ references ─ INTL-EEA-JCD-154-2018 ─ amends ─▶ INTL-EEA-AGREEMENT
                                 │ applies-in
                     ┌───────────┼───────────┐
                     ▼           ▼           ▼
                    NO          IS          LI
```

Only this one decision is modelled, and the original caution still holds for
every other.

### The Norwegian EEA pattern generalises — and the exception is the interesting part

`discovery/candidates.md` asked whether adding Iceland or Liechtenstein
*"would show whether the Norwegian EEA pattern generalises or is
Norway-specific"*. Both were added, and the answer is both halves of a yes:

| | Norway | Iceland | Liechtenstein |
|---|---|---|---|
| Act adopted | 15 June 2018 | 27 June 2018 | 4 October 2018 |
| In force | 20 July 2018 | 15 July 2018 | **1 January 2019** |
| Act's function | gives GDPR effect | gives GDPR effect | **supplements** an already-applicable GDPR |
| Route | JCD 154/2018 | JCD 154/2018 | JCD 154/2018 |

The **route** is identical in all three. The **national instrument's job** is
not, and the five-month gap is the tell: Norway's and Iceland's acts had to
be in force on the day the GDPR started to apply, because their acts were
what made it apply. Liechtenstein's did not.

Both new authorities attach to [[EU-EDPB]] on a sourced composition rule —
JCD 154/2018 provides that the supervisory authorities of the EFTA States
participate in the Board's activities — the same basis on which the national
standardisation bodies were attached to [[EU-CEN]]. Neither claims a vote
under Article 68(3).

### One vocabulary gap was real; the other was a missing node

`discovery/candidates.md` §3 listed two EU↔UN interactions the vocabulary
could not express and concluded that *"two examples is the threshold §2.3
sets for proposing a new type"*. Two things were wrong with that:

1. **The threshold is one.** §2.4 asks for "at least one real example". §2.3
   is the anchor-edge rule and sets no threshold for new types at all.
2. **The two cases were not instances of the same missing type.** One was a
   cooperation agreement between two organisations — a real gap, now filled
   by **`cooperates-with`** (the Atlas's 23rd relationship type), asserted on
   [[UN-UNESCO]] for the UNESCO–Commission AI ethics agreement. The other was
   a report submitted to a UN process, which needed **no relationship type at
   all** — only the `publication` entity type the ontology had defined and
   nothing had used. It is now [[EU-VOLUNTARY-REVIEW-2023]], and `references`
   is simply correct between a document and the policy it reports on.

**A count of unmodellable things is not a count of instances of one missing
type.** Recorded as a worked example in `metadata/relationship-types.md` §2.4.

### Creating the missing node did not always close the edge

[[EU-EUROGEOGRAPHICS]] was on the page as *"the cluster's missing middle"*,
explicitly analogised to [[EU-ESS]]. It was created, and five national
mapping and cadastral authorities now attach to it by `participates-in`:
[[NL-KADASTER]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[GB-OS]],
[[IE-TAILTE]].

**The [[EU-INSPIRE]] → UN-GGIM refusal did not close.** `EU-ESS` closed five
refused edges because the missing node was what all five had been pointing
at. Here the node was also genuinely missing — but it was never what the
INSPIRE refusal turned on. The two cases look identical on the candidates
page and are not, and the row stays open with that noted.

### The narrow UN/CEFACT question, answered by adding the instrument

*"Does any instrument already in this Atlas reference a UN/CEFACT
standard?"* — **no.** But [[EU-EMSWE]], Regulation (EU) 2019/1239, provides
for a common location database holding [[UN-LOCODE]], so the row closed by
adding the instrument rather than by finding one already present.
[[UN-EDIFACT]] was created alongside it and deliberately carries no European
edge, because none was found.

### The 2030 Agenda was never thinly sourced

It had been refused as *"nothing found beyond passing references"*. It was
being searched for on Eurostat's SDG pages, where it appears only as context.
Searching for the resolution — **A/RES/70/1** — returns the resolution.

This is the third instance of the lesson `discovery/candidates.md` already
recorded: **a refusal for want of a source is not the same as a fact being
unknowable.**

### The domain coverage table was re-measured

The old table read "3/7", "2/7", "1/7" against seven countries. Against 58
anchors: `DOMAIN-GOVERNMENT` 21, `DOMAIN-CYBERSECURITY` 13,
`DOMAIN-NATIONAL-SECURITY` 8, `DOMAIN-GEOSPATIAL` 6, `DOMAIN-MOBILITY` 2, and
`DOMAIN-HEALTH`, `DOMAIN-EDUCATION` and `DOMAIN-RESEARCH` **1 each**. The
absolute counts went up and the coverage got thinner.

### What was deliberately not done

- **No `measures` relationship type.** [[EU-DESI]] and
  [[EU-EGOV-BENCHMARK]] measure 27 and 35 countries and carry no edge to any
  of them. `cooperates-with` was added on one example because it has one
  instance and no scaling consequence; `measures` would immediately want 62
  edges, and a type added in the same batch that creates its only users has
  not been tested. Left open in `discovery/candidates.md` §3.
- **No entity for Capgemini**, the eGovernment Benchmark's contractor. A
  private firm named as the executor of one study is not an Atlas subject.
- **No `based-on` edge from [[LI-DSG]] to [[DE-BDSG]].** "Modelled after" in
  a law-firm commentary is a characterisation of legislative style, not a
  sourced statement that a specific text was adapted.
- **No entity for the eFTI Regulation (EU) 2020/1056.** Its UN/CEFACT link is
  attested in a UNECE presentation and a project website, not in the
  regulation. Queued.
- **No adoption date for [[EU-VOLUNTARY-REVIEW-2023]].** The sources give the
  HLPF window and the document reference and no adoption date, so
  `start_date` is `null` rather than a plausible-looking guess.

### Counts

| | Before | After |
|---|---|---|
| Entities | 486 | **502** |
| Edges | 5,602 | **5,847** |
| Relationship edges | 967 | **1,010** |
| Entity types in use | 16 | **17 of 17** |
| Relationship types | 22 | **23** |
| Countries with a modelled national layer | — | [[IS]] and [[LI]] added |

All four suites green: validators 5/5 (7 pre-existing plain-http warnings),
`test_build_graph.py`, `test_reverify.py`, `test_ui.mjs`.
