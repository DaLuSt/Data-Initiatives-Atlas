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
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
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
    evidence: "Confirmed by reading the DPA 2018 statute text at legislation.gov.uk (2026-08-22), Part 4, § 82(2): 'In this Part, \"intelligence service\" means— (a) the Security Service; (b) the Secret Intelligence Service; (c) the Government Communications Headquarters.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: governed-by
    target: GB-ISA-1994
    source: fact
    evidence: "Confirmed by reading the ISA 1994 statute text at legislation.gov.uk (2026-08-22), § 3(1): 'There shall continue to be a Government Communications Headquarters ... and ... its functions shall be— (a) to monitor, make use of or interfere with electromagnetic, acoustic and other emissions and any equipment producing such emissions and to obtain and provide information derived from or related to such emissions.'"
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "Confirmed by reading gchq.gov.uk's 'Legal Framework' page and the IPA 2016 statute text at legislation.gov.uk (2026-08-22): the Act's long title covers 'the interception of communications, equipment interference and the acquisition and retention of communications data, bulk personal datasets and other information', enacted 29 November 2016, and GCHQ's own page places this regime at the centre of its governance."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Legal Framework"
    url: "https://www.gchq.gov.uk/section/governance/legal-framework"
    publisher: "Government Communications Headquarters (GCHQ)"
    accessed: "2026-08-22"
  - title: "Britain enters a new era of online opportunity with opening of the National Cyber Security Centre"
    url: "https://www.gchq.gov.uk/news/britain-enters-new-era-online-opportunity-opening-ncsc"
    publisher: "Government Communications Headquarters (GCHQ)"
    accessed: "2026-08-22"
  - title: "Intelligence Services Act 1994"
    url: "https://www.legislation.gov.uk/ukpga/1994/13"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-22"
---

# Government Communications Headquarters (GCHQ)

> **Verified 2026-08-22.** gchq.gov.uk's own "Legal Framework" page and the
> ISA 1994 and DPA 2018 statute texts at legislation.gov.uk were read
> directly and confirmed the claims below, verbatim in places.

## Description

Confirmed verbatim on gchq.gov.uk's "Legal Framework" page (2026-08-22):
"The Intelligence Services Act 1994 sets out GCHQ's function as a
foreign-focused signals intelligence agency. The Investigatory Powers Act
2016 provides a modernised framework to govern the use and oversight of
investigatory powers by law enforcement and the security and intelligence
agencies." GCHQ is the UK's **signals intelligence** and information assurance agency.
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
