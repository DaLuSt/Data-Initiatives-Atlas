---
id: IE-NSB
type: organisation
name: "National Statistics Board"
alternative_names:
  - "NSB"
description: >
  Irish statutory board, established in November 1994 under the Statistics
  Act 1993, that steers the strategic direction of the Central Statistics
  Office and sets priorities for official statistics in Ireland. It has
  eight members.

level: national
country: IE
region: null

status: active
organisation_role: advisory
confidence: medium
coverage: low
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-10-11"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - IE
  - IE-CSO
relationships:
  - type: part-of
    target: IE
    source: fact
    evidence: "Scope anchor under metadata/relationship-types.md §2.3. nsb.ie, read directly (2026-10-11), is the site of the Irish National Statistics Board, which it says was 'established on a statutory basis in November 1994 under the Statistics Act 1993'."
    confidence: high
    valid_from: null
    valid_until: null
  - type: related-to
    target: IE-CSO
    source: fact
    evidence: "nsb.ie, read directly (2026-10-11): under the Act the Board steers the Central Statistics Office's overall strategic direction and sets priorities for the development of official statistics in Ireland; the CSO's Director General sits on it ex officio and the CSO nominates its Secretary. A steering relationship; no stronger type is used."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "About us — National Statistics Board"
    url: "https://nsb.ie/aboutus/"
    publisher: "National Statistics Board (Ireland)"
    accessed: "2026-10-11"
---

# National Statistics Board (Ireland)

> **Created 2026-10-11** (roadmap #459). The Board's own site was read directly; the Statistics Act 1993 itself was not, and gov.ie's page on the Board returned HTTP 403. The Board is a strategy-setting body over the statistical office, not an independence-compliance watchdog like [[GB-OSR]] or [[FR-ASP]].

## Description

The Board "was set up as a non-statutory body in 1986" and was "established on a statutory basis in November 1994 under the Statistics Act 1993". It steers the strategic direction of the Central Statistics Office ([[IE-CSO]]) and sets priorities for official statistics in Ireland. It has eight members: two chosen by the Taoiseach, three by organisations representing data users and information providers, two senior officials from the Departments of Finance and the Taoiseach, and the CSO's Director General ex officio. The Taoiseach appoints the Chairperson from the five nominated members; the CSO nominates the Secretary. Its term of office is not stated on the page read; a search summary gives three years and a different breakdown of the membership, which is why neither is repeated here.

## Relationships

`part-of` [[IE]] (anchor edge); `related-to` [[IE-CSO]].
