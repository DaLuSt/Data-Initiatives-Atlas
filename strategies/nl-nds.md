---
id: NL-NDS
type: strategy
name: Nederlandse Digitaliseringsstrategie
alternative_names:
  - NDS
  - "De Nederlandse Digitaliseringsstrategie — Samen versnellen"
description: >
  Joint Dutch digitalisation strategy of municipalities, provinces, water
  authorities, public service providers and central government, published in
  July 2025. It aims to connect existing digitalisation plans and set
  shared priorities across administrative tiers.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2025-07-04
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-FDS
  - NL-DIGIBETER
  - NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN
  - NL-VNG
  - NL-IPO
  - NL-UVW
relationships:
  - type: references
    target: NL-FDS
    source: fact
    evidence: "Confirmed by reading rijksoverheid.nl's own announcement directly (2026-08-27): one of the six priorities is 'data sharing – implementing a federated data system with standards across government levels.' digitaleoverheid.nl's own NDS page and timeline, also read directly, confirm this priority was jointly determined by stakeholders on 2 December 2024, during Phase 1 of the strategy's development."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "De Nederlandse Digitaliseringsstrategie — Samen versnellen"
    url: "https://www.rijksoverheid.nl/documenten/rapporten/2025/07/04/nederlandse-digitaliseringsstrategie"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "Nederland versnelt met vernieuwde Digitaliseringsstrategie"
    url: "https://www.rijksoverheid.nl/actueel/nieuws/2025/07/04/nederland-versnelt-met-vernieuwde-digitaliseringsstrategie"
    publisher: "Rijksoverheid"
    accessed: "2026-08-27"
  - title: "Nederlandse Digitaliseringsstrategie (NDS)"
    url: "https://www.digitaleoverheid.nl/nederlandse-digitaliseringsstrategie-nds/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Tijdlijn NDS"
    url: "https://www.digitaleoverheid.nl/nederlandse-digitaliseringsstrategie-nds/tijdlijn-nds/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Nieuwe kabinet duidelijk: de NDS gaat door"
    url: "https://www.digitaleoverheid.nl/nieuws-nds/nieuwe-kabinet-duidelijk-de-nds-gaat-door/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
---

# Nederlandse Digitaliseringsstrategie (NDS)

> **Verified 2026-08-27, continuation confirmed.** All four originally-cited
> pages were read directly, plus a fifth found and read this pass that
> resolves the entity's central open question: whether the NDS survived the
> change of cabinet. It has. `verification` moves from `search-only` to
> `primary-source`; `confidence` from `low` to `medium`.

## Description

The NDS is a joint digitalisation strategy of municipalities, provinces,
water authorities, public service providers and central government.
Confirmed by reading rijksoverheid.nl directly: it was published on
**4 July 2025**, and brings the tiers together as "één overheid" (one
unified government). Its stated purpose, per digitaleoverheid.nl's own
timeline (read directly), is to connect existing digitalisation plans and
set priorities as one government — the timeline records the process in
detail: a start letter to parliament on 7 November 2024, joint
prioritisation by stakeholders on 2 December 2024, an NDS Council announced
12 February 2025 chaired by Nathan Ducastel, and ministerial approval
before the 4 July 2025 publication.

Confirmed priorities, read directly from rijksoverheid.nl and
digitaleoverheid.nl (the two pages give slightly different framings —
rijksoverheid.nl's news article lists six numbered focus areas;
digitaleoverheid.nl's own NDS page frames "6 Priorities" plus "3
Interventions"): cloud (a sovereign government cloud and marketplace);
data sharing via a federated data system with cross-government standards;
responsible use of AI; a citizen/entrepreneur-centred "one government"
experience; digital resilience and reduced dependency on foreign tech
providers; and digital-skills development in the civil service. The three
interventions named on digitaleoverheid.nl — standards, IT procurement, and
legislation — were not previously recorded.

`status: active` is now confirmed rather than merely un-withdrawn.
**This pass resolves the genuine continuation question the prior text
flagged.** digitaleoverheid.nl's own article, read directly, confirms: "The
programme continues and retains the same name. Prioritization determines
the further course." State secretaries from **EZK and BZK** jointly
confirmed continuation — a shift from BZK's sole prior coordination — with
the EZK state secretary for digital economy and sovereignty now overseeing
the programme, no additional funding allocated, and prioritisation
frameworks set by participating teams in April 2026. `confidence` moves
from `low` to `medium` on the strength of this confirmation, though the
exact division of ministerial responsibility going forward is still not
fully settled from what was read.

## Relationship to earlier agendas

digitaleoverheid.nl's own current policy-overview page, read directly this
pass (from the [[NL-DIGIBETER]] side of this pass's research), states the
NDS explicitly "does not replace but connects existing plans" and identifies
an intervening strategy — [[NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN]]
(2022-2024) — between [[NL-DIGIBETER]] (2018-2020) and the NDS (2025). That
intervening strategy is now an Atlas entity (created 2026-09-05), and it
does carry a sourced `supersedes` edge back to [[NL-DIGIBETER]] — the
kabinetsbeleid page treats that first transition as a real succession
("NL Digibeter" ended). **No `previous_version`/`successor` is asserted
here**, though: this entity's own source explicitly declines the successor
framing for itself specifically, so extending the chain one more step to
this entity would overstate what digitaleoverheid.nl actually says about
the NDS's own relationship to what came before it.

## Relationships

- References [[NL-FDS]] as the mechanism for data-driven working — confirmed
  this pass, plus a specific date (2 December 2024) for when that priority
  was set.
- Joint strategy across [[NL-BZK]], [[NL-VNG]], [[NL-IPO]] and [[NL-UVW]] —
  the "one government" framing is confirmed by rijksoverheid.nl directly,
  though none of the five sources read this pass names VNG, IPO or UvW
  individually; they are carried over from the prior text's characterisation
  of "municipalities, provinces, water authorities."
- Not a confirmed successor to [[NL-DIGIBETER]] or to
  [[NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN]] — see above; the
  relationship is actively ruled against by this entity's own source,
  rather than merely unconfirmed.
- Continuation under the post-2025 cabinet is confirmed, with EZK now
  co-leading alongside BZK. EZK does not yet exist in the Atlas as an
  organisation entity.

## Scope note

A `strategy`, not an organisation, so outside Batch 2's nominal scope. It
was added because it surfaced during Batch 2 organisation research, is a
high-priority national strategy that Batch 1 missed, and bears directly on
an open Batch 1 question.

## Sources

Listed in frontmatter, all five read directly this pass (four originally
cited, plus the continuation article found this pass).
