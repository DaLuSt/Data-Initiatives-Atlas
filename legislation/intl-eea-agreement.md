---
id: INTL-EEA-AGREEMENT
type: law
name: Agreement on the European Economic Area
alternative_names:
  - EEA Agreement
  - EØS-avtalen
description: >
  International agreement signed at Oporto on 2 May 1992 and in force since
  1 January 1994, extending the European Union's single market to three
  EFTA states — Iceland, Liechtenstein and Norway. Its common rules are
  continuously updated by adding new EU legislation through decisions of the
  EEA Joint Committee, which is how an EU act comes to have effect in an EEA
  EFTA state.

level: international
country: null
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 1994-01-01
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - "NO"
  - IS
  - LI
  - CH
  - EU
  - NO-PERSONOPPLYSNINGSLOVEN
  - INTL-EEA-JCD-154-2018
relationships:
  - type: applies-in
    target: "NO"
    source: fact
    evidence: "Confirmed verbatim by reading europarl.europa.eu's own Fact Sheet 169 directly (2026-08-22): 'The EEA Agreement was signed on 2 May 1992 and entered into force on 1 January 1994.' eur-lex.europa.eu's summary, also read directly, confirms it extends the single market to Iceland, Liechtenstein and Norway and describes the Joint Committee mechanism: 'The EEA Joint Committee meets on a regular basis and takes decisions — by consensus — concerning the incorporation of EU legislation into the EEA Agreement.' The specific signing location 'Oporto' was NOT independently re-confirmed this pass — neither source names the city — and is retained from the original sourcing rather than dropped. government.is could not be read: it is a JavaScript-rendered single-page application and returned no static content."
    confidence: medium
    valid_from: 1994-01-01
    valid_until: null

sources:
  - title: "Agreement on the European Economic Area (summary)"
    url: "https://eur-lex.europa.eu/EN/legal-content/summary/agreement-on-the-european-economic-area.html"
    publisher: "EUR-Lex / Publications Office of the European Union"
    accessed: "2026-08-22"
  - title: "The European Economic Area (EEA), Switzerland and the North — Fact Sheet 169"
    url: "https://www.europarl.europa.eu/factsheets/en/sheet/169/the-european-economic-area-eea-switzerland-and-the-north."
    publisher: "European Parliament"
    accessed: "2026-08-22"
  - title: "European Economic Area (EEA) — General information"
    url: "https://www.government.is/topics/foreign-affairs/iceland-in-europe/european-economic-area/"
    publisher: "Government of Iceland"
    accessed: "2026-08-22"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 amending Annex XI and Protocol 37 to the EEA Agreement"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.183.01.0023.01.ENG"
    publisher: "EUR-Lex / Publications Office of the European Union"
    accessed: "2026-08-22"
  - title: "Lov om behandling av personopplysninger (personopplysningsloven), LOV-2018-06-15-38"
    url: "https://lovdata.no/dokument/NL/lov/2018-06-15-38"
    publisher: "Lovdata"
    accessed: "2026-08-22"
---

# Agreement on the European Economic Area

> **Verified 2026-08-22.** EUR-Lex's own summary and the European
> Parliament's Fact Sheet 169 were read directly and confirm the claims
> below verbatim. `government.is` is a JavaScript single-page
> application and returned no static content to read. The signing city
> "Oporto" was not independently re-confirmed by either source and is
> retained from the original sourcing; the Norwegian name "EØS-avtalen"
> is confirmed instead on lovdata.no, added as a source this pass.

## Description

Confirmed verbatim by reading europarl.europa.eu directly (2026-08-22):
"The EEA Agreement was signed on 2 May 1992 and entered into force on
1 January 1994." Signed **2 May 1992**, in force since **1 January 1994**. It
extends the EU's single market to three of the four EFTA states — **Iceland,
Liechtenstein and Norway** — with free movement of goods, services, capital
and persons.

## The mechanism this entity exists to make visible

The EEA Agreement's defining feature is that it is **not static**. Its
common rules are continuously updated by adding new EU legislation through
**decisions of the EEA Joint Committee**, taken every few weeks.

