# Unresolved

Open questions the Atlas cannot currently answer with confidence: a fact
that couldn't be verified, a relationship that seems plausible but isn't
directly sourced, a status that couldn't be confirmed. Never guess to close
one of these — resolve it with a real source, or leave it open.

## Cross-cutting

| Entity / topic | Question | Why it's unresolved | Noted by / date | Status |
|---|---|---|---|---|
| All search-only Batch 1–10 entities (101 of 110) | Every factual claim | The environment's network egress policy blocks all direct page retrieval (`EGRESS_BLOCKED` for forumstandaardisatie.nl, digitaleoverheid.nl, noraonline.nl, vng.nl, logius.nl, eur-lex.europa.eu, wikipedia.org and every other host tested). Batch 1 was completed from search-engine results on explicit instruction, with the trade-off accepted knowingly. Every entity carries `verification: search-only`. | Batch 1 / 2026-08-14 | **Open — needs full re-verification pass** |

To find every affected entity: `grep -rl "verification: search-only" .`

## Status and temporal questions

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-FDS]] | Did the OBDO formally establish the *Afsprakenstelsel Federatief Datastelsel* in February 2026? | A search result asserted this. If true, `status` should move from `planned` to `active`/`implemented`. Recent, specific, high-consequence governance claim — must be read from a primary source. | Batch 1 / 2026-08-14 | Open |
| [[NL-IBDS]] | Exact date presented to the Tweede Kamer (reported as November 2021), and current status | A *Beleidsevaluatie Interbestuurlijke Datastrategie* exists on open.overheid.nl, indicating formal evaluation. Its findings may determine whether `status: active` is still correct. | Batch 1 / 2026-08-14 | Open |
| [[NL-DIGIBETER]] | Has NL DIGIbeter been superseded? By what, and when? | Latest actualisation found is 2020. **Batch 2 update:** [[NL-NDS]] (published 4 July 2025) is the leading candidate successor — it explicitly "connects existing digitalisation plans". But "a later strategy exists" is not "this strategy formally replaced that one", so no `supersedes` link is asserted. Needs a source that states the transition. | Batch 1 / 2026-08-14; updated Batch 2 | Open (narrowed) |
| [[NL-NDS]] | Is the NDS still the operative national digitalisation strategy? | Search results state the NDS was an initiative of the previous cabinet and that a subsequent cabinet was developing its own plans, with continuation and the ministerial division of responsibility unsettled. `status: active` is recorded at `confidence: low` on the basis that it was formally published and not withdrawn. | Batch 2 / 2026-08-14 | Open |
| [[NL-BASISREGISTRATIES]] | Who owns/governs the stelsel, and how does it relate to [[NL-FDS]]? | Both address reuse and sharing of authoritative public-sector data. Whether FDS extends, replaces or sits beside the basisregistraties stelsel is unestablished, and matters for the coherence of the Dutch data-governance model. | Batch 2 / 2026-08-14 | Open |
| [[NL-CBS]] | Which ministry holds responsibility for the CBS? | Research named Economic Affairs, but Dutch ministry names and portfolio boundaries have changed repeatedly and no ministry entity exists for it. No relationship asserted. | Batch 2 / 2026-08-14 | Open |
| [[NL-NATIONAAL-ARCHIEF]] | Does a revised Archiefwet take effect on 1 January 2027? | **Batch 3 update:** corroborated by further sources (Eerste Kamer dossier 35.968; rijksoverheid document; Nationaal Archief kennisbank) and modelled as [[NL-ARCHIEFWET-2026]]. Still unread, so still unverified. | Batch 2; updated Batch 3 | Open (corroborated) |
| [[NL-ARCHIEFWET-2026]] | What is this act's correct name — Archiefwet 2021, 2026, or something else? | Sources disagree: the Eerste Kamer dossier says "Archiefwet 2026", rijksoverheid and the Raad van State say "Archiefwet 2021", the Nationaal Archief hedges with "Nieuwe Archiefwet 20xx". Bill number 35968 is stable across all. The Atlas name is provisional; the **ID must not change** even if the name does. | Batch 3 / 2026-08-14 | Open |
| [[NL-ARCHIEFWET-2026]] | On what date did the Eerste Kamer approve the bill? | A search result said "12 May" without a year. Not recorded rather than guessed. | Batch 3 / 2026-08-14 | Open |
| [[NL-WHO]] | When did the Wet implementatie Open data richtlijn enter into force? | Two conflicting dates in search results: 19 June 2024 in one, while the rijksoverheid entry-into-force announcement is dated 2 August 2024. `start_date` left null rather than guessed. | Batch 3 / 2026-08-14 | Open |
| [[NL-WHO]] | Should the Wet implementatie Open data richtlijn be a separate entity? | Currently modelled as an amending act folded into the Who. If it has independent significance, split it out. | Batch 3 / 2026-08-14 | Open (modelling) |
| [[NL-CBW]] | Did the Cyberbeveiligingswet enter into force on 15 August 2026 as reported? | Recorded `status: planned` with `start_date: 2026-08-15` — one day after this entry was written. If confirmed, move to `active` and set [[NL-WBNI]] to `superseded`. | Batch 3 / 2026-08-14 | **Open — time-critical** |
| [[NL-WDO]] | Does the Wdo transpose obligations from eIDAS or another EU instrument? | `region` is currently `null` (treated as purely national), but its subject matter overlaps EU digital identity law. Re-examine when eIDAS is added in Batch 8. | Batch 3 / 2026-08-14 | Open |
| [[NL-UAVG]] | Should the Aanpassingswet AVG (dossier 34.939) be a separate entity? | It adjusted other Dutch legislation to the GDPR. Not modelled. | Batch 3 / 2026-08-14 | Open (modelling) |
| [[NL-TNO-WET]] | What is the current consolidated text and amendment history? | The act dates from 1930 and has certainly been amended. Only a Wikipedia secondary source and an Eerste Kamer keyword page were located. Needs wetten.overheid.nl. | Batch 3 / 2026-08-14 | Open |
| [[NL-DATA-AGENDA-OVERHEID]] | Publication date, validity period, and relationship to [[NL-IBDS]] | The two cover overlapping ground. No relationship is asserted between them because none has been sourced; guessing would violate the provenance rules. | Batch 1 / 2026-08-14 | Open |
| [[NL-MIDO]] | Which bewindspersoon is currently responsible for MIDO and the GDI? | A search result named a specific serving State Secretary. Office-holder facts go stale silently. The Atlas currently records only the institution, deliberately. Decide whether office-holders should be modelled at all. | Batch 1 / 2026-08-14 | Open (design question) |

