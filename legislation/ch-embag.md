---
id: CH-EMBAG
type: law
name: Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben
alternative_names:
  - EMBAG
  - EMBaG
description: >
  Swiss federal act creating the legal basis for the digital transformation
  of the federal administration and for collaboration between authorities at
  different levels of government and with third parties. It establishes
  legal foundations for open government data and open source software,
  requiring federal authorities to release new software developments as open
  source. In force for central administrative units from 1 January 2024 and
  for decentralised units from May 2025.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2024-01-01
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH
  - CH-OPENDATA-SWISS
  - CH-DVS
relationships:
  - type: applies-in
    target: CH
    source: fact
    evidence: "Confirmed by reading netzwoche.ch directly (2026-08-22): 'Das \"Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben\" (Embag) soll Anfang 2024 in Kraft treten. Dies entschied der Bundesrat an seiner Sitzung vom 22. November [2023]... die im Gesetz verankerten Bestimmungen treten gestaffelt in Kraft: Zunächst sollen sie für die zentrale Bundesverwaltung gelten. Für die Einheiten der dezentralen Bundesverwaltung werde das Gesetz zu einem späteren Zeitpunkt... in Kraft gesetzt.' CLOSES discovery/unresolved.md row #113. The scope is now directly sourced: the statute's own Fedlex pdf-a text (SR 172.019, read directly 2026-09-19), Article 2, states 'Dieses Gesetz gilt für die zentrale Bundesverwaltung' (this Act applies to the central federal administration), with a footnoted paragraph 2 marked 'Noch nicht in Kraft' (not yet in force) corroborating the staged commencement for other bodies. The specific 'May 2025' date for decentralised units was NOT independently re-confirmed this pass and is retained from the original sourcing rather than dropped."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG)"
    url: "https://www.fedlex.admin.ch/eli/cc/2023/682/de"
    publisher: "Fedlex — Die Publikationsplattform des Bundesrechts"
    accessed: "2026-08-22"
  - title: "Bundesrat setzt E-Gov-Gesetz auf Anfang 2024 in Kraft"
    url: "https://www.netzwoche.ch/news/2023-11-23/update-bundesrat-setzt-e-gov-gesetz-auf-anfang-2024-in-kraft"
    publisher: "Netzwoche"
    accessed: "2026-08-22"
  - title: "EMBAG macht Open Source Software zur Norm"
    url: "https://app.ch/blog/embag-macht-open-source-software-zur-norm-chance-und-verpflichtung-fuer-die-bundesverwaltung"
    publisher: "APP Unternehmensberatung AG"
    accessed: "2026-08-22"
  - title: "EMBAG: Ja zu Open Source Software und Open Government Data"
    url: "https://parldigi.ch/de/embag/"
    publisher: "Parlamentarische Gruppe Digitale Nachhaltigkeit (Parldigi)"
    accessed: "2026-08-22"
  - title: "Open Government Data (OGD)"
    url: "https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd.html"
    publisher: "Bundesamt für Statistik (BFS)"
    accessed: "2026-08-22"
  - title: "Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG), SR 172.019 (pdf-a, Stand am 1. Januar 2024)"
    url: "https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2023/682/20240101/de/pdf-a/fedlex-data-admin-ch-eli-cc-2023-682-20240101-de-pdf-a.pdf"
    publisher: "Fedlex — Die Publikationsplattform des Bundesrechts"
    accessed: "2026-09-19"
---

# EMBAG — das «Digitalisierungsgesetz»

> **Verified 2026-08-22.** netzwoche.ch, app.ch and parldigi.ch were read
> directly and confirm the claims below, verbatim in places. The
> digital.swiss "massnahme" page cited previously has moved — the URL
> still resolves, but now serves the generic "Strategie Digitale Schweiz"
> landing page rather than any EMBAG-specific content, so it has been
> dropped rather than re-cited misleadingly. The long-standing "no Fedlex
> citation" gap is partly closed: the official text is at
> `fedlex.admin.ch/eli/cc/2023/682/de`, found via an outbound
> link on bfs.admin.ch's own OGD page — but Fedlex renders client-side in
> JavaScript, so this pass could retrieve it (200) without reading it. A
> genuine new connection was also found this pass: see "No relationships
> asserted" below.
>
> **Closed 2026-09-19** (`discovery/unresolved.md` row #113, alongside
> [[CH-REVDSG]]). Fedlex's pdf-a filestore path for this act's own
> in-force date — `eli/cc/2023/682/20240101/de/pdf-a/...` — was tried
> directly (constructed from the already-known 1 January 2024 commencement
> date rather than guessed blind) and returned the actual statute text,
> read locally as page images since WebFetch again returned only binary
> stream content for it.

