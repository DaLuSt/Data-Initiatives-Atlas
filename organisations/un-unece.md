---
id: UN-UNECE
type: organisation
name: United Nations Economic Commission for Europe
alternative_names:
  - UNECE
  - UN/ECE
  - ECE
description: >
  One of the five regional commissions of the United Nations, set up in 1947
  by the Economic and Social Council through resolution 36 (IV) of 28 March
  1947. Its overarching mandate is to facilitate greater economic
  integration and cooperation among its fifty-six member States and to
  promote sustainable development and economic prosperity, with pan-European
  economic integration as its major aim. It provides a platform for policy
  dialogue and the elaboration of normative outputs across transport, trade,
  environment, statistics, energy, forestry, housing, innovation,
  public-private partnerships and population. Its membership spans Europe,
  North America and Asia, and all interested United Nations member States
  may participate in its work.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 1947-03-28
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - UN
  - UN-CES
  - UN-CEFACT
  - UN-AARHUS
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Two of the four originally-cited pages (unece.org/mission, unece.org/history-1) returned HTTP 403 this pass — `unece.org` is blocked domain-wide this session, confirmed by testing the bare root domain, which also 403s. The other two were read directly: ungeneva.org's UNECE profile confirms 'set up in 1947 by ECOSOC' and 'one of five regional commissions of the United Nations'; sdgs.un.org's UN DESA entry confirms UNECE's pan-European mandate and 2030-Agenda-implementation role but does not restate the founding date. Wikipedia's UNECE article was fetched directly as a substitute for the two blocked pages and independently confirms the precise date and resolution number: 'established on 28 March 1947 by the Economic and Social Council through Resolution 36(IV)', 56 member states, and — a bonus detail — explicitly names the Conference of European Statisticians and UN/CEFACT as related bodies within UNECE's structure."
    confidence: high
    valid_from: 1947-03-28
    valid_until: null

sources:
  - title: "Mission — UNECE"
    url: "https://unece.org/mission"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "History — UNECE"
    url: "https://unece.org/history-1"
    publisher: "United Nations Economic Commission for Europe (UNECE)"
  - title: "UNECE — The United Nations Office at Geneva"
    url: "https://www.ungeneva.org/en/about/organizations/unece"
    publisher: "United Nations Office at Geneva"
    accessed: "2026-08-28"
  - title: "United Nations Economic Commission for Europe (UNECE) — UN DESA"
    url: "https://sdgs.un.org/un-system-sdg-implementation/united-nations-economic-commission-europe-unece-49127"
    publisher: "United Nations Department of Economic and Social Affairs"
    accessed: "2026-08-28"
  - title: "United Nations Economic Commission for Europe"
    url: "https://en.wikipedia.org/wiki/United_Nations_Economic_Commission_for_Europe"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
---

# UNECE — United Nations Economic Commission for Europe

> **Verified 2026-08-28, via partial source substitution.** `unece.org` is
> blocked domain-wide this session (confirmed by testing the bare root
> domain). Two of the four originally-cited pages sit on that domain and
> were unreadable; the other two (ungeneva.org, sdgs.un.org) were read
> directly, and Wikipedia's UNECE article was added as a substitute,
> independently confirming the exact founding date and resolution number.
> Three of five sources in the resulting list are now genuinely read.

## Description

UNECE is one of the **five regional commissions of the United Nations**, set
up in **1947 by ECOSOC resolution 36 (IV)** of 28 March 1947.

Its mandate is to facilitate economic integration and cooperation among its
**fifty-six member States** and to promote sustainable development, with
pan-European economic integration as its major aim. It works across
transport, trade, environment, **statistics**, energy, forestry, housing,
innovation, public-private partnerships and population.

## Why this entity closes the Atlas's largest gap

`validation/reports.md` (Batch 15) recorded the defect that survived five
country batches:

> **The UN layer is an island** — zero relationships connect its entities to
> any EU or national entity. `UN → anything` is **0**.

`discovery/candidates.md` argued that the gap was less a research problem
than a **missing intermediate entity** problem. UNECE is that entity, and it
is why three separate clusters could not previously attach:

| Cluster | What was refused | What it needed |
|---|---|---|
| Statistics | [[UN-UNSD]] → [[EU-EUROSTAT]], three times | [[UN-CES]], organised by UNECE, where Eurostat sits |
| Environmental information | nothing — the chain was never seen | [[UN-AARHUS]], a UNECE convention |
| Trade / e-business standards | nothing — never modelled | [[UN-CEFACT]], a UNECE subsidiary body |

Each of those refusals was **correct on its own terms**: no source read
stated a direct edge, and none was invented. What was missing was the node
that all three actually hang from.

## It is not a European organisation, and that matters

The obvious modelling error here would be `region: EU`, or `level: regional`
to match [[EU]]. Both are wrong.

UNECE has **56 member States spanning Europe, North America and Asia**, and
any UN member State may participate in its work. It is a *UN* body with a
regional remit, not a European body. It is therefore recorded
`level: international`, `region: null`, `country: null` — the same treatment
as [[UN-UNSD]] and [[UN-ITU]].

This is the distinction the Atlas's `region` field exists to hold, and
getting it wrong would have made the graph assert that a UN commission is
part of the European layer.

## Relationships

- `part-of` [[UN]].

[[UN-CES]] and [[UN-CEFACT]] carry `part-of` edges pointing here, and
[[UN-AARHUS]] carries `maintained-by` — in each case the edge lives on the
subsidiary or the instrument, not here.

## Sources

Listed in frontmatter, three of five read directly this pass: the UN Office
at Geneva profile, the UN DESA entry, and — substituting for the two
403-blocked `unece.org` pages — Wikipedia's UNECE article.
