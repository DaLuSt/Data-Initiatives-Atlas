# Germany — Second Country Report

Written 2026-08-15. Reproduce with `python validation/run_all.py`,
`python validation/audit.py` and `python validation/audit.py --scope DE`.

---

## What this batch was for

The Final Quality Gate listed three things that would close the Atlas's
remaining gaps. The third was:

> **A second country** — the only real test of the country-neutral model.

and `discovery/unresolved.md` recorded the same point more precisely: all
17 `applies-in` relationships targeted `NL`, so *"the mechanism is
exercised but **untested with a second country**, which is the only real
proof."*

This batch ran that test.

---

## Result

**The country-neutral model holds.** Adding Germany required:

| Changed | Not changed |
|---|---|
| A new `countries/de/` folder (anchor + index) | `metadata/schema.json` |
| 37 German entities in the **existing** flat type folders | `metadata/ontology.md` |
| `applies-in` → `DE` on 15 existing EU instruments | `metadata/taxonomy.md` |
| 2 new supra-national entities ([[EU-INSPIRE]], [[EU-GAIA-X]]) | `metadata/relationship-types.md` |
| `countries/README.md` participating-countries table | Any validation rule |

No entity type, relationship type, status or level was added. **No
`DE-EU-*` entity was created**, and `audit.py` confirms it:

```
## Country-neutrality
  no country-scoped copies of EU/UN/INTL entities (README §16 holds)
  33 applies-in relationships carry supra-national applicability
  targets: ['DE', 'NL']
```

### The graph

| | Before | After |
|---|---|---|
| Entities | 125 | **164** |
| Provenanced relationships | 131 | **189** |
| `applies-in` | 17 (all `NL`) | **33 (`NL` + `DE`)** |
| Fully disconnected entities | 0 | **0** |
| Validation | 5/5, 0 errors | **5/5, 0 errors** |

Cross-level structure, whole graph:

| Direction | Count |
|---|---|
| EU → DE | **16** |
| EU → NL | 15 |
| DE → EU | **11** |
| NL → EU | 10 |
| DE → INTL | **2** |
| NL → INTL | 2 |
| EU → INTL | 1 |
| **UN → anything** | **0** |

Germany connects to the EU layer slightly more densely than the
Netherlands does, on a layer built second from the same ontology. **The UN
layer remains isolated** — this batch did not address it and did not
pretend to.

---

## The four structures a second country made visible

### 1. One EU instrument, two national implementations — four times

```
EU-GDPR ─────────────► NL-UAVG      +  DE-BDSG
EU-NIS2 ─────────────► NL-CBW       +  DE-NIS2UMSUCG
EU-OPEN-DATA-DIRECTIVE► NL-WHO      +  DE-DNG
EU-ITS-DIRECTIVE ────► NL-NTM       +  DE-MOBILITHEK
```

Each EU instrument is **one entity** carrying `applies-in` to both
countries. This is the whole argument for the model, and it is now
demonstrated rather than asserted.

**No relationship is asserted between any pair of national
implementations.** They are siblings; the shared parent is the
relationship.

### 2. A standards chain that forks across two countries

```
              INTL-DCAT (W3C)
                    │ based-on
              EU-DCAT-AP (SEMIC)
               │            │
      NL-DCAT-AP-NL    DE-DCAT-AP-DE
      (Geonovum)       (IT-Planungsrat)
```

The first **four-level structure in the Atlas that branches across two
countries**. It also exposes a contrast invisible with one country: the
Dutch profile is custodied by a geospatial foundation, the German one was
established by a Bund-Länder political resolution. Same standard family,
different institutional logic — recorded, not smoothed away.

### 3. Two security baselines, one ancestor, two relationship types

```
INTL-ISO-IEC-27001 ──based-on──────► NL-BIO
                   ──aligned-with──► DE-IT-GRUNDSCHUTZ
```

