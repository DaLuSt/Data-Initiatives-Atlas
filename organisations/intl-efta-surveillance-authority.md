---
id: INTL-EFTA-SURVEILLANCE-AUTHORITY
type: organisation
name: EFTA Surveillance Authority
alternative_names:
  - ESA
  - European Free Trade Association Surveillance Authority
description: >
  Independent body that monitors compliance with the Agreement on the
  European Economic Area in Iceland, Liechtenstein and Norway — the three
  EEA EFTA states. It performs the watchdog role the European Commission
  performs for EU member states: monitoring the timely and correct
  implementation of EEA law and opening infringement proceedings that can
  end with a referral to the EFTA Court. Switzerland, an EFTA member but
  not an EEA party, falls outside its jurisdiction entirely. It was
  created because the European Court of Justice found, during the EEA
  Agreement's negotiation, that giving EU institutions direct powers over
  non-EU member states would violate the EU treaties. It is based in
  Brussels.

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
  - INTL-EFTA-COURT
  - EU-COMMISSION
  - "NO"
  - IS
  - LI
relationships:
  - type: part-of
    target: INTL-EEA-AGREEMENT
    source: fact
    evidence: "Confirmed by reading efta.int's own 'EEA Institutions - Two Pillar Structure' page directly (2026-08-22, fetched with an honest, identifying User-Agent — efta.int returns a bot-defense challenge to a browser User-Agent but real content to one that names itself as a bot): 'In the EFTA pillar, certain EU bodies are mirrored, such as a surveillance authority and a court of justice.' Corroborated by reading en.wikipedia.org/wiki/EFTA_Surveillance_Authority and en.wikipedia.org/wiki/European_Free_Trade_Association directly: the Authority 'monitors compliance with the Agreement on the European Economic Area (EEA) in Iceland, Liechtenstein and Norway (the EEA EFTA States)', and 'Since Switzerland is not an EEA member, it does not participate in these institutions.' Its jurisdiction is exactly the three EEA EFTA states, not the four EFTA states, so it is anchored to the Agreement rather than to [[INTL-EFTA]] under metadata/relationship-types.md §2.3 — the anchor with the matching scope is chosen over the anchor with the matching name. `eftasurv.int` remains genuinely unreadable even with an honest User-Agent: it is a JavaScript single-page application with no static content ('You need to enable JavaScript to run this app.'), and efta.int has no dedicated subpage for the Authority (guessed paths 404)."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: related-to
    target: INTL-EFTA
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/European_Free_Trade_Association directly (2026-08-22): 'The EFTA Surveillance Authority and the EFTA Court regulate the activities of the EFTA members in respect of their obligations in the European Economic Area (EEA).' Named for and closely associated with EFTA, but its jurisdiction does not match EFTA's own membership (Switzerland is excluded), so `related-to` rather than `part-of` — see the anchor edge above."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: EU-COMMISSION
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/EFTA_Surveillance_Authority directly (2026-08-22): 'ESA has powers that are similar to those of the European Commission ... ESA monitors the EEA EFTA States while the EU Commission monitors the EU Member States ... the two bodies consult each other and exchange data.' No formal cooperation instrument is named, so this is recorded as `related-to` rather than `cooperates-with`."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: related-to
    target: INTL-EFTA-COURT
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org/wiki/EFTA_Surveillance_Authority directly (2026-08-22): infringement proceedings opened by ESA are 'a three-step procedure which may result in ESA referring the case to the EFTA Court.' Both bodies were established by the same Agreement between the EFTA States on the Establishment of a Surveillance Authority and a Court of Justice, which the Atlas does not hold as a separate entity."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "EEA Institutions - Two Pillar Structure"
    url: "https://www.efta.int/eea-relations-eu/eea-institutions-two-pillar-structure"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "EFTA Surveillance Authority"
    url: "https://en.wikipedia.org/wiki/EFTA_Surveillance_Authority"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "European Free Trade Association"
    url: "https://en.wikipedia.org/wiki/European_Free_Trade_Association"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "The European Free Trade Association"
    url: "https://www.efta.int/about-efta/european-free-trade-association"
    publisher: "European Free Trade Association (EFTA)"
    accessed: "2026-08-22"
  - title: "EFTA Surveillance Authority"
    url: "https://www.eftasurv.int/"
    publisher: "EFTA Surveillance Authority"
    accessed: "2026-08-22"
