---
id: EU-CJEU
type: organisation
name: Court of Justice of the European Union
alternative_names:
  - CJEU
  - Court of Justice
description: >
  Judicial institution of the European Union, ensuring EU law is applied
  uniformly across all member states. Comprises two courts — the Court of
  Justice (27 judges, one per member state, and 11 Advocates General) and
  the General Court. Rules on actions for member states' failure to
  fulfil obligations (infringement proceedings brought by the European
  Commission under TFEU Articles 258/260), though these represent less
  than 5% of its caseload, which is dominated by preliminary rulings
  referred by national courts.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-20"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU
  - EU-OPEN-DATA-DIRECTIVE
  - EU-NIS2
  - BE-HERGEBRUIK-WET-2023
  - NL-WHO
  - IE-NCS-BILL
  - ES-LCGC
  - FR-NIS2-LOI
  - NL-CBW
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Anchor edge (metadata/relationship-types.md §2.3): the CJEU is an EU institution. Confirmed by reading curia.europa.eu's own page directly (2026-09-05): 'The Court of Justice is the highest Court of the European Union. Its mission is to ensure that EU law is followed and applied in the same way across the EU.' The page describes the CJEU's composition (Court of Justice: 27 judges plus 11 Advocates General; General Court) and its infringement-proceedings role under TFEU Articles 258/260, distinct from its dominant caseload of preliminary rulings."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "The Court of Justice of the European Union"
    url: "https://curia.europa.eu/jcms/jcms/Jo2_7024/en/"
    publisher: "Court of Justice of the European Union"
    accessed: "2026-09-05"
---

# Court of Justice of the European Union (CJEU)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` §6 (Ontology gaps) had flagged "no way to
> model enforcement against a member state," naming the missing CJEU
> entity as one of three components of that gap (alongside an
> infringement-procedure entity type and a relationship type for "was
> referred to the Court over"). [[EU-OPEN-DATA-DIRECTIVE]]'s own file
> carries the same flag, for the concrete case of four member states'
> February 2023 referral over that directive.
>
> **Closed 2026-09-20** (`discovery/unresolved.md` row #44): the second
> of the three components, the relationship type, now exists —
> `referred-to-court-over`. Six national instruments carry it. The
> infringement-procedure entity type remains unaddressed. See "What this
> closes, and what it does not" below.

## Description

Reading `curia.europa.eu`'s own page directly: the CJEU comprises two
courts — the **Court of Justice** (27 judges, one per member state, and
11 Advocates General), "the highest Court of the European Union," whose
mission is "to ensure that EU law is followed and applied in the same way
across the EU"; and the **General Court**, handling certain direct
actions and specialised appeals.

## Infringement proceedings

The Court addresses member-state breaches of EU law through **actions
for failure to fulfil obligations** (TFEU Articles 258/260), in three
stages: the Commission identifies non-compliance and warns the member
state; the state gets an opportunity to correct it; if unresolved, the
Commission brings the case to Court. Remedies include a declaration of
breach, fixed penalties plus periodic fines for continued non-compliance,
and immediate fines for unimplemented directives. Confirmed directly:
**these cases are under 5% of the Court's caseload**, which is dominated
by preliminary rulings referred by national courts.

## What this closes, and what it does not

This created the **missing node** [[EU-OPEN-DATA-DIRECTIVE]]'s own file
named — the graph can show the Court of Justice as an entity.

**Closed 2026-09-20**: the missing relationship type is filled too. A new
`referred-to-court-over` type (metadata/relationship-types.md §2.1) lets a
national transposing instrument carry a typed edge to the EU directive it
was referred over. Six instruments now carry it: [[BE-HERGEBRUIK-WET-2023]]
and [[NL-WHO]] (Open Data Directive, 15 February 2023) and
[[IE-NCS-BILL]], [[ES-LCGC]], [[FR-NIS2-LOI]] and [[NL-CBW]] (NIS2, 8 July
2026). The edge is recorded on the national instrument, per the type's own
"referred to the Court over [instrument]" phrasing, rather than as an edge
into this entity — this entity remains the institution, reachable from
each referral's own file rather than holding the referrals itself.

**What still does not exist**: an entity type for an individual
infringement procedure as a first-class object — its own stages (formal
notice, reasoned opinion, referral, judgment) tracked as one thing with a
timeline, rather than as prose and a single referral edge. Bulgaria's and
Latvia's Open Data Directive referrals also remain unlinked, for a
different reason: neither has a national transposing instrument modelled
as an Atlas entity to carry the edge. That is now the state of the gap:
narrower than when this entity was created, and honestly described as
partial rather than closed.

## Relationships

- `part-of` [[EU]] — anchor edge; an EU institution.

## Sources

Listed in frontmatter, read directly this pass.
