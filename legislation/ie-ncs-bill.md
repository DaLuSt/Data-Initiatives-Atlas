---
id: IE-NCS-BILL
type: law
name: National Cyber Security Bill
alternative_names: []
description: >
  Irish bill intended to transpose the NIS2 Directive into Irish law. The
  National Cyber Security Centre and CSIRT-IE are Ireland's current
  designated competent authority and single point of contact for NIS2,
  respectively. Ireland did not meet the Directive's transposition deadline
  of 17 October 2024; the Commission sent a reasoned opinion for failure to
  notify full transposition on 7 May 2025, and in July 2026 referred
  Ireland and three other member states to the Court of Justice of the EU
  over the failure, exposing Ireland to an initial penalty of €2.8 million
  plus daily fines. The Bill had not been enacted as at the date of this
  record.

level: national
country: IE
region: EU

status: proposed
confidence: low
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-05"
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
    evidence: "Confirmed by reading globalpolicywatch.com directly (2026-08-22): 'the proposed bill to transpose NIS2 in Ireland (the National Cyber Security Bill) has still not been enacted.' The European Commission's own NIS2-transposition tracker for Ireland (digital-strategy.ec.europa.eu, read directly) names 'National Cyber Security Centre' as the 'National competent authority for DSPs' and 'CSIRT-IE' as the 'National CSIRT' and 'Single point of contact.' NOT independently re-confirmed this pass: which body the Bill itself designates for these roles, since the Bill's own text was not located; the roles above are the Commission's account of Ireland's current designations, not a quotation of the Bill."
    confidence: low
    valid_from: null
    valid_until: null
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "Confirmed by reading williamfry.com directly (2026-08-22): 'the Network and Information Security Directive (EU) 2022/2555 (NIS2) took effect on 17 October 2024 across the EU,' and 'the General Scheme for the National Cybersecurity Bill is the proposed draft legislation to transpose NIS2 into Irish law.' The Commission's own tracker (digital-strategy.ec.europa.eu, read directly) confirms non-transposition: 'On 7 May 2025 the Commission sent a reasoned opinion for failure to notify full transposition.' globalpolicywatch.com, read directly, reports a further escalation not previously recorded: 'the European Commission referred Ireland and three other Member States to the CJEU for their failure to transpose NIS2' (July 2026)."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "NIS2 Directive implementation in Ireland"
    url: "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-ireland"
    publisher: "European Commission — Shaping Europe's digital future"
    accessed: "2026-08-22"
  - title: "NCSC: NIS2"
    url: "https://www.ncsc.gov.ie/nis2/"
    publisher: "National Cyber Security Centre (Ireland)"
    accessed: "2026-08-22"
  - title: "NIS2, Ireland and Draft Guidance"
    url: "https://www.williamfry.com/knowledge/nis2-ireland-and-draft-guidance/"
    publisher: "William Fry"
    accessed: "2026-08-22"
  - title: "Irish NCSC Issues Cyber Governance Guidance for Management Boards Ahead of NIS2 Implementation"
    url: "https://www.globalpolicywatch.com/2026/07/irish-ncsc-issues-cyber-governance-guidance-for-management-boards-ahead-of-nis2-implementation/"
    publisher: "Covington — Global Policy Watch"
    accessed: "2026-08-22"
  - title: "Ireland facing €2.8m penalty plus daily fines for failing to adopt EU cybersecurity rules"
    url: "https://www.irishtimes.com/business/2026/08/24/ireland-facing-28m-penalty-plus-daily-fines-for-failing-to-adopt-eu-cybersecurity-rules/"
    publisher: "The Irish Times"
    accessed: "2026-09-05"
---

# National Cyber Security Bill (Ireland)

> **Verified 2026-08-22.** globalpolicywatch.com, williamfry.com and the
> European Commission's own NIS2-transposition tracker for Ireland were
> read directly and confirmed the claims below, verbatim in places. The
> tracker page found this pass names the NCSC and CSIRT-IE as Ireland's
> *current* designated authorities under the still-unamended NIS1 regime
> — not a quotation of the Bill's own text, which was not located. The
> unattested alternative names "NCS Bill" and "Irish NIS2 transposition"
> have been removed.