`aligned-with` is used for Germany deliberately. [[NL-BIO]] is a baseline
built on the ISO controls; IT-Grundschutz is a **parallel methodology kept
compatible** with ISO 27001. Copying the Dutch relationship type by analogy
would have misstated it.

### 4. Two transpositions of one directive, differing in kind

| | [[DE-NIS2UMSUCG]] | [[NL-CBW]] |
|---|---|---|
| In force | 6 Dec 2025 | 15 Aug 2026 |
| Technique | **revises** the existing [[DE-BSIG]] | **new act** superseding [[NL-WBNI]] |

The Atlas can now show that member states transpose the same directive by
different legislative means, without either country's model distorting the
other.

---

## The principal finding: the model is lossy for federal states

This is the batch's most useful result and it is a **negative** one.

The `level` vocabulary runs `international / regional / national /
sectoral / local`. There is nothing for a German **Land**. Concretely lost:

- **[[EU-INSPIRE]] transposition.** Sources state Germany transposed it
  through the federal [[DE-GEOZG]] *and sixteen Land acts*. The Atlas
  records one federal act. Sixteen jointly-necessary instruments are not
  representable.
- **Data protection supervision.** [[DE-BFDI]] covers federal bodies only;
  sixteen Land authorities cover the rest. A reader seeing `country: DE` +
  "data protection authority" would wrongly infer national coverage.
- **[[DE-KOSIT]]**, hosted in the Bremen administration while operating
  under the federal [[DE-FITKO]]. Both facts are sourced; the model cannot
  hold them together, so `part-of` is recorded at `confidence: low`.
- **Verwaltungsvereinbarungen.** [[DE-GOVDATA]] and [[DE-GDI-DE]] both rest
  on Bund-Länder administrative agreements. No entity type fits.

The Atlas **cites Land governments as sources** — Brandenburg's interior
ministry, Bavaria's and Rhineland-Palatinate's geoportals — while being
unable to model them.

No sub-national level was invented. Doing so for Germany alone would be
exactly the country-specific ontology change the model exists to prevent.
This is logged as an open ontology question, and it will matter for any
federal state added later.

---

## Judgements worth auditing

### Three direction errors, caught before validation

`maintained-by` is defined as *"the target organisation maintains this
entity"*. Two edges were written backwards on the first pass and one
relationship was inverted outright:

| Written | Corrected to |
|---|---|
| `DE-IT-PLANUNGSRAT` `governed-by` → `DE-FITKO` | `DE-FITKO` `governed-by` → `DE-IT-PLANUNGSRAT` |
| `DE-FITKO` `maintained-by` → `DE-GOVDATA` | `DE-GOVDATA` `maintained-by` → `DE-FITKO` |
| `DE-BMDS` `maintained-by` → `DE` | removed — no Dutch organisation points at [[NL]] either |

The first inverted a constitutional relationship (the FITKO acts *im
Auftrag des* IT-Planungsrats). The second asserted that a portal maintains
an agency. **Neither would have failed validation** — the graph stays
connected and every check passes while the meaning is reversed. That is
worth knowing about this tooling.

The third is the more interesting one: it was a *new pattern*, not an
error of direction. EU and UN organisations attach to their anchor via
`part-of`; Dutch organisations do not attach to [[NL]] at all. Copying the
EU pattern would have given Germany a third convention. Catching drift like
this is precisely what a second country is for.

### The weakest modelling decision, flagged not hidden

[[DE-NIS2UMSUCG]] `supersedes` [[DE-BSIG]] at `confidence: low`, while
[[DE-BSIG]] stays `status: active`. **The two sides deliberately do not
agree.** The BSIG was amended, not repealed; the Atlas has no
amendment-lineage relationship type; and setting the BSIG to `superseded`
to make the record self-consistent would state something false about German
law. Compare [[DE-DNG]] → [[DE-IWG]] two files away, where a genuine
supersession *is* recorded on both sides. The batch contains both patterns,
which makes the difference legible.

