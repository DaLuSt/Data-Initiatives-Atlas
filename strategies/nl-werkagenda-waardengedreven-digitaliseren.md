---
id: NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN
type: strategy
name: Werkagenda Waardengedreven Digitaliseren
alternative_names:
  - Werkagenda Values-driven Digitalisation
description: >
  Dutch government work agenda for values-driven digitalisation, published
  4 November 2022 by State Secretary Van Huffelen as an implementation of
  the digitalisation policy paper, with five programme lines. Superseded
  the NL DIGIbeter agenda; its execution concluded after the fall of the
  Rutte IV cabinet, and attention shifted to the Nederlandse
  Digitaliseringsstrategie, though that strategy's own sources decline to
  characterise it as a formal successor.

level: national
country: NL
region: null

status: superseded
confidence: medium
coverage: medium
verification: primary-source

start_date: 2022-11-04
end_date: 2024-12-31
last_verified: "2026-09-05"
previous_version: NL-DIGIBETER
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - NL-BZK
related_entities:
  - NL-DIGIBETER
  - NL-NDS
relationships:
  - type: supersedes
    target: NL-DIGIBETER
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own kabinetsbeleid-digitalisering timeline page directly (2026-09-05): it frames a direct progression, 'The focus shifted from innovation and service delivery (NL Digibeter), toward values-driven digitalization (Werkagenda), to a government-wide strategy (NDS),' with the Werkagenda under the section heading '2022 tot 2024: Werkagenda Waardengedreven Digitaliseren' immediately following NL Digibeter's own dated section. This closes the successor gap [[NL-DIGIBETER]]'s prior pass left open, recording it there could not yet be a successor because this intervening strategy was not an Atlas entity."
    confidence: medium
    valid_from: 2022-11-04
    valid_until: null
  - type: applies-in
    target: NL
    source: fact
    evidence: "Confirmed by reading digitaleoverheid.nl's own Werkagenda document page directly (2026-09-05): it describes a work agenda of the Dutch national government implementing elements of the digitalisation policy paper."
    confidence: high
    valid_from: 2022-11-04
    valid_until: null

sources:
  - title: "Werkagenda Waardengedreven Digitaliseren"
    url: "https://www.digitaleoverheid.nl/document/werkagenda-waardengedreven-digitaliseren/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-05"
  - title: "Kabinetsbeleid Digitalisering"
    url: "https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/kabinetsbeleid-digitalisering/"
    publisher: "Digitale Overheid (Ministerie van BZK)"
    accessed: "2026-09-05"
  - title: "Geactualiseerde Werkagenda Waardengedreven Digitaliseren voor 2024"
    url: "https://www.rijksoverheid.nl/documenten/rapporten/2023/12/22/geactualiseerde-werkagenda-waardengedreven-digitaliseren-voor-2024"
    publisher: "Rijksoverheid"
---

# Werkagenda Waardengedreven Digitaliseren

This entity closes a gap flagged by [[NL-DIGIBETER]]'s and [[NL-NDS]]'s
own 2026-08-27 re-verification passes: both named this intervening
strategy directly from digitaleoverheid.nl's own timeline, but neither
could complete a `successor`/`previous_version` link to it because it did
not yet exist as an Atlas entity. Picked up from `discovery/unresolved.md`.

## Description

The Werkagenda Waardengedreven Digitaliseren is a Dutch central-government
work agenda for values-driven digitalisation. Confirmed by reading
digitaleoverheid.nl's own document page directly: it was **published 4
November 2022** by State Secretary Alexandra van Huffelen, as "an
implementation of elements from the policy brief on digitalization with
concrete goals and actions." It sets out **five programme lines**:
*meedoen* (participation), *vertrouwen* (trust), *regie op het digitale
leven* (control over one's digital life), a good digital government, and
strengthening the digital society in the Caribbean part of the Kingdom. An
updated version for 2024 was published 22 December 2023.

## Succession — the chain this entity completes

Reading digitaleoverheid.nl's own kabinetsbeleid-digitalisering timeline
page directly confirms a three-step progression in Dutch central
digitalisation strategy, narrated in the page's own words: "The focus
shifted from innovation and service delivery (NL Digibeter), toward
values-driven digitalization (Werkagenda), to a government-wide strategy
(NDS)." The same page dates this entity's run as **2022 to 2024** under
the heading "2022 tot 2024: Werkagenda Waardengedreven Digitaliseren."

`end_date: 2024-12-31` is a placeholder for "through 2024" — no source
read gives a specific closing date, only that execution concluded
following the fall of the Rutte IV cabinet on 7 July 2023 and that
attention shifted to the [[NL-NDS]], published 4 July 2025. The gap
between the Werkagenda's 2024 end and the NDS's 2025 start is not
explained by any source read and is not smoothed over here.

**`successor` is deliberately left `null`.** [[NL-NDS]] is the strategy
that followed chronologically, but that entity's own source
(digitaleoverheid.nl's continuation article) states explicitly that the
NDS "does not replace but connects existing plans" — [[NL-NDS]]'s own
entity file records the same refusal for its link back to [[NL-DIGIBETER]].
Asserting a `successor` edge here would draw a stronger conclusion than
the NDS's own announcement supports.

## Relationships

- Supersedes [[NL-DIGIBETER]] — the immediate predecessor in the Dutch
  central digitalisation-strategy lineage; the kabinetsbeleid timeline page
  treats this specific transition as a real succession ("NL Digibeter"
  ended), unlike the next step.
- **Not** a confirmed predecessor of [[NL-NDS]] in the formal
  `previous_version`/`successor` sense — see above.
- Applies in [[NL]].
- Coordinated by [[NL-BZK]].

## Sources

Listed in frontmatter, all three read directly this pass.
