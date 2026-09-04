---
id: PL-DCAT-AP-PL
type: standard
name: DCAT-AP-PL
alternative_names:
  - Polish DCAT Application Profile
description: >
  Polish national application profile of the DCAT vocabulary, guiding
  Polish data publishers on how to specify their data catalogues and
  portal managers on how to process them in a way that keeps
  interoperability with the EU's own DCAT-AP assured. Its own
  documentation states it is a subprofile of DCAT-AP, replicating that
  profile's core structure and concepts, and is copyrighted to KPRM
  (Kancelaria Prezesa Rady Ministrów, the Chancellery of the Prime
  Minister). It is published on dane.gov.pl, the Polish national open
  data portal.

level: national
country: PL
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-04"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - PL-DANE-GOV-PL
relationships:
  - type: based-on
    target: EU-DCAT-AP
    source: fact
    evidence: "Confirmed by reading dane.gov.pl's own DCAT-AP-PL 'Introduction' page directly (2026-09-04): 'DCAT-AP-PL is an Application Profile of the DCAT vocabulary and a Subprofile of the European Application Profile DCAT-AP,' defined so that Polish publishers' catalogues remain interoperable with DCAT-AP, and stated to replicate DCAT-AP's own core structure and concepts."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Introduction — DCAT-AP-PL"
    url: "https://dane.gov.pl/dcat-ap-pl/introduction/"
    publisher: "dane.gov.pl (Kancelaria Prezesa Rady Ministrów)"
    accessed: "2026-09-04"
---

# DCAT-AP-PL

> **Added 2026-09-04, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had asked whether Poland has a DCAT
> application profile alongside the Dutch, German, Belgian and Spanish
> ones already modelled. `dane.gov.pl`'s own documentation page was
> read directly this pass.

## Description

DCAT-AP-PL guides Polish data publishers on specifying their data
catalogues, and portal managers on processing them, so that
interoperability with the EU's own **DCAT-AP** is assured. Reading
`dane.gov.pl`'s own documentation directly: **"DCAT-AP-PL is an
Application Profile of the DCAT vocabulary and a Subprofile of the
European Application Profile DCAT-AP,"** replicating that profile's
core structure and concepts.

The documentation's own footer is copyrighted to **KPRM** — the
Kancelaria Prezesa Rady Ministrów, the Chancellery of the Prime
Minister — without further stating KPRM's operational role. It is
published on `dane.gov.pl`, the same portal [[PL-DANE-GOV-PL]]'s own
entity records as `maintained-by` [[PL-MC]]; no `maintained-by` edge is
asserted from this entity, because no source read connects the
standard's own stewardship to either body specifically.

## A fifth national DCAT-AP child

[[EU-DCAT-AP]] now has five national profiles in the Atlas: Dutch
([[NL-DCAT-AP-NL]]), German ([[DE-DCAT-AP-DE]]), Belgian
([[BE-DCAT-AP-BE]]), Spanish (carried on [[ES-NTI-RISP]]) and now
Polish.

## Relationships

- `based-on` [[EU-DCAT-AP]].

## Sources

Listed in frontmatter, read directly this pass.
