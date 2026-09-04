---
id: DOMAIN-CYBERSECURITY
type: domain
name: Cybersecurity
alternative_names:
  - Cyber security
  - Information security
  - Network and information security
description: >
  Subject-matter domain covering the security of network and information
  systems: the legal obligations placed on essential and important entities,
  the national and European authorities that supervise them, the baselines
  and schemes public bodies must implement, and the international management
  standards those baselines draw on.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains: []
organisations: []
related_entities: []
relationships: []

sources: []
---

# Cybersecurity

## Description

Classification node for the security of network and information systems.
Created because it connects **43 entities across three layers and fourteen
countries** — far past the two-entity threshold in `metadata/taxonomy.md`
§1, which it passed several batches ago. **Refreshed 2026-09-04**: the
country count nearly tripled since the last full pass (six → fourteen),
driven by the UK, Ireland, Portugal, Estonia, Czechia, Switzerland, Norway
and Luxembourg cluster additions, and the two gaps this page used to name —
no authority modelled for the Netherlands or Poland — are both closed.

Like [[DOMAIN-GOVERNMENT]] and [[DOMAIN-GEOSPATIAL]], this is a taxonomy
node rather than a researched entity: it carries no factual claims and
therefore no sources. Everything below is a description of what the Atlas
already holds, not a new assertion.

## What it connects

**International (2)**

[[INTL-ISO-IEC-27001]] · [[INTL-ISO-IEC-27002]]

**European (5)**

[[EU-NIS]] · [[EU-NIS2]] · [[EU-CYBERSECURITY-ACT]] · [[EU-ENISA]] ·
[[EU-CYBERSECURITY-STRATEGY]]

**National (36, across fourteen countries)**

| Country | Authority | Legislation | Baseline / scheme |
|---|---|---|---|
| 🇳🇱 Netherlands | [[NL-NCSC]] | [[NL-WBNI]] (superseded) · [[NL-CBW]] · [[NL-TWCO]] | [[NL-BIO]] |
| 🇩🇪 Germany | [[DE-BSI]] | [[DE-BSIG]] · [[DE-NIS2UMSUCG]] | [[DE-IT-GRUNDSCHUTZ]] |
| 🇧🇪 Belgium | [[BE-CCB]] | [[BE-NIS1-WET]] (superseded) · [[BE-NIS2-WET]] | — |
| 🇫🇷 France | [[FR-ANSSI]] | [[FR-NIS2-LOI]] (bill) | — |
| 🇪🇸 Spain | [[ES-CCN]] · [[ES-INCIBE]] | [[ES-LCGC]] (draft) | [[ES-ENS]] |
| 🇵🇱 Poland | [[PL-NASK]] | [[PL-KSC]] | — |
| 🇪🇪 Estonia | [[EE-CERT-EE]] | [[EE-KUBERTURVALISUSE-SEADUS]] | — |
| 🇬🇧 United Kingdom | [[GB-NCSC]] · [[GB-GCHQ]] · [[GB-OFCOM]] | [[GB-NIS-REGULATIONS]] · [[GB-CSRB]] (bill) | [[GB-CAF]] |
| 🇮🇪 Ireland | [[IE-NCSC]] | [[IE-NCS-BILL]] (bill) | — |
| 🇵🇹 Portugal | [[PT-CNCS]] | [[PT-DECRETO-LEI-125-2025]] | — |
| 🇨🇿 Czechia | [[CZ-NUKIB]] | — | — |
| 🇨🇭 Switzerland | [[CH-BACS]] | — | — |
| 🇳🇴 Norway | [[NO-NSM]] | — | — |
| 🇱🇺 Luxembourg | [[LU-CTIE]] | — | — |

[[NL-TWCO]] is a different subtopic entirely — a temporary act letting the
Dutch intelligence services investigate countries with an offensive cyber
programme, not part of the NIS2/authority/baseline framework the rest of
this table describes — included for completeness because it is tagged to
this domain.

