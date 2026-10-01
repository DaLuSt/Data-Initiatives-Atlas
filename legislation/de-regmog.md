---
id: DE-REGMOG
type: law
name: Registermodernisierungsgesetz
alternative_names:
  - RegMoG
  - Gesetz zur Einführung und Verwendung einer Identifikationsnummer in der öffentlichen Verwaltung
  - Register Modernisation Act
description: >
  German federal act dated 28 March 2021 (published 6 April 2021 as
  BGBl. I S. 591) introducing the use of an identification number in
  public administration. It makes the tax identification number under
  § 139b Abgabenordnung a change-resistant ordering feature for assigning
  administrative data to the correct person across the 50 register entries
  in the promulgated Act's Anlage (the government bill listed 56 and the
  Bundestag committee's text 51), on a phased
  implementation timeline whose core, the Identitätsnummerngesetz, entered
  into force on 31 August 2023,
  and is the legal basis on which Germany implements the once-only
  principle.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: 2021-03-28
end_date: null
last_verified: "2026-10-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-SDG
relationships:
  - type: related-to
    target: EU-SDG
    source: fact
    evidence: "CLOSES discovery/unresolved.md row #67. mgm-tp.com's own analysis piece (read directly, 2026-09-18) states: 'According to the RegMoG, 51 of the register types are to be provided with an identification number based on the tax number and thus primarily serve the exchange of evidence in the National Once-Only-Technical-System (NOOTS)' and separately, of NOOTS: 'The basis for this is the SDG Regulation adopted by the European Parliament in 2018 ... and lays the European foundation for the implementation of the Once-Only-Technical-System (OOTS). The German version is the National Once-Only Technical System (NOOTS), which is based on the OOTS.' The European Commission's own OOTS Hub page ('The Once-Only view from Germany', digital-building-blocks, read directly) independently corroborates NOOTS as Germany's OOTS implementation, run 'as part of the wider Register Modernisation programme.' `type: related-to` rather than `implements-requirement-from`, because the chain is two-step (RegMoG feeds NOOTS; NOOTS is Germany's instance of the SDG Regulation's OOTS) and no source states RegMoG itself transposes the Regulation — it remains, as this entity's own text says, domestic register law rather than a transposition instrument. **Direct statement found 2026-10-01**: the BMI's own FAQ on the Act (bmi.bund.de, read directly via the cookie-jar workaround, discovery/unresolved.md row #217) says: 'Auch europäische Vorgaben (insb. die sog. \"Single Digital Gateway\"-Verordnung) verpflichten die deutsche Verwaltung zur Umsetzung dieses sog. \"Once-Only\"-Prinzips ... Das Registermodernisierungsgesetz schafft die erforderlichen Voraussetzungen dafür.' (European requirements, in particular the Single Digital Gateway Regulation, oblige German administration to implement the once-only principle; the Registermodernisierungsgesetz creates the necessary prerequisites for it.) The ministry responsible for the Act therefore connects it to the SDG Regulation itself, not only through an analyst's two-step chain, so confidence rises from medium to high. The type stays `related-to`: the FAQ says the Act creates prerequisites for meeting an SDG-driven obligation, not that it transposes the Regulation."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Registermodernisierungsgesetz — Mit dem 'once-only'-Prinzip zur digitalen und bürgerfreundlichen Verwaltung"
    url: "https://www.walhalla.de/news/registermodernisierungsgesetz-once-only-prinzip-zur-digitalen-und-buergernahen-verwaltung"
    publisher: "Walhalla Fachverlag"
    accessed: "2026-08-28"
  - title: "Die Steuer-ID als behördenübergreifend verwendbare Personenkennziffer"
    url: "https://www.rehm-verlag.de/neues-datenschutzrecht-fuer-bayern/aktuelle-beitraege-datenschutz/die-steuer-id-als-behoerdenuebergreifend-verwendbare-personenkennziffer/"
    publisher: "rehm Verlag"
    accessed: "2026-08-28"
  - title: "Registermodernisierung: Automatisierung auf Kosten der Sicherheit"
    url: "https://netzpolitik.org/2023/registermodernisierung-automatisierung-auf-kosten-der-sicherheit/"
    publisher: "netzpolitik.org"
    accessed: "2026-08-28"
  - title: "Gesetz zur Einführung und Verwendung einer Identifikationsnummer in der öffentlichen Verwaltung (Identifikationsnummerngesetz — IDNrG)"
    url: "https://www.gesetze-im-internet.de/idnrg/BJNR059110021.html"
    publisher: "Bundesministerium der Justiz / juris (Gesetze im Internet)"
    accessed: "2026-10-01"
    note: "Article 1 of the RegMoG and its core. Read directly; ISO-8859-1 encoded."
  - title: "Entwurf eines Gesetzes zur Einführung und Verwendung einer Identifikationsnummer in der öffentlichen Verwaltung (Registermodernisierungsgesetz – RegMoG), Gesetzentwurf der Bundesregierung"
    url: "https://dserver.bundestag.de/btd/19/242/1924226.pdf"
    publisher: "Deutscher Bundestag (Drucksache 19/24226, 11 November 2020)"
    accessed: "2026-10-01"
    note: "The government bill; its Anlage lists 56 registers."
  - title: "Beschlussempfehlung und Bericht des Ausschusses für Inneres und Heimat zum RegMoG"
    url: "https://dserver.bundestag.de/btd/19/262/1926247.pdf"
    publisher: "Deutscher Bundestag (Drucksache 19/26247, 27 January 2021)"
    accessed: "2026-10-01"
    note: "The committee's amendments take the Anlage from 56 to 51 entries."
  - title: "RegMoG Registermodernisierungsgesetz"
    url: "https://www.buzer.de/RegMoG.htm"
    publisher: "buzer.de"
    accessed: "2026-08-28"
  - title: "Registermodernisierungsgesetz verkündet"
    url: "https://www.bmi.bund.de/SharedDocs/pressemitteilungen/DE/2021/04/registermodernisierungsgesetz-verkuendet.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
    accessed: "2026-10-01"
    note: "Read directly via a cookie-jar-aware fetch; the HTTP 400 recorded on 2026-08-28 was a missing session cookie, not a genuine block (discovery/unresolved.md row #217)."
  - title: "FAQs zum Registermodernisierungsgesetz"
    url: "https://www.bmi.bund.de/SharedDocs/faqs/DE/themen/moderne-verwaltung/registermodernisierung/registermodernisierung-faq-liste.html"
    publisher: "Bundesministerium des Innern und für Heimat (BMI)"
    accessed: "2026-10-01"
    note: "Read directly via the same cookie-jar workaround."
  - title: "The importance of European standards for German register modernization"
    url: "https://insights.mgm-tp.com/en/2024/publicsector/the-importance-of-european-standards-for-german-register-modernization/"
    publisher: "mgm technology partners"
    accessed: "2026-09-18"
  - title: "The Once-Only view from Germany"
    url: "https://ec.europa.eu/digital-building-blocks/sites/display/OOTS/The+Once-Only+view+from+Germany"
    publisher: "European Commission — Digital Building Blocks (OOTS Hub)"
    accessed: "2026-09-18"
