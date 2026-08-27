---
id: NL-DATA-AGENDA-OVERHEID
type: strategy
name: "NL DIGITAAL: Data Agenda Overheid"
alternative_names:
  - Data Agenda Overheid
  - NL DIGITAAL
description: >
  Dutch government data agenda, published under the NL DIGIbeter agenda for
  the digital government. It sets out how data can better serve policymaking
  and the resolution of societal issues by government.

level: national
country: NL
region: null

status: superseded
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-DIGIBETER
relationships:
  - type: part-of
    target: NL-DIGIBETER
    source: fact
    evidence: "Confirmed by reading binnenlandsbestuur.nl directly (2026-08-27): 'The Data Agenda is a component of NL DIGIbeter: Agenda Digitale Overheid, which itself forms part of the broader Dutch Digitalization Strategy.' zoek.officielebekendmakingen.nl/kst-26643-597.html — the actual redirect target of the originally-cited parlementairemonitor.nl URL (that domain ceased operations in 2024 and now redirects to Kamerstuk pages) — was read directly and confirms the agenda was presented to the Tweede Kamer under Kamerstuk 26643, the same dossier number NL DIGIbeter's own actualisations use."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "NL DIGITAAL: Data Agenda Overheid (confirmed unreadable — garbled PDF binary)"
    url: "https://zoek.officielebekendmakingen.nl/blg-876545.pdf"
    publisher: "Overheid.nl — Officiële bekendmakingen"
  - title: "Brief regering; NL DIGITAAL: Data Agenda Overheid (redirects to kst-26643-597.html — parlementairemonitor.nl ceased operations in 2024)"
    url: "https://www.parlementairemonitor.nl/9353000/1/j9vvij5epmj1ey0/vkwwhns8u3zz"
    publisher: "Parlementaire Monitor"
  - title: "Kamerstuk 26643, nr. 597"
    url: "https://zoek.officielebekendmakingen.nl/kst-26643-597.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
    accessed: "2026-08-27"
  - title: "Agenda 'verantwoord datagebruik overheid' naar Kamer"
    url: "https://www.binnenlandsbestuur.nl/digitaal/informatiehuishouding/agenda-verantwoord-datagebruik-overheid-naar-kamer"
    publisher: "Binnenlands Bestuur"
    accessed: "2026-08-27"
---

# NL DIGITAAL: Data Agenda Overheid

> **Verified 2026-08-27, sources rebuilt.** The PDF originally cited
> returned unparseable binary on fetch, and the parlementairemonitor.nl URL
> now redirects to a generic page — that entire site ceased operations in
> 2024 and no longer serves its indexed documents, confirmed by following
> its own redirect. The redirect target (a Kamerstuk on
> officielebekendmakingen.nl) and one further alternate (a contemporary
> news report) were found and read directly instead, closing the date and
> status gaps. `verification` moves from `search-only` to `primary-source`.

## Description

The Data Agenda Overheid is the Dutch government's data-specific agenda,
published under [[NL-DIGIBETER]] and transmitted to parliament by
government letter under Kamerstuk 26643. Confirmed by reading
kst-26643-597.html directly: State Secretary Raymond Knops (BZK) presented
it, describing five focus areas for 2019–2021, including using data for
societal challenges (energy transition, crime prevention), government-wide
principles for responsible data handling, improving Data.overheid.nl, and
data-policy training via a Digital Government Academy.

**Date.** The two directly-read sources disagree by five days on the exact
day: kst-26643-597.html's own content places the presentation in March
2019 without a single unambiguous day being extractable from the text
returned, while binnenlandsbestuur.nl's contemporary report states **20
March 2019**. Rather than pick one, `start_date` is left `null` and the
description above says "presented in March 2019" — the month is
corroborated by both sources, the exact day is not.

**Status.** `status` moves from `unknown` to `superseded` this pass.
Confirmed by reading digitaleoverheid.nl's own current policy-overview page
directly: it frames Dutch digitalisation policy as three successive phases
— "NL Digibeter (2018-2020)," a "Werkagenda Waardengedreven Digitaliseren
(2022-2024)," and the "Nederlandse Digitaliseringsstrategie (2025)" — in
explicitly past tense for the first two. Since this agenda is part of
NL DIGIbeter, and NL DIGIbeter's own 2018–2020 period has ended per that
page, `status: superseded` is a reasonable reading, though **no successor
entity is named**: the intervening "Werkagenda Waardengedreven
Digitaliseren" is not yet an Atlas entity and is queued in
`discovery/research-queue.md`. `successor` is left `null` rather than
pointing at [[NL-NDS]] directly, since the 2025 strategy is two phases
removed and the digitaleoverheid.nl page itself frames it as connecting
existing plans rather than replacing them.

## Relationships

- Part of [[NL-DIGIBETER]] — confirmed this pass via binnenlandsbestuur.nl's
  own words.
- Coordinated by [[NL-BZK]], confirmed by kst-26643-597.html: BZK holds the
  coordinating role from its responsibility "voor de digitale overheid en
  het borgen van grondrechten" (for digital government and safeguarding
  fundamental rights).
- The relationship to [[NL-IBDS]] remains genuinely open — no source read
  this pass or previously states whether the IBDS extends, replaces, or
  merely overlaps with this agenda. See `discovery/unresolved.md`.

## Sources

Listed in frontmatter. Two new alternate sources read directly this pass
after the original PDF proved unparseable and parlementairemonitor.nl was
confirmed to have ceased operations (it now serves only a generic page
about itself, not the indexed document).
