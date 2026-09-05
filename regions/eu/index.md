# European Union — Index

Curated navigation hub for all EU-scoped (`region: EU`) entities in the
Atlas. Human-maintained; add a wikilink here when a new EU-scoped entity is
judged important enough to belong on the region's front page.

Anchor entity: [[EU]]

> **Sourcing caveat.** Every entity below was compiled from search-engine
> results only and carries `verification: search-only`. See
> `progress/current-batch.md`.

## Strategies

- [[EU-DATA-STRATEGY]] — A European strategy for data (Feb 2020)
- [[EU-CYBERSECURITY-STRATEGY]] — Cybersecurity Strategy for the Digital Decade (Dec 2020)

## Programmes

- [[EU-DIGITAL-DECADE]] — Digital Decade Policy Programme 2030

## Initiatives

- [[EU-COMMON-DATA-SPACES]] — Common European Data Spaces _(the 14 sectoral spaces are Batch 10)_
- [[EU-EUDI-WALLET]] — European Digital Identity Wallet

## Frameworks

- [[EU-EIF]] — European Interoperability Framework

## Legislation

### Data

- [[EU-GDPR]] — General Data Protection Regulation (Reg. 2016/679) → [[NL-UAVG]]
- [[EU-DGA]] — Data Governance Act (Reg. 2022/868) ⚠ repeal proposed ✅ 2026-08-28
- [[EU-DATA-ACT]] — Data Act (Reg. 2023/2854)
- [[EU-OPEN-DATA-DIRECTIVE]] — Open Data Directive (Dir. 2019/1024) ⚠ repeal proposed → [[NL-WHO]] ✅ 2026-08-28

### Statutory bases of the European systems

- [[EU-REG-223-2009]] — European statistics _(the legal basis of [[EU-ESS]])_
- [[EU-REG-1025-2012]] — European standardisation _(recognises [[EU-CEN]],
  [[EU-CENELEC]] and [[EU-ETSI]])_

### Third-country adequacy

- [[EU-UK-ADEQUACY]] — two decisions, 2021, with a sunset clause
- [[EU-CH-ADEQUACY]] — one decision, **2000**, with none _(Decision
  2000/518/EC, still in force under Article 45(9) GDPR)_ ✅ 2026-08-28

### Transport and trade

