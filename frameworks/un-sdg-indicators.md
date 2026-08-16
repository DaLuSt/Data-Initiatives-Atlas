---
id: UN-SDG-INDICATORS
type: framework
name: Global indicator framework for the Sustainable Development Goals
alternative_names:
  - Global SDG indicator framework
  - SDG global indicators
description: >
  The global indicator framework for monitoring the Sustainable Development
  Goals of the 2030 Agenda. It was designed by an Inter-Agency and Expert
  Group under the supervision of the United Nations Statistical Commission,
  was revised in 2020 and 2025, and consists of 234 unique indicators. The
  SDGs are monitored against it at global, regional, national, local and
  thematic levels.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: null
end_date: null
last_verified: null
previous_version: null
successor: null

domains: []
organisations:
  - UN-UNSC
related_entities:
  - UN-UNSC
  - EU-SDG-INDICATORS
relationships:
  - type: governed-by
    target: UN-UNSC
    source: fact
    evidence: "The global SDG indicator framework was revised in 2020 and 2025, resulting in a framework consisting of 234 unique indicators, and was designed by an Inter-Agency and Expert Group under the supervision of the UN Statistical Commission (ec.europa.eu/eurostat 'SDG – Introduction'; ec.europa.eu/eurostat/web/sdi/information-data). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "SDG — Introduction — Statistics Explained"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=SDG_-_Introduction"
    publisher: "Eurostat — European Commission"
  - title: "Sustainable development indicators — information on data"
    url: "https://ec.europa.eu/eurostat/web/sdi/information-data"
    publisher: "Eurostat — European Commission"
  - title: "SDG Indicators and Monitoring: Systems and Processes at the Global, National and Regional Level"
    url: "https://www.esdn.eu/fileadmin/ESDN_Reports/QR_48_Final_Final.pdf"
    publisher: "European Sustainable Development Network (ESDN)"
---

# Global SDG indicator framework

> **Sourcing caveat.** This entity was compiled from search-engine results
> only; the cited pages were confirmed to exist but were not read. See
> `discovery/unresolved.md` and `progress/current-batch.md`.

## Description

The global indicator framework monitors progress against the Sustainable
Development Goals of the 2030 Agenda. It was **designed by an Inter-Agency
and Expert Group under the supervision of [[UN-UNSC]]**, revised in **2020
and 2025**, and consists of **234 unique indicators**.

## The ID collision this entity was named around

`discovery/candidates.md` flagged it, and it is worth keeping visible
because the obvious ID is wrong:

> ⚠ **`EU-SDG` is already taken** — it is the **Single Digital Gateway**
> Regulation, added in Batch 8.

Two entirely unrelated things abbreviate to SDG in this Atlas's subject
area: the **Single Digital Gateway** and the **Sustainable Development
Goals**. `metadata/ontology.md` requires IDs to be stable once assigned, so
[[EU-SDG]] cannot be renamed to make room.

Hence `UN-SDG-INDICATORS` here and [[EU-SDG-INDICATORS]] for Eurostat's set
— both explicitly about the *indicator frameworks*, which is what is
actually modelled, rather than about the Goals in the abstract.

## The 2030 Agenda itself is not modelled

This entity is the **indicator framework**, not the Agenda. The 2030 Agenda
is a UN General Assembly resolution and a much larger object; nothing was
found for it in this batch beyond passing references, and creating a node
for it from those would produce exactly the thin, encyclopedic entity the
taxonomy's threshold rule prevents.

The consequence is that this framework carries `governed-by` to the
Statistical Commission — which is sourced — and no link to the policy
instrument it serves, which is not. Queued.

## Relationships

- `governed-by` [[UN-UNSC]].

[[EU-SDG-INDICATORS]] carries the `based-on` edge pointing here.

## Sources

Listed in frontmatter. Note the asymmetry worth fixing: **two of the three
sources are Eurostat pages**, and none is from UNSD or the Inter-Agency and
Expert Group. A global UN framework is described here entirely through
European and European-network documents.
