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
last_verified: "2026-08-16"
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
Created because it connects **24 entities across three layers and six
countries** — far past the two-entity threshold in
`metadata/taxonomy.md` §1, which it passed several batches ago.

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

**National (17)**

| Country | Authority | Legislation | Baseline / scheme |
|---|---|---|---|
| 🇳🇱 Netherlands | — | [[NL-WBNI]] · [[NL-CBW]] | [[NL-BIO]] |
| 🇩🇪 Germany | [[DE-BSI]] | [[DE-BSIG]] · [[DE-NIS2UMSUCG]] | [[DE-IT-GRUNDSCHUTZ]] |
| 🇧🇪 Belgium | [[BE-CCB]] | [[BE-NIS1-WET]] · [[BE-NIS2-WET]] | — |
| 🇫🇷 France | [[FR-ANSSI]] | [[FR-NIS2-LOI]] | — |
| 🇪🇸 Spain | [[ES-CCN]] · [[ES-INCIBE]] | [[ES-LCGC]] | [[ES-ENS]] |
| 🇵🇱 Poland | — | [[PL-KSC]] | — |

## What the domain view makes visible

A domain is a cross-cutting axis: it lets you ask *"what connects to
cybersecurity?"* regardless of type, level or country. Three things become
legible that were not, and none of them is visible from any single entity.

### 1. One directive, six different national states

Every country in the Atlas has a NIS2 position, and no two are alike:

| Country | Instrument | State |
|---|---|---|
| Belgium | [[BE-NIS2-WET]] | in force **18 Oct 2024** |
| Germany | [[DE-NIS2UMSUCG]] | in force 6 Dec 2025 — **amends** [[DE-BSIG]] |
| Netherlands | [[NL-CBW]] | in force 15 Aug 2026 |
| France | [[FR-NIS2-LOI]] | **`status: unknown`** — sources contradict each other |
| Spain | [[ES-LCGC]] | **`status: proposed`** — still a draft |
| Poland | [[PL-KSC]] | in force **3 Apr 2026** — and Poland is **before the CJEU** for the delay |

Two of the six are neither "done" nor "not started", and they are unclear
in *different ways*: `unknown` means the Atlas does not know, `proposed`
means it knows the thing has not happened. Poland adds a third kind that is
**not on that axis at all** — in force, *and* the member state is in
infringement proceedings over the delay that preceded it. Spain and Poland
are at different stages of the same process (reasoned opinion, referral) and
the Atlas records neither.

### 2. The national authority is not one institution

Every country has a cyber authority, and the shape differs:

- **Germany, Belgium, France** — one named national body
  ([[DE-BSI]], [[BE-CCB]], [[FR-ANSSI]]).
- **Spain** — **two**, split by audience: [[ES-CCN]] for the public sector
  under the intelligence centre, [[ES-INCIBE]] for citizens and business —
  with [[ES-LCGC]] proposing a third body on top and redistributing
  competences between them.
- **The Netherlands and Poland** — **none in the Atlas at all.** The Dutch
  NCSC is not modelled, and Poland's CSIRT NASK, CSIRT GOV and CSIRT MON
  were not researched. **Four of six countries have an authority; two do
  not**, including the founding country.

That last row is the kind of gap a domain view is good at surfacing: it is
invisible while looking at one country's entities at a time, and obvious the
moment the domain is assembled. The Poland batch added the second instance
of it.

### 3. A three-layer chain that is nearly complete

```
   INTL-ISO-IEC-27001 / 27002        ← international management standards
              │  (referenced by national baselines)
              ▼
   NL-BIO · DE-IT-GRUNDSCHUTZ · ES-ENS   ← national public-sector baselines
```

and, separately:

```
   EU-NIS  →  EU-NIS2                ← European obligations
              │  implements-requirement-from
              ▼
   NL-CBW · DE-NIS2UMSUCG · BE-NIS2-WET · FR-NIS2-LOI · ES-LCGC
```

**The two chains do not meet.** Nothing in the Atlas connects the
ISO/EU standards layer to the baseline layer for Germany, Belgium or France,
and no source read joins the NIS2 obligations to the national baselines that
would carry them in practice. Recorded here as an observation, not closed
with an invented edge.

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
- **The Dutch NCSC** and **Poland's CSIRT NASK / CSIRT GOV / CSIRT MON** —
  not Atlas entities. Together the largest hole in this domain: two of six
  countries have no cyber authority modelled.
- **The Centro Nacional de Ciberseguridad** that [[ES-LCGC]] would create —
  deliberately not modelled, because it does not exist yet.
- **CERT functions** — CCN-CERT, INCIBE-CERT and their equivalents are named
  in several entity bodies and none is modelled.
- **[[EU-ETSI]]** — a European standards body active in cybersecurity, with
  **no ETSI standard modelled**, so nothing to tag.

## Relationships

None. Domains are referenced *by* other entities through their `domains:`
field, which is how all 23 connections above are recorded — the same pattern
as [[DOMAIN-GOVERNMENT]] and [[DOMAIN-GEOSPATIAL]].
