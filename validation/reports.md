# Validation Reports — Batches 6, 11 and 15

Findings from the three validation batches, run 2026-08-14 against 125
entities. Reproduce with:

```
python validation/run_all.py    # hard rules — fails the build
python validation/audit.py      # analytical audit — advisory
python validation/audit.py --scope NL|EU|UN|INTL
```

---

## ⚠ What these batches could and could not check

This must be stated before any findings, because it bounds everything below.

**117 of 125 entities have never had a cited source read.** Page retrieval
was blocked throughout (`EGRESS_BLOCKED` on every host tested). The
validation batches therefore split cleanly in two:

| Checkable without sources | **Not** checkable without sources |
|---|---|
| Duplicate entities and organisations | Outdated information |
| Invalid IDs, broken internal links | Incorrect statuses |
| Inconsistent metadata, vocabularies | Whether cited sources say what we claim |
| Missing sources; weak-source reliance | Whether cited URLs resolve at all |
| Unsupported relationships (provenance) | Factual accuracy of any description |
| Missing relationships (orphans, gaps) | |
| Country-specific assumptions in the ontology | |

Everything in the left column was checked and is reported below. **Nothing
in the right column has been checked.** These reports establish that the
graph is internally coherent and honestly labelled; they establish nothing
about whether its content is true.

An earlier position in this project was that the validation batches could
not run at all until sourcing was fixed. That was too absolute — the left
column is most of what the batch briefs ask for, and it found real defects.

---

## Batch 6 — Netherlands Validation

**Scope:** 61 entities (`NL-` plus the `NL` anchor).

### Defects found and fixed

| Defect | Fix |
|---|---|
| **`NL-ISHARE` fully disconnected** — no inbound or outbound edges, the only such entity in the layer | Added an explicit `related-to` → [[NL-DSGO]] marked `source: interpretation`, `confidence: low`, with the reasoning in-file |
| **`NL` anchor mislabelled** — written in Batch 0 with source URLs composed from background knowledge, never confirmed by search or fetch | Set `verification: unverified` (worse than `search-only`) and `confidence: high` → `medium` |

The second is the more serious of the two, and it was **self-inflicted in
Batch 0**: the brief says never invent URLs, and although `government.nl` and
the ISO OBP link are near-certainly correct, "near-certainly correct" is the
standard the brief rules out. The same fix was applied to [[EU]] and [[UN]].

Note that the confidence downgrade was *forced* by the repository's own
validation rule — `validate_frontmatter.py` rejects `confidence: high` on
`unverified` entities. The rule, added in Batch 1, caught its author.

### Clean results

- **No duplicates.** No name or alias is shared by two entities.
- **No broken links, no invalid IDs, no vocabulary violations** (automated
  suite, 0 errors).
- **Every non-domain entity has at least one source.**

### Standing findings — not defects, but worth knowing

- **`NL-PETRA` relies on a single encyclopedia source** and is the weakest
  entity in the layer. It says so in its own body.
- **12 entities carry no provenanced relationship of their own.** Most are
  legitimately terminal (legislation that nothing else implements), but the
  set is worth reviewing when sources become available.
- **9 relationships sit at `confidence: low`**, concentrated in the
  IBDS↔FDS pair, the RORA→EAR succession, and the NEN-3610 custody question
  — all already logged in `discovery/unresolved.md`.
- **Evidence posture:** 60 of 61 `search-only`, 1 `unverified`. Confidence
  runs 42 medium / 18 low; coverage 39 medium / 22 low.

---

## Batch 11 — EU Validation

**Scope:** 41 entities (`EU-` plus the `EU` anchor).

### Defect found and fixed

| Defect | Fix |
|---|---|
| **`EU` anchor fully disconnected** | Added `part-of` → [[EU]] from [[EU-COMMISSION]], [[EU-PARLIAMENT]] and [[EU-COUNCIL]] |

This was an **inconsistency between layers**, not an isolated oversight: the
UN layer modelled institutional membership (`UN-UNSD`, `UN-UNCTAD`,
`UN-ITU` are all `part-of` [[UN]]) while the EU layer did not. The audit
made the asymmetry visible.

A different asymmetry was examined and **left in place deliberately**:
[[NL]] is the target of 17 `applies-in` relationships while [[EU]] is the
target of none. That is correct, not a defect — a country is a place law
applies *in*; a region here is the level law comes *from*.

### The EU→national chain, verified structurally

The brief asks Batch 11 to pay particular attention to the EU→national
legislative and standards chains. Both hold:

