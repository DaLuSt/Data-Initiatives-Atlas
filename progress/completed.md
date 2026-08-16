# Completed Batches

## Final Global Relationship Pass and Quality Gate

**Date:** 2026-08-14 · **Full report:** `validation/final-quality-gate.md`

### Relationship pass (§26)

Added **12 sourced relationships** (119 → 131); entities with no
relationship of their own fell from 35 to 29. `part-of` is now the most
common type (25).

- **Institutional membership**, extending the fix Batch 11 began: the UN
  layer modelled `part-of` and the EU layer did not. Added for Eurostat and
  SEMIC (→ Commission), ENISA/EDPB/EDPS/Publications Office (→ EU), and the
  four UN instruments (→ UN).
- **Links stated in prose but missing from frontmatter:** Commission
  `produces` the Cybersecurity Strategy; DSSC Blueprint `applies-to` the
  common data spaces.

Of the four patterns §26 asks for: **standards** and **legislative** chains
are complete; **organisational** is partial; **vertical is not** — UN → EU
remains 0, and the two links that would close it were examined and refused
again for want of a source.

### Quality gate (§27)

**Two further defects found and fixed**, both Batch 0 residue:

1. Four sources claimed `accessed` dates — **asserting access that never
   happened**. Removed.
2. The `NL`/`EU`/`UN` anchors claimed `last_verified` while marked
   `verification: unverified` — a direct contradiction. Set to null.

Together with Batches 6/11/15, **every defect this project's validation has
surfaced originated in its own earliest work** — an argument for running
gates earlier, not only at the end.

**Passes:** ontology coherence, ID uniqueness and stability, temporal
integrity (5 successor + 6 previous_version chains, 0 mismatches, 3
superseded entities retained), country-neutrality (no country-scoped copies
of supra-national entities), provenance labelling (120 fact / 11
interpretation), technical integrity (5/5 checks, 0 errors).

**Does not pass:** source verification. 119 of 125 entities rest on sources
nobody has read; **no URL in the repository has been fetched.** No entity
claims `confidence: high` or `coverage: high`, correctly.

**Structurally incomplete:** the UN layer connects to nothing outside
itself.

---

## Batches 6, 11 and 15 — Validation

**Date:** 2026-08-14

**Full findings:** `validation/reports.md`. New tool: `validation/audit.py`.

### What was and was not checkable

An earlier position in this project — that the validation batches could not
run at all until sourcing was fixed — **was too absolute.** Most of what the
batch briefs ask for is checkable without sources, and doing so found real
defects.

Checkable and checked: duplicates, invalid IDs, broken links, inconsistent
metadata, missing sources, weak-source reliance, unsupported relationships,
missing relationships/orphans, country-specific assumptions.

**Not checkable, not checked:** outdated information, incorrect statuses,
whether cited sources say what the Atlas claims, whether cited URLs resolve
at all. 119 of 125 entities rest on sources nobody has read.

### Three defects found and fixed

| Batch | Defect | Fix |
|---|---|---|
| 6 | `NL-ISHARE` fully disconnected — no inbound or outbound edges | Explicit `related-to` → `NL-DSGO`, marked `source: interpretation`, `confidence: low` |
| 6 | **`NL`, `EU`, `UN` anchors cite URLs written from background knowledge in Batch 0**, never confirmed by search or fetch | Marked `verification: unverified`; `confidence: high` → `medium` |
| 11 | `EU` anchor fully disconnected, while `UN` was not | `part-of` → `EU` added from Commission, Parliament and Council |

The anchor defect is the notable one: **self-inflicted in Batch 0**, against
the brief's explicit "never invent URLs". And the confidence downgrade was
*forced* by this repository's own validation rule — `validate_frontmatter.py`
rejects `confidence: high` on `unverified` entities. The rule caught its
author.

The `EU` anchor defect was an **inconsistency between layers**: the UN layer
modelled institutional membership and the EU layer did not.

### ⚠ Principal finding: the international layer is an island

| Direction | Count |
|---|---|
| EU → NL | 15 |
| NL → EU | 10 |
| NL → INTL | 2 |
| EU → INTL | 1 |
| **UN → anything** | **0** |

The 9 UN-scoped entities connect only to each other. The brief's target is
UN → EU → National → Sector; what exists is a connected EU↔NL graph plus an
**unattached UN component**.

Two links would close most of it — `UN-UNSD` → `EU-EUROSTAT` and
`UN-FPOS` → `NL-WET-CBS` — and **both were examined and refused for want of
a source.** Closing them is the highest-value research remaining.

### Clean results

- No duplicate names or aliases across 125 entities.
- No orphans remaining, no broken links, no invalid IDs, no vocabulary
  violations.
- **No country-scoped copies of supra-national entities** — README §16
  holds. 17 `applies-in` relationships, all targeting `NL`; the mechanism is
  exercised but untested with a second country.
- Every non-domain entity has ≥1 source. Only two entities rely solely on
  weak sources: `NL-PETRA` and `UN-DATA-COMMONS`.
- 119 provenanced relationships: 108 `fact`, 11 `interpretation`, every
  interpretation labelled.
- **No entity claims `confidence: high` or `coverage: high`.**

### Verdict

The graph is **internally coherent and honestly labelled**. It is **not
verified**. These reports certify structure, not truth, and should be re-run
after the re-verification pass.

---

## Batches 12–14 — UN and International Layer

**Date:** 2026-08-14

**⚠ Evidence standard:** unchanged — all entities `verification: search-only`.
The international layer is the **weakest-sourced** in the Atlas: un.org and
ietf.org material proved largely unreachable through search, and several
entities rest on a single indirect citation.

### Batch 12 — UN Core (5 entities)

| ID | Type | Note |
|---|---|---|
| `UN-2-0` | initiative | Sept 2023 policy brief; the quintet of change |
| `UN-DATA-STRATEGY` | strategy | ⚠ **weakest in the batch** — one indirect source |
| `UN-GDC` | policy | Global Digital Compact; only an EU source located |
| `UN-FPOS` | framework | Fundamental Principles of Official Statistics |
| `UN-DATA-COMMONS` | platform | ⚠ **single Grokipedia source** |

