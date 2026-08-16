# Backlog

Full batch plan. Each batch is scoped, researched, validated and committed
independently — do not start the next one until the current one passes
validation (`CONTRIBUTING.md` — Batch workflow).

## Netherlands

- [x] **Batch 1 — Netherlands: Core Data Governance.** Done 2026-08-14, 16
  entities. **Search-only sourcing — owes a primary-source re-verification
  pass** (`grep -rl "verification: search-only" .`). See
  `progress/completed.md`.
- [ ] **Batch 1b — Re-verification of Batch 1.** Fetch and read the sources
  already cited on the 16 Batch 1 entities; confirm/correct claims; set
  `verification: primary-source`, `last_verified` and per-source
  `accessed:` dates; close the open rows in `discovery/unresolved.md`.
  Requires an environment with outbound HTTPS to public
  government/EU/standards domains. **Precondition for Batch 6.**
- [x] **Batch 2 — Netherlands: Organisations.** Done 2026-08-14, 17
  entities (13 organisations + 1 framework + 1 strategy + 2 domains).
  **Search-only sourcing — included in the Batch 1b re-verification debt.**
  See `progress/completed.md`.
- [x] **Batch 3 — Netherlands: Legislation and Regulation.** Done
  2026-08-14, 15 entities (3 EU anchors + 12 Dutch acts, including 3
  retained superseded/forthcoming instruments). Established the first
  complete EU→national→authority vertical chains. **Search-only sourcing —
  included in the Batch 1b re-verification debt.** AI legislation was *not*
  covered (no Dutch AI-specific act identified; the AI Act is Batch 8).
  See `progress/completed.md`.
- [x] **Batch 4 — Netherlands: Standards, Frameworks and Architecture.**
  Done 2026-08-14, 11 entities (5 reference architectures, 2 frameworks,
  4 standards), each standard connected to its maintainer. NORA family
  assembled; EAR→RORA succession recorded. **Search-only sourcing —
  included in the Batch 1b re-verification debt.** Not covered: the wider
  'pas toe of leg uit' standards list beyond Digikoppeling and ADR, StUF
  (no source found), WILMA, and data-quality standards specifically.
  See `progress/completed.md`.
- [x] **Batch 5 — Netherlands: Domains and Data Ecosystems.** Done
  2026-08-14, 10 entities (3 domains, 4 platforms, 3 data spaces/frameworks
  — counting `NL-ISHARE` as a framework). Domains created only on meeting
  the 2-entity threshold; Energy, Environment, Finance, Justice,
  Agriculture, Social Security and Built Environment remain below it and
  were deliberately not created. **Search-only sourcing — included in the
  Batch 1b re-verification debt.** See `progress/completed.md`.
- [x] **Batch 6 — Netherlands Validation.** Done 2026-08-14. Found and fixed
  2 defects (disconnected `NL-ISHARE`; `NL` anchor citing unconfirmed URLs).
  ⚠ **Partial by necessity** — status accuracy, currency and source content
  remain unchecked and need primary sources. See `validation/reports.md`.

## European Union

- [x] **Batch 7 — EU Core Initiatives.** Done 2026-08-14, 7 entities.
  Established the Atlas's first full strategy → EU law → national law
  chain. **Search-only sourcing**, and two entities (`EU-EIDAS2`,
  `EU-EUDI-WALLET`) rest entirely on **secondary** sources and need
  rebuilding in Batch 8. Not covered: digital sovereignty and EU AI
  strategy — no distinct, sourceable initiative found for either;
  digital-infrastructure funding instruments (Digital Europe Programme,
  EuroHPC) not researched. See `progress/completed.md`.
- [x] **Batch 8 — EU Legislation.** Done 2026-08-14, 11 new entities plus 2
  rebuilt (`EU-EIDAS2`, `EU-EUDI-WALLET`) and 7 updated. Added the
  `proposes-to-supersede` relationship type for pending repeals. Closed
  three dangling EU→national chains. **Search-only sourcing**, but most new
  entities now carry EUR-Lex citations. Not covered: sector-specific
  legislation beyond mobility (ITS) and cybersecurity; the Free Flow of
  Non-Personal Data Regulation; a EUR-Lex citation for the AI Act.
  See `progress/completed.md`.
- [x] **Batch 9 — EU Organisations and Standards.** Done 2026-08-14, 14
  entities. Completed the first end-to-end international → EU → national
  standards chain (DCAT → DCAT-AP → DCAT-AP-NL) and closed four dangling
  NL→EU links. **Search-only sourcing.** Not covered: Directorates-General
  (insufficient sourcing), Interoperable Europe Board, ETSI standards, API/
  cloud/AI/cybersecurity standards specifically, GeoDCAT-AP and StatDCAT-AP.
  See `progress/completed.md`.
- [x] **Batch 10 — EU Data Spaces.** Done 2026-08-14, 6 entities.
  ⚠ **Partial delivery of scope, deliberately.** Only 4 of the 14 data
  spaces were created — health (EHDS, well sourced), mobility, green deal
  and agriculture (purpose statements only). The other **ten were not
  created**: research returned only their names, and the brief asks for
  purpose/governance/standards/infrastructure. All ten are enumerated on
  `EU-COMMON-DATA-SPACES` and queued. Also added the Data Spaces Support
  Centre and its Blueprint. **Search-only sourcing.**
  See `progress/completed.md`.
- [x] **Batch 11 — EU Validation.** Done 2026-08-14. Found and fixed 1
  defect (disconnected `EU` anchor — an inconsistency with how the UN layer
  models membership). EU→national legislative and standards chains verified
  structurally. ⚠ **Partial by necessity.** See `validation/reports.md`.

