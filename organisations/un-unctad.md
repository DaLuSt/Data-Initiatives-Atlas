---
id: UN-UNCTAD
type: organisation
name: United Nations Trade and Development
alternative_names:
  - UNCTAD
  - UN Trade and Development
description: >
  UN body on trade and development. Within the Atlas's scope it hosts, under
  the Commission on Science and Technology for Development, a working group
  on data governance at all levels.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UN
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Both cited pages failed on every attempt this pass: unctad.org returned HTTP 403 (tried the specific working-group page, the CSTD mandate page, and unctad.org/about/history — all 403, suggesting unctad.org is broadly blocked this session, not just one page), and the unsceb.org PDF returned HTTP 404 (URL may have moved). Alternates were sought per this batch's instruction: a WebSearch specifically for the working group turned up unctad.org's own event pages by title and confirmed a genuinely new, more precise fact — the working group was established following 2024 UN General Assembly resolution A/RES/79/1, tasking the CSTD with a 'comprehensive and inclusive multi-stakeholder dialogue on data governance at all levels', with 27 state members and 27 non-state members — but this is WebSearch-snippet corroboration, not a page actually read, so it does not count toward the majority. Wikipedia's 'UN Trade and Development' article and dig.watch's UNCTAD actor page were both fetched directly; the former confirms UNCTAD generally (1964 founding, 195 member states, Geneva secretariat) but does not mention the CSTD or the data-governance working group at all, and the latter returned HTTP 403. Zero of two originally-cited sources, and zero fully on-topic alternates, were read directly this pass."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Working group on data governance at all levels"
    url: "https://unctad.org/topic/commission-on-science-and-technology-for-development/working-group-on-data-governance"
    publisher: "UN Trade and Development (UNCTAD)"
  - title: "International data governance: Pathways to progress"
    url: "https://unsceb.org/sites/default/files/2023-05/Advance%20Unedited%20-%20International%20Data%20Governance%20%E2%80%93%20Pathways%20to%20Progress_1.pdf"
    publisher: "United Nations System Chief Executives Board for Coordination"
---

# UNCTAD (UN Trade and Development)

> **Still `search-only` after a genuine attempt.** `unctad.org` appears
> broadly blocked this session — three different pages on the domain all
> returned HTTP 403, not just the one originally cited — and the UNSCEB PDF
> now 404s. Alternates were sought: WebSearch surfaced real unctad.org page
> titles and a specific, previously-unrecorded fact (2024 GA resolution
> A/RES/79/1 established the working group, 27+27 members) that is worth
> carrying forward as a research lead, but a search-result snippet is not a
> page actually read, so it does not count toward this pass's majority
> requirement. Wikipedia's UNCTAD article was read directly but does not
> mention the CSTD or the data-governance working group at all, so it
> corroborates the parent body without confirming the specific claim this
> entity exists to record. `verification` stays `search-only`.

## Description

UNCTAD is the UN body on trade and development. It enters this Atlas for one
specific reason rather than its general mandate: its **Commission on Science
and Technology for Development hosts a working group on data governance at
all levels** — one of the few explicitly international data-governance
coordination venues located in this research.

A related UN System Chief Executives Board document, *International Data
Governance: Pathways to Progress*, is cited as a second source and indicates
this work sits within a wider UN-system effort on international data
governance. Its URL now 404s and was not re-read this pass.

**A new lead, not yet confirmed by a directly-read page**: WebSearch this
pass surfaced that the working group was established following the UN
General Assembly's 2024 resolution A/RES/79/1, which tasked the CSTD with a
"comprehensive and inclusive multi-stakeholder dialogue on data governance
at all levels," and that it comprises 27 state members and 27 non-state
members. This is a genuinely more specific mandate and membership figure
than anything previously recorded here, and is worth a future pass's direct
fetch of unctad.org's own working-group page once (if) the block lifts —
recorded here as an unconfirmed lead, not adopted into the frontmatter
description or relationship evidence.

**The working group itself is not modelled as a separate entity**, nor is
the CSTD. Both are queued; the working group in particular may warrant an
`initiative` entity if its outputs turn out to be substantive.

`coverage: low`: UNCTAD's own mandate and structure were not researched, and
this entity records only its data-governance role.

Note the naming: the organisation now presents as "UN Trade and Development"
while the UNCTAD acronym remains in use. Both are recorded.

## Relationships

- Part of [[UN]].

## Sources

Listed in frontmatter — neither read directly this pass. `unctad.org`
returned HTTP 403 on every page tried (not just the one cited here) and the
UNSCEB PDF now 404s. Wikipedia's UNCTAD article and dig.watch's UNCTAD actor
page were tried as alternates; the former doesn't mention the specific
working group this entity is about, and the latter also 403'd.