### Batch 13 — Agencies and International Organisations (7 entities)

The brief's warning — *"Do not incorrectly classify non-UN organisations as
UN organisations"* — is implemented **in the ID scheme**, not just in prose:

| UN system (`UN-`) | Non-UN (`INTL-`) |
|---|---|
| `UN-UNSD` — Statistics Division | `INTL-ISO` |
| `UN-UNCTAD` — data governance working group | `INTL-IEC` |
| `UN-ITU` — **specialised agency** | `INTL-W3C` |
| | `INTL-OECD` |
| | `INTL-IETF` ⚠ thinnest |

`UN-ITU` is the case where the distinction bites: it appears in
standards-ecosystem listings alongside ISO, IEC, W3C, IETF and ETSI, but is
a UN specialised agency and carries the `UN` scope accordingly.

### Batch 14 — International Standards (2 new, 1 rebuilt)

*(Batches 12–14 added **15** entities in total, plus the `INTL-DCAT`
rebuild. An earlier draft of this report and the Batch 12–14 commit message
said 14 and 126 respectively; both were off by one. Corrected here.)*

| ID | Note |
|---|---|
| `INTL-ISO-IEC-27001` | Closes the `NL-BIO` gap open since Batch 4 |
| `INTL-ISO-IEC-27002` | ⚠ cited URL resolves to the superseded 2013 edition |
| `INTL-DCAT` | **Rebuilt** on w3.org; confidence low → medium |

### Two international → national chains now complete

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
INTL-ISO-IEC-27001 + -27002 (ISO/IEC) → NL-BIO / BIO2
```

The DCAT rebuild matters: Batch 9 flagged the top of that chain as its
weakest link because no W3C source could be found. Batch 14 found
`w3.org/TR/vocab-dcat-3/` and the chain is now sourced end to end.

**Relationships added:** 9 provenanced entries.
**Sources added:** 24 source entries.

### Scope items deliberately not delivered

- **UN DESA, UNDP, UNESCO, WHO, UNECE** — all named in Batch 13's scope; **no
  usable source was located for any**, so none was created.
- **World Bank** — omitted deliberately. Its institutions are technically UN
  specialised agencies, making the UN/non-UN call genuinely tricky, and
  misclassifying it is the precise error the brief warns against.
- **Batch 14's standards list** names data governance, metadata, data
  quality, interoperability, information management, digital identity,
  cybersecurity, AI, data sharing, APIs and knowledge graphs. **Only
  information security and metadata were covered.** This is a substantial
  under-delivery and is recorded as such.

### Honest weak points

- `UN-DATA-COMMONS` cites **Grokipedia** — an AI-generated encyclopedia and
  the weakest citation anywhere in this Atlas.
- `UN-DATA-STRATEGY` has no source dedicated to it.
- `UN-GDC`, a UN instrument, is sourced **only to a European Commission news
  page**.
- `INTL-IETF` carries almost nothing beyond its category — yet IETF RFCs
  underpin the HTTPS/DNSSEC/mail standards mandated by
  `NL-PAS-TOE-OF-LEG-UIT`, a real chain left entirely unmodelled.
- `INTL-ISO` → `NL-NEN` is **not asserted**: unlike CEN, no membership
  composition rule was sourced.
- `UN-UNSD` → `EU-EUROSTAT` is **not asserted**: no source connects the
  European Statistical System to the UN statistical system, leaving the
  statistics chain stopping at the EU.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 125
entities.

**Next:** Batch 15 (Global Validation) and the Final Quality Gate — both of
which, like Batches 6 and 11, need primary sources before they mean
anything.

---

## Batch 10 — EU Data Spaces

**Date:** 2026-08-14

**Scope:** The common European data spaces — health, mobility, energy,
finance, agriculture, manufacturing, skills, tourism, public
administration, green deal, research, media — with purpose, governance,
responsible organisations, standards, legislation, infrastructure and
participating countries for each.

**⚠ Evidence standard:** unchanged — all entities `verification: search-only`.

**Entities added (6):**

| ID | Type | Note |
|---|---|---|
| `EU-EHDS` | data-space | Health — Reg. (EU) 2025/327, the only one with its own regulation |
| `EU-EMDS` | data-space | Mobility — purpose statement only |
| `EU-GREEN-DEAL-DATA-SPACE` | data-space | Green Deal — purpose statement only |
| `EU-AGRI-DATA-SPACE` | data-space | Agriculture — purpose statement only |
| `EU-DSSC` | organisation | Data Spaces Support Centre |
| `EU-DSSC-BLUEPRINT` | framework | Shared reference architecture for data spaces |

**Ten of the fourteen data spaces were deliberately not created.** Research
returned **only their names** for cultural heritage, energy, finance,
industry, language, media, public administrations, research and innovation,
skills and tourism — no purpose, governance, standards or infrastructure.
Batch 10's brief asks for exactly those attributes; ten entities whose whole
content would be "this is one of the fourteen" is the shallow-entity failure
the brief warns against. All ten are enumerated on
[[EU-COMMON-DATA-SPACES]] and queued.

**This batch is therefore a partial delivery of its scope, and says so.**
Three of the four created are thin (one sourced purpose sentence each) and
each states that in its own body. Only `EU-EHDS` is substantively
researched.

**The most useful entity is `EU-DSSC-BLUEPRINT`.** Its rulebook and
governance-framework model is the EU-level analogue of the Dutch
*afsprakenstelsel* pattern running through [[NL-FDS]], [[NL-DSGO]],
[[NL-ISHARE]] and [[NL-HEALTH-RI]]. **No relationship is asserted** — the
resemblance is an Atlas observation, recorded as interpretation and queued.
Confirming it would connect the Dutch and EU data-space layers structurally
rather than thematically.

**Two high-value links left unasserted**, both on the same principle that
has served this project well:
- `EU-EHDS` → `NL-HEALTH-RI`: Health-RI is the obvious candidate for the
  Dutch health data access body, but the HDAB designation phase runs
  2027–2029 and nothing sources it yet.
- `EU-EMDS` → `NL-NTM`: national access points look like the natural
  building blocks of a mobility data space, but no source says so.

**Relationships added:** 6 provenanced entries.
**Sources added:** 13 source entries.

**Honest weak points:**
- `EU-EHDS` has **no EUR-Lex citation** — the strongest source is the
  Parliament's Legislative Observatory file.
- `EU-EMDS`, `EU-GREEN-DEAL-DATA-SPACE` and `EU-AGRI-DATA-SPACE` are
  `confidence: low` placeholders with citations, not researched content.
- Two sources are third-party copies or project sites rather than
  Commission material.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 110
entities.

**Next batch:** Batch 11 — EU Validation. The same caveat applies as to
Batch 6: it cannot be completed in substance while the sourcing debt stands.

---

## Batch 9 — EU Organisations and Standards

**Date:** 2026-08-14

**Scope:** European Commission and DGs, Eurostat, EDPB, EDPS, ENISA,
European Parliament, Council of the EU, Publications Office, CEN, CENELEC,
ETSI, SEMIC; plus DCAT, DCAT-AP and related standards.

**⚠ Evidence standard:** unchanged — all entities `verification: search-only`.

**Entities added (14):**

*Institutions:* `EU-COMMISSION`, `EU-PARLIAMENT`, `EU-COUNCIL`
*Agencies and supervisors:* `EU-ENISA`, `EU-EDPB`, `EU-EDPS`,
`EU-EUROSTAT`, `EU-PUBLICATIONS-OFFICE`
*Standards bodies:* `EU-CEN`, `EU-CENELEC`, `EU-ETSI`, `EU-SEMIC`
*Standards:* `EU-DCAT-AP`, `INTL-DCAT`

**The first end-to-end standards chain.** Batch 4 sketched it in prose and
refused to assert it; Batch 9 completed it:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
```

