---
id: CH-BACS
type: organisation
name: Bundesamt für Cybersicherheit
alternative_names:
  - BACS
  - OFCS
  - UFCS
description: >
  Switzerland's federal office for cybersecurity and the country's
  competence centre for cyber matters, serving as first point of contact for
  businesses, the administration, educational institutions and the public.
  Since 1 April 2025 it enforces a statutory obligation on critical
  infrastructure operators to report cyber attacks within 24 hours of
  discovery.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - CH
relationships:
  - type: part-of
    target: CH
    source: fact
    evidence: "Confirmed verbatim by reading ncsc.admin.ch directly (2026-08-22): 'Das Bundesamt für Cybersicherheit (BACS) ist das Kompetenzzentrum des Bundes für Cybersicherheit und damit erste Anlaufstelle...' Independently confirmed on de.wikipedia.org's Bundesamt für Cybersicherheit article. staatskalender.admin.ch was fetched (200) but renders client-side in JavaScript and could not be read. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Bundesamt für Cybersicherheit (BACS)"
    url: "https://www.staatskalender.admin.ch/organization/20052606"
    publisher: "Staatskalender, Schweizerische Eidgenossenschaft"
    accessed: "2026-08-22"
  - title: "Bundesamt für Cybersicherheit"
    url: "https://de.wikipedia.org/wiki/Bundesamt_f%C3%BCr_Cybersicherheit"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "Bundesamt für Cybersicherheit BACS"
    url: "https://www.ncsc.admin.ch/"
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    accessed: "2026-08-22"
  - title: "Neue Pflicht zur Meldung von Cyberangriffen für Betreiber kritischer Infrastrukturen"
    url: "https://www.bratschi.ch/en/publikationen/neue-pflicht-zur-meldung-von-cyberangriffen-fuer-betreiber-kritischer-infrastrukturen"
    publisher: "Bratschi AG"
    accessed: "2026-09-05"
---

# Bundesamt für Cybersicherheit (BACS)

> **Verified 2026-08-22.** ncsc.admin.ch and de.wikipedia.org's Bundesamt
> für Cybersicherheit article were read directly and confirm the claims
> below, verbatim in places. staatskalender.admin.ch was fetched but is
> JS-rendered and unreadable via this pass's tooling — a limitation, not
> a sourcing failure. The unattested alternative names "NCSC Switzerland"
> and "Federal Office for Cybersecurity" have been removed and replaced
> with "UFCS," the Italian abbreviation confirmed on Wikipedia's infobox
> alongside the already-listed OFCS. A finding worth flagging: BACS's own
> **English**-language site still brands itself "National Cyber Security
> Centre (NCSC)" — the German rename to BACS has not been carried across
> to the English pages.

## Description

Confirmed verbatim by reading ncsc.admin.ch (2026-08-22): "Das Bundesamt
für Cybersicherheit (BACS) ist das Kompetenzzentrum des Bundes für
Cybersicherheit und damit erste Anlaufstelle" for business, administration,
education and the public. BACS is Switzerland's federal office for
cybersecurity and its national
competence centre for cyber matters. It was previously the National
Cyber Security Centre (NCSC), and still publishes at `ncsc.admin.ch` —
including its English-language pages, which have not adopted the BACS
name at all.

## A 24-hour reporting duty, arrived at without NIS2

Confirmed by reading de.wikipedia.org directly (2026-08-22): "Am 7. März
2025 hat der Bundesrat die gesetzlich verankerte Meldepflicht für
Cyberangriffe auf kritische Infrastrukturen per 1. April 2025 in Kraft
[gesetzt]." Since **1 April 2025** (decided by the Federal Council on 7
March 2025), BACS enforces a legally anchored obligation on
operators of critical infrastructure to report cyber attacks **within 24
hours of discovery**.

That is the same headline duty [[EU-NIS2]] imposes in the Union, on
essentially the same timetable — and Switzerland is not bound by NIS2 and
has not transposed it. Six Atlas countries reach a 24-hour reporting regime
through a Directive; Switzerland legislated to the same effect on its own.

**No relationship to [[EU-NIS2]] is asserted.** The parallel is real and the
mechanism is not: no source read says the Swiss duty derives from, aligns
with, or responds to NIS2, and the resemblance of two obligations is not
evidence that one produced the other. This is the same restraint
[[CH-REVDSG]] required in the opposite direction — there the sources *do*
state the EU-facing motive, so `aligned-with` was assertable; here they do
not, so nothing is.

## The statutory basis, named 2026-09-05

Confirmed via an independent legal publication (Bratschi AG, read
directly): the reporting duty rests on **Article 74a of the
Informationssicherheitsgesetz (ISG)**, defining which entities must
report, with the operational detail (the 24-hour and 14-day deadlines,
enforcement fines up to CHF 100,000) set out in the accompanying
**Cybersecurity Ordinance (CSV)**. Both entered into force on the same
1 April 2025 date already recorded here.

The ISG itself is still **not an Atlas entity** — it was not researched
beyond this single question — so BACS still carries no `governed-by`
edge, like [[NO-NSM]] and for the same reason: the citation is now
precise, but nothing exists in the graph to point the edge at.

## Not modelled

- **NCSC/BACS's relationship to [[CH-DVS]]** and to the federal
  administration's ICT governance.
- The **cantonal** cyber-security bodies.

## Sources

Listed in frontmatter. ncsc.admin.ch and de.wikipedia.org were read
directly in the 2026-08-22 pass; staatskalender.admin.ch was retrieved
but not readable (JS-rendered). Bratschi AG's legal publication, added
and read directly 2026-09-05, names the ISG Article 74a statutory basis.
