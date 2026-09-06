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
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-PPA
related_entities:
  - NL-NORA
  - NL-GEMMA
  - NL-PPA
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "Confirmed by reading nl.wikipedia.org's own 'Nederlandse Overheid Referentie Architectuur' article directly (2026-08-27): NORA has spawned sector-specific daughter architectures, and 'PETRA (Provinciale Referentie Architectuur) provides the foundation for the architecture of provinces' — alongside GEMMA for municipalities, WILMA for water authorities, and RORA (which the same article states has 'since 2024' replaced the earlier EAR) for central government. These stand to NORA as NORA stands to the European Interoperability Reference Architecture (EIRA) — hierarchical implementations of broader principles."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-PPA
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP. Confirmed by reading petra.wikixl.nl's own 'Over de PETRA' page directly (2026-09-06): 'Het beheer van de PETRA-wiki ligt nu in handen van vakgroep PPA (Platform Provincie Architecten)' (management of the PETRA wiki now lies with the PPA working group). This replaces the entity's prior unsourced organisations:[NL-IPO] assumption, which nothing read connects to PETRA."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Nederlandse Overheid Referentie Architectuur"
    url: "https://nl.wikipedia.org/wiki/Nederlandse_Overheid_Referentie_Architectuur"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "PETRA (Provinciale EnTerprise ReferentieArchitectuur)"
    url: "https://www.noraonline.nl/wiki/PETRA_(Provinciale_EnTerprise_ReferentieArchitectuur)"
    publisher: "NORA Online"
    accessed: "2026-09-06"
  - title: "Over de PETRA"
    url: "https://petra.wikixl.nl/index.php/Over_de_PETRA"
    publisher: "PETRA online / Platform provincie-architecten"
    accessed: "2026-09-06"
---

# PETRA (Provinciale Enterprise Referentie Architectuur)

> **Verified 2026-08-27, naming and maintainer questions closed
> 2026-09-06.** This entity was flagged twice as "the weakest entity in
> the Atlas": its acronym expansion looked wrong, and its maintainer was
> an unsourced Atlas assumption. Reading PETRA's own dedicated wiki
> directly resolves both — see below.

## Description

PETRA is the reference architecture for the Dutch provinces — the
provincial counterpart to [[NL-GEMMA]] for municipalities and
[[NL-EAR]]/[[NL-RORA]] for central government. Confirmed by reading the
Wikipedia article directly this pass: RORA has "since 2024" replaced EAR as
the central-government reference architecture — a detail newly confirmed
this pass and relevant to whichever of [[NL-EAR]]/[[NL-RORA]] is current at
any given date, though those entities belong to a different batch and are
not edited here.

## The acronym, resolved 2026-09-06

The Dutch Wikipedia article on NORA, this entity's only source until now,
expands PETRA as "Provinciale Referentie Architectuur" without
"Enterprise" — which previously read as evidence the entity's own
"Enterprise" title was wrong. Reading PETRA's own dedicated sources
directly resolves it the other way: NORA Online's own wiki page is titled
"PETRA (Provinciale EnTerprise ReferentieArchitectuur)," and PETRA's own
wiki, read directly, confirms the same stylised acronym — "Enterprise" was
always part of the name; the NORA Wikipedia article's mention was simply
incomplete. The entity's existing title needed no correction.

## The maintainer, resolved 2026-09-06

**Closed a previously-flagged gap.** PETRA's own wiki, read directly:
"Het beheer van de PETRA-wiki ligt nu in handen van vakgroep PPA (Platform
Provincie Architecten)" — management of the PETRA wiki now lies with the
PPA working group, now modelled as [[NL-PPA]]. This entity previously
carried `organisations: [NL-IPO]` as an explicitly-labelled Atlas
assumption; nothing read connects IPO to PETRA at all, and the assumption
is removed in favour of the sourced [[NL-PPA]] edge.

WILMA (the water authorities' reference architecture) was named in the
original source sentence but is **not** created here: it is not named in
the batch scope and rests on the same single mention. It is queued in
`discovery/research-queue.md`. The asymmetry is deliberate and recorded.

## Relationships

- `based-on` [[NL-NORA]] — confirmed by directly reading NORA's own
  Wikipedia coverage, which lists PETRA among its *dochters*, as the
  architecture for the provinces, alongside EAR/RORA, GEMMA and WILMA.
- `maintained-by` [[NL-PPA]] — confirmed this pass; see above.

## Sources

Listed in frontmatter. The original Wikipedia source remains low in the
README's preference order (secondary); NORA Online's and PETRA's own
dedicated pages, both read directly 2026-09-06, are primary and close the
naming and maintainer gaps.
