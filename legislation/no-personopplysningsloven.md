---
id: NO-PERSONOPPLYSNINGSLOVEN
type: law
name: Lov om behandling av personopplysninger
alternative_names:
  - Personopplysningsloven
  - Personal Data Act
  - LOV-2018-06-15-38
description: >
  Norwegian act of 15 June 2018 on the processing of personal data, in force
  from 20 July 2018. It gives the General Data Protection Regulation effect
  in Norwegian law following the Regulation's incorporation into Annex XI of
  the EEA Agreement by Decision of the EEA Joint Committee No 154/2018 of
  6 July 2018, and designates Datatilsynet as the supervisory authority.

level: national
country: "NO"
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: 2018-07-20
end_date: null
last_verified: "2026-08-22"
previous_version: null
successor: null

domains:
  - DOMAIN-GOVERNMENT
organisations: []
related_entities:
  - EU-GDPR
  - NO-DATATILSYNET
  - INTL-EEA-JCD-154-2018
  - IS-PERSONUVERNDARLOG
  - LI-DSG
relationships:
  - type: implements-requirement-from
    target: EU-GDPR
    source: fact
    evidence: "Confirmed by reading lovdata.no directly (2026-08-22), the Act's own metadata record: 'Lov om behandling av personopplysninger (personopplysningsloven) ... Ikrafttredelse 20.07.2018 ... Kunngjort 15.06.2018 ... Korttittel Personopplysningsloven ... EØS/EU/Schengen EØS-avtalen vedlegg XI nr. 5e (forordning (EU) 2016/679).' Independently confirmed on EUR-Lex's own text of JCD No 154/2018, read directly: 'OJ L 183, 19.7.2018, pp. 23–26,' which recites Regulation (EU) 2016/679 (the GDPR) as the act incorporated. linklaters.com and dlapiperdataprotection.com, both read directly, corroborate the 20 July 2018 effective date and Datatilsynet's designation."
    confidence: medium
    valid_from: 2018-07-20
    valid_until: null
  - type: references
    target: INTL-EEA-JCD-154-2018
    source: fact
    evidence: "Confirmed by reading eur-lex.europa.eu's own text of the Decision directly (2026-08-22): 'Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 amending Annex XI ... and Protocol 37 ... to the EEA Agreement [2018/1022] ... OJ L 183, 19.7.2018, pp. 23–26.' lovdata.no's own metadata record for this Act cites the same instrument: 'EØS-avtalen vedlegg XI nr. 5e (forordning (EU) 2016/679).'"
    confidence: medium
    valid_from: 2018-07-20
    valid_until: null

sources:
  - title: "Decision of the EEA Joint Committee No 154/2018 of 6 July 2018 amending Annex XI and Protocol 37 to the EEA Agreement"
    url: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2018.183.01.0023.01.ENG"
    publisher: "EUR-Lex / Publications Office of the European Union"
    accessed: "2026-08-22"
  - title: "Lov om behandling av personopplysninger (personopplysningsloven), LOV-2018-06-15-38"
    url: "https://lovdata.no/dokument/NL/lov/2018-06-15-38"
    publisher: "Lovdata"
    accessed: "2026-08-22"
  - title: "Data Protected — Norway"
    url: "https://www.linklaters.com/en/insights/data-protected/data-protected---norway"
    publisher: "Linklaters"
    accessed: "2026-08-22"
  - title: "Data protection laws in Norway"
    url: "https://www.dlapiperdataprotection.com/index.html?t=law&c=NO"
    publisher: "DLA Piper"
    accessed: "2026-08-22"
---

# Personopplysningsloven (LOV-2018-06-15-38)

> **Verified 2026-08-22.** All four cited pages were read directly and
> confirm the claims below, verbatim in places — including
> `eur-lex.europa.eu`, whose bot-wall status has changed; see [[NO]] for
> the pattern this fits.

## Description

