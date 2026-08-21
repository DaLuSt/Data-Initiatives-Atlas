---
id: EU-VOLUNTARY-REVIEW-2023
type: publication
name: EU Voluntary Review on the implementation of the 2030 Agenda for Sustainable Development
alternative_names:
  - EUVR
  - EU Voluntary Review 2023
  - "COM(2023) 700 final"
description: >
  The first EU-level voluntary review of the implementation of the 2030
  Agenda for Sustainable Development, adopted by the European Commission and
  presented at the United Nations High-level Political Forum on Sustainable
  Development in New York in July 2023. It takes stock of the Union's
  internal and external implementation of the Sustainable Development Goals
  and sets out a strategic overview of EU commitments and targets, including
  quantified 2030 targets where applicable.

level: regional
country: null
region: EU

status: completed
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains: []
organisations:
  - EU-COMMISSION
related_entities:
  - EU
  - EU-COMMISSION
  - UN-2030-AGENDA
  - EU-SDG-INDICATORS
  - EU-EUROSTAT
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "The European Union presented at the United Nations in New York its first Voluntary Review on the implementation of the 2030 Agenda for Sustainable Development; the EU reaffirmed by adopting the first EU Voluntary Review its commitment to the full and timely implementation of the 2030 Agenda through its internal and external action (ec.europa.eu press corner IP/23/3801; eur-lex.europa.eu CELEX 52023DC0700). NOT READ — search-only. Anchor edge under metadata/relationship-types.md §2.3 for an EU-scoped entity."
    confidence: medium
    valid_from: 2023-07-10
    valid_until: null
  - type: references
    target: UN-2030-AGENDA
    source: fact
    evidence: "The first ever EU-level Voluntary Review of the implementation of the 2030 Agenda for Sustainable Development took stock of the EU's internal and external implementation of the Sustainable Development Goals, and was a key input to the United Nations High Level Political Forum held from 10 to 20 July 2023 in New York (ec.europa.eu press corner IP/23/3801; hlpf.un.org 'Voluntary National Reviews 2023, European Union'; eur-lex.europa.eu CELEX 52023DC0700). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-07-10
    valid_until: null
  - type: references
    target: EU-SDG-INDICATORS
    source: fact
    evidence: "EU-SDG-INDICATORS already records that the European Commission contributed to the UN's global SDG monitoring in 2023 through the first EU voluntary review; the review reports on EU progress against the indicator set Eurostat coordinates (ec.europa.eu/eurostat SDG pages; ec.europa.eu press corner IP/23/3801). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-07-10
    valid_until: null

sources:
  - title: "EU Voluntary Review on the implementation of the 2030 Agenda for Sustainable Development — COM(2023) 700 final"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52023DC0700"
    publisher: "EUR-Lex — Publications Office of the European Union"
  - title: "The EU's Voluntary Review reaffirms commitment to delivering the Sustainable Development Goals at home and around the world (IP/23/3801)"
    url: "https://ec.europa.eu/commission/presscorner/detail/en/ip_23_3801"
    publisher: "European Commission"
  - title: "Voluntary National Reviews 2023 — European Union"
    url: "https://hlpf.un.org/countries/european-union/voluntary-national-reviews-2023"
    publisher: "United Nations High-level Political Forum on Sustainable Development"
  - title: "EU Voluntary Review on the Implementation of the 2030 Agenda for Sustainable Development"
    url: "https://www.eeas.europa.eu/eeas/eu-voluntary-review-implementation-2030-agenda-sustainable-development_en"
    publisher: "European External Action Service"
---

# EU Voluntary Review 2023

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

The **first** EU-level voluntary review of the implementation of the 2030
Agenda, presented at the **UN High-level Political Forum** in New York, held
**10–20 July 2023**. It takes stock of the Union's internal *and* external
implementation of the SDGs and gives a strategic overview of EU commitments
and targets, including quantified 2030 targets where applicable.

## This entity closes a recorded vocabulary gap — by not being a relationship

`discovery/candidates.md` §3 listed two EU↔UN interactions the vocabulary
could not express, and this was the second:

> **The 2023 EU voluntary review** submitted to UN global SDG monitoring —
> *"A one-off report submitted to a UN process. `references` would be the
> closest type and would misstate it."*

The page then argued that **two** such cases met the threshold for proposing
a new relationship type.

**One of the two was not a relationship problem at all.** The review is a
document. The Atlas has had a `publication` type since the ontology was
written and had never used it, so the only way to record the review was as an
edge between the Commission and something UN-shaped — and no edge of that
kind is honest. Given a node, the modelling is ordinary: a publication,
produced by the Commission, that `references` [[UN-2030-AGENDA]] and
[[EU-SDG-INDICATORS]].

`references` was called "the closest type and would misstate it" because it
was being asked to describe *the act of submitting a report to a forum*.
Between a document and the policy it reports on, it is simply correct.

The other case — the UNESCO–Commission agreement — **is** a real gap, and it
is resolved separately, in `metadata/relationship-types.md`, by adding
`cooperates-with`.

## Dates: what is sourced and what is not

The review was **presented at the HLPF, which ran 10–20 July 2023**; that is
what the sources state and it is the only date used in this entity's
relationships. The document also carries the reference **COM(2023) 700
final**, and no source in the set gives the date the Commission adopted it.
`start_date` is therefore `null` rather than a plausible-looking guess.

## What is not modelled

The **High-level Political Forum** itself has no entity, so nothing here says
the review was *submitted to* it. That is the residue of the original
problem: the forum is named in this entity's description and sources, and
queued in `discovery/research-queue.md`. It is a smaller gap than the one
that was recorded, and it is a missing node rather than a missing type.

## Relationships

- `part-of` [[EU]] — anchor edge.
- `references` [[UN-2030-AGENDA]] and [[EU-SDG-INDICATORS]].

## Sources

Listed in frontmatter — the EUR-Lex record of COM(2023) 700 final, the
Commission press release, the HLPF's own listing of the EU's review, and the
EEAS page.
