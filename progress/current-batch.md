# Current Batch

**Status:** No batch in progress. The **four-proposals batch** was completed
on 2026-08-21, and with it the Atlas's first content-tier source confirmation.

## The four proposals, and the first content-tier verification

**Date:** 2026-08-21

This batch acted on all four next steps proposed after the candidate-clearing
batch, plus the stale queue row found while checking them. **Fourteen
entities, two vocabulary additions, and the Atlas's first content-tier source
confirmation.**

### 1. The confirmed domains — 41 entities to `primary-source`

The repository owner confirmed five domains at the **content** tier: the pages
were read and the information on them confirmed correct.

| Domain | URLs | Entities citing it |
|---|---|---|
| `europa.eu` | 231 | 144 |
| `iso.org` | 67 | 64 |
| `coe.int` | 52 | 42 |
| `bund.de` | 41 | 23 |
| `legifrance.gouv.fr` | 5 | 5 |

**The rule applied is all-sources-or-none.** An entity moved to
`primary-source` only when *every* source it cites is on a confirmed domain;
partial coverage left it `search-only`. That is deliberately strict and the
reason is mechanical: the Atlas does not record which source supports which
claim, so an unconfirmed fifth source may be the one carrying the date.

| | Entities |
|---|---|
| Fully covered → `primary-source` | **41** |
| Partially covered → unchanged | 161 |
| Not covered | 291 |
| No sources (domains, anchors — exempt) | 8 |

Two results worth recording:

- **`legifrance.gouv.fr` yielded nothing.** Five entities cite it; all five
  also cite something unconfirmed. A confirmation is not required to move
  anything — the partial-coverage rule decides.
- **`europa.eu` did almost all of it.** 38 of the 41 are EU-scoped, which is a
  fact about how the Atlas was built rather than about the Union: EU entities
  cite one publisher because EUR-Lex carries the whole instrument, while a
  national entity cites a statute database, a ministry and a commentary.
  **So the remaining yield is front-loaded** — the allowlist ranks domains by
  URL count, which overstates how much each next one would unlock.

`tools/source_hosts.py` gained a `CONTENT_CONFIRMED` set and the generated
allowlist gained a `Content confirmed` column, so this state is generated
rather than hand-maintained. Note that the table collapses all of `gouv.fr`
into one row and is therefore **not** marked confirmed — the confirmation
names one host under that namespace, not the namespace.

### 2. `level: subnational` — the blocker that had stopped four items

`level: regional` means **supra**-national in this Atlas: it is what all 69
EU-scoped entities carry. Nothing meant *sub*-national, so a Belgian Region, a
Spanish Comunidad Autónoma and a German Land had no value — and four queued
items across three countries had been blocked on it since the Belgium batch.

**`local` was the tempting shortcut and would have been wrong.** The Flemish
decreet of 2 July 2021 is primary legislation of a constituent state with its
own parliament, not a municipal by-law. Using `local` would have flattened the
difference between a legislature and a council.

Renaming `regional` to `supranational` was rejected: 69 files, the site filter
and the docs, to buy what a definition buys.

The three Belgian sub-federal Open Data Directive instruments are now modelled
— [[BE-VL-BESTUURSDECREET-2021]], [[BE-BRU-ORDONNANCE-2021]],
[[BE-WAL-DECRET-2022]] — plus [[BE-BRU-ORDONNANCE-2016]], which the Brussels
2021 ordonnance amends and which **predates the directive by two and a half
years**.

**A correction the research produced.** [[BE-HERGEBRUIK-WET-2023]] said
Flanders *"met the deadline"* because its decree *"preceded 17 July 2021 by a
fortnight"*. The annotated Codex text is sharper: the decree was **adopted**
2 July and its open-data provisions **entered into force on 17 July 2021** —
the deadline to the day. Flanders did not transpose early; it transposed
exactly on time, having legislated a fortnight before.

And the reason it was worth modelling at all:

| Level | Instrument | Against the deadline |
|---|---|---|
| Flanders | [[BE-VL-BESTUURSDECREET-2021]] | **on time** |
| Brussels-Capital | [[BE-BRU-ORDONNANCE-2021]] | 5 months late |
| Wallonia | [[BE-WAL-DECRET-2022]] | 16 months late |
| Federal | [[BE-HERGEBRUIK-WET-2023]] | 29 months late |

The Atlas showed Belgium as twenty-nine months late. Three quarters of the
country was not.

### 3. `measures` — 62 edges, one batch after the entities that needed them

