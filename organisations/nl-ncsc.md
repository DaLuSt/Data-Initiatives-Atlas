---
id: NL-NCSC
type: organisation
name: Nationaal Cyber Security Centrum
alternative_names:
  - NCSC
  - NCSC-NL
  - Versterkt NCSC
  - Dutch National Cyber Security Centre
description: >
  The Netherlands' national cyber security centre. On 1 January 2026 the
  Digital Trust Center was merged into it, creating a single strengthened
  NCSC that is the point of contact for digital resilience for all Dutch
  organisations — some 2.4 million, from sole traders to multinationals —
  with round-the-clock availability.

level: national
country: NL
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
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - NL-CBW
  - EU-NIS2
relationships:
  - type: applies-to
    target: NL-CBW
    source: interpretation
    evidence: "The strengthened NCSC is the national cyber security centre of the Netherlands and, since 1 January 2026, the single point of contact for digital resilience for all Dutch organisations; the NCSC's own publications present 2026 as the year of the Cyberbeveiligingswet and advise organisations to prepare (ncsc.nl 'Versterkt NCSC', 'DTC en NCSC vanaf 2026 verder als versterkt NCSC' and 'Ook in 2026...'; techzine.nl; binnenlandsbestuur.nl). NOT READ — search-only. Recorded as `interpretation`: the sources establish that the NCSC is the national cyber security body and that it is guiding organisations through the Cyberbeveiligingswet, but none read states that it is the competent authority or CSIRT designated under that act."
    confidence: low
    valid_from: null
    valid_until: null

sources:
  - title: "Versterkt NCSC"
    url: "https://www.ncsc.nl/over-ons/versterkt-ncsc"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
  - title: "DTC en NCSC vanaf 2026 verder als versterkt NCSC"
    url: "https://www.ncsc.nl/nieuws/dtc-en-ncsc-vanaf-2026-verder-als-versterkt-ncsc"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
  - title: "Versterkt NCSC: alle Nederlandse organisaties krijgen één aanspreekpunt voor digitale weerbaarheid"
    url: "https://www.ncsc.nl/nieuws/versterkt-ncsc-alle-nederlandse-organisaties-krijgen-een-aanspreekpunt-voor-digitale-weerbaarheid"
    publisher: "Nationaal Cyber Security Centrum (NCSC)"
  - title: "DTC en NCSC fuseren tot één Nederlandse cybersecurityorganisatie"
    url: "https://www.techzine.nl/nieuws/security/570635/dtc-en-ncsc-fuseren-tot-een-nederlandse-cybersecurityorganisatie/"
    publisher: "Techzine"
---

# Nationaal Cyber Security Centrum (NCSC)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

The NCSC is the Netherlands' national cyber security centre. Since
**1 January 2026** it is the *versterkt NCSC* — the **strengthened** NCSC,
created by merging the **Digital Trust Center** into it.

The merger changed who it serves. The NCSC's remit had been critical
infrastructure and central government; the DTC's was business, particularly
smaller firms. The merged body is the single point of contact for digital
resilience for **all** Dutch organisations — the sources give **2.4 million**
— with 24/7 availability.

## The gap this closes, and the one it does not

`discovery/research-queue.md` has recorded since the **Belgium batch** that
[[NL-CBW]] is a NIS2 act with **no authority attached**, while Belgium had
[[BE-CCB]] and Germany [[DE-BSI]]. That observation was made in 2026-08-15
terms and has been carried in every structural review since.

The Netherlands now has a cyber authority entity. **It does not yet have a
sourced designation.**

## ⚠ Why the edge is `interpretation` at `confidence: low`

Compare how the other countries' authorities connect to their NIS2 acts:

| Country | Authority | Edge to the act |
|---|---|---|
| Belgium | [[BE-CCB]] | `governed-by` **and** `produces` [[BE-NIS2-WET]] |
| France | [[FR-ANSSI]] | `applies-to` [[FR-NIS2-LOI]] |
| Germany | [[DE-BSI]] | `governed-by` [[DE-BSIG]] |
| **Netherlands** | **NCSC** | **`applies-to` [[NL-CBW]] — `interpretation`, `confidence: low`** |

What the sources establish is that the NCSC is the national cyber security
body and that it is guiding organisations through the Cyberbeveiligingswet —
its own 2026 material presents the year in those terms. What **no source read
states** is that the NCSC is the competent authority or the CSIRT *designated
under* that act.

Those are different claims. The Dutch act distributes competent-authority
roles across sectoral regulators, and asserting `governed-by` here would
claim a designation the Atlas has not seen. `source: interpretation` records
that the Atlas, not a source, drew this line.

## Not modelled

- The **Digital Trust Center**, now absorbed. It is the second body in the
  Atlas's orbit to stop existing after [[GB-DSIT]], and unlike DSIT it is not
  modelled at all — so the merger is described here and cannot be shown.
- **CSIRT-DSP** and the sectoral competent authorities under [[NL-CBW]].
- The **NCTV** and the Ministry of Justice and Security, the NCSC's parent.

## Relationships

- `applies-to` [[NL-CBW]] — ⚠ `interpretation`, `confidence: low`.

## Sources

Listed in frontmatter.
