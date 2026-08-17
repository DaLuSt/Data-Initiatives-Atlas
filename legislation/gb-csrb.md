---
id: GB-CSRB
type: law
name: Cyber Security and Resilience (Network and Information Systems) Bill
alternative_names:
  - Cyber Security and Resilience Bill
  - CSRB
description: >
  United Kingdom bill introduced to Parliament in November 2025, described
  as the most significant reform of the UK cyber security framework since
  the Network and Information Systems Regulations 2018. It amends rather
  than replaces the existing framework, extending its reach to new
  categories of organisation including managed service providers and data
  centres, strengthening reporting and enforcement, addressing supply
  chains, and placing the National Cyber Security Centre's Cyber Assessment
  Framework on a firmer statutory footing as the baseline standard for
  organisations in scope. It was expected to receive Royal Assent in 2026.

level: national
country: GB
region: null

status: proposed
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - GB-NCSC
related_entities:
  - GB-NIS-REGULATIONS
  - EU-NIS2
  - ES-LCGC
relationships:
  - type: related-to
    target: GB-NIS-REGULATIONS
    source: fact
    evidence: "The Cyber Security and Resilience Bill was introduced to Parliament in November 2025 and updates the UK's cyber security legislation covering critical national infrastructure primarily by amending the Network and Information Systems Regulations 2018; it amends rather than replaces the existing NIS framework, extending its reach to new categories of organisation, strengthening reporting and enforcement, and placing the NCSC Cyber Assessment Framework on a firmer statutory footing (commonslibrary.parliament.uk CBP-10442; gov.uk 'Summary of the Bill'; ncsc.gov.uk policy statement; globalpolicywatch.com). NOT READ — search-only. CAVEAT: recorded as related-to because the Atlas has no relationship type for amendment."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Cyber Security and Resilience (Network and Information Systems) Bill 2024-26 — research briefing CBP-10442"
    url: "https://commonslibrary.parliament.uk/research-briefings/cbp-10442/"
    publisher: "House of Commons Library"
  - title: "Cyber Security and Resilience (Network and Information Systems) Bill factsheets — Summary of the Bill"
    url: "https://www.gov.uk/government/publications/cyber-security-and-resilience-network-and-information-systems-bill-factsheets/summary-of-the-bill"
    publisher: "GOV.UK"
  - title: "Cyber Security and Resilience Bill — policy statement"
    url: "https://www.ncsc.gov.uk/pdfs/blog-post/cyber-security-resilience-bill-policy-statement.pdf"
    publisher: "National Cyber Security Centre (UK)"
  - title: "Five major changes to the regulation of cybersecurity in the UK under the Cyber Security and Resilience Bill"
    url: "https://www.globalpolicywatch.com/2025/11/five-major-changes-to-the-regulation-of-cybersecurity-in-the-uk-under-the-cyber-security-and-resilience-bill/"
    publisher: "Global Policy Watch (Covington)"
---

# Cyber Security and Resilience Bill

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

Introduced to Parliament in **November 2025** and expected to receive Royal
Assent in 2026, the CSRB is the most significant reform to UK cyber security
regulation since [[GB-NIS-REGULATIONS]]. It **amends rather than replaces**
that instrument, and would:

- extend scope to **managed service providers, data centres and supply
  chains**;
- strengthen **reporting and enforcement**;
- put the **Cyber Assessment Framework** on a firmer statutory footing as
  the baseline for organisations in scope.

## Parallel evolution, not transposition

This is what the UK did instead of NIS2, and the comparison is exact enough
to be worth stating carefully.

|  | [[EU-NIS2]] | This bill |
|---|---|---|
| Relationship to the 2016 framework | **repeals** [[EU-NIS]] | **amends** the 2018 Regulations |
| Scope extension | essential/important entities, wide sectoral expansion | MSPs, data centres, supply chains |
| Baseline | national baselines, unharmonised | the NCSC's Cyber Assessment Framework |
| Status | in force since Jan 2023, transposition due Oct 2024 | **`proposed`**, introduced Nov 2025 |

Both start from the 2016 NIS framework. Both extend scope to managed
service providers and supply chains. Neither derives from the other, and
**no relationship between them is asserted** — they are two jurisdictions
reacting to the same threat landscape, which is not a relationship. The same
position was taken for [[FR-FRANCECONNECT]] and [[DE-BUNDID]], and for
[[ES-ENS]] against [[NL-BIO]].

What can be said is that the UK is **roughly a year behind the EU's
timetable and about nine years after the shared starting point**, and that
its instrument is domestic in origin.

## The second `proposed` cyber instrument

[[ES-LCGC]] is the other one — a Spanish draft implementing NIS2. The two
are `proposed` for opposite reasons: Spain is **late transposing an
obligation** and has drawn a reasoned opinion for it; the UK is **under no
obligation at all** and is legislating on its own schedule. The status value
is identical and carries none of that difference.

## The Cyber Assessment Framework is not modelled

The CAF is central to this bill and is **not an Atlas entity**. Neither is
Ofcom, nor the sectoral competent authorities the bill would empower. The
CAF is the UK counterpart to [[NL-BIO]], [[DE-IT-GRUNDSCHUTZ]] and
[[ES-ENS]], all three of which are modelled — see [[GB-NCSC]], where the
same gap is recorded.

## `status: proposed`

Introduced November 2025, Royal Assent *expected* in 2026. This entity is
dated 17 August 2026 and the Atlas **has not established whether that has
happened** — the same class of uncertainty as [[GB-ICO]]'s Information
Commission. `proposed` is the honest value while that is unknown, and it
will be wrong the moment the bill passes.

## Relationships

- `related-to` [[GB-NIS-REGULATIONS]] — amendment, in the evidence string
  because no type carries it. The **fifth** amendment case in the Atlas; see
  [[GB-DUAA]] for the running tally.

## Sources

Listed in frontmatter — a Commons Library briefing, a GOV.UK factsheet, an
NCSC policy statement and legal commentary. Three of the four are official.
