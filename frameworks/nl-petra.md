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
relationships: []

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

No relationships are asserted. The obvious ones — `based-on` [[NL-NORA]],
`maintained-by` a provincial body — are precisely what could not be
sourced, and asserting them would be guessing.

## Sources

Listed in frontmatter — a single secondary source, low in the README's
preference order.