Confirmed by reading lovdata.no's own metadata record for the Act
directly (2026-08-22): "Ikrafttredelse 20.07.2018 ... Kunngjort
15.06.2018." Norway's Personal Data Act, adopted **15 June 2018** and in
force from **20 July 2018**. It gives [[EU-GDPR]] effect in Norwegian law and
designates [[NO-DATATILSYNET]] as the supervisory authority — confirmed
verbatim on linklaters.com: "The Norwegian Data Protection Authority will
continue to act as the supervisory authority in Norway."

## The decision in the middle is now an entity

When this act was written, [[INTL-EEA-JCD-154-2018]] existed only as a
citation — named in the description, in the `implements-requirement-from`
evidence, and in the sources. It is now modelled, and this act carries a
`references` edge to it.

Two sibling acts were written at the same time: [[IS-PERSONUVERNDARLOG]] and
[[LI-DSG]]. `discovery/candidates.md` had asked whether the pattern this
entity established *"generalises or is Norway-specific"* — see
[[IS-PERSONUVERNDARLOG]] for the three-way comparison that answers it.

## The two-month gap that proves the point

| Date | Event |
|---|---|
| 25 May 2018 | [[EU-GDPR]] becomes applicable **in the member states** |
| 15 June 2018 | This Act adopted |
| **6 July 2018** | **JCD No 154/2018 incorporates the GDPR into Annex XI of the EEA Agreement** |
| **20 July 2018** | The Act enters into force — **the GDPR takes effect in Norway** |

For **eight weeks** in 2018 the GDPR was in force across the Union and had
no effect in Norway. Nothing comparable happened in [[NL]], [[DE]], [[BE]],
[[FR]], [[ES]], [[PL]] or [[IE]], because in a member state a regulation
does not wait for anything.

That gap is the clearest available demonstration of why [[NO]] carries no
`applies-in` edge from [[EU-GDPR]].

## Why `implements-requirement-from` is still the right type

The Atlas's national GDPR instruments — [[NL-UAVG]], [[DE-BDSG]],
[[ES-LOPDGDD]], [[PL-ODO]] — all carry this type, and so does this one.

That is deliberate. The relationship type describes what the **national
instrument does**: it gives effect to requirements originating in a
supra-national instrument. That is true here in exactly the same sense.

What differs is not this edge but the **absent** one. A member state's GDPR
act sits alongside `EU-GDPR applies-in <country>`. Norway's sits alone,
because the Regulation reaches Norway through an EEA Joint Committee
decision the Atlas does not hold.

**Read the pair, not either half.** `implements-requirement-from` present
and `applies-in` absent *is* the EEA pattern, expressed in the only
vocabulary the Atlas currently has.

## An adaptation that survives into the graph

JCD No 154/2018 did not incorporate the Regulation unchanged. It required
Norway to notify its supervisory authority to the **EEA Joint Committee**
rather than to the European Commission, and provided for the GDPR's
cooperation mechanisms to run between [[NO-DATATILSYNET]] and member-state
authorities through EEA-specific channels.

This is why [[NO-DATATILSYNET]] carries no `participates-in` [[EU-EDPB]]
edge where [[NL-AP]] does.

## Not modelled

- A finding from lovdata.no's own metadata record, read directly this pass:
  the Act was last amended by **LOV-2021-06-18-124**, effective **1 January
  2022**, and itself replaced an earlier act, **LOV-2000-04-14-31**. Neither
  amendment is modelled — the entity records the Act as originally adopted.
- The Act's **national derogations** under the GDPR's opening clauses — the
  material [[DE-BDSG]] and [[NL-UAVG]] describe for their countries.
- The **e-Privacy** and sector-specific Norwegian rules.

## Sources

Listed in frontmatter, all four read directly this pass. The EUR-Lex
citation for JCD 154/2018 and the Lovdata citation for the Act are both
official; the two law-firm surveys are secondary.
