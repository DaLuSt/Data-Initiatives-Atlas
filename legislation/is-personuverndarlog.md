---
id: IS-PERSONUVERNDARLOG
type: law
name: Lög um persónuvernd og vinnslu persónuupplýsinga nr. 90/2018
alternative_names:
  - Persónuverndarlög
  - Act No. 90/2018 on Data Protection and the Processing of Personal Data
  - Icelandic Data Protection Act
description: >
  Icelandic act of 27 June 2018 on data protection and the processing of
  personal data, in force from 15 July 2018. It gives the General Data
  Protection Regulation effect in Icelandic law following the Regulation's
  incorporation into Annex XI of the EEA Agreement by Decision of the EEA
  Joint Committee No 154/2018 of 6 July 2018, and replaces Act No. 77/2000
  on the Protection of Privacy as regards the Processing of Personal Data.
  Persónuvernd continues as the supervisory authority.

level: national
country: IS
region: null

status: active
confidence: medium
coverage: medium
verification: search-only

start_date: 2018-07-15
end_date: null
last_verified: "2026-08-21"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations:
  - IS-PERSONUVERND
related_entities:
  - EU-GDPR
  - INTL-EEA-JCD-154-2018
  - INTL-EEA-AGREEMENT
  - IS-PERSONUVERND
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Iceland's Act on Data Protection and the Processing of Personal Data (Act No. 90/2018) implements the EU GDPR into Icelandic law via the EEA Agreement; the Althingi enacted it on 27 June 2018 and it entered into force on 15 July 2018, replacing Act No. 77/2000; the GDPR does not apply as binding domestic law in Iceland without a national implementing act (wipo.int WIPOLex 18498 'Act No. 90/2018 of June 27, 2018'; linklaters.com 'Data Protected — Iceland'; dlapiperdataprotection.com Iceland). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-07-15
    valid_until: null
  - type: references
    target: INTL-EEA-JCD-154-2018
    source: fact
    evidence: "The GDPR was incorporated into Annex XI of the EEA Agreement by Decision of the EEA Joint Committee No 154/2018 of 6 July 2018, which is the route by which it reaches Iceland; the national act domesticates it (eur-lex.europa.eu ELI dec/2018/1022/oj; wipo.int WIPOLex 18498; dlapiperdataprotection.com Iceland). NOT READ — search-only."
    confidence: medium
    valid_from: 2018-07-15
    valid_until: null

sources:
  - title: "Act No. 90/2018 of June 27, 2018, on Data Protection and the Processing of Personal Data (Iceland)"
    url: "https://www.wipo.int/wipolex/en/legislation/details/18498"
    publisher: "WIPO Lex — World Intellectual Property Organization"
  - title: "Data Protected — Iceland"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---iceland"
    publisher: "Linklaters"
  - title: "Data protection laws in Iceland"
    url: "https://www.dlapiperdataprotection.com/index.html?t=law&c=IS"
    publisher: "DLA Piper"
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018"
    url: "https://eur-lex.europa.eu/eli/dec/2018/1022/oj"
    publisher: "EUR-Lex — Publications Office of the European Union"
---

# Persónuverndarlög (Act No. 90/2018)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read — retrieval is blocked by
> the network egress proxy. `verification: search-only`.

## Description

Iceland's data protection act, enacted by the **Althingi on 27 June 2018**
and in force from **15 July 2018**. It replaced **Act No. 77/2000** on the
protection of privacy as regards the processing of personal data, and gives
[[EU-GDPR]] effect in Icelandic law. [[IS-PERSONUVERND]] continues as the
supervisory authority.

The sources are explicit about why a national act was needed at all: **the
GDPR does not apply as binding domestic law in Iceland without one.** An EEA
EFTA state is not reached by an EU regulation directly.

## The Norwegian pattern generalises

`discovery/candidates.md` asked exactly this question — *"Adding either
[Iceland or Liechtenstein] would show whether the Norwegian EEA pattern
generalises or is Norway-specific."* Placing the three acts side by side
answers it:

| | Norway | Iceland | Liechtenstein |
|---|---|---|---|
| Act | [[NO-PERSONOPPLYSNINGSLOVEN]] | this entity | [[LI-DSG]] |
| Adopted | 15 June 2018 | 27 June 2018 | 4 October 2018 |
| In force | 20 July 2018 | 15 July 2018 | 1 January 2019 |
| Replaces | earlier personal data act | Act No. 77/2000 | earlier DSG |
| Authority | [[NO-DATATILSYNET]] | [[IS-PERSONUVERND]] | [[LI-DATENSCHUTZSTELLE]] |
| Route | [[INTL-EEA-JCD-154-2018]] | [[INTL-EEA-JCD-154-2018]] | [[INTL-EEA-JCD-154-2018]] |

**The pattern is not Norway-specific.** All three states did the same three
things — Joint Committee decision, national implementing act, existing
authority continued — and all three did it in 2018, in a five-month window,
after the same Joint Committee decision.

What differs is only the timing, and Iceland's is the case that shows the
national act can precede the EU-side incorporation taking effect: the
Althingi enacted on **27 June**, the Joint Committee decided on **6 July**,
and the Icelandic act entered into force on **15 July**.

## Relationships

- `implements-requirement-from` [[EU-GDPR]] — the same type the Atlas uses
  for the EU→national legislative chain, and the same one
  [[NO-PERSONOPPLYSNINGSLOVEN]] carries.
- `references` [[INTL-EEA-JCD-154-2018]], the decision that put the GDPR into
  the EEA Agreement. This is the edge Norway's act could not carry when it
  was written, because the decision was not modelled.

## Sources

Listed in frontmatter — the WIPO Lex record of the act, two comparative law
surveys, and the EUR-Lex record of the Joint Committee decision.
