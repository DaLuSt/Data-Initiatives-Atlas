# Candidates

Entities that appear potentially relevant but have not yet been researched
and sourced enough to add to the graph. Move a row here to a real entity
file once it has a `type`, an ID, at least one authoritative source, and a
clear enough relationship to the rest of the graph — then delete the row.

Do not add anything here without noting where it was seen.

> **Nothing on this page has been read.** Rows were compiled from
> search-engine results; the pages cited in *Where seen* were returned by a
> search index and confirmed to exist, but page retrieval is blocked
> (`EGRESS_BLOCKED`, 403 at the proxy tunnel). **These are leads, not
> findings.**

> **Proposed IDs are written in `backticks`, not `[[wikilinks]]`.** A
> wikilink to an entity that does not exist fails Obsidian navigation, and
> `validate_links` does **not** scan `discovery/` — so wikilinks here are
> unchecked by tooling and must be verified by hand.

---

## Status: the European → UN leads have been worked

The 2026-08-16 UN-connection batch acted on this page. **The UN layer is no
longer an island.**

| Before | After |
|---|---|
| `UN → anything` = **0** | `UN → national` = **5**, `EU → UN` = **4** |
| 9 UN entities, unattached | 17 UN entities, attached in three clusters |

14 entities were created and 7 existing ones rewired. See
`progress/completed.md` for the full entry. **Rows that produced entities
have been removed from this page**; what remains below is what is still
open, plus what the batch newly opened.

The batch's own diagnosis was confirmed: in every closed cluster the refused
edge had been pointing at a node that did not exist. Creating [[EU-ESS]] and
[[UN-UNSC]] made five previously-refused statistics edges statable without
lowering the sourcing standard at all.

---

## 1. Still open — the geospatial cluster is structurally incomplete

[[UN-GGIM]] and [[UN-GGIM-EUROPE]] now exist and are connected to each
other and to [[UN]]. **The edge to the European layer does not exist**, and
was looked for.

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **EuroGeographics** — `EU-EUROGEOGRAPHICS` | organisation | EU, `level: regional` | Probably the missing European node, playing the role [[EU-ESS]] plays for statistics: the association of national mapping, cadastral and land registry authorities. It appears throughout the UN-GGIM: Europe material and authored the INSPIRE-facing presentation cited on [[UN-GGIM-EUROPE]]. **Not created in the UN batch** — every source found is its own site or trade press, and creating it on that basis would repeat the error the batch existed to correct | eurogeographics.org; gim-international.com; the EuroGeographics INSPIRE KEN deck cited on [[UN-GGIM-EUROPE]] | Spain follow-up 2026-08-16; carried through UN batch | **Candidate — the cluster's missing middle** |
| **[[EU-INSPIRE]] → the UN-GGIM structure** | relationship | — | The one edge that would finish the geospatial vertical. What exists is a 2016 EuroGeographics presentation *about* UN-GGIM delivered to an INSPIRE audience, and general discussion of INSPIRE harmonisation in UN-GGIM: Europe working groups. **That is evidence the communities talk, not that the instruments relate**, and no edge was asserted | un-ggim-europe.org working groups; eurogeographics.org INSPIRE KEN deck | UN batch / 2026-08-16 | **Open — needs a real source** |

## 2. Still open — UN/CEFACT connects to nothing European

[[UN-CEFACT]] was created and attached to [[UN-UNECE]]. Searching for EU
adoption of its standards returned material about the body and its outputs
and **nothing establishing that any EU instrument or member state adopts
them**.

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **UN/EDIFACT, UN/LOCODE, Core Component Library** | standard | UN (UNECE), `level: international` | The actual UN/CEFACT outputs, and exactly the kind of artefact this Atlas models. None is an entity; none was researched | unece.org/trade/uncefact | UN batch / 2026-08-16 | Candidate |
| **Any EU or national reference to a UN/CEFACT standard** | relationship | — | The narrow question that would connect the trade/e-business cluster: *does any instrument already in this Atlas reference one?* Quick to answer with page access | — | UN batch / 2026-08-16 | **Open — narrow, answerable** |

## 3. Newly opened — two real EU↔UN interactions the vocabulary cannot express

Both were found by the UN batch, both are genuine European↔UN connections,
and **neither could be recorded as a relationship**.

