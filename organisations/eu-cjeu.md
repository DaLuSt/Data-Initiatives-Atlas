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
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU
  - EU-OPEN-DATA-DIRECTIVE
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

This creates the **missing node** [[EU-OPEN-DATA-DIRECTIVE]]'s own file
named — the graph can now show the Court of Justice as an entity. It does
**not** close the deeper gap that file also named: there is still no
entity type for an individual infringement procedure and no relationship
type for "was referred to the Court over [instrument]." A country's
specific referral (e.g. Belgium, Bulgaria, Latvia and the Netherlands
over the Open Data Directive, February 2023) is not itself modelled here
— only the institution that hears such cases. That narrower gap remains
open, matching the discipline the INSPIRE↔UN-GGIM edge established: a
missing node and a missing edge are not the same refusal, and creating
one does not create the other.

## Relationships

- `part-of` [[EU]] — anchor edge; an EU institution.

## Sources

Listed in frontmatter, read directly this pass.