- [[EU-EMSWE]] — European Maritime Single Window environment (Reg.
  2019/1239) _(names [[UN-LOCODE]] in its common location database — the
  Atlas's only EU→UN/CEFACT edge; applicable from 15 Aug 2025)_ ✅ 2026-08-28

### Digital identity

- [[EU-EIDAS]] — eIDAS Regulation (Reg. 910/2014)
- [[EU-EIDAS2]] — European Digital Identity Framework (Reg. 2024/1183)

### Cybersecurity

- [[EU-NIS]] — NIS Directive (Dir. 2016/1148, adopted 6 Jul 2016) _(superseded 18 Oct 2024)_ → [[NL-WBNI]] ✅ 2026-08-28
- [[EU-NIS2]] — NIS2 Directive (Dir. 2022/2555) → [[NL-CBW]]
- [[EU-CER]] — Critical Entities Resilience Directive (Dir. 2022/2557)
- [[EU-CYBERSECURITY-ACT]] — Cybersecurity Act (Reg. 2019/881, adopted 17 Apr 2019) ✅ 2026-08-28

### Public services, interoperability and mobility

- [[EU-INTEROPERABLE-EUROPE-ACT]] — Interoperable Europe Act (Reg. 2024/903)
- [[EU-SDG]] — Single Digital Gateway Regulation (Reg. 2018/1724)
- [[EU-ITS-DIRECTIVE]] — ITS Directive (Dir. 2010/40/EU) → [[NL-NTM]]
- [[EU-EURO-7]] — Euro 7 vehicle emissions and battery durability
  regulation (Reg. 2024/1257) _(adopted, in force 28 May 2024, but not yet
  in effect — applies from 29 Nov 2026)_ ✅ 2026-08-28

### AI

- [[EU-AI-ACT]] — Artificial Intelligence Act (Reg. 2024/1689) _(high-risk
  timetable deferred to 2 Dec 2027 by [[EU-DIGITAL-OMNIBUS-AI]], Reg. (EU)
  2026/1744)_ ✅ 2026-08-28
- [[EU-DIGITAL-OMNIBUS-AI]] — "Digital Omnibus on AI" (Reg. (EU)
  2026/1744, COM(2025) 836), `amends` [[EU-AI-ACT]]. Adopted 8 Jul 2026,
  in force 27 Jul 2026. ✅ 2026-09-05

### Pending

- [[EU-DIGITAL-OMNIBUS]] — COM(2025) 837, Commission proposal, 19 Nov 2025.
  **Not adopted** (still under negotiation as of 24 Jul 2026). Would repeal
  [[EU-DGA]] and [[EU-OPEN-DATA-DIRECTIVE]] into [[EU-DATA-ACT]], and amend
  [[EU-GDPR]]. Corrected 2026-08-28: does **not** amend [[EU-AI-ACT]] — that
  is a distinct sibling proposal, [[EU-DIGITAL-OMNIBUS-AI]] (see above). ✅ 2026-08-28

## Cross-level chains established

Cybersecurity — the fullest chain in the Atlas, with both generations:

```
EU-CYBERSECURITY-STRATEGY  (Dec 2020)
   │ influences                    ╲ influences
EU-NIS2  ◄──supersedes── EU-NIS     EU-CER
   │                        │
NL-CBW   ◄──supersedes── NL-WBNI
```

Data protection, open data and mobility:

```
EU-GDPR                → NL-UAVG → NL-AP → (participates-in) EU-EDPB
EU-OPEN-DATA-DIRECTIVE → NL-WHO
EU-ITS-DIRECTIVE       → NL-NTM  → (part-of) NL-NDW
```

Standards — the first end-to-end international → EU → national descent:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
```

Membership chains, each resting on a sourced composition rule rather than a
source naming the Dutch body:

```
NL-AP  ──participates-in──→ EU-EDPB
NL-NEN ──participates-in──→ EU-CEN
NL-CBS ──participates-in──→ EU-EUROSTAT  (European Statistical System)
```

## Organisations

### Institutions
- [[EU-COMMISSION]] · [[EU-PARLIAMENT]] · [[EU-COUNCIL]]
- [[EU-PUBLICATIONS-OFFICE]] — publisher of EUR-Lex and the Official Journal

### Agencies and supervisors
- [[EU-ENISA]] — cybersecurity _(under [[EU-CYBERSECURITY-ACT]])_
- [[EU-EDPB]] — data protection board _(members include [[NL-AP]])_
- [[EU-EDPS]] — data protection supervisor
- [[EU-EUROSTAT]] — statistics _(ESS partner of [[NL-CBS]])_

### Standardisation
- [[EU-CEN]] _(members include [[NL-NEN]])_ · [[EU-CENELEC]] · [[EU-ETSI]]
- [[EU-SEMIC]] — semantic interoperability

### Data spaces support
- [[EU-DSSC]] — Data Spaces Support Centre

### Membership associations
- [[EU-EUROGEOGRAPHICS]] — the national mapping, cadastral and land registry
  authorities _(members include [[NL-KADASTER]], [[NO-KARTVERKET]],
  [[CH-SWISSTOPO]], [[GB-OS]], [[IE-TAILTE]])_ — the geospatial analogue of
  [[EU-ESS]]
- [[EU-GEANT]] — the national research and education networks _(37 NRENs plus
  NORDUnet; members include [[NL-SURF]] and [[DE-DFN]])_

The three associations follow one pattern — [[EU-ESS]] for statistics,
EuroGeographics for geospatial, GÉANT for research and education — and each
was invisible until it was modelled. The **edge type differs by legal shape**:
`part-of` for the ESS, whose members are constitutionally components of it
under [[EU-REG-223-2009]], and `participates-in` for the other two, whose
members are members of an association.

## Publications — the measurement layer

The Atlas's first `type: publication` entities, added 2026-08-21.

- [[EU-DESI]] — Digital Economy and Society Index _(four dimensions;
  standalone 2014–2022, then absorbed into the State of the Digital Decade
  report)_
- [[EU-EGOV-BENCHMARK]] — eGovernment Benchmark _(**35 countries**, every
  one of them already an Atlas anchor)_
- [[EU-VOLUNTARY-REVIEW-2023]] — the Union's first voluntary review to the
  [[UN-HLPF]]

All three now carry `measures` edges to the countries they assess — **62 of
them**, 27 from DESI and 35 from the benchmark. The `measures` relationship
type was added on 2026-08-21, one batch after the entities that needed it;
see `metadata/relationship-types.md` and `discovery/candidates.md` §3 for why
the separation was deliberate.

## Standards and reference architectures

- [[EU-EIF]] — European Interoperability Framework
- [[EU-DCAT-AP]] — metadata profile _(maintained by [[EU-SEMIC]])_
- [[EU-DSSC-BLUEPRINT]] — data spaces reference architecture

## Data Spaces

- [[EU-COMMON-DATA-SPACES]] — the umbrella; **all fourteen areas are now
  entities**
  - [[EU-EHDS]] — Health _(Reg. (EU) 2025/327 — **the only one with its own
    regulation**, and the only one carrying `applies-in` edges)_ ✅ 2026-08-28
  - [[EU-EOSC]] — Research and innovation _(**the most operational**: the EU
    Node has run since October 2024 and a federation of thirteen candidate
    nodes was demonstrated in 2025)_ ✅ 2026-08-28
  - [[EU-CEEDS]] — Energy _(Digital Europe Programme deployment; 15+ pilots
    across member states)_ ✅ 2026-08-28
  - [[EU-CULTURAL-HERITAGE-DATA-SPACE]] — Cultural heritage _(built on
    Europeana and its 52-60M+ digitised items — the one that started with the
    data already there)_ ✅ 2026-08-28
  - [[EU-MANUFACTURING-DATA-SPACE]] — Industry ✅ 2026-08-28
  - [[EU-FINANCIAL-DATA-SPACE]] — Finance _(FIDA is one of three components;
    the other two are unidentified)_
  - [[EU-LANGUAGE-DATA-SPACE]] — Language _(the one whose stated purpose
    includes **monetising** data)_
  - [[EU-EMDS]] — Mobility ✅ 2026-08-28
  - [[EU-GREEN-DEAL-DATA-SPACE]] — Green Deal _(references [[EU-INSPIRE]])_ ✅ 2026-08-28
  - [[EU-AGRI-DATA-SPACE]] — Agriculture ✅ 2026-08-28
  - [[EU-PUBLIC-ADMIN-DATA-SPACE]] — Public administrations _(⚠ `coverage: low`)_
  - [[EU-SKILLS-DATA-SPACE]] — Skills _(⚠ `coverage: low`)_
  - [[EU-TOURISM-DATA-SPACE]] — Tourism _(⚠ `coverage: low`)_
  - [[EU-MEDIA-DATA-SPACE]] — Media _(⚠ `coverage: low`)_

Four are still thin and say so. Completeness of the set is the claim; depth
is claimed only where `coverage` says so. See [[EU-COMMON-DATA-SPACES]].

## The international layer beneath the data spaces

- [[INTL-IDSA]] — International Data Spaces Association _(formed 2016)_
- [[INTL-IDS-RAM]] — its reference architecture model _(five layers;
  standardised in part as **DIN SPEC 27070** by [[DE-DIN]] — the first
  specification to connect to that entity from the standards side)_
- [[EU-GAIA-X]] — federated data infrastructure _([[DE-CATENA-X]] is
  `based-on` it)_

---

Last updated: 2026-08-18 (data spaces batch).
