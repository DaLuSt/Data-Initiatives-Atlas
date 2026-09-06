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
confidence: high
coverage: medium
verification: primary-source
start_date: 2022-01-01
end_date: null
last_verified: "2026-09-06"
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
    evidence: "Confirmed by reading digitale-verwaltung-schweiz.ch and efd.admin.ch directly: the site names itself 'Digitale Verwaltung Schweiz' and describes joint federal/cantonal projects (e.g. the AGOV authentication service, used across fourteen named cantons). CLOSES A PREVIOUSLY-FLAGGED GAP: efd.admin.ch's own page, read directly 2026-09-06, independently confirms the January 2022 operational-start date, which a prior pass could not re-confirm. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: high
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
  - title: "Digitale Verwaltung Schweiz"
    url: "https://www.efd.admin.ch/de/digitale-verwaltung"
    publisher: "Eidgenössisches Finanzdepartement (EFD)"
    accessed: "2026-09-06"
---

# Digitale Verwaltung Schweiz (DVS)

> **Verified 2026-08-22; legal form, governance and predecessor closed
> 2026-09-06.** Both originally-cited pages were read directly, plus the
> French, English and Italian homepages fetched to check the other
> language abbreviations. One was wrong: the Italian abbreviation is
> **ADS** ("Amministrazione digitale Svizzera"), not "AND" as previously
> recorded — corrected. The English name is confirmed as "Digital Public
> Services Switzerland." efd.admin.ch's own page, read directly this
> pass, independently confirms the January 2022 operational-start date
> and closes the legal-form/governance/predecessor gap — see below. Two
> findings worth flagging, neither acted on beyond recording: DVS's own
> homepage advertises **AGOV**, a nationwide authority-login service
> already used by fourteen cantons with "already 2 million accounts" — a
> Swiss analogue to [[GB-ONE-LOGIN]] not yet an Atlas entity — and reports
> that the Federal Council and the Conference of Cantonal Governments
> adopted a "Zielbild" (target vision) in late 2025 to evolve DVS toward
> "a political platform with binding standard-setting."

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

## Legal form, governance and predecessor, closed 2026-09-06

**Closes a previously-flagged gap.** Confirmed by reading
efd.admin.ch's own page directly (the Federal Department of Finance,
EFD): DVS operates under an "öffentlich-rechtliche Rahmenvereinbarung
über die Digitale Verwaltung Schweiz" (a public-law framework agreement),
which entered into force on **1 January 2022** — independently
corroborating the operational-start date this entity already carried.

Its governance: **Peppino Giarritta**, the "Beauftragter von Bund und
Kantonen" (representative of the Confederation and the cantons), leads
the **Delegiertenversammlung** (delegates' assembly), the operative
governing body, and its **Geschäftsstelle** (business office) is
administratively housed at the EFD's General Secretariat.

DVS **succeeded E-Government Schweiz**, the tripartite organisation that
coordinated implementation of the previous e-government strategy through
end of 2021 — confirmed directly, though E-Government Schweiz is not
itself an Atlas entity and no `previous_version` edge is asserted to a
non-existent entity. A WebSearch-only synthesis (not independently
confirmed by a directly-read page) adds that the Swiss Informatics
Conference (SIK) was also absorbed; treated as unconfirmed context, not
adopted as a sourced fact.

`coverage` raised to `medium`; `confidence` raised to `high` on the
strength of an independent federal source (efd.admin.ch) corroborating
digitale-verwaltung-schweiz.ch's own account.

DVS publishes a blog post about [[CH-EMBAG]], which is evidence it takes
an interest, not evidence of a role under the act — see [[CH-EMBAG]] for
the different edge that entity now carries to [[CH-OPENDATA-SWISS]]
instead. No edge from DVS to EMBAG is asserted.

## Sources

Listed in frontmatter, all six read directly across two passes — the
French, English and Italian homepages were added to confirm ANS, DPSS and
ADS; efd.admin.ch, added and read directly 2026-09-06, closed the legal
form, governance and predecessor gap.
