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
verification: primary-source

start_date: 2018-05-25
end_date: null
last_verified: "2026-08-27"
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
    evidence: "Confirmed by reading gesetze-im-internet.de's own official text directly (2026-08-27) — closing this entity's previously-flagged missing-official-citation gap: the BDSG's own Section 1(5) states 'Die Vorschriften dieses Gesetzes finden keine Anwendung, soweit das Recht der Europäischen Union, im Besonderen die Verordnung (EU) 2016/679 in der jeweils geltenden Fassung, unmittelbar gilt' (this law's provisions do not apply where EU law, in particular Regulation (EU) 2016/679, directly applies) — the GDPR-precedence mechanism stated in the law's own text. The official text also confirms enactment on 30 June 2017 and entry into force on 25 May 2018 ('Es ist gem. Art. 8 Abs. 1 Satz 1 dieses G am 25.5.2018 in Kraft getreten'). dsgvo-gesetz.de, also read directly, confirms adoption as part of the DSAnpUG-EU. activemind.de, also read directly, confirms the supplementary relationship and names specific opening clauses (Art. 37(4), Art. 88 GDPR) but does NOT confirm a total count of roughly 70 opening clauses — that figure remains as previously sourced to unread pages, not independently confirmed this pass."
    confidence: high
    valid_from: 2018-05-25
    valid_until: null

sources:
  - title: "Bundesdatenschutzgesetz (BDSG) — official text"
    url: "https://www.gesetze-im-internet.de/bdsg_2018/BJNR209710017.html"
    publisher: "Bundesministerium der Justiz (Gesetze im Internet)"
    accessed: "2026-08-27"
  - title: "BDSG — Bundesdatenschutzgesetz"
    url: "https://dsgvo-gesetz.de/bdsg/"
    publisher: "dsgvo-gesetz.de (Intersoft Consulting)"
    accessed: "2026-08-27"
  - title: "Das neue Bundesdatenschutzgesetz (BDSG) und Konkretisierungen der DSGVO"
    url: "https://www.activemind.de/magazin/bdsg/"
    publisher: "activeMind AG"
    accessed: "2026-08-27"
  - title: "BDSG-neu — Das neue Bundesdatenschutzgesetz"
    url: "https://www.e-recht24.de/datenschutz/13173-bdsg-neu.html"
    publisher: "eRecht24"
  - title: "Das neue Bundesdatenschutzgesetz"
    url: "https://www2.deloitte.com/dl/de/pages/legal/articles/neues-bundesdatenschutzgesetz.html"
    publisher: "Deloitte Legal Deutschland"
---

# Bundesdatenschutzgesetz (BDSG)

> **Verified 2026-08-27.** Three of five cited pages were read directly,
> closing this entity's previously-flagged weakest point: no official
> Gesetze-im-Internet or Bundesgesetzblatt citation existed. It now does
> — the BDSG's own official text was read directly, and its own Section
> 1(5) states the GDPR-precedence mechanism in these words.

## Description

The BDSG — often "BDSG-neu" to distinguish it from the pre-2018 act — was
**enacted on 30 June 2017** and adopted as part of the *Datenschutz-Anpassungs-
und -Umsetzungsgesetz EU* (DSAnpUG-EU), applying since **25 May 2018**, the
day the GDPR became applicable — both dates confirmed by reading the BDSG's
own official text directly.

The sources are emphatic about what it is not: it **cannot be regarded as
an independent and complete law**. It concretises and supplements EU data
protection law. Confirmed in the BDSG's own words at Section 1(5): its
provisions do not apply "soweit das Recht der Europäischen Union, im
Besonderen die Verordnung (EU) 2016/679 ... unmittelbar gilt" (where EU
law, in particular the GDPR, directly applies) — [[EU-GDPR]] always takes
precedence, and the BDSG supplements it only where an opening clause
expressly permits.

Those opening clauses are the reason it exists. The sources describe the
GDPR as containing roughly **70 Öffnungsklauseln** — some partial, some
facultative, some mandatory — through which certain matters are to be
regulated at national level. **That specific count was not confirmed by
any page read this pass**: activemind.de, read directly, names individual
examples (Article 37(4), Article 88 GDPR) without giving a total, and
neither the official text nor dsgvo-gesetz.de states a figure. The count
remains as previously sourced to pages not read this pass.

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

Listed in frontmatter, three of five read directly this pass: the BDSG's
own official text at Gesetze im Internet — closing the previously-flagged
gap of no government citation — plus dsgvo-gesetz.de and activemind.de.
`e-recht24.de` and the Deloitte Legal article were not re-fetched.
