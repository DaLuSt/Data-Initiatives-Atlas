---
id: NL-TIB
type: organisation
name: Toetsingscommissie Inzet Bevoegdheden
alternative_names:
  - TIB
  - Investigatory Powers Commission
description: >
  Dutch commission that carries out binding prior review of the lawfulness
  of the AIVD's and MIVD's intended use of certain special powers under the
  Wet op de inlichtingen- en veiligheidsdiensten 2017. It reviews after the
  responsible minister has decided, and consists of three members — at
  least two with a judicial background — plus a secretary and technical
  advisor.

level: national
country: NL
region: EU

status: active
confidence: high
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - NL-WIV-2017
  - NL-AIVD
  - NL-MIVD
  - NL-CTIVD
  - NL-TWCO
relationships:
  - type: applies-to
    target: NL-AIVD
    source: fact
    evidence: "Confirmed by reading tib-ivd.nl's own 'Taken en bevoegdheden' page directly (2026-08-27): the TIB reviews whether special powers used by the AIVD and MIVD are lawful, assessing ministerial authorisation against four criteria — necessity, proportionality, subsidiarity and targeted application (specificity) — and 'het oordeel van de TIB is bindend' (the TIB's judgment is binding). nl.wikipedia.org's dedicated TIB article, also read directly, corroborates the four-criteria test and the binding effect."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-to
    target: NL-MIVD
    source: fact
    evidence: "Confirmed by reading defensie.nl's own oversight page directly (2026-08-27): the TIB 'provides mandatory advance approval for sensitive MIVD capabilities like computer hacking or phone wiretapping', applying the same necessity/proportionality/subsidiarity/specificity test, with a binding judgment."
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: NL-WIV-2017
    source: fact
    evidence: "Confirmed by reading nl.wikipedia.org's dedicated TIB article directly (2026-08-27): the TIB was established 1 September 2017 by the Wiv 2017 but became operationally active only 1 April 2018 — itself part of why the wider act's entry into force slipped from 1 January to 1 May 2018, per the Wiv 2017's own Wikipedia article, also read directly this pass."
    confidence: high
    valid_from: 2018-05-01
    valid_until: null
  - type: references
    target: NL-TWCO
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #190. aivd.nl's own TWCO page (read directly on that entity, 2026-08-27) states the temporary act shifts oversight of certain powers from TIB pre-approval towards real-time CTIVD monitoring with binding authority to halt an operation. NL-TWCO's own consolidated text at wetten.overheid.nl, re-read article by article (2026-09-19), now names the specific powers: Article 8 removes TIB review for one power entirely (transferred to CTIVD), Articles 4, 5, 9-10 carry CTIVD's binding real-time authority, and Article 14e retains TIB pre-approval (made explicitly binding) for a fifth. `type: references` rather than `governed-by`: TWCO narrows this entity's remit for the powers it covers rather than governing the TIB as a body."
    confidence: high
    valid_from: "2024-07-01"
    valid_until: null

sources:
  - title: "Taken en bevoegdheden"
    url: "https://www.tib-ivd.nl/wat-doet-de-tib/taken-en-bevoegdheden"
    publisher: "Toetsingscommissie Inzet Bevoegdheden (TIB)"
    accessed: "2026-08-27"
  - title: "Toetsingscommissie Inzet Bevoegdheden"
    url: "https://nl.wikipedia.org/wiki/Toetsingscommissie_Inzet_Bevoegdheden"
    publisher: "Wikipedia"
    accessed: "2026-08-27"
  - title: "Toetsingscommissie inzet bevoegdheden"
    url: "https://www.eerstekamer.nl/trefwoord/toetsingscommissie_inzet"
    publisher: "Eerste Kamer der Staten-Generaal"
---

# Toetsingscommissie Inzet Bevoegdheden (TIB)

