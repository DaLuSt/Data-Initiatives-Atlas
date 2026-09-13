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
last_verified: "2026-09-13"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-CYBERSECURITY
organisations:
  - LU-ILR
  - LU-CSSF
related_entities:
  - EU-NIS2
  - LU-GOVCERT
  - LU-CIRCL
relationships:
  - type: implements-requirement-from
    target: EU-NIS2
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (LU-CTIE's own 'named but not modelled' finding, 2026-09-05). Confirmed by reading two independent primary/quasi-primary sources directly (2026-09-06): the Luxembourg government's own press release (gouvernement.lu, 6 July 2026, 'Cybersécurité: l'ILR présente la nouvelle loi NIS 2') names the act verbatim as 'loi du 5 mai 2026 concernant des mesures destinées à assurer un niveau élevé de cybersécurité'; ILR's own NIS2 page (ilr.lu), read independently, gives the English title 'Act of 5 May 2026 on measures to ensure a high level of cybersecurity,' states it 'came into force on 10 May 2026' and 'repealed the previous NIS1 Act.' Both are consistent with the WebSearch-corroborated Mémorial A n° 225 (6 May 2026) publication citation from DataGuidance's own reporting. **CONFIRMED DIRECTLY 2026-09-13**: the Official Journal citation is no longer WebSearch-only — read the Act's own text directly via data.legilux.public.lu's filestore subdomain (a working alternate to legilux.public.lu's unreadable JavaScript SPA, first found on [[LU-LOI-DONNEES-PENAL-2018]]). The Act's own recital cites 'la directive (UE) 2022/2555 du Parlement européen et du Conseil du 14 décembre 2022' by its full name, confirming the EU-NIS2 target directly rather than via secondary description."
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
  - title: "JOURNAL OFFICIEL DU GRAND-DUCHÉ DE LUXEMBOURG — MÉMORIAL A N° 225 du 6 mai 2026"
    url: "https://data.legilux.public.lu/filestore/eli/etat/leg/loi/2026/05/05/a225/jo/fr/pdfa/eli-etat-leg-loi-2026-05-05-a225-jo-fr-pdfa.pdf"
    publisher: "Journal Officiel du Grand-Duché de Luxembourg (Legilux)"
    accessed: "2026-09-13"
---

# Loi du 5 mai 2026 concernant des mesures destinées à assurer un niveau élevé de cybersécurité

> **Created 2026-09-06**, closing a gap [[LU-CTIE]] flagged on
> 2026-09-05 as "named, with sources, not yet modelled." Two independent
> primary/quasi-primary sources — the Luxembourg government's own press
> release and ILR's own NIS2 page — were read directly and agree on the
> Act's title, entry-into-force date and the repeal of the predecessor
> NIS1 act.
>
> **Confirmed directly 2026-09-13.** The Official Journal citation, until
> now WebSearch-only, is closed: `data.legilux.public.lu`'s filestore
> subdomain (a working alternate to `legilux.public.lu`'s unreadable
> JavaScript SPA, first found on [[LU-LOI-DONNEES-PENAL-2018]]) serves the
> Act's own text in full. See "Confirmed against the Act's own text" below.

## Description

Luxembourg's transposition of [[EU-NIS2]], confirmed by reading the
government's own 6 July 2026 press release directly: "loi du 5 mai 2026
concernant des mesures destinées à assurer un niveau élevé de
cybersécurité." ILR's own NIS2 page, read independently, gives the same
act in English and confirms it "came into force on 10 May 2026" and
"repealed the previous NIS1 Act." A WebSearch cross-check of DataGuidance's
reporting adds the Official Journal citation — **Mémorial A n° 225**,
published **6 May 2026** — independently confirmed 2026-09-13 by reading
the Act's own text directly (see below).

## Confirmed against the Act's own text, 2026-09-13

Reading Mémorial A N° 225 directly, via Legilux's filestore subdomain,
confirms the full official title verbatim: "Loi du 5 mai 2026 concernant
des mesures destinées à assurer un niveau élevé de cybersécurité et
portant modification de: 1° la loi modifiée du 14 août 2000 relative au
commerce électronique; 2° la loi modifiée du 23 juillet 2016 portant
création d'un Haut-Commissariat à la Protection nationale; 3° la loi du
17 décembre 2021 sur les réseaux et les services de communications
électroniques." The Act was signed by **Grand-Duc Guillaume**, following
adoption by the Chambre des Députés on 28 April 2026 and the Conseil
d'État's opinion of 5 May 2026 (dispensing with a second vote). Its own
recital cites "la directive (UE) 2022/2555 du Parlement européen et du
Conseil du 14 décembre 2022" — [[EU-NIS2]] — by name.

**Article 6(6)**, read directly, carves three bodies out of the Act's
supervision-and-enforcement chapter (Articles 12–15): the **Service de
renseignement de l'État** (State Intelligence Service, under its own 5
July 2016 reorganisation act), **services of the Minister responsible for
Defence**, and the **Armée luxembourgeoise** (under its 7 August 2023
organisation act) — the same shape of carve-out [[NL-WIV-2017]]-style
regimes and [[FR-NIS2-LOI]]'s CER/DORA bundling both show elsewhere in
the Atlas's NIS2 layer, though Luxembourg expresses it as an explicit
statutory exclusion rather than a separate instrument.

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

- The **predecessor NIS1-era act**, repealed by this one — see the
  `applies-in` relationship's evidence field for why no `supersedes` edge
  is asserted.
- The **three acts this Act amends**, per its own preamble: the modified
  law of 14 August 2000 on electronic commerce, the modified law of 23
  July 2016 creating the Haut-Commissariat à la Protection nationale, and
  the law of 17 December 2021 on electronic communications networks and
  services — none independently researched or modelled this pass.

> **Closed 2026-09-12**: CSSF, GOVCERT.LU and CIRCL — all named above but
> left unmodelled in the 2026-09-06 pass — are now [[LU-CSSF]],
> [[LU-GOVCERT]] and [[LU-CIRCL]], closing `discovery/unresolved.md`
> row #181 in full. [[LU-CSSF]] carries its own `governed-by` edge to this
> Act; GOVCERT.LU and CIRCL sit under [[LU-HCPN]] and [[LU-LHC]]
> respectively, one level removed from this Act itself.

## Relationships

- `implements-requirement-from` [[EU-NIS2]].
- `applies-in` [[LU]] — a scope anchor; the repeal of the unmodelled
  predecessor act is recorded in body text rather than as a `supersedes`
  edge.

## Sources

Listed in frontmatter. The government's own press release and ILR's own
NIS2 page were both read directly 2026-09-06; ILR's FAQ page was read
directly in the prior (2026-09-05) pass and is carried over; the
DataGuidance citation supplied the Mémorial publication date, now
independently confirmed by the Act's own text (Mémorial A N° 225), read
directly 2026-09-13 via Legilux's filestore subdomain — the strongest
citation this entity carries.
