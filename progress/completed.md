# Completed Batches

## Batch 4 — Netherlands: Standards, Frameworks and Architecture

**Date:** 2026-08-14

**Scope:** Dutch reference architectures, standards-management models,
security baselines, and metadata/API/interoperability standards, each
connected to its maintaining organisation as the batch brief requires.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
entities are `verification: search-only`.

**Entities added (11):**

*Reference architectures — the NORA family:*

| ID | Tier | Note |
|---|---|---|
| `NL-GEMMA` | Municipalities | Only member with a **sourced** `based-on` → NORA |
| `NL-EAR` | Central government | `superseded`, `successor: NL-RORA` |
| `NL-RORA` | Central government | Successor since 2024 |
| `NL-PETRA` | Provinces | Weakest entity in the Atlas — see below |
| `NL-ROSA` | Education sector | `level: sectoral` |

*Frameworks:*

| ID | Note |
|---|---|
| `NL-BOMOS` | The Dutch "standard for running a standard" |
| `NL-BIO` | Security baseline for all government tiers; current version BIO2 |

*Standards (all connected to a maintainer):*

| ID | Maintainer | Note |
|---|---|---|
| `NL-DIGIKOPPELING` | Logius | On the mandatory list |
| `NL-ADR` | Logius | On the mandatory list |
| `NL-DCAT-AP-NL` | Geonovum | Bridges to European data catalogues |
| `NL-NEN-3610` | Geonovum / NEN | Custody split — see below |

**Entities updated:** `NL-NORA` (family table + `related_entities`),
`NL-GEONOVUM` (BOMOS alignment), `countries/nl/index.md`.

**Relationships added:** 10 provenanced entries — 5 `maintained-by`,
2 `part-of` (onto the mandatory standards list), 1 `based-on`,
1 `supersedes`, 1 `applies-in`, plus `derived-from` and `aligned-with`.

**Sources added:** 33 source entries.

**Where derivation was refused.** Only [[NL-GEMMA]] carries a sourced
`based-on` → NORA. For PETRA, ROSA and EAR the derivation from NORA is
highly likely but was not stated by any source, so it is recorded as
`related_entities` association rather than asserted as a relationship. This
is the single most repeated judgement in the batch: family membership is
claimable, derivation is not.

**Honest weak points:**
- **`NL-PETRA` is the weakest entity in the Atlas.** It rests on one
  sentence in one Wikipedia article. Its maintainer, its NORA relationship
  and even its acronym expansion are unsourced, and its `organisations:
  [NL-IPO]` link is an explicit Atlas assumption. It is included because
  Batch 4's scope names PETRA; the weakness is stated in the entity itself.
- **WILMA was deliberately not created**, though named in the same source
  sentence as PETRA — it is not in the batch scope and rests on the same
  single mention. The asymmetry is recorded in both entities' notes.
- **StUF was searched for and not created**: the search returned no usable
  source, and inventing one was not an option.
- `NL-RORA`'s `start_date: 2024-01-01` is a placeholder for "during 2024".
- `NL-BOMOS` has **no `maintained-by`** — custody is genuinely split across
  Forum Standaardisatie, NOiV, ECP and Logius.
- `NL-NEN-3610`'s `maintained-by` → Geonovum is `confidence: low`: the
  source says *aanspreekpunt*, which is weaker than the relationship claims.

**Threshold now met:** `DOMAIN-EDUCATION` connects two entities
([[NL-SURF]], [[NL-ROSA]]) and so qualifies under taxonomy §1. It was
**not** created here — Batch 4 is standards, not domains — and is queued for
Batch 5.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 62
entities.

**Next batch:** Batch 5 — Netherlands: Domains and Data Ecosystems.

---

## Batch 3 — Netherlands: Legislation and Regulation

**Date:** 2026-08-14

**Scope:** Dutch and applicable European legislation on data, privacy, data
sharing, digital government, open data, public information, archives,
digital identity, cybersecurity and information management, classified per
`metadata/taxonomy.md` §2.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked, so all
entities are `verification: search-only`.

**Entities added (15):**

*EU legislation (minimal anchors — Batch 8 deepens):*

