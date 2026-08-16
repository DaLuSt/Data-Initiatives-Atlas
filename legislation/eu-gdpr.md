---
id: EU-GDPR
type: regulation
name: General Data Protection Regulation
alternative_names:
  - GDPR
  - Regulation (EU) 2016/679
  - Algemene verordening gegevensbescherming
  - AVG
description: >
  EU regulation on the protection of natural persons with regard to the
  processing of personal data and on the free movement of such data.
  Directly applicable across the Union; applicable from 25 May 2018.

level: regional
country: null
region: EU

status: active
confidence: low
coverage: low
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
  - NL-UAVG
  - NL-AP
  - EU-DIGITAL-OMNIBUS
relationships:
  - type: applies-in
    target: NL
    source: fact
    evidence: "As an EU regulation the GDPR is directly applicable in all member states; the Netherlands adopted the UAVG as implementing legislation, in force from the GDPR's date of application. NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null
  - type: applies-in
    target: DE
    source: fact
    evidence: "As an EU regulation the GDPR is directly applicable in all member states; Germany adopted the Bundesdatenschutzgesetz as part of the Datenschutz-Anpassungs- und -Umsetzungsgesetz EU, applicable since 25 May 2018, which supplements and concretises the GDPR where its opening clauses permit (dsgvo-gesetz.de/bdsg; activemind.de). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-05-25
    valid_until: null
  - type: applies-in
    target: BE
    source: fact
    evidence: "As an EU regulation the GDPR is directly applicable in all member states; Belgium adopted the wet van 30 juli 2018 as implementing legislation, in force from 5 September 2018, supplementing the GDPR where it left room for national legislators (ejustice.just.fgov.be ELI wet/2018/07/30; gegevensbeschermingsautoriteit.be). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-09-05
    valid_until: null

sources:
  - title: "General data protection regulation (GDPR) — summary"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/general-data-protection-regulation-gdpr.html"
    publisher: "EUR-Lex (Publications Office of the European Union)"
---

# General Data Protection Regulation (GDPR)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited page was confirmed to exist but was not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The GDPR — Regulation (EU) 2016/679 — governs the protection of natural
persons in relation to the processing of personal data and the free movement
of such data. It protects individuals when their data is processed by the
private sector and most of the public sector. It became applicable on
25 May 2018.

## Scope note

This is a deliberately **minimal EU anchor entity**, created in Batch 3
rather than Batch 8. Batch 3's scope explicitly includes "applicable
European legislation", and without this entity the Dutch implementation
chain — [[NL-UAVG]] → GDPR — could not be expressed at all, which is the
Atlas's central purpose. `coverage: low` reflects that it has not been
researched in its own right.

**Batch 8 reviewed but did not fully deepen this entity.** The full Official
Journal citation, legislative history, and the EDPB/EDPS relationships are
still outstanding — the latter awaiting Batch 9. `coverage` stays `low`.

## ⚠ Amendment proposed

[[EU-DIGITAL-OMNIBUS]] (19 November 2025) proposes to amend the GDPR,
notably by adding a lawful basis of legitimate interest for processing
personal data when developing or operating AI systems, subject to
safeguards. The proposal is reported to face strong opposition from data
protection authorities, NGOs and academics on exactly this point.

`status` remains `active` and unchanged — an amendment proposal changes
nothing until adopted.

## Relationships

- Applies in [[NL]], [[DE]] and [[BE]] — and in every other member state;
  those `applies-in` relationships are added as countries join the Atlas,
  per the country-neutral model.
- Implemented by three national acts: [[NL-UAVG]], [[DE-BDSG]] and
  [[BE-GDPR-WET]]. **This entity was not duplicated to accommodate any of
  them** — there is no `NL-EU-GDPR`, `DE-EU-GDPR` or `BE-EU-GDPR`, which is
  the whole point of the country-neutral model.
- [[NL-AP]] is the Dutch supervisory authority designated under it.
  [[BE-APD]] supervises the Belgian act. [[DE-BFDI]] supervises German
  federal bodies, but is *not* linked to [[DE-BDSG]] — no source read
  states it, and German supervision is split across the Länder.

## Sources

Listed in frontmatter. Note the cited source is a EUR-Lex *summary* page,
not the Official Journal text; Batch 8 should cite the authoritative text.
