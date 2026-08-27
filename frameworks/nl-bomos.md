---
id: NL-BOMOS
type: framework
name: Beheer- en OntwikkelModel voor Open Standaarden
alternative_names:
  - BOMOS
description: >
  Dutch model describing a layered set of activities relevant to developing
  and managing open standards. Used by Dutch standards-management
  organisations as a common reference for how a standard should be
  developed, governed and maintained.

level: national
country: NL
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source

start_date: null
end_date: null
last_verified: "2026-08-27"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-LOGIUS
  - NL-FORUM-STANDAARDISATIE
related_entities:
  - NL-GEONOVUM
relationships:
  - type: derived-from
    target: NL-FORUM-STANDAARDISATIE
    source: fact
    evidence: "Confirmed by reading forumstandaardisatie.nl's own 2022 BOMOS presentation directly (2026-08-27): BOMOS 'began in 2006 when a working group at Bureau Forum Standaardisatie started developing the methodology,' with version 1 published in 2009 and version 2 in 2010, expanding in 2012 as 'BOMOS2i' under Forum Standaardisatie's leadership. ecp.nl, also read directly, corroborates: BOMOS was 'developed based on an earlier Forum Standaardisatie report and refined through workshops' with Kennisnet/EduStandaard, Geonovum and other parties."
    confidence: high
    valid_from: null
    valid_until: null
  - type: maintained-by
    target: NL-LOGIUS
    source: fact
    evidence: "Confirmed by reading logius-standaarden.github.io's own BOMOS 3.0.1 'Fundament' document directly (2026-08-27), dated 2 November 2023: 'Logius serves as the publisher and primary maintainer,' with editors from Logius, HAN University of Applied Sciences and TNO. forumstandaardisatie.nl's own presentation, also read directly, confirms the handover: 'Around 2017, Logius took over further development, adding a standards framework,' with version 3.0.0 released in 2022. This closes the maintainer-uncertainty question the prior text left open for Logius's side of it; Forum Standaardisatie's historical role (2006–2017) is now dated precisely rather than left as a vague origin claim."
    confidence: high
    valid_from: null
    valid_until: null

sources:
  - title: "Beheer- en OntwikkelModel voor Open Standaarden (BOMOS)"
    url: "https://ecp.nl/beheer-en-ontwikkelmodel-voor-open-standaarden-bomos/"
    publisher: "ECP | Platform voor de InformatieSamenleving"
    accessed: "2026-08-27"
  - title: "BOMOS: The Foundation 3.0.1"
    url: "https://logius-standaarden.github.io/publicatie/bomos/fundament/en/3.0.1/"
    publisher: "Logius"
    accessed: "2026-08-27"
  - title: "Het Beheer- en Ontwikkelmodel voor Open Standaarden (BOMOS) — presentatie"
    url: "https://www.forumstandaardisatie.nl/vergaderingen/2022/fs-20220608-5-presentatie-bomos"
    publisher: "Forum Standaardisatie"
    accessed: "2026-08-27"
  - title: "Beheer- en Ontwikkelmodel voor Open Standaarden Versie 2 — deel 1: de basis"
    url: "https://www.forumstandaardisatie.nl/sites/default/files/BFS/4-basisinformatie/publicaties/BOMOS2-deel-1-(de-basis).pdf"
    publisher: "Forum Standaardisatie"
---

# BOMOS

> **Verified 2026-08-27.** Three of four cited pages were read directly,
> and they resolve the prior text's central open question: BOMOS's current
> maintainer. `verification` moves from `search-only` to `primary-source`;
> a `maintained-by` [[NL-LOGIUS]] relationship is now asserted with a dated
> handover, where previously none was asserted to either named organisation.

## Description

BOMOS is described as a tool for and by the standardisation community: it
sets out a layered set of activities relevant to developing and managing
open standards. In effect it is the Dutch meta-standard — a standard for how
to run a standard — which is why it sits at the centre of several other
Atlas entities rather than at the edge.

Confirmed by reading forumstandaardisatie.nl's own presentation directly,
its history now has real dates: it **began in 2006** as a working group at
Bureau Forum Standaardisatie; **version 1** was published in **2009**,
**version 2** in **2010**; it expanded into **BOMOS2i in 2012** under Forum
Standaardisatie; **around 2017, Logius took over** further development,
adding a standards framework; and **version 3.0.0** was released in
**2022**. Version 3.0.1 of the "Fundament," read directly at
logius-standaarden.github.io, is dated **2 November 2023** and lists Erwin
Folmer (HAN University of Applied Sciences), Gül Işik and Edwin Wisse (both
Logius), and Wouter van den Berg (TNO) as editors. The methodology was
refined through knowledge from Geonovum, Kadaster, TNO and Logius
departments, per the forumstandaardisatie.nl presentation.

Its practical force shows in [[NL-GEONOVUM]]'s use: Geonovum applies BOMOS
to every standard it manages, and has held the Forum Standaardisatie
designation "Excellent management process" (uitstekend beheerproces) for
its base standards since December 2014 — this specific claim was not
re-confirmed by any page read this pass and is carried over from the prior
text.

**The maintainer question is now resolved for the current custodian.**
BOMOS originates from a 2006 Forum Standaardisatie working group, but since
around 2017 its development has been led by [[NL-LOGIUS]], which
logius-standaarden.github.io's own document, read directly, names as
publisher and primary maintainer of the current (3.0.1) version. Both
organisations remain in `organisations:`, reflecting their sequential
historical and current roles, and both now carry sourced relationships
rather than an unresolved question.

## Relationships

- `derived-from` [[NL-FORUM-STANDAARDISATIE]] — its 2006 origin as a Forum
  Standaardisatie working-group methodology, confirmed this pass with dates.
- `maintained-by` [[NL-LOGIUS]] — **new this pass**, closing the maintainer
  gap: Logius is BOMOS's current publisher and maintainer since taking over
  development around 2017.
- Applied by [[NL-GEONOVUM]] to all standards it manages.

## Sources

Listed in frontmatter, three of four read directly this pass. The BOMOS2
Version 2 PDF was not re-fetched.
