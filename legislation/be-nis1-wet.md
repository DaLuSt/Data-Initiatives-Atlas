---
id: BE-NIS1-WET
type: law
name: NIS1-wet
alternative_names:
  - Wet van 7 april 2019
  - Wet tot vaststelling van een kader voor de beveiliging van netwerk- en informatiesystemen van algemeen belang voor de openbare veiligheid
  - Loi du 7 avril 2019
description: >
  Former Belgian act of 7 April 2019 establishing a framework for the
  security of network and information systems of general interest for
  public safety. Replaced by the NIS2 act of 26 April 2024 with effect from
  18 October 2024. Retained in the Atlas as a superseded entity so the
  Belgian cybersecurity lineage remains traceable.

level: national
country: BE
region: EU

status: superseded
confidence: low
coverage: low
verification: search-only

start_date: null
end_date: 2024-10-18
last_verified: null
previous_version: null
successor: BE-NIS2-WET

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - BE-NIS2-WET
relationships: []

sources:
  - title: "Entry into force of Belgian acts transposing NIS2: what you need to know"
    url: "https://www.eubelius.com/en/news/entry-into-force-of-belgian-acts-transposing-nis2-what-you-need-to-know"
    publisher: "Eubelius"
  - title: "De NIS2-wet"
    url: "https://ccb.belgium.be/nl/nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "NIS2 | CCB Belgium"
    url: "https://ccb.belgium.be/regulation/nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
---

# NIS1-wet (Belgium, 7 April 2019)

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The act of **7 April 2019** established a framework for the security of
network and information systems of general interest for public safety. It
was **replaced by [[BE-NIS2-WET]]** with effect from 18 October 2024.

## Why a thin entity is kept

Almost nothing about this act is recorded: not its entry into force, not
its substance, not — recorded as a fact — that it transposed the original
NIS Directive. `confidence` and `coverage` are both `low`, honestly.

It exists because the Atlas retains superseded entities rather than
deleting them, and never reuses an ID. Without it, [[BE-NIS2-WET]]'s
`previous_version` would dangle and Belgium's cybersecurity lineage would
begin in 2024 with no sign that anything preceded it.

The same judgement produced [[NL-WBNI]], [[DE-IWG]], [[NL-WOB]],
[[NL-EAR]] and [[EU-NIS]]. **[[NL-WBNI]] is the exact parallel**: a
superseded national NIS act retained under its successor.

## What is deliberately not recorded

**No `implements-requirement-from` → [[EU-NIS]] is asserted**, though the
2019 date and the subject matter make it near-certain that this act
transposed the original NIS Directive — which *is* an Atlas entity, so
unlike [[DE-IWG]] the relationship would have somewhere to point.

It is refused anyway: every source cited here is about the **NIS2** act and
mentions this one only as the thing being replaced. None says what it
transposed. Asserting it would be inferring from a date, which is the
failure mode §21 of the original brief names.

This is a link that one page read would almost certainly close, and it
would give the Atlas a second `EU-NIS` → national descent. Logged in
`discovery/unresolved.md`.

## Relationships

**None asserted.** Reached from [[BE-NIS2-WET]] via `supersedes` and
`previous_version`.

## Sources

Listed in frontmatter — all three are sources about the successor act.
