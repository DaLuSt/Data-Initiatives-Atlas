---
id: INTL-X-ROAD
type: technology
name: X-Road
alternative_names:
  - X-Road®
  - X-tee (Estonian deployment)
description: >
  Open-source data exchange layer for secure, unified data exchange
  between organisations, owned and developed by the Nordic Institute for
  Interoperability Solutions and released under the MIT licence. It
  originated as Estonia's national data exchange layer, passed into joint
  Estonian-Finnish stewardship in 2017, and is deployed internationally
  beyond its member states.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-NIIS
  - EE-X-TEE
relationships:
  - type: maintained-by
    target: INTL-NIIS
    source: fact
    evidence: "niis.org's own History page, re-read directly 2026-11-22: after the 2013 Memorandum of Understanding between Estonia and Finland, 'The Parties decided to deepen the cooperation in a more formal yet flexible manner by forming a separate jointly managed special purpose organisation to administer the X-Road development – the Nordic Institute for Interoperability Solutions', and the X-Road core was published 'as open source under the MIT licence ... in two parts in 2015–2016'. e-estonia.com and x-road.global's history page, read 2026-08-28, give NIIS the same role. The founding month (June 2017) and the 3 October 2016 release day came from an encyclopedia article and are not relied on (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "X-Road"
    url: "https://en.wikipedia.org/wiki/X-Road"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "Nordic Institute for Interoperability Solutions — History"
    url: "https://www.niis.org/history"
    publisher: "Nordic Institute for Interoperability Solutions (NIIS)"
    accessed: "2026-08-28"
  - title: "e-Estonia — NIIS"
    url: "https://e-estonia.com/solutions/interoperability-services/niis/"
    publisher: "e-Estonia"
    accessed: "2026-08-28"
  - title: "X-Road — X-Road History"
    url: "https://x-road.global/xroad-history"
    publisher: "X-Road (NIIS)"
    accessed: "2026-08-28"
  - title: "Changes in the X-Road Development"
    url: "https://www.niis.org/blog/2018/5/27/changes-in-the-x-road-development"
    publisher: "Nordic Institute for Interoperability Solutions (NIIS)"
    accessed: "2026-08-28"
---

# X-Road

> **Verified 2026-08-28.** All three originally-cited pages were read
> directly, plus x-road.global's own history page as a fourth, added to
> the sources list. `verification` moves from `search-only` to
> `primary-source`. Two corrections follow from the read.

## Description

The open-source data exchange software that Estonia's [[EE-X-TEE]] runs on,
released under the **MIT licence** and free to any individual or
organisation.

## A national system that became an international product

This is a shape the Atlas has not held before. [[NL-DIGIKOPPELING]],
[[BE-BELGIF]] and their peers are national artefacts that stayed national.
X-Road began as Estonia's data exchange layer, was taken into **joint
Estonian–Finnish ownership** under [[INTL-NIIS]] in 2017, and is now
deployed well beyond its members.

**⚠ Correction: the "Japan" claim does not survive a direct read.** The
previous pass asserted "Japan among the adopters cited" from search results
alone. x-road.global's own history page — the authoritative deployment
record, read directly this pass — lists Finland, the Faroe Islands
("Heldin"), El Salvador ("Tenoli"), Iceland, Åland and Ukraine as adopters
and partners, and does **not** mention Japan. Wikipedia's X-Road article,
also read directly, likewise says nothing about Japan. The claim is
therefore dropped rather than repeated; if a Japanese deployment exists it
is not confirmed by either source this Atlas cites.

The Atlas therefore separates two things a single name usually hides:

| | |
|---|---|
| **[[INTL-X-ROAD]]** | the software, owned and developed by [[INTL-NIIS]] |
| **[[EE-X-TEE]]** | Estonia's own deployment of it |

That is the same separation the Atlas already makes for [[INTL-DCAT]] and
[[NL-DCAT-AP-NL]] — a specification and a national instantiation are not one
entity — and it is the reason a reader can ask "who else runs this?" without
the question collapsing into "who else is Estonia?"

## Naming

**X-tee** is the Estonian name and **X-Road** the international one. Search
results before this pass claimed the English name of the *Estonian* system
changed to X-tee specifically in 2018. That precise date was not confirmed
by any page read directly: Wikipedia's X-Road article does not state it,
and niis.org's own blog post on the 2018 transition ("Changes in the X-Road
Development," read this pass) documents the transfer of core development
responsibility to NIIS in June 2018 without discussing a naming change. The
underlying distinction — X-tee for Estonia's deployment, X-Road for the
shared international technology — is well corroborated by both niis.org
and x-road.global; the specific year of the naming split is left
unconfirmed rather than restated as settled fact.

## Not modelled

The deployments outside the member states — the Faroe Islands, El Salvador,
Åland and Ukraine, named by x-road.global's own history page — because no
source read gives them enough substance to create country-scoped entities,
and several are sub-national or autonomous territories the `level`
vocabulary cannot express, the same reason [[INTL-NIIS]] does not model
them either.

## Sources

Listed in frontmatter, all five read directly this pass.

