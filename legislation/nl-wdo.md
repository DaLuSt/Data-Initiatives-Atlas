---
id: NL-WDO
type: law
name: Wet digitale overheid
alternative_names:
  - Wdo
  - Digital Government Act
description: >
  Dutch digital government act, in force in phases from 1 July 2023. It
  requires public service providers to determine the assurance level
  required for access to each digital service, mandates digital
  accessibility, and gives statutory force to designated open standards.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2023-07-01
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
  - NL-LOGIUS
related_entities:
  - NL-PAS-TOE-OF-LEG-UIT
  - NL-GDI
relationships:
  - type: influences
    target: NL-PAS-TOE-OF-LEG-UIT
    source: fact
    evidence: "Under the Wdo public organisations must use recognised open standards, with the HTTPS standard legally required for publicly accessible government websites and web applications (digitaleoverheid.nl Wdo pages). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-07-01
    valid_until: null

sources:
  - title: "Wet digitale overheid (Wdo)"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/wetgeving/wet-digitale-overheid-wdo/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Wet digitale overheid op 1 juli 2023 van kracht"
    url: "https://www.digitaleoverheid.nl/nieuws/wet-digitale-overheid-op-1-juli-2023-van-kracht/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Veelgestelde vragen over de inwerkingtreding van de Wdo"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/wetgeving/wet-digitale-overheid/veelgestelde-vragen-over-de-inwerkingtreding-van-de-wdo/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
  - title: "Staatsblad 2023, 160"
    url: "https://zoek.officielebekendmakingen.nl/stb-2023-160.html"
    publisher: "Overheid.nl — Officiële bekendmakingen"
---

# Wet digitale overheid (Wdo)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The Wdo gives legal substance to the intention of a digitally functioning
(semi-)government. It entered into force **in phases** from 1 July 2023
rather than all at once; `start_date` records the first phase.

Obligations reported from that date:

- **Assurance levels.** Public service providers must determine, per
  service, which trust/assurance level (betrouwbaarheidsniveau) is required
  for access to their digital services.
- **Accessibility.** Government websites and applications must meet
  statutory digital accessibility requirements, referenced to WCAG 2.1.
- **Open standards.** Public organisations must use recognised open
  standards; HTTPS is named as legally required for publicly accessible
  government websites and web applications.
- **Stelsel Toegang**, the access system enabling service providers to
  connect to all recognised login methods.

The Wdo is the point where the Dutch open-standards regime acquires
statutory teeth: [[NL-PAS-TOE-OF-LEG-UIT]] operates on an
apply-or-explain basis, while the Wdo makes specified standards
outright mandatory. That relationship is recorded as `influences`; whether a
more precise relationship type is warranted is worth revisiting.

The Wdo also connects to the identity and access services within
[[NL-GDI]] operated by [[NL-LOGIUS]], though the specific services covered
have not been established.

## Classification

Dutch national legislation: `region` is `null` rather than `EU`.

**Batch 8 examined this and left it unchanged.** Both [[EU-EIDAS]]
(Regulation 910/2014) and [[EU-EIDAS2]] (Regulation 2024/1183) now exist as
entities, and eIDAS 2.0 can be ruled out on dates — the Wdo came into force
in July 2023, before eIDAS 2.0 entered into force in May 2024. The original
eIDAS Regulation remains the plausible candidate.

But plausible is not sourced. No source read states that the Wdo transposes
910/2014, and the inference "both concern digital identity, therefore one
transposes the other" is precisely what the Atlas's provenance rules
exclude. `region` stays `null` and no relationship is asserted until a
source says otherwise. See `discovery/unresolved.md`.

## Relationships

- Influences [[NL-PAS-TOE-OF-LEG-UIT]] by giving statutory force to
  designated open standards.
- Relates to [[NL-GDI]] and [[NL-LOGIUS]] through the Stelsel Toegang.

## Sources

Listed in frontmatter.
