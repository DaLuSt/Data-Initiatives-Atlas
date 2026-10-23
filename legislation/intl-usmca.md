---
id: INTL-USMCA
type: agreement
name: "Agreement between the United States of America, the United Mexican States, and Canada (USMCA)"
alternative_names:
  - "USMCA"
  - "CUSMA"
  - "T-MEC"
  - "United States-Mexico-Canada Agreement"
  - "Canada-United States-Mexico Agreement"
description: >
  The trade agreement of the United States, Mexico and Canada that replaced the North American Free Trade Agreement
  and entered into force on 1 July 2020. Among its 34 chapters, Chapter 19 on digital trade covers personal
  information protection, cross-border transfers of information, computing facilities, cybersecurity, source code and
  open government data. A Free Trade Commission oversees it, and a joint review is due on every sixth anniversary.

level: regional
country: null
region: null

status: active
confidence: high
coverage: low
verification: primary-source
start_date: 2020-07-01
end_date: null
last_verified: "2026-10-23"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations:
  - INTL-USMCA-FTC
related_entities:
  - INTL-USMCA-FTC
  - INTL-USMCA-CH19
  - US
  - MX
  - CA
relationships:
  - type: applies-in
    target: US
    source: fact
    evidence: "USTR's agreement page, read directly (2026-10-23): 'The United States-Mexico-Canada Agreement (USMCA) entered into force on July 1, 2020'; the text is the 'Agreement between the United States of America, the United Mexican States, and Canada'. The United States is one of the three Parties."
    confidence: high
    valid_from: 2020-07-01
    valid_until: null
  - type: applies-in
    target: MX
    source: fact
    evidence: "USTR's agreement page, read directly (2026-10-23): 'The United States-Mexico-Canada Agreement (USMCA) entered into force on July 1, 2020'; the text is the 'Agreement between the United States of America, the United Mexican States, and Canada'. Mexico is one of the three Parties."
    confidence: high
    valid_from: 2020-07-01
    valid_until: null
  - type: applies-in
    target: CA
    source: fact
    evidence: "USTR's agreement page, read directly (2026-10-23): 'The United States-Mexico-Canada Agreement (USMCA) entered into force on July 1, 2020'; the text is the 'Agreement between the United States of America, the United Mexican States, and Canada'. Canada is one of the three Parties."
    confidence: high
    valid_from: 2020-07-01
    valid_until: null
  - type: related-to
    target: INTL-USMCA-FTC
    source: fact
    evidence: "Article 30.1 (read directly 2026-10-23): 'The Parties hereby establish a Free Trade Commission'."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "United States-Mexico-Canada Agreement"
    url: "https://ustr.gov/trade-agreements/free-trade-agreements/united-states-mexico-canada-agreement"
    publisher: "Office of the United States Trade Representative"
    accessed: "2026-10-23"
  - title: "Protocol replacing the North American Free Trade Agreement (USMCA Protocol)"
    url: "https://ustr.gov/sites/default/files/files/agreements/FTA/USMCA/Text/USMCA_Protocol.pdf"
    publisher: "Office of the United States Trade Representative"
    accessed: "2026-10-23"
  - title: "USMCA Chapter 34, Final Provisions"
    url: "https://ustr.gov/sites/default/files/files/agreements/FTA/USMCA/Text/34_Final_Provisions.pdf"
    publisher: "Office of the United States Trade Representative"
    accessed: "2026-10-23"
  - title: "USMCA Chapter 30, Administrative and Institutional Provisions"
    url: "https://ustr.gov/sites/default/files/files/agreements/FTA/USMCA/Text/30%20Administrative%20and%20Institutional%20Provisions.pdf"
    publisher: "Office of the United States Trade Representative"
    accessed: "2026-10-23"
  - title: "USTR Seeks Public Comment on the 2027 Joint Review of USMCA (2 October 2026)"
    url: "https://ustr.gov/about/policy-offices/press-office/press-releases/2026/october/ustr-seeks-public-comment-2027-joint-review-usmca"
    publisher: "Office of the United States Trade Representative"
    accessed: "2026-10-23"
---

# USMCA / CUSMA / T-MEC

> **Created 2026-10-23** (roadmap #544, Northern America's regional instruments). Sourced from the United States Trade Representative's own pages and the agreement's text on them (the Protocol, Chapters 19, 30 and 34), read directly. The other chapters were not read.

## Description

USTR: the agreement "entered into force on July 1, 2020" and "substituted the North America Free Trade Agreement". The Protocol of Amendment says it enters into force "on the first day of the third month following the last notification" and, on entry into force, terminates the North American Agreement on Labor Cooperation. NAFTA has no entity in the Atlas, so there is no `supersedes` edge. Article 34.6 lets a Party withdraw six months after written notice; Article 34.7 terminates the agreement 16 years after entry into force unless each Party confirms a new 16-year term, with a joint review by the Free Trade Commission on the sixth anniversary (and annually afterwards if a Party does not confirm).

## What it carries in the Atlas

[[INTL-USMCA-CH19]] (digital trade), the only chapter modelled. [[INTL-USMCA-FTC]] is the body that supervises it.

## Open

On 2 October 2026 USTR announced a public consultation, with comments due 12 January 2027, "in advance of the 2027 joint review of the Agreement". Reports that the United States declined on 1 July 2026 to confirm an extension, which would trigger annual reviews, come from law-firm and news pages, not from a Party's own site, and are **not** recorded here: see `discovery/unresolved.md` row #254.

## Relationships

`applies-in` the three Parties (all have a country anchor); `related-to` [[INTL-USMCA-FTC]].

## Sources

Listed in frontmatter, read directly.
