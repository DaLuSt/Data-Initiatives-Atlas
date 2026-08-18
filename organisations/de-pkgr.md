---
id: DE-PKGR
type: organisation
name: Parlamentarisches Kontrollgremium
alternative_names:
  - PKGr
  - Parliamentary Control Panel
description: >
  Committee of the German Bundestag responsible for the parliamentary
  oversight of the three federal intelligence services — the BND, the BfV
  and the MAD. It operates under the Gesetz über die parlamentarische
  Kontrolle nachrichtendienstlicher Tätigkeit des Bundes (PKGrG).

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - DE-PKGRG
  - DE-BND
  - DE-BFV
  - DE-BAMAD
  - DE-UKR
relationships:
  - type: governed-by
    target: DE-PKGRG
    source: fact
    evidence: "The Gesetz über die parlamentarische Kontrolle nachrichtendienstlicher Tätigkeit des Bundes (PKGrG) is the act governing the Parlamentarisches Kontrollgremium (gesetze-im-internet.de/pkgrg; bundestag.de 'Parlamentarisches Kontrollgremium (PKGr)'; de.wikipedia.org 'Parlamentarisches Kontrollgremium'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BND
    source: fact
    evidence: "The Parlamentarisches Kontrollgremium is responsible for controlling the federal intelligence services and oversees the Bundesnachrichtendienst, the Militärischer Abschirmdienst and the Bundesamt für Verfassungsschutz (bundestag.de 'Parlamentarisches Kontrollgremium (PKGr)'; de.wikipedia.org 'Parlamentarisches Kontrollgremium'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BFV
    source: fact
    evidence: "The Parlamentarisches Kontrollgremium oversees the Bundesnachrichtendienst, the Militärischer Abschirmdienst and the Bundesamt für Verfassungsschutz (bundestag.de 'Parlamentarisches Kontrollgremium (PKGr)'; de.wikipedia.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BAMAD
    source: fact
    evidence: "The Parlamentarisches Kontrollgremium oversees the Bundesnachrichtendienst, the Militärischer Abschirmdienst and the Bundesamt für Verfassungsschutz (bundestag.de 'Parlamentarisches Kontrollgremium (PKGr)'; de.wikipedia.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "PKGrG — Gesetz über die parlamentarische Kontrolle nachrichtendienstlicher Tätigkeit des Bundes"
    url: "https://www.gesetze-im-internet.de/pkgrg/BJNR234610009.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
  - title: "Parlamentarisches Kontrollgremium (PKGr)"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse19/weitere_gremien/parlamentarisches_kontrollgremium"
    publisher: "Deutscher Bundestag"
  - title: "Parlamentarisches Kontrollgremium"
    url: "https://de.wikipedia.org/wiki/Parlamentarisches_Kontrollgremium"
    publisher: "Wikipedia"
---

# Parlamentarisches Kontrollgremium (PKGr)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The PKGr is the Bundestag body that exercises **parliamentary** control over
all three federal intelligence services: [[DE-BND]], [[DE-BFV]] and
[[DE-BAMAD]]. Unlike the German services themselves, it covers the whole
triad with a single mandate under a single act, [[DE-PKGRG]].

## Parliamentary control, not judicial control

Germany runs the two in parallel, and the distinction is the point of having
both:

- The **PKGr** is composed of parliamentarians and controls expenditure,
  administration and general activity. It is political accountability.
- The **[[DE-UKR]]** is an independent, judicial-style body applying legal
  standards to individual measures. It is legality review.

The comparison across the Atlas is clean. The UK runs the same pair —
[[GB-ISC]] for parliamentary control, [[GB-IPCO]] for legality — while the
Netherlands separates by *timing* instead ([[NL-TIB]] before, [[NL-CTIVD]]
after), and Poland's principal body [[PL-KSS]] is parliamentary with no
independent judicial counterpart in this Atlas.

## It can take the government to the Constitutional Court

The sources record a mechanism worth noting: the Federal Constitutional
Court decides disputes between the PKGr and the Federal Government, on the
application of the Federal Government **or of at least two-thirds of the
PKGr's members**. Parliamentary oversight here is not merely advisory; the
committee has standing.

## Not modelled

- The **G10-Kommission**, the body that authorises measures under
  [[DE-G10]]. It is distinct from the PKGr and was not researched.
- The **Vertrauensgremium** and other Bundestag bodies with intelligence
  budget functions.
- The PKGr's **composition and majority rules**, beyond the two-thirds
  figure above.

## Relationships

- `governed-by` [[DE-PKGRG]].
- `applies-to` [[DE-BND]], [[DE-BFV]] and [[DE-BAMAD]].

## Sources

Listed in frontmatter.