This is the international → EU → national standards descent the brief's
final relationship pass calls for, and the first the Atlas holds
end-to-end. `INTL-DCAT` is also the Atlas's first `INTL`-scoped entity.

**Four dangling links closed:** `NL-AP` → `EU-EDPB`, `NL-NEN` → `EU-CEN`,
`NL-CBS` → `EU-EUROSTAT`, `EU-CYBERSECURITY-ACT` → `EU-ENISA`.

**A recurring evidence pattern, marked consistently.** Three of those
closures rest on **composition rules** rather than sources naming the Dutch
body: "the EDPB comprises representatives from each national supervisory
authority", "CEN brings together the national standardisation bodies of 33
European countries", "the ESS is the partnership between Eurostat and the
national statistical institutes". Each is a reasonable inference from a
sourced rule — not a guess, but not a direct citation either. Every one says
so in its `evidence` field at `confidence: medium`.

**Relationships added:** 10 provenanced entries.
**Sources added:** 27 source entries.

**Deliberate omissions:**
- **Directorates-General were not created.** DG CONNECT is named once as a
  DCAT-AP co-initiator; no DG structure research was done. Creating DG
  entities from a passing mention would repeat the `NL-PETRA` mistake.
- **No adoption relationships from Parliament/Council to the 16 legislative
  entities.** That would add 32 edges conveying one fact already implied by
  entity type, drowning the substantive chains. Recorded as a modelling
  question instead.
- **Interoperable Europe Board** not created — two passing mentions only.
- **Regulation 1025/2012 and Regulation 223/2009** described but not
  modelled; both are legislation and outside this batch's scope.

**Honest weak points:**
- `INTL-DCAT` has **no W3C source** — both citations are second-hand
  descriptions. The top of the flagship chain is its weakest link.
  Batch 14 should rebuild it, as Batch 8 rebuilt `EU-EIDAS2`.
- `EU-PUBLICATIONS-OFFICE` has no source describing it; its EUR-Lex
  publisher role is asserted from the Atlas's own citation practice, which
  is circular.
- `EU-ETSI` is the clearest incompleteness: ICT standardisation is central
  to this Atlas's subject, and **no ETSI standard was modelled**.
- `EU-EDPB` cites a commercial blog for an EU institution.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 104
entities.

**Next batch:** Batch 10 — EU Data Spaces.

---

## Batch 8 — EU Legislation

**Date:** 2026-08-14

**Scope:** GDPR, Data Governance Act, Data Act, Open Data Directive, eIDAS /
European Digital Identity, AI Act, NIS2, Cybersecurity Act, Interoperable
Europe Act, Single Digital Gateway, and relevant sector-specific
legislation — relevance assessed rather than assumed.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
entities are `verification: search-only`. Sourcing quality nonetheless
improved markedly: **most new entities carry EUR-Lex Official Journal
citations**, unlike Batch 7.

**Entities added (11):**

| ID | Type | Citation |
|---|---|---|
| `EU-DGA` | regulation | Reg. (EU) 2022/868 — EUR-Lex ✓ |
| `EU-DATA-ACT` | regulation | Reg. (EU) 2023/2854 — EUR-Lex ✓ |
| `EU-AI-ACT` | regulation | Reg. (EU) 2024/1689 — no EUR-Lex link found |
| `EU-EIDAS` | regulation | Reg. (EU) No 910/2014 — indirect only |
| `EU-NIS` | directive | Dir. (EU) 2016/1148 — superseded 18 Oct 2024 |
| `EU-CER` | directive | Dir. (EU) 2022/2557 — EUR-Lex ✓ |
| `EU-CYBERSECURITY-ACT` | regulation | Reg. (EU) 2019/881 — EUR-Lex summary ✓ |
| `EU-INTEROPERABLE-EUROPE-ACT` | regulation | Reg. (EU) 2024/903 — EUR-Lex ✓ |
| `EU-SDG` | regulation | Reg. (EU) 2018/1724 — EUR-Lex summary ✓ |
| `EU-ITS-DIRECTIVE` | directive | Dir. 2010/40/EU — EUR-Lex ✓ |
| `EU-DIGITAL-OMNIBUS` | regulation | COM(2025) 836 — **proposal, not adopted** |

