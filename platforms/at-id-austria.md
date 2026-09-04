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
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - AT
  - AT-BRZ
  - AT-EGOVG
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
  - type: governed-by
    target: AT-EGOVG
    source: fact
    evidence: "A research-queue pickup (2026-09-04) closed the 'four statutes, no legal-basis entity' gap this file previously carried unconfirmed. Reading ris.bka.gv.at's own consolidated E-Government-Gesetz text directly finds its §§4-7 define the E-ID (Elektronischer Identitätsnachweis) function ID Austria implements: a personal binding combining a qualified electronic signature with an encrypted Stammzahl and sector-specific identifier (bPK), with registration from age 14 via passport authorities or police. The Meldegesetz 1991, Passgesetz 1992 and Personenstandsgesetz 2013 — the other three statutes this file previously named — were also read directly and each cites the E-GovG's own E-ID function rather than granting one independently, so only the E-GovG carries this edge."
    confidence: medium
    valid_from: 2005-01-01
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
  - title: "E-Government-Gesetz - Bundesrecht konsolidiert"
    url: "https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20003230"
    publisher: "Rechtsinformationssystem des Bundes (RIS)"
    accessed: "2026-09-04"
---

# ID Austria

> **Verified 2026-08-26; legal basis closed 2026-09-04.** All three
> originally cited pages were read directly; BRZ's own page and
> oesterreich.gv.at's own imprint independently confirm the description
> and `maintained-by` edge in the government's own words. `bmdw.gv.at` —
> the ministry page this entity's original "four statutes" claim rested
> on — no longer resolves at all (checked by direct DNS lookup): the
> Bundesministerium für Digitalisierung und Wirtschaftsstandort itself
> appears to no longer exist as a separate ministry. Its digital-
> government platform, oesterreich.gv.at, states in its own imprint that
> it is now published by the **Bundeskanzleramt** (Federal Chancellery)
> — a real reorganisation, not a like-for-like URL move. A research-queue
> pickup then read all four statutes directly on `ris.bka.gv.at` and
> closed the legal-basis gap — see below.

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

## The legal basis, closed — and corrected

This entity previously claimed introducing the oesterreich.gv.at
platform and ID Austria required amendments to the **E-Government Act,
the Registration Act, the Civil Status Act and the Passport Act**,
sourced only to the now-dead `bmdw.gv.at` page, and had carried that
claim as unconfirmed since the source went dark — the same honest
treatment given [[FR-HEALTH-DATA-HUB]]'s unreconfirmed member count.

A research-queue pickup (2026-09-04) read all four statutes directly on
`ris.bka.gv.at`, Austria's official consolidated-law database, and
found a **narrower** picture than the original claim implied: only the
**E-Government-Gesetz** ([[AT-EGOVG]]) defines and grants the E-ID
function ID Austria implements, in its own §§4-7. The Meldegesetz 1991,
Passgesetz 1992 and Personenstandsgesetz 2013 each *cite* that same
E-GovG function to permit electronic registration, passport-expiry
notices and child-naming respectively — they consume the E-ID function
rather than each granting a separate one, so no fifth-way entity or
edge is created for any of them. The Austrian identity layer's
legal-basis gap — the same shape as [[ES-CLAVE]]'s still-queued
statutory basis — is now closed with a single `governed-by` edge to
[[AT-EGOVG]].

## Relationships

- `part-of` [[AT]].
- `maintained-by` [[AT-BRZ]].
- `governed-by` [[AT-EGOVG]] — closed 2026-09-04.

## Sources

Listed in frontmatter. BRZ's own product page and oesterreich.gv.at's
own homepage and imprint were read directly in the 2026-08-26 pass; the
dead `bmdw.gv.at` page this entity previously cited is gone. The
E-Government-Gesetz's own RIS text was read directly in the 2026-09-04
pass that closed the legal-basis gap.
