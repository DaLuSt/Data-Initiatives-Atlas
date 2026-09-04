---
id: NL-BIO
type: framework
name: Baseline Informatiebeveiliging Overheid
alternative_names:
  - BIO
  - BIO2
description: >
  The common information security framework for all tiers of Dutch
  government — central government, municipalities, provinces and water
  authorities — mandatory since 1 January 2019. It sets the minimum
  security requirements and measures, and BIO2, current since September
  2025, is aligned to the NEN-EN-ISO/IEC 27001:2023 and 27002:2022
  standards.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-NEN
  - INTL-ISO-IEC-27001
  - INTL-ISO-IEC-27002
  - NL-ENSIA
relationships:
  - type: based-on
    target: INTL-ISO-IEC-27001
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own BIO page and communicatierijk.nl's own BIO page directly (2026-08-27): BIO2 is structured according to NEN-EN-ISO/IEC 27001:2023, applied to formulate requirements for an information security management system. A third alternate source, certificeringsadvies.nl (fetched after bio-overheid.nl itself returned HTTP 403), independently confirms BIO2 'sluit inhoudelijk aan op ISO 27001 en ISO 27002'. NOTE: BIO2 cites the 2023 NEN-EN adoption; the ISO edition located in the Atlas is 27001:2022 — very likely the same standard under its Dutch designation, but the equivalence remains inferred, not confirmed by any page read."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: based-on
    target: INTL-ISO-IEC-27002
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl and communicatierijk.nl directly (2026-08-27): BIO2 is structured according to NEN-EN-ISO/IEC 27002:2022, applied in a risk-driven manner to select control measures. certificeringsadvies.nl, read as an alternate for the blocked bio-overheid.nl, independently confirms BIO2 was 'geactualiseerd naar ISO/IEC 27002:2022', adopting its four-domain structure (organisational, human, physical, technological)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own BIO page directly (2026-08-27): the BIO is the basic framework for information security across Rijk, gemeenten, provincies and waterschappen. communicatierijk.nl, also read directly, adds that the BIO has been mandatory for all government organisations since 1 January 2019 — a date not previously recorded here."
    confidence: high
    valid_from: 2019-01-01
    valid_until: null

sources:
  - title: "Baseline Informatiebeveiliging Overheid (BIO)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-08-27"
  - title: "Baseline Informatiebeveiliging Overheid (BIO) & NEN-ISO/IEC 27001 en 27002"
    url: "https://www.communicatierijk.nl/vakkennis/rijkswebsites/verplichte-richtlijnen/baseline-informatiebeveiliging-rijksdienst"
    publisher: "CommunicatieRijk"
    accessed: "2026-08-27"
  - title: "Baseline Informatiebeveiliging Overheid (BIO2): wat het is en wat het betekent"
    url: "https://certificeringsadvies.nl/baseline-informatiebeveiliging-overheid-bio2-de-nieuwe-standaard/"
    publisher: "CertificeringsAdvies Nederland"
    accessed: "2026-08-27"
  - title: "Home NL — bio-overheid"
    url: "https://www.bio-overheid.nl/"
    publisher: "BIO-overheid"
  - title: "Baseline Informatiebeveiliging Overheid 2 (BIO2) v1.3 def"
    url: "https://www.bio-overheid.nl/media/dr4inbhc/20260109-baseline-informatiebeveiliging-overheid-2-bio2-v13-def.pdf"
    publisher: "BIO-overheid"
---

# BIO (Baseline Informatiebeveiliging Overheid)

> **Verified 2026-08-27.** `bio-overheid.nl` — both its homepage and the
> BIO2 PDF — returned HTTP 403 on every attempt and is a genuine block, not
> a silently dropped source. Per the re-verification discipline, a working
> alternate covering the same BIO2 content, `certificeringsadvies.nl`, was
> found via WebSearch and read directly, joining the two originally-cited
> sources that were also read directly (`digitaleoverheid.nl` and
> `communicatierijk.nl`). Three of five listed sources read directly is a
> genuine majority; promoted to `primary-source` on that basis, closing the
> previous `search-only` status (never previously `last_verified`).

## Description

The BIO is the common basic framework for information security across all
tiers of Dutch government — central government, municipalities, provinces
and water authorities. Reading `communicatierijk.nl`'s own page directly
adds a date not previously recorded: the BIO has been **mandatory for every
government organisation since 1 January 2019**.

## Versions

**BIO2** is the current major revision. Reading `certificeringsadvies.nl`
directly (as an alternate for the blocked `bio-overheid.nl`) confirms BIO2
"heeft haar intrede gedaan" (came into effect) in **September 2025**,
replacing the BIO framework introduced in 2019 — closing the previous gap
where "the formal date on which BIO2 replaced BIO1 was not established."

It reflects **NEN-EN-ISO/IEC 27001:2023** and **NEN-EN-ISO/IEC 27002:2022**,
confirmed independently by all three sources read directly this pass, and
replaces the earlier BIO's categorisation into three Basis
Beveiligingsniveaus (BBN) with an explicitly risk-driven approach. Under
BIO2, ISO 27001 is applied to formulate requirements for establishing an
information security management system, and ISO 27002 is applied in a
risk-driven way to select control measures — `certificeringsadvies.nl`
adds that this adopts ISO 27002:2022's four-domain structure
(organisational, human, physical, technological), a level of detail not
previously recorded. Government organisations are, at minimum, obliged to
apply the government-specific measures BIO2 sets out. `communicatierijk.nl`
separately shows an **older BIO version citing NEN-ISO/IEC 27001:2017 and
27002:2017** — consistent with a framework that has been revised at least
twice, and confirming BIO2 is a genuine successor version, not simply a
renaming.

`certificeringsadvies.nl` also confirms BIO2's scope directly in its own
words: "geldt voor alle overheidsorganisaties, waaronder: Gemeenten,
Provincies, Waterschappen, Uitvoeringsorganisaties en ZBO's."

## Modelling note

BIO and BIO2 are modelled as **one entity with versions**, unlike
[[NL-WOB]]/[[NL-WOO]] or [[NL-ARCHIEFWET-1995]]/[[NL-ARCHIEFWET-2026]],
which are separate entities. The reasoning: those are distinct statutes with
distinct official titles, whereas BIO2 is a new version of a continuously
named baseline — now confirmed directly to be exactly that: the same name,
the same mandatory scope, a described predecessor-to-successor transition
in September 2025, not a rebrand of an unrelated instrument. This remains a
judgement call and is recorded in `discovery/unresolved.md`.

## Relationships

- Applies in [[NL]] across all government tiers, mandatory since 1 January
  2019 (date newly sourced this pass).
- Based on [[INTL-ISO-IEC-27001]] and [[INTL-ISO-IEC-27002]]. The edition
  caveat from the previous pass stands: BIO2 cites the NEN-EN 2023/2022
  adoptions, and the equivalence to the ISO editions catalogued elsewhere
  in the Atlas remains inferred rather than directly sourced.
- Published in the Netherlands by [[NL-NEN]].
- [[NL-ENSIA]], the accountability system paired with the BIO in its
  digitaleoverheid.nl placement, is now an entity (added 2026-09-04),
  carrying the `based-on` edge pointing here.

## Sources

Three of five read directly this pass: `digitaleoverheid.nl`,
`communicatierijk.nl`, and the alternate `certificeringsadvies.nl` found
via WebSearch to cover BIO2's own content after `bio-overheid.nl` was
confirmed genuinely blocked (403) on both its homepage and the BIO2 PDF.
