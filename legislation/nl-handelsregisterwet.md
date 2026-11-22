---
id: NL-HANDELSREGISTERWET
type: act
name: Handelsregisterwet 2007
alternative_names:
  - Handelsregisterwet
  - Hrw 2007
description: >
  Dutch act governing the commercial register, the statutory basis of the
  Handelsregister maintained by the Kamer van Koophandel.

level: national
country: NL
region: EU

status: active
rank: ordinary
confidence: medium
coverage: low
verification: primary-source
start_date: 2007-03-22
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-KVK
related_entities:
  - NL-BASISREGISTRATIES
  - NL-KVK
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "Handelsregisterwet 2007 is a Dutch act, published on wetten.overheid.nl under identifier BWBR0021777 (wetten.overheid.nl/BWBR0021777), confirmed 2026-08-21. Anchor edge — added under the rule in metadata/relationship-types.md §2.3 that every entity must reach its scope anchor. It asserts scope and nothing more."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Handelsregisterwet 2007 — BWBR0021777"
    url: "https://wetten.overheid.nl/BWBR0021777"
    publisher: "Overheid.nl (wetten.nl)"
    accessed: "2026-08-21"
  - title: "Handelsregisterwet 2007 — informatie"
    url: "https://wetten.overheid.nl/BWBR0021777/informatie"
    publisher: "Overheid.nl (wetten.nl)"
    accessed: "2026-08-21"
---

# Handelsregisterwet 2007

> **Verified 2026-08-21.** Every cited source was read and confirmed to
> support what this entity says. `verification: primary-source`.
>
> **Closed 2026-09-06**: BRIS and the Company Law Directive, previously
> flagged as unmodelled, are now [[EU-BRIS]] and
> [[EU-COMPANY-LAW-DIRECTIVE]].

## Description

The statutory basis of [[NL-NHR]], the Dutch commercial register. The
statute text opens: *"Wet van 22 maart 2007, houdende regels omtrent een
basisregister van ondernemingen"* — enacted 22 March 2007, which is now
recorded as `start_date`. BWBR0021777 and the official abbreviation `Hrw
2007` are both confirmed on the `wetten.overheid.nl` metadata page.

## The register's European counterpart, closed 2026-09-06

Of the ten Dutch base registrations, the commercial register is the one with
the clearest EU-level analogue: business registers are interconnected across
the Union through the Business Registers Interconnection System, now
[[EU-BRIS]], under the Company Law Directive, now
[[EU-COMPANY-LAW-DIRECTIVE]]. [[NL-NHR]] carries the `applies-to` edge from
[[EU-BRIS]] — see that entity for the sourcing.

## Relationships

- `applies-in` [[NL]] — an anchor edge.

## Who keeps it (2026-11-22)

Article 3(1): "Het handelsregister wordt gehouden door de Kamer", the Kamer van Koophandel ([[NL-KVK]], Article 1), which is also the controller for its processing (Article 3(2)). Read directly on wetten.overheid.nl; recorded as a `governed-by` edge on [[NL-KVK]].

## Sources

Listed in frontmatter.
