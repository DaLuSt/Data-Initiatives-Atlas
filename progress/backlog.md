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
  term between `national` and `local`, so no German Land, no Belgian Region
  and no Spanish Comunidad Autónoma is representable — and `regional` cannot
  be reused because it already means supra-national. Confirmed general by
  Belgium and given a **third distinct shape** by Spain; three of five
  countries are affected. The Atlas's best-evidenced ontology defect by a
  wide margin. Blocks OSLO, Digitaal Vlaanderen, the Länder, seventeen
  Spanish regional open data portals, and several other queued items.
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
- [ ] **A cybersecurity domain entity.** Well over twenty entities across
  three layers and five countries qualify under the taxonomy §1 threshold.
  Deliberately not created inside a country batch.
- [ ] **The Open Data Directive transpositions for Belgium and France.**
  Neither identified. Both countries have a well-known *earlier* open data
  act (2016 in both cases) that looks like the answer and chronologically
  cannot be it. **Spain closed its equivalent gap** — [[ES-LEY-37-2007]] as
  amended in 2021 — and had the same trap dated 2007, so three of five
  countries have it and it is a research hazard, not a coincidence. Two of
  five gaps remain.
- [ ] **Resolve [[FR-NIS2-LOI]]'s status.** Sources contradict each other
  on whether France's NIS2 transposition is in force. The only entity in
  the Atlas with that problem.
- [ ] **Connect the DPAs to the EDPB.** **Five** national data protection
  authorities, one sourced link. Five page reads would fix four edges.
- [x] **A third country.** **Done 2026-08-15: Belgium**, 14 entities.
  Confirmed the model reusable a third time, and confirmed the federal
  limitation is **general** — and worse in Belgium, where `regional` is
  already taken by the supra-national meaning. See `progress/completed.md`.
- [x] **A fourth country — a *unitary* one.** **Done 2026-08-16: France**,
  11 entities. Raised **no new ontology question at all** — the first
  country of which that is true — which isolates the federal `level` gap as
  the model's single real defect. See `progress/completed.md`.
- [x] **A fifth country outside the founding-six / Benelux-DACH group.**
  **Done 2026-08-16: Spain**, 17 entities. Southern European, a later
  enlargement, and a constitutional form none of the others use — and still
  no ontology, schema, folder, validation or generator change. The model is
  **not western-European-shaped**. It also gave the federal `level` gap a
  **third distinct shape** (Comunidades Autónomas), which localises the
  defect in the vocabulary rather than in any country's constitution. See
  `progress/completed.md`.
- [ ] **A sixth country outside western Europe entirely.** All five are
  western European EU member states. A central or northern European state
  (Poland, Estonia) — or a non-EU one — would test the two assumptions five
  EU members cannot: that the EU layer is the right regional parent, and
  that `applies-in` is the right way to attach a country to it.

## Opened by the Spain batch

- [ ] **Create an `EU-ESS` entity for the European Statistical System.** The
  single highest-value modelling fix available. The sources describe
  Eurostat and the national statistical offices as members of one system;
  the Atlas currently expresses that as one weak `related-to` edge marked
  `source: interpretation` ([[ES-INE]]). One entity with `part-of` edges
  would connect **four** national statistical offices at once and close most
  of the statistics cluster properly.
- [ ] **Decide whether the national legal-instrument rank should be
  modelled.** Spain's `Ley Orgánica` has constitutional rank and can only be
  amended by absolute majority; `type: law` flattens that, as it already
  flattens *Gesetz*/*Verordnung*, *wet*/*koninklijk besluit* and
  *loi*/*ordonnance*. Five countries have been modelled without the field;
  adding it now means re-reading every instrument.
- [ ] **Decide whether partial implementation is expressible.**
  [[ES-LOPDGDD]] implements the GDPR *with part of itself* — its Title X on
  digital rights descends from nothing European. Relationships are
  whole-entity to whole-entity. One example so far; do not add a type on one.
- [ ] **Resolve [[ES-LCGC]]'s passage.** When Spain's NIS2 transposition
  becomes law, the Centro Nacional de Ciberseguridad becomes a real entity
  and the INCIBE/CCN competence split becomes modellable.
- [ ] **Confirm the DCAT-AP-ES alignment is in force.** [[ES-NTI-RISP]]'s
  `based-on` [[EU-DCAT-AP]] is `confidence: low` because the model is in
  administrative processing.
- [ ] **Model Red.es**, so [[ES-DATOS-GOB-ES]] can carry a `maintained-by`
  edge like the Dutch and German portals do.

## Explicitly out of scope for now

- Countries beyond the five modelled (structure supports them; no content
  until a country is actually researched — README §"Country Participation
  Model").
- Any graph database — Git + Markdown/YAML remains the sole source of truth
  (README §"Source of Truth").
