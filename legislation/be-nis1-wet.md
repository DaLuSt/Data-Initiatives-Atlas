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
  public safety, transposing Directive (EU) 2016/1148 (the original NIS
  Directive). Published in the Belgisch Staatsblad on 3 May 2019. Replaced
  by the NIS2 act of 26 April 2024 with effect from 18 October 2024.
  Retained in the Atlas as a superseded entity so the Belgian cybersecurity
  lineage remains traceable.

level: national
country: BE
region: EU

status: superseded
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: 2024-10-18
last_verified: "2026-08-26"
previous_version: null
successor: BE-NIS2-WET

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - BE-NIS2-WET
  - EU-NIS
relationships:
  - type: implements-requirement-from
    target: EU-NIS
    source: fact
    evidence: "Confirmed by reading the act's own text at etaamb.openjustice.be directly (2026-08-26), closing a gap this entity had flagged since the Belgium batch: Article 2 states 'Deze wet voorziet met name in de omzetting van de Europese Richtlijn (EU) 2016/1148' — this act specifically transposes European Directive (EU) 2016/1148 (the original NIS Directive). The act was promulgated 7 April 2019 and published in the Belgisch Staatsblad on 3 May 2019."
    confidence: high
    valid_from: 2019-05-03
    valid_until: 2024-10-18

sources:
  - title: "Entry into force of Belgian acts transposing NIS2: what you need to know"
    url: "https://www.eubelius.com/en/news/entry-into-force-of-belgian-acts-transposing-nis2-what-you-need-to-know"
    publisher: "Eubelius"
    accessed: "2026-08-26"
  - title: "De NIS2-wet"
    url: "https://ccb.belgium.be/nl/nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "NIS2 | CCB Belgium"
    url: "https://ccb.belgium.be/regulation/nis2"
    publisher: "Centrum voor Cybersecurity België (CCB)"
  - title: "Wet van 07/04/2019 tot vaststelling van een kader voor de beveiliging van netwerk- en informatiesystemen van algemeen belang voor de openbare veiligheid"
    url: "https://etaamb.openjustice.be/nl/wet-van-07-april-2019_n2019011507.html"
    publisher: "etaamb / OpenJustice (Belgisch Staatsblad)"
    accessed: "2026-08-26"
---

# NIS1-wet (Belgium, 7 April 2019)

> **Verified 2026-08-26.** The act's own text was read directly at
> etaamb.openjustice.be, closing the gap this entity had flagged since the
> Belgium batch — the original three sources, all about the successor
> NIS2 act, remain unread and say nothing about this act's own content.
> `verification: primary-source` on the strength of the act's own text, the
> equivalent-strength direct evidence the re-verification rules allow when a
> majority of the original citations cannot be reached.

## Description

The act of **7 April 2019** established a framework for the security of
network and information systems of general interest for public safety. It
was **promulgated 7 April 2019 and published in the Belgisch Staatsblad on
3 May 2019** (confirmed by reading its own text), and **replaced by
[[BE-NIS2-WET]]** with effect from 18 October 2024.

## The gap this entity flagged is now closed

Previously: *"No `implements-requirement-from` → [[EU-NIS]] is asserted,
though the 2019 date and the subject matter make it near-certain that this
act transposed the original NIS Directive... This is a link that one page
read would almost certainly close."*

That page was read this pass. The act's own **Article 2**, at
etaamb.openjustice.be: *"Deze wet voorziet met name in de omzetting van de
Europese Richtlijn (EU) 2016/1148"* — this law specifically implements
Directive (EU) 2016/1148, the original NIS Directive. `implements-
requirement-from` → [[EU-NIS]] is now recorded as a fact, giving the Atlas
a second `EU-NIS` → national descent.

## Why a thin entity is kept, and what is still thin

The entity exists because the Atlas retains superseded entities rather than
deleting them, and never reuses an ID. Without it, [[BE-NIS2-WET]]'s
`previous_version` would dangle and Belgium's cybersecurity lineage would
begin in 2024 with no sign that anything preceded it.

The same judgement produced [[NL-WBNI]], [[DE-IWG]], [[NL-WOB]],
[[NL-EAR]] and [[EU-NIS]]. **[[NL-WBNI]] is the exact parallel**: a
superseded national NIS act retained under its successor.

`coverage: low` remains: beyond the transposition fact and the publication
date, the act's substantive obligations — scope, designated authorities,
penalties — are still not recorded. The three original sources, all about
the NIS2 successor, were not re-fetched this pass; they say nothing about
this act's own content that the new reading does not already supersede.

## Relationships

- `implements-requirement-from` [[EU-NIS]] — new this pass, confirmed from
  the act's own text.
- Reached from [[BE-NIS2-WET]] via `supersedes` and `previous_version`.

## Sources

One of four read directly this pass — the act's own text, the source that
matters most for this entity's central claim. The three original sources
are all about the successor NIS2 act and remain unread.
