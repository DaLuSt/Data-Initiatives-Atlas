---
id: DE-G10
type: law
name: Gesetz zur Beschränkung des Brief-, Post- und Fernmeldegeheimnisses
alternative_names:
  - Artikel 10-Gesetz
  - G10G
description: >
  German federal act restricting the privacy of correspondence, post and
  telecommunications guaranteed by Article 10 of the Basic Law, and setting
  the conditions under which the federal intelligence services may interfere
  with it. It applies across all three services rather than to one of them,
  and is named by the federal data protection commissioner among the
  essential legal bases for intelligence data processing.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
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
  - DE-BND
  - DE-BFV
  - DE-BAMAD
  - DE-BNDG
  - DE-BVERFSCHG
  - DE-MADG
  - DE-G10-KOMMISSION
relationships: []

sources:
  - title: "Die Arbeit der Nachrichtendienste"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse20/weitere_gremien/parlamentarisches_kontrollgremium/nachrichtendienste-867434"
    publisher: "Deutscher Bundestag"
    accessed: "2026-08-22"
  - title: "Aufsicht über die Nachrichtendienste des Bundes"
    url: "https://www.bfdi.bund.de/DE/Fachthemen/Inhalte/Nachrichtendienste/Kontrollandschaft-Nachrichtendienste-des-Bundes.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
  - title: "Recht & Gesetz"
    url: "https://geheimdienste.org/recht-und-gesetz"
    publisher: "geheimdienste.org"
    accessed: "2026-08-22"
  - title: "G 10 — Gesetz zur Beschränkung des Brief-, Post- und Fernmeldegeheimnisses"
    url: "https://bundestag.github.io/gesetze/g/g10_2001/"
    publisher: "Deutscher Bundestag (community-maintained statute mirror)"
    accessed: "2026-09-05"
    note: "gesetze-im-internet.de's own text (g10_2001/BJNR125410001.html) returned HTTP 503 on repeated attempts this pass; this mirror substitutes."
  - title: "Artikel 10-Gesetz"
    url: "https://de.wikipedia.org/wiki/Artikel_10-Gesetz"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
---

# Artikel 10-Gesetz (G10)

> **Verified 2026-08-22.** The Bundestag's "Die Arbeit
> der Nachrichtendienste" page and the BfDI's "Kontrolllandschaft
> Nachrichtendienste des Bundes" page were read directly and confirmed the
> claims below. `geheimdienste.org` was fetched but not needed to support
> any claim once the two official pages had.
>
> **Updated 2026-09-05**: the act's enactment date is now sourced and the
> G10-Kommission it establishes is now modelled as
> [[DE-G10-KOMMISSION]].

## Description

The G10 restricts the secrecy of correspondence, post and
telecommunications guaranteed by **Article 10 of the Grundgesetz**, and sets
the conditions on which the federal services may interfere with it.

Confirmed directly on bfdi.bund.de's "Kontrolllandschaft Nachrichtendienste
des Bundes" page (2026-08-22): the G10G is named alongside the BVerfSchG,
MADG, BNDG and TKG as one of "die wesentlichen Rechtsgrundlagen für
Datenverarbeitungen der Nachrichtendienste des Bundes."

## The one German act that is about a power rather than a body

[[DE-BNDG]], [[DE-BVERFSCHG]] and [[DE-MADG]] each constitute a service. The
G10 does not. It governs **interception**, and therefore reaches all three —
which is why [[DE-BND]], [[DE-BFV]] and [[DE-BAMAD]] each carry two
`governed-by` edges, one to their own act and one to this.

In that respect the G10 is Germany's counterpart to
[[FR-LOI-RENSEIGNEMENT-2015]] and [[GB-IPA-2016]] — instruments that
legislate techniques rather than institutions. The difference is scope: the
French and British acts cover the *whole* range of intrusive techniques,
while the G10 covers the specific constitutional right in Article 10.

Germany therefore has **both** kinds of statute at once, where France and
the UK lean on the powers-based one and the Netherlands, Belgium, Spain and
Poland lean on the body-based one.

## Its name says what it does to a constitutional right

The act is universally called the *Artikel 10-Gesetz*, after the article of
the Basic Law it limits. A statute named for the right it restricts is
unusual and worth noticing: the constitutional cost is in the title.

## The enactment date and G10-Kommission, closed 2026-09-05

This entity previously carried `coverage: low` and `start_date: null`.
`gesetze-im-internet.de`'s own text returned HTTP 503 on repeated
attempts this pass; `bundestag.github.io`'s community-maintained mirror,
read directly, substitutes: "Ausfertigungsdatum: 26.06.2001" —
`start_date` is now recorded as **26 June 2001**. The same mirror's §
15 constitutes the **G10-Kommission**, the body authorising measures
under this act, previously flagged as unmodelled here and on
[[DE-PKGR]]. It is now [[DE-G10-KOMMISSION]], distinct from [[DE-PKGR]]
and from [[DE-UKR]].

## Sources

Listed in frontmatter. The bundestag.github.io mirror and
de.wikipedia.org's dedicated article added and read directly 2026-09-05.