| ID | Type | Note |
|---|---|---|
| `EU-GDPR` | regulation | Regulation (EU) 2016/679 |
| `EU-OPEN-DATA-DIRECTIVE` | directive | Directive (EU) 2019/1024 |
| `EU-NIS2` | directive | Directive (EU) 2022/2555 |

*Dutch implementation legislation (`region: EU`):*

| ID | Implements | Note |
|---|---|---|
| `NL-UAVG` | `EU-GDPR` | In force 25 May 2018 |
| `NL-WHO` | `EU-OPEN-DATA-DIRECTIVE` | Amended 2024 by Wet implementatie Open data richtlijn |
| `NL-CBW` | `EU-NIS2` | `status: planned`, in force 15 Aug 2026 |

*Dutch national legislation (`region: null`):*

| ID | Note |
|---|---|
| `NL-WOO` | In force 1 May 2022; supersedes `NL-WOB` |
| `NL-WDO` | Phased from 1 July 2023 |
| `NL-ARCHIEFWET-1995` | Superseded from 1 Jan 2027 |
| `NL-WET-BRP` | In force 6 Jan 2014 |
| `NL-WET-CBS` | CBS became a ZBO 1 Jan 2004 |
| `NL-TNO-WET` | 1930, in force 1932 |

*Retained for temporal integrity:*

| ID | Status |
|---|---|
| `NL-WOB` | `superseded` (1 May 2022), `successor: NL-WOO` |
| `NL-WBNI` | `active` with `end_date: 2026-08-15`, `successor: NL-CBW` |
| `NL-ARCHIEFWET-2026` | `planned`, in force 1 Jan 2027 |

**The first complete vertical chain.** Batch 3's main structural achievement
is that the Atlas can now express what it was built for:

```
EU-GDPR  →  NL-UAVG  →  NL-AP
(regulation) (implementing act) (supervisory authority)
```

with `applies-in → NL` on the EU entity rather than a Dutch copy of it.
Two further chains follow the same shape via `NL-WHO` and `NL-CBW`.

**Dangling Batch 2 relationships closed (5):** `NL-AP` (→ UAVG + GDPR),
`NL-NATIONAAL-ARCHIEF` (→ Archiefwet 1995, with `valid_until: 2027-01-01`),
`NL-CBS` (→ Wet op het CBS), `NL-TNO` (→ TNO-wet),
`NL-BASISREGISTRATIES` (→ Wet BRP, at `confidence: low` — see below).

**Relationships added:** 19 provenanced entries, including 4
`implements-requirement-from`, 3 `applies-in`, 3 `supersedes`, 4
`governed-by`, 4 `applies-to`, 1 `influences`.

**Sources added:** 42 source entries.

**Temporal modelling exercised for the first time.** Three supersession
chains are now represented with both `successor`/`previous_version` fields
and `supersedes` relationships carrying `valid_from` dates, and one
relationship (`NL-NATIONAAL-ARCHIEF` → Archiefwet 1995) carries a
`valid_until`. `NL-CBW` is recorded as `planned` with a commencement date of
15 August 2026 — the day after this batch was written — which makes it a
live demonstration of why `status` must never be read from a stale snapshot.

**Known gaps and honest weak points:**
- `NL-WHO` has **no `start_date`**: two sources gave conflicting
  entry-into-force dates (19 June vs 2 August 2024) and neither was
  preferred over the other.
- `NL-ARCHIEFWET-2026` appears under three different names across sources
  (Archiefwet 2021 / 2026 / "20xx"). The name is provisional; the ID is not.
- `NL-TNO-WET` is the weakest entity: a 1930 act with no located
  consolidated text and a Wikipedia secondary source.
- `NL-BASISREGISTRATIES` → `NL-WET-BRP` is recorded at `confidence: low`
  because the Wet BRP governs one registration, not the stelsel; the link
  should move to a BRP entity once the individual registrations exist.
- `NL-WDO` is classified as purely national, but its subject matter overlaps
  EU digital identity law; flagged for re-examination when eIDAS lands.
- Handelsregisterwet was **not** created — no adequate source was located,
  so `NL-KVK`'s statutory basis remains open rather than being filled with
  a guess.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 51
entities.