**Entities rebuilt (2):** `EU-EIDAS2` and `EU-EUDI-WALLET` — Batch 7 flagged
both as resting entirely on secondary sources. Both are now built on the
EUR-Lex Official Journal text of Reg. (EU) 2024/1183 and the Commission's
Digital Building Blocks pages, with `confidence` raised low → medium. This
was Batch 8's stated first priority and it is done.

**Entities updated (7):** `EU-NIS2` (supersedes NIS), `NL-WBNI` (implements
NIS), `NL-NTM` (implements ITS Directive), `EU-CYBERSECURITY-STRATEGY`
(influences CER), `EU-GDPR` and `EU-OPEN-DATA-DIRECTIVE` (Omnibus notes),
`EU-EIF` (Interoperable Europe Act association), `NL-WDO` (eIDAS question
narrowed).

**New relationship type: `proposes-to-supersede`.** The Digital Omnibus
proposes to repeal the DGA and the Open Data Directive. `supersedes` would
assert something untrue — the repeal has not happened — while `references`
would understate it to the point of hiding a pending repeal from anyone
reading those entities. A purpose-built type was added and documented in
`metadata/relationship-types.md`, `controlled-vocabularies.md` and
`schema.json`. Pending legislation is a permanent feature of this domain, so
this will recur.

**Three dangling chains closed:**

| Chain | Closed by |
|---|---|
| `EU-NIS` → `NL-WBNI` | New `EU-NIS` entity |
| `EU-ITS-DIRECTIVE` → `NL-NTM` | New `EU-ITS-DIRECTIVE` entity |
| `EU-CYBERSECURITY-STRATEGY` → `EU-CER` | New `EU-CER` entity |

The ITS one is worth noting: Batch 5 refused to assert the relationship
because no source named the instrument. Three batches later the instrument
was found and the link made with a real citation — the honest gap was
closable, whereas a guess would have needed correcting.

The cybersecurity picture is now the Atlas's most complete, with both
generations and all three package elements:

```
EU-CYBERSECURITY-STRATEGY  (Dec 2020)
   │ influences                    ╲ influences
EU-NIS2  ◄──supersedes── EU-NIS     EU-CER
   │                        │
NL-CBW   ◄──supersedes── NL-WBNI
```

**Relationships added:** 18 provenanced entries.
**Sources added:** 26 source entries, the majority official.

**Relevance assessed, not assumed.** The brief warns against classifying
every digital regulation as a data initiative. Each borderline inclusion
carries an explicit justification in-file: the AI Act on training-data
governance and the proposed GDPR AI lawful basis; the Cybersecurity Act on
certification as a precondition for trusted data infrastructure; the SDG
Regulation on the once-only principle.

**Honest weak points:**
- `EU-AI-ACT` has **no EUR-Lex citation** — sourced to a specialist
  reference site and Wikipedia. Weakest of the new legislation entities.
- `EU-DIGITAL-OMNIBUS` has only a CELEX reference; all substance comes from
  law-firm commentary. Its **current** legislative status is unverified and
  time-sensitive.
- `EU-EIDAS` was created for structural reasons only; its own content is
  unresearched.
- The EIF ↔ Interoperable Europe Act relationship is **not asserted** — no
  source states how they relate, and it determines whether the EU
  interoperability layer has one root or two.
- `NL-WDO`'s EU origin remains unresolved: eIDAS 2.0 ruled out on dates,
  910/2014 plausible but unsourced. `region` stays `null`.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 90
entities.

**Next batch:** Batch 9 — EU Organisations and Standards. It would close
ENISA, the Interoperable Europe Board, EDPB/EDPS, and the
DCAT → DCAT-AP → DCAT-AP-NL standards chain.

---

## Batch 7 — EU Core Initiatives

**Date:** 2026-08-14

**Scope:** European Data Strategy, Digital Decade, European interoperability
initiatives, European data spaces, European digital identity, digital
sovereignty, digital infrastructure, AI strategy, cybersecurity strategy.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
entities are `verification: search-only`. **Two entities are additionally
weak** — see below.

**Note on batch order:** Batch 6 (Netherlands Validation) was skipped, on
the reasoning recorded in `progress/current-batch.md`: it cannot be
completed in substance while the sourcing debt stands. Proceeding to the EU
layer under the declared constraint was chosen over producing a hollow
validation report.

**Entities added (7):**

| ID | Type | Note |
|---|---|---|
| `EU-DATA-STRATEGY` | strategy | COM(2020) 66, 19 Feb 2020 |
| `EU-COMMON-DATA-SPACES` | initiative | Pillar 4 of the data strategy |
| `EU-DIGITAL-DECADE` | programme | Decision (EU) 2022/2481 |
| `EU-EIF` | framework | European Interoperability Framework |
| `EU-CYBERSECURITY-STRATEGY` | strategy | 16 Dec 2020 |
| `EU-EIDAS2` | regulation | Reg. 2024/1183 — **weakly sourced** |
| `EU-EUDI-WALLET` | initiative | **weakly sourced** |

**The Atlas's first full three-level chain.** Batch 7's main structural
result:

```
EU-CYBERSECURITY-STRATEGY   (strategy, Dec 2020)
        │ influences
EU-NIS2                     (directive, Dec 2022)
        │ implements-requirement-from
NL-CBW                      (Dutch act, in force Aug 2026)
        │ supersedes
NL-WBNI                     (predecessor Dutch act)
```

Strategy → EU legislation → national implementation → superseded
predecessor, all with provenanced relationships. This is the vertical
pattern the brief's final relationship pass calls for.

**Relationships added:** 7 provenanced entries — 3 `applies-in` (to NL),
1 `influences`, 1 `produces`, 1 `part-of`, 1 `based-on`.

**Sources added:** 15 source entries.

