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
- [ ] **Batch 2 — Netherlands: Organisations.** Expand the Dutch
  organisation graph (ministries, executive agencies, public authorities,
  standards bodies, research organisations, sector organisations) — only
  where there is a meaningful relationship to the data/digital ecosystem.
- [ ] **Batch 3 — Netherlands: Legislation and Regulation.** Dutch and
  applicable EU legislation on data, privacy, data sharing, digital
  government, open data, public information, archives, digital identity,
  AI, cybersecurity, interoperability, digital infrastructure, information
  management — classified per `metadata/taxonomy.md` §2.
- [ ] **Batch 4 — Netherlands: Standards, Frameworks and Architecture.**
  Forum Standaardisatie standards, NORA, GEMMA, EAR, MIDO, ROSA, PETRA,
  metadata/API/interoperability/data-quality/security standards, connected
  to their maintaining organisation.
- [ ] **Batch 5 — Netherlands: Domains and Data Ecosystems.** Government,
  Mobility, Health, Finance, Geospatial, Environment, Energy, Education,
  Justice, Public Safety, Economy, Agriculture, Social Security, Research,
  Infrastructure; plus data spaces, federated ecosystems, national/open-data
  platforms, sectoral initiatives — only where they add real relationships.
- [ ] **Batch 6 — Netherlands Validation.** Full duplicate/ID/link/metadata/
  source/relationship/status audit of everything added in Batches 1–5.

## European Union

- [ ] **Batch 7 — EU Core Initiatives.** European Data Strategy, Digital
  Decade, European interoperability initiatives, European data spaces,
  European digital identity, digital sovereignty, digital infrastructure,
  AI strategy, cybersecurity strategy.
- [ ] **Batch 8 — EU Legislation.** GDPR, Data Governance Act, Data Act,
  Open Data Directive, eIDAS/European Digital Identity, AI Act, NIS2,
  Cybersecurity Act, Interoperable Europe Act, Single Digital Gateway, and
  relevant sector-specific legislation — relevance assessed, not assumed.
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
