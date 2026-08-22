---
id: DE-PKGR
type: organisation
name: Parlamentarisches Kontrollgremium
alternative_names:
  - PKGr
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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the PKGrG statute text at gesetze-im-internet.de (2026-08-22), which constitutes and governs the Parlamentarisches Kontrollgremium throughout — see e.g. § 14: 'Das Bundesverfassungsgericht entscheidet über Streitigkeiten zwischen dem Parlamentarischen Kontrollgremium und der Bundesregierung.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BND
    source: fact
    evidence: "Confirmed by reading bundestag.de's 'Die Arbeit der Nachrichtendienste' page (2026-08-22): 'Die nachrichtendienstliche Tätigkeit des Bundes unterliegt der Kontrolle des Deutschen Bundestages und seiner Gremien, insbesondere der des Parlamentarischen Kontrollgremiums und des Vertrauensgremiums des Haushaltsausschusses.' This follows the page's earlier statement that the three federal services are the BND, MAD and BfV."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BFV
    source: fact
    evidence: "Confirmed by reading bundestag.de's 'Die Arbeit der Nachrichtendienste' page (2026-08-22): the same 'unterliegt der Kontrolle ... des Parlamentarischen Kontrollgremiums' statement applies to all three named services, including the BfV."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: DE-BAMAD
    source: fact
    evidence: "Confirmed by reading bundestag.de's 'Die Arbeit der Nachrichtendienste' page (2026-08-22): the same 'unterliegt der Kontrolle ... des Parlamentarischen Kontrollgremiums' statement applies to all three named services, including the MAD."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "PKGrG — Gesetz über die parlamentarische Kontrolle nachrichtendienstlicher Tätigkeit des Bundes"
    url: "https://www.gesetze-im-internet.de/pkgrg/BJNR234610009.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    accessed: "2026-08-22"
  - title: "Parlamentarisches Kontrollgremium (PKGr)"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse19/weitere_gremien/parlamentarisches_kontrollgremium"
    publisher: "Deutscher Bundestag"
    accessed: "2026-08-22"
  - title: "Parlamentarisches Kontrollgremium"
    url: "https://de.wikipedia.org/wiki/Parlamentarisches_Kontrollgremium"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# Parlamentarisches Kontrollgremium (PKGr)

> **Verified 2026-08-22.** The PKGrG statute text and
> bundestag.de's "Die Arbeit der Nachrichtendienste" page were read
> directly and confirmed the claims below, including the §14 PKGrG
> Constitutional Court mechanism (see below).

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

Confirmed directly in **§ 14 PKGrG** ("Gerichtliche Zuständigkeit"),
read 2026-08-22: "Das Bundesverfassungsgericht entscheidet über
Streitigkeiten zwischen dem Parlamentarischen Kontrollgremium und der
Bundesregierung auf Antrag der Bundesregierung oder von mindestens zwei
Dritteln der Mitglieder des Parlamentarischen Kontrollgremiums." Parliamentary
oversight here is not merely advisory; the committee has standing to sue.

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
