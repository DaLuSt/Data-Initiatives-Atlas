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
verification: search-only

start_date: 1947-03-28
end_date: null
last_verified: null
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
    evidence: "UNECE was set up in 1947 by ECOSOC, which adopted resolution 36 (IV) on 28 March 1947 setting up the ECE and giving it its terms of reference; it is one of the five regional commissions of the United Nations (unece.org/mission; unece.org/history-1; ungeneva.org UNECE page). NOT READ — search-only."
    confidence: medium
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
  - title: "United Nations Economic Commission for Europe (UNECE) — UN DESA"
    url: "https://sdgs.un.org/un-system-sdg-implementation/united-nations-economic-commission-europe-unece-49127"
    publisher: "United Nations Department of Economic and Social Affairs"
---

# UNECE — United Nations Economic Commission for Europe

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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

Listed in frontmatter — UNECE's own mission and history pages, the UN Office
at Geneva profile, and the UN DESA entry.