| Interaction | Why it was not modelled | Where seen | Noted by / date | Status |
|---|---|---|---|---|
| **UNESCO–European Commission agreement** on accelerating implementation of the AI ethics Recommendation | It is a funding-and-cooperation agreement to help *other* countries implement the Recommendation (€4 m for least developed countries). The Commission is not adopting, implementing or governed by it. No relationship type says "has an agreement with" | unesco.org partnership article; dig.watch | UN batch / 2026-08-16 | Open (vocabulary) |
| **The 2023 EU voluntary review** submitted to UN global SDG monitoring | A one-off report submitted to a UN process. `references` would be the closest type and would misstate it | ec.europa.eu/eurostat SDG pages | UN batch / 2026-08-16 | Open (vocabulary) |

**Two examples is the threshold `metadata/relationship-types.md` §2.3 sets
for proposing a new type.** It was deliberately not proposed by a batch that
could not read the sources. This is the clearest live candidate for the next
vocabulary change.

## 4. Carried leads, unchanged

| Name | Suspected type | Suspected scope | Why it might matter | Where seen | Noted by / date | Status |
|---|---|---|---|---|---|---|
| **The 2030 Agenda itself** — `UN-2030-AGENDA` | policy | UN, `level: international` | [[UN-SDG-INDICATORS]] models the indicator framework and has **no link to the policy instrument it serves**. Nothing was found for the Agenda beyond passing references; a node built from those would be the thin encyclopedic entity the taxonomy threshold prevents | ec.europa.eu/eurostat SDG pages | UN batch / 2026-08-16 | Candidate |
| **UN Global Platform / Committee of Experts on Big Data** — `UN-GLOBAL-PLATFORM` | platform | UN, `level: international` | A second, independent attachment point for national statistical offices, alongside [[EU-ESS]] | ggim.un.org; unstats.un.org (not opened) | Spain follow-up / 2026-08-16 | Weak lead |
| **ITU standards** — no ID proposed | standard | UN (ITU), `level: international` | [[UN-ITU]] exists and **no ITU standard is modelled** | `discovery/research-queue.md`, Batch 13 | Batch 13; carried | Carried lead |
| **UNCTAD data governance work** — no ID proposed | initiative | UN, `level: international` | [[UN-UNCTAD]] exists with no instrument beneath it; its CSTD working group on data governance is queued | `discovery/research-queue.md`, Batch 13 | Batch 13; carried | Carried lead |
| **UN DESA, UNDP, WHO** | organisation | UN, `level: international` | Named in Batch 13's scope and refused for want of sources. The UN batch reversed that refusal for **UNESCO and UNECE** but did not go looking for these three | Batch 13 scope | Batch 13; carried | Carried lead |
| **Regulation (EC) No 223/2009** | law | EU, `level: regional` | [[EU-ESS]]'s legal basis, cited as a source and **not modelled**. Deliberately left with Regulation (EU) 1025/2012 (the ESO legal base) so the Atlas stays consistent about statutory bases rather than creating one of the pair | EUR-Lex CELEX 32009R0223 | Batch 9; re-raised UN batch | Candidate |

---

## What the UN batch closed, for the record

Removed from this page because the entities now exist:

| Was queued as | Became |
|---|---|
| `UN-UNECE` — "the missing joint" | [[UN-UNECE]], parent of three clusters |
| `UN-CES` | [[UN-CES]], with [[EU-EUROSTAT]] `participates-in` |
| `UN-UNSC` | [[UN-UNSC]], splitting the intergovernmental body from [[UN-UNSD]] |
| `EU-ESS` | [[EU-ESS]], with Eurostat and four national offices `part-of` |
| `INTL-OECD-CSSP` | [[INTL-OECD-CSSP]] — the OECD gap closed by the same page, as predicted |
| `UN-AARHUS` + `EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE` | both created; the Atlas's **first complete UN → EU → national chain** |
| `UN-UNESCO` + the AI ethics Recommendation | both created; the Batch 13 refusal reversed |
| `UN-CEFACT`, `UN-GGIM`, `UN-GGIM-EUROPE` | created, attached to their UN parents, European edges still open |
| `UN-SDG-INDICATORS` / `EU-SDG-INDICATORS` | both created, avoiding the [[EU-SDG]] collision |