## Batch 4 — standards and architecture

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-PETRA]] | Almost everything: maintainer, relationship to NORA, even the acronym's expansion | **Weakest entity in the Atlas.** Rests on a single sentence in one Wikipedia article. Included because Batch 4's scope names PETRA explicitly. The `organisations: [NL-IPO]` association is an Atlas assumption, not sourced. | Batch 4 / 2026-08-14 | Open |
| [[NL-RORA]] | When exactly in 2024 did RORA succeed EAR, and what is RORA's scope and maintainer? | `start_date: 2024-01-01` is a **placeholder for "during 2024"**, not a sourced date. Correct or null it on re-verification. | Batch 4 / 2026-08-14 | Open |
| [[NL-EAR]] / [[NL-RORA]] | Why does roraonline.nl describe itself as "the knowledge base of the Enterprise Architectuur Rijksdienst" if RORA succeeded EAR? | The site naming sits oddly with the succession claim. Both earonline.nl and roraonline.nl appear live. | Batch 4 / 2026-08-14 | Open |
| [[NL-BOMOS]] | Who currently maintains BOMOS? | Genuinely unclear: originates from a Forum Standaardisatie report, built by the NOiV programme bureau, hosted by ECP, current version published under Logius standards. No `maintained-by` asserted. | Batch 4 / 2026-08-14 | Open |
| [[NL-NEN-3610]] | Is Geonovum the maintainer, or only the point of contact for application? | The sourced statement says *aanspreekpunt*, which is weaker than `maintained-by`. As a NEN-numbered standard it is published by NEN. Custody appears split. | Batch 4 / 2026-08-14 | Open |
| [[NL-BIO]] | On what date did BIO2 replace BIO1? | A BIO2 document dated 9 Jan 2026 was located, but no formal transition date. | Batch 4 / 2026-08-14 | Open |
| [[NL-DCAT-AP-NL]] | Adoption date of v3.0 | Adoption is announced but undated in the search result. | Batch 4 / 2026-08-14 | Open |
| College Standaardisatie | Was the College the predecessor decision body to the [[NL-OBDO]]? | **Batch 4 corroboration:** a Digikoppeling source describes the comply-or-explain list as "of the College Standaardisatie", while Batch 1 sources name the OBDO. Consistent with a historical succession, but not confirmed. | Batch 1; corroborated Batch 4 | Open (corroborated) |

