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
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-28"
previous_version: null
successor: null

domains: []
organisations:
  - UN-UNSC
related_entities:
  - UN-UNSC
  - EU-SDG-INDICATORS
  - UN-2030-AGENDA
relationships:
  - type: governed-by
    target: UN-UNSC
    source: fact
    evidence: "Confirmed by reading Eurostat's own 'SDG — Introduction' Statistics Explained page directly (2026-08-28): the framework 'was designed by an Inter-Agency and Expert Group under the supervision of the UN Statistical Commission,' and following the General Assembly's initial 232-indicator list in July 2017, comprehensive reviews in 2020 and 2025 produced 'a revised global SDG indicator framework consisting of 234 unique indicators.' The second cited page (ec.europa.eu/eurostat/web/sdi/information-data) was also read directly but describes the EU's own 102-indicator SDG set rather than the global framework, so it corroborates the entity's general subject area without independently confirming the UNSC-supervision claim."
    confidence: high
    valid_from: null
    valid_until: null
  - type: implements
    target: UN-2030-AGENDA
    source: fact
    evidence: "Confirmed by reading Eurostat's 'SDG — Introduction' page directly (2026-08-28), which states the framework was created specifically to monitor progress toward the 2030 Agenda's 17 SDGs, plus [[UN-2030-AGENDA]]'s own cited un.org/sdgs.un.org and unfpa.org pages (also read directly this pass — see that entity), which confirm the Agenda's adoption as A/RES/70/1 on 25 September 2015 with 17 goals and 169 targets."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "SDG — Introduction — Statistics Explained"
    url: "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=SDG_-_Introduction"
    publisher: "Eurostat — European Commission"
    accessed: "2026-08-28"
  - title: "Sustainable development indicators — information on data"
    url: "https://ec.europa.eu/eurostat/web/sdi/information-data"
    publisher: "Eurostat — European Commission"
    accessed: "2026-08-28"
  - title: "SDG Indicators and Monitoring: Systems and Processes at the Global, National and Regional Level"
    url: "https://www.esdn.eu/fileadmin/ESDN_Reports/QR_48_Final_Final.pdf"
    publisher: "European Sustainable Development Network (ESDN)"
---

# Global SDG indicator framework

> **Verified 2026-08-28.** Two of three cited pages were read directly.
> Eurostat's own "SDG — Introduction" page states the Inter-Agency and
> Expert Group / UN Statistical Commission supervision and the 234-indicator
> count in its own words, including a detail not previously recorded here:
> the General Assembly's *initial* list (July 2017) held 232 indicators,
> before the 2020 and 2025 reviews brought it to 234. The ESDN PDF returned
> only unparseable binary and was not read.

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

Listed in frontmatter, two of three read directly this pass (both Eurostat
pages). The ESDN PDF was fetched but returned unparseable binary rather than
readable text. The asymmetry flagged previously still stands and is
reconfirmed rather than resolved: **every source actually read is a
Eurostat page**, and none is from UNSD or the Inter-Agency and Expert Group
itself. A global UN framework is described here entirely through European
documents — accurate on the facts checked, but still a one-sided citation
base worth closing with a direct UNSD/sdgs.un.org indicator-framework page
in a future pass.
