---
id: EU-EFTI-REGULATION
type: regulation
name: Regulation (EU) 2020/1056 on electronic freight transport information
alternative_names:
  - eFTI Regulation
  - Electronic Freight Transport Information Regulation
description: >
  Regulation of the European Parliament and of the Council of 15 July
  2020 on electronic freight transport information, applicable from 21
  August 2024. It requires competent authorities to accept relevant
  freight transport information that Union law requires businesses to
  make available to them in electronic form, exchanged through certified
  eFTI platforms and eFTI service providers, in place of paper
  documents. Its aim is to reduce administrative costs, improve
  enforcement, and make freight transport and logistics more efficient
  and sustainable. The regulation delegates the definition of the eFTI
  common data set itself to a future Commission delegated act, rather
  than specifying it directly.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2020-07-15
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-MOBILITY
organisations: []
related_entities:
  - EU
  - EU-EMSWE
relationships:
  - type: applies-in
    target: EU
    source: fact
    evidence: "Confirmed verbatim by reading eur-lex.europa.eu's own text of the Regulation directly (2026-08-22): 'REGULATION (EU) 2020/1056 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 15 July 2020 on electronic freight transport information (Text with EEA relevance) ... This Regulation shall be binding in its entirety and directly applicable in all Member States.' Article 18 states it 'shall apply from 21 August 2024', with a handful of named articles (on delegated powers, certification and access) applying from entry into force instead."
    confidence: medium
    valid_from: 2024-08-21
    valid_until: null

sources:
  - title: "Regulation (EU) 2020/1056 of the European Parliament and of the Council of 15 July 2020 on electronic freight transport information"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32020R1056"
    publisher: "EUR-Lex — Publications Office of the European Union"
    accessed: "2026-08-22"
---

# eFTI Regulation

> **Closes a research question with a negative result.**
> `discovery/candidates.md` and [[EU-EMSWE]] both noted a claim, found
> only in a UNECE presentation and a project website, that the eFTI data
> set is built on the UN/CEFACT Multi-Modal Transport Reference Data
> Model (MMT-RDM) — which would be a second EU→UN/CEFACT edge alongside
> [[UN-LOCODE]]. This pass reads the Regulation's full text directly and
> searches it for "UN/CEFACT", "CEFACT", "MMT" and "UNECE": **none
> appears anywhere in the operative text.** The claim is not merely
> unread, as the original note assumed once outbound HTTPS was blocked —
> it is genuinely absent from the instrument itself, now that the
> instrument has been read. No such relationship is asserted.

## Description

Confirmed verbatim by reading eur-lex.europa.eu's own text of the
Regulation directly (2026-08-22): its stated aim is "to encourage the
digitalisation of freight transport and logistics to reduce
administrative costs, improve enforcement capabilities of competent
authorities, and enhance the efficiency and sustainability of
transport." It addresses "a large amount of information which is still
exchanged in paper format among businesses, and between businesses and
competent authorities," which "represents a significant administrative
burden for logistics operators" and "has a negative impact on the
environment."

Adopted **15 July 2020**, it applies from **21 August 2024** (Article
18), with a small set of articles on delegated powers, certification and
access applying earlier, from the Regulation's entry into force.

## Where the UN/CEFACT connection would actually have to live

The Regulation does not specify the eFTI common data set itself. Article
2 delegates that task to the Commission: a delegated act "supplementing
this Regulation by establishing and amending the common data set and
data subsets," due "no later than 21 February 2023," which must "seek to
ensure the interoperability of the eFTI common data set and eFTI data
subsets with relevant data models that are accepted internationally or
at Union level, including multimodal data models."

That is as close as the primary legal text comes to naming an
international data model, and it names none specifically. If the
UN/CEFACT MMT-RDM connection secondary sources describe is real, it
belongs in that delegated act — not identified, dated or read this pass
— rather than in the Regulation itself. This is a narrower and more
precise gap than the one originally logged.

## Not modelled

- The **delegated act establishing the eFTI common data set**, due by
  21 February 2023 under Article 2 — not identified. This is the
  instrument that would actually carry any UN/CEFACT reference, if one
  exists.
- The **certification scheme** for eFTI platforms and eFTI service
  providers (Articles 7–10).
- The **national regulatory information requirements** each member
  state notifies to the Commission (Annex I, Part B).

## Relationships

- `applies-in` [[EU]].

## Sources

Listed in frontmatter — the full text of the Regulation, read directly
this pass and searched for every term the UN/CEFACT claim would need to
appear under.