## Batch 5 — domains and data ecosystems

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-ISHARE]] | Is iSHARE still a Dutch entity, or now European? | Recorded `country: NL` on its Topsector Logistiek origin, but it presents at **ishare.eu** and operates in a European data-space context. An initiative that began national and became cross-border is the case the `country` field handles worst. May warrant `country: null` + `region: EU`. Settle in Batch 10. | Batch 5 / 2026-08-14 | Open (ontology-relevant) |
| [[NL-NTM]] | Which EU instrument imposes the national access point obligation? | Sources state every European country must have one, but none named the instrument. `region: EU` is set and the obligation described, but **no `implements-requirement-from` is asserted**. Completing this is a clean EU→national chain. | Batch 5 / 2026-08-14 | Open |
| [[NL-HEALTH-RI]] | Should Health-RI be split into an organisation and an infrastructure? | The name denotes both, and sources use it for both. Modelled as one `data-space` because the infrastructure has no proper name of its own. | Batch 5 / 2026-08-14 | Open (modelling) |
| [[NL-NDW]] | Is NDW a platform or an organisation? | Typed `platform` for its primary function, but it is a partnership of 19 governments with its own entry in the government organisation register. | Batch 5 / 2026-08-14 | Open (modelling) |
| [[NL-DSGO]] | Was DSGO v1.0 launched on 18 June **2024**? | Sources give "launched on 18 June" and separately "programme ran 2021–June 2024". `start_date: 2024-06-18` assumes these are the same moment — **an Atlas inference, not a sourced date**. | Batch 5 / 2026-08-14 | Open |
| [[NL-PDOK]] | Precise establishment date in 2013 | `start_date: 2013-01-01` is a placeholder for "in 2013". Same pattern as [[NL-RORA]] and [[NL-ISHARE]]. | Batch 5 / 2026-08-14 | Open |
| [[NL-DATA-OVERHEID]] | Who operates the portal? | `organisations: [NL-BZK]` reflects BZK's general open-data policy remit and is an **Atlas association, not a sourced operator claim**. | Batch 5 / 2026-08-14 | Open |
| Placeholder `start_date` convention | Should "year known, date unknown" be recorded as `YYYY-01-01` or left null? | Now used on four entities ([[NL-RORA]], [[NL-PDOK]], [[NL-ISHARE]], and partially [[NL-DSGO]]). A January-1st placeholder is indistinguishable from a real 1 January date, which is a genuine data-quality problem. Consider a convention or a `date_precision` field. | Batch 5 / 2026-08-14 | **Open (schema question)** |

