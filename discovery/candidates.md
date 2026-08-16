# Candidates

Entities that appear potentially relevant but have not yet been researched
and sourced enough to add to the graph. Move a row here to a real entity
file once it has a `type`, an ID, at least one authoritative source, and a
clear enough relationship to the rest of the graph — then delete the row.

Do not add anything here without noting where it was seen.

> **Nothing on this page has been read.** Every row below was compiled from
> search-engine results during the Spain batch follow-up; the pages cited in
> *Where seen* were returned by a search index and confirmed to exist, but
> page retrieval is blocked (`EGRESS_BLOCKED`, 403 at the proxy tunnel).
> **These are leads, not findings.** A candidate becomes an entity only
> after its sources have actually been read.

> **Proposed IDs are written in `backticks`, not `[[wikilinks]]`.** A
> wikilink to an entity that does not exist fails `validate_links`. Only
> entities that are already in the Atlas are linked.

---

## Why this page is about the UN layer

`validation/reports.md` (Batch 15) recorded the Atlas's largest structural
defect, and five country batches have not touched it:

> **The UN layer is an island** — zero relationships connect its entities to
> any EU or national entity. `UN → anything` is **0**.

The target architecture is UN → EU → national → sector. What exists is a
well-connected EU↔national graph and a **separate, unattached UN
component**. Every country batch has made the EU↔national half denser while
leaving the vertical gap exactly where it was.

The reason it has survived is consistent and worth stating plainly: the
links were **refused for want of a source**, not overlooked. `UN-UNSD` →
[[EU-EUROSTAT]] has been examined and refused three times.

**This page exists because that refusal now looks avoidable.** The searches
below found candidate sources for several of these links on the first
attempt — including one Eurostat page that appears to state the
statistics connection outright. The gap may be less a research problem than
a *missing intermediate entity* problem: in most of these clusters, the
edge that would not resolve is one the Atlas has no node for.

---

## 1. Bridge entities — the ones that would close the gap directly

**UNECE is the single most obvious absence in the Atlas.** It is a UN
regional commission whose region *is* Europe: the exact UN→EU joint the
Atlas is missing, and the parent body of three separate clusters below
(statistics, environmental information, e-business standards).

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **UN Economic Commission for Europe (UNECE)** — `UN-UNECE` | organisation | UN, `level: international` | **The missing joint.** A UN regional commission for Europe, and the parent of UN/CEFACT, the Conference of European Statisticians and the Aarhus Convention. Almost every other row on this page hangs off it. Modelling it first would make the rest cheap | unece.org (multiple sections); referenced from ec.europa.eu Eurostat "Statistical cooperation" | Spain follow-up / 2026-08-16 | **Candidate — highest value** |
| **Conference of European Statisticians (CES)** — `UN-CES` | programme | UN (UNECE), `level: international` | Search results state that **Eurostat represents the EU in the CES, organised by UNECE**, alongside the UN Statistical Commission and the OECD statistics committee. If the Eurostat page says this, it is a `participates-in` edge from [[EU-EUROSTAT]] into the UN layer — **the single link that would close most of the vertical gap** | ec.europa.eu/eurostat Statistics Explained, "Statistical cooperation – introduction"; unece.org/statistics/ces | Spain follow-up / 2026-08-16 | **Candidate — read this page first** |
| **UN Statistical Commission** — `UN-UNSC` | organisation | UN, `level: international` | Currently **folded into [[UN-UNSD]]** on a single sourced sentence, which `discovery/unresolved.md` already flags as an open modelling question. The same Eurostat page reportedly names the Commission as a forum Eurostat sits in, so splitting it may be what unblocks the edge | same Eurostat page; ggim.un.org; UN SDG indicator framework material | Batch 13; re-raised 2026-08-16 | Candidate (modelling + link) |
| **European Statistical System (ESS)** — `EU-ESS` | framework | EU, `level: regional` | Already queued from the Spain batch as the fix for [[ES-INE]]'s weak `related-to` edge. It is **the European half of the same bridge**: Eurostat plus the national statistical offices. One entity would connect four national offices *and* give the CES/UNSC edges something structurally correct to attach to | ine.es "Qué es el SEE"; eur-lex.europa.eu summary "Estadísticas europeas" | Spain batch / 2026-08-16 | **Queued — see `research-queue.md`** |

**Why these four are grouped.** They are not four independent leads; they
are one chain the Atlas is missing the middle of:

```
   UN-UNSC / UN-CES  (global + European statistical governance)
            ▲
       participates-in?           ← the refused edge
            │
   EU-EUROSTAT ── part-of ──►  EU-ESS      ← does not exist
                                  ▲
                              part-of
                                  │
        ES-INE · NL-CBS · DE-DESTATIS · BE-STATBEL
```

The Atlas currently holds the bottom row and `EU-EUROSTAT`, and nothing
else. That is why five separate `→ Eurostat` and `→ UN-FPOS` links have all
been refused: **there is nowhere correct for them to point.**

---

## 2. Instruments that would give a genuine UN → EU → national chain