---

# Registermodernisierungsgesetz (RegMoG)

> **Closed 2026-10-01** (`discovery/unresolved.md` row #226 opened): the
> Act's own statutory text on `gesetze-im-internet.de` is now read
> directly — entry into force 31 August 2023, deadline arithmetic, the
> Bundesverwaltungsamt as the Registermodernisierungsbehörde, § 4 data,
> § 16 evaluation — and its Anlage lists **50** registers where this
> entity's secondary sources say 51. Traced the same day through the
> government bill (56) and the Interior Committee text (51): the secondary
> sources' figure is the committee stage; the step to 50 is unexplained.
>
> **Closed 2026-10-01** (`discovery/unresolved.md` row #217): the HTTP 400
> on both `bmi.bund.de` pages was a missing session cookie, not a block.
> Both are now read directly. The press release confirms the promulgation
> date; the FAQ contains a **direct statement connecting the Act to the
> Single Digital Gateway Regulation**, which the "once-only chain" section
> below said no source supplied. See "What the ministry's own FAQ says".
>
> **Re-verified 2026-08-28.** Both `bmi.bund.de` pages return HTTP 400 Bad
> Request on every attempt this pass — consistent with the same domain
> being unreachable across other entities in this batch ([[DE-OZG]]). The
> three non-government sources (Walhalla, rehm-Verlag, netzpolitik.org)
> all loaded directly, and `buzer.de`, a legal-database mirror, was added
> and read directly to confirm the statute's own date and Bundesgesetzblatt
> citation. Three (now four) of six is a genuine majority.
> `verification: primary-source`.
>
> **Closed 2026-09-18** (`discovery/unresolved.md` row #67): the refusal
> below is closed, not by finding RegMoG itself transposing [[EU-SDG]],
> but by tracing the two-step chain through NOOTS. See "The once-only
> chain, found" below.

## The statutory text, read directly — 2026-10-01

`gesetze-im-internet.de`, which returned HTTP 503 on the one attempt of
2026-08-28 and was not retried, loads now, and its text of the **Gesetz zur
Einführung und Verwendung einer Identifikationsnummer in der öffentlichen
Verwaltung (Identifikationsnummerngesetz, IDNrG)** — Article 1 of the
RegMoG — is read directly. What it establishes:

- **Entry into force**: the footnote states the IDNrG entered into force on
  **31 August 2023** ("gem. Art. 22 Satz 2 iVm Bek. v. 24.8.2023 I Nr. 230
  mWv 31.8.2023"), while § 12 (the ordinance power) took effect earlier,
  on **7 April 2021**, under Art. 22 Satz 1. This is the exact date behind
  the "August 2023" step buzer.de's phased timeline gives below.
- **Goals (§ 1)**: the tax ID under § 139b AO is introduced as an
  additional ordering feature in the registers listed in the Anlage in
  order to assign a natural person's data unambiguously in an
  administrative procedure, improve data quality, and reduce the
  resubmission of data public bodies already hold.
- **Deadline (§ 2)**: register-holding bodies must store the ID and
  replace the corresponding stored data with the Bundeszentralamt für
  Steuern's "bis spätestens zum Ablauf des fünften auf das Inkrafttreten
  dieses Gesetzes folgenden Kalenderjahres" (by the end of the fifth
  calendar year following entry into force). Applied to a 31 August 2023
  entry into force this falls at the end of **2028** — the Atlas's own
  arithmetic on the sourced date, not a figure any source states, and it
  differs from the end-2026 horizon rehm-Verlag implies from the 2021
  enactment.
- **The authority (§ 3)**: the *Registermodernisierungsbehörde* — which
  maintains the register overview, passes the ID and basic data to
  register holders and steers the projects — is the **Bundesverwaltungsamt**
  ("Das Bundesverwaltungsamt nimmt die Aufgaben der
  Registermodernisierungsbehörde wahr"). The BVA is not an Atlas entity.
- **Data (§ 4)**: the basic data are the ID, family name, former names,
  given names, doctorate, date and place of birth, sex, nationalities,
  current or last known address, date of death, and move-in and move-out
  dates; the further data are information blocks under the Bundesmeldegesetz
  and the month and year of the last administrative contact. This matches
  the BMI FAQ's list below item for item.
- **Purpose limits (§ 5)**: processing the ID for other purposes is
  inadmissible except for services under the Onlinezugangsgesetz
  ([[DE-OZG]]) on a legal basis or with consent, and for a register-based
  census.
- **Offence (§ 17)**: unauthorised collection, storage, transmission or
  dissemination is punishable by up to one year's imprisonment or a fine,
  prosecuted only on application of the data subject, the controller or the
  data-protection authorities.
- **Evaluation (§ 16)**: the ministry must report to the Bundestag in the
  third year after entry into force and every three years thereafter, and
  in the fifth year assess effectiveness "unter Einbeziehung von
  wissenschaftlichem Sachverstand", with recommendations on whether
  **sector-specific identification numbers** are introduced for other areas
  or **one uniform number for all registers** is implemented — the same
  choice between sector-specific and uniform identifiers that the critics
  below dispute.

**The register count, traced through three documents — partly explained.**
Three primary texts, each read directly, give three different numbers:

| Stage | Document | Entries in the Anlage |
|---|---|---|
| Government bill, 11 Nov 2020 | Bundestag Drucksache 19/24226 | **56** |
| Interior Committee text, 27 Jan 2021 | Drucksache 19/26247 | **51** (the bill's 56 less five deleted) |
| Promulgated Act, current consolidated text | `gesetze-im-internet.de` | **50** |

The committee's amendments delete five entries, "Nummern 32, 40, 41, 46
und 48": the Schuldnerverzeichnis, the Insolvenzregister, the
Rechtsdienstleisterregister, the Rechtsanwaltskammern directories and the
Liegenschaftskataster. Its explanation attributes three of the deletions
to the Bundesrat's opinion of 6 November 2020 (BR-Drs. 563/20), the
Liegenschaftskataster to a further Bundesrat point, and the Rechtsanwalts-
kammer directories to the Bundesrechtsanwaltskammer's objection that they
do not serve administrative procedures. The committee also renames two
entries (the civil-status registers and the accident-insurance employers'
directory) and replaces the EMAS register with the Zulassungsregister for
environmental verifiers, none of which changes the count.

**So the "51" in this entity's secondary sources (rehm-Verlag; mgm
technology partners) matches the committee text, not the promulgated
Act.** Both are accurate for the stage they describe. The Act as
promulgated has 50.

**What is still unexplained** is the last step, 51 to 50. Compared with the
committee text, the promulgated Anlage lacks the "Register zum
vorübergehenden Schutz nach § 91a des Aufenthaltsgesetzes" and the
"Bauvorlagenberechtigungsverzeichnisse", and adds a new item 43 for all
lists, directories or registers that the Länder's architects' and
engineers' chambers keep by law. Nothing in the committee report mentions
either change, and the promulgated Anlage's Fundstelle, BGBl. I 2021,
596-597, carries no amendment note. A plenary amendment, a change after the
Bundestag vote or a later amendment are all possible and none is asserted.
The Gazette text itself (`bgbl.de` serves only a JavaScript shell) and the
Bundestag's final-vote record were not read.

Two other details from the same documents. The bill's own problem statement
cites a 2017 National Regulatory Control Council opinion putting the number
of central and decentralised data registers at about **220**, the figure
this entity attributes to walhalla.de. And the committee changed § 16
para. 2 to require the effectiveness report in the **fifth** year after
entry into force rather than the sixth, which matches the promulgated text
read above. Some Anlage entries are collective, so no figure is a count of
databases.

## Description

The RegMoG is dated **28 March 2021** and was published on **6 April 2021**
as **BGBl. I S. 591** — the exact citation confirmed directly on the
2026-08-28 pass via buzer.de, closing the "no statutory text" gap flagged
in the entity's earlier text. (The official `gesetze-im-internet.de` copy
returned HTTP 503 that day; it is read directly as of 2026-10-01 — see the
section above.)

It introduces the use of an identification number in public administration,
so that administrative data can be assigned to the correct person securely
and in conformity with data protection law using a **change-resistant
ordering feature** — the tax identification number, formally the
Identifikationsnummer under **§ 139b Abgabenordnung**.

The sources describe the consequence bluntly: the Steuer-ID takes on the
function of a **general personal identifier** (allgemeine Personenkennziffer),
confirmed directly to be stored as an "additional ordering
characteristic" (zusätzliches Ordnungsmerkmal) in **51 registers**
(rehm-Verlag's own figure, read directly, updating the entity's earlier
"roughly 50" — the figure matches the Bundestag committee's text of
27 January 2021, while the promulgated Act's Anlage lists 50; see the
section above) — including the
residents' register, the driving licence and weapons registers, and with
pension and health insurance funds. walhalla.de, read directly, adds
context this entity did not previously carry: the reform addresses
fragmentation across roughly **220** central and decentralised registers.

**Timeline, now sourced with appropriate uncertainty rather than a single
figure**: rehm-Verlag's page (read directly) describes a "five-year
implementation window from the law's 2021 enactment," implying an
end-2026 horizon for full register integration; buzer.de (read directly)
instead describes a genuinely **phased** rollout with different provisions
taking effect at different times (immediately on 7 April 2021, then August
2023, November 2023, 2024 and 2025, with later announcements referencing
May 2026), gated in most cases on the Federal Interior Ministry declaring
the technical prerequisites met under Article 22 of the act, rather than
running to one fixed deadline. Both are recorded rather than picking
one arbitrarily, since they describe a genuinely staggered process rather
than contradicting each other outright.

Its purpose is the **once-only principle**: data and documentation already
held in registers should not have to be submitted repeatedly. Citizens,
businesses and organisations supply their data once, and authorities
retrieve it for each subsequent administrative process.

## The German counterpart to the Dutch base registers

This is the German analogue of [[NL-BASISREGISTRATIES]] and of the
identity infrastructure the Dutch stelsel rests on — the same problem
(authoritative person data reused across government) solved by a
different mechanism (one existing tax number pressed into service as a
cross-domain key, rather than a system of designated authentic
registrations).

**No relationship to the Dutch entities is asserted**, and the difference
is instructive enough to be worth stating: functionally equivalent
national programmes need not be structurally comparable, and the Atlas
should not imply they are.

## The once-only chain, found — 2026-09-18

For several passes, `implements-requirement-from` → [[EU-SDG]] was refused:
the once-only principle is the organising idea of both the RegMoG and the
Single Digital Gateway Regulation, but no source read connected them
directly, and the RegMoG reads as domestic register law rather than a
transposition instrument.

The gap is closed, not by overturning that reading, but by tracing the
chain a step further. mgm technology partners' own analysis, read
directly, states plainly: *"According to the RegMoG, 51 of the register
types are to be provided with an identification number based on the tax
number and thus primarily serve the exchange of evidence in the National
Once-Only-Technical-System (NOOTS)."* The same source states NOOTS's own
origin: *"The basis for this is the SDG Regulation adopted by the European
Parliament in 2018 ... and lays the European foundation for the
implementation of the Once-Only-Technical-System (OOTS). The German
version is the National Once-Only Technical System (NOOTS), which is
based on the OOTS."* The European Commission's own OOTS Hub page, read
directly, independently corroborates NOOTS as Germany's OOTS
implementation, run "as part of the wider Register Modernisation
programme."

So the connection is real and now sourced, but two steps rather than one:
RegMoG's 51 identified registers feed NOOTS, and NOOTS is Germany's
instance of the SDG Regulation's OOTS. `type: related-to` is used rather
than `implements-requirement-from`, since no source states RegMoG itself
transposes the Regulation — the earlier judgment that it is domestic
register law, not a transposition instrument, stands.

**A link to the Steuer-ID or the Abgabenordnung** remains refused. Neither
is an Atlas entity, and creating a tax statute to hang this on would be
building the graph around a single reference.

## What the ministry's own FAQ says — 2026-10-01

Read directly (the page was unreachable on every earlier pass, a missing
session cookie rather than a block): the BMI's FAQ answers "Warum brauchen
wir das überhaupt?" by tying the Act both to national and to European
requirements. Once-only electronic exchange of data and evidence is a
precondition for user-friendly digital administration, and "auch
europäische Vorgaben (insb. die sog. 'Single Digital Gateway'-Verordnung)
verpflichten die deutsche Verwaltung zur Umsetzung dieses sog.
'Once-Only'-Prinzips". Citizens must be unambiguously identifiable when
using services under the Onlinezugangsgesetz ([[DE-OZG]]), and "das
Registermodernisierungsgesetz schafft die erforderlichen Voraussetzungen
dafür".

This is the **direct connection to [[EU-SDG]]** the previous section said
no source supplied. It does not say the Act *transposes* the Regulation —
it says the Act creates the prerequisites for meeting an obligation the
Regulation imposes — so the relationship stays `related-to`, now at
`confidence: high`. Whether that wording is closer to `implements-
requirement-from` is a vocabulary judgement, not a sourcing gap, and is
left as it stands rather than decided on one FAQ answer.

The FAQ also states, in the ministry's own words: the tax ID was chosen
because it is already stored in many registers and is a "nicht-sprechende"
(non-speaking) number generated at random, so that using it "bedeutet
keinen Zugriff auf Steuerdaten"; the basic data stored alongside it
(family and former names, given names, doctorate, date and place of birth,
sex, nationalities, current or last known address, information blocks
under the Bundesmeldegesetz, date of death, move-in and move-out dates and
the month and year of the last administrative contact) are set out in § 4
of the Identitätsnummerngesetz (IDNrG); and "es wird kein neuer zentraler
Datenbestand geschaffen" — the registers' contents are not merged centrally.

## Contested, and recorded as such

One cited source is a **critical piece from netzpolitik.org**, read
directly this pass, on the security implications of automating register
access. It is included deliberately, and this pass's direct reading
sharpens what it says rather than merely confirming it existed: it reports
the government **rejected a "Domain-ID Model"** — separate identifiers per
sector, which would have prevented centralised profiling — as "too
expensive" and "very difficult to implement." It also reports a specific
Bundesrat concern, read directly: the technical system for protecting
people who have filed an Auskunftssperre (information block, e.g. abuse
victims) "cannot effectively prevent" staff misuse given the large number
of employees with register access.

A general personal identifier is constitutionally contentious in Germany
for well-known historical reasons, and an Atlas entry that cited only the
responsible ministry's own material would present a contested measure as
settled. (When this was written, on 2026-08-28, the ministry's own pages
could not be fetched; they can now, and are cited below alongside the
critics.)

The Atlas records no position on the merits. It records that the measure is
contested, and specifically how, because that is a fact about the
initiative. Since 2026-10-01 the ministry's own side is also on record,
read directly in its FAQ: that no new central data store is created, that
registers' contents stay where they are, that the number does not replace
a person's name or ID card towards authorities, and that profile-building
is "rechtlich ausgeschlossen" (legally excluded) and backed by logging,
data-protection-officer oversight and criminal penalties of up to one
year. Those are the ministry's assertions about the design; the critics'
objections above are not answered by restating them.

## Relationships

- `related-to` [[EU-SDG]] — closed 2026-09-18 at `confidence: medium`,
  raised to `high` 2026-10-01 on the BMI FAQ's direct statement. See above.

Also reached from [[DE-BMI]], which `produces` it (`valid_until:
"2025-05-06"` as of the same pass, see [[DE-BMI]]).

## Sources

Listed in frontmatter — three of the original five plus one added mirror
were read directly in the 2026-08-28 pass; `bmi.bund.de`'s two pages
returned HTTP 400 on every attempt that pass. **Closed 2026-10-01**: that
was a missing session cookie, and both are now read directly. Two sources tracing the NOOTS/OOTS
chain — mgm technology partners' analysis and the European Commission's
own OOTS Hub page — were added and read directly 2026-09-18.
