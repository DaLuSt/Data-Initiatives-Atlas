---
id: DE-BDSG
type: law
name: Bundesdatenschutzgesetz
alternative_names:
  - BDSG
  - "BDSG-neu"
  - Federal Data Protection Act
description: >
  German federal data protection act, adopted as part of the
  Datenschutz-Anpassungs- und -Umsetzungsgesetz EU (DSAnpUG-EU) and
  applicable since 25 May 2018 alongside the GDPR. It supplements and
  concretises the GDPR where the regulation's opening clauses
  (Öffnungsklauseln) permit member states to legislate, and is not a
  self-standing or complete data protection code.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2018-05-25
end_date: null
last_verified: null
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-GDPR
  - NL-UAVG
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "The BDSG was adopted as part of the Datenschutz-Anpassungs- und -Umsetzungsgesetz EU and has applied since 25 May 2018 together with the GDPR; it supplements and concretises the GDPR, which contains roughly 70 opening clauses allowing national legislators to regulate certain matters at member-state level. The GDPR takes precedence and the BDSG supplements it only where opening clauses expressly permit (dsgvo-gesetz.de/bdsg; activemind.de; e-recht24.de). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "BDSG — Bundesdatenschutzgesetz"
    url: "https://dsgvo-gesetz.de/bdsg/"
    publisher: "dsgvo-gesetz.de (Intersoft Consulting)"
  - title: "Das neue Bundesdatenschutzgesetz (BDSG) und Konkretisierungen der DSGVO"
    url: "https://www.activemind.de/magazin/bdsg/"
    publisher: "activeMind AG"
  - title: "BDSG-neu — Das neue Bundesdatenschutzgesetz"
    url: "https://www.e-recht24.de/datenschutz/13173-bdsg-neu.html"
    publisher: "eRecht24"
  - title: "Das neue Bundesdatenschutzgesetz"
    url: "https://www2.deloitte.com/dl/de/pages/legal/articles/neues-bundesdatenschutzgesetz.html"
    publisher: "Deloitte Legal Deutschland"
---

# Bundesdatenschutzgesetz (BDSG)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The BDSG — often "BDSG-neu" to distinguish it from the pre-2018 act — was
adopted as part of the *Datenschutz-Anpassungs- und -Umsetzungsgesetz EU*
(DSAnpUG-EU) and has applied since **25 May 2018**, the day the GDPR became
applicable.

The sources are emphatic about what it is not: it **cannot be regarded as
an independent and complete law**. It concretises and supplements EU data
protection law. [[EU-GDPR]] always takes precedence, and the BDSG
supplements it only where an opening clause expressly permits.

Those opening clauses are the reason it exists. The GDPR contains roughly
**70 Öffnungsklauseln** — some partial, some facultative, some mandatory —
through which certain matters are to be regulated at national level.

## The country-neutrality test, in one entity

This is the entity the whole Germany batch was built to produce.

[[EU-GDPR]] is **one** Atlas entity. It is now implemented by **two**
national acts:

```
                    EU-GDPR
                   /        \
   implements-requirement-from
                 /            \
          NL-UAVG              DE-BDSG
```

and it carries `applies-in` relationships to **both** [[NL]] and [[DE]].

What did *not* happen is the point. There is no `DE-EU-GDPR`. There is no
German copy of the regulation, no German fork of its text, and no
country-prefixed duplicate of any EU instrument anywhere in this batch —
the pattern README §16 forbids and `validation/audit.py` actively scans for.
Adding a second country required no ontology change, no new relationship
type, and no new folder.

The same structure now holds four times over: [[EU-NIS2]] →
[[NL-CBW]] / [[DE-NIS2UMSUCG]], [[EU-OPEN-DATA-DIRECTIVE]] →
[[NL-WHO]] / [[DE-DNG]], and [[EU-ITS-DIRECTIVE]] → [[NL-NTM]] /
[[DE-MOBILITHEK]].

## A comparison the Atlas can now make and could not before

[[NL-UAVG]] and the BDSG are the same instrument type doing the same job in
two member states. **No relationship is asserted between them** — they are
siblings, not relatives, and `related-to` between national implementations
of the same EU act would be an Atlas inference dressed as a fact.

Both are reachable from [[EU-GDPR]], which is the correct route: the thing
they genuinely share is their parent.

## Sources

Listed in frontmatter. **All four are commercial legal-information
publishers** — a law-firm magazine, two legal-tech sites and a Big Four
legal practice. None is a government source, and **no Gesetze-im-Internet
or Bundesgesetzblatt URL is cited**, because none was returned by search.

For an entity that carries this much structural weight, that is the
weakest part of the record and it should be the first German entity
re-sourced when page retrieval is possible.
