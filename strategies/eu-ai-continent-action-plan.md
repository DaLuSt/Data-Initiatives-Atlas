---
id: EU-AI-CONTINENT-ACTION-PLAN
type: strategy
name: AI Continent Action Plan
alternative_names:
  - AI Continent Action Plan
  - COM(2025) 165
description: >
  European Commission strategy, presented 9 April 2025 as COM(2025) 165,
  setting out how the EU aims to become a global leader in artificial
  intelligence by turning its research talent and industrial base into "AI
  accelerators." Organised around five pillars — large-scale AI computing
  infrastructure, access to high-quality data, AI adoption in strategic
  sectors, AI skills and talent, and simplifying AI Act implementation — it
  is explicitly distinct from the AI Act itself: a competitiveness and
  adoption strategy rather than a binding legal instrument, one of whose
  five pillars is helping industry and member states implement the Act.

level: regional
country: null
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2025-04-09
end_date: null
last_verified: "2026-09-25"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-AI-ACT
  - EU-TECH-SOVEREIGNTY-PACKAGE
relationships:
  - type: related-to
    target: EU-AI-ACT
    source: fact
    evidence: "Confirmed by reading the European Commission's own 'AI continent action plan' page directly (2026-09-25): one of the plan's five pillars, 'Simplifying the implementation of the AI act,' states 'The Commission is supporting companies and EU countries in the implementation of the AI Act,' citing published guidelines on prohibited AI practices, codes of practice under development, and the AI Act Service Desk. This is support for adoption of an existing regulation, not a legislative or transposition relationship, so `related-to` is used rather than `implements-requirement-from` or `amends` — the plan does not change the Act's text or obligations. Closes discovery/unresolved.md row #40, which asked whether a distinct EU AI strategy, separate from the AI Act, exists."
    confidence: high
    valid_from: 2025-04-09
    valid_until: null

sources:
  - title: "Shaping Europe's leadership in artificial intelligence with the AI continent action plan"
    url: "https://commission.europa.eu/topics/competitiveness/ai-continent_en"
    publisher: "European Commission"
    accessed: "2026-09-25"
  - title: "AI Continent Action Plan COM(2025)165 (document listing on the Commission's own page; PDF itself not fetched)"
    url: "https://commission.europa.eu/document/download/f633985c-440a-4285-95c3-9fe16fd0fc65_en"
    publisher: "European Commission"
---

# AI Continent Action Plan

> **Created 2026-09-25**, closing `discovery/unresolved.md` row #40
> ("Is there a distinct EU AI strategy entity, separate from the AI Act?
> Searches returned mostly AI-and-cybersecurity material, no clearly
> identifiable standalone strategy document. No entity created."). The
> Commission's own "AI continent" page, read directly, names and dates
> the document the original search missed: COM(2025) 165, presented
> 9 April 2025.

## Description

Confirmed by reading the European Commission's own page directly: the
**AI Continent Action Plan** is the Commission's strategy "to turn EU
strengths, such as unparalleled talent and strong traditional industries,
into AI accelerators." It was presented **9 April 2025** as **COM(2025)
165**, with an accompanying Annex published the same day.

## Five pillars, all named directly on the Commission's own page

1. **Large-scale AI computing infrastructure** — at least 19 "AI
   factories" on Europe's supercomputing network, up to 5 "AI
   gigafactories," the InvestAI facility (€20 billion), and a proposed
   Cloud and AI Development Act aiming to triple EU data-centre capacity
   within five to seven years.
2. **Access to high-quality data** — a "data union strategy" and "data
   labs" within the AI factories.
3. **AI adoption in strategic sectors** — the "Apply AI Strategy,"
   responding to the page's own figure that only 13.5% of EU companies
   currently use AI.
4. **AI skills and talent** — educating and retaining AI experts within
   the EU and attracting talent from outside it.
5. **Simplifying AI Act implementation** — published guidelines on
   prohibited AI practices, codes of practice under development, and the
   AI Act Service Desk.

None of the four other pillars' named sub-initiatives (the Data Union
Strategy, Apply AI Strategy, InvestAI, or the proposed Cloud and AI
Development Act) is modelled as its own Atlas entity — named here in
prose as components of this plan, not separately researched.

## Distinct from the AI Act — the row's actual question

Row #40 asked whether a standalone EU AI strategy exists apart from
[[EU-AI-ACT]]. It does, and the Commission's own page draws the
distinction directly: the Action Plan is a competitiveness and adoption
strategy — investment, infrastructure, skills, data access — of which
*supporting the AI Act's implementation* is only the fifth of five
pillars, not the plan's subject. `related-to` [[EU-AI-ACT]] is recorded
rather than a stronger type, since the plan neither amends the Act's
text nor transposes an obligation — it funds and coordinates adoption
of AI generally, alongside helping industry comply with the Act that
already exists.

## Relationships

- `related-to` [[EU-AI-ACT]] — see above.
- Reached by [[EU-TECH-SOVEREIGNTY-PACKAGE]] (new 2026-09-25), which
  `related-to` this entity via a shared component — the Cloud and AI
  Development Act, one of the Tech Sovereignty Package's own two
  legislative proposals, which the Commission's own page says will
  "complement and support ... the AI Continent Action Plan." The edge is
  recorded on that entity's own file.

## Sources

Listed in frontmatter, both read directly.
