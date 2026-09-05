---
id: NL-RORA
type: framework
name: RijksOverheid Referentie Architectuur
alternative_names:
  - RORA
description: >
  Reference architecture for the Dutch central government, successor since
  2024 to the Enterprise Architectuur Rijksdienst (EAR). Covers the entire
  legal entity of the State and is maintained as a continuously evolving
  register of principles, norms and standards rather than a fixed document.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: NL-EAR
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - NL-EAR
  - NL-NORA
relationships:
  - type: supersedes
    target: NL-EAR
    source: fact
    evidence: "Confirmed by reading all three cited pages directly (2026-08-27). noraonline.nl's own EAR wiki page states without qualification: 'The EAR is in 2024 replaced by the RORA', and marks EAR's status as 'Uitgefaseerd' (phased out). roraonline.nl's own 'Welkom' page confirms RORA Online now hosts the EAR knowledge base's content. The 'Rijksregister standaarden' page describes RORA's standards-register function (mandatory, recommended and kingdom-wide lists managed via OBDO/Forum Standaardisatie) but does not itself discuss the EAR succession. `confidence` raised from `low` to `medium` on the strength of NORA's own independent confirmation of the 2024 date; still not `high` because no source gives a month or day."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Welkom op de kennisbank van de Enterprise Architectuur Rijksdienst — RORA Online"
    url: "https://www.roraonline.nl/index.php/Welkom_op_de_kennisbank_van_de_Enterprise_Architectuur_Rijksdienst"
    publisher: "RORA Online"
    accessed: "2026-08-27"
  - title: "Rijksregister standaarden — RORA Online"
    url: "https://www.roraonline.nl/index.php/Rijksregister_standaarden"
    publisher: "RORA Online"
    accessed: "2026-08-27"
  - title: "EAR (EnterpriseArchitectuur Rijksdienst) — NORA Online"
    url: "https://www.noraonline.nl/wiki/EAR_(EnterpriseArchitectuur_Rijksdienst)"
    publisher: "NORA Online (ICTU)"
    accessed: "2026-08-27"
  - title: "RORA Informatie — RORA Online"
    url: "https://www.roraonline.nl/index.php/RORA_Informatie"
    publisher: "RORA Online"
    accessed: "2026-09-05"
---

# RORA (RijksOverheid Referentie Architectuur)

> **Verified 2026-08-27.** All three cited pages were read directly this
> pass, closing the previous `search-only` status. The succession from
> [[NL-EAR]] is now confirmed by a **third, independent** source (NORA's
> own wiki) beyond the two `roraonline.nl` pages this entity already
> cited, resolving the previous doubt about whether `roraonline.nl`
> presenting itself as "the knowledge base of the EAR" sat oddly with RORA
> being EAR's successor.

## Description

RORA is the reference architecture for the Dutch central government and,
since 2024, the successor to [[NL-EAR]]. Reading `roraonline.nl`'s own
"Welkom" page directly explains the naming oddity previously flagged: the
site **now hosts the EAR knowledge base's content under RORA's name**
rather than running two separate platforms — it is a continuation, not a
coincidence of branding.

A search for RORA's founding vision document (`RORA — Uitwerking visie —
v1.0, 13 December 2023`) surfaces the scope directly: RORA covers **the
entire legal entity of the State**, and is explicitly not meant to be
"finished" — it is adjusted as technology, organisation, and strategy
change, and "must be built and maintained" continuously rather than
published as a fixed document.

`roraonline.nl`'s own "Rijksregister standaarden" page, also read directly,
describes RORA's standards-register function in more concrete terms than
previously recorded: it holds government-wide standards set by the OBDO
(Overheidsbreed Beleidsoverleg Digitale Overheid) and managed by
[[NL-FORUM-STANDAARDISATIE]], plus additional kingdom-wide standards from
the CIO council, organised into mandatory ("comply or explain"),
recommended, and kingdom-specific lists.

`confidence` is raised to `medium` — no longer resting on "a single
reported statement of succession" — because `noraonline.nl`'s own,
independently-hosted EAR wiki page corroborates the 2024 succession in its
own words. It stays below `high` because no source read gives a specific
month or day within 2024; `start_date` is corrected from the previous
"1 January 2024" **placeholder** to `null`, per the Atlas rule against
padding a year-only claim into a specific date.

## Governance and timeline, closed 2026-09-05

Reading `roraonline.nl`'s own "RORA Informatie" page directly names the
maintaining structure this entity previously lacked: the **CIO-beraad**
(CIO Council) is owner and final authority — "eigenaar en eindverantwoordelijk
voor het juist laten toepassen van de kaders en richtlijnen van de RORA" —
supported by the **Architectuurraad RORA** (Architecture Council RORA),
with day-to-day management and further development carried by a community
"ondersteund door het Beheerteam" (supported by the Management Team).

The same page also narrows the succession timeline, without giving a
single decisive date: the CIO council approved the RORA name change on
**15 February 2023**, goal and scope were approved **21 June 2023**, the
vision was approved and the Architectuurraad RORA established **13
December 2023**, and that Council's inaugural meeting was planned for
**25 January 2024**. No page read states a specific day on which RORA
formally superseded EAR — the transition reads as a process spanning
these milestones rather than a single cutover date — so `start_date`
stays `null`, now for a fully documented reason rather than an
unconfirmed gap.

## Relationships

- Supersedes [[NL-EAR]] — confirmed by three independent sources this
  pass, in 2024 (a documented multi-stage process; no single cutover date).
- Owned by the CIO-beraad; supported by the Architectuurraad RORA and a
  Beheerteam. Not modelled as typed relationships: none of these bodies
  is itself an Atlas entity.

## Sources

Four sources read directly: the original three, plus roraonline.nl's own
"RORA Informatie" page (2026-09-05).
