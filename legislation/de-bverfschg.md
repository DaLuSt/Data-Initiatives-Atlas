---
id: DE-BVERFSCHG
type: law
name: Bundesverfassungsschutzgesetz
alternative_names:
  - BVerfSchG
description: >
  German federal act governing the Bundesamt für Verfassungsschutz and the
  cooperation between the federation and the Länder in matters of
  constitutional protection. It is one of the three service-specific acts of
  the federal intelligence services and is named by the federal data
  protection commissioner among the essential legal bases for intelligence
  data processing.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: "1990-12-20"
end_date: null
last_verified: "2026-09-26"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - DE-BFV
  - DE-BNDG
  - DE-MADG
  - DE-G10
relationships: []

sources:
  - title: "Die Arbeit der Nachrichtendienste"
    url: "https://www.bundestag.de/webarchiv/Ausschuesse/ausschuesse20/weitere_gremien/parlamentarisches_kontrollgremium/nachrichtendienste-867434"
    publisher: "Deutscher Bundestag"
    accessed: "2026-08-22"
  - title: "Aufsicht über die Nachrichtendienste des Bundes"
    url: "https://www.bfdi.bund.de/DE/Fachthemen/Inhalte/Nachrichtendienste/Kontrollandschaft-Nachrichtendienste-des-Bundes.html"
    publisher: "Bundesbeauftragte für den Datenschutz und die Informationsfreiheit (BfDI)"
    accessed: "2026-08-22"
  - title: "Recht & Gesetz"
    url: "https://geheimdienste.org/recht-und-gesetz"
    publisher: "geheimdienste.org"
    accessed: "2026-08-22"
  - title: "Bundesverfassungsschutzgesetz (BVerfSchG) — BJNR029700990"
    url: "https://www.gesetze-im-internet.de/bverfschg/BJNR029700990.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    accessed: "2026-09-05"
  - title: "Bundesverfassungsschutzgesetz (BVerfSchG)"
    url: "https://bundestag.github.io/gesetze/b/bverfschg/"
    publisher: "Deutscher Bundestag (community-maintained statute mirror)"
    accessed: "2026-09-25"
    note: "gesetze-im-internet.de returned HTTP 503 on repeated attempts this pass; this mirror substitutes for the amendment-history citation."
---

# Bundesverfassungsschutzgesetz (BVerfSchG)

> **Verified 2026-08-22.** The Bundestag's "Die Arbeit
> der Nachrichtendienste" page and the BfDI's "Kontrolllandschaft
> Nachrichtendienste des Bundes" page were read directly and confirmed the
> claims below. `geheimdienste.org` was fetched but not needed to support
> any claim once the two official pages had.
>
> **Updated 2026-09-05**: the act's own consolidated text was found on
> `gesetze-im-internet.de` and read directly, closing the previously
> flagged citation gap and sourcing `start_date`.
>
> **Narrowed 2026-09-25** (`discovery/unresolved.md` row #194): the
> amendment history beyond enactment is now sourced too, via
> `bundestag.github.io`'s community-maintained mirror.
>
> **Closed 2026-09-26**: the act's internal structure (its four
> Abschnitte) is now sourced too, via the same mirror — row #194's last
> remaining clause, for both this act and [[DE-MADG]].

## Description

The BVerfSchG is the act governing [[DE-BFV]]. It is listed first among the
main legal frameworks for the German services, and first among the essential
legal bases for their data processing, in both the Bundestag's and the
BfDI's accounts.

Confirmed directly on bfdi.bund.de's "Kontrolllandschaft Nachrichtendienste
des Bundes" page (2026-08-22): "Die wesentlichen Rechtsgrundlagen für
Datenverarbeitungen der Nachrichtendienste des Bundes ... sind das
BVerfSchG, das MADG, das BNDG, das G10G und das TKG."

## The Gesetze-im-Internet gap, closed 2026-09-05

This entity previously carried `coverage: low` because no
Gesetze-im-Internet URL had been found by search, unlike [[DE-BNDG]] and
[[DE-PKGRG]]. A fresh search located it: `gesetze-im-internet.de` hosts
the act's own consolidated text at `BJNR029700990.html`, whose header,
read directly, gives its full official title — "Gesetz über die
Zusammenarbeit des Bundes und der Länder in Angelegenheiten des
Verfassungsschutzes und über das Bundesamt für Verfassungsschutz" — and
states "Ausfertigungsdatum: 20.12.1990", also cited there in full as
"Bundesverfassungsschutzgesetz vom 20. Dezember 1990 (BGBl. I S. 2954,
2970)". `start_date` is now recorded as **20 December 1990** rather than
left `null`.

Its structure and amendment history beyond the enactment date remain
unread — this pass confirmed the citation, not the act's substantive
provisions.

**Amendment history closed 2026-09-25**: `bundestag.github.io`'s
community-maintained statute mirror, read directly (the official
`gesetze-im-internet.de` page returned HTTP 503 on every attempt this
pass, as it did for [[DE-MADG]] on 2026-09-05), gives the act's own
"Zuletzt geändert durch" (most recently amended by) line: **"Art. 2 G v.
20.8.2012 I 1798"** — 20 August 2012.

**Internal structure closed 2026-09-26**: `discovery/unresolved.md` row
#194's last remaining clause. Confirmed by reading `bundestag.github.io`'s
mirror directly, the act runs in **four Abschnitte**:

| Abschnitt | §§ | Subject |
|---|---|---|
| Erster | 1–7 | Cooperation, tasks of the constitutional-protection authorities |
| Zweiter | 8–16 | [[DE-BFV]] itself |
| Dritter | 17–26 | Transmission provisions (Übermittlungsvorschriften) |
| Vierter | 27 | Final provisions |

## The federal/Länder question this act raises and the Atlas cannot answer

The German constitutional-protection system is federal **and** state-level:
sixteen Landesämter operate alongside [[DE-BFV]], and the act's own subject
matter includes cooperation between the federation and the Länder.

The Atlas has no sub-national level, so none of that is modelled. A reader
should not take a single `DE` law entity plus a single `DE` service entity
as describing German domestic intelligence — the same warning
[[DE-BFDI]] carries about data protection supervision.

## Sources

Listed in frontmatter. The act's own consolidated text at
gesetze-im-internet.de added and read directly 2026-09-05;
`bundestag.github.io`'s mirror re-read directly 2026-09-26 for the act's
internal structure.
