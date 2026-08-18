---
id: IE-NCS-BILL
type: law
name: National Cyber Security Bill
alternative_names:
  - NCS Bill
  - Irish NIS2 transposition
description: >
  Irish bill intended to transpose the NIS2 Directive into Irish law,
  assigning competent-authority functions to the National Cyber Security
  Centre and CSIRT-IE and establishing an enforcement and penalty framework.
  Ireland did not meet the Directive's transposition deadline of 17 October
  2024, and the Bill had not been enacted as at the date of this record.

level: national
country: IE
region: EU

status: proposed
confidence: low
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - EU-NIS2
  - IE-NCSC
relationships:
  - type: applies-to
    target: IE-NCSC
    source: fact
    evidence: "Ireland's National Cyber Security Bill assigns competent-authority functions to the NCSC Ireland and to Ireland's Computer Security Incident Response Team (CSIRT-IE) and establishes an enforcement and penalty framework; NIS2 will be transposed through the Bill, with the National Cyber Security Centre acting as the lead authority for oversight and enforcement (williamfry.com 'NIS2, Ireland and Draft Guidance'; globallawexperts.com 'NIS2 Compliance Ireland'; ncsc.gov.ie/nis2). NOT READ — search-only. The Bill was not enacted as at the date of this record, so this describes its content, not law in force."
    confidence: low
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "In Ireland NIS2 will be transposed through the National Cyber Security Bill, with the National Cyber Security Centre acting as the lead authority for oversight and enforcement; the Bill assigns competent-authority functions to the NCSC and to CSIRT-IE and establishes an enforcement and penalty framework. The transposition deadline of 17 October 2024 was not met (williamfry.com 'NIS2, Ireland and Draft Guidance'; digital-strategy.ec.europa.eu 'NIS2 Directive implementation in Ireland'; ncsc.gov.ie/nis2; globalpolicywatch.com). NOT READ — search-only."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "NIS2 Directive implementation in Ireland"
    url: "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-ireland"
    publisher: "European Commission — Shaping Europe's digital future"
  - title: "NCSC: NIS2"
    url: "https://www.ncsc.gov.ie/nis2/"
    publisher: "National Cyber Security Centre (Ireland)"
  - title: "NIS2, Ireland and Draft Guidance"
    url: "https://www.williamfry.com/knowledge/nis2-ireland-and-draft-guidance/"
    publisher: "William Fry"
  - title: "Irish NCSC Issues Cyber Governance Guidance for Management Boards Ahead of NIS2 Implementation"
    url: "https://www.globalpolicywatch.com/2026/07/irish-ncsc-issues-cyber-governance-guidance-for-management-boards-ahead-of-nis2-implementation/"
    publisher: "Covington — Global Policy Watch"
---

# National Cyber Security Bill (Ireland)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `status: proposed`, `confidence: low`.

## Description

The Bill intended to transpose [[EU-NIS2]] into Irish law, assigning
competent-authority functions to [[IE-NCSC]] and to CSIRT-IE and
establishing an enforcement and penalty framework.

## A transposition that is overdue, not merely pending

| Date | Event |
|---|---|
| **17 October 2024** | NIS2 transposition deadline — **not met by Ireland** |
| — | Transposition to proceed via the National Cyber Security Bill |
| Q3 2026 | Planning assumption reported for the legislation |
| Q4 2026 | End of Ireland's EU Council Presidency, before which transposition is reported to be intended |

The Atlas already holds one pending cyber instrument — [[GB-CSRB]], the UK's
Cyber Security and Resilience Bill. **These two are not the same kind of
thing**, and the distinction is worth stating because the graph will show
them identically:

- [[GB-CSRB]] is a **sovereign choice**. The UK is outside NIS2's scope and
  is legislating to address the same problem. Its entity is careful to say
  it is *not* a transposition.
- This Bill **is** a transposition, by a member state, of a Directive whose
  deadline has passed.

## ⚠ Why `confidence: low`

Three things are unsettled and all are load-bearing:

1. **Whether it has been enacted.** The date of this record is 18 August
   2026; the most recent source reports a Q3 2026 planning assumption and an
   intention to transpose before the end of Q4 2026. `status: proposed` is
   the honest reading as at the date recorded, and it may already be stale.
2. **Its final content.** One source states plainly that the content will be
   finalised only once NIS2 is transposed.
3. **Its title.** "National Cyber Security Bill" is what the sources call
   it; the enacted short title may differ.

An `implements-requirement-from` edge from an unenacted bill is a claim
about intent, not about law, and it is carried at `confidence: low` for that
reason.

## The scope change the sources record

Irish regulatory scope is reported to expand from around **450** operators
under NIS1 to between **4,500 and 6,000** entities under NIS2 — a tenfold
increase. Nothing comparable is recorded for any other transposition in the
Atlas, because no other entity's sources give the figures.

## Not modelled

- **CSIRT-IE**, which the Bill also designates.
- Ireland's **NIS1 transposition**, the instrument the 450 operators sit
  under today.
- The **Cyber Fundamentals Framework (CyFun)**, named by the sources as the
  NCSC's preferred risk-based framework. CyFun originates with [[BE-CCB]]
  in Belgium, so an Irish adoption would be a genuine cross-border edge —
  and no source read states that the Irish NCSC has adopted it as opposed to
  referring to it.

## Sources

Listed in frontmatter. The Commission's own NIS2-implementation page is the
strongest citation; the rest are the NCSC's page and two law-firm analyses.
