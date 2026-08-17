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
- [x] **Connect the UN layer** — **Done 2026-08-16.** `UN → anything` was 0
  through five country batches; it is now `EU → UN` = 4 and
  `UN → national` = 5. 14 entities added, 7 rewired, no relationship type
  added and no sourcing standard lowered. The refused edges had been
  pointing at nodes that did not exist — [[EU-ESS]] and [[UN-UNSC]] are
  those nodes. See `progress/completed.md`.
- [ ] **Connect the UN layer's *legislative* half.** The batch connected the
  organisational statistics layer. `UN-FPOS` → `NL-WET-CBS` and
  `UN-FPOS` → `DE-BSTATG` are untouched: national statistical *legislation*
  still has no UN link, while the offices themselves now do.
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
- [x] **A cybersecurity domain entity.** **Done 2026-08-16:**
  [[DOMAIN-CYBERSECURITY]], connecting **23 entities** across three layers
  and five countries. Deliberately created outside a country batch, which is
  why it could be scoped by subject rather than by country. See
  `progress/completed.md`.
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
- [x] **A sixth country outside western Europe entirely.** **Done
  2026-08-16: Poland**, 10 entities. A 2004 accession state with a post-1989
  administrative tradition. **Both assumptions held** — the EU layer is the
  right regional parent and `applies-in` attached it unchanged. It raised
  two new questions, both about **time** rather than structure: an
  instrument in force *while the member state is before the CJEU*
  ([[PL-KSC]]), and a national system *subject to* a requirement it cannot
  meet ([[PL-MOBYWATEL]] and eIDAS 2.0). See `progress/completed.md`.
- [ ] **A seventh country outside the EU entirely.** All six are EU member
  states, so `applies-in` from EU instruments has never been tested against
  a country the EU cannot bind. A non-EU European state (Norway,
  Switzerland, the UK) would test whether the `region: EU` field and the
  `applies-in` mechanism still behave, or whether the Atlas has quietly
  assumed EU membership.

## Opened by the Spain batch

- [x] **Create an `EU-ESS` entity for the European Statistical System.**
  **Done 2026-08-16.** [[EU-ESS]] now carries [[EU-EUROSTAT]] and four
  national statistical offices by `part-of`, sourced to the composition rule
  in Regulation (EC) No 223/2009. [[ES-INE]]'s weak `related-to` edge was
  removed rather than left beside it.