This cluster is the strongest on the page, and it is not about statistics.

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **Aarhus Convention** (Access to Information, Public Participation in Decision-making and Access to Justice in Environmental Matters) — `UN-AARHUS` | law / convention | UN (UNECE), `level: international` | **The best candidate in the Atlas for a first real UN → EU descent.** A UNECE convention signed 25 June 1998, in force 30 October 2001, to which **the EU and all 27 member states are Parties**. Access to information held by public authorities is squarely the Atlas's subject matter, and "all member states are Parties" is exactly the shape `applies-in` already models | environment.ec.europa.eu "The Aarhus Convention and the EU"; aarhusclearinghouse.unece.org | Spain follow-up / 2026-08-16 | **Candidate — highest value** |
| **Directive 2003/4/EC on public access to environmental information** — `EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE` | law | EU, `level: regional` | Reportedly **adopted because the EU became a party to the Aarhus Convention**. If so this is a sourced `implements-requirement-from` from an EU directive to a UN instrument — the first of its kind here — and it would then carry `applies-in` to all five modelled countries, with national transpositions to find in each | eur-lex.europa.eu CELEX 32003L0004; environment.ec.europa.eu | Spain follow-up / 2026-08-16 | **Candidate — highest value** |
| **2030 Agenda / global SDG indicator framework** — `UN-2030-AGENDA`, `UN-SDG-INDICATORS` | policy / framework | UN, `level: international` | 234 unique indicators, revised 2020 and 2025, designed by an Inter-Agency and Expert Group **under the supervision of the UN Statistical Commission**. Eurostat monitors the EU against ~100 indicators of which **55 are derived from or similar to the UN list**, and the Commission contributed an EU voluntary review in 2023. That is a quantified, sourceable descent | ec.europa.eu/eurostat "SDG – Introduction" and `/web/sdi/information-data`; ec.europa.eu/eurostat news "New EU SDG indicator list established" | Spain follow-up / 2026-08-16 | Candidate |

> ⚠ **ID collision warning.** `EU-SDG` is **already taken** — it is the
> **Single Digital Gateway** Regulation, added in Batch 8. A Sustainable
> Development Goals entity must not reuse it. Suggested:
> `EU-SDG-INDICATORS` for Eurostat's set, and `UN-SDG-INDICATORS` for the
> global framework. This is exactly the kind of clash
> `discovery/duplicates.md` exists to catch, and it would have been easy to
> walk into.

**Why the Aarhus chain matters more than the statistics one.** The
statistics gap is the one the Atlas has documented most, but it is blocked
on a *modelling* problem (the missing `EU-ESS`). Aarhus is blocked on
nothing but reading two pages, and it produces a complete vertical:

```
   UN-AARHUS  (UNECE convention, 1998)
        │  implements-requirement-from?
        ▼
   EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE  (2003/4/EC)
        │  applies-in
        ▼
   NL · DE · BE · FR · ES   ← national transpositions, all five to find
```

It also touches instruments already in the Atlas: environmental information
access is adjacent to [[EU-INSPIRE]], [[EU-OPEN-DATA-DIRECTIVE]] and the
national open-government acts ([[NL-WOO]], [[ES-LEY-37-2007]]). **No such
relationship is asserted** — the adjacency is a reason to research, not a
finding.

---

## 3. UN bodies already named in the Atlas but never modelled

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **UNESCO** — `UN-UNESCO` | organisation | UN, `level: international` | **Refused in Batch 13 for want of any usable source.** That refusal now looks reversible: search results describe UNESCO and the **European Commission signing an agreement** to accelerate implementation of the AI ethics Recommendation, with a €4 million budget and Global Forums hosted by Czechia and Slovenia under their EU Presidencies | unesco.org "Artificial intelligence: Partnership between UNESCO and the EU"; dig.watch | Batch 13; re-raised 2026-08-16 | **Candidate — refusal may be reversible** |
| **UNESCO Recommendation on the Ethics of AI** — `UN-AI-ETHICS-RECOMMENDATION` | framework | UN, `level: international` | Adopted **November 2021 by 193 member states** — nearly three years before the AI Act applied, and around two years before [[ES-AESIA]] was created. Would sit above [[EU-AI-ACT]] in a way the Atlas currently cannot show, and ~30 countries reportedly use it in national legislation | unesco.org/en/artificial-intelligence/recommendation-ethics; unesdoc.unesco.org | Spain follow-up / 2026-08-16 | Candidate |
| **UN/CEFACT** — `UN-CEFACT` | organisation | UN (UNECE), `level: international` | A **subsidiary intergovernmental body of UNECE** and the ECOSOC focal point for trade facilitation recommendations and **electronic business standards**. Produces standards of exactly the kind the Atlas models (UN/EDIFACT, UN/LOCODE, Core Components). EU adoption is **not** sourced yet — that is the gap to close | unece.org/trade/uncefact; unece.org/trade/uncefact/introduction | Spain follow-up / 2026-08-16 | Candidate (EU link unsourced) |
| **UN-GGIM** — `UN-GGIM` | programme | UN, `level: international` | UN Committee of Experts on Global Geospatial Information Management, established **July 2011 by ECOSOC resolution**. The geospatial counterpart to the statistical system, and the Atlas already has a geospatial cluster ([[EU-INSPIRE]], [[DOMAIN-GEOSPATIAL]], [[NL-GEONOVUM]], [[DE-GEOZG]]) with no international parent | ggim.un.org; un.org/globalgeospatial regional committees | Spain follow-up / 2026-08-16 | Candidate |
| **UN-GGIM: Europe** — `UN-GGIM-EUROPE` | programme | UN, `level: international` | The **European regional committee**, formally established 1 October 2014 in Chișinău. Its stated aim is aligning European geospatial work with the global UN-GGIM programme. INSPIRE is discussed in its context, though **no source read states a relationship** — that is the thing to verify | un-ggim-europe.org "About Us"; eurogeographics.org INSPIRE KEN webinar deck | Spain follow-up / 2026-08-16 | Candidate |
| **UN Statistical Commission's Big Data / Global Platform work** — `UN-GLOBAL-PLATFORM` | platform | UN, `level: international` | Mentioned around the UNSD and UN-GGIM material as the operational arm of UN big-data statistics work. Would be a second, independent attachment point for national statistical offices | ggim.un.org; unstats.un.org (not opened) | Spain follow-up / 2026-08-16 | Weak lead |

