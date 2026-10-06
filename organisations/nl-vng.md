---
id: NL-VNG
type: organisation
name: Vereniging van Nederlandse Gemeenten
name_en: "Association of Netherlands Municipalities"
alternative_names:
  - VNG
  - Association of Netherlands Municipalities
description: >
  Association of Dutch municipalities. Within the data/digital ecosystem it
  coordinates joint municipal information management, runs the Common Ground
  programme, and represents municipalities in government-wide digital
  governance bodies.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-OBDO
  - NL-ICTU
relationships:
  - type: maintained-by
    target: NL-COMMON-GROUND
    source: interpretation
    evidence: "Recorded from the VNG side: Common Ground is presented on vng.nl as a VNG programme. Direction expressed as VNG→Common Ground for navigability; the authoritative framing belongs on the Common Ground entity."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: participates-in
    target: NL-OBDO
    source: fact
    evidence: "FIXES A SOURCING GAP: this edge cited digitaleoverheid.nl's MIDO governance page in evidence text since creation, but that page was never added to this entity's own `sources:` list, carried no accessed date, and was never independently read for this entity — an unread citation reused from NL-OBDO's own sourcing. Confirmed by reading the page directly 2026-09-27 via its WordPress REST API (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=governance — the workaround documented in discovery/unresolved.md row #216, the rendered page itself remaining bot-walled): 'Leden van het OBDO zijn onder andere vertegenwoordigers van ministeries, CIO Rijk, de Vereniging Nederlandse Gemeenten (VNG), het Interprovinciaal Overleg (IPO) en de Unie van Waterschappen (UvW)' (OBDO members include representatives of ministries, CIO Rijk, the VNG, IPO and UvW)."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Common Ground"
    url: "https://vng.nl/onderwerpen/common-ground"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-20"
  - title: "Governance Digitale Overheid"
    url: "https://vng.nl/artikelen/governance-digitale-overheid"
    publisher: "Vereniging van Nederlandse Gemeenten (VNG)"
    accessed: "2026-08-20"
  - title: "Governance Meerjarenprogramma Infrastructuur Digitale overheid (MIDO)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/governance/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-27"
    note: "Added this pass, closing a sourcing gap: this page was cited in the OBDO-membership edge's evidence since creation but never listed here or independently read. The rendered page is genuinely bot-walled (JavaScript verification challenge). Read directly via the site's own WordPress REST API instead (www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=governance) — the workaround documented in discovery/unresolved.md row #216."
---

# Vereniging van Nederlandse Gemeenten (VNG)

> **Verified 2026-08-20.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.
>
> **Closed 2026-09-27**: the OBDO-membership edge cited digitaleoverheid.nl's
> MIDO governance page in evidence text since creation, but that page was
> never listed in this entity's own `sources:` and was never independently
> read for this entity — a gap this pass fixes with a genuine direct read
> via the site's own WordPress REST API (the workaround documented in
> `discovery/unresolved.md` row #216), confirming VNG's membership in the
> OBDO's own words. `confidence` on that edge raised medium→high.

## Description

The VNG is the association of Dutch municipalities. It enters the Atlas
through its role in collective municipal information management: it runs the
[[NL-COMMON-GROUND]] programme, through which municipalities jointly
restructure their information provision, and it represents municipalities in
government-wide digital governance, including membership of the [[NL-OBDO]].
With [[NL-BZK]] it co-founded [[NL-ICTU]] in 2001.

`coverage: low` — the VNG's sourcing here is incidental to the Common Ground
and governance research rather than drawn from a general institutional
profile. A re-verification pass should add a primary VNG source about the
association itself.

## Relationships

- Runs [[NL-COMMON-GROUND]].
- Participates in [[NL-OBDO]].
- Co-founder of [[NL-ICTU]], with [[NL-BZK]].

## Sources

Listed in frontmatter. **3 of 3 now read directly**: the two vng.nl pages
(earlier pass), and, added 2026-09-27 to close a sourcing gap,
digitaleoverheid.nl's MIDO governance page via the site's own WordPress
REST API (`www.digitaleoverheid.nl/wp-json/wp/v2/pages?slug=governance`)
— the workaround documented in `discovery/unresolved.md` row #216.
