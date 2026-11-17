---
id: EU-COMMISSION
type: organisation
name: European Commission
alternative_names:
  - Commission
  - EC
description: >
  Executive body of the European Union and holder of the right of
  legislative initiative. Under the ordinary legislative procedure it
  submits legislative proposals to the European Parliament and the Council,
  and it authors the strategies and communications that shape EU digital and
  data policy.

level: regional
country: null
region: EU

status: active
confidence: medium
coverage: low
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-11-17"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-PARLIAMENT
  - EU-COUNCIL
  - EU-CYBERSECURITY-STRATEGY
  - EU-EUROSTAT
  - EU-SEMIC
relationships:
  - type: part-of
    target: EU
    source: fact
    evidence: "Treaty on European Union (consolidated, CELEX 12016M/TXT), read directly 2026-11-17 from the Publications Office text: Article 13(1), \"The Union's institutions shall be: — the European Parliament, — the European Council, — the Council, — the European Commission ...\"; Article 17(1), \"The Commission shall promote the general interest of the Union and take appropriate initiatives to that end\", and 17(2), \"Union legislative acts may only be adopted on the basis of a Commission proposal, except where the Treaties provide otherwise.\""
    confidence: medium
    valid_from: null
    valid_until: null
  - type: produces
    target: EU-DATA-STRATEGY
    source: fact
    evidence: "The Communication 'A European strategy for data', COM(2020) 66 final of 19.2.2020, read directly 2026-11-17 from the Publications Office (CELEX 52020DC0066): 'The actions are based on four pillars', the fourth being 'D. Common European data spaces in strategic sectors and domains of public interest'."
    confidence: high
    valid_from: 2020-02-19
    valid_until: null
  - type: produces
    target: EU-CYBERSECURITY-STRATEGY
    source: fact
    evidence: "JOIN(2020) 18 final, read directly 2026-11-17 from the Publications Office text (CELEX 52020JC0018): 'EUROPEAN COMMISSION Brussels, 16.12.2020 JOIN(2020) 18 final JOINT COMMUNICATION TO THE EUROPEAN PARLIAMENT AND THE COUNCIL The EU's Cybersecurity Strategy for the Digital Decade'. A joint communication, so co-authored with the High Representative, who is not an Atlas entity; the document's signature block was not read."
    confidence: medium
    valid_from: 2020-12-16
    valid_until: null
  - type: produces
    target: EU-DIGITAL-OMNIBUS
    source: fact
    evidence: "The proposal itself, read directly 2026-11-17 from the Publications Office (COM(2025) 837 final, PDF): 'EUROPEAN COMMISSION Brussels, 19.11.2025 COM(2025) 837 final 2025/0360 (COD) Proposal for a REGULATION ... (Digital Omnibus)'. The earlier record cited COM(2025) 836, which is the separate proposal on the AI Act (now [[EU-DIGITAL-OMNIBUS-AI]]); corrected here."
    confidence: high
    valid_from: 2025-11-19
    valid_until: null

sources:
  - title: "The ordinary legislative procedure"
    url: "https://www.consilium.europa.eu/en/council-eu/decision-making/ordinary-legislative-procedure/"
    publisher: "Council of the European Union"
  - title: "Ordinary legislative procedure — overview"
    url: "https://www.europarl.europa.eu/olp/en/ordinary-legislative-procedure/overview"
    publisher: "European Parliament"
  - title: "COM(2020) 66 final (CELEX 52020DC0066)"
    url: "https://publications.europa.eu/resource/celex/52020DC0066"
    publisher: "Publications Office of the European Union"
    accessed: "2026-11-17"
  - title: "Treaty on European Union (consolidated version 2016), Articles 13 to 17"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016M/TXT"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-11-17"
  - title: "JOIN(2020) 18 final — The EU's Cybersecurity Strategy for the Digital Decade"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52020JC0018"
    publisher: "EUR-Lex (Publications Office of the European Union)"
    accessed: "2026-11-17"
---

# European Commission

> **Verified 2026-08-21.** Every source this entity cites is on a domain the
> repository owner confirmed read and correct — `europa.eu`. `verification:
> primary-source`. See `docs/re-verification.md` §"The confirmed domains".

## Description

The European Commission is the EU's executive body and holds the right of
legislative initiative: the ordinary legislative procedure begins with a
Commission proposal submitted to [[EU-PARLIAMENT]] and [[EU-COUNCIL]], and
the Commission is represented in the procedure by the responsible
Commissioner or the Director-General of the department handling the dossier.

Within the Atlas it appears in two roles: author of the strategies and
communications that open the EU policy chains ([[EU-DATA-STRATEGY]],
[[EU-CYBERSECURITY-STRATEGY]]), and originator of the legislative proposals
that become the regulations and directives in `legislation/`.

## Directorates-General

Batch 9 created none, because no source describing a Directorate-General had
been read and a single passing mention would have repeated the [[NL-PETRA]]
mistake. **Decided 2026-10-13 (roadmap #509):** a Directorate-General is an
entity when an Atlas entity's own read source says the department develops,
maintains or provides it, and the department's own Commission page has been
read. The rule, and the departments checked, are in `metadata/ontology.md` §6.
Today that is [[EU-DG-EMPL]] (ESCO and Europass) and [[EU-EUROSTAT]], which
was modelled the same way before the question was asked.

`coverage: low` for the same reason: this entity records the Commission's
role in the chains the Atlas already holds, not the institution itself.

## Relationships

- Produces [[EU-DATA-STRATEGY]] and [[EU-DIGITAL-OMNIBUS]].
- Co-legislates with [[EU-PARLIAMENT]] and [[EU-COUNCIL]].

## Sources

Listed in frontmatter.
