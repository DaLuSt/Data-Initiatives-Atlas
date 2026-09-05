---
id: DE-BUNDESDRUCKEREI
type: organisation
name: Bundesdruckerei
alternative_names:
  - Bundesdruckerei Gruppe GmbH
description: >
  German federal printing and secure-identity company, producing German
  passports, ID cards, residence permits and driving licences, and
  supporting federal agencies' integration of the ID card's online
  (eID) function. Converted to a private-law company in 1994, sold to
  Apax Partners in 2000, and reacquired by the federal government in
  2009. Wholly (100%) federally owned, with the Federal Ministry of
  Finance exercising shareholder duties.

level: national
country: DE
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-09-05"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities: []
relationships:
  - type: part-of
    target: DE
    source: fact
    evidence: "Anchor edge (metadata/relationship-types.md §2.3): Bundesdruckerei is a body of the German federal state. Confirmed by reading bundesfinanzministerium.de's own January 2019 Monatsbericht analysis directly (2026-09-05): converted to a private-law company in 1994 (state retained full ownership initially), sold entirely to Apax Partners in 2000, reacquired by the federal government in a transaction completed 8 October 2009, and today 100% owned by the federal government with the Federal Ministry of Finance (BMF) exercising shareholder duties. No Bundesministerium der Finanzen entity exists yet in the Atlas to carry a more specific `part-of` edge."
    confidence: high
    valid_from: 2009-10-08
    valid_until: null

sources:
  - title: 'Die Bundesdruckerei – Vom "Staatsdrucker" zu einem führenden Unternehmen für IT-Sicherheitslösungen'
    url: "https://www.bundesfinanzministerium.de/Monatsberichte/2019/01/Inhalte/Kapitel-3-Analysen/3-7-beteiligungsbilanz-bundesdruckerei.html"
    publisher: "Bundesministerium der Finanzen (BMF)"
    accessed: "2026-09-05"
  - title: "Solutions for governments"
    url: "https://www.bundesdruckerei.de/en/fields-use/solutions-governments"
    publisher: "Bundesdruckerei Gruppe GmbH"
    accessed: "2026-09-05"
---

# Bundesdruckerei

> **Added 2026-09-05, `verification: primary-source` from creation.**
> `discovery/research-queue.md` had named Bundesdruckerei as unmodelled
> alongside [[DE-ITZBUND]], which was closed the same pass. The Federal
> Ministry of Finance's own retrospective analysis was read directly.

## Description

Bundesdruckerei is Germany's federal printing and secure-identity company.
Reading `bundesdruckerei.de`'s own page directly, it has "a tradition of
producing Germany's ID cards and passports" and today manufactures **ID
cards, passports, residence permits, office ID cards, visas and driving
licences**, supplying complete ID systems from application through to
delivery. It also **supports federal agencies in integrating the ID
card's online (eID) function** — no dedicated Atlas entity for that eID
function exists yet, so this is recorded here in prose rather than as a
relationship.

## Ownership history: privatised, then reacquired

Reading the Federal Ministry of Finance's (BMF) own January 2019
Monatsbericht analysis directly: the cabinet decided in **1994** to
convert Bundesdruckerei into a private-law company, though the federal
government retained full ownership at first. In **2000** the government
sold its entire stake to the investment group **Apax Partners** — genuine
privatisation — and financial difficulties in the early 2000s nearly
caused insolvency. In **September 2008** the government decided to
reacquire Bundesdruckerei, a transaction completed **8 October 2009**,
driven by changed security-policy interests. It remains **100%
federally owned** today, a private-law entity in substance publicly
controlled, with the **Federal Ministry of Finance** exercising
shareholder duties. No Bundesministerium der Finanzen entity exists yet
in the Atlas, so `part-of` [[DE]] is recorded as an anchor edge.

## Relationships

- `part-of` [[DE]] — anchor edge; 100% federally owned since the 2009
  reacquisition, with no Bundesministerium der Finanzen entity yet to
  carry a more specific one.

## Sources

Listed in frontmatter, both read directly this pass.
