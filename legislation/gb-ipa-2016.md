---
id: GB-IPA-2016
type: law
name: Investigatory Powers Act 2016
alternative_names:
  - Investigatory Powers Act
description: >
  United Kingdom act providing a modernised framework governing the use and
  oversight of investigatory powers by law enforcement and the security and
  intelligence agencies. It created the Investigatory Powers Commissioner's
  Office, merging three predecessor commissioner offices into one, and
  covers over 600 public authorities.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2016-11-29
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB-MI5
  - GB-SIS
  - GB-GCHQ
  - GB-IPCO
  - GB-ISA-1994
  - GB-SSA-1989
relationships:
  - type: references
    target: GB-ISA-1994
    source: fact
    evidence: "Confirmed by reading legislation.gov.uk (2026-08-22): Schedule 10, Part 2 of the Investigatory Powers Act 2016 is headed 'Intelligence Services Act 1994' and contains provisions amending that act."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "Investigatory Powers Act 2016 — Schedule 10 Part 2"
    url: "https://www.legislation.gov.uk/ukpga/2016/25/schedule/10/part/2/crossheading/intelligence-services-act-1994"
    publisher: "The National Archives (legislation.gov.uk)"
    accessed: "2026-08-22"
  - title: "Investigatory Powers"
    url: "https://www.ipco.org.uk/investigatory-powers/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
    accessed: "2026-08-22"
  - title: "What we do"
    url: "https://www.ipco.org.uk/what-we-do/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
    accessed: "2026-08-22"
  - title: "Legal Framework"
    url: "https://www.gchq.gov.uk/section/governance/legal-framework"
    publisher: "Government Communications Headquarters (GCHQ)"
    accessed: "2026-08-22"
---

# Investigatory Powers Act 2016

> **Verified 2026-08-22.** The statute text at legislation.gov.uk and
> IPCO's own pages were read directly and confirmed the claims below,
> including the exact Royal Assent date.

## Description

Confirmed directly on legislation.gov.uk (2026-08-22): "An Act to make
provision about the interception of communications, equipment interference
and the acquisition and retention of communications data, bulk personal
datasets and other information", enacted **29 November 2016**. The IPA provides a **modernised framework** governing the use and oversight
of investigatory powers by law enforcement and the security and intelligence
agencies, and created [[GB-IPCO]].

## A powers act, like the French one, reached from the opposite direction

The UK and France both ended up legislating **techniques rather than
institutions** — [[GB-IPA-2016]] and [[FR-LOI-RENSEIGNEMENT-2015]], one year
apart — but from opposite starting points.

France had **no** organic acts for its services and legislated the powers to
fill that gap; the 2015 law is the primary instrument, and the services'
Atlas entities point at nothing else.

The UK **already had** agency acts ([[GB-SSA-1989]], [[GB-ISA-1994]]) and
added a powers act **on top**; its services carry `governed-by` edges to
both, and to [[GB-DPA-2018]] besides.

Germany did the same layering much earlier and much more narrowly, with
[[DE-G10]] covering one constitutional right rather than the whole field.

## It consolidated three oversight offices into one

[[GB-IPCO]] absorbed the Office of Surveillance Commissioners, the
Interception of Communications Commissioner's Office and the Intelligence
Services Commissioner's Office, plus the Office for Communications Data
Authorisations.

Because the act governs **powers**, its overseer follows those powers into
every body that holds them — **over 600 public authorities**, not only the
three agencies.

## `references` [[GB-ISA-1994]], and nothing stronger

Schedule 10 Part 2 amends the 1994 act. The relationship is `references`:
the IPA modifies the earlier act without replacing it, and both remain in
force and both appear as `governed-by` targets on [[GB-SIS]] and
[[GB-GCHQ]].

## Not modelled

- The **Investigatory Powers (Amendment) Act 2024**.
- **RIPA 2000**, largely superseded by this act but not wholly repealed.
- The **double lock** warrant mechanism and the **Judicial Commissioners** —
  the UK's nearest analogue to [[NL-TIB]]. No source read describes it, so
  it is absent from [[GB-IPCO]] too.
- The **Investigatory Powers Tribunal**.

## Sources

Listed in frontmatter.
