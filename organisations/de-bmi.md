---
id: DE-BMI
type: organisation
name: Bundesministerium des Innern
alternative_names:
  - BMI
  - Federal Ministry of the Interior
  - Bundesministerium des Innern und für Heimat
description: >
  German federal interior ministry. Within the scope of the Atlas it is the
  department responsible for administrative modernisation, register
  modernisation and open-government legislation, and the ministry in whose
  portfolio the Bundesamt für Sicherheit in der Informationstechnik and the
  Statistisches Bundesamt sit.

level: national
country: DE
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - DE-BMDS
relationships:
  - type: produces
    target: DE-DATENSTRATEGIE
    source: fact
    evidence: "The Nationale Datenstrategie was jointly developed and presented by the BMDV, the BMWK and the BMI (bmi.bund.de press release 'Bundeskabinett beschließt Nationale Datenstrategie'; bmdv.bund.de). NOT READ — search-only. Two of the three co-authoring ministries are not Atlas entities. CLOSES discovery/unresolved.md row #60: `valid_until` set to 2025-05-06, the date egovernment.de's own reporting on the organisational decree (read directly 2026-09-18) and DE-BMI's own body text confirm as when BMDS absorbed BMI's digital-competence departments — the precise date the row asked for, rather than the vaguer 'after the reorganisation' this entity previously carried."
    confidence: medium
    valid_from: null
    valid_until: "2025-05-06"
  - type: produces
    target: DE-REGMOG
    source: fact
    evidence: "The BMI announced the promulgation of the Registermodernisierungsgesetz and maintains the ministry's FAQ on Registermodernisierung (bmi.bund.de 'Registermodernisierungsgesetz verkündet'; bmi.bund.de FAQ). NOT READ — search-only. CLOSES discovery/unresolved.md row #60: `valid_until` set to 2025-05-06 on the same basis as the DE-DATENSTRATEGIE edge above."
    confidence: medium
    valid_from: null
    valid_until: "2025-05-06"
  - type: produces
    target: DE-DNG
    source: fact
    evidence: "The BMI ran the legislative procedure for the act amending the E-Government-Gesetz and introducing the act on the use of public sector data (bmi.bund.de Gesetzgebungsverfahren 'zweites-open-data-gesetz'). NOT READ — search-only. The BMWK also presents the package. CLOSES discovery/unresolved.md row #60: `valid_until` set to 2025-05-06 on the same basis as the two edges above."
    confidence: medium
    valid_from: null
    valid_until: "2025-05-06"

sources:
  - title: "Bundeskabinett beschließt Nationale Datenstrategie"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2023/08/nationale-datenstrategie.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Registermodernisierungsgesetz verkündet"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2021/04/registermodernisierungsgesetz-verkuendet.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Gesetz zur Änderung des E-Government-Gesetzes und zur Einführung des Gesetzes für die Nutzung von Daten des öffentlichen Sektors"
    url: "https://www.bmi.bund.de/SharedDocs/gesetzgebungsverfahren/DE/DVI1/zweites-open-data-gesetz.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Upgrade für ein Digitales Deutschland ist da: Das OZG-Änderungsgesetz tritt in Kraft"
    url: "https://www.bmi.bund.de/SharedDocs/kurzmeldungen/DE/2024/07/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Bund hat seine 115 wichtigsten Verwaltungsleistungen bis Ende 2024 erfolgreich digitalisiert"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2024/12/ozg.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
  - title: "Bundesministerium des Innern"
    url: "https://de.wikipedia.org/wiki/Bundesministerium_des_Innern"
    publisher: "Wikipedia"
    accessed: "2026-09-05"
  - title: "BMDS bündelt Zuständigkeiten aus sechs Häusern"
    url: "https://www.egovernment.de/bmds-buendelt-zustaendigkeiten-aus-sechs-haeusern-a-7477b927211437b688e91eee2351357d/"
    publisher: "eGovernment Computing (egovernment.de)"
    accessed: "2026-09-18"
