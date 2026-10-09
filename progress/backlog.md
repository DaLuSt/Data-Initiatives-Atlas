# Backlog

Full batch plan. Each batch is scoped, researched, validated and committed
independently — do not start the next one until the current one passes
validation (`CONTRIBUTING.md` — Batch workflow).

> **Reconciled 2026-10-07 (roadmap issue #448).** Every item that was still unchecked
> was checked against the repository. Of 69, **39 were already done, superseded or
> decided** and are now ticked with what was found; the **30 still open** (six of them
> narrowed to what is left) each carry a pointer to the roadmap issue that now owns
> them: #457 vocabulary decisions (7), #458 Netherlands modelling (4), #459 United
> Kingdom (7), #460 coverage gaps (8), #461 consistency checks (4). The roadmap
> (`docs/roadmap.md`) is where open work is tracked; this file remains the history of
> the batches and the reasoning behind them.

## Netherlands

- [x] **Batch 1 — Netherlands: Core Data Governance.** Done 2026-08-14, 16
  entities. **Search-only sourcing — owes a primary-source re-verification
  pass** (`grep -rl "verification: search-only" .`). See
  `progress/completed.md`.
- [x] **Batch 1b — Re-verification of Batch 1.** **Done — verified 2026-10-07:** every one of the 740 entities is now `verification: primary-source`; the re-verification debt this item was part of is closed (`docs/re-verification.md` is the procedure that was used).
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
  rebuilding in Batch 8. **Digital sovereignty and EU AI strategy closed
  2026-09-25** — no distinct, sourceable initiative existed for either at
  the time (`discovery/unresolved.md` rows #39/#40), but both have since
  been presented by the Commission: [[EU-TECH-SOVEREIGNTY-PACKAGE]]
  (3 June 2026) and [[EU-AI-CONTINENT-ACTION-PLAN]] (9 April 2025). Not
  covered: digital-infrastructure funding instruments (Digital Europe
  Programme, EuroHPC) not researched. See `progress/completed.md`.
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

- [x] **Re-verification pass.** **Done — verified 2026-10-07:** `grep -rl "verification: search-only"` finds no entity; all 740 are `primary-source`.
- [x] **Connect the UN layer** — **Done 2026-08-16.** `UN → anything` was 0
  through five country batches; it is now `EU → UN` = 4 and
  `UN → national` = 5. 14 entities added, 7 rewired, no relationship type
  added and no sourcing standard lowered. The refused edges had been
  pointing at nodes that did not exist — [[EU-ESS]] and [[UN-UNSC]] are
  those nodes. See `progress/completed.md`.
- [x] **Connect the UN layer's *legislative* half.** Duplicate of the `UN-FPOS` → national statistical legislation item below, which carries the open work (roadmap #460).
- [x] **Add a second country** — the only real test of the country-neutral
  model. **Done 2026-08-15: Germany**, 39 entities, no ontology change, no
  `DE-EU-*` duplicate, `applies-in` targets now `['DE', 'NL']`. See
  `validation/germany-second-country-report.md`.

## Opened by the Germany batch

- [x] **Resolve the federal modelling gap.** **Done — verified 2026-10-07:** `level: subnational` exists and 23 entities carry it (`metadata/ontology.md` §4); Länder, Regions and Comunidades Autónomas are representable.
- [x] **Decide on an amendment relationship type.** **Done — verified 2026-10-07:** `amends` is in `metadata/relationship-types.md` (decided 2026-09-20; it applies however extensive the revision), and `DE-NIS2UMSUCG` → `DE-BSIG` and the UK cases use it.
- [ ] **Settle what `country` means for a data space.** `DE-CATENA-X` and
  `NL-ISHARE` are two independent instances of the same problem — the field
  conflates origin, governance and operation. → Roadmap #457.
- [x] **`EU-INSPIRE` → `NL`.** **Done — verified 2026-10-07:** `EU-INSPIRE` has `applies-in` for eleven countries including `NL`.
- [x] **A cybersecurity domain entity.** **Done 2026-08-16:**
  [[DOMAIN-CYBERSECURITY]], connecting **23 entities** across three layers
  and five countries. Deliberately created outside a country batch, which is
  why it could be scoped by subject rather than by country. See
  `progress/completed.md`.
- [ ] **The Open Data Directive transposition for France.** Belgium is done (`BE-HERGEBRUIK-WET-2023` and the three regional instruments, 2026-08/09). France has `FR-LOI-VALTER` and `FR-LRN` pointing at the earlier PSI Directive and no instrument linked to `EU-OPEN-DATA-DIRECTIVE`; the 2016 act looks like the answer and chronologically cannot be it. → Roadmap #460.
- [x] **Resolve [[FR-NIS2-LOI]]'s status.** **Done — verified 2026-10-07:** the contradiction was resolved on 2026-08-26 from ANSSI's own page (`status: planned`), and the Commission's CJEU referral of 8 July 2026 is a typed `referred-to-court-over` edge.
- [x] **Connect the DPAs to the EDPB.** **Done — verified 2026-10-07:** twenty national data protection authorities and the EDPS have `participates-in` edges to `EU-EDPB`.
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
- [x] **A sixth country outside western Europe entirely.** **Done
  2026-08-16: Poland**, 10 entities. A 2004 accession state with a post-1989
  administrative tradition. **Both assumptions held** — the EU layer is the
  right regional parent and `applies-in` attached it unchanged. It raised
  two new questions, both about **time** rather than structure: an
  instrument in force *while the member state is before the CJEU*
  ([[PL-KSC]]), and a national system *subject to* a requirement it cannot
  meet ([[PL-MOBYWATEL]] and eIDAS 2.0). See `progress/completed.md`.
- [x] **A seventh country outside the EU entirely.** **Done — verified 2026-10-07:** Norway, Switzerland, the United Kingdom, Iceland and Liechtenstein are all modelled; `applies-in` and `region: EU` coexist with non-EU countries.

## Opened by the Spain batch

- [x] **Create an `EU-ESS` entity for the European Statistical System.**
  **Done 2026-08-16.** [[EU-ESS]] now carries [[EU-EUROSTAT]] and four
  national statistical offices by `part-of`, sourced to the composition rule
  in Regulation (EC) No 223/2009. [[ES-INE]]'s weak `related-to` edge was
  removed rather than left beside it.
- [x] **Decide whether the binding force of an instrument should be modelled.** **Done — verified 2026-10-07:** the `type: law` split into `act`, `decision`, `subordinate-legislation` and `agreement` (#404), the `soft-law` type for non-binding instruments (#406) and the optional `rank` field (#408); `metadata/versioning.md` lists them.
- [ ] **Decide whether partial implementation is expressible.**
  [[ES-LOPDGDD]] implements the GDPR *with part of itself* — its Title X on
  digital rights descends from nothing European. Relationships are
  whole-entity to whole-entity. One example so far; do not add a type on one. → Roadmap #457.
- [ ] **Resolve [[ES-LCGC]]'s passage.** When Spain's NIS2 transposition
  becomes law, the Centro Nacional de Ciberseguridad becomes a real entity
  and the INCIBE/CCN competence split becomes modellable. → Roadmap #460.
- [ ] **Confirm the DCAT-AP-ES alignment is in force.** [[ES-NTI-RISP]]'s
  `based-on` [[EU-DCAT-AP]] is `confidence: low` because the model is in
  administrative processing. → Roadmap #460.
- [x] **Model Red.es.** **Done — verified 2026-10-07:** `ES-RED-ES` exists and `ES-DATOS-GOB-ES` is `maintained-by` it.

## Opened by the UN-connection batch

- [x] **Propose a relationship type for cooperation acts.** **Done — verified 2026-10-07:** `cooperates-with` exists (used for `UN-UNESCO` ↔ `EU-COMMISSION`, among others) and `EU-VOLUNTARY-REVIEW-2023` is modelled.
- [ ] **Finish the geospatial cluster.** Narrowed 2026-10-07: `EU-EUROGEOGRAPHICS` now exists (six national mapping agencies participate), but no edge reaches `EU-INSPIRE` from it, from `UN-GGIM` or from `UN-GGIM-EUROPE`. → Roadmap #460.
- [x] **Connect UN/CEFACT to anything European.** **Done — verified 2026-10-07:** `UN-EDIFACT`, `UN-LOCODE` and `UN-CCL` exist as `maintained-by` UN-CEFACT outputs, and `EU-EMSWE` `references` `UN-LOCODE`.
- [ ] **`UN-FPOS` → national statistical legislation.** The batch connected
  the statistical *offices*; the *legislation* ([[NL-WET-CBS]],
  [[DE-BSTATG]]) still has no UN link. → Roadmap #460.
- [x] **INSEE.** France is now the only one of five countries with no
  statistical office in [[EU-ESS]] — a visible hole in a modelled structure
  rather than one absence among unconnected nodes.
- [x] **Model Regulation (EC) No 223/2009 and Regulation (EU) 1025/2012.** **Done — verified 2026-10-07:** `EU-REG-223-2009` and `EU-REG-1025-2012` exist.
- [x] **Source [[INTL-OECD-CSSP]] from the OECD.** **Done — verified 2026-10-07:** it now cites the OECD's own `oecdgroups.oecd.org` body page alongside the Eurostat one.

## Opened by the basisregistraties batch

- [x] **Propose relationship types for data movement.** **Done — verified 2026-10-07:** `uses-data-from` and `carries-identifier-of` were added (#293) and carry the Dutch examples (`NL-BELASTINGDIENST` → `NL-WOZ`, `NL-RDW` → `NL-BRP`, `NL-BRK` → `NL-NHR`, `NL-BRP` → `NL-BAG`).
- [ ] **Decide whether `authentiek gegeven` needs a field.** The legal status
  that makes a base registry authoritative — data other bodies must use and
  may not independently re-determine — appears in ten descriptions and
  nowhere in the structured data. → Roadmap #458.
- [ ] **Model the Dutch statute AWR Chapter IVA.** Narrowed 2026-10-07: Wet BAG, BGT, BRO, WOZ, BRP, CBS, the Handelsregisterwet, Kadasterwet and Wegenverkeerswet are now entities, and `NL-BRT` is `governed-by` `NL-KADASTERWET`; only the AWR chapter is missing. → Roadmap #458.
- [ ] **Decide how to model Dutch municipalities.** They hold the [[NL-BAG]]
  and determine [[NL-WOZ]] values, and are absent from the graph. **Not** the
  federal `level` gap — `local` exists — but there is no obvious entity to
  create. Same question covers the [[NL-BGT]]'s seven bronhouder categories
  and SVB-BGT. → Roadmap #458.
- [ ] **Settle the register typing.** The ten are `platform`; a
  basisregistratie is arguably a dataset with a legal status, and there is no
  `register` or `dataset` type. → Roadmap #458.
- [x] **Resolve [[NL-FDS]] ↔ [[NL-BASISREGISTRATIES]].** **Done — verified 2026-10-07:** closed 2026-09-18 (`unresolved.md` rows #133 and #138); the relationship is sourced from FDS's own knowledge base.
- [x] **Digimelding and SVB-BGT.** **Done — verified 2026-10-07:** `NL-DIGIMELDING` and `NL-SVB-BGT` exist.

## Opened by the Poland batch

- [ ] **A relationship type for an unmet obligation.** [[PL-MOBYWATEL]] is
  subject to [[EU-EIDAS2]] and **cannot satisfy it**; the edge is recorded
  as `related-to` with the substance in the evidence string, because
  `implements-requirement-from` asserts the opposite and `governed-by`
  implies the arrangement works. This is a **sixth** sourced connection the
  vocabulary cannot express, and the one with the shortest fuse. → Roadmap #457.
- [ ] **Model the stages of an infringement.** Narrowed 2026-10-07: `referred-to-court-over` records the CJEU referral (`ES-LCGC`, `FR-NIS2-LOI`, `NL-WHO` and others); the stages before it (reasoned opinion) and after it (judgment) remain unmodelled. → Roadmap #457.
- [ ] **The Polish cybersecurity authorities.** Narrowed 2026-10-07: `PL-CSIRT-MON` and `PL-NASK` exist; CSIRT NASK and CSIRT GOV do not. → Roadmap #460.
- [x] **PESEL**, Poland's population register and the counterpart of
  [[NL-BRP]]. Modelled as [[PL-PESEL]] and [[PL-EWIDENCJA-LUDNOSCI]] in the
  second research-queue pickup, 2026-08-22.
- [x] **Dz.U. citation for [[PL-ODO]].** **Done — verified 2026-10-07:** it cites `eli.gov.pl/eli/DU/2018/1000` and `dziennikustaw.gov.pl/DU/2018/1000`.
- [x] **Krajowe Ramy Interoperacyjności, a Polish DCAT profile, the operator of [[PL-DANE-GOV-PL]] and the Act on Public Statistics.** **Done — verified 2026-10-07:** `PL-KRI`, `PL-DCAT-AP-PL`, `PL-USTAWA-STATYSTYCE-1995` exist and `PL-DANE-GOV-PL` is `maintained-by` `PL-MC`.
- [ ] **GIODO**, the predecessor data protection authority. The sources say
  the President took over only *part* of its competencies, so no clean
  succession was asserted — the third institutional transformation the Atlas
  has touched, after Spain's completed one and Poland's pending COI one. → Roadmap #460.

## Opened by the site filter batch

- [x] **Filter state is not in the URL.** **Done — verified 2026-10-07:** the address carries the view, focus, depth, filters, search, layout and names, so a filtered view can be shared; `docs/graph.md` describes it.
- [x] **`confidence` is close to a constant.** Superseded: re-counted 2026-10-07 over 1,565 typed relationships, 1,020 are `medium`, 501 `high` and 44 `low`; the field carries information now.
- [ ] **A domain with no entity still gets a facet row**, labelled by its ID
  rather than a name. Nothing currently triggers this — `metadata/taxonomy.md`
  §1.3 requires a taxonomy row with the entity — but the generator reports it
  instead of hiding it, and a validator rule would catch it earlier. → Roadmap #461.

## Opened by the comparison matrix

All three were produced by putting the countries side by side; none is
visible from any single entity.

- [ ] **The GDPR supervisory authority is modelled inconsistently.** Seven
  entities carry `implements-requirement-from` [[EU-GDPR]]. Six are national
  laws. The seventh is [[NL-AP]] — an **organisation**, and the only
  supervisory authority in the Atlas that carries the edge.
  [[BE-APD]], [[DE-BFDI]], [[ES-AEPD]], [[FR-CNIL]] and [[PL-UODO]] do not.
  Decide which pattern is right and apply it to all six: either the
  authority implements the GDPR's Chapter VI requirement in every country,
  or it does so in none and the Dutch edge belongs on [[NL-UAVG]] alone. → Roadmap #461.
- [x] **[[EU-EIDAS]] has no `applies-in` edges.** **Done — verified 2026-10-07:** it has `applies-in` for 30 countries.
- [x] **[[EU-INSPIRE]] applies in five countries and not the Netherlands.** **Done — verified 2026-10-07:** see the `EU-INSPIRE` → `NL` item above.
- [x] **13 of 20 instruments apply in all six countries with no national instrument modelled.** Superseded: the counts date from the six-country Atlas; the live **Compare** view derives the same picture for every country and shows where the gaps are.

## Opened by the United Kingdom batch

- [x] **The EU adequacy decisions for the UK.** **Done — verified 2026-10-07:** `EU-UK-ADEQUACY` exists (`governed-by` `EU-GDPR` and `EU-LED`, `references` `GB-UK-GDPR` and `GB-DUAA`).
- [x] **`country` is a field, not an edge — and `GB` is an orphan anchor.** **Done — verified 2026-10-07:** `validation/audit.py` reports no fully disconnected entities; thirteen UK instruments and bodies point `applies-in` or `part-of` at `GB`.
- [ ] **A fan-out succession is not expressible.** [[GB-DSIT]]'s functions
  went three ways. `successor` is a single field, described in
  `metadata/metadata-schema.md` as a way to *chain* superseded entities, and
  a chain is the wrong shape for a split. Set to `null`, with the split in
  prose. → Roadmap #457.
- [ ] **A status for "mandated, commencement unverified".** [[GB-ICO]] is
  being replaced by an Information Commission under [[GB-DUAA]] s.117, and
  the Atlas cannot establish whether that has happened. Distinct from
  [[FR-NIS2-LOI]]'s `unknown` (sources conflict) and [[ES-LCGC]]'s
  `proposed` (still a draft). [[GB-CSRB]] has the same problem. **Update 2026-10-07:** the `GB-ICO` case itself resolved: the change took effect on 30 September 2026 and is modelled (`GB-INFORMATION-COMMISSION` succeeds `GB-ICO`); the missing status value remains for the next mandated-but-uncompleted change. → Roadmap #457.
- [x] **An amendment relationship type — fourth data point.** **Done — verified 2026-10-07:** `amends` exists (see above) and is used for `GB-DUAA` and `GB-CSRB`.
- [x] **A UK geospatial entity.** **Done — verified 2026-10-07:** `GB-OS` and `GB-GEOSPATIAL-STRATEGY` are in `DOMAIN-GEOSPATIAL`.
- [x] **The Cyber Assessment Framework.** **Done — verified 2026-10-07:** `GB-CAF` exists.
- [x] **The UK Statistics Authority.** **Done — verified 2026-10-07:** `GB-UKSA` exists (the question of who holds the `UN-CES` seat stays open, roadmap #459).
- [ ] **A UK open data instrument.** Whether the Re-use of Public Sector
  Information Regulations survive as assimilated law was not researched, so
  [[GB-DATA-GOV-UK]] connects to [[EU-OPEN-DATA-DIRECTIVE]] not at all while
  four other countries have a sourced transposition. → Roadmap #459.
- [ ] **A government source for the July 2026 machinery-of-government
  change.** [[GB-DCMS]] rests entirely on trade press; [[GB-DSIT]]'s
  abolition is reported, not cited. → Roadmap #459.
- [x] **A legislation.gov.uk citation for [[GB-DPA-2018]].** **Done — verified 2026-10-07:** it cites `legislation.gov.uk/ukpga/2018/12/part/4` and the DUAA's Part 5.

## Opened by the UK connection batch

- [ ] **Reconsider `applies-in` to one's own country — probably by removing
  it, not extending it.** The loose-nodes batch examined the blanket pass and
  declined it. 72 national instruments lack the edge; adding all 72 would
  make **72 of 181** `applies-in` edges tautological, and the type is defined
  as *"the primary mechanism for country-neutral applicability"* — one
  supra-national instrument reaching many countries. The Compare view already
  filters `applies-in` by scope for exactly this reason. The eight existing
  cases ([[NL-BIO]], [[NL-PAS-TOE-OF-LEG-UIT]] and the six UK ones) are the
  anomaly. Decide deliberately; do not let it spread by default. → Roadmap #461.
- [ ] **Who holds the UK's [[UN-CES]] seat?** [[GB-UKSA]] was created to
  settle it and did not. The participation is recorded on both the Authority
  and [[GB-ONS]]; one of those two edges is wrong. → Roadmap #459.
- [x] **The Office for Statistics Regulation.** **Done — verified 2026-10-09:** `GB-OSR` exists, `part-of` `GB-UKSA`. Still open, and now only a question: whether the other six countries have an oversight body above their statistical office that the Atlas has not researched (roadmap #459 stays open for it).
- [x] **Ordnance Survey of Northern Ireland.** **Done — verified 2026-10-09:** `GB-OSNI` exists (`subnational`; part of Land and Property Services, itself not modelled).
- [ ] **A British Standard, any British Standard.** [[GB-BSI]] participates
  in five standards bodies and maintains nothing the Atlas holds. The same
  is true of [[NL-NEN]] and [[DE-DIN]]. → Roadmap #459.
- [x] **The Law Enforcement Directive.** **Done — verified 2026-10-07:** `EU-LED` exists and `EU-UK-ADEQUACY` is `governed-by` it.
- [ ] **A status for a future-dated lapse.** [[EU-UK-ADEQUACY]] is `active`
  with `end_date: 2031-12-27` — a sunset clause, not a historical end. Third
  variant of the status gap [[GB-ICO]] opened. → Roadmap #457.
- [ ] **The sectoral NIS competent authorities** — energy, transport, health,
  drinking water. [[GB-OFCOM]] and [[GB-ICO]] are modelled; Schedule 1 names
  more. → Roadmap #459.

## Resolved 2026-08-18 — own-country `applies-in`

Earlier batches recorded that own-country `applies-in` should be
**reconsidered rather than extended**, and declined to add it to eighteen
national acts.

**That is now settled the other way, on the maintainer's instruction**, and
written into `metadata/relationship-types.md` §2.3: every entity must reach
its scope anchor, and an instrument with no other edge takes `applies-in` to
its own country.

The original objection was not wrong — the edge does give `applies-in` a
second, weaker meaning alongside the EU-instrument-reaches-member-state one
that makes the Atlas country-neutral. The trade was judged worth it: a second
meaning that is documented, enforced and visible in the ontology costs less
than two dozen entities being invisible in the graph.

What remains open is the **presentation** question, not the modelling one:
the site does not distinguish an anchor edge from a researched one, so a
reader counting `applies-in` edges will over-count cross-border
applicability. Anchor edges are identifiable — every one ends its evidence
with a sentence saying so — so a filter or a badge is buildable.

- [ ] **Distinguish anchor edges in the interactive graph**, so the
  `applies-in` count means one thing again. → Roadmap #461.

## Opened by the structural review of 2026-08-18

A review after the intelligence-services batch, prompted by the question
"what should be added next". The full ranked detail is in
`discovery/candidates.md`; this is the actionable summary.

**Acted on immediately:** Norway, Switzerland and Ireland were added in the
batch of 2026-08-18. What follows is what that review found and did **not**
act on.

### Better value than any new country — **all four done 2026-08-18**

Completed in the cheap-structural-fixes batch. [[EU-EDPB]] went from 2 to 8
incoming edges, [[EU-CEN]] from 3 to 7, [[EU-ESS]] from 7 to 8.
[[FR-INSEE]], [[BE-NBN]], [[FR-AFNOR]], [[ES-UNE]], [[PL-PKN]],
[[NL-NCSC]] and [[PL-NASK]] were created. The items below are kept as the
record of what was outstanding.

- [x] **Connect the national DPAs to [[EU-EDPB]].** `EU-EDPB` has **2**
  incoming edges ([[NL-AP]] and [[EU-EDPS]]) against [[EU-ESS]]'s **6**.
  The Atlas holds eight data protection authorities and links one. The
  Spain batch called [[EU-ESS]] "the single highest-value item this batch
  produced"; the identical play is unplayed here and **needs no new
  entity**.
- [x] **INSEE.** **Done — verified 2026-10-07:** `FR-INSEE` exists.
- [x] **NBN, AFNOR, UNE, PKN** — the four missing national standards
  bodies. [[GB-BSI]] is the most connective UK entity; the pattern works.
- [x] **A Dutch cyber authority.** [[NL-CBW]] is a NIS2 act with no
  authority attached.

### The vocabulary the Atlas defines and does not use

- [x] **`technology`.** **Done — verified 2026-10-07:** `INTL-X-ROAD` and `INTL-IDS-CONNECTOR` are the first two.
- [x] **`publication`.** **Done — verified 2026-10-07:** `EU-DESI`, `EU-EGOV-BENCHMARK` and `EU-VOLUNTARY-REVIEW-2023` exist (oversight reports are still not modelled).
- [x] **`region` entities and the EEA Agreement.** **Done — verified 2026-10-07:** `INTL-EEA-AGREEMENT`, its Joint Committee and three decisions exist; `region` entities are still only `EU`, and the EEA is modelled as an agreement.
- [x] **`level: local`.** Decided: kept in the vocabulary and unused (`discovery/unresolved.md` #231).

### The domain layer is lopsided

Cybersecurity, government and national-security are 7/7. Geospatial is 3/7,
mobility 2/7, and **health, education and research are 1/7 — the
Netherlands only.**

- [ ] **A health-data batch for ES, BE, PL and GB.** Narrowed 2026-10-07: health entities now exist for NL, DE, FR, FI and DK; Spain, Belgium, Poland and the UK have none, in an Atlas that holds `EU-EHDS`. → Roadmap #460.

### Countries, ranked

Italy, Estonia (+ Finland, for NIIS/X-Road), Denmark, Sweden, Austria,
Czechia, Portugal. Reasoning and the structural argument for each are in
`discovery/candidates.md`.

- [x] **Iceland and Liechtenstein.** **Done — verified 2026-10-07:** both are modelled (`IS-*`, `LI-*`).

## Explicitly out of scope for now

- Countries beyond the five modelled (structure supports them; no content
  until a country is actually researched — README §"Country Participation
  Model").
- Any graph database — Git + Markdown/YAML remains the sole source of truth
  (README §"Source of Truth").
