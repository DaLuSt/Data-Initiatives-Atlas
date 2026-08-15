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
- [ ] **Batch 9 — EU Organisations and Standards.** European Commission and
  relevant DGs, Eurostat, EDPB, EDPS, ENISA, European Parliament, Council of
  the EU, Publications Office, CEN, CENELEC, ETSI, SEMIC, relevant
  programmes/partnerships; DCAT, DCAT-AP, interoperability frameworks,
  SEMIC specs, data-space/API/cloud/AI/cybersecurity standards.
- [ ] **Batch 10 — EU Data Spaces.** Health, Mobility, Energy, Finance,
  Agriculture, Manufacturing, Skills, Tourism, Public Administration, Green
  Deal, Research, Media — purpose, governance, standards, legislation,
  infrastructure, participating countries, related initiatives.
- [ ] **Batch 11 — EU Validation.** Full audit, with particular attention to
  the EU→national legislative chain and EU→national standards chain.

## International / UN

- [ ] **Batch 12 — UN Core.** UN Data Strategy, UN Digital Strategy, UN 2.0,
  Global Digital Compact, SDG data initiatives, UN statistical initiatives,
  UN Data Commons, UN digital-government initiatives.
- [ ] **Batch 13 — UN Agencies and International Organisations.** UN DESA,
  UNDP, UNCTAD, UNESCO, WHO, UNECE, OECD, World Bank, ITU, ISO, IEC, W3C,
  IETF, other authoritative international organisations — correctly typed
  and leveled, UN-system vs. non-UN kept distinct.
- [ ] **Batch 14 — International Standards and Frameworks.** Global
  standards/frameworks for data governance, metadata, data quality,
  interoperability, information management, digital identity,
  cybersecurity, AI, data sharing, APIs, knowledge graphs.
- [ ] **Batch 15 — Global Validation.** Validate the international layer and
  its relationships to the EU layer.

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
