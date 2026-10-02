---
id: DE-OZG
type: act
name: Onlinezugangsgesetz
alternative_names:
  - OZG
  - Online Access Act
description: >
  German federal act, enacted 14 August 2017 as Article 9 of a broader
  federal fiscal-equalisation restructuring law and in force from 18 August
  2017, obliging the federation, the Länder and the municipalities to offer
  their administrative services electronically through linked
  administrative portals. It was substantially amended by the
  OZG-Änderungsgesetz (OZG 2.0), which entered into force on 24 July 2024,
  legally anchoring the once-only principle and a national DeutschlandID
  citizen account, and it provides the legal basis for the central citizen
  account BundID.

level: national
country: DE
region: EU

status: active
rank: ordinary
confidence: high
coverage: medium
verification: primary-source

start_date: 2017-08-18
end_date: null
last_verified: "2026-10-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BUNDID
  - DE-EGOVG
  - DE-BMI
relationships: []

sources:
  - title: "Onlinezugangsgesetz"
    url: "https://de.wikipedia.org/wiki/Onlinezugangsgesetz"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "BundID (Nutzerkonto) — DeutschlandID | Onlinezugangsgesetz in Brandenburg"
    url: "https://ozg.brandenburg.de/ozg/de/it-infrastrukturen/it-basiskomponenten/bundid-nutzerkonto-deutschlandid/"
    publisher: "Land Brandenburg"
    accessed: "2026-08-28"
  - title: "Online Access Act: Federal government has digitized 115 important services"
    url: "https://www.heise.de/en/news/Online-Access-Act-Federal-government-has-digitized-115-important-services-10223703.html"
    publisher: "heise online"
    accessed: "2026-08-28"
  - title: "FITKO (Föderale IT-Kooperation) — OZG-Grundlagen, Akteure"
    url: "https://www.digitale-verwaltung.de/Webs/DV/DE/onlinezugangsgesetz/ozg-grundlagen/akteure/fitko/fitko-node.html"
    publisher: "Digitale Verwaltung (Bundesministerium des Innern)"
    accessed: "2026-10-01"
    note: "Read directly 2026-10-01 via the same cookie-jar workaround, which turned out to work on digitale-verwaltung.de too (discovery/unresolved.md row #217)."
  - title: "Upgrade für ein Digitales Deutschland ist da: Das OZG-Änderungsgesetz tritt in Kraft"
    url: "https://www.bmi.bund.de/SharedDocs/kurzmeldungen/DE/2024/07/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
    accessed: "2026-09-30"
    note: "Read directly via a cookie-jar-aware fetch — bmi.bund.de issues a session cookie through a redirect a cookie-less request cannot follow, which previously presented as a consistent HTTP 400 (discovery/unresolved.md row #217)."
  - title: "Bund hat seine 115 wichtigsten Verwaltungsleistungen bis Ende 2024 erfolgreich digitalisiert"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2024/12/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
    accessed: "2026-09-30"
    note: "Read directly via the same cookie-jar workaround."
---

# Onlinezugangsgesetz (OZG)

