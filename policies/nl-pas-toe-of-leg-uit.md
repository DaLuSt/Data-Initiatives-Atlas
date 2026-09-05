---
id: NL-PAS-TOE-OF-LEG-UIT
type: policy
name: "'Pas toe of leg uit'-beleid"
alternative_names:
  - Pas toe of leg uit
  - Apply-or-explain policy
  - Comply or explain
description: >
  Dutch policy obliging (semi-)government organisations to apply the open
  standards on the 'pas toe of leg uit' list when procuring or
  (re)organising ICT above a stated threshold value of €50,000, or else to
  explain the deviation. The list is maintained by Forum Standaardisatie.

level: national
country: NL
region: null

status: active
confidence: high
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-FORUM-STANDAARDISATIE
related_entities:
  - NL-OBDO
relationships:
  - type: maintained-by
    target: NL-FORUM-STANDAARDISATIE
    source: fact
    evidence: "Forum Standaardisatie maintains the lijst open standaarden and publishes the 'pas toe of leg uit' policy and its assessment procedure (forumstandaardisatie.nl)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "The obligation applies to (semi-)government organisations in the Netherlands (forumstandaardisatie.nl/pas-toe-leg-uit-beleid). Confirmed by re-reading the same page directly (2026-09-05): its Definitions section states the obligation attaches to an 'ICT-dienst of ICT-product... welke bij aanschaf een waarde vertegenwoordigt van ten minste € 50.000' — an ICT service or product representing a procurement value of at least €50,000 — closing the previously-flagged unverified-threshold question."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "'Pas toe of leg uit'-beleid"
    url: "https://www.forumstandaardisatie.nl/pas-toe-leg-uit-beleid"
    publisher: "Forum Standaardisatie"
    accessed: "2026-09-05"
  - title: "Lijst open standaarden"
    url: "https://www.forumstandaardisatie.nl/open-standaarden"
    publisher: "Forum Standaardisatie"
    accessed: "2026-08-20"
  - title: "'Pas toe of leg uit'-standaarden (verplicht)"
    url: "https://www.forumstandaardisatie.nl/open-standaarden/verplicht"
    publisher: "Forum Standaardisatie"
    accessed: "2026-08-20"
  - title: "Toetsingsprocedure en criteria voor de lijst open standaarden"
    url: "https://www.forumstandaardisatie.nl/toetsingsprocedure-en-criteria-voor-de-lijst-open-standaarden"
    publisher: "Forum Standaardisatie"
    accessed: "2026-08-20"
---

# 'Pas toe of leg uit'-beleid

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.
>
> **Updated 2026-09-05**: the €50,000 procurement threshold, previously
> flagged as unverified, is now confirmed directly against
> forumstandaardisatie.nl's own Definitions section. `confidence` raised
> to `high`.

## Description

'Pas toe of leg uit' (apply or explain) is the Dutch open-standards policy.
All (semi-)government organisations are obliged to apply the open standards
appearing on the 'pas toe of leg uit' list when procuring or (re)organising
ICT above a stated purchase threshold of **€50,000**, confirmed by
re-reading forumstandaardisatie.nl's own page directly (2026-09-05): its
Definitions section defines the obligation as attaching to an *"ICT-dienst
of ICT-product... welke bij aanschaf een waarde vertegenwoordigt van ten
minste € 50.000."*

Where a procurement or development falls within an application area listed
on the list, the corresponding standard(s) must be applied or requested. If
relevant standards are requested in a procurement but no supplier offers
them, deviation is possible only for compelling reasons, which must be
disclosed in the organisation's annual report.

The list is split between standards carrying the obligation and a separate
list of recommended standards. Any organisation may nominate a standard for
addition to, or removal from, either list; a formal assessment procedure
against published criteria then applies. [[NL-FORUM-STANDAARDISATIE]]
maintains the list and runs that procedure; the [[NL-OBDO]] takes the
formal decisions.

The individual standards on the list are Batch 4 scope and are not yet Atlas
entities.

## Relationships

- Maintained by [[NL-FORUM-STANDAARDISATIE]]; decided by [[NL-OBDO]].
- Applies in [[NL]].

## Sources

Listed in frontmatter.
