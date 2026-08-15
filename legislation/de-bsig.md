---
id: DE-BSIG
type: law
name: BSI-Gesetz
alternative_names:
  - BSIG
  - Gesetz über das Bundesamt für Sicherheit in der Informationstechnik
  - Act on the Federal Office for Information Security
description: >
  German federal act constituting the Bundesamt für Sicherheit in der
  Informationstechnik and defining the scope of its tasks, including its
  role under § 4 BSIG as the central reporting point for IT security. It
  was substantially expanded by the IT-Sicherheitsgesetz in 2015 and
  comprehensively revised by the NIS-2-Umsetzungsgesetz with effect from
  6 December 2025.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - DE-BSI
related_entities:
  - DE-NIS2UMSUCG
relationships: []

sources:
  - title: "Gesetz über das Bundesamt für Sicherheit in der Informationstechnik (BSI-Gesetz — BSIG)"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/Gesetze-und-Verordnungen/BSI-Gesetz/bsi-gesetz_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  - title: "BSI — Auftrag"
    url: "https://www.bsi.bund.de/DE/Das-BSI/Auftrag/auftrag_node.html"
    publisher: "Bundesamt für Sicherheit in der Informationstechnik (BSI)"
  - title: "NIS2-Umsetzungsgesetz in Deutschland 2025"
    url: "https://www.openkritis.de/it-sicherheitsgesetz/nis2-umsetzung-gesetz-cybersicherheit.html"
    publisher: "OpenKRITIS"
  - title: "Umsetzung der EU-Direktive NIS2 in Deutschland (NIS2-Umsetzungsgesetz)"
    url: "https://www.deloitte.com/de/de/services/consulting-risk/perspectives/umsetzung-eu-direktive-nis2-nis2umsucg.html"
    publisher: "Deloitte Deutschland"
---

# BSI-Gesetz (BSIG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BSIG constitutes [[DE-BSI]] and defines the scope of its tasks. Under
**§ 4 BSIG** the BSI acts as the central reporting point for IT security,
collecting and evaluating information on vulnerabilities, malware and
attack patterns.

Two expansions are sourced:

- The **IT-Sicherheitsgesetz**, in force from 2015, significantly widened
  the BSI's tasks and powers.
- [[DE-NIS2UMSUCG]] **comprehensively revised** the BSIG with effect from
  6 December 2025, in preference to enacting a separate NIS2 statute.

`coverage: low`: the act's structure, its date of original enactment and
its substantive obligations are not recorded, because no source read states
them. What is recorded is its relationship to the BSI and to the NIS2
transposition.

## Why this entity is `status: active` while something `supersedes` it

[[DE-NIS2UMSUCG]] carries a `supersedes` relationship pointing here, and
this entity is nevertheless `active` rather than `superseded`. That is a
deliberate inconsistency, not an oversight.

The BSIG was **amended, not repealed**. It continues in force under its own
name with substantially new content. The `supersedes` relationship is a
poor fit recorded at `confidence: low` for want of an amendment-lineage
relationship type; setting this entity to `superseded` to match it would
compound a modelling compromise into a false statement about German law.

Where the Atlas has a genuine supersession it says so on both sides —
[[NL-WBNI]] is `superseded` and [[NL-CBW]] `supersedes` it; [[DE-IWG]] is
`superseded` and [[DE-DNG]] `supersedes` it. The absence of that pairing
here is the signal that this case is different.

The full reasoning, and the relationship-type question it raises, is set
out in [[DE-NIS2UMSUCG]] and logged in `discovery/unresolved.md`.

## Relationships

**None asserted from this entity.** It is reached from [[DE-BSI]]
(`governed-by`) and from [[DE-NIS2UMSUCG]] (`supersedes`).

## Sources

Listed in frontmatter.
