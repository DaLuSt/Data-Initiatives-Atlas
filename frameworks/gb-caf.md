---
id: GB-CAF
type: framework
name: Cyber Assessment Framework
alternative_names:
  - CAF
  - NCSC CAF
description: >
  Outcome-based cyber security assessment framework published by the UK
  National Cyber Security Centre, built on four high-level objectives —
  managing security risk, protecting against cyber attack, detecting cyber
  security events, and minimising the impact of incidents — comprising
  fourteen principles. It is used to assess whether the security outcomes of
  essential functions are actually met, rather than to certify a management
  system. The Cyber Security and Resilience Bill would place it on a firmer
  statutory footing as the baseline standard for organisations in scope.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - GB-NCSC
related_entities:
  - INTL-ISO-IEC-27001
  - GB-NIS-REGULATIONS
  - GB-CSRB
  - NL-BIO
  - DE-IT-GRUNDSCHUTZ
  - ES-ENS
relationships:
  - type: aligned-with
    target: INTL-ISO-IEC-27001
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's 'Cyber Assessment Framework' article (2026-08-22): 'the framework is incredibly similar to the categories of controls, created by ISO 27001, [though] they aren't exactly identical as categories of control focuses on the different types of controls, while the CAF is an assessment focused on improving cybersecurity measures.' CAVEAT: the sources describe an alignment and third-party mappings, not an NCSC-published normative mapping."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: GB
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's 'Cyber Assessment Framework' article (2026-08-22): the CAF was 'developed by the United Kingdom's National Cyber Security Centre (NCSC) in 2018 for overlooking the security of operations, to meet the Security of Network & Information Systems Regulations (NIS Regulations) by supporting Critical National Infrastructure (CNI) requirements.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Cyber Assessment Framework"
    url: "https://en.wikipedia.org/wiki/Cyber_Assessment_Framework"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "NCSC CAF to ISO 27001 Mappings"
    url: "https://explore.ontolocy.com/controls-and-frameworks/caf-iso-27001-mappings/"
    publisher: "Ontolocy"
    accessed: "2026-08-22"
  - title: "NCSC Cyber Assessment Framework: Structure and Scope"
    url: "https://cyberfortgroup.com/glossary/ncsc-caf/"
    publisher: "Cyberfort Group"
    accessed: "2026-08-22"
---

# Cyber Assessment Framework

> **Verified 2026-08-22.** en.wikipedia.org's "Cyber Assessment Framework"
> article, ontolocy.com's and cyberfortgroup.com's mapping pages were read
> directly and confirmed the claims below, including the framework's
> founding year (2018) — not previously recorded as `start_date` since only
> the year, not a full date, is established.

## Description

Confirmed directly on en.wikipedia.org (2026-08-22): "The Cyber Assessment
Framework (CAF) is a mechanism developed by the United Kingdom's National
Cyber Security Centre (NCSC) in **2018** ... The CAF has fourteen
principles, which are divided into four objectives." The CAF is [[GB-NCSC]]'s **outcome-based** assessment framework: four
objectives — managing security risk, protecting against cyber attack,
detecting cyber security events, minimising the impact of incidents — across
**fourteen principles**. [[GB-CSRB]] would put it on a statutory footing as
the baseline for organisations in scope.

## The fourth national baseline, and the one that is a different kind of thing

Three batches recorded that the UK had no counterpart to the national
security baselines other countries carry. It has one, and it does not work
the same way.

| Country | Baseline | Relationship to ISO/IEC 27001 | Kind |
|---|---|---|---|
| Netherlands | [[NL-BIO]] | `based-on` 27001 **and** 27002 | control set |
| Germany | [[DE-IT-GRUNDSCHUTZ]] | `aligned-with` 27001 | methodology + control catalogue |
| Spain | [[ES-ENS]] | — *(none modelled)* | royal decree with audit annex |
| **United Kingdom** | **this entity** | **`aligned-with` 27001** | **outcome-based assessment** |

The distinction the sources keep making is worth carrying: **ISO/IEC 27001
certifies that a management system exists; the CAF asks whether the security
outcomes were actually achieved.** They are described as complementary rather
than alternative. That is why the edge is `aligned-with` and not `based-on` —
the CAF is not built out of 27001's controls the way [[NL-BIO]] is.

⚠ The mappings cited are **third-party**, not an NCSC-published normative
correspondence. The evidence string says so, and it is the reason this is
`confidence: medium`.

## Closing a chain the cybersecurity domain said was broken

[[DOMAIN-CYBERSECURITY]] records that the Atlas holds two three-layer chains
that **do not meet**: international standards down to national baselines, and
EU obligations down to national transpositions. It named the UK as having
neither.

This entity gives the UK **both halves at once**:

```
   INTL-ISO-IEC-27001                     ← international standard
          ▲ aligned-with
        GB-CAF                            ← national baseline
          ▲ references
        GB-CSRB  → amends → GB-NIS-REGULATIONS → implements → EU-NIS
```

The UK is now the only country in the Atlas where a national baseline, a
national cyber instrument and an EU directive are connected end to end — and
it got there without being in the EU, because the NIS Regulations were made
while it still was.

## Relationships

- `aligned-with` [[INTL-ISO-IEC-27001]].
- `applies-in` [[GB]] — the same treatment [[NL-BIO]] carries for the
  Netherlands.

[[GB-NCSC]] carries the `produces` edge pointing here, and [[GB-CSRB]] the
`references` edge.

## Sources

Listed in frontmatter. The originally cited NCSC policy-statement PDF and
Commons Library briefing are gone or bot-walled — replaced with
en.wikipedia.org and the two third-party ISO-mapping pages, all read
directly.