## Batch 7 — EU core initiatives

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| ~~[[EU-EIDAS2]] / [[EU-EUDI-WALLET]]~~ | No official EU source | **Resolved in Batch 8** — both rebuilt on the EUR-Lex Official Journal text of Reg. (EU) 2024/1183 and the Commission's Digital Building Blocks pages. Confidence raised from low to medium. | Batch 7; resolved Batch 8 | Closed |
| [[EU-EIF]] → [[NL-NORA]] | Is NORA formally the Netherlands' National Interoperability Framework under the EIF? | NORA is described as "the interoperability framework for the Dutch government", but that is a description, not a designation. Confirming it would connect the EU and Dutch framework layers directly — one of the highest-value open items. Only `related_entities` recorded; no relationship asserted. | Batch 7 / 2026-08-14 | **Open — high value** |
| [[EU-EIF]] | Has the new EIF version been adopted? | The Commission aimed to submit a new version to the Interoperable Europe Board at end-2025/early-2026. Relative to this entry (Aug 2026) the "revised in 2017" description may be stale. | Batch 7 / 2026-08-14 | Open |
| [[EU-EUDI-WALLET]] | Have member states actually deployed wallets? | `status: planned` is deliberately conservative — the reported "late 2026" deadline had not passed at the time of writing and no deployment was evidenced. Check whether the Netherlands has issued one. | Batch 7 / 2026-08-14 | Open |
| [[NL-WDO]] | *(updated)* Does the Wdo transpose eIDAS? | **Batch 7 update:** [[EU-EIDAS2]] is probably a red herring — the Wdo came into force July 2023, before eIDAS 2.0 entered into force in May 2024. If the Wdo transposes anything it is more likely the original eIDAS Regulation (910/2014), which is not yet an entity. | Batch 3; updated Batch 7 | Open (narrowed) |
| [[EU-DIGITAL-DECADE]] | Should Decision (EU) 2022/2481 be a separate `legislation/` entity? | The Atlas models the programme, not the establishing Decision. | Batch 7 / 2026-08-14 | Open (modelling) |
| "Digital sovereignty" | Is there a distinct EU digital-sovereignty initiative warranting an entity? | Named in Batch 7's scope, but sources treat it as a framing within [[EU-DIGITAL-DECADE]] rather than a named initiative with its own governance. **No entity created.** | Batch 7 / 2026-08-14 | Open (scope) |
| EU AI strategy | Is there a distinct EU AI *strategy* entity, separate from the AI Act? | Named in Batch 7's scope. Searches returned mostly AI-and-cybersecurity material, not a clearly identifiable standalone strategy document. **No entity created** rather than inventing one. | Batch 7 / 2026-08-14 | Open (scope) |

