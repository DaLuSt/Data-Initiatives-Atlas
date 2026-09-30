---
id: EU-CER
type: directive
name: Critical Entities Resilience Directive
alternative_names:
  - CER Directive
  - Directive (EU) 2022/2557
description: >
  EU directive on the resilience of critical entities, approved 14 December
  2022, aimed at strengthening the preparedness of critical infrastructure
  against threats so that vital societal functions and economic activities
  are maintained. It repeals Council Directive 2008/114/EC.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-30"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CZ
  - LU
  - PT
  - IE
  - NL-WWKE
  - EU-NIS2
  - EU-CYBERSECURITY-STRATEGY
relationships:
  - type: applies-in
    target: PT
    source: fact
    evidence: "As an EU directive, Critical Entities Resilience Directive is binding on every member state as to the result to be achieved and requires national transposition, and Portugal is a member state (eur-lex.europa.eu; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: LU
    source: fact
    evidence: "As an EU directive, Critical Entities Resilience Directive is binding on every member state as to the result to be achieved and requires national transposition, and Luxembourg is a member state (eur-lex.europa.eu; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: CZ
    source: fact
    evidence: "As an EU directive, Critical Entities Resilience Directive is binding on every member state as to the result to be achieved and requires national transposition, and Czechia is a member state (eur-lex.europa.eu; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: IE
    source: fact
    evidence: "As an EU directive, Critical Entities Resilience Directive is binding on every member state as to the result to be achieved and requires national transposition, and Ireland is a member state (eur-lex.europa.eu; digital-strategy.ec.europa.eu). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "As an EU directive it requires transposition by member states; the Netherlands transposed via the Wet weerbaarheid kritieke entiteiten, passed alongside the Cyberbeveiligingswet (EUR-Lex ELI dir/2022/2557; rijksoverheid.nl, April 2026). **Closed 2026-09-30**: that transposing instrument is now [[NL-WWKE]] (created 2026-09-05), whose own file confirms directly, via nctv.nl read directly, that it implements 'de Critical Entities Resilience Directive (CER-richtlijn)' — the `implements-requirement-from` edge is recorded there rather than duplicated here, per the convention used for EU-NIS2's own national transpositions."
    confidence: high
    valid_from: 2026-08-15
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Germany included (EUR-Lex ELI dir/2022/2557). NOT READ — search-only. Unlike the Netherlands entry above, NO German transposing instrument has been identified: none was returned by search, and none is recorded in this Atlas. The relationship rests solely on the directive binding every member state."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Belgium included (EUR-Lex ELI dir/2022/2557). NOT READ — search-only. As with Germany above, NO Belgian transposing instrument has been identified; the relationship rests solely on the directive binding every member state."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: FR
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, France included (EUR-Lex ELI dir/2022/2557). NOT READ — search-only. France's 'loi Resilience' is sourced as transposing REC, NIS2 and DORA together, but that instrument's status is contested and no relationship to it is asserted from this entity; see FR-NIS2-LOI."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: ES
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Spain included (EUR-Lex ELI dir/2022/2557). NOT READ - search-only. No Spanish transposing instrument was identified in this batch and none is asserted."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: PL
    source: fact
    evidence: "As an EU directive it requires transposition by all member states, Poland included (EUR-Lex ELI dir/2022/2557). NOT READ - search-only. No Polish transposing instrument was identified in this batch and none is asserted."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Directive (EU) 2022/2557 (CER) — Official Journal"
    url: "https://eur-lex.europa.eu/eli/dir/2022/2557/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "Directive (EU) 2022/2557 — PDF text"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022L2557"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# Critical Entities Resilience Directive (Directive (EU) 2022/2557)

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Closed 2026-09-30**: this file's own "Dutch counterpart, not yet an
> entity" section had gone stale — [[NL-WWKE]] was created 2026-09-05,
> over three weeks before this fix, and now carries the
> `implements-requirement-from` edge back to this directive. Fixed below,
> along with a separate stale "Relationships" listing that still named
> only six of the ten countries this entity's own `applies-in` edges
> cover.

## Description

The CER Directive concerns the resilience of critical entities. It was
approved by the European Parliament on 14 December 2022 — the same day as
[[EU-NIS2]] — and aims to strengthen the preparedness of critical
infrastructure against threats so that vital societal functions and economic
activities are maintained. It repeals Council Directive 2008/114/EC, which
established a procedure for identifying and protecting critical European
entities in the energy and transport sectors. That older directive is not
modelled.

## Completing the December 2020 package

[[EU-CYBERSECURITY-STRATEGY]] was presented as one of three documents in a
single package: the strategy itself, the NIS2 proposal, and the proposal for
this directive. With CER now an entity, all three elements of that package
are represented, and the strategy's `influences` relationships can span the
full package rather than just its cybersecurity half.

## Dutch counterpart, now an entity — closed 2026-09-30

The Netherlands passed the **Wet weerbaarheid kritieke entiteiten**
alongside the Cyberbeveiligingswet — the Tweede Kamer approved both on 15
April 2026, per the source already cited on [[NL-CBW]]. That Dutch act,
queued since Batch 3, was created 2026-09-05 as [[NL-WWKE]] — closing the
gap this section used to flag. It carries an `implements-requirement-from`
edge to this directive, confirmed by reading nctv.nl's own page directly,
mirroring [[NL-CBW]] → [[EU-NIS2]]. This entity's own stale reference to
the gap (still present as of this file's 2026-08-21 verification, nearly
a month after NL-WWKE's creation) is fixed here.

`coverage: low`: the directive's substantive obligations were not
researched.

## Relationships

- Applies in [[PT]], [[LU]], [[CZ]], [[IE]], [[NL]], [[DE]], [[BE]], [[FR]],
  [[ES]] and [[PL]] — one entity, ten countries so far (this section was
  stale, still naming only six). Every other member state belongs here
  too; the `applies-in` relationships are added as countries join the
  Atlas.
- Implemented by [[NL-WWKE]] in the Netherlands (see above).
- Companion to [[EU-NIS2]]; both stem from [[EU-CYBERSECURITY-STRATEGY]].

## Sources

Listed in frontmatter.