---

# EFTA Surveillance Authority

> **Verified 2026-08-22, and a correction to standing guidance.**
> `efta.int` was treated as bot-walled (403) in every earlier pass this
> session, on the strength of a browser-spoofing User-Agent. Fetched
> instead with an honest, identifying User-Agent — the kind
> `tools/reverify.py` itself sends — `efta.int` returns real content:
> 200, not 403. It has no dedicated subpage for this Authority (guessed
> paths 404), but its "Two Pillar Structure" overview page confirms the
> Authority's place in the EFTA pillar directly. `eftasurv.int` was
> re-tested the same way and remains genuinely unreadable — a JavaScript
> single-page application with no static content ("You need to enable
> JavaScript to run this app. Loading application. Please wait."). Two
> Wikipedia articles, read directly and cross-checked against each other,
> fill in the detail efta.int itself does not carry.

## Description

Confirmed by reading en.wikipedia.org/wiki/EFTA_Surveillance_Authority
directly (2026-08-22): "The EFTA Surveillance Authority (ESA) monitors
compliance with the Agreement on the European Economic Area (EEA) in
Iceland, Liechtenstein and Norway (the EEA EFTA States)." ESA operates
independently of the states themselves and performs the same watchdog
role the European Commission performs for the Union: monitoring whether
EEA law incorporated under [[INTL-EEA-AGREEMENT]] is transposed correctly
and on time, and opening infringement proceedings when it is not.
Confirmed independently by reading efta.int's own "Two Pillar Structure"
page directly (2026-08-22): "In the EFTA pillar, certain EU bodies are
mirrored, such as a surveillance authority and a court of justice."

## Why it exists

Confirmed by reading en.wikipedia.org/wiki/European_Free_Trade_Association
directly (2026-08-22): "The original plan for the EEA lacked the EFTA
Court: the European Court of Justice was to exercise those roles.
However, during the negotiations for the EEA agreement, the European
Court of Justice ruled by the Opinion 1/91 that it would be a violation
of the treaties to give to the EU institutions these powers with respect
to non-EU members." (The EFTA Surveillance Authority article frames the
same event as a letter from the Court to the Council of the European
Union rather than naming the Opinion; both describe the same 1991
finding.)

The result is the EEA's "two-pillar structure": the EU institutions form
one pillar, the EEA EFTA states' own mirror institutions — this Authority
and the EFTA Court — form the other, and the two pillars are bridged by
the EEA Joint Committee. [[INTL-EEA-JOINT-COMMITTEE]] and
[[INTL-EFTA-COURT]] are now also Atlas entities, created in the same pass
as this one.

## What it is not

It monitors **Iceland, Liechtenstein and Norway** — the three EEA EFTA
states — and not Switzerland, an EFTA member that never ratified the EEA
Agreement. That is why this entity's anchor edge points at
[[INTL-EEA-AGREEMENT]] and not at [[INTL-EFTA]]: EFTA's own fourth member
falls outside its jurisdiction entirely.

## Not modelled

- The **Surveillance and Court Agreement** itself — the instrument,
  separate from the EEA Agreement, that formally establishes both this
  Authority and the EFTA Court. It is named in both Wikipedia sources but
  is not an Atlas entity.
- Its **internal organisation and staffing** (90 employees of 22
  nationalities, per the Wikipedia article).
- Individual **infringement cases and referrals** to the EFTA Court.

## Sources

Listed in frontmatter. Both Wikipedia articles were read directly this
pass; `efta.int` is bot-walled (403) and `eftasurv.int` is a JavaScript
single-page application with no static content — both are cited to
record the attempt honestly, not as read sources.