**Next batch:** Batch 4 — Netherlands: Standards, Frameworks and
Architecture (Forum Standaardisatie standards, GEMMA, EAR, ROSA, PETRA,
BOMOS, metadata/API/interoperability standards).

---

## Batch 2 — Netherlands: Organisations

**Date:** 2026-08-14

**Scope:** Expand the Dutch organisation graph across data governance,
digital government, information management, interoperability, standards,
public-sector data, statistics, research and digital infrastructure.

**⚠ Evidence standard:** unchanged from Batch 1 — page retrieval remained
blocked, so all substantive entities are `verification: search-only` with no
`accessed:` dates, `last_verified: null`, no `confidence: high`, and a
visible caveat in each body.

**Entities added (17):**

| ID | Type | Note |
|---|---|---|
| `NL-IPO` | organisation | Provinces (koepel) |
| `NL-UVW` | organisation | Water authorities (koepel) |
| `NL-CBS` | organisation | National statistical office, ZBO since 2004 |
| `NL-KADASTER` | organisation | Holds BRK |
| `NL-KVK` | organisation | Holds Handelsregister |
| `NL-RDW` | organisation | Holds BRV since 2008 |
| `NL-GEONOVUM` | organisation | Geo-standards |
| `NL-NEN` | organisation | National standards institute |
| `NL-NICTIZ` | organisation | Health information standards (`level: sectoral`) |
| `NL-AP` | organisation | Data protection authority |
| `NL-NATIONAAL-ARCHIEF` | organisation | Archives / information management |
| `NL-SURF` | organisation | Education & research ICT cooperative |
| `NL-TNO` | organisation | Applied research |
| `NL-BASISREGISTRATIES` | framework | Stelsel van Basisregistraties |
| `NL-NDS` | strategy | Nederlandse Digitaliseringsstrategie (July 2025) |
| `DOMAIN-GEOSPATIAL` | domain | Connects Kadaster + Geonovum |
| `DOMAIN-RESEARCH` | domain | Connects SURF + TNO |

**Entities updated:** `countries/nl/index.md` (restructured with grouped
organisation sections).

**Relationships added:** 9 provenanced entries (4 `participates-in` to the
base-registry system, 2 `participates-in` to OBDO/IBDS, 1 `references`,
1 `aligned-with`, 1 additional), plus lightweight reference lists.

**Sources added:** 45 source entries across the 17 entities.

**Two deliberate out-of-scope additions.** Batch 2 is nominally
organisations only; two non-organisation entities were added and the reason
is recorded in a "Scope note" section in each file:
- `NL-BASISREGISTRATIES` (framework) — without it, Kadaster, KVK and RDW
  would be three disconnected agency nodes rather than participants in one
  data system. Graph coherence was judged to outrank batch purity.
- `NL-NDS` (strategy) — surfaced during organisation research, is a
  high-priority national strategy that Batch 1 missed, and directly narrows
  the open question about whether NL DIGIbeter was superseded.

**Taxonomy discipline held.** `DOMAIN-HEALTH` (for Nictiz) and
`DOMAIN-EDUCATION` (for SURF) were **not** created, because
`metadata/taxonomy.md` §1 requires a domain to connect two or more entities
and each would currently connect one. Both are queued for Batch 5, and both
entities carry a note explaining the gap. `DOMAIN-EDUCATION` was caught by
`validate_relationships.py` after being referenced before creation — the
validator did its job.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, across 36 entities.

**Known gaps:**
- All 30 search-only entities (Batches 1+2) still need primary-source
  re-verification.
- `discovery/unresolved.md` now holds 20 open questions; 5 new ones from
  this batch concern NDS continuity under a new cabinet, the
  basisregistraties↔FDS relationship, CBS's responsible ministry, the
  reported 1 Jan 2027 Archiefwet revision, and three entity-typing calls.
- 21 items queued in `discovery/research-queue.md`, including CIO Rijk, Het
  Waterschapshuis, VNG Realisatie, CCS, AcICT, DANS/Health-RI/RIVM/NWO,
  SIDN, BOMOS, and the ten individual basisregistraties.
