---
id: CH-REVDSG
type: law
name: Bundesgesetz über den Datenschutz (revidiert)
alternative_names:
  - revDSG
  - nDSG
  - DSG
  - Swiss Federal Act on Data Protection
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
verification: search-only

start_date: 2023-09-01
end_date: null
last_verified: "2026-08-18"
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
    evidence: "The revised Federal Act on Data Protection is a Swiss federal act, in force throughout Switzerland since 1 September 2023 together with the new Data Protection Ordinance; it governs the processing of personal data by federal bodies and by private persons (kmu.admin.ch 'Neues Datenschutzgesetz (revDSG)'; kalaidos-fh.ch; edoeb.admin.ch). NOT READ — search-only. Cantonal and communal bodies are governed by cantonal data protection acts, not by this one."
    confidence: medium
    valid_from: 2023-09-01
    valid_until: null
  - type: aligned-with
    target: EU-GDPR
    source: fact
    evidence: "The revised Datenschutzgesetz came into force on 1 September 2023, replacing an act dating from 1992 which was no longer up to date and did not meet the EU's level of data protection; the legislator wanted to harmonise the law with the GDPR to prevent competitive disadvantages in data exchange with EU companies, and the revision was driven by the need to maintain Switzerland's adequacy status under GDPR Article 45 (kmu.admin.ch 'Neues Datenschutzgesetz (revDSG)'; kalaidos-fh.ch 'Revidiertes Datenschutzgesetz ab Sept. 2023'; piwikpro.de 'Datenschutzgesetz Schweiz 2023 (revDSG)'). NOT READ — search-only."
    confidence: medium
    valid_from: 2023-09-01
    valid_until: null

sources:
  - title: "Neues Datenschutzgesetz (revDSG)"
    url: "https://www.kmu.admin.ch/de/neues-datenschutzgesetz-revdsg"
    publisher: "KMU-Portal, Staatssekretariat für Wirtschaft (SECO)"
  - title: "Revidiertes Datenschutzgesetz ab Sept. 2023 — Was ist neu?"
    url: "https://www.kalaidos-fh.ch/de-CH/Blog/Posts/2022/10/Digitalisierung-1086-Revidiertes-Datenschutzgesetz-2023-Was-ist-neu"
    publisher: "Kalaidos Fachhochschule"
  - title: "Datenschutzgesetz Schweiz 2023 (revDSG): der praktische Leitfaden"
    url: "https://piwikpro.de/blog/datenschutzgesetz-schweiz-2023-revdsg/"
    publisher: "Piwik PRO"
---

# Revidiertes Datenschutzgesetz (revDSG)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

Switzerland's revised Federal Act on Data Protection, in force since
**1 September 2023** alongside a new Data Protection Ordinance (DSV). It
replaced an act dating from **1992**.

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

Listed in frontmatter. **Only the KMU-Portal citation is a federal source**,
and no Fedlex citation for the act text was returned by search. For an
entity carrying this much comparative weight that is the weakest point, and
it should be re-sourced against `fedlex.admin.ch` first.

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
