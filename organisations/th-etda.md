---
id: TH-ETDA
type: organisation
name: "Electronic Transactions Development Agency (ETDA), Thailand"
alternative_names:
  - "ETDA"
  - "สำนักงานพัฒนาธุรกรรมทางอิเล็กทรอนิกส์"
description: >
  Thailand's agency for promoting, supporting and developing electronic transactions, founded in 2011 under the Electronic Transactions
  Act B.E. 2544 (2001) (Revised Edition) and now also the Electronic Transactions Development Agency Act B.E. 2562 (2019). It works
  through licensing, registration, notification, standard-setting, legislation and sandbox testing on government, private and public
  e-transactions, runs the national root certification authority and trust services, and publishes its own data governance and personal
  data protection policies (in Thai).

level: national
country: TH
region: null

status: active
organisation_role: regulatory
confidence: high
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-01"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
  - DOMAIN-DIGITAL-INFRASTRUCTURE
organisations: []
related_entities:
  - TH
  - TH-ETA-2001
relationships:
  - type: part-of
    target: TH
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. ETDA's Background page (read directly 2026-11-01, English): 'The Agency was founded in 2011 to play a major role in promoting, supporting and developing electronic transactions (e-transactions) or online transactions under the Electronic Transactions Act of B.E. 2544 (A.D. 2001) (Revised Edition) and the Electronic Transactions Development Agency Act of B.E. 2562 (A.D. 2019).'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: governed-by
    target: TH-ETA-2001
    source: fact
    evidence: "The same page names the Electronic Transactions Act B.E. 2544 (Revised Edition) as the law under which the Agency promotes e-transactions; its Laws page lists the Act and Committee notifications first."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "ETDA Background — Electronic Transactions Development Agency"
    url: "https://www.etda.or.th/en/about-etda/mission-of-etda.aspx"
    publisher: "Electronic Transactions Development Agency (ETDA), Thailand"
    accessed: "2026-11-01"
  - title: "Laws — Electronic Transactions Development Agency"
    url: "https://www.etda.or.th/en/ETC/strategy-law-standard/law.aspx"
    publisher: "Electronic Transactions Development Agency (ETDA), Thailand"
    accessed: "2026-11-01"
---

# Electronic Transactions Development Agency (Thailand)

> **Created 2026-11-01** (roadmap #470, country group 1, Thailand). Two English pages of ETDA's own site read directly (the earlier probes had only reached `pdpc.or.th`, which answers 403). `start_date` is empty: the page gives 2011 as the founding year only. The ETDA Act B.E. 2562 is named and not modelled; the Thai-language Data Governance Policy was listed and not read.

## Relationships

Part of [[TH]]; works under [[TH-ETA-2001]].