> **Verified 2026-08-27.** Two of three cited pages were read directly this
> pass — tib-ivd.nl's own page and the dedicated Dutch Wikipedia article —
> closing the previous `search-only` status. The Eerste Kamer keyword page
> was not re-fetched; nothing it previously supported is contradicted.
>
> **Updated 2026-09-19** (`discovery/unresolved.md` row #190): a
> `references` edge to [[NL-TWCO]] closes the gap where NL-AIVD and
> NL-CTIVD already documented the TIB-to-CTIVD oversight shift but this
> entity did not. **Closed fully, same day**: [[NL-TWCO]]'s own text,
> re-read article by article, names the specific powers that move.

## Description

The TIB conducts **binding prior review** of whether the intended use of
certain special powers by [[NL-AIVD]] and [[NL-MIVD]] is lawful, assessed
against four named criteria — confirmed directly on tib-ivd.nl's own page:
**necessity, proportionality, subsidiarity and targeted application**
(specificity).

Its composition is now sourced precisely rather than approximately: reading
the Dutch Wikipedia article directly gives **three members**, at least two
with a judicial background, supported by a secretary and a technical
adviser — not simply "two judges and a technical expert" as previously
recorded. As of April 2023 the named members were Anne Mieke Zwaneveld
(chair), Eric Druijf and Otto Vermeulen. That composition tells you what the
review is for: a legality check by people qualified to make one, not a
policy or proportionality body in the political sense.

## It reviews *after* the minister decides

This is the detail most easily got wrong. The TIB does not advise the
minister in advance of the decision; it reviews **after** the responsible
minister has already granted permission, and its decision is **binding** —
"het oordeel van de TIB is bindend", per its own page. A minister's
authorisation that the TIB finds unlawful does not take effect. In
emergencies, per both tib-ivd.nl and Wikipedia, services may act first,
with TIB review following.

That makes the Dutch model unusually strong on paper compared with, for
instance, the French one: [[FR-CNCTR]] issues an *avis* to the Prime
Minister, who may proceed against it, with recourse to the Conseil d'État.

## The commission that delayed its own act

[[NL-WIV-2017]] was to enter into force on 1 January 2018. It entered into
force on **1 May 2018** instead. Reading the Wikipedia article on the TIB
directly gives a sharper picture than "candidates took longer to find": the
TIB was established by the Wiv 2017 as of **1 September 2017** but did not
become operational until **1 April 2018** — a six-month gap the article
attributes to the need to align the new commission's working method with
European case law requirements, not only staffing. Early operation was
rocky: the article cites May–October 2018 figures of roughly 5.5% of AIVD
and 4.1% of MIVD requests found unlawful, which the responsible ministries
characterised at the time as start-up issues.

## Not modelled

- The **specific statutory list** of powers requiring TIB approval under
  the Wiv 2017 itself — the sources name examples (hacking, wiretapping,
  directional microphones), not the underlying articles.

**Which specific powers move under [[NL-TWCO]], closed 2026-09-19**: that
Act's own text, read article by article, names the powers exactly.
[[NL-TWCO]] Article 8 removes TIB review entirely for one power (general
analysis of already-collected traffic/location data, otherwise TIB-reviewed
under Wiv 2017 Art. 36(1)), transferring it to [[NL-CTIVD]]'s binding
real-time stop authority alongside three other powers (Arts. 4, 5, 9–10).
[[NL-TWCO]] Article 14e goes the other way for a fifth power — real-time
interception of communications traffic data going forward, under Wiv 2017
Art. 55(1) — keeping TIB pre-approval and making its binding force
explicit. See [[NL-TWCO]] for the full article-by-article breakdown.

## Relationships

- `applies-to` [[NL-AIVD]] and [[NL-MIVD]].
- `governed-by` [[NL-WIV-2017]].
- `references` [[NL-TWCO]] — `confidence: high`. Closes
  `discovery/unresolved.md` row #190: the specific powers that move from
  TIB pre-approval to CTIVD real-time monitoring are now named, matching
  [[NL-AIVD]] and [[NL-CTIVD]].

## Sources

Two of three read directly in the 2026-08-27 pass: tib-ivd.nl's own
tasks-and-powers page and the dedicated Dutch Wikipedia article. The
Eerste Kamer keyword page was not re-fetched. The `references` NL-TWCO
edge added 2026-09-19 cites aivd.nl's own TWCO page and, for the specific
powers, [[NL-TWCO]]'s own consolidated text at wetten.overheid.nl — both
already read directly on that entity, not a new fetch on this one.
