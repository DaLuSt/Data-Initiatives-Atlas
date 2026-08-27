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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading nl.wikipedia.org's own 'Nederlandse Overheid Referentie Architectuur' article directly (2026-08-27): NORA has spawned sector-specific daughter architectures, and 'PETRA (Provinciale Referentie Architectuur) provides the foundation for the architecture of provinces' — alongside GEMMA for municipalities, WILMA for water authorities, and RORA (which the same article states has 'since 2024' replaced the earlier EAR) for central government. These stand to NORA as NORA stands to the European Interoperability Reference Architecture (EIRA) — hierarchical implementations of broader principles."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Nederlandse Overheid Referentie Architectuur"
    url: "https://nl.wikipedia.org/wiki/Nederlandse_Overheid_Referentie_Architectuur"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
---

# PETRA (Provinciale Enterprise Referentie Architectuur)

> **Verified 2026-08-27.** The single cited page was read directly this
> pass, confirming the one relationship it supports and surfacing a naming
> discrepancy. `verification` moves from `search-only` to `primary-source`
> — on the strength of reading the one source this entity has, not because
> a majority of many sources was reached; this remains, honestly, a
> thinly-sourced entity.

## Description

PETRA is the reference architecture for the Dutch provinces — the
provincial counterpart to [[NL-GEMMA]] for municipalities and
[[NL-EAR]]/[[NL-RORA]] for central government. Confirmed by reading the
Wikipedia article directly this pass: RORA has "since 2024" replaced EAR as
the central-government reference architecture — a detail newly confirmed
this pass and relevant to whichever of [[NL-EAR]]/[[NL-RORA]] is current at
any given date, though those entities belong to a different batch and are
not edited here.

**This remains the weakest entity in its research generation and should be
treated with caution**, even though its one source is now read directly
rather than merely indexed. It rests on a single sentence in one secondary
source (a Wikipedia article on NORA) which named PETRA alongside the other
architectures — reading the page directly did not surface additional
substance, only confirm what was already recorded. No provincial or IPO
source for PETRA was located this pass either, its maintainer is still not
established, and **the acronym expansion is now more clearly wrong than
uncertain**: the Wikipedia article, read directly, expands PETRA only as
"Provinciale Referentie Architectuur" — it does not use "Enterprise"
anywhere. The entity's own `id`/title uses "Provinciale Enterprise
Referentie Architectuur," which no source read (this pass or previously)
supports; this is flagged rather than silently changed, since renaming the
entity's title is outside this pass's scope and the source for "Enterprise"
might exist elsewhere and simply not have surfaced. See
`discovery/unresolved.md`.

It is included because Batch 4's scope names PETRA explicitly, and
recording a poorly-sourced entity with its weakness stated is more useful
than silently omitting a named scope item. The `organisations: [NL-IPO]`
association is an **Atlas assumption** from the provincial tier, not a
sourced statement of ownership — nothing read this pass names IPO as
PETRA's maintainer or owner.

WILMA (the water authorities' reference architecture) was named in the same
source sentence but is **not** created here: it is not named in the batch
scope and rests on the same single mention. It is queued in
`discovery/research-queue.md`. The asymmetry is deliberate and recorded.

## Relationships

`based-on` [[NL-NORA]] — confirmed by directly reading NORA's own Wikipedia
coverage, which lists PETRA among its *dochters*, as the architecture for
the provinces, alongside EAR/RORA, GEMMA and WILMA.

`maintained-by` a provincial body is still unasserted — no source read
names one — and the naming and maintainer weaknesses above stand. The
remaining unsourced items are what could not be sourced, and asserting them
would be guessing.

## Sources

Listed in frontmatter — a single source, now read directly, still low in
the README's preference order (secondary, Wikipedia).