## International / UN

- [x] **Batch 12 — UN Core.** Done 2026-08-14, 5 entities. **Search-only, and
  the weakest-sourced layer in the Atlas** — un.org material was largely
  unreachable through search. `UN-DATA-COMMONS` rests on a Grokipedia page;
  `UN-DATA-STRATEGY` has no dedicated source; `UN-GDC` is sourced only to an
  EU page. Not covered: UN Digital Strategy as a distinct entity, SDG data
  initiatives, UN digital-government initiatives (e.g. the E-Government
  Survey). See `progress/completed.md`.
- [x] **Batch 13 — UN Agencies and International Organisations.** Done
  2026-08-14, 7 entities. UN/non-UN distinction implemented in the ID scheme
  (`UN-` vs `INTL-`). **Not created: UN DESA, UNDP, UNESCO, WHO, UNECE** (no
  usable source found for any) and **World Bank** (omitted deliberately —
  its institutions are technically UN specialised agencies and
  misclassifying it is the error the brief warns against).
  See `progress/completed.md`.
- [x] **Batch 14 — International Standards and Frameworks.** Done
  2026-08-14, 2 new entities plus `INTL-DCAT` rebuilt on w3.org.
  ⚠ **Substantially under-delivered against its scope.** Of the eleven
  standard areas listed, **only information security (ISO/IEC 27001/27002)
  and metadata (DCAT) were covered.** Data quality, interoperability,
  information management, digital identity, AI, data sharing, APIs and
  knowledge graphs are all uncovered and queued.
  See `progress/completed.md`.
- [x] **Batch 15 — Global Validation.** Done 2026-08-14. **Principal
  finding: the UN layer is an island** — zero relationships connect its 9
  entities to any EU or NL entity. Country-neutrality holds; no duplicates;
  no orphans. ⚠ **Partial by necessity.** See `validation/reports.md`.

## Final passes (after all batches above)

- [x] **Final Global Relationship Pass** — done 2026-08-14. 12 sourced
  relationships added. Standards and legislative chains complete;
  organisational partial; **vertical incomplete — UN → EU is still 0**, and
  the two links that would close it were refused for want of a source.
- [x] **Final Quality Gate** — done 2026-08-14. Passes on ontology,
  metadata, temporal integrity, country-neutrality and technical integrity.
  **Does not pass on source verification** — no URL in the repository has
  been fetched. Two further Batch 0 defects found and fixed.
  See `validation/final-quality-gate.md`.

## Remaining work

- [ ] **Re-verification pass** — the single highest-value item. Needs
  outbound HTTPS; every URL is already recorded in entities' `sources:`.
- [ ] **Connect the UN layer** — `UN-UNSD` → `EU-EUROSTAT` and
  `UN-FPOS` → `NL-WET-CBS` would close most of the vertical gap. The
  Germany batch added two more candidates of the same shape
  (`DE-DESTATIS` → `EU-EUROSTAT`, `DE-BSTATG` → `UN-FPOS`), all four
  refused for want of a source and clustered in
  `discovery/unresolved.md`.
- [x] **Add a second country** — the only real test of the country-neutral
  model. **Done 2026-08-15: Germany**, 39 entities, no ontology change, no
  `DE-EU-*` duplicate, `applies-in` targets now `['DE', 'NL']`. See
  `validation/germany-second-country-report.md`.

## Opened by the Germany batch

- [ ] **Resolve the federal modelling gap.** The `level` vocabulary has no
  term between `national` and `local`, so no German Land and no Belgian
  Region is representable — and `regional` cannot be reused because it
  already means supra-national. Confirmed general by the Belgium batch, and
  now the Atlas's best-evidenced ontology defect. Blocks OSLO, Digitaal
  Vlaanderen, the Länder, and several other queued items.
- [ ] **Decide on an amendment relationship type.**
  `DE-NIS2UMSUCG` → `DE-BSIG` is recorded as `supersedes` at
  `confidence: low` for what is an amending act, with the two entities
  deliberately not agreeing. `relationship-types.md` §2.3 permits adding a
  type; it was not done on unread sources.
- [ ] **Settle what `country` means for a data space.** `DE-CATENA-X` and
  `NL-ISHARE` are two independent instances of the same problem — the field
  conflates origin, governance and operation.
- [ ] **`EU-INSPIRE` → `NL`.** Added with an `applies-in` to `DE` only,
  making an EU directive look German-specific. First-priority gap.
- [ ] **A cybersecurity domain entity.** Thirteen entities across three
  layers and three countries qualify under the taxonomy §1 threshold.
- [ ] **Belgium's Open Data Directive transposition.** Not identified; the
  2016 act found is PSI-era and chronologically cannot be it. Belgium is
  the only Atlas country without one recorded.
- [x] **A third country.** **Done 2026-08-15: Belgium**, 14 entities.
  Confirmed the model reusable a third time, and confirmed the federal
  limitation is **general** — and worse in Belgium, where `regional` is
  already taken by the supra-national meaning. See `progress/completed.md`.
- [ ] **A fourth country — a *unitary* one.** All three tests so far have
  been the Netherlands plus two federal states. A second unitary country
  (France, Spain, Ireland) would show whether anything else in the model is
  Netherlands-shaped, which the two federal cases could not isolate.

## Explicitly out of scope for now

- Countries other than the Netherlands and Germany (structure supports
  them; no content until a country is actually researched — README
  §"Country Participation Model").
- Any graph database — Git + Markdown/YAML remains the sole source of truth
  (README §"Source of Truth").
