---
id: NO-DIGDIR
type: organisation
name: Digitaliseringsdirektoratet
alternative_names:
  - Digdir
  - Norwegian Digitalisation Agency
description: >
  Norway's digitalisation agency, subordinate to the Ministry of
  Digitalisation and Public Governance. It is the government's principal
  instrument for faster and more coordinated digitalisation of the public
  sector, and is responsible for the operation, development and management
  of the national common solutions including ID-porten, Altinn, the contact
  and reservation register, the digital mailbox, eSignering, ELMA, eInnsyn
  and eFormidling.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NO-ID-PORTEN
  - NO-ALTINN
relationships:
  - type: maintained-by
    target: NO-ID-PORTEN
    source: interpretation
    evidence: "Digitaliseringsdirektoratet has responsibility for the operation, development and management of ID-porten, the contact and reservation register, the digital mailbox, eSignering, ELMA, eInnsyn and eFormidling, and modernises society-critical common solutions such as ID-porten and Altinn (digdir.no 'Kva er Digitaliseringsdirektoratet?'; digdir.no 'Kraftig vekst i bruk av digitale fellesløsningar'). NOT READ — search-only. Recorded as `interpretation` because `maintained-by` in this repository means the target maintains the subject, and the sources describe operational responsibility rather than using a maintenance term."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Kva er Digitaliseringsdirektoratet?"
    url: "https://www.digdir.no/digdir/kva-er-digitaliseringsdirektoratet/703"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
  - title: "Digitaliseringsdirektoratets strategi"
    url: "https://www.digdir.no/digdir/digitaliseringsdirektoratets-strategi/2497"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
  - title: "Kraftig vekst i bruk av digitale fellesløsningar"
    url: "https://www.digdir.no/digdir/kraftig-vekst-i-bruk-av-felleslosninger/1206"
    publisher: "Digitaliseringsdirektoratet (Digdir)"
---

# Digitaliseringsdirektoratet (Digdir)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Digdir is Norway's digitalisation agency, subordinate to the **Ministry of
Digitalisation and Public Governance**, and the government's principal
instrument for coordinated digitalisation of the public sector.

Its remit is unusually concrete for a body of this kind: it does not only
set direction, it **runs the national common solutions** —
[[NO-ID-PORTEN]], [[NO-ALTINN]], the contact and reservation register, the
digital mailbox, eSignering, ELMA, eInnsyn and eFormidling.

## The pattern it belongs to

Every country in the Atlas has a body in roughly this position, and they
divide into two kinds:

| Sets direction **and** runs platforms | Sets direction, others run platforms |
|---|---|
| Digdir, [[GB-GDS]], [[FR-DINUM]] | [[NL-LOGIUS]] is the operator, not the strategist |

Digdir belongs with GDS and DINUM. The [[GB-GDS]] entity records the same
combination — "the digital centre of government; sets direction **and** runs
the platforms" — and it is the reason both entities carry `maintained-by`
edges to identity platforms.

## The relationship type, and why it is `interpretation`

`maintained-by` in this repository means **the target maintains the
subject**, a direction the repository has got wrong before and now checks
for. The edge here reads "[[NO-ID-PORTEN]] is maintained by Digdir", which
is the intended claim.

It carries `source: interpretation` rather than `fact` because the sources
say Digdir has *responsibility for operation, development and management* —
plainly the same thing, but the Atlas records the gap between the words used
and the word asserted rather than closing it silently.

## Not modelled

- The **Ministry of Digitalisation and Public Governance** (Digitaliserings-
  og forvaltningsdepartementet), Digdir's parent. No Norwegian ministry is
  an Atlas entity, so Digdir carries no `part-of` edge — the same coverage
  limit recorded on [[FR-DGSI]] and [[NL-MIVD]].
- **KS**, the Norwegian association of local and regional authorities, which
  the sources say shares responsibility with Digdir for the *Én digital
  offentlig sektor* strategy's action plan. It is a local-government body,
  and the Atlas has no `level: local`.
- The **Én digital offentlig sektor** strategy itself (June 2019).
- **eInnsyn, eFormidling, ELMA, eSignering** and the digital mailbox —
  named by the sources as Digdir's responsibilities and not researched.

## Relationships

- `maintained-by` [[NO-ID-PORTEN]] — i.e. ID-porten is maintained by Digdir.

## Sources

Listed in frontmatter.
