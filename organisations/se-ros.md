---
id: SE-ROS
type: organisation
name: "Rådet för den officiella statistiken"
name_en: "Council for Official Statistics"
alternative_names:
  - "ROS"
  - "Council for Official Statistics"
description: >
  Council of the Swedish producers of official statistics, established by
  the government on 1 February 2002 to advise and support Statistics Sweden
  in coordinating official statistics. It reports to the Government each
  year on the system for official statistics.

level: national
country: SE
region: null

status: active
organisation_role: advisory
confidence: high
coverage: low
verification: primary-source
start_date: 2002-02-01
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - SE
  - SE-SCB
relationships:
  - type: part-of
    target: SE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. Statistics Sweden's own page, read directly (2026-10-11): 'The Council for Official Statistics (ROS) was established on 1 February 2002. The Council has been created by the government, and Statistics Sweden's directive (2016:822) regulates the tasks and composition.'"
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: SE-SCB
    source: fact
    evidence: "Statistics Sweden's page, read directly (2026-10-11): the Council 'has the task to give advice and support to Statistics Sweden in the role of coordination for the official statistics'; the Director General of Statistics Sweden chairs it. Advice and coordination, not oversight of Statistics Sweden itself."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "The Council for Official Statistics — Statistics Sweden"
    url: "https://www.scb.se/en/About-us/main-activity/councils-and-boards/the-council-for-official-statistics/"
    publisher: "Statistics Sweden (SCB)"
    accessed: "2026-10-11"
---

# Council for Official Statistics (ROS), Sweden

> **Created 2026-10-11** (roadmap #459, bodies beside statistical offices). Statistics Sweden's English page was read directly. The Council is a **coordination and advice body of the producers of official statistics**, chaired by Statistics Sweden's own Director General; it is not an independent watchdog like [[GB-OSR]], [[FR-ASP]] or [[EU-ESGAB]].

## Description

Established on 1 February 2002 by the government; its tasks and composition are regulated by Statistics Sweden's directive (2016:822). It advises and supports [[SE-SCB]] in its coordinating role: promoting cooperation between the statistical agencies, advising them on principle matters of quality and on facilitating data provision, keeping a list of their statistical products and compiling an annual publishing plan, and, by 31 March each year, reporting to the Government on the system for official statistics, including an analysis of the quality evaluations the agencies must carry out under section 13 a of the Official Statistics Ordinance (2001:100). It consists of at most twelve agency directors and a chair; six seats are permanent (the Swedish Social Insurance Agency, Forest Agency, National Board of Health and Welfare, Energy Agency, Board of Agriculture and National Agency for Education), the others appointed by Statistics Sweden for up to three years. It meets at least once a year.

## Relationships

`part-of` [[SE]] (anchor edge); `related-to` [[SE-SCB]].
