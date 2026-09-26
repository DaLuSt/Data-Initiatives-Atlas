---
id: BE-IIS
type: organisation
name: Institut interfédéral de Statistique
alternative_names:
  - IIS
  - Interfederaal Instituut voor de Statistiek
description: >
  Belgian coordinating body for the country's federal and regional
  statistical authorities. Its own site states it celebrated its tenth
  anniversary on 19 March 2026, consistent with the body becoming
  operational around 2016. Reported elsewhere (search-indexed content
  this pass could not independently confirm by reading a source
  directly — see evidence below) to bring together Statbel, IWEPS, IBSA
  and VSA alongside the Federal Planning Bureau, the National Bank of
  Belgium and the SPF Economy, under a cooperation agreement following
  Belgium's sixth state reform.

level: national
country: BE
region: EU

status: active
confidence: low
coverage: low
verification: primary-source
organisation_role: consultative

start_date: null
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-INDICATEURS-DEVELOPPEMENT-DURABLE
relationships:
  - type: part-of
    target: BE
    source: fact
    evidence: "Closes a gap BE-INDICATEURS-DEVELOPPEMENT-DURABLE's own file had flagged ('the Institut interfederal de la Statistique ... is not independently researched or modelled here'). belgium.be-family domains (statbel.fgov.be, news.belgium.be) returned CAPTCHA/403 on every attempt, matching the block already documented in discovery/unresolved.md's known-blocks table; a PDF activity report on the IIS's own separate domain (iis-statistics.be) could not be extracted as text in this environment (no PDF-rendering tool available). What was actually read directly: iis-statistics.be's own French homepage (2026-09-26), which states the Institute celebrated its 10th anniversary on 19 March 2026 -- the only fact this entity treats as confirmed. A web search of the same domain's other pages surfaced further detail (a 15 July 2014 cooperation agreement, a six-member Board of Administration, four statutory missions) that this pass could NOT verify by reading a source directly -- per the Atlas's own discipline that a search-engine summary is a lead, not evidence, none of that additional detail is asserted here. `confidence: low` reflects this: only the entity's existence, its coordinating role, and the ~2016 operational timing (implied by the anniversary date) are treated as sourced. Anchor edge under metadata/relationship-types.md §2.3, asserting Belgian federal scope via `level: national`."
    confidence: low
    valid_from: null
    valid_until: null
  - type: related-to
    target: BE-INDICATEURS-DEVELOPPEMENT-DURABLE
    source: fact
    evidence: "Confirmed on BE-INDICATEURS-DEVELOPPEMENT-DURABLE's own already-cited source, which states its 84 SDG indicators 'were selected by the Institut interfederal de la Statistique.'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Institut interfédéral de Statistique — Accueil"
    url: "https://www.iis-statistics.be/index_fr.html"
    publisher: "Institut interfédéral de Statistique"
    accessed: "2026-09-26"
---

# Institut interfédéral de Statistique (IIS)

> **Created 2026-09-26**, closing a gap [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]]'s
> own file had flagged (graph completion, not a numbered
> `discovery/unresolved.md` row). `belgium.be`-family domains
> (`statbel.fgov.be`, `news.belgium.be`) returned CAPTCHA/403 on every
> attempt, matching the block already documented in
> `discovery/unresolved.md`'s known-blocks table; a PDF activity report
> on the IIS's own separate domain could not be extracted as text in
> this environment. Only one source was actually read directly this
> pass — see below — so this entity is deliberately thin,
> `confidence: low`, rather than repeating richer detail this pass could
> not verify.

## Description

The IIS is Belgium's coordinating body for federal and regional
statistics. Its own homepage, read directly (2026-09-26), states the
Institute celebrated its **10th anniversary on 19 March 2026** —
consistent with an operational start around **2016**, though no source
read directly gives an exact founding date.

**Reported but not independently confirmed this pass**: search-indexed
content referencing the IIS's own activity reports and belgium.be
(itself blocked) describes it as bringing together Statbel, IWEPS, IBSA
and VSA alongside the Federal Planning Bureau, the National Bank of
Belgium and the SPF Economy, under a cooperation agreement signed 15
July 2014 following Belgium's sixth state reform. Per the Atlas's own
discipline that a search-engine summary is a lead, not evidence, none of
this is asserted as fact here — it is recorded only as a lead for a
future pass with a working PDF-rendering path or unblocked `belgium.be`
access.

## The body behind Belgium's SDG indicator selection

[[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]]'s own file names the IIS as the
body that selected its 84 SDG indicators — the gap this entity closes,
at least to the extent of giving the IIS an entity to point at.

## Not modelled

- Its member institutions, cooperation-agreement date, statutory
  missions and Board of Administration — reported in search-indexed
  content but not confirmed by a source read directly this pass (see
  above).

## Relationships

- `part-of` [[BE]] (anchor edge, `level: national`).
- `related-to` [[BE-INDICATEURS-DEVELOPPEMENT-DURABLE]] —
  `confidence: medium`.

## Sources

Listed in frontmatter — one source, read directly. `belgium.be`-family
pages and a PDF activity report were found but could not be read this
pass (CAPTCHA/403 and no PDF-rendering tool respectively); worth
retrying in a future session.