## Batch 8 — EU legislation

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-DIGITAL-OMNIBUS]] | What is the proposal's **current** legislative status? | Recorded as at its 19 Nov 2025 introduction, with adoption reported as expected around end-2026. This entry is written Aug 2026, so the proposal may have advanced, been amended, or stalled. Everything downstream — three proposed repeals — depends on it. | Batch 8 / 2026-08-14 | **Open — time-sensitive** |
| [[EU-DIGITAL-OMNIBUS]] | Exact scope of the proposed amendments | All substantive detail comes from law-firm and academic commentary; only the CELEX reference is official. Read the proposal text. | Batch 8 / 2026-08-14 | Open |
| [[EU-AI-ACT]] | Which obligations were postponed by the AI-related omnibus amendment? | The phased timetable is recorded as originally reported; postponements are acknowledged but undetailed. The 2 Aug 2026 transparency phase landed 12 days before this entry. | Batch 8 / 2026-08-14 | Open |
| [[EU-AI-ACT]] | No EUR-Lex citation located | Sourced to artificialintelligenceact.eu and Wikipedia, unlike DGA/Data Act/NIS2/eIDAS2 which have Official Journal links. | Batch 8 / 2026-08-14 | Open |
| [[EU-EIF]] / [[EU-INTEROPERABLE-EUROPE-ACT]] | How do the Act and the Framework relate? | Does the Act give the EIF legal standing, supersede it, or govern it? Determines whether the EU interoperability layer has one root or two. **No relationship asserted.** | Batch 8 / 2026-08-14 | **Open — structural** |
| [[EU-EIDAS]] | The regulation's own content and dates | Created in Batch 8 purely so the [[NL-WDO]] question is expressible. Its only source is the amending regulation. | Batch 8 / 2026-08-14 | Open |
| [[NL-WDO]] | *(updated)* Does the Wdo transpose eIDAS 910/2014? | **Batch 8 update:** eIDAS 2.0 ruled out on dates (Wdo July 2023 precedes it). Original eIDAS is the plausible candidate but nothing sources the transposition. `region` stays `null`. | Batch 3; updated Batch 7, 8 | Open (narrowed) |
| [[EU-SDG]] | The once-only principle mechanism, and the Dutch implementation | Relevance was assessed on the once-only principle, but that mechanism was not researched, and no Dutch counterpart is modelled. | Batch 8 / 2026-08-14 | Open |
| Free Flow of Non-Personal Data Regulation | Not modelled | Named as a third repeal target of the Omnibus. Should exist for the repeal picture to be complete. | Batch 8 / 2026-08-14 | Open |

## Batches 9–10 — EU organisations, standards and data spaces

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-EHDS]] → [[NL-HEALTH-RI]] | Will Health-RI be the Dutch health data access body? | The EHDS requires member states to designate HDABs during 2027–2029. Health-RI is the obvious candidate but nothing sources it, and the designation phase had not begun. Confirming it completes an EU-regulation → national-infrastructure chain. | Batch 10 / 2026-08-14 | **Open — high value** |
| [[EU-EMDS]] → [[NL-NTM]] | Does the mobility data space build on the national access point network? | Close to self-evident, and therefore exactly the kind of link this project has repeatedly been wrong to assume. Association only. | Batch 10 / 2026-08-14 | Open |
| [[EU-DSSC-BLUEPRINT]] ↔ Dutch afsprakenstelsels | Do [[NL-FDS]], [[NL-DSGO]], [[NL-ISHARE]] and [[NL-HEALTH-RI]] map onto the Blueprint's rulebook model? | The resemblance is striking and entirely unsourced. Confirming it would connect the Dutch and EU data-space layers structurally rather than thematically. | Batch 10 / 2026-08-14 | **Open — structural** |
| [[INTL-DCAT]] | No W3C source located | Both citations are second-hand descriptions of DCAT. The top of the Atlas's flagship standards chain is its weakest link. **Rebuild in Batch 14**, as Batch 8 rebuilt [[EU-EIDAS2]]. | Batch 9 / 2026-08-14 | **Open — priority** |
| [[EU-PUBLICATIONS-OFFICE]] | No source describing the organisation | Its EUR-Lex publisher role — relied on by the whole `legislation/` folder — is asserted from the Atlas's own citation practice, which is circular. | Batch 9 / 2026-08-14 | Open |
| [[EU-EDPB]], [[EU-CEN]], [[EU-EUROSTAT]] membership links | Are [[NL-AP]], [[NL-NEN]] and [[NL-CBS]] confirmed members? | All three rest on **composition rules** ("comprises representatives from each national supervisory authority") rather than sources naming the Dutch body. Inference from a sourced rule, marked as such at `confidence: medium`. | Batch 9 / 2026-08-14 | Open |
| [[EU-EHDS]] | Should the regulation be split from the data space? | Modelled as one entity, matching [[NL-BIO]] and [[NL-HEALTH-RI]]. Reg. (EU) 2025/327 is substantial legislation and may warrant its own entity. No EUR-Lex citation was located either. | Batch 10 / 2026-08-14 | Open (modelling) |
| [[EU-SEMIC]], [[EU-DSSC]] | Are these organisations, programmes, or something else? | SEMIC is described as an "action"; DSSC's legal form is unclear. `organisation` is the best available fit for both, with reservations. | Batches 9–10 | Open (modelling) |
| [[EU-PARLIAMENT]] / [[EU-COUNCIL]] | Should legislative adoption be modelled? | Currently **not** — it would add 32 edges conveying one fact already implied by entity type. If wanted, do it systematically with a dedicated relationship type. | Batch 9 / 2026-08-14 | Open (modelling) |
| Directorates-General | Which DGs are relevant, and should they be entities? | DG CONNECT is named once as a DCAT-AP co-initiator. No DG research was done; none created. | Batch 9 / 2026-08-14 | Open |

