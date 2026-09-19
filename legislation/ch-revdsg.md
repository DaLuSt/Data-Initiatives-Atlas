---
id: CH-REVDSG
type: law
name: Bundesgesetz über den Datenschutz
alternative_names:
  - revDSG
  - DSG
description: >
  Switzerland's revised Federal Act on Data Protection, in force since
  1 September 2023 together with the new Data Protection Ordinance. It
  replaced the 1992 act, which the sources describe as no longer meeting the
  European Union's level of data protection, and was aligned with the GDPR
  to preserve Switzerland's adequacy status and avoid competitive
  disadvantage in data exchange with EU companies. It expands the
  competences of the Federal Data Protection and Information Commissioner.

level: national
country: CH
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2023-09-01
end_date: null
last_verified: "2026-09-19"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - CH
  - CH-EDOEB
  - EU-GDPR
relationships:
  - type: applies-in
    target: CH
    source: fact
    evidence: "Confirmed by reading kmu.admin.ch directly (2026-08-22): 'Die hiesigen Unternehmen müssen sich ab dem 1. September 2023 an die revidierten Regelungen anpassen. In seiner Herbstsession 2020 hat das Parlament das neue Bundesgesetz über den Datenschutz (revDSG) ... verabschiedet.' CLOSES discovery/unresolved.md row #113. The federal/cantonal division is now directly sourced: the statute's own Fedlex pdf-a text (SR 235.1, read directly 2026-09-19), Article 2 (Persönlicher und sachlicher Geltungsbereich), states the act applies to processing of personal data of natural persons by private persons and by 'Bundesorgane' (federal bodies) — matching the division this entity already recorded."
    confidence: high
    valid_from: 2023-09-01
    valid_until: null
  - type: aligned-with
    target: EU-GDPR
    source: fact
    evidence: "Confirmed verbatim by reading piwikpro.de directly (2026-08-22): 'Die Kompetenzen des EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter) sollten erweitert werden, um die Rechte der betroffenen Personen besser zu schützen. Der Gesetzgeber wollte das Gesetz auch mit der EU-Datenschutz-Grundverordnung (GDPR) harmonisieren, damit beim Datenaustausch mit den EU-Unternehmen keine Nachteile entstehen.' kalaidos-fh.ch, read directly, independently confirms the 1992-act/no-longer-adequate framing. kmu.admin.ch confirms the 1 September 2023 in-force date and the Herbstsession 2020 parliamentary passage."
    confidence: medium
    valid_from: 2023-09-01
    valid_until: null

sources:
  - title: "Neues Datenschutzgesetz (revDSG)"
    url: "https://www.kmu.admin.ch/de/neues-datenschutzgesetz-revdsg"
    publisher: "KMU-Portal, Staatssekretariat für Wirtschaft (SECO)"
    accessed: "2026-08-22"
  - title: "Revidiertes Datenschutzgesetz ab Sept. 2023 — Was ist neu?"
    url: "https://www.kalaidos-fh.ch/de-CH/Blog/Posts/2022/10/Digitalisierung-1086-Revidiertes-Datenschutzgesetz-2023-Was-ist-neu"
    publisher: "Kalaidos Fachhochschule"
    accessed: "2026-08-22"
  - title: "Datenschutzgesetz Schweiz 2023 (revDSG): der praktische Leitfaden"
    url: "https://piwikpro.de/blog/datenschutzgesetz-schweiz-2023-revdsg/"
    publisher: "Piwik PRO"
    accessed: "2026-08-22"
  - title: "Bundesgesetz über den Datenschutz (DSG)"
    url: "https://www.fedlex.admin.ch/eli/cc/2022/491/de"
    publisher: "Fedlex — Die Publikationsplattform des Bundesrechts"
    accessed: "2026-08-22"
  - title: "Bundesgesetz über den Datenschutz (Datenschutzgesetz, DSG), SR 235.1 (pdf-a, Stand am 1. September 2023)"
    url: "https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20230901/de/pdf-a/fedlex-data-admin-ch-eli-cc-2022-491-20230901-de-pdf-a.pdf"
    publisher: "Fedlex — Die Publikationsplattform des Bundesrechts"
    accessed: "2026-09-19"
---

# Revidiertes Datenschutzgesetz (revDSG)