[[EU-DESI]] and [[EU-EGOV-BENCHMARK]] measured 27 and 35 countries and carried
no edge to any of them, because no relationship type meant "measures".
`discovery/candidates.md` had argued for waiting: *"a type added in the same
batch that creates its only users has not been tested against anything."*

Added now, in the following batch. `measures` is directional and asymmetric —
being measured implies nothing about the target, which is exactly why it could
not be `applies-in`, and why `references` would have suggested citation rather
than assessment.

**The 62 edges rest on each publication's sourced scope rule**, not on 62
individual sources — the same basis [[NL-NEN]] attaches to [[EU-CEN]] on. Every
evidence string says so.

The contrast with `cooperates-with` is the point: that type was added on a
single example because it had one instance and no scaling consequence.
`measures` immediately wanted 62 edges and got a batch of separation first.

### 4. Health, education and research — the three domains stuck at 1 of 58

| Domain | Before | After |
|---|---|---|
| [[DOMAIN-HEALTH]] | 1 | **5** |
| [[DOMAIN-RESEARCH]] | 1 | **2** |
| [[DOMAIN-EDUCATION]] | 1 | **2** |

Health was called *"the single largest correction available"*: the Atlas held
[[EU-EHDS]] and one country's health entities. Four countries were added, and
they turn out to answer the same problem **three different ways**:

| | Body | Shape |
|---|---|---|
| [[DE]] | [[DE-GEMATIK]] + [[DE-GDNG]] | statute creates a research data centre; a separate company runs the exchange infrastructure |
| [[FR]] | [[FR-HEALTH-DATA-HUB]] + [[FR-SNDS]] | a public-interest grouping of **56 members** holds the platform |
| [[FI]] | [[FI-FINDATA]] + [[FI-SECONDARY-USE-ACT]] | a statutory **permit authority** licenses access to data others hold |
| [[DK]] | [[DK-SUNDHEDSDATASTYRELSEN]] | the authority **holds the registers itself** |

Pool, license, custody. Every one of these countries has "a national health
data body"; they do materially different jobs, and only placing them side by
side shows it. Recorded on [[DOMAIN-HEALTH]].

Research and education gained [[EU-GEANT]] — the **third** membership
association after [[EU-ESS]] and [[EU-EUROGEOGRAPHICS]] — with [[NL-SURF]] and
[[DE-DFN]] attached, plus [[DE-NFDI]], whose [[EU-EOSC]] membership is
**sourced** rather than inferred.

Germany now has two research-data bodies that are not the same thing:
[[DE-DFN]] is the network and attaches to GÉANT; [[DE-NFDI]] is the data
infrastructure and attaches to EOSC. The Netherlands collapses both roles into
[[NL-SURF]] and Germany does not — a finding rather than a modelling artefact.

### 5. The stale queue row

`discovery/research-queue.md` still carried *"`applies-in` to the 17 new EU
member states"* as **Next**. [[EU-GDPR]] has all 27; the work was done in the
publication batch and the row survived its cleanup. Removed, along with two
others this batch closed. **No new rows were added** — limits are recorded in
entity prose instead, on instruction.

### What was deliberately not done

- **No `verification` change for the 161 partially covered entities.** The
  all-or-none rule is the whole reason the sweep is trustworthy.
- **No `based-on` edge from [[FR-HEALTH-DATA-HUB]] to the loi OTSS.** The law
  of 24 July 2019 is named in every French health source and none gives it a
  JORF or Legifrance identifier, which is what the Atlas's French legislation
  entities are keyed on.
- **No date for [[DE-GDNG]].** The sources describe the act and its effects
  and none gives its date. `start_date` is `null`.
- **No entities for** the Forschungsdatenzentrum Gesundheit, the Kanta
  Services, the Danish National Patient Register, CERN or ESA — each named
  once in a source about something else.
- **[[FR-SNDS]] is `coverage: low` and says so at length.** Everything known
  about it comes from sources *about the Plateforme*. It is on the edge of the
  taxonomy threshold, not clear of it, and the entity states that plainly.

### Counts

| | Before | After |
|---|---|---|
| Entities | 502 | **516** |
| Edges | 5,856 | **6,170** |
| Relationship edges | 1,010 | **1,095** |
| `verification: primary-source` | 40 | **81** |
| Relationship types | 23 | **24** |
| `level` values in use | 4 | **5** |
| Research-queue rows | 207 | **204** |

All four suites green: validators 5/5 (7 pre-existing plain-http warnings),
`test_build_graph.py` 41 OK, `test_reverify.py` 36 OK, `test_ui.mjs` 86/86.
