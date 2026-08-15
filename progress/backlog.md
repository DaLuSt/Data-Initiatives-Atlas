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
- [ ] **Batch 6 — Netherlands Validation.** Full duplicate/ID/link/metadata/
  source/relationship/status audit of everything added in Batches 1–5.
  ⚠ **Blocked in substance by the search-only debt** — see
  `progress/current-batch.md`. The automated suite already passes; what
  Batch 6 additionally asks for (outdated information, incorrect statuses,
  missing sources, unsupported relationships) requires reading primary
  sources. Do Batch 1b first.

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
- [ ] **Batch 11 — EU Validation.** Full audit, with particular attention to
  the EU→national legislative chain and EU→national standards chain.
  ⚠ **Blocked in substance by the search-only debt**, exactly as Batch 6 is.
  The automated suite passes; status/source/relationship accuracy needs
  primary sources. Do the re-verification pass first.

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
- [ ] **Batch 15 — Global Validation.** Validate the international layer and
  its relationships to the EU layer. ⚠ **Blocked in substance by the
  search-only debt**, as Batches 6 and 11 are — and most acutely here, since
  the international layer is the weakest-sourced in the Atlas.

## Final passes (after all batches above)

- [ ] **Final Global Relationship Pass** — vertical (UN→EU→National→Sector),
  horizontal (country↔country), standards, legislative and organisational
  relationship sweeps.
- [ ] **Final Quality Gate** — repository-wide ontology, metadata, sources,
  relationships, geography and technical-integrity review per the task
  brief §27.

## Explicitly out of scope for now

- Countries other than the Netherlands (structure supports them; no content
  until a country is actually researched — README §"Country Participation
  Model").
- Any graph database — Git + Markdown/YAML remains the sole source of truth
  (README §"Source of Truth").