## Description

Confirmed by reading netzwoche.ch directly (2026-08-22): "Das
'Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von
Behördenaufgaben' (Embag) soll Anfang 2024 in Kraft treten." The EMBAG creates the legal basis for the digital transformation of the
Swiss federal administration and for collaboration between authorities at
different levels of government and with third parties. Its stated principle
is **"digital first"** for federal business processes.

## Read directly at last — 2026-09-19

Fedlex's own pdf-a text, read directly for the first time, gives the
statute's title page: **"Bundesgesetz über den Einsatz elektronischer
Mittel zur Erfüllung von Behördenaufgaben (EMBAG), SR 172.019, vom
17. März 2023 (Stand am 1. Januar 2024)"** — adopted **17 March 2023**,
consolidated to the **1 January 2024** commencement date already carried
in `start_date`. Article 1 confirms its purpose (enabling cross-government
collaboration and the expansion of electronic-means use); Article 2
confirms the scope this entity's `applies-in` evidence already carried
from netzwoche.ch — "Dieses Gesetz gilt für die zentrale
Bundesverwaltung" (this act applies to the central federal
administration) — and a footnoted paragraph 2, marked "Noch nicht in
Kraft" (not yet in force), corroborates the staged commencement for other
bodies this entity already records via netzwoche.ch's reporting.

## The Atlas's first statutory open-source mandate

This is why the entity matters beyond Switzerland.

The EMBAG requires federal authorities to make **new software developments
available as open source software** — the *"Public Money – Public Code"*
principle, written into a national statute rather than into a policy or a
strategy.

The Atlas holds open data instruments for every country: [[EU-OPEN-DATA-DIRECTIVE]]
and its transpositions ([[NL-WHO]], [[DE-DNG]], [[BE-HERGEBRUIK-WET]]). It
holds **no other law that obliges a public administration to publish its
software.** Open data and open *code* are different obligations, and until
now the Atlas only recorded the first.

## Two commencement dates

| Date | Scope |
|---|---|
| **1 January 2024** | Central administrative units of the federal government |
| **May 2025** | Decentralised units — **not independently re-confirmed 2026-08-22** |

`start_date` records the first. Staged commencement by *organisational
scope* rather than by subject matter is unusual in this Atlas — compare
[[GB-DUAA]], staged by provision, and [[NL-TWCO]], which is time-limited.

## One of two obvious edges is now asserted

The obvious edges are to [[CH-OPENDATA-SWISS]] — the federal open data
portal, which this act's open government data provisions plainly concern —
and to [[CH-DVS]].

**The first is now sourced.** Confirmed by reading bfs.admin.ch's own "Open
Government Data (OGD)" page directly (2026-08-22): "Der Masterplan OGD
2024−2027 ... zielt darauf ab, die Daten der öffentlichen Verwaltung gemäss
dem [EMBAG] frei zugänglich zu machen. Die Geschäftsstelle OGD ... betreibt
das Portal opendata.swiss." The OGD office that operates opendata.swiss
states directly that it does so pursuant to the EMBAG. [[CH-OPENDATA-SWISS]]
now carries `governed-by` this entity on that basis.

**The second is not.** No source read connects [[CH-DVS]] to the EMBAG by
name beyond DVS's own blog post *about* the act, which is evidence of
interest, not evidence of a role under it. That edge remains unasserted and
is logged in `discovery/unresolved.md`.

## Not modelled

- **EMBAV**, the accompanying ordinance.
- The act's **collaboration provisions** between Confederation, cantons and
  communes — the part most relevant to the `level: local` question the Atlas
  has open.

## Sources

Listed in frontmatter, all five read directly in the 2026-08-22 pass
(Fedlex retrieved but not readable at that time). **The Fedlex pdf-a text
is now read directly** (2026-09-19) — see "Read directly at last" above.
