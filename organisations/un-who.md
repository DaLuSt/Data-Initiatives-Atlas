---
id: UN-WHO
type: organisation
name: World Health Organization
alternative_names:
  - WHO
description: >
  United Nations agency dedicated to advancing global health, founded in
  1948 under its Constitution. Governed by the World Health Assembly, on
  which all 194 member states sit. Runs the Global Health Observatory,
  its main international health-data platform.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1948-04-07
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-HEALTH
organisations: []
related_entities:
  - UN
  - UN-WHO-GHO
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading who.int's own 'About WHO' page directly (2026-09-05): 'The WHO is the United Nations agency dedicated to advancing global health,' founded in 1948 and governed by the World Health Assembly, on which WHO's 194 member states sit. The page's own wording is 'United Nations agency' rather than the more specific 'UN specialized agency' term used by secondary sources (e.g. Refworld, WHO's own history page), so the broader term actually confirmed on this page is used here rather than the more specific one."
    confidence: high
    valid_from: 1948-04-07
    valid_until: null

sources:
  - title: "About WHO"
    url: "https://www.who.int/about"
    publisher: "World Health Organization"
    accessed: "2026-09-05"
---

# World Health Organization (WHO)

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/candidates.md` had named "UN DESA, UNDP, WHO" together as
> "refused for want of sources" in Batch 13. This pass read `who.int`'s
> own "About WHO" page directly and found enough to model WHO on its own
> terms. [[UN-UNDP]] was separately confirmed the same pass; DESA remains
> unmodelled.

## Description

WHO is, in its own words, "the United Nations agency dedicated to
advancing global health" — it "connects nations, partners and people to
promote health, keep the world safe and serve the vulnerable." Confirmed
by reading `who.int`'s own page directly: founded **1948** under its
Constitution (in force from **7 April 1948**, celebrated annually as
World Health Day), governed by the **World Health Assembly**, on which
all **194 member states** sit.

## Runs the Global Health Observatory

WHO's main international health-data platform, the **Global Health
Observatory (GHO)**, is now a separate Atlas entity: [[UN-WHO-GHO]].

## Relationships

- Part of [[UN]].
- `maintained-by` edge (WHO as target) recorded on [[UN-WHO-GHO]]'s own
  file.

## Sources

Listed in frontmatter, read directly this pass.