Switzerland and Norway sit outside NIS2's scope (Switzerland is not an EU or
EEA member; Norway's EEA status has not been confirmed to extend NIS2 to it
in any source read), so their authorities have no `implements-requirement-from`
edge to [[EU-NIS2]] and none is asserted. Czechia and Luxembourg have an
authority modelled with no NIS2-transposition legislation entity yet — a
gap, not a finding that none exists.

## What the domain view makes visible

A domain is a cross-cutting axis: it lets you ask *"what connects to
cybersecurity?"* regardless of type, level or country. Three things become
legible that were not, and none of them is visible from any single entity.

### 1. One directive, ten different national states

Ten EU/EEA countries in the Atlas have a NIS2 transposition position, and no
two are alike:

| Country | Instrument | State |
|---|---|---|
| Belgium | [[BE-NIS2-WET]] | in force **18 Oct 2024** |
| Germany | [[DE-NIS2UMSUCG]] | in force **6 Dec 2025** — **amends** [[DE-BSIG]] |
| Estonia | [[EE-KUBERTURVALISUSE-SEADUS]] | in force **1 Jan 2026** — amends the existing 2018 act |
| Portugal | [[PT-DECRETO-LEI-125-2025]] | in force **3 Apr 2026** |
| Poland | [[PL-KSC]] | in force **3 Apr 2026** — after a **Commission letter of formal notice** for the delay |
| Netherlands | [[NL-CBW]] | in force **15 Aug 2026** |
| France | [[FR-NIS2-LOI]] | `status: planned` — still a bill as of August 2026 |
| Spain | [[ES-LCGC]] | `status: proposed` — still a draft, approved by Cabinet Jan 2025 |
| Ireland | [[IE-NCS-BILL]] | `status: proposed` — and Ireland (with three other member states) was **referred to the Court of Justice of the EU** in July 2026 for failing to transpose |
| United Kingdom | [[GB-CSRB]] | `status: proposed` — not bound by NIS2 post-Brexit; updates the UK's own 2018 NIS Regulations to match its reforms |

**Corrected this pass**: an earlier version of this table put Poland "before
the CJEU" for its delay. No source read supports that — [[PL-KSC]]'s own
entity found the European Commission's page names Poland among 23 states
sent a **letter of formal notice**, the infringement procedure's first
stage, not a referral. **Ireland is the member state actually referred to
the Court of Justice** in this batch, a materially different and later
stage of the same procedure. France's earlier `status: unknown` — recorded
because two sources contradicted each other — has since resolved to
`planned`, sourced to the bill's current parliamentary state.

The United Kingdom is a different case entirely: it is not an EU member and
NIS2 does not apply to it. [[GB-NIS-REGULATIONS]] (2018) already exists as
retained law from the original NIS Directive, and [[GB-CSRB]] updates that
regime on its own timetable, in step with but not because of NIS2.

### 2. The national authority is not one institution

Every one of the fourteen countries now has at least one cyber authority
modelled, and the shape still differs sharply:

- **Germany, Belgium, France, Poland, Estonia, Portugal, Czechia,
  Switzerland, Norway, Luxembourg, Ireland** — one named national body each
  ([[DE-BSI]], [[BE-CCB]], [[FR-ANSSI]], [[PL-NASK]], [[EE-CERT-EE]],
  [[PT-CNCS]], [[CZ-NUKIB]], [[CH-BACS]], [[NO-NSM]], [[LU-CTIE]],
  [[IE-NCSC]]).
- **Spain** — **two**, split by audience: [[ES-CCN]] for the public sector
  under the intelligence centre, [[ES-INCIBE]] for citizens and business —
  with [[ES-LCGC]] proposing a third body on top and redistributing
  competences between them.
- **The Netherlands** — **one**, [[NL-NCSC]], now modelled and confirmed
  (2026-08-27) as one of several sectoral CSIRTs under [[NL-CBW]], not a
  sole government-wide authority.
- **The United Kingdom** — **three**, by function rather than audience:
  [[GB-NCSC]] (operational, part of [[GB-GCHQ]]), [[GB-GCHQ]] (its
  intelligence-agency parent), and [[GB-OFCOM]] (sector regulator for
  telecoms under [[GB-NIS-REGULATIONS]]).

