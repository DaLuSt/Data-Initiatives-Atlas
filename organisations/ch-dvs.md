---
id: CH-DVS
type: organisation
name: Digitale Verwaltung Schweiz
alternative_names:
  - DVS
  - ANS
  - ADS
  - Digital Public Services Switzerland
description: >
  Joint organisation of the Swiss Confederation, the cantons and the
  communes for the digital transformation of public administration,
  operational since January 2022. It succeeded the earlier E-Government
  Schweiz arrangement and coordinates digital government across all three
  levels of the Swiss federal system.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 2022-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH
  - CH-EMBAG
relationships:
  - type: part-of
    target: CH
    source: fact
    evidence: "Confirmed by reading digitale-verwaltung-schweiz.ch directly (2026-08-22): the site names itself 'Digitale Verwaltung Schweiz' and describes joint federal/cantonal projects (e.g. the AGOV authentication service, used across fourteen named cantons). The exact January 2022 operational-start date was NOT independently re-confirmed this pass — the homepage's current news content does not restate its own founding date, and no 'about us' subpage with that detail was located. Retained from the original sourcing rather than dropped. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Digitale Verwaltung Schweiz"
    url: "https://www.digitale-verwaltung-schweiz.ch/"
    publisher: "Digitale Verwaltung Schweiz (DVS)"
    accessed: "2026-08-22"
  - title: "#16 EMBAG: Ein Enabling-Gesetz der Digitalisierung"
    url: "https://www.digitale-verwaltung-schweiz.ch/blog/16-embag-ein-enabling-gesetz-der-digitalisierung"
    publisher: "Digitale Verwaltung Schweiz (DVS)"
    accessed: "2026-08-22"
  - title: "Administration numérique suisse"
    url: "https://www.administration-numerique-suisse.ch/"
    publisher: "Administration numérique suisse (ANS)"
    accessed: "2026-08-22"
  - title: "Digital Public Services Switzerland"
    url: "https://www.digitale-verwaltung-schweiz.ch/en"
    publisher: "Digital Public Services Switzerland (DPSS)"
    accessed: "2026-08-22"
  - title: "Amministrazione digitale Svizzera"
    url: "https://www.digitale-verwaltung-schweiz.ch/it"
    publisher: "Amministrazione digitale Svizzera (ADS)"
    accessed: "2026-08-22"
---

# Digitale Verwaltung Schweiz (DVS)

> **Verified 2026-08-22.** Both originally-cited pages were read directly,
> plus the French, English and Italian homepages fetched to check the
> other language abbreviations. One was wrong: the Italian abbreviation
> is **ADS** ("Amministrazione digitale Svizzera"), not "AND" as
> previously recorded — corrected. The English name is confirmed as
> "Digital Public Services Switzerland." The January 2022
> operational-start date could not be independently re-confirmed this
> pass and is retained rather than removed — see that relationship's
> evidence. Two findings worth flagging, neither acted on
> beyond recording: DVS's own homepage advertises **AGOV**, a nationwide
> authority-login service already used by fourteen cantons with "already
> 2 million accounts" — a Swiss analogue to [[GB-ONE-LOGIN]] not yet an
> Atlas entity — and reports that the Federal Council and the Conference
> of Cantonal Governments adopted a "Zielbild" (target vision) in late
> 2025 to evolve DVS toward "a political platform with binding
> standard-setting."

## Description

Confirmed by reading digitale-verwaltung-schweiz.ch directly (2026-08-22).
DVS is the joint organisation of the **Confederation, the cantons and the
communes** for digital transformation of public administration. It was set
up during 2021 and became operational from **January 2022** — this date
was not independently re-confirmed this pass; see the caveat above.

## The Atlas's first tri-level joint body

Every other digital-government body in the Atlas belongs to one level of
government. [[NO-DIGDIR]] is a national directorate; [[GB-GDS]] sits in
central government; [[DE-FITKO]] comes closest, as a federation/Länder
vehicle, but still spans two levels rather than three.

DVS is constituted jointly across **all three** Swiss levels. That is a
genuinely different organisational form, and it is the one the Atlas is
least equipped to represent: it has no `level: local`, so the communal third
of this body has nowhere to attach.

The entity is filed `level: national` because that is the closest available
value, **not because the description is accurate.** This is the clearest
single illustration of the `level` gap logged in
`discovery/candidates.md`.

## ⚠ `coverage: low`, and still no relationships beyond the anchor

Two federal pages were read directly this pass, both of DVS's own site.
Its legal form, its governance, and its predecessor *E-Government Schweiz*
remain unestablished — no dedicated "about us" or history page was
located.

DVS publishes a blog post about [[CH-EMBAG]], which is evidence it takes
an interest, not evidence of a role under the act — see [[CH-EMBAG]] for
the different edge that entity now carries to [[CH-OPENDATA-SWISS]]
instead. No edge from DVS to EMBAG is asserted.

## Sources

Listed in frontmatter, all five read directly this pass — the French,
English and Italian homepages were added to confirm ANS, DPSS and ADS.
