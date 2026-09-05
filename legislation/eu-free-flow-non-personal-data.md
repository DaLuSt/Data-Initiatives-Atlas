---
id: EU-FREE-FLOW-NON-PERSONAL-DATA
type: regulation
name: Free Flow of Non-Personal Data Regulation
alternative_names:
  - Regulation (EU) 2018/1807
  - FFD Regulation
description: >
  EU regulation establishing a framework for the free flow of non-personal
  electronic data within the Union, prohibiting unjustified data
  localisation requirements. Adopted 14 November 2018, published in the
  Official Journal 28 November 2018, and generally applicable from 28 May
  2019, with a 30 May 2021 deadline for member states to end existing
  localisation restrictions. One of three instruments the proposed Digital
  Omnibus would repeal, transferring its provisions into the Data Act.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2019-05-28
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-DATA-ACT
  - EU-GDPR
  - EU-DIGITAL-OMNIBUS
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "As an EU regulation it is binding in its entirety and directly applicable in all member states without national transposition. Confirmed by reading legislation.gov.uk's own retained-EU-law text of the Regulation directly (2026-09-05): full title 'Regulation (EU) 2018/1807 of the European Parliament and of the Council of 14 November 2018 on a framework for the free flow of non-personal data in the European Union', entered into force 20 days after Official Journal publication and became generally applicable six months after publication."
    confidence: high
    valid_from: 2019-05-28
    valid_until: null
  - type: related-to
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading legislation.gov.uk's own text directly (2026-09-05): the Regulation states it explicitly complements rather than replaces data protection law, and that GDPR's rules on personal data 'are not affected by this Regulation' — the two regimes are deliberately kept distinct, with mixed datasets receiving coordinated treatment under both."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Regulation (EU) 2018/1807 of the European Parliament and of the Council of 14 November 2018 on a framework for the free flow of non-personal data in the European Union"
    url: "https://www.legislation.gov.uk/eur/2018/1807/2020-01-31"
    publisher: "legislation.gov.uk (UK retained-EU-law mirror)"
    accessed: "2026-09-05"
  - title: "Regulation - 2018/1807 - EN - EUR-Lex (not read — eur-lex.europa.eu confirmed unreachable to this environment's fetch tooling)"
    url: "https://eur-lex.europa.eu/eli/reg/2018/1807/oj/eng"
    publisher: "EUR-Lex (Publications Office of the European Union)"
  - title: "New Regulation Favors Free Flow of Non-Personal Data in the EU"
    url: "https://www.jonesday.com/en/insights/2018/12/new-regulation-favors-free-flow-of-nonpersonal-dat"
    publisher: "Jones Day"
---

# Free Flow of Non-Personal Data Regulation

Picked up from `discovery/unresolved.md`, which flagged this instrument
as unmodelled despite being named as a repeal target in
[[EU-DIGITAL-OMNIBUS]]'s own sources — the repeal picture was incomplete
without a node for the third instrument.

## Description

Confirmed by reading legislation.gov.uk's own retained-EU-law text of the
Regulation directly: Regulation (EU) 2018/1807, adopted **14 November
2018**, establishes a framework for the free flow of non-personal
electronic data in the EU. Its central mechanism prohibits unjustified
**data localisation requirements** — rules forcing data to be stored or
processed within a specific member state — except where justified on
public-security grounds. It also covers data availability for competent
authorities and data-porting mechanisms for professional users switching
providers.

Per a WebSearch cross-check of the Regulation's own Official Journal
record: published **28 November 2018**, entered into force 20 days later,
and became generally applicable **28 May 2019** (six months after
publication) — recorded here as `start_date`. Member states separately
had until **30 May 2021** to bring any pre-existing data-localisation
measures into compliance.

## Relationship to data protection law

Read directly from legislation.gov.uk: the Regulation is explicit that it
does not affect GDPR's rules on personal data — the two regimes are
deliberately kept distinct, covering non-personal and personal data
respectively, with mixed datasets (the more common real-world case)
receiving coordinated treatment under both.

## Why this entity exists

[[EU-DIGITAL-OMNIBUS]]'s own re-verification pass (2026-08-28) confirmed,
from whitecase.com's and medialaws.eu's analyses, that the Omnibus
proposal would repeal three instruments — the Data Governance Act, the
Open Data Directive, and this Regulation — transferring them into the Data
Act. The first two already had Atlas entities ([[EU-DGA]],
[[EU-OPEN-DATA-DIRECTIVE]]); this Regulation did not, leaving the repeal
picture visibly incomplete. Not yet superseded: like [[EU-DGA]] and
[[EU-OPEN-DATA-DIRECTIVE]], `status` stays `active` because the Omnibus
remains a proposal, not adopted law.

## Relationships

- Applies in [[EU]] — directly applicable EU regulation, anchor edge.
- Related to [[EU-GDPR]] — deliberately non-overlapping regimes for
  non-personal vs. personal data.
- [[EU-DIGITAL-OMNIBUS]] proposes to repeal this Regulation — the typed
  `proposes-to-supersede` edge is recorded on that entity, pointing here,
  matching the convention already used for its edges to [[EU-DGA]] and
  [[EU-OPEN-DATA-DIRECTIVE]]. Not yet adopted, so `status` here stays
  `active`.

## Sources

Two of three read directly this pass (legislation.gov.uk, Jones Day);
EUR-Lex's own text was not — confirmed unreachable to this environment's
fetch tooling, consistent with every other EUR-Lex attempt logged
elsewhere in this Atlas.
