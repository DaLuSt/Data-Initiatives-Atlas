---
id: AT-ID-AUSTRIA
type: platform
name: ID Austria
alternative_names:
  - ID-Austria
description: >
  Austria's national digital identity, which enables citizens to prove
  their identity to digital applications and services. It is delivered by
  the Bundesrechenzentrum as an evolution of the earlier Handy-Signatur
  and Bürgerkarte, and is the access key to the oesterreich.gv.at digital
  government platform.

level: national
country: AT
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-26"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - AT
  - AT-BRZ
relationships:
  - type: part-of
    target: AT
    source: fact
    evidence: "Confirmed by reading brz.gv.at's own ID Austria page and oesterreich.gv.at directly (2026-08-26), both government-operated: anchor edge under metadata/relationship-types.md §2.3, asserting no more than national scope."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: AT-BRZ
    source: fact
    evidence: "Confirmed independently on two government pages, read directly (2026-08-26): brz.gv.at's own ID Austria page states 'Die ID Austria ist der österreichische elektronische Identitätsnachweis (eID), der es Menschen ermöglicht, sich sicher online zu identifizieren' (ID Austria is the Austrian electronic identity proof (eID) that lets people identify themselves securely online), presented among BRZ's own products; oesterreich.gv.at's own imprint states 'Technische Betreuung: Bundesrechenzentrum GmbH' (technical operation: Bundesrechenzentrum GmbH) for the platform ID Austria unlocks."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ID Austria - BRZ"
    url: "https://www.brz.gv.at/was-wir-tun/services-produkte/id-austria.html"
    publisher: "Bundesrechenzentrum (BRZ)"
    accessed: "2026-08-26"
  - title: "Startseite - oesterreich.gv.at"
    url: "https://www.oesterreich.gv.at/"
    publisher: "Bundeskanzleramt Österreich"
    accessed: "2026-08-26"
  - title: "Impressum - oesterreich.gv.at"
    url: "https://www.oesterreich.gv.at/de/ueber-oesterreichgvat/impressum"
    publisher: "Bundeskanzleramt Österreich"
    accessed: "2026-08-26"
---

# ID Austria

> **Verified 2026-08-26.** All three cited pages were read directly;
> BRZ's own page and oesterreich.gv.at's own imprint independently
> confirm the description and `maintained-by` edge in the government's
> own words. `bmdw.gv.at` — the ministry page this entity's "four
> statutes" claim rested on — no longer resolves at all (checked by
> direct DNS lookup): the Bundesministerium für Digitalisierung und
> Wirtschaftsstandort itself appears to no longer exist as a separate
> ministry. Its digital-government platform, oesterreich.gv.at, states
> in its own imprint that it is now published by the **Bundeskanzleramt**
> (Federal Chancellery) — a real reorganisation, not a like-for-like URL
> move. No replacement source for the specific four-statute claim was
> found, so it is not repeated as newly confirmed; see below.

## Description

Austria's national digital identity — the successor to two earlier
Austrian credentials. BRZ's own page states this directly: "Die ID
Austria ist eine Weiterentwicklung von Handy-Signatur und
Bürgerkarte" (ID Austria is a further development of the mobile-phone
signature and the citizen card), usable both by public administration
and the private sector, and able to sign PDF documents with an
electronic signature the source describes as "der eigenhändigen
Unterschrift gleichgestellt und europaweit einsetzbar" (equivalent to a
handwritten signature and usable EU-wide) — language that gestures at
eIDAS-style qualified electronic signatures without naming the
Regulation, so no [[EU-EIDAS]] relationship is asserted from this
alone.

## The digital-policy portfolio moved to the Chancellery

The platform ID Austria unlocks, oesterreich.gv.at, states in its own
imprint, read directly: "Herausgeber: Bundeskanzleramt Österreich"
(publisher: Federal Chancellery of Austria) — not a digitalisation
ministry. This entity's only other original source, `bmdw.gv.at` — the
Bundesministerium für Digitalisierung und Wirtschaftsstandort — is now
a dead domain, checked by direct DNS lookup. Read together, this looks
like the digital portfolio moving to the Chancellery rather than a mere
broken link, but no source read states that transition explicitly, so
it is reported as an observation, not a fact.

## Four statutes had to move — not reconfirmed this pass

This entity previously claimed introducing the oesterreich.gv.at
platform and ID Austria required amendments to the **E-Government Act,
the Registration Act, the Civil Status Act and the Passport Act**,
sourced only to the now-dead `bmdw.gv.at` page. Neither replacement
page read this pass (BRZ's or Digital Austria's) repeats this claim in
any form. It is carried forward as unconfirmed rather than dropped or
re-asserted as newly verified — the same honest treatment given
[[FR-HEALTH-DATA-HUB]]'s unreconfirmed member count when its source
went dark. None of the four acts is an Atlas entity, so the Austrian
identity layer still has a platform with no legal-basis entity attached
- the same shape as [[ES-CLAVE]], whose statutory basis is also queued.

## Sources

Listed in frontmatter, all three read directly this pass — BRZ's own
product page and oesterreich.gv.at's own homepage and imprint. The dead
`bmdw.gv.at` page this entity previously cited is gone; see caveat
above.
