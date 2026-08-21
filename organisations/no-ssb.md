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
start_date: null
end_date: null
last_verified: "2026-08-21"
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
---

# Statistisk sentralbyrå (SSB)

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`. ⚠
> `coverage: low` — see below.

## Description

SSB is Norway's national statistical institute.

## ⚠ No `part-of` [[EU-ESS]] edge, unlike every other statistical office here

Five national statistical offices in the Atlas carry `part-of` [[EU-ESS]]:
[[NL-CBS]], [[DE-DESTATIS]], [[BE-STATBEL]], [[ES-INE]] and [[PL-GUS]]. The
sixth, [[GB-ONS]], does not — it reaches the international layer through
[[UN-CES]] instead, having left the Union.

SSB is the **third pattern**, and the Atlas cannot yet state it.

The ESS is defined in its own sources as the partnership between the
Commission (Eurostat) and the national statistical institutes **of the
member states**. Norway is not a member state. EEA EFTA states participate
in European statistical cooperation under the EEA Agreement's own
provisions, on terms this batch did not establish.

Asserting `part-of` [[EU-ESS]] would put Norway in the member-state
category, which is the specific error the [[NO]] anchor exists to prevent.
Asserting nothing leaves the entity thin — and that is the honest state.
`EU-ESS` is listed in `related_entities` so the connection is discoverable
without being claimed.

This is the same shape as the missing `applies-in` edges: **the gap is the
finding.**

## ⚠ `coverage: low`

Only the institute's own front page and the Eurostat ESS page were returned
by search. Its statutory basis (*statistikkloven*), its governance and its
relationship to Eurostat are all unestablished. Compare [[PL-GUS]] and
[[DE-DESTATIS]], which have both a statute and an ESS edge.

## Sources

Listed in frontmatter.