**⚠ Two entities are materially weaker than the rest.** [[EU-EIDAS2]] and
[[EU-EUDI-WALLET]] rest **entirely on secondary sources** — law-firm
articles, vendor blogs and Wikipedia. No EUR-Lex or Commission citation was
located for either, unlike [[EU-GDPR]], [[EU-NIS2]] and
[[EU-OPEN-DATA-DIRECTIVE]]. Both carry `confidence: low` and an explicit
in-file warning, and **Batch 8 should rebuild them** rather than merely
deepen them.

**Two scope items produced no entity, deliberately:**
- **Digital sovereignty** — named in the batch scope, but sources treat it
  as a framing within [[EU-DIGITAL-DECADE]] rather than a named initiative
  with its own governance. An entity for a theme would have nothing
  verifiable attached.
- **EU AI strategy** — searches returned AI-and-cybersecurity material
  rather than a clearly identifiable standalone strategy document. The AI
  Act is Batch 8. Recorded as an open scope question rather than invented.

**The 14 data spaces were deliberately not created.** They are listed in
prose on [[EU-COMMON-DATA-SPACES]] and queued for Batch 10, where the brief
requires researching each one's purpose, governance, standards, legislation
and participating countries. Fourteen thin entities from a single list would
be precisely the shallow-entity failure the brief warns against.

**Highest-value open question raised:** is [[NL-NORA]] formally the
Netherlands' National Interoperability Framework under [[EU-EIF]]?
Confirming it would connect the EU and Dutch framework layers directly. Only
an association is recorded; no relationship asserted.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 79
entities.

**Next batch:** Batch 8 — EU Legislation. Priority: rebuild `EU-EIDAS2` and
`EU-EUDI-WALLET` on official sources.

---

## Batch 5 — Netherlands: Domains and Data Ecosystems

**Date:** 2026-08-14

**Scope:** Dutch data domains, data spaces, federated data ecosystems,
national and open-data platforms, and sectoral data initiatives.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
substantive entities are `verification: search-only`.

**Entities added (10):**

*Domains (created only on meeting the 2-entity threshold):*

| ID | Members that justified it |
|---|---|
| `DOMAIN-EDUCATION` | `NL-SURF`, `NL-ROSA` |
| `DOMAIN-HEALTH` | `NL-NICTIZ`, `NL-HEALTH-RI` |
| `DOMAIN-MOBILITY` | `NL-NDW`, `NL-NTM` |

*Platforms:*

| ID | Note |
|---|---|
| `NL-DATA-OVERHEID` | National open data portal; depends on `NL-DCAT-AP-NL` |
| `NL-PDOK` | Geodata platform, founded 2013 |
| `NL-NDW` | National road traffic data portal, opened 2009 |
| `NL-NTM` | National access point for mobility data — an EU obligation |

*Data spaces and ecosystems:*

| ID | Note |
|---|---|
| `NL-HEALTH-RI` | Federated national health data infrastructure |
| `NL-DSGO` | Built-environment agreement framework |
| `NL-ISHARE` | Trust framework used to establish data spaces |

**Entities updated:** `NL-SURF`, `NL-ROSA`, `NL-NICTIZ` retro-tagged with
their new domains, and the notes explaining the previously-missing domains
rewritten to record that the gap is closed. Plus `countries/nl/index.md`.

**The domain threshold held, and paid off.** `DOMAIN-EDUCATION` was withheld
in Batch 2 (SURF alone) and again in Batch 4 (SURF + ROSA, but wrong batch);
`DOMAIN-HEALTH` was withheld in Batch 2 (Nictiz alone). Both were created
here only once genuinely justified. Seven further domains named in the Batch
5 brief — Energy, Environment, Finance, Justice, Agriculture, Social
Security, Built Environment — remain **below the threshold and were not
created**, which is the rule working as intended rather than the batch being
incomplete.

**Relationships added:** 4 provenanced entries (`depends-on`,
`participates-in`, `part-of`, and one interpretation), plus domain tagging
across 6 entities.

**Sources added:** 26 source entries.

**A near-complete EU chain, deliberately left open.** [[NL-NTM]] exists
because every European country must have a national access point for
mobility data. The obligation is sourced; **the instrument imposing it is
not** — no source located named it. So `region: EU` is set and the
obligation described in prose, but no `implements-requirement-from` is
asserted. Batch 8 should close it.

**Honest weak points:**
- [[NL-ISHARE]] is recorded `country: NL` on its Dutch origin, but presents
  at ishare.eu in a European context. This is the country-neutral model's
  hardest case — a national initiative that went cross-border — and is
  flagged for resolution in Batch 10 rather than guessed now.
- [[NL-DSGO]]'s `start_date` combines two separate statements ("launched 18
  June" + "programme ended June 2024") into one date. That inference is
  marked as an inference.
- [[NL-DATA-OVERHEID]]'s `organisations: [NL-BZK]` is an Atlas association,
  not a sourced operator claim.
- [[NL-HEALTH-RI]] and [[NL-NDW]] both have genuine typing ambiguity
  (infrastructure vs organisation; platform vs organisation).

**New schema question raised.** Four entities now carry a `YYYY-01-01`
`start_date` meaning "year known, day unknown" ([[NL-RORA]], [[NL-PDOK]],
[[NL-ISHARE]], partly [[NL-DSGO]]). A January-1st placeholder is
indistinguishable from a real 1 January date — a genuine data-quality
problem. Recorded in `discovery/unresolved.md` as a schema question:
either adopt a convention or add a `date_precision` field.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 72
entities.

**Next batch:** Batch 6 — Netherlands Validation. Note that Batch 6 cannot
be completed properly while the search-only sourcing debt stands; see
`progress/current-batch.md`.

---

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

---

# Germany — Second Country (2026-08-15)

**Scope:** Germany as the second national scope, following the Final
Quality Gate's identification of *"a second country — the only real test of
the country-neutral model"* as one of three outstanding items.

**Entities added: 39.** 125 → **164**.