That is the route by which an EU act comes to have effect in an EEA EFTA
state, and it is the thing the Atlas could describe in prose and not draw.

The worked example is [[EU-GDPR]] and Norway:

| Date | Event |
|---|---|
| 25 May 2018 | GDPR applicable **in the member states** |
| **6 July 2018** | **JCD No 154/2018 incorporates the GDPR into Annex XI of this Agreement** |
| 20 July 2018 | [[NO-PERSONOPPLYSNINGSLOVEN]] in force — the GDPR takes effect in Norway |

**Eight weeks of divergence.** A member state cannot have that gap.

## Why this entity carries `applies-in` [[NO]] and no EU instrument does

The distinction is the whole point.

- **The EEA Agreement applies in Norway.** Norway is a party to it. That is
  a plain, sourced statement of territorial application, and it is the edge
  asserted here.
- **[[EU-GDPR]] does not apply in Norway** in the sense `applies-in` carries
  elsewhere in this repository — of its own force, or through a
  transposition the instrument itself requires. It has effect there because
  *this Agreement* was amended to include it.

So [[NO]] is reached, correctly, through the instrument that actually
reaches it.

## The chain's middle is now an entity

This section previously warned that **JCD No 154/2018 was not an entity**,
that the Atlas could therefore draw only the endpoints of the EEA route, and
that the chain's middle was *"recorded in prose here and on
[[NO-PERSONOPPLYSNINGSLOVEN]]"*.

[[INTL-EEA-JCD-154-2018]] now exists, and the chain is drawable end to end:

```
EU-GDPR ◀─ references ─ INTL-EEA-JCD-154-2018 ─ amends ─▶ INTL-EEA-AGREEMENT
                                 │ applies-in
                     ┌───────────┼───────────┐
                     ▼           ▼           ▼
                    NO          IS          LI
```

**Only this one decision is modelled**, and the original caution still holds
for the rest: cataloguing every Joint Committee decision that incorporates an
EU act into this Agreement is a large piece of work, and none of the others
is an entity. This one was created because three national data protection
acts and this Agreement were all describing it in prose.

## Switzerland signed it and never joined

Confirmed by reading europarl.europa.eu directly (2026-08-22):
"Switzerland chose not to ratify the agreement following a negative
referendum on the matter." [[CH]] never became a party to the Agreement
and remains an EFTA member outside the EEA, which is why its relationship
with the Union runs through bilateral agreements instead. The specific
claims that Switzerland *signed* the Agreement in 1992 and that the
referendum fell in **December 1992** were not independently re-confirmed
this pass — the Parliament's fact sheet states only the outcome, not
those details — and are retained from the original sourcing.

That is why this entity carries `applies-in` to Norway and **not** to
Switzerland, and it is the cleanest available illustration that the two
non-member countries in this Atlas are in genuinely different positions.

## Not modelled

- **Iceland and Liechtenstein**, the other two EEA EFTA states. Adding
  either would show whether the Norwegian pattern generalises.
- ~~The **EEA Joint Committee**, **EFTA**, the **EFTA Surveillance
  Authority** and the **EFTA Court**~~ — now [[INTL-EEA-JOINT-COMMITTEE]],
  [[INTL-EFTA]], [[INTL-EFTA-SURVEILLANCE-AUTHORITY]] and
  [[INTL-EFTA-COURT]], all created in the same pass as this note.
- The **Annexes and Protocols**. Annex XI (electronic communication,
  audiovisual services and information society) is the one that matters for
  this Atlas and is named in the evidence rather than modelled.
- The **1994 EU enlargement**, which took Austria, Finland and Sweden out of
  the EFTA side of the Agreement and into the Union.

## Sources

Listed in frontmatter, plus lovdata.no added this pass for the Norwegian
name. EUR-Lex's summary and the European Parliament's fact sheet were
read directly; `government.is` could not be (JS-rendered, no static
content); the EUR-Lex JCD citation is covered by
[[INTL-EEA-JCD-154-2018]]'s own re-verification.
