---
id: LU-LOI-NIS2
type: law
name: "Loi du 5 mai 2026 concernant des mesures destinées à assurer un niveau élevé de cybersécurité"
alternative_names:
  - "Loi NIS 2"
  - "NIS 2 Act (Luxembourg)"
  - "Act of 5 May 2026 on measures to ensure a high level of cybersecurity"
description: >
  Luxembourg's act transposing the EU NIS2 Directive, published in
  Mémorial A n° 225 (6 May 2026) and entering into force 10 May 2026,
  repealing the country's prior NIS1-era cybersecurity act. It designates
  the Institut Luxembourgeois de Régulation (ILR) as competent authority
  for most sectors and the Commission de Surveillance du Secteur
  Financier (CSSF) for banking, financial-market infrastructure, digital
  infrastructure and ICT service management insofar as those fall under
  CSSF supervision.

level: national
country: LU
region: EU

status: active
confidence: high
coverage: low
verification: primary-source

start_date: 2026-05-10
end_date: null
last_verified: "2026-09-06"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - LU-ILR
related_entities:
  - EU-NIS2
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (LU-CTIE's own 'named but not modelled' finding, 2026-09-05). Confirmed by reading two independent primary/quasi-primary sources directly (2026-09-06): the Luxembourg government's own press release (gouvernement.lu, 6 July 2026, 'Cybersécurité: l'ILR présente la nouvelle loi NIS 2') names the act verbatim as 'loi du 5 mai 2026 concernant des mesures destinées à assurer un niveau élevé de cybersécurité'; ILR's own NIS2 page (ilr.lu), read independently, gives the English title 'Act of 5 May 2026 on measures to ensure a high level of cybersecurity,' states it 'came into force on 10 May 2026' and 'repealed the previous NIS1 Act.' Both are consistent with the WebSearch-corroborated Mémorial A n° 225 (6 May 2026) publication citation from DataGuidance's own reporting."
    confidence: high
    valid_from: 2026-05-10
    valid_until: null
  - type: applies-in
    target: LU
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. The Act repeals Luxembourg's prior NIS1-era cybersecurity act (confirmed by ILR's own page: 'repealed the previous NIS1 Act'), but that predecessor act is not itself an Atlas entity, so `supersedes` (which requires a real target entity) is not used; the repeal fact is recorded in this entity's body text instead. This edge asserts LU scope and nothing more."
    confidence: high
    valid_from: 2026-05-10
    valid_until: null

sources:
  - title: "Cybersécurité: l'ILR présente la nouvelle loi NIS 2"
    url: "https://gouvernement.lu/fr/actualites/toutes_actualites/communiques/2026/07-juillet/06-cybersecurite-nis-2.html"
    publisher: "Le gouvernement du Grand-Duché de Luxembourg"
    accessed: "2026-09-06"
  - title: "NIS 2"
    url: "https://www.ilr.lu/en/sectors/niss/nis-2/"
    publisher: "Institut Luxembourgeois de Régulation (ILR)"
    accessed: "2026-09-06"
  - title: "Frequently asked questions about NIS2 (FAQ)"
    url: "https://www.ilr.lu/en/sectors/niss/nis-2/frequently-asked-questions-about-nis2-faq/"
    publisher: "Institut Luxembourgeois de Régulation (ILR)"
    accessed: "2026-09-05"
  - title: "Luxembourg: Official Journal publishes NIS2 Transposition Law"
    url: "https://www.dataguidance.com/news/luxembourg-official-journal-publishes-nis2"
    publisher: "DataGuidance"
---

# Loi du 5 mai 2026 concernant des mesures destinées à assurer un niveau élevé de cybersécurité

> **Created 2026-09-06**, closing a gap [[LU-CTIE]] flagged on
> 2026-09-05 as "named, with sources, not yet modelled." Two independent
> primary/quasi-primary sources — the Luxembourg government's own press
> release and ILR's own NIS2 page — were read directly and agree on the
> Act's title, entry-into-force date and the repeal of the predecessor
> NIS1 act.

## Description

Luxembourg's transposition of [[EU-NIS2]], confirmed by reading the
government's own 6 July 2026 press release directly: "loi du 5 mai 2026
concernant des mesures destinées à assurer un niveau élevé de
cybersécurité." ILR's own NIS2 page, read independently, gives the same
act in English and confirms it "came into force on 10 May 2026" and
"repealed the previous NIS1 Act." A WebSearch cross-check of DataGuidance's
reporting adds the Official Journal citation — **Mémorial A n° 225**,
published **6 May 2026** — not independently verified by reading
Mémorial/Legilux directly, since `legilux.public.lu` is a JavaScript
single-page application returning no static content (the same block
[[LU-LOI-PROTECTION-DONNEES]] recorded).

## Two competent authorities, split by sector

Confirmed by reading ILR's own FAQ page directly (2026-09-05 pass, carried
over on [[LU-CTIE]]): **ILR** is competent authority "for the vast majority
of sectors," while the **Commission de Surveillance du Secteur Financier
(CSSF)** holds that role "for the banking sector and the financial market
infrastructure sector, as well as for the digital infrastructure sector and
the ICT service management sector, regarding the activities that fall
under the supervision of" the CSSF. CSSF itself is not created as an Atlas
entity here — a second regulator is a larger addition than a single
transposition-law batch should make in one pass.

## Not modelled

- **CSSF**, Luxembourg's financial regulator and the Act's second
  competent authority, per above.
- **GOVCERT.LU** and **CIRCL**, named as Luxembourg's two CSIRTs in
  secondary sources (pwc.lu, lawgitech.eu, nis-2-directive.com per
  [[LU-CTIE]]'s 2026-09-05 finding) but not confirmed on either primary
  source read this pass, and not created as entities.
- The **predecessor NIS1-era act**, repealed by this one — see the
  `applies-in` relationship's evidence field for why no `supersedes` edge
  is asserted.

## Relationships

- `implements-requirement-from` [[EU-NIS2]].
- `applies-in` [[LU]] — a scope anchor; the repeal of the unmodelled
  predecessor act is recorded in body text rather than as a `supersedes`
  edge.

## Sources

Listed in frontmatter. The government's own press release and ILR's own
NIS2 page were both read directly 2026-09-06; ILR's FAQ page was read
directly in the prior (2026-09-05) pass and is carried over; the
DataGuidance citation is WebSearch-corroborated only, for the Mémorial
publication date.