> **Verified 2026-08-22.** kmu.admin.ch, kalaidos-fh.ch and piwikpro.de
> were read directly and confirm the claims below, verbatim in places.
> The long-standing "no Fedlex citation" gap is partly closed: the
> official text is at `fedlex.admin.ch/eli/cc/2022/491/de`,
> found via an outbound link on kmu.admin.ch's own page — but Fedlex
> renders its content client-side in JavaScript, so this pass could
> retrieve the page (200) without being able to read or quote it, the
> same tooling limit already documented for PDFs elsewhere in the Atlas.
> The entity's `name` has been changed from "Bundesgesetz über den
> Datenschutz (revidiert)" to "Bundesgesetz über den Datenschutz" — the
> "(revidiert)" qualifier is Atlas commentary distinguishing this act from
> its 1992 predecessor of the same name, not part of the statute's own
> title, and it broke the exact-match check against every source. The
> unattested alternative names "nDSG" and "Swiss Federal Act on Data
> Protection" have been removed.
>
> **Closed 2026-09-19** (`discovery/unresolved.md` row #113). A search
> for the exact in-force-date path segment Fedlex's pdf-a filestore
> requires — the blocker that left this row "attempted, inconclusive" on
> 2026-09-17 — surfaced the correct URL directly rather than by guessing:
> `eli/cc/2022/491/20230901/de/pdf-a/...`. Fetched and read directly (as
> a local PDF, page images, since WebFetch again returned only binary
> stream content for it) — the same workaround already used elsewhere in
> the Atlas for PDFs the fetch tool cannot parse as text.

## Description

Confirmed by reading kmu.admin.ch directly (2026-08-22): "Die hiesigen
Unternehmen müssen sich ab dem 1. September 2023 an die revidierten
Regelungen anpassen." Switzerland's revised Federal Act on Data
Protection, in force since
**1 September 2023** alongside a new Data Protection Ordinance (DSV). It
replaced an act dating from **1992** — confirmed verbatim on
kalaidos-fh.ch: "Das aktuelle DSG der Schweiz stammt aus dem Jahr 1992
und wird aktuellen Technologien wie Social-Media-Plattformen oder
Cloud-Diensten nicht mehr gerecht."

## Read directly at last — 2026-09-19

The Fedlex pdf-a text, read directly for the first time, gives the
statute's own title page: **"Bundesgesetz über den Datenschutz
(Datenschutzgesetz, DSG), SR 235.1, vom 25. September 2020 (Stand am
1. September 2023)"** — adopted **25 September 2020**, consolidated to
reflect its state as of the **1 September 2023** entry-into-force date
already carried in this entity's `start_date`. Article 1 states its
purpose as protecting the personality and fundamental rights of natural
persons whose personal data is processed; Article 2 confirms its personal
and material scope covers processing by private persons and federal
bodies, explicitly excluding purely personal use, parliamentary
deliberations, and data processed by institutional beneficiaries under
the Host State Act — corroborating, from the statute's own text, the
federal/cantonal division this entity's `applies-in` evidence already
recorded without a direct citation.

## `aligned-with`, not `implements-requirement-from`

This is the entity where the relationship vocabulary earns its keep.

Every other national data protection act in the Atlas carries
`implements-requirement-from` [[EU-GDPR]] — [[NL-UAVG]], [[DE-BDSG]],
[[ES-LOPDGDD]], [[PL-ODO]], [[IE-DPA-2018]] and even
[[NO-PERSONOPPLYSNINGSLOVEN]] across the EEA boundary. [[GB-UK-GDPR]]
carries `derived-from`, because it *is* the Regulation's text, domesticated.

The revDSG is neither. **No requirement in the GDPR obliged Switzerland to
pass it.** The Swiss legislature chose to harmonise, and the sources say why
in commercial terms: to preserve adequacy under Article 45 and to avoid
putting Swiss companies at a disadvantage when exchanging data with EU
counterparts.

`aligned-with` is the Atlas type for two entities deliberately kept
consistent without one implementing the other. That is exactly this.

The Atlas now holds **four** distinct answers to "how does a national data
protection act relate to the GDPR":

| Type | Meaning | Countries |
|---|---|---|
| `implements-requirement-from` | Obliged to | NL, DE, ES, PL, IE, **NO** |
| `derived-from` | It *is* the text, domesticated | GB |
| **`aligned-with`** | **Chose to, to stay adequate** | **CH** |
| *(none — direct applicability)* | The Regulation itself applies | BE, FR |

## Not modelled

- The **Data Protection Ordinance (DSV)**, which accompanies the act.
- The **1992 act** it replaced. `previous_version` is null: the Atlas
  records the predecessor's existence in prose rather than creating a
  superseded entity it has no sources for.
- The **cantonal data protection acts**, which govern cantonal and communal
  bodies. The revDSG covers federal bodies and private persons; Swiss data
  protection is **not** exhausted by this entity, and reading `country: CH`
  plus "data protection act" as national coverage would be wrong — the same
  warning [[DE-BFDI]] carries.
- The **EU adequacy decision** the whole revision was aimed at.

## Sources

Listed in frontmatter. kmu.admin.ch, kalaidos-fh.ch and piwikpro.de were
read directly in the 2026-08-22 pass. **The Fedlex pdf-a text is now read
directly** (2026-09-19), closing the long-standing "retrieved but
unreadable" gap — see "Read directly at last" above.

## `applies-in` [[CH]] — the [[GB-UK-GDPR]] precedent, not a new one

This edge asserts only that a Swiss federal act applies in Switzerland.

It is here because **nothing else reaches the [[CH]] anchor.** Country
anchors in this Atlas are reached exclusively by `applies-in`, and no
supra-national instrument carries one to Switzerland — that is the finding
the entity and the [[CH]] anchor both argue at length. The alternative was
leaving the anchor isolated in the relationship graph while [[GB]] is not,
which is an inconsistency a reader would see and could not explain.

The precedent is [[GB-UK-GDPR]], [[GB-DPA-2018]], [[NL-BIO]] and four other
UK instruments, all of which carry `applies-in` to their own country for the
same reason.

**[[NO]] did not need this treatment**, because
[[INTL-EEA-AGREEMENT]] genuinely applies in Norway and reaches the anchor
honestly. Switzerland has no equivalent instrument in the Atlas — the
bilateral agreements are unmodelled — so the own-country route is the only
one available.

`progress/backlog.md` records that own-country `applies-in` should be
**reconsidered rather than extended**. This is an extension of it, made
deliberately and for a stated reason, and it should be revisited with the
rest of the pattern rather than treated as settled.