## Factual details flagged in entity bodies

| Entity | Question | Noted by / date | Status |
|---|---|---|---|
| [[NL-PAS-TOE-OF-LEG-UIT]] | Is the procurement threshold €50,000, and is that figure current? | Batch 1 / 2026-08-14 | Open |
| [[NL-FORUM-STANDAARDISATIE]] | Exact 2006 establishment date and instrument reference; current status of the College Standaardisatie (established alongside the Forum) | Batch 1 / 2026-08-14 | Open |
| [[NL-OBDO]] | Precise boundary between the OBDO's advisory role and its decision-making role. Two Staatscourant items (stcrt-2018-9728, stcrt-2022-18861) are likely instellingsbesluiten. | Batch 1 / 2026-08-14 | Open |
| [[NL-GDI]] | Does "GDI" expand to *Generieke* or *Gezamenlijke* Digitale Infrastructuur? Search results used both. May be a real terminology change or inconsistent secondary sources. | Batch 1 / 2026-08-14 | Open |

## Entity typing questions

| Entity | Question | Noted by / date | Status |
|---|---|---|---|
| [[NL-FDS]] | Typed `framework` on the basis of its self-description as an *afsprakenstelsel*. `initiative` or `programme` are defensible alternatives. | Batch 1 / 2026-08-14 | Open |
| [[NL-COMMON-GROUND]] | Typed `initiative`; described in sources as both a vision and a programme, so `framework`/`programme` are defensible. | Batch 1 / 2026-08-14 | Open |
| [[NL-GDI]] | Typed `platform`; it is a collection of systems and agreements rather than one system, so `framework` is partly apt too. | Batch 1 / 2026-08-14 | Open |
| [[NL-BASISREGISTRATIES]] | Typed `framework`; it is a system of registrations plus supporting services, so `platform` is arguable. | Batch 2 / 2026-08-14 | Open |
| [[NL-NEN]] | NEN has been the name of a cooperation between the NNI foundation and the NEC foundation since 2000. The Atlas models only the foundation named in `name`. Whether the cooperation or the NEC warrant separate entities is unresolved. | Batch 2 / 2026-08-14 | Open |
| [[NL-NICTIZ]] | Recorded at `level: sectoral` rather than `national` — a national organisation whose authority is bounded to healthcare. Confirm this reading of `level` is the intended one across the Atlas. **Batch 4 applied the same reading to [[NL-ROSA]]**, so the convention is now used twice and should be settled. | Batch 2; reinforced Batch 4 | Open (ontology question) |
| [[NL-BIO]] | Should BIO and BIO2 be one entity or two? | Modelled as one entity with versions, unlike Wob/Woo and Archiefwet 1995/2026 which are separate. Reasoning: BIO2 is a new version of a continuously named baseline, not a distinct instrument. Split if re-verification contradicts this. | Batch 4 / 2026-08-14 | Open (modelling) |
| [[NL-ADR]] | Should the Nederlandse API Strategie be a separate entity, with the ADR `part-of` it? | The ADR is part IIa of a strategy that was split into sub-documents, several of which are on the comply-or-explain list. Only the ADR is modelled. | Batch 4 / 2026-08-14 | Open (modelling) |
