---
id: NL-ODISSEI
type: organisation
name: Open Data Infrastructure for Social Science and Economic Innovations
alternative_names:
  - ODISSEI
description: >
  The Netherlands' national research infrastructure for the social
  sciences. A consortium of 45 member organisations, launched in 2016 and
  hosted by Erasmus University's School of Social and Behavioral Sciences,
  providing access to data (including CBS microdata and the LISS panel),
  secure supercomputing facilities and research support services.
  Operational budget comes from member contributions; strategic
  development is financed by external grants, principally NWO's Large
  Scale Research Infrastructure programme.

level: national
country: NL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2016-01-01
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-NWO
  - NL-CBS
  - NL-DANS
relationships:
  - type: related-to
    target: NL
    source: fact
    evidence: "Anchor edge (metadata/relationship-types.md §2.3): ODISSEI is a member-owned consortium of 45 organisations, not part of the Dutch state, so `related-to` is used rather than `part-of` — the same convention applied to NL-SURF and NL-NICTIZ. Confirmed by reading odissei-data.nl's own 'About ODISSEI' page directly (2026-09-05): governed by an independent Supervisory Board and Management Board, hosted administratively by Erasmus University."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About ODISSEI"
    url: "https://odissei-data.nl/en/about-odissei/"
    publisher: "ODISSEI"
    accessed: "2026-09-05"
---

# ODISSEI

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had flagged ODISSEI as "named alongside
> DANS/RIVM/NWO/SIDN, all now modelled; ODISSEI alone remains
> unresearched." Its own "About ODISSEI" page was read directly this pass.

## Description

ODISSEI is the Netherlands' **National Research Infrastructure for
Social Sciences**. Reading `odissei-data.nl`'s own page directly: it
provides "access to data, expertise and computing," including **CBS
microdata**, the **LISS panel**, secure supercomputing facilities (OSSC
and SANE), data-collection capabilities and research-support services
such as FAIR data support and ethical consultation.

## Structure and funding

Confirmed directly: ODISSEI was **launched in 2016** and is **hosted by
Erasmus University's** School of Social and Behavioral Sciences. It
operates as a **consortium of 45 member organisations**, governed by an
independent **Supervisory Board** (seven delegates, its highest
decision-making body) and a **Management Board** led by a Scientific
Director, with an Advisory Board alongside. Its operational budget comes
from member contributions; strategic development is financed by external
grants, principally **NWO's Large Scale Research Infrastructure
programme** — the same funding relationship, via [[NL-NWO]], that
underlies [[NL-DANS]]. The page cites over €25 million secured through
Roadmap and SSHOC-NL grants.

Because it is a member-owned consortium rather than a body of the Dutch
state, `related-to` [[NL]] is recorded as the anchor edge, the same
convention already used for [[NL-SURF]] and [[NL-NICTIZ]].

## Relationships

- `related-to` [[NL]] — anchor edge; member-owned consortium, not part of
  the state.

## Sources

Listed in frontmatter, read directly this pass.
