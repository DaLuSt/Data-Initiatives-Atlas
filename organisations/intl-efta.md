---
id: INTL-EFTA
type: organisation
name: European Free Trade Association
alternative_names:
  - EFTA
description: >
  Intergovernmental organisation of Iceland, Liechtenstein, Norway and
  Switzerland, set up in 1960 by seven founding states for the promotion of
  free trade and economic integration. Three of its four members — Iceland,
  Liechtenstein and Norway — are also parties to the Agreement on the
  European Economic Area and are known as the EEA EFTA states; Switzerland
  is not, and regulates its relationship with the European Union through
  bilateral agreements instead. Of the original seven members, all but
  Norway and Switzerland have since left to join the European Union.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 1960-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-EEA-AGREEMENT
  - EU
  - INTL-EFTA-SURVEILLANCE-AUTHORITY
  - INTL-EFTA-COURT
relationships:
  - type: related-to
    target: INTL-EEA-AGREEMENT
    source: fact
    evidence: "Confirmed verbatim by reading efta.int's own 'The European Free Trade Association' page directly (2026-08-22, fetched with an honest, identifying User-Agent — efta.int returns a bot-defense challenge to a browser User-Agent but real content to one that names itself as a bot): 'The European Free Trade Association (EFTA) is the intergovernmental organisation of Iceland, Liechtenstein, Norway and Switzerland. It was set up in 1960 by its then seven Member States for the promotion of free trade and economic integration between its members,' and its main tasks include 'Managing the Agreement on the European Economic Area (EEA Agreement), which brings together the Member States of the European Union and three of the EFTA States – Iceland, Liechtenstein and Norway – in a single market.' Corroborated by reading en.wikipedia.org/wiki/European_Free_Trade_Association directly: 'To participate in the EU's single market, Iceland, Liechtenstein, and Norway are parties to the Agreement on a European Economic Area (EEA) ... Switzerland has a set of multilateral agreements with the EU and its member states instead.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-EFTA-SURVEILLANCE-AUTHORITY
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/European_Free_Trade_Association directly (2026-08-22): 'The EFTA Surveillance Authority and the EFTA Court regulate the activities of the EFTA members in respect of their obligations in the European Economic Area (EEA). Since Switzerland is not an EEA member, it does not participate in these institutions.' Recorded here as `related-to` rather than `part-of` for the same reason the Authority's own entity gives: its jurisdiction (the three EEA EFTA states) does not match EFTA's own membership (which includes Switzerland)."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-EFTA-COURT
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/European_Free_Trade_Association directly (2026-08-22), same passage as the Surveillance Authority edge above. Recorded as `related-to` rather than `part-of` for the same reason: the Court's jurisdiction excludes Switzerland."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "The European Free Trade Association"
    url: "https://www.efta.int/about-efta/european-free-trade-association"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "European Free Trade Association"
    url: "https://en.wikipedia.org/wiki/European_Free_Trade_Association"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "The EEA EFTA States"
    url: "https://www.efta.int/eea-relations-eu/eea-institutions-two-pillar-structure/eea-efta-states"
    publisher: "European Free Trade Association (EFTA)"
  - title: "EU, EEA, EFTA and Schengen Area countries"
    url: "https://www.government.nl/themes/international-cooperation/european-union/eu-eea-efta-and-schengen-area-countries"
    publisher: "Government of the Netherlands"
---

# EFTA

> **Verified 2026-08-22, and a correction to standing guidance.**
> `efta.int` was treated as bot-walled (403) in every earlier pass this
> session on the strength of a browser-spoofing User-Agent. Fetched
> instead with an honest, identifying User-Agent, `efta.int` returns real
> content — 200, not 403 — and its own "About EFTA" page was read
> directly and confirms the founding date and the four-member list
> verbatim; en.wikipedia.org's article corroborates independently and
> supplies the EFTA/EEA split. The gap this entity's own "Not modelled"
> section named — the EFTA Surveillance Authority, the EFTA Court and the
> EEA Joint Committee — is closed: all three are now Atlas entities.

## Description

The four-state free trade association that [[NO]]'s entity has listed under
"not modelled" since the Norway batch, created here because [[IS]] and
[[LI]] joined the Atlas and the gap became three countries wide.

## Four members, two relationships to EU law

EFTA membership and EEA membership are not the same thing, and the split runs
straight through this organisation:

| State | EFTA | EEA | How EU law reaches it |
|---|---|---|---|
| [[IS]] | yes | yes | Incorporation into [[INTL-EEA-AGREEMENT]], then national implementation |
| [[LI]] | yes | yes | Same |
| [[NO]] | yes | yes | Same |
| [[CH]] | yes | **no** | Bilateral agreements and autonomous law |

Switzerland's electorate rejected EEA membership in 1992, and the bilateral
route has been the Swiss arrangement ever since. [[CH]] records what that
means for data protection specifically.

## A one-way door

Of EFTA's seven founding members, five have left — and every one of them left
for the European Union: [[AT]], [[DK]], [[PT]], [[SE]] and [[GB]], joined
later by [[FI]], which acceded to EFTA after the founding.

No state has ever moved the other way. That makes EFTA the clearest available
illustration of a fact the Atlas's country layer otherwise only implies: the
European integration frameworks are ordered, and states move up them.

## Not modelled

- ~~The **EFTA Surveillance Authority** and the **EFTA Court**~~ — now
  [[INTL-EFTA-SURVEILLANCE-AUTHORITY]] and [[INTL-EFTA-COURT]].
- ~~The **EEA Joint Committee**~~ — now [[INTL-EEA-JOINT-COMMITTEE]].
- EFTA's free trade agreements with third countries.
- The **EFTA Council**, the **EFTA Secretariat** and the **Standing
  Committee** — EFTA's own institutions, as opposed to the EEA institutions
  above.

## Sources

Listed in frontmatter.
