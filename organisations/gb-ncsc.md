---
id: GB-NCSC
type: organisation
name: National Cyber Security Centre
alternative_names:
  - NCSC
description: >
  The United Kingdom's technical authority on cyber security. It is not a
  competent authority under the Network and Information Systems Regulations
  2018, but is expected to play a role in coordination between the
  sectoral competent authorities and in the dissemination of general
  guidance. It publishes the Cyber Assessment Framework, which the Cyber
  Security and Resilience Bill would place on a firmer statutory footing as
  the baseline standard for organisations in scope.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - GB-CAF
  - GB-NIS-REGULATIONS
  - GB-CSRB
  - DE-BSI
  - BE-CCB
  - FR-ANSSI
  - ES-CCN
  - GB-GCHQ
relationships:
  - type: part-of
    target: GB-GCHQ
    source: fact
    evidence: "Confirmed by reading ncsc.gov.uk's own 'What we do at the NCSC' page (2026-08-22): 'The National Cyber Security Centre, a part of GCHQ, helps businesses, the public sector and individuals protect the online services and devices that we all depend on.'"
    confidence: medium
    valid_from: 2016-10-01
    valid_until: null
  - type: produces
    target: GB-CAF
    source: fact
    evidence: "Confirmed by reading en.wikipedia.org's 'Cyber Assessment Framework' article (2026-08-22): 'The Cyber Assessment Framework (CAF) is a mechanism developed by the United Kingdom's National Cyber Security Centre (NCSC) in 2018 for overlooking the security of operations, to meet the Security of Network & Information Systems Regulations (NIS Regulations).'"
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "What we do at the NCSC"
    url: "https://www.ncsc.gov.uk/section/about-ncsc/what-we-do"
    publisher: "National Cyber Security Centre (UK)"
    accessed: "2026-08-22"
  - title: "The Network and Information Systems Regulations 2018: how will they apply in practice?"
    url: "https://www.osborneclarke.com/insights/the-network-and-information-systems-regulations-2018-how-will-they-apply-in-practice"
    publisher: "Osborne Clarke"
    accessed: "2026-08-22"
  - title: "Cyber Assessment Framework"
    url: "https://en.wikipedia.org/wiki/Cyber_Assessment_Framework"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
---

# National Cyber Security Centre

> **Verified 2026-08-22.** ncsc.gov.uk's own "What we do" page and
> en.wikipedia.org's "Cyber Assessment Framework" article were read
> directly and confirmed the claims below, including the CAF's founding
> year. The originally cited NCSC policy-statement PDF now 404s and
> `commonslibrary.parliament.uk` returns a bot-defense challenge; both were
> replaced or dropped rather than re-cited unread.

## Description

The NCSC is the UK's **technical authority** on cyber security. It publishes
the **Cyber Assessment Framework (CAF)**, and has warned of a widening gap
between the complexity of cyber threats and the UK's defensive capability in
critical national infrastructure.

## A national cyber authority that is deliberately not the regulator

This is what distinguishes the UK from every other country in
[[DOMAIN-CYBERSECURITY]].

| Country | Authority | Is it the NIS competent authority? |
|---|---|---|
| Germany | [[DE-BSI]] | yes |
| Belgium | [[BE-CCB]] | yes |
| France | [[FR-ANSSI]] | yes |
| Spain | [[ES-CCN]] + [[ES-INCIBE]] | split by audience |
| Netherlands | — | *no authority modelled* |
| Poland | — | *no authority modelled* |
| **United Kingdom** | **this entity** | **explicitly no** |

The UK took a **sector-by-sector approach**: [[GB-NIS-REGULATIONS]] names a
list of competent authorities in its Schedule 1 — the departments
responsible for energy, transport, health and drinking water, Ofcom for
digital infrastructure, and **[[GB-ICO]] for relevant digital service
providers**. The NCSC coordinates between them and issues guidance, and
regulates none of them.

So the Atlas now holds **three distinct arrangements**: one national body
that both advises and regulates (DE, BE, FR); two bodies split by audience
(ES); and one technical authority that is explicitly *not* a regulator, with
the regulatory function distributed across sectoral bodies (GB). Spain's
split looked like the outlier when it was written. It is now one of three
shapes, and the UK's is the only one where the data protection authority is
also a cyber regulator.

## `coverage: low`

The NCSC's founding, its relationship to GCHQ and its statutory basis if any
are unrecorded.

**The Cyber Assessment Framework is now modelled** — see [[GB-CAF]] — closing
what an earlier version of this entity called "the clearest single research
target in this batch". The UK now has a national baseline in the Atlas
alongside [[NL-BIO]], [[DE-IT-GRUNDSCHUTZ]] and [[ES-ENS]].

## Relationships

- `produces` [[GB-CAF]].

**Still nothing for the coordination role.** The NCSC's position under
[[GB-NIS-REGULATIONS]] is coordination without competence, and no
relationship type expresses "named in the statute as a coordinator without
regulatory power". [[GB-OFCOM]] and [[GB-ICO]] carry `applies-to` edges to
that instrument because they *are* competent authorities; the NCSC
deliberately carries none, and the absence is the accurate statement.

## Sources

Listed in frontmatter.

## The NCSC is part of GCHQ

Added with the intelligence-services batch: the NCSC is a **component of
[[GB-GCHQ]]**, the UK's signals intelligence agency. It was established in
October 2016 by merging CESG — GCHQ's own information security arm — with
the Centre for the Protection of National Infrastructure, CERT-UK and the
Centre for Cyber Assessment.

This is worth stating on this entity and not only on [[GB-GCHQ]], because
the rest of this file describes a body that publishes [[GB-CAF]], advises
industry and is explicitly *not* the NIS competent authority. All of that
remains true, and it is done from inside an intelligence agency.

Only one other country in the Atlas is arranged this way: [[ES-CCN]] is
`part-of` [[ES-CNI]]. Five keep the two functions apart — [[DE-BSI]] under
[[DE-BMI]], [[FR-ANSSI]] under the SGDSN, [[BE-CCB]], and the Dutch and
Polish arrangements.

The domain list here is unchanged: the NCSC keeps
[[DOMAIN-CYBERSECURITY]] and [[DOMAIN-GOVERNMENT]] and does **not** take
[[DOMAIN-NATIONAL-SECURITY]]. It is a cyber-security body that sits inside
an intelligence agency, not an intelligence service.
