---
id: NL-DIGIBETER
type: strategy
name: "NL DIGIbeter: Agenda Digitale Overheid"
alternative_names:
  - NL DIGIbeter
  - Agenda Digitale Overheid
description: >
  Dutch government agenda for the digital government, launched in July 2018
  with 71 actions. Described as a 'rolling agenda' updated annually, with
  published actualisations in 2019 and 2020. Coordinated by the Ministry of
  the Interior and Kingdom Relations.

level: national
country: NL
region: null

status: superseded
confidence: medium
coverage: medium
verification: primary-source

start_date: 2018-07-01
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-DATA-AGENDA-OVERHEID
relationships: []

sources:
  - title: "Agenda Digitale Overheid 'NL DIGIbeter' (bijlage bij 26643, nr. 549) (parlementairemonitor.nl ceased operations in 2024)"
    url: "https://www.parlementairemonitor.nl/9353000/1/j9vvij5epmj1ey0/vkq4lkmrtfzs"
    publisher: "Parlementaire Monitor"
  - title: "Agenda Digitale Overheid geactualiseerd: NL DIGIbeter 2019 (confirmed dead, HTTP 404)"
    url: "https://www.digitaleoverheid.nl/nieuws/agenda-digitale-overheid-geactualiseerd-nl-digibeter-2019/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "NL DIGIbeter 2020 Agenda Digitale Overheid (bijlage bij 26643, nr. 700) (parlementairemonitor.nl ceased operations in 2024)"
    url: "https://www.parlementairemonitor.nl/9353000/1/j9vvij5epmj1ey0/vla5jymx4bw2"
    publisher: "Parlementaire Monitor"
  - title: "Kabinetsbeleid Digitalisering"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/kabinetsbeleid-digitalisering/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Kamerstuk 26643, nr. 700"
    url: "https://zoek.officielebekendmakingen.nl/kst-26643-700.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
    accessed: "2026-08-27"
---

# NL DIGIbeter: Agenda Digitale Overheid

> **Verified 2026-08-27, sources rebuilt, status resolved.** Both
> parlementairemonitor.nl citations are confirmed dead — that site ceased
> operations in 2024 and its URLs now serve only a generic page about the
> monitor itself, not the indexed documents; one digitaleoverheid.nl link
> returned HTTP 404. The kabinetsbeleid-digitalisering page was read
> directly and, for the first time, states plainly that NL DIGIbeter ended
> — closing the `status: unknown` question the prior text left open by
> policy. A Kamerstuk alternate was found and read to recover the 2020
> actualisation's content. `verification` moves from `search-only` to
> `primary-source`.

## Description

NL DIGIbeter is the Dutch government's agenda for the digital government,
launched in July 2018 with 71 actions of varying type and size. It was
conceived as a 'rolling agenda', updated annually; confirmed by reading
kst-26643-700.html directly, the 2020 actualisation — sent to the Tweede
Kamer on **29 June 2020** by State Secretary Knops — reports progress on
2019 actions (a chatbot developed with municipalities, the Perceelwijzer
land-data app, a "Startup in Residence" digital-literacy card game reaching
roughly 2,000 participants) and sets three priorities for 2020–2021:
digital inclusion, secure citizen-centred services, and the ethics of
technology deployment.

[[NL-BZK]] holds the coordinating role, from its responsibility for the
digital government and for safeguarding fundamental rights — carried over
from the prior text and consistent with kst-26643-700.html's own framing
(the State Secretary's letter).

**`status` is resolved, from `unknown` to `superseded`.**
Confirmed by reading digitaleoverheid.nl's own current policy-overview page
directly: it explicitly frames "NL Digibeter (2018-2020)" as a closed,
past-tense phase of government digitalisation policy, followed by
[[NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN]] (2022-2024), and then the
2025 [[NL-NDS]], which the same page states explicitly "does not replace
but connects existing plans."

**`successor` closed 2026-09-05.** The intervening strategy the prior pass
found named but unmodelled — picked up from this gap's own
`discovery/unresolved.md` entry — is now an Atlas entity. `successor` now
points to it rather than skipping ahead to [[NL-NDS]], which would have
overstated a two-steps-removed succession the sources never state directly.

## Relationships

- [[NL-DATA-AGENDA-OVERHEID]] is the data-specific agenda published under
  NL DIGIbeter.
- Coordinated by [[NL-BZK]].
- Superseded by [[NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN]] (via
  `successor`), which is itself superseded by [[NL-NDS]]. No direct
  `supersedes`/`superseded-by` relationship is asserted between this entity
  and [[NL-NDS]]: the actual named intervening strategy is the correct
  target, and skipping it would overstate what the sources say.

## Sources

Listed in frontmatter. digitaleoverheid.nl's kabinetsbeleid page and a
Kamerstuk alternate read directly this pass; both parlementairemonitor.nl
citations confirmed dead (site discontinued 2024) and one digitaleoverheid.nl
citation confirmed dead (HTTP 404).
