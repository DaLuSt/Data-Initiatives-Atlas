---
id: GB-GCHQ
type: organisation
name: Government Communications Headquarters
alternative_names:
  - GCHQ
description: >
  The United Kingdom's signals intelligence and information assurance
  agency. The Intelligence Services Act 1994 sets out its function as a
  foreign-focused signals intelligence agency and placed it on a statutory
  basis alongside SIS. The National Cyber Security Centre is part of GCHQ,
  and its use of investigatory powers is governed by the Investigatory
  Powers Act 2016.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - GB-ISA-1994
  - GB-IPA-2016
  - GB-DPA-2018
  - GB-NCSC
  - GB-SIS
  - GB-MI5
  - GB-IPCO
  - GB-ISC
relationships:
  - type: governed-by
    target: GB-DPA-2018
    source: fact
    evidence: "Part 4 of the Data Protection Act 2018 is separate from the UK GDPR regime and sets out a data protection regime for intelligence services processing; the intelligence services are the Security Service (MI5), the Secret Intelligence Service (MI6) and GCHQ, and all processing of personal data they undertake is governed by Part 4 (ico.org.uk 'Guide to Intelligence Services Processing' and 'Scope and key definitions'; assets.publishing.service.gov.uk 'Data Protection Act 2018 Factsheet — Intelligence services processing'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GB-ISA-1994
    source: fact
    evidence: "The Intelligence Services Act 1994 establishes and regulates the Secret Intelligence Service and the Government Communications Headquarters, providing a statutory basis for their activities, and sets out GCHQ's function as a foreign-focused signals intelligence agency (legislation.gov.uk ukpga/1994/13; gchq.gov.uk 'Legal Framework'; en.wikipedia.org 'Intelligence Services Act 1994'). NOT READ — search-only."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "The Investigatory Powers Act 2016 provides a modernised framework to govern the use and oversight of investigatory powers by law enforcement and the security and intelligence agencies; GCHQ publishes its legal framework covering these acts (gchq.gov.uk 'Legal Framework'; legislation.gov.uk ukpga/2016/25; ipco.org.uk). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Legal Framework"
    url: "https://www.gchq.gov.uk/section/governance/legal-framework"
    publisher: "Government Communications Headquarters (GCHQ)"
  - title: "Britain enters a new era of online opportunity with opening of the National Cyber Security Centre"
    url: "https://www.gchq.gov.uk/news/britain-enters-new-era-online-opportunity-opening-ncsc"
    publisher: "Government Communications Headquarters (GCHQ)"
  - title: "Intelligence Services Act 1994"
    url: "https://www.legislation.gov.uk/ukpga/1994/13"
    publisher: "The National Archives (legislation.gov.uk)"
---

# Government Communications Headquarters (GCHQ)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

GCHQ is the UK's **signals intelligence** and information assurance agency.
[[GB-ISA-1994]] sets out its function as a foreign-focused signals
intelligence agency and placed it on a statutory basis alongside
[[GB-SIS]].

## The entity that connects this batch to the Atlas that already existed

[[GB-NCSC]] — the National Cyber Security Centre — has been an Atlas entity
since the UK batch, where it appears as the UK's technical cyber-security
authority, `produces` [[GB-CAF]], and is explicitly *not* the NIS competent
authority (that is [[GB-OFCOM]] and [[GB-ICO]]).

**The NCSC is part of GCHQ.** It was established in October 2016, bringing
together CESG — GCHQ's own information security arm — with the Centre for
the Protection of National Infrastructure, CERT-UK and the Centre for Cyber
Assessment.

That single edge, asserted on [[GB-NCSC]], is what makes the UK's cyber
governance legible: the body that writes the UK's cyber assessment framework
and advises industry is a component of a **signals intelligence agency**.
Every other country in the Atlas separates these — [[FR-ANSSI]] is not part
of [[FR-DGSE]], [[DE-BSI]] is under [[DE-BMI]] not [[DE-BND]], [[BE-CCB]] is
not part of [[BE-ADIV]].

Spain is the one partial exception, and it goes the same way as the UK:
[[ES-CCN]] is `part-of` [[ES-CNI]].

So the Atlas now records **two** countries whose national cyber-security
authority sits inside an intelligence service, and five that keep them
apart. That comparison could not be made before this batch, because the
intelligence side of it did not exist.

## Two domains

This is the only entity in the batch carrying both
[[DOMAIN-NATIONAL-SECURITY]] and [[DOMAIN-CYBERSECURITY]], for the reason
above. [[GB-NCSC]] keeps only its cyber-security domain: it is a
cyber-security body that happens to sit inside an intelligence agency, not
an intelligence service in its own right.

## Relationships

- `governed-by` [[GB-ISA-1994]], [[GB-IPA-2016]] and [[GB-DPA-2018]] (Part 4).

The `part-of` edge runs **from** [[GB-NCSC]] **to** this entity, and is
asserted there — the Atlas never mirrors a relationship onto both ends.

## Sources

Listed in frontmatter.