- **Country anchor (1):** `DE` (`countries/de/de.md` + `index.md`).
- **Strategies (4):** `DE-DIGITALSTRATEGIE`, `DE-DATENSTRATEGIE`,
  `DE-MODERNISIERUNGSAGENDA-BUND`, `DE-MODERNISIERUNGSAGENDA-FOEDERAL`.
- **Initiatives (2):** `DE-DEUTSCHLAND-STACK`, `DE-GDI-DE`.
- **Organisations (9):** `DE-BMDS`, `DE-BMI`, `DE-IT-PLANUNGSRAT`,
  `DE-FITKO`, `DE-KOSIT`, `DE-BSI`, `DE-DESTATIS`, `DE-BFDI`, `DE-DIN`.
- **Legislation (11):** `DE-BDSG`, `DE-IFG`, `DE-DNG`, `DE-IWG`
  (superseded), `DE-EGOVG`, `DE-OZG`, `DE-REGMOG`, `DE-BSIG`,
  `DE-NIS2UMSUCG`, `DE-BSTATG`, `DE-GEOZG`.
- **Standards and frameworks (5):** `DE-XOEV`, `DE-XRECHNUNG`,
  `DE-DCAT-AP-DE`, `DE-IT-GRUNDSCHUTZ`, `DE-IT-ARCHITEKTURRICHTLINIEN`.
- **Platforms (3):** `DE-GOVDATA`, `DE-BUNDID`, `DE-MOBILITHEK`.
- **Data spaces (2):** `DE-MDS`, `DE-CATENA-X`.
- **Supra-national, reached through German research (2):** `EU-INSPIRE`,
  `EU-GAIA-X` — both `country: null`, deliberately not German-scoped.

**Existing entities modified: 15.** `applies-in` → `DE` added alongside the
existing `applies-in` → `NL` on `EU-GDPR`, `EU-NIS2`, `EU-CER`,
`EU-DATA-ACT`, `EU-DGA`, `EU-OPEN-DATA-DIRECTIVE`, `EU-AI-ACT`,
`EU-CYBERSECURITY-ACT`, `EU-EIDAS2`, `EU-SDG`,
`EU-INTEROPERABLE-EUROPE-ACT`, `EU-ITS-DIRECTIVE`, `EU-EHDS`, `EU-EIF`,
`EU-DIGITAL-DECADE`.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, against 164 entities. `audit.py` reports no
duplicates, no fully disconnected entities, no weak-source-only German
entity, and country-neutrality holding: `targets: ['DE', 'NL']`.

**Result:** the country-neutral architecture holds. Adding a country
required **no change** to `metadata/schema.json`, `metadata/ontology.md`,
`metadata/taxonomy.md`, `metadata/relationship-types.md`, the folder
structure or any validation rule, and produced **no `DE-EU-*` entity**.
Four EU instruments now have two national implementations each; the DCAT
standards chain forks across both countries.

**Principal finding — negative:** the model is **lossy for federal
states**. The `level` vocabulary has no term between `national` and
`local`, so Germany's sixteen Länder are not representable. No sub-national
level was invented.

**Known gaps:** unchanged sourcing position — 155 of 164 entities are
`verification: search-only` and no URL has been fetched. `EU-INSPIRE`
carries `applies-in` → `DE` but not → `NL`, making it look German-specific.
The UN layer remains isolated. Ten refused links and the batch's modelling
questions are recorded in `discovery/unresolved.md`; omitted entities in
`discovery/research-queue.md`.

**Full report:** `validation/germany-second-country-report.md`.

---

# Batch 16 — Interactive Knowledge Graph and GitHub Pages (2026-08-15)

**Scope:** publish the Atlas as an interactive knowledge graph, generated
automatically from the repository and deployed to GitHub Pages. An
implementation batch — **no Atlas content was researched or added**, and no
entity file, frontmatter field or wikilink was changed.

**Added:**

- `tools/build_graph.py` — the generator. Reuses `validation/common.py` as
  its parser so the graph and the validation suite cannot disagree.
- `tools/test_build_graph.py` — 32 tests (in CI).
- `tools/test_ui.mjs` — 47 browser checks (local; needs Playwright).
- `site/` — the static application: `index.html`, `app.css`, `app.js`,
  generated `graph.json` + `details.json`, and Cytoscape.js 3.34.1 (MIT)
  vendored under `site/vendor/`.
- `.github/workflows/pages.yml` — build and deploy, `main` only.
- `docs/graph.md`, `docs/graph-architecture.md`,
  `docs/graph-development.md`, `docs/github-pages.md`.

**Modified:** `.github/workflows/validate.yml` (now also runs the generator
tests and a build check), `README.md` (Explore the Atlas + No Manual Graph
Maintenance), `CONTRIBUTING.md` (regenerate the graph after editing data).

**Graph produced:** 164 nodes, 1,307 edges — 189 typed relationships, 473
associations, 645 wikilinks. The three edge classes are kept distinct
rather than flattened; only typed relationships are drawn by default.

**Validation result:** `validation/run_all.py` 5/5 passed, 0 errors;
`tools/test_build_graph.py` 32 tests OK; `tools/test_ui.mjs` 47/47.

**Defects found by the new tests, and fixed:** two inverted edge directions
(`governed-by` on the wrong entity, `maintained-by` reversed) — neither
would have failed validation, because the graph stays connected while the
meaning reverses — and unreadable label density in the default view.

**Deployment:** verified. `pages.yml` run 31893120291 completed
successfully on 2026-08-15 — `configure-pages`, `upload-pages-artifact` and
`deploy-pages` all green — after the repository's Pages source was switched
to GitHub Actions. The first attempt failed at `configure-pages` because
that setting had not yet been made; no workflow can make it.

**Known gaps:** the graph canvas is not keyboard-traversable; the List view
is the accessible route. Large-graph performance figures come from a
synthetic 1,500-node stress test, not from real data at that size.

---

# Belgium — Third Country (2026-08-15)

**Scope:** Belgium as the third national scope. Requested directly; also the
outstanding backlog item *"a third country — Germany proved the model
reusable and revealed one real limitation; a third would test whether the
limitation is general."*

