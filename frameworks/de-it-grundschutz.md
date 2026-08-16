---
id: DE-IT-GRUNDSCHUTZ
type: framework
name: IT-Grundschutz
alternative_names:
  - BSI IT-Grundschutz
  - IT-Grundschutz-Kompendium
description: >
  Information security methodology developed by the Bundesamt für
  Sicherheit in der Informationstechnik, set out in the BSI-Standards 200-1
  (ISMS requirements), 200-2 (IT-Grundschutz methodology), 200-3 (risk
  analysis) and 200-4 (business continuity management), together with the
  IT-Grundschutz-Kompendium of over 100 regularly updated building blocks.
  BSI-Standard 200-1 is stated to be fully compatible with ISO/IEC 27001.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - DE-BSI
related_entities:
  - INTL-ISO-IEC-27001
  - NL-BIO
relationships:
  - type: maintained-by
    target: DE-BSI
    source: fact
    evidence: "IT-Grundschutz is the methodology developed by the BSI, set out in the BSI-Standards 200-1 to 200-4 and the IT-Grundschutz-Kompendium (de.wikipedia.org 'BSI-Standard'; bsi.bund.de). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: aligned-with
    target: INTL-ISO-IEC-27001
    source: fact
    evidence: "BSI-Standard 200-1 defines the general requirements for an ISMS and is fully compatible with ISO 27001; the standard-level protection approach (Standard-Absicherung) carries a certification option, and mappings between IT-Grundschutz and ISO 27001 are published (de.wikipedia.org 'BSI-Standard'; legiscope.com; secjur.com). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "BSI-Standard"
    url: "https://de.wikipedia.org/wiki/BSI-Standard"
    publisher: "Wikipedia"
  - title: "BSI IT-Grundschutz: Methodik und Standards 200-2/3/4"
    url: "https://www.legiscope.com/blog/bsi-grundschutz-methodik-leitfaden.html"
    publisher: "Legiscope"
  - title: "ISO 27001 und BSI Grundschutz: Unterschiede und Mapping"
    url: "https://www.secjur.com/blog/iso-27001-bsi-grundschutz"
    publisher: "secjur"
  - title: "IT-Grundschutz-Kompendium — BSI-Standard für Informationssicherheit"
    url: "https://informationssicherheitsbeauftragter-dresden.de/it-grundschutz-kompendium/"
    publisher: "Informationssicherheitsbeauftragter Dresden"
  - title: "BSI-Standard 200-2: IT-Grundschutz-Methodik"
    url: "https://www.ing-ism.de/magazin/bsi-standard-200-2-it-grundschutz-methodik/"
    publisher: "ing-ism.de"
---

# IT-Grundschutz

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

IT-Grundschutz is the information security methodology developed by
[[DE-BSI]]. It systematises information security from structural analysis
through to certification, and is set out across four **BSI-Standards** and
a compendium:

| Standard | Subject |
|---|---|
| **200-1** | General requirements for an ISMS |
| **200-2** | The operative IT-Grundschutz methodology |
| **200-3** | Risk analysis |
| **200-4** | Business continuity management (BCMS) |

The **IT-Grundschutz-Kompendium**, which has applied to the 200-x series
since 2018, comprises **over 100 Bausteine** (building blocks), updated
regularly to track the changing threat landscape.

BSI-Standard 200-1 describes the tasks management must take on, how the
security organisation is to be built, and what documentation duties exist.
BSI-Standard 200-2 sets out three approaches: **Basis-Absicherung** as a
fast entry point, **Kern-Absicherung** for critical assets, and
**Standard-Absicherung** as the recommended full protection with a
certification option.

## The third international→national standards descent

The Atlas had two chains running from an international standard down to a
national one. This is the third, and the first where the national
instrument is a **methodology aligned with** the international standard
rather than a profile derived from it:

```
INTL-DCAT (W3C)  → EU-DCAT-AP → NL-DCAT-AP-NL     (profile chain)
INTL-ISO-IEC-27001/-27002 → NL-BIO                (baseline derived from)
INTL-ISO-IEC-27001        → DE-IT-GRUNDSCHUTZ     (aligned-with)
```

The relationship type differs deliberately. [[NL-BIO]] is a baseline built
on the ISO controls. IT-Grundschutz is a **parallel methodology** that
BSI-Standard 200-1 keeps compatible with [[INTL-ISO-IEC-27001]], with
published mappings between the two and a certification route that runs
through ISO 27001 on the basis of IT-Grundschutz. `aligned-with` is
defined in `metadata/relationship-types.md` as *"two entities are
deliberately kept consistent without one implementing the other"*, which is
exactly this case.

Using `based-on` or `derived-from` here — as would be natural by analogy
with [[NL-BIO]] — would misstate the relationship. Germany did not build a
national profile of ISO 27001; it built its own scheme and keeps it
compatible.

## A comparison the two-country Atlas makes available

[[NL-BIO]] and IT-Grundschutz are the Dutch and German government
information-security baselines. They now sit in the Atlas with a **common
ancestor** ([[INTL-ISO-IEC-27001]]) and **different relationship types to
it** — which is a more informative record than either entity alone, and
was not expressible before a second country existed.

**No relationship between them is asserted.**

## Relationships

- Maintained by [[DE-BSI]].
- `aligned-with` [[INTL-ISO-IEC-27001]].

## Sources

Listed in frontmatter. **No bsi.bund.de IT-Grundschutz page is cited** —
the searches returned Wikipedia and consultancy explainers rather than the
BSI's own IT-Grundschutz pages. For a framework published by a federal
authority that is a poor sourcing position, and it caps confidence at
medium despite the subject being well documented in reality.