```
EU-CYBERSECURITY-STRATEGY → EU-NIS2 → NL-CBW → (supersedes) NL-WBNI
                          ↘ EU-CER
EU-GDPR                → NL-UAVG → NL-AP → (participates-in) EU-EDPB
EU-OPEN-DATA-DIRECTIVE → NL-WHO
EU-ITS-DIRECTIVE       → NL-NTM → (part-of) NL-NDW
EU-DCAT-AP             → NL-DCAT-AP-NL
```

25 cross-level relationships run between the EU and NL layers (15 EU→NL,
10 NL→EU).

### Standing findings

- **4 relationships at `confidence: low`, all on [[EU-DIGITAL-OMNIBUS]]** —
  appropriate, since it is an unadopted proposal whose substance rests on
  law-firm commentary.
- **8 entities carry no provenanced relationship of their own.**
- **Every non-domain entity has at least one source**, and no EU entity
  relies solely on weak sources.

---

## Batch 15 — Global Validation

**Scope:** whole graph, 125 entities.

### ⚠ Principal finding: the international layer is an island

The cross-level relationship census:

| Direction | Count |
|---|---|
| EU → NL | 15 |
| NL → EU | 10 |
| NL → INTL | 2 |
| EU → INTL | 1 |
| **UN → anything** | **0** |
| **anything → UN** | **0** |

**The 9 UN-scoped entities have no relationship to any EU or Netherlands
entity.** They connect only to each other and to [[UN]].

This is the single most significant structural gap in the Atlas. The brief's
target architecture is UN → EU → National → Sector; what exists is a
connected EU→NL graph with a separate, unattached UN component and a thin
INTL bridge.

**It has not been papered over.** Two specific links would close most of it
and both were examined and refused for want of a source:

- `UN-UNSD` → `EU-EUROSTAT` — the European Statistical System is plainly
  part of the global statistical system, but no source read says so.
- `UN-FPOS` → `NL-WET-CBS` — countries are tracked on whether statistical
  legislation aligns with the Fundamental Principles, but no source
  connects the Dutch act to them.

Both are logged in `discovery/unresolved.md`. Closing them is the highest-
value single piece of research remaining in the project.

### The INTL bridge does work

Where international entities *are* connected, the chains are complete and
sourced:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
INTL-ISO-IEC-27001 + -27002 (ISO/IEC) → NL-BIO
```

These are the only two international → national descents in the Atlas, and
they are the template for what the UN layer lacks.

### Country-neutrality: holds

- **No country-scoped copies of supra-national entities.** No
  `NL-EU-DATA-ACT` pattern anywhere (README §16).
- **17 `applies-in` relationships**, all targeting `NL` — the only country
  in the Atlas. The mechanism is in place and exercised; it is **untested
  with a second country**, which is the real proof and remains outstanding.

### Ontology consistency

- **6 domain entities**, every one connecting ≥2 entities as
  `metadata/taxonomy.md` §1 requires. Seven further domains named in batch
  briefs were withheld for falling below that threshold.
- **No duplicate names or aliases** across 125 entities.
- **Type distribution:** organisation 41, framework 14, law 12, regulation
  10, standard 8, strategy 7, data-space 6, domain 6, platform 6, directive
  5, initiative 4, policy 2, programme 2, country 1, region 1.

### Evidence posture, whole graph

| Field | Distribution |
|---|---|
| `verification` | search-only 116, primary-source 6, **unverified 3** |
| `confidence` | medium 95, low 30, **high 0** |
| `coverage` | low 70, medium 55, **high 0** |
| `status` | active 115, planned 4, superseded 3, unknown 2, proposed 1 |

The 6 `primary-source` entities are the domain taxonomy nodes, which make no
factual claims. **No entity in the Atlas claims `confidence: high` or
`coverage: high`** — appropriate, and enforced for confidence by validation.

### Relationship provenance, whole graph

119 provenanced relationships: **108 `source: fact`, 11
`source: interpretation`**. Every interpretation is labelled at the
relationship level and explained in the entity body. 13 sit at
`confidence: low`.

Weak-source reliance across the whole graph is down to two entities:
[[NL-PETRA]] (encyclopedia) and [[UN-DATA-COMMONS]] (an AI-generated
encyclopedia — the weakest citation in the repository).

---

## Verdict

**The graph is internally coherent.** No duplicates, no broken links, no
orphans, no vocabulary violations, no country-neutrality breaches, and
provenance labelled consistently throughout. Three real defects were found
and fixed.

**The graph is not verified.** 117 of 125 entities rest on sources nobody
has read, and 3 rest on URLs nobody has even confirmed exist. The batches
could not check status accuracy, currency, or whether any cited page says
what the Atlas claims it says.

**The international layer does not yet connect to the rest.** That is a
structural gap, not a labelling one, and no amount of source-free validation
can close it.

These three batches should be re-run after the re-verification pass. Until
then this report certifies structure, not truth.
