---
id: PL
type: country
name: Poland
alternative_names:
  - Republic of Poland
  - Polska
  - Rzeczpospolita Polska
description: >
  Country anchor entity for Poland, the sixth national scope covered by the
  Data Initiatives Atlas and the first outside western Europe. Used as the
  target of `country` fields and `applies-in` relationships for
  Polish-scoped entities.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - EU
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Poland is one of the 27 member states of the European Union, having acceded on 1 May 2004; the Union's own list of EU countries records its accession date together with its Schengen and euro status (european-union.europa.eu 'EU countries'). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3: it records EU membership and asserts no more than that. Added in the European country batch so that all fifty anchors carry the same membership edge."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EU countries"
    url: "https://european-union.europa.eu/principles-countries-history/eu-countries_en"
    publisher: "European Union"
  - title: "PL — Poland (ISO 3166-1 country code)"
    url: "https://www.iso.org/obp/ui/#iso:code:3166:PL"
    publisher: "International Organization for Standardization (ISO)"
  - title: "Ministerstwo Cyfryzacji — Portal Gov.pl"
    url: "https://www.gov.pl/web/cyfryzacja"
    publisher: "Ministerstwo Cyfryzacji"
  - title: "Ustawa z dnia 11 sierpnia 2021 r. o otwartych danych i ponownym wykorzystywaniu informacji sektora publicznego"
    url: "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20210001641"
    publisher: "Internetowy System Aktów Prawnych (ISAP) — Sejm RP"
---

# Poland

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Poland (ISO 3166-1 alpha-2: `PL`) is the **sixth country** populated in the
Data Initiatives Atlas, after [[NL]], [[DE]], [[BE]], [[FR]] and [[ES]].

Polish entities live in the same flat type folders as every other country's,
tagged `country: PL`. EU instruments that apply in Poland reference it via
an `applies-in` relationship — the same single entity that already carries
`applies-in` to five other countries.

## Why Poland, specifically

`progress/backlog.md` asked for this one:

> *A sixth country outside western Europe entirely. All five are western
> European EU member states. A central or northern European state (Poland,
> Estonia) — or a non-EU one — would test the two assumptions five EU
> members cannot: that the EU layer is the right regional parent, and that
> `applies-in` is the right way to attach a country to it.*

Poland is central European, acceded to the EU in **2004** — a different
enlargement from any of the five — and has a post-1989 administrative
tradition none of them share.

**Both assumptions held.** The EU layer is the right regional parent for a
2004 accession state exactly as it is for a founding member, and
`applies-in` attached Poland with no modification. No schema, ontology,
taxonomy, relationship-type, folder, validation or generator change; no
`PL-EU-*` entity.

## What Poland changes

Unlike [[FR]], which raised no new question at all, Poland raises two — and
both are about **time**, not structure.

### A sixth NIS2 state, and a new kind

| Country | Instrument | State |
|---|---|---|
| Belgium | [[BE-NIS2-WET]] | in force 18 Oct 2024 |
| Germany | [[DE-NIS2UMSUCG]] | in force 6 Dec 2025 — amends [[DE-BSIG]] |
| Netherlands | [[NL-CBW]] | in force 15 Aug 2026 |
| France | [[FR-NIS2-LOI]] | **`unknown`** — sources contradict each other |
| Spain | [[ES-LCGC]] | **`proposed`** — still a draft |
| **Poland** | **[[PL-KSC]]** | **in force 3 Apr 2026 — and Poland is before the CJEU for having been late** |

Poland is the first country in the Atlas where an instrument is **in force
and the member state is simultaneously in infringement proceedings** over
the delay that preceded it. `status: active` is correct and says nothing
about that.

### The first sourced eIDAS2 link in the Atlas — and it is negative

[[PL-MOBYWATEL]] is reported to be **architecturally incompatible with
eIDAS 2.0**, unable to function as a European Digital Identity Wallet, with
adaptation deemed technically impossible and replacement promised by end of
2026.

Three batches have recorded that *no country in the Atlas is linked to
[[EU-EIDAS2]]* and that the deadline was approaching. Poland provides the
first sourced connection, and what it says is that the national system
**cannot meet the requirement**. See [[PL-MOBYWATEL]] for why the Atlas
struggles to express that.

## What Poland confirms

- **The 2016-act trap has a documented answer.** Belgium and France both
  have a 2016 open data act that looks like the Open Data Directive
  transposition and cannot be. Poland had the identical 2016 act — and
  [[PL-OTWARTE-DANE]] **explicitly repeals it**. Four of six countries now
  have a sourced transposition; the two gaps stay open, but the shape of
  their answer is now visible.
- **A fifth national statistical office in [[EU-ESS]].** [[PL-GUS]] joins
  on the strength of GUS's own description of the ESS. France remains the
  only modelled country with no statistical office.
- **A second pending organisational transformation.** [[PL-COI]] is subject
  to a draft law converting it into an *Agencja Informatyzacji* — the same
  shape as Spain's completed [[ES-SGAD]] → [[ES-AEAD]], caught at an
  earlier stage.

## Relationships

See `countries/pl/index.md` for the curated index of Polish entities.

## Sources

Listed in frontmatter, including the ISO Online Browsing Platform entry —
the same citation [[DE]], [[BE]], [[FR]] and [[ES]] carry.

**No `accessed` date and no `last_verified`** — nothing about this entity
has been checked against a source.
