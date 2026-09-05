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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UN
  - UN-GDC
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "unctad.org, dig.watch and sdg.iisd.org remain blocked this pass (all HTTP 403), consistent with every prior attempt. But the substantive claim this entity exists to record is now confirmed by a genuinely stronger source than any of those: reading un.org's own official 'Annex I: Global Digital Compact' page directly (2026-09-05) — the UN General Assembly's own text, adopted as part of Resolution A/RES/79/1, the Pact for the Future — quotes paragraph 48 verbatim: 'we request the Commission on Science and Technology for Development to establish a dedicated working group to engage in a comprehensive and inclusive multi-stakeholder dialogue on data governance at all levels as relevant for development.' This is the primary legal instrument establishing the working group, read directly rather than corroborated by WebSearch synthesis, closing the gap the prior pass left open. UNCTAD's general 1964-founding/195-member-state/Geneva-secretariat facts were separately confirmed in the prior pass via Wikipedia, geneva.china-mission.gov.cn and inclusiveias.com."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Working group on data governance at all levels"
    url: "https://unctad.org/topic/commission-on-science-and-technology-for-development/working-group-on-data-governance"
    publisher: "UN Trade and Development (UNCTAD)"
  - title: "International data governance: Pathways to progress"
    url: "https://unsceb.org/sites/default/files/2023-05/Advance%20Unedited%20-%20International%20Data%20Governance%20%E2%80%93%20Pathways%20to%20Progress_1.pdf"
    publisher: "United Nations System Chief Executives Board for Coordination"
  - title: "UN Trade and Development"
    url: "https://en.wikipedia.org/wiki/UN_Trade_and_Development"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "United Nations Conference on Trade And Development, UNCTAD"
    url: "https://geneva.china-mission.gov.cn/eng/bjzl/zzzl/202007/t20200727_8299799.htm"
    publisher: "Permanent Mission of the People's Republic of China to the UN Office at Geneva"
    accessed: "2026-08-28"
  - title: "UN Trade and Development (UNCTAD) – Mandate, Functions, Reports"
    url: "https://inclusiveias.com/un-trade-and-development-unctad-upsc/"
    publisher: "InclusiveIAS"
    accessed: "2026-08-28"
  - title: "Annex I: Global Digital Compact"
    url: "https://www.un.org/pact-for-the-future/en/annex-i-global-digital-compact"
    publisher: "United Nations (Pact for the Future / Summit of the Future)"
    accessed: "2026-09-05"
---

# UNCTAD (UN Trade and Development)

> **Promoted to `primary-source` 2026-09-05.** `unctad.org`, `dig.watch`
> and `sdg.iisd.org` remain blocked (all HTTP 403), the same as every
> prior attempt. But the substantive claim this entity exists to record —
> that a CSTD working group on data governance was established, and why —
> is now confirmed by reading **`un.org`'s own official text directly**:
> the Global Digital Compact's Annex I page, part of UN General Assembly
> resolution A/RES/79/1 (the Pact for the Future). That is a stronger
> source than any `unctad.org` page would have been — it is the actual
> founding instrument, not a secondary description of it.

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

**Confirmed 2026-09-05, by a directly-read page.** Reading `un.org`'s own
"Annex I: Global Digital Compact" page directly — the actual text of UN
General Assembly resolution A/RES/79/1, the Pact for the Future — quotes
paragraph 48 verbatim: *"we request the Commission on Science and
Technology for Development to establish a dedicated working group to
engage in a comprehensive and inclusive multi-stakeholder dialogue on data
governance at all levels as relevant for development."* [[UN-GDC]]'s own
file is updated with the same finding and now carries an `influences` edge
here. The 27-state/27-non-state membership figure from the prior pass's
WebSearch snippet was not re-confirmed by a directly-read page this pass
and is not restated as a sourced fact.

**The working group itself is not modelled as a separate entity**, nor is
the CSTD. Both are queued; the working group in particular may warrant an
`initiative` entity if its outputs turn out to be substantive.

`coverage: low`: UNCTAD's own mandate and structure were not researched, and
this entity records only its data-governance role.

Note the naming: the organisation now presents as "UN Trade and Development"
while the UNCTAD acronym remains in use. Both are recorded.

## Relationships

- Part of [[UN]].
- `influences` edge (UNCTAD as target) recorded on [[UN-GDC]]'s own file,
  added 2026-09-05 — paragraph 48 requests the CSTD working group.

## Sources

`unctad.org`, `dig.watch` and `sdg.iisd.org` remain blocked (HTTP 403) on
every attempt across two passes. The claim this entity exists to record
is now confirmed via a stronger, directly-read source instead: `un.org`'s
own Annex I: Global Digital Compact page. Wikipedia, geneva.china-mission.
gov.cn and inclusiveias.com (read in the prior pass) confirm UNCTAD's
general existence but not the working group specifically.
