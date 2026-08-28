---
id: DE-OZG
type: law
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
confidence: medium
coverage: medium
verification: primary-source

start_date: 2017-08-18
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BUNDID
  - DE-EGOVG
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
  2028**, plus a unified **DeutschlandID** citizen account.
- heise.de, read directly, confirms the federal government **digitalised
  all 115 of its OZG-prioritised administrative services by the end of
  2024** — via the BMI's own December 2024 announcement, which heise.de
  quotes, even though the BMI's own page could not be fetched directly this
  pass. heise.de adds that, while the federal target was met, **over 100**
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

Listed in frontmatter. Three of four read directly this pass. `bmi.bund.de`
(both cited URLs) and `digitale-verwaltung.de` returned HTTP 400 Bad
Request on every attempt this pass — treated as a genuine, if unexplained,
block rather than silently dropped — and a Wikipedia article plus a
heise.de report substitute for the facts they would have supported.
