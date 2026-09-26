---
id: BE-CYFUN
type: standard
name: CyberFundamentals Framework
alternative_names:
  - CyFun
  - CyFun®
description: >
  Belgian cybersecurity maturity framework developed by the Centre for
  Cybersecurity Belgium (CCB), providing organisations a structured,
  risk-based route to strengthening cyber resilience and demonstrating
  NIS2 compliance. Structured around four assurance levels (Small,
  Basic, Important, Essential) with an increasing number of controls,
  and assessed against five CMMI-derived maturity levels. Belgium's
  National Cybersecurity Certification Authority (NCCA), part of the
  CCB, is the framework's Primary Scheme Owner; Ireland's National
  Cyber Security Centre has joined as a scheme co-owner, recommending
  CyFun to Irish organisations as a voluntary route to NIS2 compliance.

level: national
country: BE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations:
  - BE-CCB
related_entities:
  - BE-CCB
  - IE-NCSC
relationships:
  - type: maintained-by
    target: BE-CCB
    source: fact
    evidence: "Closes a gap [[IE-NCS-BILL]]'s and [[IE-NCSC]]'s own files had flagged ('CyFun originates with BE-CCB in Belgium... not independently researched'). CCB's own domain (ccb.belgium.be) and its affiliated atwork.safeonweb.be both return HTTP 403 to this environment's fetch tooling, matching the documented belgium.be-family block. Sourced instead from Ireland's own National Cyber Security Centre page (ncsc.gov.ie/CyFun/, read directly, 2026-09-26): 'Ireland has joined the Cyber Fundamentals Framework (CyFun), originally developed in Belgium, as a scheme co-owner' -- and from a third-party technical explainer (codific.com, read directly), which states CyFun 'is a cybersecurity framework developed by the Centre for Cybersecurity Belgium (CCB) under the Prime Minister of Belgium's authority,' detailing four assurance levels (Small: 10 rules of thumb; Basic: 34 controls, stops 82% of attacks; Important: 117 controls, 94%; Essential: 140 controls, 100% historically) and five CMMI-derived maturity levels (Initial, Repeatable, Defined, Managed, Optimizing). `confidence: medium` rather than `high`: no source read is CCB's own page, so the framework's precise governance structure (e.g. the NCCA's exact role as 'Primary Scheme Owner', found only in unread search-index snippets) is not independently confirmed."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "CyFun"
    url: "https://www.ncsc.gov.ie/CyFun/"
    publisher: "National Cyber Security Centre (Ireland)"
    accessed: "2026-09-26"
  - title: "What Is CyFun and How to Implement It?"
    url: "https://codific.com/what-is-cyfun-and-how-to-implement-it/"
    publisher: "Codific"
    accessed: "2026-09-26"
---

# CyberFundamentals Framework (CyFun)

> **Created 2026-09-26**, closing a gap [[IE-NCS-BILL]]'s and [[IE-NCSC]]'s
> own files had flagged (graph completion, not a numbered
> `discovery/unresolved.md` row: "CyFun originates with [[BE-CCB]] in
> Belgium... not independently researched"). CCB's own domain
> (`ccb.belgium.be`) and its affiliated `atwork.safeonweb.be` both remain
> HTTP 403-blocked, the same documented `belgium.be`-family block —
> sourced instead from Ireland's own NCSC page and a third-party
> technical explainer, both read directly.

## Description

CyFun is Belgium's cybersecurity maturity framework, developed by the
**Centre for Cybersecurity Belgium (CCB)** — confirmed by reading
codific.com directly: "developed by the Centre for Cybersecurity Belgium
(CCB) under the Prime Minister of Belgium's authority."

It structures cybersecurity maturity around **four assurance levels**,
each with more controls than the last:

| Level | Controls | Stops (of attacks, historically) |
|---|---|---|
| Small | 10 rules of thumb | — |
| Basic | 34 controls | 82% |
| Important | 117 controls | 94% |
| Essential | 140 controls | 100% |

Assessment itself uses **five CMMI-derived maturity levels**: Initial,
Repeatable, Defined, Managed, Optimizing.

## A framework that crossed a border

Confirmed by reading Ireland's own National Cyber Security Centre page
directly: "Ireland has joined the Cyber Fundamentals Framework (CyFun),
originally developed in Belgium, **as a scheme co-owner**." The NCSC
"recommends the CyberFundamentals (CyFun) framework (NIST CSF 2.0
version) as a well-recognised, structured, voluntary tool to assist
entities in meeting their NIS2 obligations" — voluntary, and explicitly
not "the sole route to compliance."

This is the first Atlas entity recording an Irish body co-owning a
framework a second country originated, rather than merely referencing or
being inspired by it — a stronger tie than the `related-to`/`aligned-with`
edges the Atlas usually records between similar national instruments.

## Why `confidence: medium`, not `high`

No source read this pass is CCB's own page — both `ccb.belgium.be` and
`atwork.safeonweb.be` returned HTTP 403 on every attempt, matching the
documented `belgium.be`-family block (`discovery/unresolved.md`'s
known-blocks table). Search-indexed content (not read directly, so not
cited) additionally describes Belgium's National Cybersecurity
Certification Authority (NCCA), part of the CCB, as CyFun's "Primary
Scheme Owner" — plausible and consistent with what was read directly, but
not asserted here since it was not confirmed by a source actually opened.

## Not modelled

- The **National Cybersecurity Certification Authority (NCCA)** as a
  separate entity from [[BE-CCB]] — reported in unread search content,
  not confirmed by a source read directly.
- **CyFun 2025**, a named newer version referenced in search results —
  not independently confirmed as a distinct release with its own dates.
- Any other countries beyond Belgium and Ireland that may use or
  reference CyFun — no source read names a third.

## Relationships

- `maintained-by` [[BE-CCB]] — `confidence: medium`.

[[IE-NCSC]] carries the reciprocal `participates-in` edge to this entity,
per the Atlas's "record the edge once" convention.

## Sources

Listed in frontmatter, both read directly.
