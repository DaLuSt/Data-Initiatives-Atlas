---
id: DE-G10-KOMMISSION
type: organisation
name: G10-Kommission
alternative_names:
  - G 10-Kommission
description: >
  Independent German body that decides on the legality and necessity of
  restriction measures under the Artikel 10-Gesetz (G10) and exercises
  control over the federal intelligence services' collection, processing
  and use of personal data obtained under that act. Its members are
  appointed by the Parlamentarisches Kontrollgremium for the duration of
  a Bundestag legislative period.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 2001-06-26
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - DE-G10
  - DE-PKGR
  - DE-BND
  - DE-BFV
  - DE-BAMAD
relationships:
  - type: governed-by
    target: DE-G10
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP on DE-G10 and DE-PKGR. gesetze-im-internet.de's own text of the G10 act returned HTTP 503 on repeated attempts this pass; bundestag.github.io's community-maintained statute mirror, read directly, substitutes: Section 15(1) establishes the G10-Kommission ('Die G 10-Kommission besteht aus dem Vorsitzenden, der die Befähigung zum Richteramt besitzen muss, und drei Beisitzern sowie vier stellvertretenden Mitgliedern...'), and Section 15(5) gives it the decision authority quoted in the description. de.wikipedia.org's 'Artikel 10-Gesetz' article, read directly and independently, corroborates in its own words: 'Die G 10-Kommission entscheidet von Amts wegen als unabhängiges und an keine Weisungen gebundenes Organ über die Notwendigkeit und Zulässigkeit sämtlicher durch die Nachrichtendienste' [vorgenommenen Beschränkungsmaßnahmen]."
    confidence: medium
    valid_from: 2001-06-26
    valid_until: null
  - type: applies-to
    target: DE-BND
    source: fact
    evidence: "The G10-Kommission's Section 15(5) mandate — control over 'the entire collection, processing and use of personal data obtained under this act by federal intelligence services' — covers all three federal services, per bundestag.github.io's mirror of the statute text, read directly. DE-BND is one of the three named in that same section's context via DE-G10's own scope."
    confidence: medium
    valid_from: 2001-06-26
    valid_until: null
  - type: applies-to
    target: DE-BFV
    source: fact
    evidence: "Same Section 15(5) mandate as the DE-BND edge — the G10-Kommission's control covers all three federal services under DE-G10's scope."
    confidence: medium
    valid_from: 2001-06-26
    valid_until: null
  - type: applies-to
    target: DE-BAMAD
    source: fact
    evidence: "Same Section 15(5) mandate as the DE-BND edge — the G10-Kommission's control covers all three federal services under DE-G10's scope."
    confidence: medium
    valid_from: 2001-06-26
    valid_until: null

sources:
  - title: "G 10 — Gesetz zur Beschränkung des Brief-, Post- und Fernmeldegeheimnisses (§ 15)"
    url: "https://bundestag.github.io/gesetze/g/g10_2001/"
    publisher: "Deutscher Bundestag (community-maintained statute mirror)"
    accessed: "2026-09-05"
  - title: "G 10 — Gesetz zur Beschränkung des Brief-, Post- und Fernmeldegeheimnisses"
    url: "https://www.gesetze-im-internet.de/g10_2001/BJNR125410001.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    note: "Confirmed unreachable this pass: HTTP 503 on repeated attempts."
  - title: "Artikel 10-Gesetz"
    url: "https://de.wikipedia.org/wiki/Artikel_10-Gesetz"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
---

# G10-Kommission

> **Created 2026-09-05**, closing a gap [[DE-G10]] and [[DE-PKGR]] both
> flagged: "Germany appears here with two oversight bodies where it has
> at least three."

## Description

The G10-Kommission is the independent body that decides, before and
after the fact, on the **legality and necessity** of measures restricting
the privacy of correspondence, post and telecommunications under
[[DE-G10]]. Confirmed by reading bundestag.github.io's mirror of the
statute directly: § 15(1) constitutes the Commission of a chairperson
(who must be qualified for judicial office), three assessors and four
alternate members; § 15(5) gives it decision authority over "the
legality and necessity of restriction measures" and control over "the
entire collection, processing and use of personal data obtained under
this act by federal intelligence services."

de.wikipedia.org's dedicated article, read directly and independently,
corroborates in its own words: the Commission "decides ex officio, as an
independent organ bound by no instructions, on the necessity and
permissibility of all restriction measures undertaken by the
intelligence services."

## Appointed by the PKGr, distinct from it

Members are selected by [[DE-PKGR]] — the Parlamentarisches
Kontrollgremium — after consulting the Federal Government, and serve for
the duration of a Bundestag legislative period. The two bodies are
related but distinct in kind, the same distinction [[DE-PKGR]]'s own
entry already draws between itself and [[DE-UKR]]:

- **PKGr**: parliamentarians, political accountability, oversight of
  expenditure and general activity.
- **G10-Kommission**: judicially-qualified independent members,
  legality review of individual measures — Germany's analogue to
  [[NL-TIB]]'s binding prior review and the UK's [[GB-IPCO]] double lock,
  though for the G10 power specifically rather than the whole
  investigatory-powers range.

The Commission meets at least monthly and operates under strict
confidentiality requirements, per the mirror's own text.

## The third German oversight body, now modelled

Germany's federal intelligence oversight has (at least) three layers:
[[DE-PKGR]] (parliamentary), [[DE-UKR]] (legality review of BND
measures specifically, under a separate 2022 reform), and this
Commission (legality review of G10 interception measures across all
three services). This entity closes the gap both [[DE-G10]] and
[[DE-PKGR]] flagged: Germany no longer appears with only two oversight
bodies modelled.

## Not modelled

- The Commission's precise composition procedure and current membership.
- Its relationship to [[DE-UKR]], which reviews a different, narrower
  set of BND-specific measures under a separate 2022 reform — no source
  read states how the two bodies' remits interact where they might
  overlap.

## Relationships

- `governed-by` [[DE-G10]].
- `applies-to` [[DE-BND]], [[DE-BFV]] and [[DE-BAMAD]].

## Sources

Two of three read directly. `gesetze-im-internet.de`'s own text of the
G10 act returned HTTP 503 on repeated attempts this pass; the
`bundestag.github.io` mirror substitutes and de.wikipedia.org
independently corroborates.
