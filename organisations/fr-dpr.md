---
id: FR-DPR
type: organisation
name: Délégation parlementaire au renseignement
alternative_names:
  - DPR
  - Parliamentary Intelligence Delegation
description: >
  Joint body of the French National Assembly and Senate exercising
  parliamentary oversight of the general activity and resources of the
  specialised intelligence services, as distinct from the CNCTR's legality
  control of specific intelligence techniques. Established by the law of
  9 October 2007.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2007-10-09
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - FR-LOI-DPR-2007
  - FR-DGSE
  - FR-DGSI
  - FR-DRM
  - FR-DRSD
  - FR-CNCTR
relationships:
  - type: governed-by
    target: FR-LOI-DPR-2007
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (FR-CNCTR's own 'Not modelled' section, which named the DPR explicitly as France's missing parliamentary counterpart to DE-PKGR, GB-ISC and PL-KSS). Confirmed by reading legifrance.gouv.fr's own JORF text of the law of 9 October 2007 directly (2026-09-06), corroborated independently by the Assemblée nationale's own page on the délégation, in full agreement on composition and mission."
    confidence: high
    valid_from: 2007-10-09
    valid_until: null
  - type: applies-to
    target: FR-DGSE
    source: fact
    evidence: "The law's own text, read directly, gives the DPR's mandate as monitoring 'the general activity and means of specialised services' under the ministers responsible for internal security, defence, the economy and the budget — the same ministerial span [[FR-CNCTR]]'s own page uses to name its six services, of which DGSE, DGSI, DRM and DRSD are the four this Atlas models. See the body text for the two services (DNRED, TRACFIN) this edge does not cover."
    confidence: medium
    valid_from: 2007-10-09
    valid_until: null
  - type: applies-to
    target: FR-DGSI
    source: fact
    evidence: "Same evidence and caveat as the DGSE edge above: the law's ministerial-span wording covers DGSI's parent ministry (interior/internal security), matching FR-CNCTR's own remit."
    confidence: medium
    valid_from: 2007-10-09
    valid_until: null
  - type: applies-to
    target: FR-DRM
    source: fact
    evidence: "Same evidence and caveat as the DGSE edge above: the law's ministerial-span wording covers DRM's parent ministry (defence), matching FR-CNCTR's own remit."
    confidence: medium
    valid_from: 2007-10-09
    valid_until: null
  - type: applies-to
    target: FR-DRSD
    source: fact
    evidence: "Same evidence and caveat as the DGSE edge above: the law's ministerial-span wording covers DRSD's parent ministry (defence), matching FR-CNCTR's own remit."
    confidence: medium
    valid_from: 2007-10-09
    valid_until: null

sources:
  - title: "LOI n° 2007-1443 du 9 octobre 2007 portant création d'une délégation parlementaire au renseignement"
    url: "https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000252177/"
    publisher: "Légifrance (République française)"
    accessed: "2026-09-06"
  - title: "Délégation parlementaire au renseignement"
    url: "https://www.assemblee-nationale.fr/dyn/17/organes/offpar/delegation-parlementaire-au-renseignement"
    publisher: "Assemblée nationale"
    accessed: "2026-09-06"
---

# Délégation parlementaire au renseignement (DPR)

> **Created 2026-09-06**, closing a gap [[FR-CNCTR]] flagged explicitly:
> "France appears here with judicial-style control and no parliamentary
> control, which is not an accurate picture of French oversight." Two
> independent primary sources — Légifrance's own text of the founding law
> and the Assemblée nationale's own page — were read directly and agree.

## Description

The DPR is a **joint body** of the National Assembly and the Senate,
established by the **law of 9 October 2007**. Confirmed by reading
Légifrance's own text directly: it comprises **eight members** — four
deputies, four senators — plus the presidents of each chamber's permanent
committee for internal security and defence, who sit ex officio. Its
mission is to monitor "the general activity and means of specialised
services" under the ministers responsible for internal security, defence,
the economy and the budget: evaluating public policy in the field and
following current and future challenges, not reviewing individual
intelligence-gathering operations.

## Parliamentary control, not legality control

The same distinction the Atlas already draws for Germany, the UK and the
Netherlands now holds for France too:

- The **DPR** is parliamentary: political accountability for budgets,
  organisation and general activity, composed of legislators.
- **[[FR-CNCTR]]** is judicial-style legality control: an independent
  administrative authority of magistrates, parliamentarians and a
  technical expert, reviewing the authorisation and use of specific
  intelligence techniques.

France now shows the same pairing as [[DE-PKGR]]/[[DE-UKR]] and
[[GB-ISC]]/[[GB-IPCO]] — parliamentary oversight alongside independent
legality review — where before it showed only the CNCTR half.
[[PL-KSS]] remains the one Atlas country confirmed to have **only**
parliamentary oversight, and — as of 2026-09-06 — an ECHR finding that no
independent legality-review body exists there at all.

## What it may not see

Confirmed by reading Légifrance's own text directly: operational
activities, government instructions to the services, and exchanges with
foreign intelligence services are explicitly excluded from what ministers
must disclose to the delegation. Members and staff hold security
clearances under Penal Code Article 413-9 and are bound by
national-defence secrecy; the DPR publishes annual reports while
protecting classified material.

## Four of six services, the same understatement as CNCTR's

The DPR's ministerial-span wording (interior security, defence, economy,
budget) plausibly covers all six services [[FR-CNCTR]] names — including
DNRED and TRACFIN, under the economy/budget ministries — but neither
source read this pass names the six services individually for the DPR the
way CNCTR's own page does. The four `applies-to` edges here therefore
carry the same understatement CNCTR's own entity already documents: DNRED
and TRACFIN are not modelled, so the edges cover four of what is likely
six services in the DPR's actual remit.

## Not modelled

- **DNRED** and **TRACFIN** — see above and [[FR-CNCTR]].
- Amendments to the DPR's composition and remit since 2007 — later
  legislatures' own pages show renewed compositions, not researched here.

## Relationships

- `governed-by` [[FR-LOI-DPR-2007]].
- `applies-to` [[FR-DGSE]], [[FR-DGSI]], [[FR-DRM]] and [[FR-DRSD]] — the
  same four services [[FR-CNCTR]] carries, for the same coverage-limit
  reason.

## Sources

Listed in frontmatter, both read directly 2026-09-06 and in full
agreement.
