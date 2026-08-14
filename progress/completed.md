# Completed Batches

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
