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
verification: search-only

start_date: null
end_date: null
last_verified: null
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
relationships:
  - type: produces
    target: GB-CAF
    source: fact
    evidence: "The National Cyber Security Centre publishes the Cyber Assessment Framework, which the Cyber Security and Resilience Bill would place on a firmer statutory footing as the baseline standard for organisations in scope (ncsc.gov.uk Cyber Security and Resilience Bill policy statement; commonslibrary.parliament.uk CBP-10442; cyberfortgroup.com 'NCSC Cyber Assessment Framework: Structure and Scope'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Cyber Security and Resilience Bill — policy statement"
    url: "https://www.ncsc.gov.uk/pdfs/blog-post/cyber-security-resilience-bill-policy-statement.pdf"
    publisher: "National Cyber Security Centre (UK)"
  - title: "Cyber Security and Resilience (Network and Information Systems) Bill 2024-26"
    url: "https://commonslibrary.parliament.uk/research-briefings/cbp-10442/"
    publisher: "House of Commons Library"
  - title: "The Network and Information Systems Regulations 2018: how will they apply in practice?"
    url: "https://www.osborneclarke.com/insights/the-network-and-information-systems-regulations-2018-how-will-they-apply-in-practice"
    publisher: "Osborne Clarke"
---

# National Cyber Security Centre

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

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
