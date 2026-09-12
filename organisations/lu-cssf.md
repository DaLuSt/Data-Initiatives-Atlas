---
id: LU-CSSF
type: organisation
name: Commission de Surveillance du Secteur Financier
alternative_names:
  - CSSF
description: >
  Luxembourg's public institution supervising the professionals and
  products of the financial sector, established by the loi du 23
  décembre 1998 portant création d'une commission de surveillance du
  secteur financier, succeeding the Commissariat aux Bourses. Since
  Luxembourg's NIS2 transposition act of 5 May 2026, it is the sectoral
  competent authority for the banking sector, financial market
  infrastructure, and — insofar as they fall under its own supervision —
  the digital infrastructure and ICT service management sectors, applying
  DORA as lex specialis alongside the general NIS2 competent authority,
  the Institut Luxembourgeois de Régulation.

level: national
country: LU
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: 1998-12-23
end_date: null
last_verified: "2026-09-12"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations: []
related_entities:
  - LU
  - LU-ILR
  - LU-LOI-NIS2
relationships:
  - type: part-of
    target: LU
    source: fact
    evidence: "Anchor edge under metadata/relationship-types.md §2.3. Confirmed by reading cssf.lu's own homepage and its own page for the Law of 23 December 1998 directly (2026-09-12): CSSF is 'a public institution which supervises the professionals and products of the Luxembourg financial sector,' established by the loi du 23 décembre 1998 portant création d'une commission de surveillance du secteur financier, which also lists the entity categories under its supervision (credit institutions, investment firms, payment/e-money institutions, crypto-asset service providers, investment fund managers)."
    confidence: medium
    valid_from: 1998-12-23
    valid_until: null
  - type: governed-by
    target: LU-LOI-NIS2
    source: fact
    evidence: "CLOSES PART OF A PREVIOUSLY-FLAGGED GAP (discovery/unresolved.md row #181; LU-CTIE, LU-LOI-NIS2, LU-ILR). Already sourced on LU-LOI-NIS2 (created 2026-09-06) by reading ILR's own FAQ page directly: CSSF is competent authority 'for the banking sector and the financial market infrastructure sector, as well as for the digital infrastructure sector and the ICT service management sector, regarding the activities that fall under the supervision of' the CSSF, applying DORA as lex specialis. Recorded at the same relationship type as LU-ILR's own governed-by edge to the same Act, since both regulators derive their NIS2 competent-authority role from it, split by sector."
    confidence: high
    valid_from: 2026-05-10
    valid_until: null

sources:
  - title: "About us"
    url: "https://www.cssf.lu/en/"
    publisher: "Commission de Surveillance du Secteur Financier (CSSF)"
    accessed: "2026-09-12"
  - title: "Law of 23 December 1998 (consolidated version)"
    url: "https://www.cssf.lu/en/Document/law-of-23-december-1998-2/"
    publisher: "Commission de Surveillance du Secteur Financier (CSSF)"
    accessed: "2026-09-12"
  - title: "Frequently asked questions about NIS2 (FAQ)"
    url: "https://www.ilr.lu/en/sectors/niss/nis-2/frequently-asked-questions-about-nis2-faq/"
    publisher: "Institut Luxembourgeois de Régulation (ILR)"
    accessed: "2026-09-05"
---

# Commission de Surveillance du Secteur Financier (CSSF)

> **Created 2026-09-12**, closing the last of the three named-but-unmodelled
> nodes tracked in `discovery/unresolved.md` row #181 (after [[LU-ILR]] and
> [[LU-LOI-NIS2]] on 2026-09-06). CSSF's own homepage and its own page for
> its founding law were read directly; its NIS2 competent-authority role
> was already sourced via [[LU-ILR]]'s own FAQ page in the prior pass.

## Description

Confirmed by reading `cssf.lu` directly: CSSF is "a public institution
which supervises the professionals and products of the Luxembourg
financial sector," established by the **loi du 23 décembre 1998 portant
création d'une commission de surveillance du secteur financier**,
succeeding the Commissariat aux Bourses. Its own page for that law,
also read directly, lists the categories of entities under its
supervision: credit institutions, investment firms, payment and
electronic-money institutions, crypto-asset service providers, and
investment fund managers, among others.

## NIS2 competent authority for the financial sector

[[LU-LOI-NIS2]] and [[LU-ILR]] already established, by reading ILR's own
FAQ page directly, that CSSF holds the NIS2 competent-authority role "for
the banking sector and the financial market infrastructure sector, as
well as for the digital infrastructure sector and the ICT service
management sector, regarding the activities that fall under the
supervision of" the CSSF — applying **DORA** as *lex specialis* rather
than the general NIS2 framework administered by [[LU-ILR]] for the
"vast majority of sectors." CSSF's own homepage, read directly this pass,
does not itself use the term NIS2 but links to "ICT and cyber risk — for
DORA entities" among its topics, consistent with this split.

## Relationships

- `part-of` [[LU]] — anchor edge.
- `governed-by` [[LU-LOI-NIS2]] — the Act assigning CSSF its sectoral
  NIS2 competent-authority function, at the same relationship type as
  [[LU-ILR]]'s equivalent edge.

## Not modelled

- CSSF's DORA-specific supervisory instruments and circulars (e.g.
  circulaire CSSF 24/847 on ICT incident notification) — named in
  secondary sourcing but not created as separate entities here.

## Sources

Listed in frontmatter. CSSF's own homepage and founding-law page were
read directly 2026-09-12; ILR's FAQ page was read directly in the prior
(2026-09-05) pass and is carried over for the NIS2 role.
