---
id: INTL-ISOC
type: organisation
name: Internet Society
alternative_names:
  - ISOC
description: >
  International non-profit organisation supporting the development and use
  of the Internet. It is the corporate parent of the IETF Administration
  LLC, which provides the legal home for the IETF, the Internet Architecture
  Board and the Internet Research Task Force, and it provides significant
  funding to the IETF under an operating agreement between the two.

level: international
country: null
region: null

status: active
confidence: medium
coverage: low
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - INTL-IETF
relationships: []

sources:
  - title: "The Updated IETF-ISOC Relationship (draft-ietf-iasa2-rfc2031bis)"
    url: "https://datatracker.ietf.org/doc/draft-ietf-iasa2-rfc2031bis/08/"
    publisher: "IETF Datatracker"
  - title: "IETF Administration — overview"
    url: "https://www.ietf.org/administration/overview/"
    publisher: "Internet Engineering Task Force (IETF)"
  - title: "Internet Society extends major financial support commitment to the IETF"
    url: "https://www.ietf.org/blog/isoc-financial-commitment/"
    publisher: "Internet Engineering Task Force (IETF)"
---

# Internet Society (ISOC)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`. ⚠ `coverage: low`.

## Description

The Internet Society is an international non-profit supporting the
development and use of the Internet.

## Why it exists in this Atlas

It was created for one reason: **[[INTL-IETF]] had no parent.**

Under the rule that every entity must reach its scope anchor, the IETF was
the single hardest case in the repository. It is not part of the European
Union, not part of the United Nations, and belongs to no country — so
neither of the Atlas's two anchoring conventions could reach it, and there
is no `INTL` anchor entity to fall back on.

The honest answer was to find the IETF's **actual** parent rather than
attach it to a convenient one. The **IETF Administration LLC** provides the
corporate legal home for the IETF, the [[INTL-IETF]]'s companion bodies the
Internet Architecture Board and the Internet Research Task Force, and that
LLC is a **single-member disregarded entity of the Internet Society** —
operating as a branch or division of ISOC. ISOC also provides significant
IETF funding under an operating agreement between the two, and appoints one
member of the IETF LLC's board.

So the IETF is `part-of` ISOC, and the edge is asserted on [[INTL-IETF]].

## ISOC is a root, and that is fine

ISOC itself is part of nothing. Neither are [[EU]], [[UN]] or any country
anchor — the Atlas has always had roots, and the rule is that every entity
**reaches** an anchor, not that every entity has a parent. ISOC is reached
by the incoming edge from [[INTL-IETF]].

## ⚠ `coverage: low` — this entity is a stub with a job

Nothing about ISOC beyond its relationship to the IETF was researched: not
its founding, its governance, its membership, its policy work, nor its
chapters. It should be filled out or, if a better parent for [[INTL-IETF]]
is found, reconsidered.

## Not modelled

- The **IETF Administration LLC** itself, which is the entity legally
  interposed between ISOC and the IETF. Modelling it would make the chain
  exact — `INTL-IETF` → IETF LLC → ISOC — at the cost of a node whose only
  content is a tax status. The simplification is recorded here rather than
  hidden.
- The **Internet Architecture Board (IAB)** and the **Internet Research Task
  Force (IRTF)**, which share the same corporate home.

## Sources

Listed in frontmatter — all three from the IETF's own datatracker and site.