**Entities added: 14.** 164 → **178**. Relationships 189 → **218**.

- **Country anchor (1):** `BE` (`countries/be/be.md` + `index.md`).
- **Organisations (5):** `BE-BOSA`, `BE-CCB`, `BE-APD`, `BE-STATBEL`,
  `BE-KSZ`.
- **Legislation (5):** `BE-GDPR-WET`, `BE-NIS2-WET`, `BE-NIS1-WET`
  (superseded), `BE-HERGEBRUIK-WET`, `BE-KSZ-WET`.
- **Frameworks and standards (2):** `BE-BELGIF`, `BE-DCAT-AP-BE`.
- **Platforms (1):** `BE-DATA-GOV-BE`.

**Existing entities modified:** `applies-in` → `BE` added to 16 EU
instruments, and the stale "Applies in [[NL]]" prose in all of them
corrected to name all three countries — those bodies had never been updated
for Germany either.

**Validation result:** `run_all.py` 5/5, 0 errors; `test_build_graph.py`
32 tests OK; `audit.py` reports `targets: ['BE', 'DE', 'NL']`.

**Result:** the country-neutral model held for a third time, again with no
change to `metadata/schema.json`, `metadata/ontology.md`,
`metadata/taxonomy.md`, `metadata/relationship-types.md`, the folder
structure, any validation rule or the graph generator. No `BE-EU-*` entity.

**Structural gains:**

- **[[EU-GDPR]] now has three national implementing acts** and remains one
  entity.
- **[[EU-NIS2]] has three transpositions** differing in date and technique —
  Belgium 18 Oct 2024 (new act), Germany 6 Dec 2025 (amends [[DE-BSIG]]),
  Netherlands 15 Aug 2026 (new act). Belgium transposed nearly two years
  before the Netherlands.
- **The DCAT chain forks three ways** — one W3C standard, one European
  profile, three national profiles, each recorded once.
- **[[EU-EIF]] → [[BE-BELGIF]]** closes a link Germany had to refuse: the
  Atlas's first EIF → national-framework descent.

**Principal finding — the federal gap is general, and worse in Belgium.**
Germany showed no `level` term fits a Land. Belgium shows the term that
would fit is **already taken**: `regional` means supra-national here. The
cost is concrete — **OSLO**, a major Flemish semantic-interoperability
programme squarely in this Atlas's subject matter, is not modelled at all.
No sub-national level was invented.

**Known gaps:** Belgium's Open Data Directive transposition was not
identified (the 2016 act found is PSI-era and chronologically cannot be
it); three national statistical offices now sit in the Atlas and none
connects upward; only one of three national DPAs connects to the EDPB.
Sourcing position unchanged — every Belgian entity is `search-only`.

---

# France — Fourth Country (2026-08-16)

**Scope:** France as the fourth national scope, and specifically as a
**unitary** state. `progress/backlog.md` asked for this: *"a fourth country
— a unitary one. All three tests so far have been the Netherlands plus two
federal states. A second unitary country would show whether anything else
in the model is Netherlands-shaped, which the two federal cases could not
isolate."*

**Entities added: 11.** 178 → **189**. Relationships 218 → **242**.

- **Country anchor (1):** `FR`.
- **Organisations (4):** `FR-DINUM`, `FR-ETALAB`, `FR-CNIL`, `FR-ANSSI`.
- **Legislation (3):** `FR-LIL`, `FR-LRN`, `FR-NIS2-LOI`.
- **Frameworks (1):** `FR-RGI`.
- **Platforms (2):** `FR-DATA-GOUV`, `FR-FRANCECONNECT`.

**Existing entities modified:** `applies-in` → `FR` on 16 EU instruments,
with the three-country prose updated to four.

**Validation:** `run_all.py` 5/5, 0 errors; `test_build_graph.py` 32 tests
OK; `audit.py` → `targets: ['BE', 'DE', 'FR', 'NL']`.

**Principal result — a negative.** France is the **first country whose
addition raised no new ontology question at all.** Every entity fitted an
existing type, level, status and relationship type; nothing needed a caveat
about what the Atlas could not express.

That isolates the defect. With only Germany and Belgium it was unclear
whether the model was federal-lossy or simply Netherlands-shaped. A second
unitary state separates the two: **the ontology is sound for unitary states
and lossy for federal ones**, and the loss is confined to the `level`
vocabulary.

**Other findings:**

- **A third GDPR technique.** France amended the 1978 loi Informatique et
  Libertés *in place* — a deliberate, sourced choice — where the other
  three countries passed new acts. The entity implementing the GDPR in
  France is 40 years older than the regulation.
- **The amendment-lineage question, answered from the other side.**
  Germany's [[DE-NIS2UMSUCG]] → [[DE-BSIG]] needed a `supersedes`
  compromise because the amending act has its own name. France records the
  amending instruments as facts in the amended act's body and needs no
  relationship type at all. Two countries, two workarounds — the clearest
  evidence yet that the missing type is worth adding.
- **Four DPAs, one EDPB link.** [[FR-CNIL]] joins Germany and Belgium in
  having no sourced link to [[EU-EDPB]]. The Atlas now shows a Board with
  one member, which is a sourcing artefact rather than structure.
- **Four national open data portals**, and their institutional weight
  tracks the constitutional structure of the state — from a department
  inside a Prime Minister's directorate to an agreement among seventeen
  governments.

**Known gaps:** France's Open Data Directive transposition was not
identified (second country with this gap after Belgium); [[FR-NIS2-LOI]] is
`status: unknown` because sources contradict each other on whether it is in
force — the only such entity in the Atlas; no French DCAT profile was
found, so the DCAT fork stops at three countries; INSEE is not modelled.

---

# Spain — Fifth Country (2026-08-16)