- Several organisations (`NL-AP`, `NL-NEN`, `NL-NATIONAAL-ARCHIEF`) have
  **no relationships recorded**, because their defining links are to
  legislation (Batch 3) or to EU/international bodies (Batches 8–13) that
  do not yet exist. These are documented gaps, not omissions.
- `NL-KVK` is the weakest entity in the batch: its only general-profile
  source is Wikipedia, low in the README's source preference order.

**Next batch:** Batch 3 — Netherlands: Legislation and Regulation. This is
where several currently-dangling organisation relationships get closed.

---

## Batch 1 — Netherlands: Core Data Governance

**Date:** 2026-08-14

**Scope:** Core Dutch data-governance landscape — Forum Standaardisatie,
IBDS, Federatief Datastelsel, NORA, Common Ground, MIDO, Data Agenda
Overheid, NL DIGIbeter, and the organisations and governance bodies
connecting them.

**⚠ Evidence standard for this batch:** the 15 substantive entities were
compiled from **search-engine results only**. The environment's network
egress policy blocked every attempt at direct page retrieval, so no cited
source was actually read. This was raised as a blocker and the reduced
standard was then accepted explicitly. Consequences, applied consistently:

- all 15 substantive entities carry `verification: search-only`
  (`DOMAIN-GOVERNMENT`, the 16th, is a taxonomy node making no factual
  claims and needs no external sourcing);
- no entity claims `confidence: high` (validation now enforces this);
- no `accessed:` dates are recorded on sources (nothing was accessed);
- `last_verified` is `null` throughout;
- each entity body opens with a visible sourcing caveat;
- unverified specifics (dates, thresholds, recent governance decisions) are
  named as unverified in prose rather than stated flatly.

**Entities added (16):**

| ID | Type | Folder |
|---|---|---|
| `DOMAIN-GOVERNMENT` | domain | `domains/` |
| `NL-BZK` | organisation | `organisations/` |
| `NL-FORUM-STANDAARDISATIE` | organisation | `organisations/` |
| `NL-OBDO` | organisation | `organisations/` |
| `NL-LOGIUS` | organisation | `organisations/` |
| `NL-ICTU` | organisation | `organisations/` |
| `NL-VNG` | organisation | `organisations/` |
| `NL-IBDS` | strategy | `strategies/` |
| `NL-DIGIBETER` | strategy | `strategies/` |
| `NL-DATA-AGENDA-OVERHEID` | strategy | `strategies/` |
| `NL-PAS-TOE-OF-LEG-UIT` | policy | `policies/` |
| `NL-NORA` | framework | `frameworks/` |
| `NL-FDS` | framework | `frameworks/` |
| `NL-MIDO` | programme | `programmes/` |
| `NL-COMMON-GROUND` | initiative | `initiatives/` |
| `NL-GDI` | platform | `platforms/` |

**Entities updated:** `countries/nl/index.md` (curated NL hub, previously
empty).

**Relationships added:** 13 provenanced entries in `relationships:` lists
(4 `maintained-by`, 2 `owned-by`, 1 `produces`, 1 `implements`, 1
`implemented-by`, 1 `part-of`, 1 `governed-by`, 1 `applies-to`, 1
`applies-in`, 1 `participates-in`), plus lightweight
`organisations:`/`related_entities:`/`domains:` references throughout. Of
the provenanced entries, 8 are `source: fact` and 5 are
`source: interpretation` — the interpretations are the IBDS↔FDS link, the
entity-type judgements, and three relationships recorded from the
organisation's side for navigability.

**Sources added:** 38 source entries across the 16 entities, all URLs
returned by web search (none invented, none read).

**Schema/tooling changes made during this batch:**
- Added optional `verification` field (`primary-source` | `search-only` |
  `unverified`) to the metadata schema, documented in
  `metadata/metadata-schema.md` and `metadata/controlled-vocabularies.md`,
  and added to `templates/entity-template.md`.
- `validate_frontmatter.py`: validates `verification`; rejects
  `confidence: high` on search-only/unverified entities; suppresses the
  `last_verified` reminder where it would be by-design noise.
- `validate_relationships.py`: rejects self-referencing relationship
  targets (added after one slipped into a draft).
- `validate_sources.py`: exempts `type: domain` taxonomy nodes from the
  missing-sources warning.
