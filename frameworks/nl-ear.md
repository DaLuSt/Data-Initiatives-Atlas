---
id: NL-EAR
type: framework
name: Enterprise Architectuur Rijksdienst
alternative_names:
  - EAR
description: >
  Enterprise architecture for the Dutch central government, formally
  established 10 June 2014 (replacing an earlier architecture, MARIJ),
  addressing the organisation of information provision for the Concern
  Rijksdienst. Replaced in 2024 by the RijksOverheid Referentie
  Architectuur (RORA).

level: national
country: NL
region: null

status: superseded
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: NL-RORA

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-NORA
  - NL-RORA
relationships:
  - type: based-on
    target: NL-NORA
    source: fact
    evidence: "Confirmed by reading noraonline.nl's own 'NORA_dochters' page directly (2026-08-27): NORA's daughter architectures ('NORA dochters') include EAR for central government, GEMMA for municipalities, PETRA for the provinces and WILMA for the water boards, alongside domain and chain architectures such as ROSA for education. The same page marks EAR's status as 'Vervangen' (replaced) and names RORA as its replacement. This closes the previous 'NOT READ — search-only' gap."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "The EAR (EnterpriseArchitectuur Rijksdienst) — NORA Online"
    url: "https://www.noraonline.nl/wiki/EAR_(EnterpriseArchitectuur_Rijksdienst)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
  - title: "Status en beheer EAR — RORA Online"
    url: "https://www.roraonline.nl/index.php/Status_en_beheer_EAR"
    publisher: "RORA Online"
    accessed: "2026-08-27"
  - title: "NORA dochters — NORA Online"
    url: "https://www.noraonline.nl/wiki/NORA_dochters"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
---

# EAR (Enterprise Architectuur Rijksdienst)

> **Verified 2026-08-27 — sources replaced, not just re-checked.** This
> entity's original two cited pages, both on `earonline.nl`, are now
> **genuinely dead**: the domain fails to resolve entirely (DNS
> `ENOTFOUND`), not merely blocked. Per the re-verification discipline,
> WebSearch was used to find working alternate sources covering the same
> facts, all on the related `roraonline.nl` and `noraonline.nl` domains
> (which host the same EAR knowledge base under new custodianship), and all
> three were read directly. `earonline.nl` has been dropped from the
> frontmatter `sources` list and replaced.

## Description

The EAR addressed the organisation of information provision within the
Dutch central government, describing both the existing situation and the
intended future arrangement of information provision for the Concern
Rijksdienst. It sat alongside [[NL-GEMMA]] (municipalities) and
[[NL-PETRA]] (provinces) as the central-government member of the Dutch
reference-architecture family.

**Formal establishment, now sourced precisely.** Reading
`roraonline.nl`'s own "Status en beheer EAR" page directly (a page that
itself discusses EAR's founding, despite being hosted on what is now the
successor's site) gives an exact sequence: the Interdepartementale
Commissie Chief Information Officers (ICCIO) approved the EAR on **5 June
2014**, and the Interdepartementale Commissie Bedrijfsvoering Rijksdienst
(ICBR) formally established it five days later, on **10 June 2014** — "
daarmee is de EAR formeel vastgesteld." The same page states the EAR
itself **replaced an earlier architecture, MARIJ** ("De EAR vervangt
daarmee de MARIJ") — a predecessor not previously recorded here and not
itself modelled.

**Succession by RORA, now confirmed directly rather than inferred from
site branding.** `noraonline.nl`'s own EAR wiki page states without
qualification: "The EAR is in 2024 replaced by the RORA," and marks the
EAR's status as **"Uitgefaseerd"** (phased out). The `NORA_dochters` page
independently corroborates: it lists EAR's status as "Vervangen" and RORA
as the current central-government member of the NORA family in its place.
`start_date` for the succession is left `null` on the [[NL-RORA]] side —
no source read gives a month or day within 2024, only the year, so the
previous "1 January 2024" placeholder there is corrected to `null`.

The previously-recorded ambiguity about `earonline.nl` still being live
while `roraonline.nl` calls itself "the knowledge base of the Enterprise
Architectuur Rijksdienst" is now resolved in the domain's favour of
`roraonline.nl`: `earonline.nl` no longer resolves at all, and
`roraonline.nl` demonstrably hosts current EAR/RORA content, including the
EAR's own establishment history.

## Relationships

- Superseded by [[NL-RORA]] (recorded on that entity) — confirmed directly,
  in 2024.
- `based-on` [[NL-NORA]] — now `source: fact`, confirmed via NORA's own
  "dochters" (daughters) wiki page naming EAR explicitly.

## Sources

All three read directly this pass, replacing the two dead `earonline.nl`
URLs this entity previously cited.
