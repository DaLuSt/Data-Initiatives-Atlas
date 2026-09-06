---
id: NL-HDAB-NL
type: programme
name: Programma Health Data Access Body Nederland (HDAB-NL)
alternative_names:
  - HDAB-NL
description: >
  Dutch government programme preparing the technical infrastructure for
  the country's future Health Data Access Body (HDAB) under the European
  Health Data Space Regulation. Led by the Ministry of Health, Welfare
  and Sport (VWS) together with RIVM, CBS, ICTU and Health-RI, it
  develops four technical business functions — a national dataset
  catalogue, a Data Access Applications Management Solution, a secure
  processing environment, and a national contact point for secondary use
  connected to HealthData@EU — for handover to the future HDAB
  organisation once established.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-HEALTH
  - DOMAIN-GOVERNMENT
organisations:
  - NL-RIVM
  - NL-CBS
  - NL-ICTU
related_entities:
  - NL
  - NL-HEALTH-RI
  - EU-EHDS
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED HIGH-VALUE GAP (discovery/unresolved.md: 'will Health-RI be the Dutch health data access body?'). Confirmed by reading the Minister of Health, Welfare and Sport's own letter to the Tweede Kamer directly (Kamerstuk 27 529, nr. 356, 20 January 2026, dossier PDF read directly): 'Het Ministerie van Volksgezondheid, Welzijn en Sport (VWS) heeft hiervoor het programma HDAB-NL opgezet... Het programma HDAB-NL is in november 2023 van start gegaan voor een periode van vier jaar. Het Ministerie van VWS werkt in het programma samen met RIVM, CBS, ICTU en Health-RI' (the Ministry of VWS set up the HDAB-NL programme for this purpose... the programme started in November 2023 for a four-year period. The Ministry of VWS works in the programme together with RIVM, CBS, ICTU and Health-RI). The same letter states the four technical business functions (dataset catalogue, DAAMS, secure processing environment, NCPSD) and that 'na het aflopen van het programma HDAB-NL, de ontwikkelde technisch bedrijfsfuncties worden overgedragen aan de toekomstige organisatie HDAB' (after the HDAB-NL programme ends, the developed technical business functions will be transferred to the future HDAB organisation). Anchor edge under metadata/relationship-types.md §2.3."
    confidence: high
    valid_from: 2023-11-01
    valid_until: null
  - type: implements-requirement-from
    target: EU-EHDS
    source: fact
    evidence: "The same ministerial letter states the programme exists specifically to prepare the Netherlands' compliance with the EHDS's Health Data Access Body requirement, and that its technical components will transfer to the future HDAB. Recorded at the programme level rather than asserting the future HDAB organisation itself exists yet — the letter states the Minister 'ben ik voornemens om een nieuw zelfstandig bestuursorgaan (zbo) op te richten' (I intend to establish a new independent administrative body), not yet created."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Kamerbrief over de implementatie van de EHDS (Kamerstuk 27 529, nr. 356)"
    url: "https://www.tweedekamer.nl/downloads/document?id=2026D02216"
    publisher: "Ministerie van Volksgezondheid, Welzijn en Sport (VWS) / Tweede Kamer der Staten-Generaal"
    accessed: "2026-09-06"
---

# Programma Health Data Access Body Nederland (HDAB-NL)

> **Added 2026-09-06.** `discovery/unresolved.md` had flagged, since the
> EHDS's own creation, "will Health-RI be the Dutch health data access
> body?" as one of the highest-value open questions in the Atlas. A
> Minister's own letter to the Tweede Kamer (20 January 2026), read
> directly, answers it — not with a yes, but with the actual, more
> specific arrangement: a preparatory technical programme with five
> named partners, and a still-to-be-created independent body as the
> eventual HDAB itself.

## Description

Confirmed by reading the Minister of Health, Welfare and Sport's own
letter to the Tweede Kamer directly (Kamerstuk 27 529, nr. 356, 20
January 2026): the Ministry of VWS "heeft hiervoor het programma
HDAB-NL opgezet, dat zich richt op de ontwikkeling van de noodzakelijke
technische vereisten" (has set up the HDAB-NL programme for this
purpose, which focuses on developing the necessary technical
requirements) to prepare the Netherlands' future Health Data Access
Body under the [[EU-EHDS]] Regulation.

The programme started in **November 2023** for a **four-year period**,
with VWS working alongside **RIVM, CBS, ICTU and [[NL-HEALTH-RI]]** —
named in the letter's own words as "partijen die reeds een belangrijke
rol spelen in het kader van secundair gebruik van elektronische
gezondheidsgegevens" (parties that already play an important role in
the secondary use of electronic health data).

It develops four technical business functions, confirmed directly from
the letter:

1. A national dataset catalogue (making visible which data categories
   exist for secondary use).
2. A Data Access Applications Management Solution (DAAMS) — the system
   for requesting health data for secondary use.
3. A secure processing environment for anonymised/pseudonymised data.
4. A national contact point for secondary use (NCPSD), a digital
   gateway connected to the EU's HealthData@EU infrastructure.

## The answer to "will Health-RI be the HDAB": not quite

The Minister's letter states directly that the government intends to
create a **new independent administrative body (zelfstandig
bestuursorgaan, zbo)** as the actual HDAB: "ben ik voornemens om een
nieuw zelfstandig bestuursorgaan (zbo) op te richten." Health-RI is not
designated as the HDAB itself — it is one of four partners preparing the
HDAB's future technical infrastructure, which will be **handed over**
to the new zbo once established: "na het aflopen van het programma
HDAB-NL, de ontwikkelde technisch bedrijfsfuncties worden overgedragen
aan de toekomstige organisatie HDAB."

This narrows, rather than fully answers, the open question: the letter
does not name a target date for the zbo's creation beyond the EHDS's own
2029 deadline for HDAB operability, and the zbo itself is not yet an
Atlas entity (nothing to model — it does not yet exist).

## Relationships

- `applies-in` [[NL]] — anchor edge.
- `implements-requirement-from` [[EU-EHDS]], `confidence: medium` — the
  programme's purpose is EHDS compliance preparation.

`organisations` also carries [[NL-RIVM]], [[NL-CBS]] and [[NL-ICTU]] as
programme partners alongside [[NL-HEALTH-RI]], which carries its own
`participates-in` edge to this entity.

## Sources

Listed in frontmatter, read directly this pass.