**The gap this page previously recorded — "the Netherlands and Poland have
no authority in the Atlas at all, including the founding country" — is
closed on both counts.** [[NL-NCSC]] and [[PL-NASK]] were added in later
passes; [[PL-NASK]] `implements` [[PL-KSC]] for CSIRT NASK specifically,
while Poland's CSIRT GOV role sits with [[PL-ABW]], which the Atlas tags to
[[DOMAIN-NATIONAL-SECURITY]] rather than this domain — the intelligence
service running a CSIRT function is itself the finding, not an omission to
fix here. **CSIRT MON remains unmodelled**, because Poland's Ministry of
National Defence is not an Atlas entity.

### 3. A three-layer chain that is nearly complete

```
   INTL-ISO-IEC-27001 / 27002        ← international management standards
              │  (referenced by national baselines)
              ▼
   NL-BIO · DE-IT-GRUNDSCHUTZ · ES-ENS · GB-CAF   ← national public-sector baselines
```

and, separately:

```
   EU-NIS  →  EU-NIS2                ← European obligations
              │  implements-requirement-from
              ▼
   NL-CBW · DE-NIS2UMSUCG · BE-NIS2-WET · FR-NIS2-LOI · ES-LCGC ·
   PL-KSC · EE-KUBERTURVALISUSE-SEADUS · PT-DECRETO-LEI-125-2025 · IE-NCS-BILL
```

**The two chains still do not meet.** Nothing in the Atlas connects the
ISO/EU standards layer to the baseline layer for any of these countries,
and no source read joins the NIS2 obligations to the national baselines
that would carry them in practice. Recorded here as an observation, not
closed with an invented edge. The new baseline in this pass, [[GB-CAF]],
adds a fourth national scheme to a chain that still has no top-to-bottom
link anywhere.

## Boundary decisions

Two calls were made about what this domain covers, and both are judgements
rather than facts:

**[[EU-CER]] is excluded.** The Critical Entities Resilience Directive is
NIS2's sibling — adopted the same day, aimed at the same operators — but it
governs **physical** resilience, not network and information security.
Tagging it here would say the Atlas thinks CER is a cybersecurity
instrument, and it is not.

The boundary is genuinely awkward, and the Atlas shows exactly where:
[[FR-NIS2-LOI]] is a **single French instrument transposing NIS2, CER and
DORA together**. It is tagged to this domain because of its NIS2 content, so
the domain boundary cuts through one national law.

**Data protection is excluded.** [[EU-GDPR]] and the national data
protection authorities are about personal data, not system security, even
though the two are routinely discussed together and several authorities have
both remits. [[FR-CNIL]]'s body records that it is described as
strengthening collaboration with [[FR-ANSSI]] — a relationship the Atlas
does not assert because it was not established well enough to model.

## Not connected here

- **[[EU-CER]]** — excluded, see above.
- **Poland's CSIRT MON** — not an Atlas entity, because Poland's Ministry of
  National Defence is not one either. CSIRT NASK ([[PL-NASK]]) and CSIRT GOV
  ([[PL-ABW]], tagged to [[DOMAIN-NATIONAL-SECURITY]] instead) are both now
  modelled.
- **The Centro Nacional de Ciberseguridad** that [[ES-LCGC]] would create —
  deliberately not modelled, because it does not exist yet.
- **CERT functions** — CCN-CERT, INCIBE-CERT and their equivalents are named
  in several entity bodies and none is modelled.
- **CSIRT-IE** — Ireland's single point of contact under the current regime,
  named in [[IE-NCS-BILL]]'s own body but not modelled as a separate entity;
  [[IE-NCSC]] carries the competent-authority role.
- **[[EU-ETSI]]** — a European standards body active in cybersecurity, with
  **no ETSI standard modelled**, so nothing to tag.
- **The Digital Trust Center**, merged into [[NL-NCSC]] on 1 January 2026 —
  described on that entity's own page, not modelled separately.

## Relationships

None. Domains are referenced *by* other entities through their `domains:`
field, which is how all 43 connections above are recorded — the same pattern
as [[DOMAIN-GOVERNMENT]] and [[DOMAIN-GEOSPATIAL]].
