---
id: UN-2030-AGENDA
type: policy
name: "Transforming our world: the 2030 Agenda for Sustainable Development"
alternative_names:
  - 2030 Agenda
  - "A/RES/70/1"
  - Agenda 2030
description: >
  Resolution adopted by the United Nations General Assembly on 25 September
  2015 as A/RES/70/1. It sets out 17 Sustainable Development Goals and 169
  targets, framed as a shared global plan of action to end poverty, foster
  peace, safeguard the rights and dignity of all people and protect the
  planet by 2030. It is the policy instrument the global SDG indicator
  framework was built to monitor.

level: international
country: null
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: 2015-09-25
end_date: 2030-12-31
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations: []
related_entities:
  - UN
  - UN-SDG-INDICATORS
  - EU-SDG-INDICATORS
  - EU-VOLUNTARY-REVIEW-2023
  - UN-UNDP
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed by reading sdgs.un.org/2030agenda and unfpa.org's copy of the resolution directly (2026-08-28) — the network egress block that stopped this from being read in the prior pass is no longer in effect for these domains. Both confirm: General Assembly resolution A/RES/70/1, 'Transforming our world: the 2030 Agenda for Sustainable Development', adopted 25 September 2015, setting out 17 Sustainable Development Goals and 169 targets, framed around the principle that 'no one will be left behind.' docs.un.org/en/A/RES/70/1 was also fetched but returned only a bare document-viewer navigation shell with no readable resolution text, so it was not counted as read."
    confidence: high
    valid_from: 2015-09-25
    valid_until: null

sources:
  - title: "Transforming our world: the 2030 Agenda for Sustainable Development (A/RES/70/1)"
    url: "https://sdgs.un.org/2030agenda"
    publisher: "United Nations Department of Economic and Social Affairs"
    accessed: "2026-08-28"
  - title: "A/RES/70/1 — General Assembly resolution, seventieth session"
    url: "https://docs.un.org/en/A/RES/70/1"
    publisher: "United Nations"
  - title: "Transforming our World: The 2030 Agenda for Sustainable Development"
    url: "https://www.unfpa.org/resources/transforming-our-world-2030-agenda-sustainable-development"
    publisher: "United Nations Population Fund"
    accessed: "2026-08-28"
---

# The 2030 Agenda for Sustainable Development

> **Verified 2026-08-28.** Two of three cited pages were read directly this
> pass. The network egress block noted in the prior pass no longer applies
> to `sdgs.un.org` or `unfpa.org` — both loaded normally. `docs.un.org`
> returned only a JavaScript document-viewer shell with no resolution text
> and was not counted as read.

## Description

General Assembly resolution **A/RES/70/1**, adopted **25 September 2015**:
*Transforming our world: the 2030 Agenda for Sustainable Development*. It
sets out **17 Sustainable Development Goals** and **169 targets**, as a
shared plan of action to 2030.

## The instrument the indicator framework serves

`discovery/candidates.md` carried this as a candidate with a specific
diagnosis:

> *[[UN-SDG-INDICATORS]] models the indicator framework and has **no link to
> the policy instrument it serves***

and a specific reason for refusing it:

> *Nothing was found for the Agenda beyond passing references; a node built
> from those would be the thin encyclopedic entity the taxonomy threshold
> prevents*

The second half no longer holds, and the reason is worth recording because it
is a recurring pattern. The UN batch was searching Eurostat's SDG pages,
where the Agenda appears only as context for the indicators. Searching for
**the resolution** — by number — returns the resolution: its adopting body,
its date, its symbol, its structure of 17 goals and 169 targets, and its own
text. The Agenda was never thinly sourced; it was being looked for in the
wrong place.

This is the same lesson `discovery/candidates.md` already records at the end
of the "cheap structural fixes" section: **a refusal for want of a source is
not the same as a fact being unknowable.**

## Relationships

- `part-of` [[UN]] — anchor edge, and literally true of a General Assembly
  resolution.
- [[UN-SDG-INDICATORS]] `implements` this Agenda; the edge lives on the
  indicator framework, which is the instrument that operationalises the
  policy.
- [[EU-VOLUNTARY-REVIEW-2023]] `references` it.
- [[UN-UNDP]] `implements` this Agenda — added 2026-09-05, recorded on
  UNDP's own file.

## What is not modelled

The **High-level Political Forum on Sustainable Development**, the UN body
that receives voluntary national reviews, is not an entity. It is named in
[[EU-VOLUNTARY-REVIEW-2023]] and queued in `discovery/research-queue.md`.

## Sources

Listed in frontmatter — two of three read directly this pass: the UN DESA
page for the Agenda and UNFPA's copy of the resolution text. The UN
documents record of A/RES/70/1 loaded only as a navigation shell.