**Scope:** Spain as the fifth national scope, and specifically as the first
country **outside the founding-six / Benelux-DACH group**.
`progress/backlog.md` asked for this: *"A fifth country outside the
founding-six / Benelux-DACH group. All four so far are neighbouring western
European states with similar administrative traditions. A Nordic, southern
or central European state (Ireland, Spain, Poland, Estonia) would test
whether the model is western-European-shaped rather than merely
country-neutral — a question four similar countries cannot answer."*

**Entities added: 17.** 189 → **206**. Relationships 242 → **269**.

- **Country anchor (1):** `ES`.
- **Organisations (7):** `ES-AEAD`, `ES-SGAD`, `ES-AEPD`, `ES-AESIA`,
  `ES-INCIBE`, `ES-CCN`, `ES-INE`.
- **Legislation (3):** `ES-LOPDGDD`, `ES-LEY-37-2007`, `ES-LCGC`.
- **Frameworks (2):** `ES-ENI`, `ES-ENS`.
- **Standards (1):** `ES-NTI-RISP`.
- **Platforms (2):** `ES-DATOS-GOB-ES`, `ES-CLAVE`.
- **Strategies (1):** `ES-ESPANA-DIGITAL-2026`.

**Existing entities modified:** `applies-in` → `ES` on 16 EU instruments,
with the four-country prose updated to five; the NIS2 transposition table,
the GDPR technique table and the Open Data Directive table each gained a
fifth row.

**Validation:** `run_all.py` 5/5, 0 errors, 0 warnings;
`test_build_graph.py` 32 tests OK; `test_ui.mjs` 47/47;
`audit.py` → `targets: ['BE', 'DE', 'ES', 'FR', 'NL']`.

**Principal result — the model is not western-European-shaped.** Spain is
southern European, joined the EU in a later enlargement than any of the
first four, and organises its state on a constitutional principle none of
them use. It required **no ontology, schema, taxonomy, relationship-type,
folder, validation or generator change**, and produced no `ES-EU-*` entity.
The standing objection that four neighbouring states cannot demonstrate
country-neutrality is answered.

**Second result — the federal gap has a third shape, which localises it.**
Spain is a **State of Autonomies**: seventeen Comunidades Autónomas with
devolved competences of differing scope, neither a federation nor a unitary
state. Germany's Länder, Belgium's Regions and Spain's Comunidades
Autónomas are three constitutionally distinct arrangements, and **the Atlas
fails on all three identically.** That is the strongest evidence yet that
the defect sits in the `level` vocabulary rather than in any country's
constitutional shape. Three of five countries are now affected.

The Spanish cost is measurable: seventeen regional open data portals (over
14,000 datasets by 2019), regional data protection authorities, autonomous
communities managing over 35 % of consolidated public spending, and
*cogobernanza del Estado y las Comunidades Autónomas* as **one of two
cross-cutting axes** of `ES-ESPANA-DIGITAL-2026` — of which the Atlas can
model only the state half.

**Four things Spain closed:**

- **The first national link to [[EU-AI-ACT]].** [[ES-AESIA]] is the first
  AI supervisory agency in the EU, created in 2023 **before** the
  Regulation applied, and designated under Article 70. Four countries had
  been added without any national AI body at all. Recorded as `governed-by`
  rather than `implements-requirement-from`, which is reserved for legal
  instruments.
- **The Open Data Directive transposition, on the third attempt.**
  [[ES-LEY-37-2007]] as amended by Real Decreto-ley 24/2021 — an omnibus
  instrument transposing eight directives, produced late and under threat
  of infringement proceedings. The "obvious earlier act" trap that caught
  Belgium and France (2016 in both) exists in Spain too, dated **2007**;
  three of five countries have it, so it is a research hazard rather than a
  coincidence.
- **The fourth branch of the DCAT chain.** [[ES-NTI-RISP]] is the only one
  of the four national profiles that is a **legally mandatory technical
  norm** rather than an agreed profile — recorded at `confidence: low`
  because the DCAT-AP-ES model is still in administrative processing.
- **The first edge in the statistics cluster**, after five refusals across
  four countries. [[ES-INE]] `related-to` [[EU-EUROSTAT]], deliberately at
  `source: interpretation`, `confidence: low`, because the sources describe
  a three-party structure (the European Statistical System) rather than a
  bilateral relationship. The correct fix — an `EU-ESS` entity — was **not**
  created inside a country batch.

**Also recorded:**

- **The Atlas's first organisational succession.** [[ES-AEAD]] `supersedes`
  [[ES-SGAD]], constituted 21 February 2025. `supersedes` was introduced for
  legislation and carried an organisational transformation unmodified — a
  reusability result. What it cannot express is that this was a
  *transformation* rather than an abolition and replacement.
- **Five countries, five NIS2 states.** [[ES-LCGC]] is `status: proposed`;
  [[FR-NIS2-LOI]] is `status: unknown`. *We know it has not happened* versus
  *we do not know* — both expressible, and side by side for the first time
  on instruments transposing one directive.
- **Five DPAs, still one EDPB link.** [[ES-AEPD]] joins Germany, Belgium and
  France in having none. The artefact is now more expensive to leave open
  rather than clearer.
- **A third national identity architecture.** [[ES-CLAVE]] is neither
  federation ([[FR-FRANCECONNECT]]) nor central account ([[DE-BUNDID]]) but
  a credential scheme, and it is the only one that treats identification and
  signature as separate problems. The eIDAS2 wallet deadline is now roughly
  four months away with **no country in the Atlas linked to it**.

**Known gaps:** no BOE citation for Real Decreto 729/2023, the decree
creating AESIA; the `Ley Orgánica` constitutional rank is not modelled, and
neither is partial implementation (LOPDGDD's Title X implements nothing
European); Red.es is cited but not created, so `ES-DATOS-GOB-ES` has no
`maintained-by` edge; the Centro Nacional de Ciberseguridad that
[[ES-LCGC]] would create was **not** given a node, because it does not
exist; Ley 39/2015 and 40/2015 were not modelled.

Sourcing position unchanged — every Spanish entity is `search-only`,
`last_verified: null`, no `accessed` dates. 200 of 206 entities are unread.
