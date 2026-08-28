---
id: DE-IT-GRUNDSCHUTZ
type: framework
name: IT-Grundschutz
alternative_names:
  - BSI IT-Grundschutz
  - IT-Grundschutz-Kompendium
description: >
  Information security methodology developed and maintained by the
  Bundesamt für Sicherheit in der Informationstechnik, set out in the
  BSI-Standards 200-1 (ISMS requirements), 200-2 (IT-Grundschutz
  methodology: Basis-, Kern- and Standard-Absicherung), 200-3 (risk
  analysis) and 200-4 (business continuity management), together with the
  IT-Grundschutz-Kompendium of roughly 100 regularly updated building
  blocks across ten layers. BSI-Standard 200-1 is confirmed by the BSI's
  own site to be compatible with ISO/IEC 27001, and organisations can
  achieve ISO 27001 certification on the basis of IT-Grundschutz.

level: national
country: DE
region: null

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
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
    evidence: "Confirmed by reading bsi.bund.de's own two pages directly (2026-08-28): 'BSI-Standards' (bsi.bund.de/DE/.../bsi-standards_node.html) and the English 'IT-Grundschutz' page (bsi.bund.de/EN/.../it-grundschutz_node.html) both state the BSI developed and maintains IT-Grundschutz and the BSI-Standards 200-1 to 200-4. This closes the previously-flagged gap of no bsi.bund.de citation on this entity; both pages were located via a targeted search after the entity's original sources (Wikipedia and consultancy explainers) returned no bsi.bund.de URL."
    confidence: high
    valid_from: null
    valid_until: null
  - type: aligned-with
    target: INTL-ISO-IEC-27001
    source: fact
    evidence: "Confirmed by reading bsi.bund.de's own 'BSI-Standards' page directly (2026-08-28): 'BSI-Standard 200-1 ... compatible with the ISO-Standard 27001' and incorporates guidance from ISO 27002. secjur.com, also read directly, quotes the stronger claim that '[d]ie BSI-Standards 200-1 und 200-2 orientieren sich explizit an den Anforderungen der ISO 27001' and states the BSI publishes an official mapping table correlating all 93 ISO 27001:2022 controls to IT-Grundschutz modules. The BSI's own English page confirms organisations can achieve ISO 27001 certification 'based on IT-Grundschutz.' This is now confirmed on the BSI's own site, not only third-party commentary."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "BSI — BSI-Standards"
    url: "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "BSI — IT-Grundschutz"
    url: "https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
    accessed: "2026-08-28"
  - title: "BSI-Standard"
    url: "https://de.wikipedia.org/wiki/BSI-Standard"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "BSI IT-Grundschutz: Methodik und Standards 200-2/3/4"
    url: "https://www.legiscope.com/blog/bsi-grundschutz-methodik-leitfaden.html"
    publisher: "Legiscope"
    accessed: "2026-08-28"
  - title: "ISO 27001 und BSI Grundschutz: Unterschiede und Mapping"
    url: "https://www.secjur.com/blog/iso-27001-bsi-grundschutz"
    publisher: "secjur"
    accessed: "2026-08-28"
  - title: "IT-Grundschutz-Kompendium — BSI-Standard für Informationssicherheit"
    url: "https://informationssicherheitsbeauftragter-dresden.de/it-grundschutz-kompendium/"
    publisher: "Informationssicherheitsbeauftragter Dresden"
    accessed: "2026-08-28"
  - title: "BSI-Standard 200-2: IT-Grundschutz-Methodik"
    url: "https://www.ing-ism.de/magazin/bsi-standard-200-2-it-grundschutz-methodik/"
    publisher: "ing-ism.de"
---

# IT-Grundschutz

> **Re-verified 2026-08-28.** Six of seven cited pages read directly,
> including — closing the previously-flagged weakest point — the BSI's own
> two current pages on the standard, found via targeted search since the
> entity's original source list contained no `bsi.bund.de` URL at all.
> `verification: primary-source`; `confidence` raised to `high` since the
> central claims (BSI authorship, ISO 27001 compatibility) now rest on the
> standard-setter's own site rather than only Wikipedia and consultancies.

## Description

IT-Grundschutz is the information security methodology developed and
maintained by [[DE-BSI]] — confirmed directly this pass on the BSI's own
site. It systematises information security from structural analysis
through to certification, and is set out across four **BSI-Standards** and
a compendium:

| Standard | Subject |
|---|---|
| **200-1** | General requirements for an ISMS, confirmed by the BSI's own page to be compatible with ISO/IEC 27001 |
| **200-2** | The operative IT-Grundschutz methodology: Basis-, Kern- and Standard-Absicherung |
| **200-3** | Risk analysis |
| **200-4** | Business continuity management (BCMS) |

The **IT-Grundschutz-Kompendium**, which has applied to the 200-x series
since 2018, comprises — per informationssicherheitsbeauftragter-dresden.de,
read directly — roughly **100 Bausteine** (building blocks) organised into
**ten layers** (ISMS, ORP, CON, OPS, DER, APP, SYS, NET, INF, IND), updated
annually to track the changing threat landscape.

BSI-Standard 200-1 describes the tasks management must take on, how the
security organisation is to be built, and what documentation duties exist.
BSI-Standard 200-2 sets out three approaches: **Basis-Absicherung** as a
fast entry point, **Kern-Absicherung** for critical assets, and
**Standard-Absicherung** as the recommended full protection with a
certification option — all now confirmed directly on the BSI's own page as
well as in the secondary sources.

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
BSI-Standard 200-1 keeps compatible with [[INTL-ISO-IEC-27001]] — now
confirmed on the BSI's own site rather than only via secjur.com's
commentary — with an official BSI-published mapping table (secjur.com,
read directly, describes it as correlating all 93 ISO 27001:2022 controls
to IT-Grundschutz modules) and a certification route that runs through ISO
27001 on the basis of IT-Grundschutz. `aligned-with` is defined in
`metadata/relationship-types.md` as *"two entities are deliberately kept
consistent without one implementing the other"*, which is exactly this
case.

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

- Maintained by [[DE-BSI]] — confirmed directly this pass, `confidence:
  high`.
- `aligned-with` [[INTL-ISO-IEC-27001]] — confirmed directly this pass,
  `confidence: high`.

## Sources

Listed in frontmatter. Six of seven read directly this pass, including two
`bsi.bund.de` pages found via search — the previously-noted gap ("**No
bsi.bund.de IT-Grundschutz page is cited**") is now closed. `ing-ism.de`
was not re-fetched this pass; it is not needed for the majority.
