---
id: NL-PETRA
type: framework
name: Provinciale Enterprise Referentie Architectuur
alternative_names:
  - PETRA
  - Provinciale Referentie Architectuur
description: >
  Reference architecture for the Dutch provinces, serving as the reference
  point for provincial architecture. The provincial member of the Dutch
  reference-architecture family alongside GEMMA (municipalities) and
  EAR/RORA (central government).

level: national
country: NL
region: null

status: active
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-IPO
related_entities:
  - NL-NORA
  - NL-GEMMA
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "NORA has daughter architectures (NORA dochters) from government domains, including EAR for central government, GEMMA for municipalities, PETRA for the provinces and WILMA for the water boards, alongside domain and chain architectures such as ROSA for education, KARWEI for work and income and SRK for the criminal justice chain (noraonline.nl/wiki/NORA_dochters; noraonline.nl/wiki/Visie_op_dochters; nl.wikipedia.org 'Nederlandse Overheid Referentie Architectuur'). NOT READ — search-only. This entity is PETRA, the provincial architecture, named in that list."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Nederlandse Overheid Referentie Architectuur"
    url: "https://nl.wikipedia.org/wiki/Nederlandse_Overheid_Referentie_Architectuur"
    publisher: "Wikipedia"
---

# PETRA (Provinciale Enterprise Referentie Architectuur)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

PETRA is the reference architecture for the Dutch provinces — the
provincial counterpart to [[NL-GEMMA]] for municipalities and
[[NL-EAR]]/[[NL-RORA]] for central government.

**This is the weakest entity in Batch 4 and should be treated with
caution.** It rests on a single sentence in one secondary source (a
Wikipedia article on NORA) which named PETRA alongside the other
architectures. No provincial or IPO source for PETRA was located, its
maintainer was not established, its relationship to [[NL-NORA]] is not
sourced, and even the expansion of the acronym is uncertain — sources gave
both "Provinciale Enterprise Referentie Architectuur" and "Provinciale
Referentie Architectuur".

It is included because Batch 4's scope names PETRA explicitly, and
recording a poorly-sourced entity with its weakness stated is more useful
than silently omitting a named scope item. The `organisations: [NL-IPO]`
association is an **Atlas assumption** from the provincial tier, not a
sourced statement of ownership.

WILMA (the water authorities' reference architecture) was named in the same
source sentence but is **not** created here: it is not named in the batch
scope and rests on the same single mention. It is queued in
`discovery/research-queue.md`. The asymmetry is deliberate and recorded.

## Relationships

`based-on` [[NL-NORA]] is **now sourced** — NORA's own wiki lists PETRA
among its *dochters*, as the architecture for the provinces, alongside EAR,
GEMMA, WILMA and [[NL-ROSA]]. That closes the more important of the two gaps
below.

`maintained-by` a provincial body is still unasserted, and the rest of this
entity's weaknesses stand. The remaining unsourced items are what could not be
sourced, and asserting them would be guessing.

## Sources

Listed in frontmatter — a single secondary source, low in the README's
preference order.
