---
id: UN-HLPF
type: organisation
name: United Nations High-level Political Forum on Sustainable Development
alternative_names:
  - HLPF
  - High-level Political Forum
description: >
  The central United Nations platform for the follow-up and review of the
  2030 Agenda for Sustainable Development and its 17 Sustainable
  Development Goals. It is held annually in New York under the auspices
  of the UN Economic and Social Council and, every four years, also
  under the UN General Assembly. It receives Voluntary National Reviews
  from UN member states and voluntary reviews from other bodies, such as
  the European Union's first review in July 2023, and replaced the
  Commission on Sustainable Development on 24 September 2013.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2013-07-09
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - UN
  - UN-2030-AGENDA
  - EU-VOLUNTARY-REVIEW-2023
relationships:
  - type: part-of
    target: UN
    source: fact
    evidence: "Confirmed verbatim by reading sustainabledevelopment.un.org's own 'High-level Political Forum on Sustainable Development' page directly (2026-08-22): 'The High-level Political Forum on Sustainable Development (HLPF) is the central United Nations platform for the follow-up and review of the 2030 Agenda for Sustainable Development and its 17 Sustainable Development Goals (SDGs).' Corroborated by reading en.wikipedia.org/wiki/High-level_Political_Forum_on_Sustainable_Development directly, whose infobox names its parent organisations as 'United Nations Economic and Social Council' and 'United Nations General Assembly' — both principal UN organs, neither separately modelled in the Atlas — so this anchors directly to [[UN]] under metadata/relationship-types.md §2.3. `hlpf.un.org`, the Forum's own subdomain and the URL already cited on [[EU-VOLUNTARY-REVIEW-2023]], returns a bot-defense challenge (403) even with an honest, identifying User-Agent; `sustainabledevelopment.un.org` — a different UN Department of Economic and Social Affairs subdomain carrying the same content — was not blocked and is cited instead."
    confidence: medium
    valid_from: 2013-07-09
    valid_until: null

sources:
  - title: "High-level Political Forum on Sustainable Development"
    url: "https://sustainabledevelopment.un.org/hlpf"
    publisher: "United Nations Department of Economic and Social Affairs"
    accessed: "2026-08-22"
  - title: "United Nations High-level Political Forum on Sustainable Development"
    url: "https://en.wikipedia.org/wiki/High-level_Political_Forum_on_Sustainable_Development"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Voluntary National Reviews 2023 — European Union"
    url: "https://hlpf.un.org/countries/european-union/voluntary-national-reviews-2023"
    publisher: "United Nations High-level Political Forum on Sustainable Development"
---

# United Nations High-level Political Forum on Sustainable Development

> **Closes a gap named on two discovery pages.** [[EU-VOLUNTARY-REVIEW-2023]]
> has said since it was created that "the review was a key input to the
> United Nations High Level Political Forum," and that the Forum itself
> "has no entity, so nothing here says the review was *submitted to* it.
> That is the residue of the original problem." `discovery/candidates.md`
> and `discovery/research-queue.md` both carried the same row. This
> entity closes it, and [[EU-VOLUNTARY-REVIEW-2023]] now carries the
> `references` edge its own text said was missing.

## Description

Confirmed verbatim by reading sustainabledevelopment.un.org's own page
directly (2026-08-22): "The High-level Political Forum on Sustainable
Development (HLPF) is the central United Nations platform for the
follow-up and review of the 2030 Agenda for Sustainable Development and
its 17 Sustainable Development Goals (SDGs)." It meets annually — "The
2026 HLPF will be convened from Tuesday, 7 July, to Wednesday, 15 July
2026" — and is where [[EU-VOLUNTARY-REVIEW-2023]] and every UN member
state's Voluntary National Review is presented.

## History

Confirmed by reading en.wikipedia.org directly (2026-08-22): the Forum
was formed on **9 July 2013** and "replaced the Commission on Sustainable
Development on the 24 September 2013." Its infobox names its parent
organisations as the UN Economic and Social Council and the UN General
Assembly — under whose joint authority it holds two different kinds of
meeting, an annual ministerial-level session under ECOSOC and a
higher-level session under the General Assembly every four years.

## The forum's own domain is bot-walled; a sibling domain is not

`hlpf.un.org` — the domain this Atlas already cited, unread, on
[[EU-VOLUNTARY-REVIEW-2023]] — returns a bot-defense challenge (403) to
every path tried, an honest User-Agent included. This entity is sourced
instead from `sustainabledevelopment.un.org`, a UN DESA subdomain
carrying the same institutional description, and from Wikipedia for the
founding history `sustainabledevelopment.un.org` does not carry. The
`hlpf.un.org` citation for the EU's specific review remains in the
sources list, cited but unread, since it names something real even if
its content could not be confirmed this pass.

## Not modelled

- The **Commission on Sustainable Development**, the body the HLPF
  replaced in 2013.
- Individual **Voluntary National Reviews** other than the EU's, and the
  **ministerial declarations** the Forum adopts.
- The distinction between the Forum's **ECOSOC-level** annual meetings
  and its **General-Assembly-level** meetings every fourth year — named
  above in prose, not modelled as separate entities.

## Sources

Listed in frontmatter. `sustainabledevelopment.un.org` and the Wikipedia
article were read directly this pass; `hlpf.un.org` remains bot-walled
(403) and unread.