### Scoping resisted

[[EU-GAIA-X]] arrived entirely through German research — found via
[[DE-CATENA-X]], explained by the Gaia-X Hub Germany, backed by German
government and industry. It is recorded `country: null`, `region: EU`,
because the sources say it is a **Belgian-law association founded jointly
by German and French institutions**. `DE-GAIA-X` would have been §16's
forbidden pattern arrived at by mis-scoping a new entity rather than
duplicating an existing one — the version a validator cannot catch.

### Ten links refused

Fully listed in `discovery/unresolved.md`. Three that cost the most:

- **[[DE-XRECHNUNG]] → EN 16931 / [[EU-CEN]]** — would give a fifth EU→DE
  chain running through a standards body. No source read states it.
- **[[DE-DESTATIS]] → [[EU-EUROSTAT]]** — Destatis's sourced remit includes
  harmonising statistics "for the purposes of the European Union" but does
  not name Eurostat. This is now the **third** refused link in the
  statistics cluster, alongside [[UN-UNSD]] → [[EU-EUROSTAT]] and
  [[UN-FPOS]] → [[NL-WET-CBS]]; [[DE-BSTATG]] → [[UN-FPOS]] makes four.
- **[[DE-BFDI]] → [[EU-EDPB]]** — [[NL-AP]] carries exactly this link.
  German representation on the EDPB is precisely the detail that must not
  be guessed.

Two independent instances of the same unsourced resemblance are not
evidence. They are two instances of the same unsourced resemblance.

---

## A gap this batch created

[[EU-INSPIRE]] was added because [[DE-GEOZG]] needed a parent. It carries
`applies-in` → [[DE]] and **not** → [[NL]], because the German
transposition is sourced and the Dutch one is not — the Dutch geospatial
batch predates this entity and none of its sources named the directive.

The result is an EU directive that **looks German-specific**, which is
misleading in the opposite direction from the usual failure mode. It is
flagged in the entity body and logged as a first-priority gap: unlike most
refused links here, this one is near-certain to be closable by a single
page read.

---

## Evidence posture

Unchanged in kind, and that is the point.

| Field | German layer (37) | Whole graph (164) |
|---|---|---|
| `verification` | search-only 37 | search-only 155, primary-source 6, unverified 3 |
| `confidence` | medium 35, low 2, **high 0** | medium 132, low 32, **high 0** |
| `coverage` | medium 30, low 7, **high 0** | medium 87, low 77, **high 0** |
| Weak-source-only entities | **0** | 2 (both pre-existing) |

**No German URL has been fetched.** Page retrieval was blocked throughout
(`EGRESS_BLOCKED`, 403 at the proxy tunnel, re-tested at the start of this
batch). Every German entity carries the sourcing caveat, no `accessed`
dates were written, and `last_verified` is null throughout.

One improvement: the [[DE]] anchor is `verification: search-only`, not
`unverified`. [[NL]], [[EU]] and [[UN]] are all `unverified` because they
were written in Batch 0 with URLs composed from background knowledge. The
single URL cited for [[DE]] was returned by a search index. The second
country was written to the corrected standard from the start rather than
being retro-fitted into it.

---

## Verdict

**Structurally: passes, and now demonstrably so.** The country-neutral
architecture was an assertion with one country and is a demonstrated
property with two. Four EU instruments have two national implementations
each, a standards chain forks across both countries, and no supra-national
entity was duplicated.

**Evidentially: unchanged, which is to say it does not pass.** 155 of 164
entities rest on sources nobody has read. The German layer is no better
sourced than the Dutch one and in places worse — [[DE-BDSG]], the entity
carrying the most structural weight in the batch, rests entirely on
commercial legal publishers.

**One real limitation found:** the model is lossy for federal states. That
finding could not have been made without a second country, and it is the
strongest argument for adding a third.
