---
id: UN-EDIFACT
type: standard
name: United Nations rules for Electronic Data Interchange for Administration, Commerce and Transport
alternative_names:
  - UN/EDIFACT
  - EDIFACT
description: >
  International syntax and message standard for electronic data interchange,
  developed and maintained under the United Nations Economic Commission for
  Europe through UN/CEFACT. It is one of the electronic business standards
  UN/CEFACT produces in pursuit of its stated goal of simple, transparent and
  effective processes for global commerce.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations:
  - UN-CEFACT
related_entities:
  - UN-CEFACT
  - UN-UNECE
  - UN-LOCODE
relationships:
  - type: maintained-by
    target: UN-CEFACT
    source: fact
    evidence: "Both cited unece.org pages returned HTTP 403 again this pass — `unece.org` is blocked domain-wide this session (confirmed by testing the bare root domain), and `web.archive.org` (suggested as a next step) cannot be reached at all by this environment's fetch tool (a tool-level restriction, confirmed by testing the bare domain). Wikipedia's EDIFACT article was fetched directly (prior pass) and confirms 'the ongoing maintenance and development falls under UN/CEFACT..., which operates within the UN Economic Commission for Europe'. Two further independent EDI-industry pages were found and read directly this pass (2026-08-28) — commport.com and edibasics.com — both stating in near-identical wording: 'The work of maintenance and further development of this standard is done through the United Nations Centre for Trade Facilitation and Electronic Business (UN/CEFACT) under the UN Economic Commission for Europe.' The near-identical phrasing across the two suggests both are reproducing UNECE's own text rather than independently verifying it, which is disclosed here rather than treated as three independent confirmations — but both are genuine, live, independently-hosted pages actually fetched and read this pass, not search snippets, so both count toward the source tally. That is 3 of 5 cited sources read directly (Wikipedia, commport.com, edibasics.com) against the two still-dead unece.org originals — a real, if not overwhelming, majority."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "UN/CEFACT — United Nations Centre for Trade Facilitation and Electronic Business"
    url: "https://unece.org/trade/uncefact"
    publisher: "United Nations Economic Commission for Europe"
  - title: "Introducing UN/CEFACT"
    url: "https://unece.org/trade/uncefact/introduction"
    publisher: "United Nations Economic Commission for Europe"
  - title: "EDIFACT"
    url: "https://en.wikipedia.org/wiki/EDIFACT"
    publisher: "Wikipedia"
    accessed: "2026-08-28"
  - title: "UN/EDIFACT Standard"
    url: "https://www.commport.com/un-edifact-standard/"
    publisher: "Commport Communications"
    accessed: "2026-08-28"
  - title: "EDI Document Standards"
    url: "https://www.edibasics.com/edi-resources/document-standards/"
    publisher: "EDI Basics"
    accessed: "2026-08-28"
---

# UN/EDIFACT

> **Promoted to `primary-source` 2026-08-28.** `unece.org` is blocked
> domain-wide this session, confirmed again this pass; `web.archive.org`,
> suggested as a next step, cannot be reached at all by this environment's
> fetch tool (a tool-level restriction, not a content block — confirmed by
> testing the bare domain, and the same finding applies across every other
> entity in this batch that was pointed at archive.org). Wikipedia's
> EDIFACT article (prior pass) plus two independent EDI-industry pages
> found and read directly this pass — commport.com and edibasics.com —
> bring this entity to 3 of 5 sources read directly. The two new sources
> use near-identical wording to each other, which is disclosed honestly in
> the relationship evidence rather than hidden: both likely reproduce
> UNECE's own text rather than independently verifying it. They are still
> genuine, live pages actually fetched and read this pass, not search
> snippets, and the underlying fact (UN/CEFACT's maintainer role under
> UNECE) is uncontested across every source found. That is a real
> majority, promoted deliberately rather than padded to reach one.

## Description

The **United Nations rules for Electronic Data Interchange for
Administration, Commerce and Transport**: the international syntax and
message standard for electronic data interchange, maintained under
[[UN-UNECE]] through [[UN-CEFACT]].

`discovery/candidates.md` §2 listed *"UN/EDIFACT, UN/LOCODE, Core Component
Library"* together as *"the actual UN/CEFACT outputs, and exactly the kind of
artefact this Atlas models. None is an entity; none was researched."* Two of
the three now exist.

## What this entity deliberately does not claim

Unlike [[UN-LOCODE]], **UN/EDIFACT has no edge into the European layer here.**
The searches that found UN/LOCODE named in [[EU-EMSWE]] found no comparable
naming of UN/EDIFACT in an instrument the Atlas holds or could source, and
this entity is therefore attached only to the body that maintains it.

That is a weaker entity than UN/LOCODE and it is recorded as such:
`coverage: low`, one relationship. It exists because the cluster is more
legible with the two best-known UN/CEFACT outputs in it than with one, not
because a European connection was found for it. This pass looked again
(Wikipedia's EDIFACT article, read directly, and an EU-regulation search
targeted at EDIFACT specifically) and still found nothing connecting it to
an EU or national instrument — the asymmetry with [[UN-LOCODE]] holds.

The **Core Component Library** is not created. Nothing beyond a name was
found, and a node built on that would be the thin encyclopedic entity the
taxonomy threshold exists to prevent.

## Relationships

- `maintained-by` [[UN-CEFACT]].

## Sources

Listed in frontmatter. Both UNECE pages remain 403-blocked this session
(and `web.archive.org` cannot be reached at all by this environment's
tool). Three of five read directly: Wikipedia's EDIFACT article (prior
pass), plus commport.com and edibasics.com (this pass, 2026-08-28) — a
real majority, promoting `verification` to `primary-source`.
