---
id: NO-PST
type: organisation
name: Politiets sikkerhetstjeneste
alternative_names:
  - PST
  - Norwegian Police Security Service
description: >
  Norway's domestic security and counter-intelligence service, directly
  subordinate to the Ministry of Justice and Public Security. It
  monitors and analyses domestic threats to national security interests,
  prevents and investigates threats to the realm's security, develops
  threat assessments, and protects government officials. Its tasks,
  organisation and use of preventive coercive measures are regulated in
  Chapter III A (§§ 17a–17f) of the Police Act, rather than a dedicated
  statute of its own. Together with the Etterretningstjenesten and the
  Nasjonal sikkerhetsmyndighet it forms Norway's three intelligence,
  surveillance and security services.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - "NO"
  - NO-NSM
  - NO-ETTERRETNINGSTJENESTEN
relationships:
  - type: part-of
    target: "NO"
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #112). Anchor edge under metadata/relationship-types.md §2.3, since no Ministry of Justice and Public Security entity is yet modelled to anchor to instead. Confirmed by reading pst.no's own page directly (2026-09-13): PST is 'directly subordinate to the Ministry of Justice and Preparedness' for oversight and governance."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Om PST"
    url: "https://www.pst.no/om-pst/"
    publisher: "Politiets sikkerhetstjeneste (PST)"
    accessed: "2026-09-13"
  - title: "Legal framework — EOS Committee"
    url: "https://eos-utvalget.no/en/home/about-the-eos-committee/legal-framework/"
    publisher: "EOS-utvalget (Norwegian Parliamentary Intelligence Oversight Committee)"
    accessed: "2026-09-13"
---

# Politiets sikkerhetstjeneste (PST)

> **Created 2026-09-13**, closing `discovery/unresolved.md` row #112 in
> full — the second of Norway's two previously-unmodelled security
> services, alongside [[NO-ETTERRETNINGSTJENESTEN]]. PST's own site and
> the EOS Committee's own legal-framework page were read directly.

## Description

Confirmed by reading `pst.no`'s own page directly: PST "is both an
intelligence, security and police service" whose mission is to
"understand, communicate and counter the most serious threats to
security in the realm." Its five core areas: monitoring and analysing
domestic threats to national security interests; preventing and
investigating threats to the realm's security; developing threat
assessments; communicating the threat picture to decision-makers and the
public; and protecting government officials.

PST is **directly subordinate to the Ministry of Justice and Public
Security** — confirmed on the same page.

## A chapter, not a dedicated statute

Confirmed by reading `pst.no` and `eos-utvalget.no` directly: unlike
[[NO-ETTERRETNINGSTJENESTEN]] (governed by its own 2020 Act) and
[[NO-NSM]] (governed by the 2018 Security Act), PST's "tasks,
organization and use of coercive measures in preventive work are
regulated in the Police Act chapter III A (§ 17a to 17f)" — a chapter of
the general Police Act (Politiloven) that governs the whole police
force, not a statute dedicated to PST itself. `eos-utvalget.no`
additionally names the Criminal Procedure Act (governing PST
investigations) and the Personal Data Act (2010, with 2013 regulations)
as further governing PST's data handling.

No separate `NO-POLITILOVEN` entity is created for the general Police
Act: creating one to carry a single chapter would overstate what PST
itself rests on, matching the threshold already applied elsewhere in the
Atlas to provisions embedded in general statutes (e.g. the Dutch AWR's
Chapter IVA). The relationship is recorded in prose rather than as a
`governed-by` edge.

## One of Norway's three security services

Confirmed on [[NO-NSM]]'s own file, sourced from `nsm.no` directly: NSM
states that it forms, together with **Etterretningstjenesten** and
**PST**, "Norges tre etterretnings- overvåkings- og sikkerhetstjenester"
(Norway's three intelligence, surveillance and security services). All
three are now Atlas entities.

## Relationships

- `part-of` [[NO]] — anchor edge; no Ministry of Justice and Public
  Security entity is yet modelled to anchor to instead.

## Not modelled

- The general **Police Act (Politiloven)**, of which Chapter III A
  governs PST — named in prose above, not created as a separate entity.
- The **Criminal Procedure Act** and **Personal Data Act (2010)**, both
  named by the EOS Committee as further governing PST's work.

## Sources

Listed in frontmatter, both read directly 2026-09-13.