---

# Bundesministerium des Innern (BMI)

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `bund.de`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".
>
> **Updated 2026-09-05**: the ministry's current formal name, previously
> flagged as unclear, is now confirmed directly — see below.
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #60): the three
> `produces` relationships below now carry `valid_until: "2025-05-06"`,
> the organisational-decree date on which DE-BMDS absorbed the digital
> competences this entity's own text already named as historical. See
> "The name and the reorganisation" below.

## Description

The BMI is Germany's federal interior ministry. The Atlas records it for
its role in public-administration digitalisation rather than for its full
portfolio, which is much wider and out of scope here — hence
`coverage: low`.

Within that scope the sources establish that the BMI:

- co-authored the [[DE-DATENSTRATEGIE]] with the BMDV and the BMWK;
- announced the promulgation of the [[DE-REGMOG]] and maintains the
  ministry's Registermodernisierung FAQ;
- ran the legislative procedure for the "second open data act" package that
  amended the [[DE-EGOVG]] and introduced the [[DE-DNG]];
- announced the entry into force of the OZG-Änderungsgesetz and the
  completion of the federal government's 115 priority [[DE-OZG]] services.

[[DE-BSI]] is a Bundesoberbehörde in the BMI's portfolio, and
[[DE-DESTATIS]] sits in its Geschäftsbereich. Those `part-of` links are
recorded on the agencies themselves.

## The name and the reorganisation — name resolved 2026-09-05

The ministry has been styled both *Bundesministerium des Innern* and
*Bundesministerium des Innern und für Heimat*; the cited press releases use
the latter, which reflected the 2021–2025 designation.

**The current formal name is now confirmed directly.** Reading German
Wikipedia's own article on the ministry (de.wikipedia.org, 2026-09-05):
*"Bundeskanzler Friedrich Merz ordnete am 6. Mai 2025 in einem
Organisationserlass die Umbenennung in Bundesministerium des Innern an"* —
Chancellor Merz ordered the renaming back to **Bundesministerium des
Innern** by organisational decree on **6 May 2025**, reversing the
*"...und für Heimat"* designation that had been in effect since 8 December
2021. This is the same 6 May 2025 reorganisation date on which
[[DE-BMDS]] and [[DE-BMV]] were split out — the name change and the
competence transfer are the same event, not two separate ones.

Since [[DE-BMDS]] took over digital competences from six departments
including this one in that reorganisation, the BMI's role in several of
the relationships above is historical rather than current. The
relationships are recorded as facts about who did what at the time, with
`valid_from` left null because no source dates the *production* of each
instrument itself more precisely than what each entity's own text
already records.

**Closed 2026-09-18**: reading egovernment.de's own reporting on the
organisational decree directly confirms precisely which departments moved
and when — "digitale Verwaltung inkl. OZG-Steuerung ... IT-Beschaffung
des Bundes, ... Steuerung der IT des Bundes, die Netze des Bundes, die
Cyber-Sicherheit in der Bundesverwaltung und das Recht der digitalen
Verwaltung" moved from the BMI to the BMDS, with effect from the same **6
May 2025** decree already cited above for the name change. All three
`produces` relationships below now carry `valid_until: "2025-05-06"` on
that basis: the BMI is recorded as having produced each instrument (an
unchanging historical fact), and as having ceased to be the responsible
department for that policy area on that date.

## Relationships

- Produces [[DE-DATENSTRATEGIE]], [[DE-REGMOG]] and [[DE-DNG]].

Each `produces` evidence field names the co-authoring ministries that are
**not** Atlas entities, so the record does not imply sole authorship.

## Sources

Listed in frontmatter — all five are BMI pages, which is circular for an
entity about the BMI. It is the same weakness flagged on
[[EU-PUBLICATIONS-OFFICE]]. The facts they support are administrative
announcements about the ministry's own legislative work, which is the case
where self-sourcing is least troubling, but it is a weakness nonetheless.