## Description

Confirmed by reading globalpolicywatch.com directly (2026-08-22): "the
proposed bill to transpose NIS2 in Ireland (the National Cyber Security
Bill) has still not been enacted." The Bill intends to transpose
[[EU-NIS2]] into Irish law. [[IE-NCSC]] and CSIRT-IE are confirmed, via
the European Commission's own tracker, as Ireland's current designated
competent authority and single point of contact respectively — though
that tracker describes today's designations, not the Bill's content.

## A transposition that is overdue, not merely pending

| Date | Event |
|---|---|
| **17 October 2024** | NIS2 transposition deadline — **not met by Ireland** |
| **7 May 2025** | Commission sends a reasoned opinion for failure to notify full transposition |
| **July 2026** | Commission refers Ireland and three other member states to the CJEU over the failure |
| — | Transposition to proceed via the National Cyber Security Bill |
| Q3 2026 | Planning assumption reported for the legislation |
| Q4 2026 | End of Ireland's EU Council Presidency, before which transposition is reported to be intended |

## A new escalation found this pass

Confirmed by reading globalpolicywatch.com directly (2026-08-22): "Days
after the publication of the guidance, the European Commission referred
Ireland and three other Member States to the CJEU for their failure to
transpose NIS2." This is a harder deadline consequence than the reasoned
opinion the entity previously recorded, and it was not in the sources
originally cited.

The Atlas already holds one pending cyber instrument — [[GB-CSRB]], the UK's
Cyber Security and Resilience Bill. **These two are not the same kind of
thing**, and the distinction is worth stating because the graph will show
them identically:

- [[GB-CSRB]] is a **sovereign choice**. The UK is outside NIS2's scope and
  is legislating to address the same problem. Its entity is careful to say
  it is *not* a transposition.
- This Bill **is** a transposition, by a member state, of a Directive whose
  deadline has passed.

## Re-checked 2026-09-05: still not enacted, and a penalty figure is now known

The Irish Times, read directly (24 August 2026): the Bill "has not yet
been enacted" and remains "in legislative process, awaiting progression
through the Oireachtas." Ireland faces an **initial penalty of €2.8
million plus daily fines** for continued non-compliance, and Aon called
on the government to prioritise the Bill "when the Oireachtas returns in
September and to progress it through its remaining stages as quickly as
possible." A further WebSearch the same day found no report of enactment
since. `status: proposed` is confirmed current, not stale, as of this
re-check.

## ⚠ Why `confidence: low`

Three things are unsettled and all are load-bearing:

1. **Whether it has been enacted.** Confirmed still not enacted as of 24
   August 2026 (see re-check above), with the Oireachtas expected to
   resume work on it in September 2026. `status: proposed` remains the
   honest reading.
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

- **CSIRT-IE** as a separate entity. Whether the *Bill itself* designates
  it (as opposed to CSIRT-IE already holding that role under the current,
  NIS1-based regime) was not confirmed this pass — see the caveat above.
- Ireland's **NIS1 transposition**, the instrument the 450 operators sit
  under today.
- The **Cyber Fundamentals Framework (CyFun)**, named by the sources as the
  NCSC's preferred risk-based framework. CyFun originates with [[BE-CCB]]
  in Belgium, so an Irish adoption would be a genuine cross-border edge —
  and no source read states that the Irish NCSC has adopted it as opposed to
  referring to it.

## Sources

Listed in frontmatter, all four read directly this pass. The Commission's
own NIS2-implementation page is the strongest citation; the NCSC's own
page confirms NIS2 is not yet in force in Ireland ("the earlier version
of NIS2 (NIS1) is still operational and continues to apply") without
naming the Bill itself, and the remaining two are trade-press analyses.
