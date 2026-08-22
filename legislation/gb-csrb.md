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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - GB-NCSC
related_entities:
  - GB-CAF
  - GB-NIS-REGULATIONS
  - EU-NIS2
  - ES-LCGC
relationships:
  - type: references
    target: GB-CAF
    source: fact
    evidence: "Confirmed by reading gov.uk's 'Summary of the Bill' factsheet (2026-08-22), which describes NCSC's 'recent launch of Cyber Assessment Framework version 4.0' and the bill's intent to place it on a firmer statutory footing."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: GB-NIS-REGULATIONS
    source: fact
    evidence: "Confirmed by reading gov.uk's 'Summary of the Bill' factsheet (2026-08-22): 'Since then, cyber criminals are exploiting new routes – managed service providers, data centres and critical parts of supply chains – to threaten our way of life ... By bringing into scope more of the core services.' This describes an extension of, not a replacement for, the NIS Regulations 2018 framework. CAVEAT: recorded as related-to because the Atlas has no relationship type for amendment."
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
    accessed: "2026-08-22"
  - title: "Five major changes to the regulation of cybersecurity in the UK under the Cyber Security and Resilience Bill"
    url: "https://www.globalpolicywatch.com/2025/11/five-major-changes-to-the-regulation-of-cybersecurity-in-the-uk-under-the-cyber-security-and-resilience-bill/"
    publisher: "Global Policy Watch (Covington)"
    accessed: "2026-08-22"
---

# Cyber Security and Resilience Bill

> **Verified 2026-08-22.** gov.uk's own "Summary of the Bill" factsheet
> and Global Policy Watch's legal commentary were read directly and
> confirmed the claims below. `commonslibrary.parliament.uk` returned a
> bot-defense challenge (403) and was not read.

## Description

Introduced to Parliament in **November 2025** and expected to receive Royal
Assent in 2026, the CSRB is the most significant reform to UK cyber security
regulation since [[GB-NIS-REGULATIONS]]. Confirmed on globalpolicywatch.com
(2026-08-22): the Bill "will amend the existing Network and Information
Systems Regulations 2018 ... to cover, among other things, data centers and
managed service providers ... [and] increase potential fines—up to GBP 17m
or 4% of the worldwide turnover." It **amends rather than replaces**
that instrument, and would:

- extend scope to **managed service providers, data centres and supply
  chains**;
- strengthen **reporting and enforcement**, with fines up to **£17 million
  or 4% of worldwide turnover**;
- put the **Cyber Assessment Framework** — confirmed on gov.uk to have
  recently reached "version 4.0" — on a firmer statutory footing as
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

## The Cyber Assessment Framework, now modelled

The CAF is central to this bill and is now an Atlas entity — [[GB-CAF]] —
which this bill `references`. It is the UK counterpart to [[NL-BIO]],
[[DE-IT-GRUNDSCHUTZ]] and [[ES-ENS]], and it is `aligned-with`
[[INTL-ISO-IEC-27001]], so the chain from an international standard down
through a national baseline to an EU directive is complete on the UK side.

[[GB-OFCOM]] is modelled too. **The sectoral competent authorities the bill
would empower — the departments for energy, transport, health and drinking
water — still are not.**

## `status: proposed`

Introduced November 2025, Royal Assent *expected* in 2026. This entity is
dated 17 August 2026 and the Atlas **has not established whether that has
happened** — the same class of uncertainty as [[GB-ICO]]'s Information
Commission. `proposed` is the honest value while that is unknown, and it
will be wrong the moment the bill passes.

## Relationships

- `references` [[GB-CAF]] — the framework this bill would put on a statutory
  footing.
- `related-to` [[GB-NIS-REGULATIONS]] — amendment, in the evidence string
  because no type carries it. The **fifth** amendment case in the Atlas; see
  [[GB-DUAA]] for the running tally.

## Sources

Listed in frontmatter — a Commons Library briefing (bot-walled, not read
this pass), a GOV.UK factsheet, and legal commentary. The originally cited
NCSC policy-statement PDF now 404s and was dropped rather than re-cited
unread.