- Added `DOMAIN` as a valid ID scope in `metadata/schema.json` and
  `metadata/ontology.md` §2.1 — `DOMAIN-GOVERNMENT` was rejected by the
  Batch 0 pattern, a genuine gap between `taxonomy.md` and the schema.
- Both new checks were tested against injected violations to confirm they
  actually fire.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, across 19 entities.

**Known gaps:**
- All 16 entities need a primary-source re-verification pass (see
  `progress/current-batch.md`).
- 12 specific open questions recorded in `discovery/unresolved.md`, covering
  status/temporal questions (FDS establishment, IBDS evaluation, whether
  NL DIGIbeter is superseded), factual details (the €50,000 threshold, the
  2006 Forum establishment date, GDI's expansion) and three entity-typing
  judgements.
- 8 follow-on research items queued in `discovery/research-queue.md`
  (IPO, UvW, CIO Rijk, College Standaardisatie, individual GDI services,
  GEMMA/EAR/ROSA/PETRA, individual open standards, MIDO sub-documents).
- No legislation yet (Batch 3), no EU links yet (Batch 7+).

**Next batch:** Batch 2 — Netherlands: Organisations.

---

## Batch 0 — Repository Architecture

**Date:** 2026-08-14

**Scope:** Implement repository structure, ontology, taxonomy, relationship
model, metadata schema, controlled vocabularies, templates, validation
rules and contribution guidelines. No broad Netherlands/EU/UN research
performed.

**Entities added:**
- `NL` (`countries/nl/nl.md`) — country anchor
- `EU` (`regions/eu/eu.md`) — region anchor
- `UN` (`international/un/un.md`) — organisation anchor, international level

All three are structural anchors with `coverage: low`, sourced only to
ISO/official EU/UN homepages — not researched content.

**Entities updated:** None (repository was empty of entities before this batch).

**Relationships added:** None yet — the three anchors have no
`relationships:` entries; they exist to be targeted by future entities'
`applies-in`/`country`/`region` fields.

**Sources added:** 3 (one per anchor entity — ISO 3166 OBP for NL, and the
official EU and UN websites).

**Structure/tooling created:**
- Repository folders: `initiatives/`, `legislation/`, `policies/`,
  `strategies/`, `standards/`, `frameworks/`, `programmes/`,
  `organisations/`, `data-spaces/`, `platforms/`, `publications/`,
  `domains/`, `countries/nl/`, `regions/eu/`, `international/un/`,
  `metadata/`, `templates/`, `discovery/`, `validation/`, `progress/`,
  `.github/workflows/` — each populated with a scope-defining `README.md`
  where relevant.
- `metadata/ontology.md`, `metadata/taxonomy.md`,
  `metadata/relationship-types.md`, `metadata/metadata-schema.md`,
  `metadata/controlled-vocabularies.md`, `metadata/schema.json`.
- `templates/entity-template.md`.
- `CONTRIBUTING.md`.
- `discovery/candidates.md`, `discovery/unresolved.md`,
  `discovery/duplicates.md`, `discovery/research-queue.md` (all empty —
  no research performed yet).
- `validation/common.py` + `validate_ids.py`, `validate_frontmatter.py`,
  `validate_links.py`, `validate_relationships.py`, `validate_sources.py`,
  `run_all.py`, `requirements.txt`.
- `.github/workflows/validate.yml` — runs `validation/run_all.py` on every
  PR and push to `main`.
- `README.md` — repository structure diagram updated to include
  `platforms/`, `publications/`, and the full `metadata/` file list.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, against the 3 anchor entities plus navigation pages.

**Design decisions:** recorded in `metadata/ontology.md` §6; summarised in
the Batch 0 completion report delivered to the user.

**Known gaps:** No substantive content yet — Batches 1–15 are all still
open. See `progress/backlog.md`.

**Next batch:** Batch 1 — Netherlands: Core Data Governance (Forum
Standaardisatie, Federatief Datastelsel, IBDS, NORA, Common Ground, MIDO,
Data Agenda Overheid, NL Digitaal, and related programmes). Awaiting
approval before starting, per the task brief's instruction to stop after
Batch 0.
