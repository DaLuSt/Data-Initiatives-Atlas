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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
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
    evidence: "Confirmed by reading cnctr.fr's own pages directly (2026-08-26): 'Les techniques de renseignement contrôlées par la CNCTR' and 'Les finalités' both describe the Prime Minister's authorisation process taken after the CNCTR's opinion, under the law of 24 July 2015. `legifrance.gouv.fr`'s JORF text of that law is genuinely bot-walled (403) even with an honest User-Agent, so the law's own text was not read."
    confidence: medium
    valid_from: 2015-07-24
    valid_until: null
  - type: applies-to
    target: FR-DGSE
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own 'Les principaux services de renseignement' page directly (2026-08-26): it lists and describes, by name, 'La Direction générale de la sécurité extérieure (DGSE)', 'La direction générale de la Sécurité intérieure (DGSI)', 'La direction du renseignement militaire (DRM)', 'La direction du renseignement et de la sécurité de la défense (DRSD)', 'La Direction nationale du renseignement et des enquêtes douanières (DNRED)' and TRACFIN as the six services of the intelligence community subject to the CNCTR's control."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-DGSI
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own 'Les principaux services de renseignement' page directly (2026-08-26): 'Service actif de la police nationale, la direction générale de la sécurité intérieure est chargée, sur l'ensemble du territoire de la République, de rechercher, de centraliser et d'exploiter le renseignement intéressant la sécurité nationale' — a new detail this entity did not previously carry (DGSI as an active service of the national police)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-DRM
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own 'Les principaux services de renseignement' page directly (2026-08-26): 'La direction du renseignement militaire a été créée par un décret du 16 juin 1992. Ses missions sont définies aux articles D.3126-10 et D.3126-14 du code de la défense, et son organisation est fixé par l'arrêté du 30 mars 2016' (the DRM was created by a decree of 16 June 1992; its missions are defined at articles D.3126-10 and D.3126-14 of the Code de la Défense, and its organisation set by the order of 30 March 2016) — a founding date and legal basis this cluster did not previously carry anywhere. The same page also notes DRM is one of two services (with TRACFIN) that do not have access to the full range of intelligence techniques, unlike the other four."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: FR-DRSD
    source: fact
    evidence: "Confirmed by reading cnctr.fr's own 'Les principaux services de renseignement' page directly (2026-08-26): 'La DRSD, service de renseignement dont dispose le ministre de la défense pour assumer ses responsabilités en matière de sécurité du personnel, des informations, du matériel et des installations sensibles, a notamment pour mission de mettre en œuvre des mesures de contre-ingérence' — matching the DRSD's own self-description found on defense.gouv.fr."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Les principaux services de renseignement"
    url: "https://www.cnctr.fr/services-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
    accessed: "2026-08-26"
  - title: "Les techniques de renseignement contrôlées par la CNCTR"
    url: "https://www.cnctr.fr/en/techniques-de-renseignement"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
    accessed: "2026-08-26"
  - title: "Les finalités pouvant légalement justifier le recours à des techniques de renseignement"
    url: "https://www.cnctr.fr/en/finalites"
    publisher: "Commission nationale de contrôle des techniques de renseignement (CNCTR)"
    accessed: "2026-08-26"
---

# Commission nationale de contrôle des techniques de renseignement (CNCTR)

> **Verified 2026-08-26.** All three cited pages were read directly.
> CNCTR's own services page names all six first-circle services and
> gives [[FR-DRM]] its first sourced founding date and legal basis
> (decree of 16 June 1992). `legifrance.gouv.fr` remains genuinely
> bot-walled.

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

Confirmed by reading cnctr.fr's own list directly (2026-08-26): it names
six principal services — DGSE, DGSI, DRM, DRSD, DNRED and TRACFIN. The
Atlas holds four — DNRED and TRACFIN are not modelled, as recorded on
[[FR-DGSE]] — so **the four edges here understate the CNCTR's remit by
two**. That is a coverage limit of the Atlas, and the entity says so
rather than letting the graph imply the commission oversees only what
is drawn.

The same page adds a nuance this entity did not previously carry: DRM
and TRACFIN are the two services that do **not** have access to the
full range of intelligence techniques the law provides, unlike the
other four — a distinction that qualifies [[FR-DRSD]]'s own claim to
use "all" the techniques, which the CNCTR's page does not contradict
for DRSD specifically.

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

Listed in frontmatter, all three read directly this pass.
