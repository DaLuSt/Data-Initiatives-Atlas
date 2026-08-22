---
id: INTL-EFTA-COURT
type: organisation
name: EFTA Court
alternative_names: []
description: >
  Supranational judicial body serving Iceland, Liechtenstein and Norway —
  the three EEA EFTA states — and one half of the two-pillar structure
  that lets the Agreement on the European Economic Area be enforced
  without giving EU institutions direct power over non-member states. It
  performs the European Court of Justice's role for the EEA EFTA side:
  ruling on infringement actions the EFTA Surveillance Authority refers
  to it, and on questions of EEA law referred by national courts.
  Established under the Agreement between the EFTA States on the
  Establishment of a Surveillance Authority and a Court of Justice, it
  took up its functions on 1 January 1994 with judges from the EFTA
  states then outside the EU, moved from Geneva to Luxembourg in
  September 1996 after Austria, Finland and Sweden left EFTA for the EU,
  and today sits with three permanent judges, one nominated by each of
  Iceland, Liechtenstein and Norway.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: 1994-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-EEA-AGREEMENT
  - INTL-EFTA
  - INTL-EFTA-SURVEILLANCE-AUTHORITY
  - "NO"
  - IS
  - LI
relationships:
  - type: part-of
    target: INTL-EEA-AGREEMENT
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/EFTA_Court directly (2026-08-22): 'According to Article 108(2) of the EEA Agreement of 2 May 1992, the EFTA States taking part in the EEA Agreement shall establish a court of justice. That obligation was complied with by the conclusion of the \"Surveillance and Court Agreement\" (SCA).' Corroborated by reading efta.int's own 'EEA Institutions - Two Pillar Structure' page directly (fetched with an honest, identifying User-Agent — efta.int returns a bot-defense challenge to a browser User-Agent but real content to one that names itself as a bot): 'In the EFTA pillar, certain EU bodies are mirrored, such as a surveillance authority and a court of justice.' Its jurisdiction is exactly the three EEA EFTA states (Iceland, Liechtenstein, Norway), matching INTL-EEA-AGREEMENT's own party list rather than the four states of [[INTL-EFTA]], so the Agreement is the anchor under metadata/relationship-types.md §2.3."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: related-to
    target: INTL-EFTA
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/European_Free_Trade_Association directly (2026-08-22): 'The EFTA Surveillance Authority and the EFTA Court regulate the activities of the EFTA members in respect of their obligations in the European Economic Area (EEA). Since Switzerland is not an EEA member, it does not participate in these institutions.' Named for and closely tied to EFTA, but its jurisdiction does not match EFTA's own membership, so `related-to` rather than `part-of`."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-EFTA-SURVEILLANCE-AUTHORITY
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/EFTA_Surveillance_Authority directly (2026-08-22): infringement proceedings opened by the Authority are 'a three-step procedure which may result in ESA referring the case to the EFTA Court.' Both bodies were established by the same Surveillance and Court Agreement."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EEA Institutions - Two Pillar Structure"
    url: "https://www.efta.int/eea-relations-eu/eea-institutions-two-pillar-structure"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "EFTA Court"
    url: "https://en.wikipedia.org/wiki/EFTA_Court"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "European Free Trade Association"
    url: "https://en.wikipedia.org/wiki/European_Free_Trade_Association"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "EFTA Court"
    url: "https://www.eftacourt.int/"
    publisher: "EFTA Court"
    accessed: "2026-08-22"
---

# EFTA Court

> **Verified 2026-08-22, and a correction to standing guidance.**
> `efta.int` was treated as bot-walled (403) in every earlier pass this
> session, on the strength of a browser-spoofing User-Agent. Fetched
> instead with an honest, identifying User-Agent, `efta.int` returns real
> content: 200, not 403. It has no dedicated subpage for this Court
> (guessed "about" paths 404), but its "Two Pillar Structure" overview
> page confirms the Court's place in the EFTA pillar directly.
> `eftacourt.int` was re-tested the same way and still serves only a live
> case-docket and hearings-list regardless of the path requested — the
> homepage and `/the-court/` both return an identical list of upcoming
> hearings, not institutional description. Two Wikipedia articles, read
> directly and cross-checked against each other, fill in the detail
> neither official site carries.

## Description

Confirmed by reading en.wikipedia.org/wiki/EFTA_Court directly
(2026-08-22): "The EFTA Court is a supranational judicial body
responsible for the three EFTA members who are also members of the
European Economic Area (EEA): Iceland, Liechtenstein and Norway." It
performs the European Court of Justice's role for the EEA EFTA side of
the two-pillar structure, since giving the ECJ itself power over
non-member states was found to conflict with the EU treaties (see
[[INTL-EFTA-SURVEILLANCE-AUTHORITY]] for the same finding). Confirmed
independently by reading efta.int's own "Two Pillar Structure" page
directly (2026-08-22): "In the EFTA pillar, certain EU bodies are
mirrored, such as a surveillance authority and a court of justice."

## History confirmed directly

The Court "took up its functions" on **1 January 1994**, when the EEA
Agreement entered into force, with five judges nominated by Austria,
Finland, Iceland, Norway and Sweden — the EFTA states then outside the
EU. Switzerland could not ratify the EEA Agreement after its 1992
referendum, and Liechtenstein postponed membership until 1 May 1995. In
1995 Austria, Finland and Sweden left EFTA for the EU, leaving the three
current EEA EFTA states, and the Court moved its seat from **Geneva to
Luxembourg on 1 September 1996** — alongside the European Court of
Justice and the General Court. It now sits with **three permanent
judges**, one nominated by each of Iceland, Liechtenstein and Norway,
plus six ad hoc judges.

## What it is not

Like [[INTL-EFTA-SURVEILLANCE-AUTHORITY]], its jurisdiction is the three
EEA EFTA states and not Switzerland, EFTA's fourth member — the reason
its anchor edge points at [[INTL-EEA-AGREEMENT]] rather than
[[INTL-EFTA]].

## Not modelled

- The **Surveillance and Court Agreement** as a separate instrument.
- The Court's **case law** — its rulings on homogeneity with EU law,
  state liability and fundamental rights, catalogued in detail on the
  Wikipedia article and nowhere else in this Atlas.
- Its **President and Registry**.

## Sources

Listed in frontmatter. `efta.int`'s "Two Pillar Structure" page and both
Wikipedia articles were read directly this pass with an honest
User-Agent; `eftacourt.int` returns only live case-docket content
regardless of path.
