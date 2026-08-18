---
id: FR-CNCTR
type: organisation
name: Commission nationale de contrôle des techniques de renseignement
alternative_names:
  - CNCTR
  - National Commission for the Control of Intelligence Techniques
description: >
  French independent administrative authority that controls the use of
  intelligence-gathering techniques, both before authorisation and after
  implementation. Requests to use a technique go to the Prime Minister, who
  decides after seeking the CNCTR's opinion. It is composed of magistrates,
  parliamentarians and a person qualified in electronic communications.

level: national
country: FR
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - FR-LOI-RENSEIGNEMENT-2015
  - FR-DGSE
  - FR-DGSI
  - FR-DRM
  - FR-DRSD
relationships:
  - type: governed-by
    target: FR-LOI-RENSEIGNEMENT-2015
    source: fact
    evidence: "Requests to use intelligence techniques are addressed to the Prime Minister, who grants or denies authorisation after seeking the opinion of the CNCTR; the CNCTR is an independent administrative authority composed of magistrates, a person qualified in electronic communications and parliamentarians, and conducts both prior and posterior control of the techniques governed by the law of 24 July 2015 (cnctr.fr 'Les techniques de renseignement contrôlées par la CNCTR' and 'Les finalités'; legifrance.gouv.fr JORFTEXT000030931899). NOT READ — search-only."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null
  - type: applies-to
    target: FR-DGSE
    source: fact
    evidence: "The CNCTR publishes the list of the principal intelligence services subject to its control, comprising the first-circle services DGSE, DGSI, DRM, DRSD, DNRED and TRACFIN, and conducts prior and posterior control of the intelligence techniques they use (cnctr.fr 'Les principaux services de renseignement'; cnctr.fr 'Les techniques de renseignement contrôlées par la CNCTR'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-DGSI
    source: fact
    evidence: "The CNCTR publishes the list of the principal intelligence services subject to its control, comprising the first-circle services DGSE, DGSI, DRM, DRSD, DNRED and TRACFIN (cnctr.fr 'Les principaux services de renseignement'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-DRM
    source: fact
    evidence: "The CNCTR publishes the list of the principal intelligence services subject to its control, comprising the first-circle services DGSE, DGSI, DRM, DRSD, DNRED and TRACFIN (cnctr.fr 'Les principaux services de renseignement'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-DRSD
    source: fact
    evidence: "The CNCTR publishes the list of the principal intelligence services subject to its control, comprising the first-circle services DGSE, DGSI, DRM, DRSD, DNRED and TRACFIN; the DRSD is authorised to implement all intelligence-gathering techniques governed by the July 2015 law (cnctr.fr 'Les principaux services de renseignement'; fr.wikipedia.org 'Direction du renseignement et de la sécurité de la Défense'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Les techniques de renseignement contrôlées par la CNCTR"
    url: "https://www.cnctr.fr/en/techniques-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
  - title: "Les finalités pouvant légalement justifier le recours à des techniques de renseignement"
    url: "https://www.cnctr.fr/en/finalites"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
---

# Commission nationale de contrôle des techniques de renseignement (CNCTR)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The CNCTR is an **independent administrative authority** controlling the use
of intelligence-gathering techniques by the French services. It exercises
both *prior* control — before a technique is authorised — and *posterior*
control, checking that implementation matched the legal framework.

Its composition mixes three professions on purpose: **magistrates**,
**parliamentarians**, and a **person qualified in electronic
communications**. Judicial, democratic and technical competence in one body.

## Its opinion is an opinion

This is the sharpest contrast in the batch, and it runs directly against
[[NL-TIB]].

- In France, a request goes to the **Prime Minister**, who grants or refuses
  it **after seeking the CNCTR's opinion**. The Prime Minister may proceed
  against that opinion.
- In the Netherlands, [[NL-TIB]]'s decision is **binding**. A ministerial
  authorisation the TIB finds unlawful does not take effect.

France's counterweight is judicial rather than pre-emptive: the 2015 law
opens a right of appeal to the **Conseil d'État** to any citizen with an
interest in acting, and the CNCTR itself may refer a matter there when it
believes an authorisation was granted irregularly. The Conseil d'État can
annul the decision, compensate the applicant, **order the destruction of
collected data**, and refer the matter to the public prosecutor.

Two different answers to the same problem: stop it in advance, or unwind it
afterwards through a court.

## The four services, and the two that are not here

The CNCTR's own list of principal services is the source for the
`applies-to` edges, and it names six. The Atlas holds four — DNRED and
TRACFIN are not modelled, as recorded on [[FR-DGSE]] — so **the four edges
here understate the CNCTR's remit by two**. That is a coverage limit of the
Atlas, and the entity says so rather than letting the graph imply the
commission oversees only what is drawn.

## Not modelled

- The **Conseil d'État**, which the appeal route runs to.
- The **délégation parlementaire au renseignement (DPR)**, France's
  parliamentary oversight body — the counterpart to [[DE-PKGR]],
  [[GB-ISC]] and [[PL-KSS]]. It was not researched, so France appears here
  with judicial-style control and no parliamentary control, which is **not**
  an accurate picture of French oversight.

## Relationships

- `governed-by` [[FR-LOI-RENSEIGNEMENT-2015]].
- `applies-to` [[FR-DGSE]], [[FR-DGSI]], [[FR-DRM]] and [[FR-DRSD]].

## Sources

Listed in frontmatter.