---

## 4. The non-UN international layer, which has the same problem

Not UN, but the same structural gap and — in one case — reportedly the same
source sentence.

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **OECD Committee on Statistics and Statistical Policy (CSSP)** — `INTL-OECD-CSSP` | programme | INTL, `level: international` | [[INTL-OECD]] has been in the Atlas since Batch 13 **with no instrument and no link to anything**. The same Eurostat "Statistical cooperation" page reportedly names the CSSP alongside the UNSC and CES as forums Eurostat sits in — so **one page read may close the OECD gap and the UN gap together** | ec.europa.eu/eurostat "Statistical cooperation – introduction" | Spain follow-up / 2026-08-16 | **Candidate — same page as row 1.2** |
| **EuroGeographics** — `EU-EUROGEOGRAPHICS` | organisation | EU, `level: regional` | European association of national mapping, cadastral and land registry authorities; appears throughout the UN-GGIM: Europe material. Would be the European node between UN-GGIM: Europe and national geospatial bodies, the same shape `EU-ESS` plays for statistics | eurogeographics.org; gim-international.com | Spain follow-up / 2026-08-16 | Candidate |
| **ITU standards** — no ID proposed | standard | UN (ITU), `level: international` | [[UN-ITU]] exists and **no ITU standard is modelled**, already noted in `research-queue.md`. Listed here because ITU is one of the three bodies behind the ISO/IEC/ITU standards world the Atlas already models through [[INTL-ISO]] and [[INTL-IEC]] | `discovery/research-queue.md`, Batch 13 | Batch 13; carried | Carried lead |
| **UNCTAD data governance work** — no ID proposed | initiative | UN, `level: international` | [[UN-UNCTAD]] exists with no instrument beneath it; its CSTD working group on data governance is already queued | `discovery/research-queue.md`, Batch 13 | Batch 13; carried | Carried lead |

---

## Suggested order of work

Ranked by *edges closed per page read*, not by importance:

1. **The Eurostat "Statistical cooperation" page.** One page. If it says
   what the search summary says, it yields [[EU-EUROSTAT]] → UN Statistical
   Commission, → CES, **and** → OECD CSSP. Three vertical edges, two layers
   connected, from a single read.
2. **The two Aarhus pages** (`environment.ec.europa.eu/law-and-governance/aarhus_en`
   and the EUR-Lex text of 2003/4/EC). Two pages for a complete UN → EU →
   national chain, plus five national transpositions to queue.
3. **Create `EU-ESS`.** No reading required — it is a modelling decision
   already queued, and it makes the statistics edges structurally correct
   instead of merely present.
4. **`UN-UNECE` as an entity.** Also mostly a modelling decision. It is the
   parent of items 1, 2 and UN/CEFACT; without it those three sit in the
   Atlas as unrelated facts.
5. **UNESCO**, revisiting the Batch 13 refusal against the EU partnership
   material.
6. Everything else.

**Steps 1–4 are the whole of the vertical gap.** They are four reads and two
modelling decisions, and none of them requires a new relationship type: they
use `participates-in`, `part-of`, `implements-requirement-from` and
`applies-in`, all already in `metadata/relationship-types.md` §2.1.

## What this page deliberately does not do

- **Nothing here has been asserted anywhere else in the Atlas.** No entity
  file, no relationship and no `related_entities` entry was changed to
  anticipate any of it. The UN layer is still an island, and the graph still
  shows it as one.
- **No entity was created from a search summary.** Every row is a lead with
  a named place to look, which is the whole contract of this file.
- **The adjacencies noted above are reasons to research, not findings.**
  That Aarhus-style environmental information access sits near
  [[EU-OPEN-DATA-DIRECTIVE]] is an observation about subject matter, not a
  sourced relationship, and it must not become one without a source that
  states it.