- [ ] **Decide whether the binding force of an instrument should be
  modelled.** Two batches have now hit the same missing property from
  opposite directions. Spain: `type: law` flattens the constitutional rank
  of a `Ley Orgánica`, as it already flattens *Gesetz*/*Verordnung*,
  *wet*/*koninklijk besluit* and *loi*/*ordonnance*. The UN batch:
  [[UN-AARHUS]] is a binding convention and the
  [[UN-AI-ETHICS-RECOMMENDATION]] is non-binding soft law, and nothing
  distinguishes them. Six batches have run without the field; adding it now
  means re-reading every instrument.
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

## Opened by the UN-connection batch

- [ ] **Propose a relationship type for cooperation acts.** Two real EU↔UN
  interactions could not be recorded: the **UNESCO–European Commission
  agreement** on AI ethics implementation, and the **2023 EU voluntary
  review** submitted to UN SDG monitoring. Neither is adoption,
  implementation, governance or reference. Two examples is the threshold
  `metadata/relationship-types.md` §2.3 sets — this is the clearest live
  candidate for the next vocabulary change, and it should be decided by a
  batch that can read the sources.
- [ ] **Finish the geospatial cluster.** [[UN-GGIM]] and
  [[UN-GGIM-EUROPE]] exist and connect to [[UN]]; **no edge reaches
  [[EU-INSPIRE]]**. The missing middle is probably **EuroGeographics**,
  playing the role [[EU-ESS]] plays for statistics — not created, because
  every source found is its own site or trade press.
- [ ] **Connect UN/CEFACT to anything European.** [[UN-CEFACT]] is attached
  to [[UN-UNECE]] and to nothing else. The narrow, answerable question:
  *does any instrument already in this Atlas reference a UN/CEFACT
  standard?* UN/EDIFACT, UN/LOCODE and the Core Component Library are
  unmodelled.
- [ ] **`UN-FPOS` → national statistical legislation.** The batch connected
  the statistical *offices*; the *legislation* ([[NL-WET-CBS]],
  [[DE-BSTATG]]) still has no UN link.
- [ ] **INSEE.** France is now the only one of five countries with no
  statistical office in [[EU-ESS]] — a visible hole in a modelled structure
  rather than one absence among unconnected nodes.
- [ ] **Model Regulation (EC) No 223/2009**, [[EU-ESS]]'s legal base, and
  Regulation (EU) 1025/2012 for the European standardisation organisations.
  Deliberately left as a pair so the Atlas stays consistent about statutory
  bases.
- [ ] **Source [[INTL-OECD-CSSP]] from the OECD.** It is currently described
  entirely by a participant — one Eurostat page — which gives it two
  competing names (CSSP / CSTAT) and no independent confirmation.

## Opened by the basisregistraties batch

- [ ] **Propose relationship types for data movement.** The single clearest
  outstanding vocabulary decision, and now supported by **five** sourced
  examples across two batches:
  **authorised use** ([[NL-BELASTINGDIENST]] → [[NL-WOZ]], [[NL-RDW]] →
  [[NL-BRP]]), **key-sharing couplings** ([[NL-BRK]] ↔ [[NL-NHR]],
  [[NL-BAG]] ↔ [[NL-BRP]]), and the two EU↔UN cooperation acts from the UN
  batch. `metadata/relationship-types.md` §2.3's threshold is two.
- [ ] **Decide whether `authentiek gegeven` needs a field.** The legal status
  that makes a base registry authoritative — data other bodies must use and
  may not independently re-determine — appears in ten descriptions and
  nowhere in the structured data.
- [ ] **Model the Dutch statutes behind the registers.** Wet BAG, Wet BGT,
  Wet BRO, Wet WOZ, AWR Chapter IVA, Handelsregisterwet, Kadasterwet,
  Wegenverkeerswet. Named in descriptions, no entities. A legislation batch,
  not a registry one — and **[[NL-BRT]] has no sourced statute at all**.
- [ ] **Decide how to model Dutch municipalities.** They hold the [[NL-BAG]]
  and determine [[NL-WOZ]] values, and are absent from the graph. **Not** the
  federal `level` gap — `local` exists — but there is no obvious entity to
  create. Same question covers the [[NL-BGT]]'s seven bronhouder categories
  and SVB-BGT.
- [ ] **Settle the register typing.** The ten are `platform`; a
  basisregistratie is arguably a dataset with a legal status, and there is no
  `register` or `dataset` type.
- [ ] **Resolve [[NL-FDS]] ↔ [[NL-BASISREGISTRATIES]].** Open since Batch 2,
  untouched by this batch, and now more visible with the stelsel fully
  modelled.
- [ ] **Digimelding**, the stelsel's error-reporting facility, and
  **SVB-BGT**. Named in single sources, not created.

## Opened by the Poland batch

- [ ] **A relationship type for an unmet obligation.** [[PL-MOBYWATEL]] is
  subject to [[EU-EIDAS2]] and **cannot satisfy it**; the edge is recorded
  as `related-to` with the substance in the evidence string, because
  `implements-requirement-from` asserts the opposite and `governed-by`
  implies the arrangement works. This is a **sixth** sourced connection the
  vocabulary cannot express, and the one with the shortest fuse.
- [ ] **Model infringement status.** [[PL-KSC]] is `status: active` and
  Poland is before the CJEU for the delay that preceded it; [[ES-LCGC]] drew
  a reasoned opinion, the stage before referral. Neither fact is in the
  structured data.
- [ ] **The Polish cybersecurity authorities.** CSIRT NASK, CSIRT GOV and
  CSIRT MON. Poland and the Netherlands are now both countries with
  cybersecurity legislation modelled and **no cyber authority** — see
  [[DOMAIN-CYBERSECURITY]].
- [ ] **PESEL**, Poland's population register and the counterpart of
  [[NL-BRP]]. Named in [[PL-COI]]'s list of systems and nothing more.
- [ ] **Dz.U. citation for [[PL-ODO]]**, the weakest-sourced of the six
  national GDPR instruments — no ISAP or Dziennik Ustaw reference found.
- [ ] **Krajowe Ramy Interoperacyjności**, a Polish DCAT profile, the
  operator of [[PL-DANE-GOV-PL]], and the Act on Public Statistics behind
  [[PL-GUS]]. All named, none modelled.
- [ ] **GIODO**, the predecessor data protection authority. The sources say
  the President took over only *part* of its competencies, so no clean
  succession was asserted — the third institutional transformation the Atlas
  has touched, after Spain's completed one and Poland's pending COI one.

## Opened by the site filter batch

- [ ] **Filter state is not in the URL.** `applyRoute()` reads only an entity
  ID from the hash, so a filtered view cannot be shared or bookmarked. "Every
  cybersecurity entity in Poland" is now one click away and **zero clicks
  away for the next reader**, which undercuts the point of a public atlas.
- [ ] **`confidence` is close to a constant.** 317 of 346 typed relationships
  are `medium`, 27 are `low` and **2 are `high`**. That distribution is now
  visible in one glance, and it means the field currently carries almost no
  information. Either the criteria for `high` are unusable in practice, or
  the Atlas has been under-claiming; both are worth a deliberate pass rather
  than a per-entity fix.
- [ ] **A domain with no entity still gets a facet row**, labelled by its ID
  rather than a name. Nothing currently triggers this — `metadata/taxonomy.md`
  §1.3 requires a taxonomy row with the entity — but the generator reports it
  instead of hiding it, and a validator rule would catch it earlier.

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
  or it does so in none and the Dutch edge belongs on [[NL-UAVG]] alone.
- [ ] **[[EU-EIDAS]] has no `applies-in` edges**, although it is `active`
  and [[DE-BUNDID]] implements it. Every other active EU instrument in the
  matrix attaches to all six countries. ([[EU-NIS]] is also empty and that
  is correct — it is `superseded`.)
- [ ] **[[EU-INSPIRE]] applies in five countries and not the Netherlands.**
  `['BE', 'DE', 'ES', 'FR', 'PL']` — the founding country is the gap,
  despite [[DOMAIN-GEOSPATIAL]] and a national geo-portal. Almost certainly
  an omission predating the `applies-in` convention.
- [ ] **13 of 20 instruments apply in all six countries with no national
  instrument modelled at all** — 88 of the matrix's 120 cells. That is the
  single largest content gap the Atlas can now state precisely, and it is a
  research queue rather than a defect.

## Opened by the United Kingdom batch

- [ ] **The EU adequacy decisions for the UK.** Renewed **19 December 2025**
  for six years, to **27 December 2031**, following [[GB-DUAA]]. This is the
  most important single link between the UK and the EU data layer and **no
  entity or edge represents it**. It is also the only route by which a
  non-member country connects to the EU layer *as a matter of present EU
  law* rather than by history ([[GB-NIS-REGULATIONS]]) or derivation
  ([[GB-UK-GDPR]]).
- [ ] **`country` is a field, not an edge — and `GB` is an orphan anchor.**
  `validation/audit.py` reports `1 fully disconnected: ['GB']`. The other
  six anchors are reachable through frontmatter only because EU instruments
  point `applies-in` at them; the UK's 13 entities carry `country: GB`,
  which the generator does not emit as an association edge. Options: emit
  `country` as an association (≈250 new edges, changes every country's graph
  shape), or accept that a country anchor's reachability depends on EU
  membership. **The second is what the Atlas currently asserts, and it is
  wrong.**
- [ ] **A fan-out succession is not expressible.** [[GB-DSIT]]'s functions
  went three ways. `successor` is a single field, described in
  `metadata/metadata-schema.md` as a way to *chain* superseded entities, and
  a chain is the wrong shape for a split. Set to `null`, with the split in
  prose.
- [ ] **A status for "mandated, commencement unverified".** [[GB-ICO]] is
  being replaced by an Information Commission under [[GB-DUAA]] s.117, and
  the Atlas cannot establish whether that has happened. Distinct from
  [[FR-NIS2-LOI]]'s `unknown` (sources conflict) and [[ES-LCGC]]'s
  `proposed` (still a draft). [[GB-CSRB]] has the same problem.
- [ ] **An amendment relationship type — fourth data point, first with no
  workaround.** [[GB-DUAA]] amends [[GB-UK-GDPR]] *and* [[GB-DPA-2018]],
  both still in force, so neither Germany's `supersedes` nor France's and
  Poland's absorption is available. [[GB-CSRB]] → [[GB-NIS-REGULATIONS]] is
  a fifth case. This item has now survived four batches.
- [ ] **A UK geospatial entity.** Ordnance Survey is unmodelled and the
  Geospatial Commission was merged into [[GB-GDS]] in January 2025. The UK
  is the only country in the Atlas with **no entity in
  [[DOMAIN-GEOSPATIAL]]**.
- [ ] **The Cyber Assessment Framework**, the UK counterpart to [[NL-BIO]],
  [[DE-IT-GRUNDSCHUTZ]] and [[ES-ENS]] — all three modelled. Central to
  [[GB-CSRB]] and named by [[GB-NCSC]].
- [ ] **The UK Statistics Authority and the Office for Statistics
  Regulation.** Their absence weakens [[GB-ONS]]'s [[UN-CES]] edge, whose
  sources establish that *the UK* holds the seat without saying which body
  does.
- [ ] **A UK open data instrument.** Whether the Re-use of Public Sector
  Information Regulations survive as assimilated law was not researched, so
  [[GB-DATA-GOV-UK]] connects to [[EU-OPEN-DATA-DIRECTIVE]] not at all while
  four other countries have a sourced transposition.
- [ ] **A government source for the July 2026 machinery-of-government
  change.** [[GB-DCMS]] rests entirely on trade press; [[GB-DSIT]]'s
  abolition is reported, not cited.
- [ ] **A legislation.gov.uk citation for [[GB-DPA-2018]]** — every source
  found describes it through [[GB-DUAA]]'s changes to it, the same failure
  mode as [[PL-ODO]].

## Opened by the UK connection batch

- [ ] **`applies-in` to one's own country, for the other six.** The UK's
  national instruments now carry `applies-in` to [[GB]], which is what
  reconnected the orphaned anchor. The same is equally true of every
  national instrument in [[NL]], [[DE]], [[BE]], [[FR]], [[ES]] and [[PL]],
  and only [[NL-BIO]] and [[NL-PAS-TOE-OF-LEG-UIT]] carry it. Either do it
  everywhere or decide the convention is UK-specific and say why.
- [ ] **Who holds the UK's [[UN-CES]] seat?** [[GB-UKSA]] was created to
  settle it and did not. The participation is recorded on both the Authority
  and [[GB-ONS]]; one of those two edges is wrong.
- [ ] **The Office for Statistics Regulation**, and whether the other six
  countries have an oversight body above their statistical office that the
  Atlas simply has not researched. [[GB-UKSA]] is currently the only one.
- [ ] **Ordnance Survey of Northern Ireland.** [[GB-OS]] maps **Great
  Britain**; the UK-wide geospatial picture is incomplete without OSNI.
- [ ] **A British Standard, any British Standard.** [[GB-BSI]] participates
  in five standards bodies and maintains nothing the Atlas holds. The same
  is true of [[NL-NEN]] and [[DE-DIN]].
- [ ] **The Law Enforcement Directive** (Directive 2016/680), one of the two
  legal bases of [[EU-UK-ADEQUACY]] and not an Atlas entity, so that entity's
  `governed-by` edge names only [[EU-GDPR]].
- [ ] **A status for a future-dated lapse.** [[EU-UK-ADEQUACY]] is `active`
  with `end_date: 2031-12-27` — a sunset clause, not a historical end. Third
  variant of the status gap [[GB-ICO]] opened.
- [ ] **The sectoral NIS competent authorities** — energy, transport, health,
  drinking water. [[GB-OFCOM]] and [[GB-ICO]] are modelled; Schedule 1 names
  more.

## Explicitly out of scope for now

- Countries beyond the five modelled (structure supports them; no content
  until a country is actually researched — README §"Country Participation
  Model").
- Any graph database — Git + Markdown/YAML remains the sole source of truth
  (README §"Source of Truth").