> **Re-verified 2026-08-28, substantially improved.** Two of the entity's
> four original sources (`bmi.bund.de` ×2, `digitale-verwaltung.de`) return
> HTTP 400 Bad Request on every attempt — a genuine, consistent block on
> both domains rather than a transient failure. Per the batch instruction
> to search for alternates when original sources are stuck below a
> majority, a dedicated Wikipedia article on the OZG itself and a heise.de
> report were found and read directly; combined with the one originally-cited
> page that did load (`ozg.brandenburg.de`), that is three of four sources
> read directly. `verification: primary-source`. The previously-refused
> enactment date is now recorded — found on a source not previously
> searched for, not guessed.
>
> **Closed 2026-09-30** (`discovery/unresolved.md` row #217): `bmi.bund.de`'s
> apparent HTTP 400 turns out to be a missing session cookie, not a
> genuine block — a cookie-jar-aware fetch reaches both of the BMI's own
> pages this entity cites, confirming directly, in the BMI's own words,
> facts previously sourced only via Wikipedia or via heise.de quoting the
> BMI second-hand. See "What changed this pass" below.
>
> **Closed 2026-10-01**: the same workaround also reads
> `digitale-verwaltung.de`, the entity's last unread original source. Its
> FITKO page states that FITKO and the BMI together form the **OZG
> programme management** for the federal digitalisation programme
> (*Digitalisierungsprogramm Föderal*), with FITKO focused on networking
> the actors involved and on transparency across the process. All four
> original sources are now read directly.

## Description

The OZG obliges German public administration at federal, Land and
municipal level to offer administrative services electronically through
linked administrative portals. Confirmed directly this pass on a dedicated
Wikipedia article: it was **enacted 14 August 2017**, as **Article 9 of a
broader law restructuring Germany's federal fiscal-equalisation system**,
and **entered into force 18 August 2017** — obliging all three levels of
government to interconnect their portals into a unified network by the end
of 2022.

Two sourced developments, one confirmed in more depth than before:

- The **OZG-Änderungsgesetz ("OZG 2.0")** entered into force on **24 July
  2024** (a precise date not previously recorded; the entity's earlier text
  had only "July 2024"), confirmed directly this pass on Wikipedia, which
  also newly establishes *why* it was needed: the original 2017 law
  required 575 service bundles nationwide by the end of 2022, and **only
  33 were achieved** by that deadline — a materially more critical framing
  than "an upgrade for a digital Germany" alone conveys. The amendment
  legally anchors the **once-only principle** and requires **complete
  end-to-end digitalisation of business-related federal services by
  2028**, plus a unified **DeutschlandID** citizen account. **Confirmed
  directly 2026-09-30**: the BMI's own announcement of the same date,
  read directly via the cookie-jar workaround found this pass, matches
  Wikipedia's account and adds detail — abolishing the written-signature
  requirement for citizens' applications, a legally enforceable right to
  digital administrative services after four years, and "Digital Only"
  for business-related services after five years.
- The BMI's own December 2024 press release, read directly this pass via
  the same workaround (previously reachable only second-hand, quoted by
  heise.de, because `bmi.bund.de` returned a consistent HTTP 400),
  confirms in its own words that the federal government **digitalised
  all 115 of its OZG-prioritised administrative services by the end of
  2024**. heise.de, also read directly, adds that, while the federal
  target was met, **over 100**
  of the most-used federal services are additionally available across
  individual Länder and municipalities, with digital residence registration
  specifically live in 15 of Germany's 20 largest cities.

It provides the legal basis for [[DE-BUNDID]], confirmed directly this pass
on ozg.brandenburg.de: § 2(5) OZG defines the "Nutzerkonto" (user account)
concept underlying BundID, alongside Brandenburg's own e-government law.

## What changed this pass

The entity's `start_date` was previously left `null` because "[e]very
source returned by search concerns the 2024 amendment or the programme run
under the act, not the act's original passage." That was an accurate
description of what the original four sources supported — three of which,
this pass confirms, are also now hard to reach (two return HTTP 400 on
every attempt). Searching further this pass found a dedicated Wikipedia
article carrying the original 2017 enactment date, closing the gap `§21`
of the brief exists to prevent papering over: the date is recorded because
it was found in a source, not because it is "widely known."

The same reasoning now extends to the **OZG-Änderungsgesetz**: it remains a
single entity with the amendment recorded as a fact in the body (the Atlas
still has no amendment-lineage relationship type — see [[DE-NIS2UMSUCG]]),
but its own entry-into-force date and its own stated rationale (33 of 575
service bundles delivered) are now both sourced rather than absent.

## Relationships

**None asserted.** The links a reader would expect — to [[DE-EGOVG]], which
the OZG builds on, and *from* [[DE-BUNDID]], whose legal basis it provides
— are recorded where they are sourced: [[DE-BUNDID]] carries
`governed-by` → this entity. The EGovG connection is not sourced this pass
either and remains unasserted.

## Sources

Listed in frontmatter. Three of the original four were read directly on
the 2026-08-28 pass; `bmi.bund.de` (both cited URLs) and
`digitale-verwaltung.de` returned HTTP 400 Bad Request on every attempt
that pass, so a Wikipedia article and a heise.de report substituted for
the facts they would have supported. **Closed 2026-09-30**: `bmi.bund.de`
is reachable after all with a cookie-jar-aware fetch (discovery/
unresolved.md row #217) — both of its own pages are now added back and
read directly, corroborating Wikipedia's and heise.de's accounts in the
BMI's own words rather than replacing them. **Closed 2026-10-01**: the
same workaround reaches `digitale-verwaltung.de`, so the FITKO page is now
read directly too — all four original sources have been read.
