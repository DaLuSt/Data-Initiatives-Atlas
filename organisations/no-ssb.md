---
id: NO-SSB
type: organisation
name: Statistisk sentralbyrå
alternative_names:
  - SSB
  - Statistics Norway
description: >
  Norway's national statistical institute, responsible for producing and
  disseminating official statistics. As the statistical office of an EEA
  EFTA state it cooperates with Eurostat under the EEA Agreement's
  statistical provisions rather than as a member of the European Statistical
  System in the sense that applies to EU member states.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
organisation_role: executive
start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - "NO"
  - EU-ESS
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "Statistisk sentralbyrå is Norway's national statistical institute (ssb.no), confirmed 2026-08-21. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: EU-ESS
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #106). Confirmed by reading ec.europa.eu/eurostat's own 'Statistical cooperation in and around Europe' news page directly (2026-09-13): 'Iceland, Liechtenstein, and Norway participate in the European Statistical System (ESS) through the European Economic Area (EEA) agreement.' Independently corroborated on [[EU-ESS]]'s own file (re-verified 2026-08-28, reading the same Eurostat ESS overview page directly): 'The partnership also includes the EFTA countries.' Recorded as `participates-in` rather than `part-of` — the type the five member-state NSIs carry — preserving the distinction this entity's own text already draws: Norway participates under the EEA Agreement's own statistical provisions (Annex XXI / Protocol 30, per efta.int, itself bot-walled and unread), not as a member state."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Statistisk sentralbyrå"
    url: "https://www.ssb.no/"
    publisher: "Statistisk sentralbyrå (SSB)"
    accessed: "2026-08-21"
  - title: "European Statistical System (ESS)"
    url: "https://ec.europa.eu/eurostat/web/european-statistical-system"
    publisher: "Eurostat / European Commission"
    accessed: "2026-08-21"
  - title: "Statistics Norway — English"
    url: "https://www.ssb.no/en"
    publisher: "Statistisk sentralbyrå (SSB)"
    accessed: "2026-08-21"
  - title: "Statistical cooperation in and around Europe"
    url: "https://ec.europa.eu/eurostat/web/products-eurostat-news/-/wdn-20220913-1"
    publisher: "Eurostat — European Commission"
    accessed: "2026-09-13"
---

# Statistisk sentralbyrå (SSB)

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`. ⚠
> `coverage: low` — see below.
>
> **Updated 2026-09-13**: added `participates-in` [[EU-ESS]], closing
> `discovery/unresolved.md` row #106 — see below.

## Description

SSB is Norway's national statistical institute.

## A third pattern, now stated: `participates-in` rather than `part-of`

Five national statistical offices in the Atlas carry `part-of` [[EU-ESS]]:
[[NL-CBS]], [[DE-DESTATIS]], [[BE-STATBEL]], [[ES-INE]] and [[PL-GUS]]. The
sixth, [[GB-ONS]], does not — it reaches the international layer through
[[UN-CES]] instead, having left the Union.

SSB is a genuine third pattern, and it is now expressible. Confirmed by
reading `ec.europa.eu/eurostat`'s own "Statistical cooperation in and
around Europe" page directly: "Iceland, Liechtenstein, and Norway
participate in the European Statistical System (ESS) through the
European Economic Area (EEA) agreement." [[EU-ESS]]'s own file
independently found the same fact on Eurostat's ESS overview page: "the
partnership also includes the EFTA countries."

Norway is not a member state, so `part-of` — the edge the five member-state
NSIs carry — would overstate the relationship and put Norway in the
member-state category, which is the specific error the [[NO]] anchor
exists to prevent. `participates-in` is the correct, weaker type: Norway
takes part in the ESS under the EEA Agreement's own statistical
provisions (Annex XXI and Protocol 30, per `efta.int`'s own page on the
subject, itself bot-walled in this environment and not independently
read) rather than as a member.

## ⚠ `coverage: low`

Its statutory basis (*statistikkloven*) and its internal governance
remain unestablished. Compare [[PL-GUS]] and [[DE-DESTATIS]], which have
both a statute and an ESS edge.

## Relationships

- `part-of` [[NO]] — anchor edge.
- `participates-in` [[EU-ESS]] — added 2026-09-13, on the EEA Agreement's
  statistical provisions rather than as a member state.

## Sources

Listed in frontmatter, all four read directly.
