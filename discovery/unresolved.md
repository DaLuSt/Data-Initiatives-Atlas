# Unresolved

Open questions the Atlas cannot currently answer with confidence: a fact
that couldn't be verified, a relationship that seems plausible but isn't
directly sourced, a status that couldn't be confirmed. Never guess to close
one of these — resolve it with a real source, or leave it open.

## Cross-cutting

| Entity / topic | Question | Why it's unresolved | Noted by / date | Status |
|---|---|---|---|---|
| All unread-source entities (**389 of 396**: 386 `search-only` + 3 `unverified` ([[NL]], [[EU]], [[UN]]); regenerate the count with `python tools/source_hosts.py`) | Every factual claim | The environment's network egress policy blocks all direct page retrieval (`EGRESS_BLOCKED` for forumstandaardisatie.nl, digitaleoverheid.nl, noraonline.nl, vng.nl, logius.nl, eur-lex.europa.eu, wikipedia.org and every other host tested). Batch 1 was completed from search-engine results on explicit instruction, with the trade-off accepted knowingly. Every entity carries `verification: search-only`. | Batch 1 / 2026-08-14 | **Open — needs full re-verification pass** |

To find every affected entity: `grep -rl "verification: search-only" .`

**The worklist for closing this is generated:**
| [[ES-LO-2-2002]] | Is `catedrapsyd.unizar.es` still a live host? | The first full sweep with `tools/reverify.py` found this cited source **did not resolve at all**, while every other host tested resolved. In this environment all known hosts resolve to the proxy's interceptor, so a non-resolving host points at a genuinely dead one rather than a blocked one. | Full sweep / 2026-08-19 | ✅ **Confirmed dead on re-verification 2026-08-26** — genuinely DNS-dead. BOE's own text of the act was read directly instead and now carries the entity's `primary-source` promotion. |

| [[BE]], [[DE]], [[FR]], [[IT]], [[LU]], [[NL]] | Should the founding six be keyed on 25 March 1957 or 1 January 1958? | A verification pass on 2026-08-20 supplied **25 March 1957** — the day the Treaty of Rome was *signed*. The Atlas uses **1 January 1958**, the day it *entered into force*, because that is what the Union's own list of EU countries says and that page is the cited source on every one of these entities. Strictly neither is an accession: the six founded the Communities rather than joining them. Both dates are now recorded on each entity. **Deciding for 1957 means changing the evidence strings and the cited source together** | Verification pass / 2026-08-20 | Open (modelling) |

**Link-checked so far (2026-08-20):** the 22 candidate sources for Forum
Standaardisatie, the IBDS/FDS, NORA, Common Ground and MIDO, plus 22 of the
highest-value domains and a machine reachability sweep over all 52
institutional domains. All confirmed except `gob.es`, which has no apex site.
**None of this changed any entity's `verification`** — it establishes that
the citations are right, not that the entities' claims are supported. See
`docs/re-verification.md` on the three tiers.

**The pass now has a runner:** `tools/reverify.py`, documented in
`docs/re-verification.md`. It fetches an entity's sources, checks the
legal identifiers the entity claims against the retrieved page text, and
stamps `accessed:`/`last_verified:`/`verification:` on approval. Under
the current egress policy every source returns `BLOCKED` and nothing is
written — which is the tool reporting the environment honestly, not
failing.

`discovery/reverification-allowlist.md` lists every host the Atlas cites,
derived from the entity files by `tools/source_hosts.py`. Page retrieval is
blocked by an **environment-level egress policy** — the proxy answers
`403 to CONNECT` — which no change inside a session can lift. The allowlist
is what to request.

## Status and temporal questions

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-FDS]] | Did the OBDO formally establish the *Afsprakenstelsel Federatief Datastelsel* in February 2026? | A search result asserted this; recent, specific, high-consequence governance claim — needed reading from a primary source. | Batch 1 / 2026-08-14 | ✅ **Resolved — Batch 1 re-verification, 2026-08-21.** Confirmed on digitaleoverheid.nl: "In februari 2026 heeft het OBDO het Afsprakenstelsel Federatief Datastelsel vastgesteld." `status` moved `planned` → `active`. Data-provider rules are adopted; data-consumer rules are still to follow, per the same source. |
| [[NL-IBDS]] | Exact date presented to the Tweede Kamer (reported as November 2021), and current status | A *Beleidsevaluatie Interbestuurlijke Datastrategie* exists on open.overheid.nl, indicating formal evaluation. | Batch 1 / 2026-08-14 | ✅ **Resolved — Batch 1 re-verification, 2026-08-21.** 18 November 2021, confirmed independently on digitaleoverheid.nl and noraonline.nl's page metadata; `start_date` set. The evaluation report (Panteia, 7 January 2026, "Definitief") describes 2025 as an ongoing "opschaling en borging" phase with recommendations for continuation — `status: active` confirmed correct, `confidence` raised to `medium`. |
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
| [[NL-MIDO]] | Which bewindspersoon is currently responsible for MIDO and the GDI? | A search result named a specific serving State Secretary. Office-holder facts go stale silently. | Batch 1 / 2026-08-14 | **Closed — by decision, reaffirmed Batch 1 re-verification 2026-08-21.** The Atlas records only the institution ([[NL-BZK]]'s Directorate Digital Government, advised by [[NL-OBDO]]), not the office-holder. [[NL-MIDO]]'s body states this explicitly as a deliberate choice. |

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
| [[EU-EIF]] → [[NL-NORA]] | Is NORA formally the Netherlands' National Interoperability Framework under the EIF? | NORA is described as "the interoperability framework for the Dutch government", but that is a description, not a designation. | Batch 7 / 2026-08-14 | ✅ **Resolved — Batch 1 re-verification, 2026-08-21.** Kamerstuk 26643-128 (2008 Kabinetsbesluit inzake ICT) confirms EIF developments are anchored in NORA, but narrowly — for public services with cross-border data exchange, not as a blanket NIF designation. [[NL-NORA]] now carries `based-on` → [[EU-EIF]] on that sourced, narrower basis. |
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
| [[INTL-DCAT]] | No W3C source located | Both citations are second-hand descriptions of DCAT. The top of the Atlas's flagship standards chain is its weakest link. **Rebuild in Batch 14**, as Batch 8 rebuilt [[EU-EIDAS2]]. | Batch 9 / 2026-08-14 | ✅ **Resolved 2026-08-27.** Batch 14 had already rebuilt the entity on w3.org citations, but a frontmatter/body drift left `verification: search-only` and every evidence string reading "NOT READ" — neither page had actually been fetched. Both now read directly, confirming the Recommendation date and backward-compatibility claim in the specification's own words. `verification: primary-source`, `confidence: high`. |
| [[EU-PUBLICATIONS-OFFICE]] | No source describing the organisation | Its EUR-Lex publisher role — relied on by the whole `legislation/` folder — is asserted from the Atlas's own citation practice, which is circular. | Batch 9 / 2026-08-14 | Open |
| [[EU-EDPB]], [[EU-CEN]], [[EU-EUROSTAT]] membership links | Are [[NL-AP]], [[NL-NEN]] and [[NL-CBS]] confirmed members? | All three rest on **composition rules** ("comprises representatives from each national supervisory authority") rather than sources naming the Dutch body. Inference from a sourced rule, marked as such at `confidence: medium`. | Batch 9 / 2026-08-14 | Open |
| [[EU-EHDS]] | Should the regulation be split from the data space? | Modelled as one entity, matching [[NL-BIO]] and [[NL-HEALTH-RI]]. Reg. (EU) 2025/327 is substantial legislation and may warrant its own entity. No EUR-Lex citation was located either. | Batch 10 / 2026-08-14 | Open (modelling) |
| [[EU-SEMIC]], [[EU-DSSC]] | Are these organisations, programmes, or something else? | SEMIC is described as an "action"; DSSC's legal form is unclear. `organisation` is the best available fit for both, with reservations. | Batches 9–10 | Open (modelling) |
| [[EU-PARLIAMENT]] / [[EU-COUNCIL]] | Should legislative adoption be modelled? | Currently **not** — it would add 32 edges conveying one fact already implied by entity type. If wanted, do it systematically with a dedicated relationship type. | Batch 9 / 2026-08-14 | Open (modelling) |
| Directorates-General | Which DGs are relevant, and should they be entities? | DG CONNECT is named once as a DCAT-AP co-initiator. No DG research was done; none created. | Batch 9 / 2026-08-14 | Open |

## Batches 6, 11, 15 — validation findings

| Entity / topic | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| **The UN layer is unconnected** | Nothing links the 9 UN entities to any EU or NL entity | The brief's target architecture is UN → EU → National → Sector. What exists is a connected EU↔NL graph plus a **separate, unattached UN component**. The single most significant structural gap in the Atlas. | Batch 15 / 2026-08-14 | ✅ **Resolved — UN-connection batch, 2026-08-16.** `EU → UN` is now 4 and `UN → national` is 5. The diagnosis in `discovery/candidates.md` held: in every cluster the refused edge pointed at a node that did not exist. Creating [[EU-ESS]], [[UN-UNSC]], [[UN-UNECE]] and [[UN-CES]] made the statistics edges statable, and [[UN-AARHUS]] → [[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]] gave the first complete UN → EU → national chain. **No sourcing standard was lowered and no relationship type was added.** |
| [[UN-UNSD]] → [[EU-EUROSTAT]] | Is the European Statistical System part of the global statistical system? | Would close most of the UN-layer gap on its own. Plainly true in substance; **no source read says it**. | Batch 13; confirmed Batch 15 | ✅ **Resolved differently — UN batch, 2026-08-16.** The edge as posed was never correct: UNSD is a secretariat and Eurostat does not relate to it directly. Eurostat `participates-in` [[UN-UNSC]] and [[UN-CES]] — forums, sourced to Eurostat's own cooperation page — and [[UN-UNSD]] is `governed-by` the Commission. **Three refusals of this row were right.** |
| [[UN-FPOS]] → [[NL-WET-CBS]] | Does Dutch statistical legislation align with the Fundamental Principles? | Countries are tracked on exactly this. Would give a UN → national chain. | Batch 12; confirmed Batch 15 | Open |
| [[NL]], [[EU]], [[UN]] anchors | Do their cited URLs exist? | **Written in Batch 0 from background knowledge, never confirmed by search or fetch** — the brief says never invent URLs. Now marked `verification: unverified`, worse than the `search-only` majority. Self-inflicted, caught by the Batch 6 audit. | Batch 6 / 2026-08-14 | ✅ **Resolved 2026-08-27.** [[EU]] had already been re-verified to `primary-source` in an earlier pass. [[NL]] and [[UN]] are now closed too: european-union.europa.eu and government.nl were read directly for NL (ISO's OBP confirmed genuinely bot-walled); un.org's homepage and "About Us" page were read directly for UN. All three URLs turned out correct — background knowledge was right, but "very likely correct" was never the bar. |
| `applies-in` with one country | Is the country-neutral model actually reusable? | All 17 `applies-in` relationships target `NL`. The mechanism is exercised but **untested with a second country**, which is the only real proof. | Batch 15 / 2026-08-14 | ✅ **Resolved — Germany batch, 2026-08-15.** 33 `applies-in` relationships now target `['DE', 'NL']`. Adding a second country required no ontology, schema, folder or validation change, and produced no `DE-EU-*` entity. See `countries/README.md`. |
| 40 entities with no provenanced relationship | Are these legitimately terminal or under-linked? | Many are terminal by nature (legislation nothing implements). Worth reviewing when sources are available. Was 35 before the Germany batch; 10 of the 37 German entities are in this category. | Batch 15; recounted 2026-08-15 | Open |

## Batches 12–14 — UN and international

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[UN-DATA-STRATEGY]] | Everything — publication date, structure, objectives, status | The only sourced statement is that it "reaffirms the need for data analysis as a core skill". **No source dedicated to the strategy was located.** Weakest entity in Batch 12. | Batch 12 / 2026-08-14 | **Open — priority** |
| [[UN-DATA-COMMONS]] | Every specific claim | **The only source is a Grokipedia page** — an AI-generated encyclopedia, the weakest citation anywhere in this Atlas. The Google partnership and Sept 2024 expansion are unverified. | Batch 12 / 2026-08-14 | **Open — priority** |
| [[INTL-IETF]] | Everything beyond its category | Single indirect source (an academic toolkit listing eight SDOs); no ietf.org citation, no IETF standard modelled. Yet IETF RFCs underpin the HTTPS/DNSSEC/mail standards on [[NL-PAS-TOE-OF-LEG-UIT]]. | Batch 13 / 2026-08-14 | Open |
| [[UN-GDC]] | Adoption date, and a un.org source | The only source is a **European Commission news page** — odd and weak for a UN compact. The Summit of the Future is named but not dated. | Batch 12 / 2026-08-14 | Open |
| [[INTL-ISO-IEC-27002]] | Cited URL points at **edition 2 (2013)**, a superseded edition | The current edition is 27002:2022, which is what BIO2 references. The ISO OBP link located resolves to the older edition and older title. | Batch 14 / 2026-08-14 | Open |
| [[NL-BIO]] → ISO editions | Is NEN-EN-ISO/IEC 27001:**2023** the same standard as ISO/IEC 27001:**2022**? | BIO2 cites the NEN-EN adoption years; the ISO editions differ by one year. Almost certainly the Dutch/European adoption of the same standard, but the equivalence is **inferred, not sourced**. | Batch 14 / 2026-08-14 | Open |
| [[INTL-ISO]] → [[NL-NEN]] | Is NEN a member of ISO? | Batch 2 recorded NEN as a 1947 ISO co-founder, but no composition rule was sourced (unlike CEN's "33 national bodies"), so **no relationship is asserted** — unlike the CEN, EDPB and Eurostat membership links. Should be easy to close. | Batch 13 / 2026-08-14 | Open |
| [[UN-UNSD]] → [[EU-EUROSTAT]] | Does the European Statistical System connect to the UN statistical system? | **No source read connects the levels.** One of the clearest remaining gaps in the Atlas's vertical structure — the statistics chain stops at the EU. | Batch 13 / 2026-08-14 | ✅ **Resolved — UN batch, 2026-08-16.** See the Batch 15 row above; the connection runs through forums, not between the two organisations. |
| [[UN-FPOS]] → [[NL-WET-CBS]] | Does Dutch statistical legislation align with the FPOS? | Countries are tracked on exactly this. Establishing it would give an international → national chain in statistics, parallel to DCAT in metadata. | Batch 12 / 2026-08-14 | Open |
| [[UN-UNSD]] | Should UNSD and the UN Statistical Commission be separate entities? | UNSD is the secretariat; the Commission is the intergovernmental body. Folded into one on a single sourced sentence. | Batch 13 / 2026-08-14 | ✅ **Resolved — UN batch, 2026-08-16.** Split. A source distinguishes them: the Commission **oversees the work of** UNSD, and UNSD **acts as the Commission's secretariat**. The split is what made [[EU-EUROSTAT]]'s edge statable — it sits in the Commission, not in the Division. |
| ISO/IEC JTC 1 | Should the joint technical committee be an entity? | It is arguably what actually produces the 27000-family standards, sitting between the two organisations and the standards. Not modelled. | Batch 14 / 2026-08-14 | Open (modelling) |
| [[UN-2-0]] | The quintet PDF sits under a `2021/09` path while the policy brief is dated Sept 2023 | Suggests the quintet framing predates the brief, or the file was re-filed. `start_date: 2023-09-01` is a placeholder. | Batch 12 / 2026-08-14 | Open |
| World Bank | Not modelled | Named in Batch 13's scope. Its institutions are technically UN specialised agencies, making the UN/non-UN call genuinely tricky — **omitted rather than risk misclassifying it**, which is the specific error the brief warns about. | Batch 13 / 2026-08-14 | Open (deliberate) |

## Germany batch — second country (2026-08-15)

### The federal modelling gap — the batch's principal finding

| Topic | Question | Why it matters | Status |
|---|---|---|---|
| **No sub-national level** | The `level` vocabulary runs `international / regional / national / sectoral / local` with nothing for a German Land | Germany's sixteen Länder are **not representable**. Concretely lost: the sixteen Land acts that, with [[DE-GEOZG]], jointly transpose [[EU-INSPIRE]]; the sixteen Land data protection authorities alongside [[DE-BFDI]]; [[DE-KOSIT]]'s hosting in the Bremen administration. The Atlas **cites Land governments as sources** while unable to model them. Matters for any federal state added later — Austria, Belgium, Spain, Switzerland. | **Open — ontology, highest value from this batch** |
| Verwaltungsvereinbarungen | Should Bund-Länder administrative agreements be entities? | Both [[DE-GOVDATA]] and [[DE-GDI-DE]] rest on one. Neither legislation nor policy in the Atlas's sense; no entity type fits. A recurring German constitutional device, twice in one batch. | Open (ontology) |

### Relationship-type questions

| Entity | Question | Why it matters | Status |
|---|---|---|---|
| [[DE-NIS2UMSUCG]] → [[DE-BSIG]] | Is there a relationship type for an **amending act**? | The NIS2UmsuCG comprehensively revised the BSIG; it did not repeal it. `supersedes` overstates, `influences` understates. Recorded as `supersedes` at `confidence: low`, with [[DE-BSIG]] deliberately left `status: active` — the two sides **do not agree**, and are meant not to. `relationship-types.md` §2.3 permits adding a type; not done here on unread sources. | **Open — the batch's principal modelling question** |
| [[DE-BUNDID]] → [[EU-EIDAS]] | `implements-requirement-from` or `aligned-with`? | Sources say BundID "follows the provisions of" eIDAS and accepts other member states' eIDs. A portal conforms; legislation transposes. Marginal call, recorded at low confidence. | Open (modelling) |
| [[DE-KOSIT]] → [[DE-FITKO]] | Is `part-of` right for an office hosted by a Land but operating under a federal cooperation? | Both statements are sourced and the model cannot hold them together. Recorded `part-of` at `confidence: low`. A direct consequence of the federal gap above. | Open (modelling) |
| [[DE-CATENA-X]], [[NL-ISHARE]] | What does `country` mean for a data space? | **Two independent instances of the same problem.** The field conflates origin, governance and operation; both entities originate nationally and operate transnationally (Catena-X has a Shanghai hub and a CAAM agreement). Two cases make it a property of the model, not of either entity. | **Open — ontology** |
| [[DE-BUNDID]] → DeutschlandID | Rename or succession? | Modelled as a rename (`alternative_names`), **no successor entity created**, because sources describe a continuing service. Revisit if the transition proves to be a distinct service. | Open (modelling) |

### Refused links — sourced-looking but unsourced

| Link | Why refused | Value if closed | Status |
|---|---|---|---|
| [[DE-DESTATIS]] → [[EU-EUROSTAT]] | Destatis's sourced remit includes "harmonisation of statistics for the purposes of the European Union" but **does not name Eurostat** | Third member of the statistics cluster below | ✅ **Resolved — UN batch, 2026-08-16.** Destatis is now `part-of` [[EU-ESS]], sourced to the ESS composition rule. The edge to Eurostat itself is still not asserted and does not need to be. |
| [[DE-BSTATG]] → [[UN-FPOS]] | The act's principles read as a restatement of the Fundamental Principles; no source says so | Fourth member of the cluster | **Open — structural** |
| [[DE-XRECHNUNG]] → [[EU-CEN]] / EN 16931 | XRechnung is in all likelihood the German CIUS of the European e-invoicing norm under Directive 2014/55/EU. **No source read states it**; neither the directive nor EN 16931 is an Atlas entity | A fifth EU→DE chain, and one running through a **standards body** rather than a legislature — the DCAT shape Batch 15 asked for more of | **Open — high value, low effort** |
| [[EU-INSPIRE]] → [[NL]] | INSPIRE certainly applies in the Netherlands, but the Dutch geospatial batch predates this entity and none of its sources named the directive | Removes the false impression that INSPIRE is German-specific | **Open — first priority, near-certainly one page read** |
| [[DE-BFDI]] → [[EU-EDPB]] | [[NL-AP]] carries exactly this link. German representation on the EDPB (federal vs Land authorities) is precisely the detail that must not be guessed | A free DE→EU edge | ✅ **Resolved.** [[EU-GDPR]] Article 68(3) itself answers the multi-authority question: where more than one supervisory authority exists, "a joint representative shall be appointed in accordance with that Member State's law." `participates-in` asserted; which authority currently holds the joint-representative role is still not established and is not claimed. |
| [[DE-BUNDID]] → [[EU-EIDAS2]] / [[EU-EUDI-WALLET]] | eIDAS2 requires wallets by end-2026 and BundID is the obvious German starting point; no source connects them | Will matter within months | ✅ **Resolved — verification-gap push, 2026-08-22.** bmds.bund.de now states the connection directly ("Im Kontext der novellierten eIDAS-Verordnung wird die Anbindung der BundID an die EU Digital Identity Wallet ... vorbereitet"). `implements-requirement-from` → [[EU-EUDI-WALLET]] asserted at low confidence, since the connection is described as being prepared, not live. |
| [[DE-MDS]] → [[EU-EMDS]] | Same refusal Batch 10 made for [[EU-EMDS]] → [[NL-NTM]]. **Two national mobility data spaces now sit unconnected to their apparent European parent** | Closes both at once | Open |
| [[DE-REGMOG]] → [[EU-SDG]] | Once-only is the SDG Regulation's organising idea and RegMoG is Germany's once-only vehicle, but RegMoG is domestic register law and no source connects them | — | Open |
| [[EU-GAIA-X]] → [[EU-COMMON-DATA-SPACES]] / [[EU-DSSC-BLUEPRINT]] | Plainly part of the same European effort; the Commission source cited is *about* Gaia-X, not a statement of relationship | — | Open |
| [[DE-BFDI]] → [[DE-BDSG]] | The BfDI is the authority the BDSG constitutes, but no source read states it in citable terms | — | Open |

### Factual gaps

| Entity | Question | Status |
|---|---|---|
| [[DE-DATENSTRATEGIE]] | **Adoption date contested across sources** — BMI URL path says August 2023, two other sources say 12 and 14 September 2023. `start_date` left null rather than guessed. Also: is it still in force after the creation of [[DE-BMDS]] and the [[DE-MODERNISIERUNGSAGENDA-BUND]]? | Open |
| [[DE-DIGITALSTRATEGIE]] | `status: unknown`. Its 2025 horizon has passed; sources suggest targets were missed; **no source states it was completed, superseded or extended** | Open |
| [[DE-OZG]] | The act's **own enactment date was never established** — every source concerns the 2024 amendment or the programme. Widely known to be 2017, which is exactly why it is not recorded | Open |
| [[DE-BDSG]] | **All four sources are commercial legal publishers.** No Gesetze-im-Internet or BGBl citation, for the entity carrying the most structural weight in the batch | ✅ **Resolved 2026-08-27.** gesetze-im-internet.de's own official text, found via search and read directly, confirms enactment (30 June 2017), entry into force (25 May 2018), and the GDPR-precedence mechanism in the law's own Section 1(5). Three of five sources now read directly; the "~70 opening clauses" count remains unconfirmed by any page actually read. |
| [[DE-IWG]] | Nothing established beyond its replacement by [[DE-DNG]]. All three sources are about the DNG. Which PSI directive it transposed is unknown | Open |
| [[DE-BMI]] | Current formal name unclear (*des Innern* vs *des Innern und für Heimat*), and its `produces` relationships are historical: [[DE-BMDS]] took digital competences from six departments in May 2025 | Open |
| [[DE-IT-GRUNDSCHUTZ]] | **No bsi.bund.de IT-Grundschutz page cited** — searches returned Wikipedia and consultancy explainers for a framework published by a federal authority | Open |
| [[DE-MODERNISIERUNGSAGENDA-FOEDERAL]] | The **five fields of action are not recorded** — no source read names them | Open |
| [[DE-IT-ARCHITEKTURRICHTLINIEN]] | The **content** of the guidelines is unknown; only existence, custody, governance and version 1.9.0 are recorded | Open |
| [[DE-DCAT-AP-DE]] | The 28 June 2018 IT-Planungsrat resolution rests on a single secondary statement; no decision document cited | Open |
| [[DE-CATENA-X]] | No catena-x.net source; described entirely through Fraunhofer institutes and trade press | Open |
| [[NL-CBW]] | `start_date: 2026-08-15` — **today**. The entity's own body asks a reader after that date to verify and, if confirmed, move it to `active` and [[NL-WBNI]] to `superseded`. Not done: it cannot be verified without page retrieval | **Open — actionable the moment egress is available** |

## Belgium batch — third country (2026-08-15)

### The federal modelling gap is general, and Belgium sharpens it

| Topic | Question | Why it matters | Status |
|---|---|---|---|
| **No sub-national level — confirmed general** | Germany found no term fits a Land. Belgium finds the term that *would* fit is **already taken**: `level: regional` means supra-national in this Atlas ([[EU]] carries it). | The cost is now concrete and large: **OSLO** — a Flemish semantic-interoperability and linked-data standards programme squarely in this Atlas's subject matter — is not modelled at all, nor are Digitaal Vlaanderen, the Agence du Numérique, Paradigm, or any Region or Community. Belgium's coverage **understates** its reality more than any other country's. Two federal states, two different failure modes, same root cause. | **Open — ontology, the Atlas's best-evidenced defect** |
| Multilingual names | Belgium has three official languages; `name` uses the Dutch form where the sources found were Dutch, French in `alternative_names`. | A sourcing artefact presented as a naming decision. `FOD BOSA`/`SPF BOSA` and `KSZ`/`BCSS` are equally official. The Atlas has no multilingual name field and did not gain one. | Open (ontology) |
| `level: sectoral` for nationally-constituted bodies | [[BE-KSZ]] joins [[NL-NICTIZ]] and [[NL-ROSA]] in being recorded `sectoral` — a national body whose authority is bounded to one sector. | The convention is now used four times across three countries on precedent alone. It should be written into `metadata/taxonomy.md` or abandoned. | Open (ontology) |

### Refused links — Belgium

| Link | Why refused | Status |
|---|---|---|
| [[BE-HERGEBRUIK-WET]] → [[EU-OPEN-DATA-DIRECTIVE]] | **Chronologically impossible**: the act is 2016, the directive 2019/1024. Sources say it aligns with the earlier PSI Directive, which is not an Atlas entity. **Belgium's actual Open Data Directive transposition was not identified.** The sharpest pattern-matching trap in the batch — the shape of the Atlas made a wrong answer attractive. | ✅ **Resolved between batches, closed by re-verification pass 2026-08-26.** [[BE-HERGEBRUIK-WET-2023]] (created after this batch ran) is Belgium's transposition, amending this act. Reading the 2016 act's own consolidated (Justel) text this pass confirms the 2023 amendment inserted a direct citation to Directive (EU) 2019/1024 into its Article 1 — but per the Atlas's amends/amending convention, the `implements-requirement-from` edge stays on [[BE-HERGEBRUIK-WET-2023]], not here. |
| [[BE-NIS1-WET]] → [[EU-NIS]] | Near-certain, and [[EU-NIS]] *is* an Atlas entity so the link has somewhere to point — but every source cited is about the successor act and none states what the 2019 act transposed. Would give a second `EU-NIS` → national descent. | ✅ **Resolved — re-verification pass, 2026-08-26.** The one page read closed it: the act's own Article 2 at etaamb.openjustice.be states "Deze wet voorziet met name in de omzetting van de Europese Richtlijn (EU) 2016/1148." `implements-requirement-from` → [[EU-NIS]] now asserted. |
| [[BE-APD]] → [[EU-EDPB]] | No source read mentions the EDPB. Three national DPAs now sit in the Atlas and **only [[NL-AP]] connects to the Board** — a sourcing artefact, not a fact about European data protection governance. | ✅ **Resolved — re-verification pass, 2026-08-26.** Reading gdpr-info.eu directly confirms Article 68(3) GDPR requires the Board to include one supervisory authority per Member State; the GBA/APD is Belgium's. Also found: the `participates-in` [[EU-EDPB]] edge was **already present in this entity's own frontmatter** (added at some point after this table entry was written) while its body text still said the link was "refused for want of a source" — a frontmatter/body drift bug, now corrected on [[BE-APD]] itself. |
| [[BE-STATBEL]] → [[EU-EUROSTAT]] / [[UN-FPOS]] | Nothing found. ⚠ **The claim that "none connects upward" was wrong when written and was repeated for three batches** — [[NL-CBS]] already carried a `participates-in` edge to Eurostat, with ESS-membership reasoning in its evidence. Corrected in the UN batch. | ✅ **Partly resolved — UN batch, 2026-08-16.** Statbel is now `part-of` [[EU-ESS]]. ⚠ **The re-verification pass of 2026-08-26 found the same wrong claim still standing in [[BE-STATBEL]]'s own body prose**, ten days after the frontmatter was corrected — a second instance of the frontmatter/body drift bug also found on [[BE-APD]]. Corrected this pass; Wikipedia additionally corroborates with "Statbel serves as Belgium's official representative to Eurostat." The [[UN-FPOS]] half is still open. |
| [[BE-KSZ]] → [[EU-SDG]] | The KSZ predates the regulation by 28 years and no source connects them — the same refusal made for [[DE-REGMOG]]. | Open |
| [[BE-DATA-GOV-BE]] → [[BE-HERGEBRUIK-WET]] | Portal and open-data act, obviously related, no source states it. Same call as [[DE-GOVDATA]] / [[DE-DNG]]. | Open |
| [[BE-BOSA]] → [[BE-BELGIF]] | BELGIF is sourced as co-owned by the federal state, Regions and Communities — precisely not something BOSA owns. | Open (deliberate) |

### Closed by Belgium

| Link | Result |
|---|---|
| [[EU-EIF]] → a national interoperability framework | ✅ **Closed.** [[BE-BELGIF]] is sourced as Belgium's NIF and as taking the EIF's 12 principles as its basis. The Atlas's **first EIF → national-framework descent**. The equivalent German question ([[DE-IT-ARCHITEKTURRICHTLINIEN]]) and Dutch question ([[NL-NORA]]) stay open, and are now sharper for having a worked example. |

### Factual gaps — Belgium

| Entity | Question | Status |
|---|---|---|
| [[BE-NIS2-WET]] | No Belgisch Staatsblad ELI URI cited; publication and entry-into-force dates rest on CCB reporting. | Partly resolved — re-verification pass, 2026-08-26. Two more independent external sources (kpmglaw.be, prebes.be) now corroborate the 17 May 2024 publication date and the replacement of [[BE-NIS1-WET]]; CCB's own three pages remain bot-walled and no ELI URI has yet been found. |
| [[BE-KSZ-WET]] | Only two sources, one of them the KSZ's page about its own founding act. Act content unknown. | Partly resolved — re-verification pass, 2026-08-26. The KSZ's own page, read directly, quotes Article 1 verbatim. Remaining act content (governance, funding) still unknown; still only two sources. |
| [[BE-STATBEL]] | **No statutory basis found** — no Belgian equivalent of [[DE-BSTATG]] or [[NL-WET-CBS]], so no `governed-by` is recorded. | **Found 2026-08-27** — the Wet van 4 juli 1962 betreffende de openbare statistiek, read directly at etaamb.openjustice.be. Still no `governed-by` edge: the 1962 act is not yet its own Atlas entity. **Open — create the entity, then add the edge.** |
| [[BE-HERGEBRUIK-WET]] | Scope, obligations and relationship to the current EU regime all unknown. | Partly resolved — re-verification pass, 2026-08-26. The act's own text (both original and current consolidated versions) was read directly, confirming its 2016 PSI Directive transposition and the 2023 amendment's insertion of a Directive (EU) 2019/1024 reference. Full substantive obligations (licensing, pricing, appeals commission) remain sourced only from BIPT's secondary account. |

### Belgium re-verification pass (2026-08-26)

All 24 `country: BE` entities carrying `verification: search-only` were
checked against primary sources, as the fifteenth entry in the
verification-gap series (following the France, Austria, Finland, Estonia
and Czechia tails). **18 of 24 promoted to `primary-source`**; 6 stayed
`search-only` for want of a majority of readable sources. See
`countries/be/index.md` for the full list and each entity's own `Sources`
section for its read/unread breakdown.

Two frontmatter/body drift bugs were found and fixed, both predating this
pass — see the [[BE-APD]] and [[BE-STATBEL]] rows above. Two stale-index
bugs were also found and fixed in `countries/be/index.md`, independent of
the 24-entity list: its EU-instrument comparison table still showed
[[EU-OPEN-DATA-DIRECTIVE]] as "not established" for Belgium although
[[BE-HERGEBRUIK-WET-2023]] had already closed that gap before this pass
began, and NBN was called "not modelled" in the index's own "Not modelled"
section while [[BE-NBN]] already existed as an entity and was simply
missing from the "Organisations" list above it.

A genuine dating error was also caught and corrected on
[[BE-HERGEBRUIK-WET-2023]]: it was published in the Belgisch Staatsblad on
**23 January 2024**, not 25 December 2023 as previously recorded — 25
December 2023 is the act's own date (promulgation). The EUR-Lex national
implementing measures register independently corroborates 23 January 2024.

A genuine host-block pattern emerged, the Belgian counterpart to the
`.gouv.fr` block found in the France batch: `bosa.belgium.be`,
`ccb.belgium.be`, `news.belgium.be`, `data.gov.be`, `financien.belgium.be`,
`statbel.fgov.be` and `atwork.safeonweb.be` all returned CAPTCHA
verification pages or plain 403s to every attempt, even with an honest
User-Agent, while `vsse.be`, `sgrs.be`, `comiteri.be`,
`gegevensbeschermingsautoriteit.be`, `ksz-bcss.fgov.be`,
`ejustice.just.fgov.be`, `etaamb.openjustice.be`, `wallex.wallonie.be` and
`codex.vlaanderen.be` were all reachable. This explains most of why
[[BE-BOSA]], [[BE-CCB]], [[BE-STATBEL]] and [[BE-DATA-GOV-BE]] stayed
`search-only` despite genuine effort to reach a majority via alternate
external sources (law firms, employers' federations, Wikipedia, GitHub).

### Second Belgium pass — the six leftover tails (2026-08-27)

The six entities left `search-only` above were re-attempted individually,
using `WebSearch` to find previously-uncited alternate pages rather than
re-fetching the same blocked URLs. **Four closed:** [[BE-TOEZICHTSWET-1991]]
and [[BE-COMITE-I]] both promoted once `ejustice.just.fgov.be`'s Justel
page — which had timed out three times in the first pass — succeeded on a
fourth attempt; [[BE-CCB]] promoted on five independent law-firm analyses
of the NIS2 royal decree (Eubelius, nis-2-directive.com, Simont Braun,
Lydian, Eversheds Sutherland); [[BE-STATBEL]] promoted once
etaamb.openjustice.be surfaced the 1962 public statistics act, closing a
gap open since the first pass. **Two did not close:** [[BE-BOSA]] and
[[BE-DATA-GOV-BE]] remain `search-only` — every new route tried
(`dtservices.bosa.be`, `fedweb.belgium.be`, `digitall.be`, `selor.be`,
`werkenvoor.be`) redirects or 403s back into the same blocked domains,
confirming the block is comprehensive rather than page-specific. GitHub
(`Fedict/dcattools`) and a third-party API directory did yield genuine new
technical detail for [[BE-DATA-GOV-BE]] without reaching a majority of its
sources.

## France batch — fourth country (2026-08-16)

### The result is a negative, and that is the point

France is unitary, and was added specifically to test whether anything in
the model besides the federal `level` gap was Netherlands-shaped
(`progress/backlog.md`). **It raised no new ontology question at all** —
every entity fitted an existing type, level, status and relationship type.

Combined with Germany and Belgium this isolates the defect: **the ontology
is sound for unitary states and lossy for federal ones**, and the loss is
confined to the `level` vocabulary rather than being a general
country-shape problem. Nothing new is opened here; the federal row above
stands unchanged.

### Refused links — France

| Link | Why refused | Status |
|---|---|---|
| [[FR-RGI]] → [[EU-EIF]] | The RGI is very probably France's NIF, which is exactly why it is refused: nothing read mentions the EIF, the NIF concept or European interoperability. [[BE-BELGIF]] is sourced on both counts; the RGI is sourced on neither. **[[EU-EIF]] now has four countries and one national-framework link.** | Open |
| [[FR-LRN]] → [[EU-OPEN-DATA-DIRECTIVE]] | **Chronologically impossible** — the act is 2016, the directive 2019/1024. The same trap Belgium sprang. France's actual transposition (understood to be a 2021 ordinance) was not identified. **Two of four countries now have this gap.** | **Open — priority** |
| [[FR-CNIL]] → [[EU-EDPB]] | No source read mentions the EDPB. **Four national DPAs now sit in the Atlas and only [[NL-AP]] connects to the Board** — the clearest single example in the Atlas of a sourcing artefact masquerading as structure. Four pages would close it. | ✅ **Resolved 2026-08-27.** gdpr-info.eu's own text of Article 68(3) GDPR, read directly, states the Board is composed of one supervisory authority per Member State — a general rule this Atlas had already accepted as `source: fact` confirmation for [[DE-BFDI]] (2026-08-22), [[BE-APD]] and [[ES-AEPD]] (2026-08-26), but had inconsistently still refused for CNIL. Corrected for consistency: all five national DPAs now modelled in the Atlas carry a sourced `participates-in` [[EU-EDPB]] edge. |
| [[FR-FRANCECONNECT]] → [[EU-EIDAS]] / [[EU-EIDAS2]] | Nothing read mentions eIDAS or cross-border recognition, even though a national identity federation is precisely what eIDAS governs. The eIDAS2 wallet deadline (end 2026) is now four months away and **no country in the Atlas is linked to it**. | **Open — becoming time-critical** |
| [[FR-NIS2-LOI]] → [[EU-CER]] | The vehicle is sourced as transposing REC, NIS2 and DORA together, but the instrument's own status is unresolved; the relationship would inherit that. | Open (deliberate) |
| [[FR-DATA-GOUV]] → [[FR-LRN]] | Portal and open-data act, obviously related, nowhere stated. Same call as the German and Belgian equivalents — now made four times. | Open |

### Factual gaps — France

| Entity | Question | Status |
|---|---|---|
| [[FR-NIS2-LOI]] | **Sources directly contradict each other**: one says transposition is by Law n° 2025-90 of 26 February 2025; another says the bill was adopted by the Senate on 12 March 2025 and awaits promulgation, expected mid-2026. Both cannot be true. `status: unknown`, `start_date: null`, no law number recorded. **The only entity in the Atlas whose sources conflict about whether the instrument is in force.** | **Open — priority** |
| [[FR-LIL]] | No Légifrance citation for loi 78-17 itself; the 1978 date rests on the CNIL and secondary commentary. Three of five sources are chamber-of-commerce or law-firm material. | Open |
| [[FR-RGI]] | The specification PDF is cited from **april.org**, an advocacy association hosting a copy, because no numerique.gouv.fr URL for it was returned. | Open |
| French DCAT profile | **Not established.** data.gouv.fr certainly exposes DCAT — the European portal harvests it — but no named French application profile was found, so the DCAT fork stops at three countries instead of four. | Open |
| INSEE | Not modelled — only a passing mention in an unrelated article. France is therefore the **only one of the five countries with no statistical office in [[EU-ESS]]**, which is now a visible hole in a modelled structure rather than a missing entity among unconnected ones. | **Open — more visible since the UN batch** |

## Spain batch — fifth country (2026-08-16)

### The model is not western-European-shaped

Spain is the first country outside the founding-six / Benelux-DACH group,
added specifically to test the objection that four neighbouring states with
similar administrative traditions cannot demonstrate country-neutrality. It
required **no ontology, schema, taxonomy, relationship-type, folder,
validation or generator change**, and produced no `ES-EU-*` entity. The
objection is answered.

### The federal gap has a third shape — and that localises it

| Country | Sub-national tier | What the Atlas can express |
|---|---|---|
| Germany | 16 Länder (federal) | nothing |
| Belgium | Regions and Communities (federal) | nothing — and `regional` is already taken by the supra-national meaning |
| **Spain** | **17 Comunidades Autónomas (State of Autonomies — neither federal nor unitary)** | **nothing** |

Three constitutionally distinct arrangements; **the Atlas fails on all three
identically**. That is the strongest evidence yet that the defect is in the
`level` vocabulary and not in any country's constitutional shape. Three of
five countries are now affected.

Spanish cost, specifically: **seventeen regional open data portals** (over
14,000 datasets by 2019), regional data protection authorities, autonomous
communities managing **over 35 % of consolidated public spending**, and
*cogobernanza del Estado y las Comunidades Autónomas* — **one of two
cross-cutting axes** of [[ES-ESPANA-DIGITAL-2026]], of which the Atlas can
model only the state half.

### Closed by Spain

| Item | How |
|---|---|
| **Open Data Directive transposition** | [[ES-LEY-37-2007]], as amended by Real Decreto-ley 24/2021. **Three of five countries now closed**; Belgium and France stay open. The "obvious earlier act" trap is confirmed as a research hazard in three of five countries — 2016 in Belgium and France, **2007** in Spain. |
| **First national link to [[EU-AI-ACT]]** | [[ES-AESIA]] `governed-by` the AI Act. Spain created the agency in 2023, before the Regulation applied — the first EU member state to have one. |
| **First edge in the statistics cluster** | [[ES-INE]] `related-to` [[EU-EUROSTAT]], `source: interpretation`, `confidence: low`. **Superseded by the UN batch:** replaced with `part-of` [[EU-ESS]] at `source: fact`, which is what the Spain batch itself said the correct fix would be. |
| **Fourth branch of the DCAT chain** | [[ES-NTI-RISP]] `based-on` [[EU-DCAT-AP]] — and the only branch that is a legally mandatory norm rather than a profile. |

### Refused links — Spain

| Link | Why refused | Status |
|---|---|---|
| [[ES-ENI]] → [[EU-EIF]] | Nothing read mentions the EIF or the NIF concept. **Refused for the third time** (Germany, France, now Spain), and for the same reason each time: the pattern makes it look expected, which is not evidence. [[EU-EIF]] now has five countries and one national-framework link. | Open |
| [[ES-CLAVE]] → [[EU-EIDAS]] / [[EU-EIDAS2]] | An `implements-requirement-from` edge exists at `confidence: low`, but its two now-read specific sources (eidas.redsara.es, viafirma.com) confirm the general Spanish eIDAS node and that DNIe (not Cl@ve) is the notified scheme — neither states that administrations integrate via Cl@ve. **The eIDAS2 wallet deadline is now roughly four months away and no country in the Atlas is linked to it.** [[FR-FRANCECONNECT]] predicted this would become a factual question; it now is one. | **Open — time-critical, re-checked 2026-08-27** |
| [[ES-AEPD]] → [[EU-EDPB]] | No source read mentions the Board. **Five national DPAs, one sourced link.** | ✅ **Resolved 2026-08-26** — gdpr-info.eu's own text of Article 68(3) GDPR, read directly, names one supervisory-authority seat per member state on the Board; AEPD now carries the edge at `confidence: medium`. [[DE-BFDI]], [[BE-APD]] and [[FR-CNIL]] remain unsourced — the same one-article read would close all three. |
| [[ES-ESPANA-DIGITAL-2026]] → [[EU-DIGITAL-DECADE]] | Nothing read connects them, though the strategy is aligned with the Recovery Plan. Same refusal as [[NL-DIGIBETER]] and [[DE-DIGITALSTRATEGIE]] — three national strategies, three refusals. | Open |
| [[ES-ESPANA-DIGITAL-2026]] — which two axes? | **Genuine source conflict, found 2026-08-27.** Widely-syndicated coverage (and this entity's own prior description) names the two new cross-cutting axes as public-private collaboration and co-governance with the Autonomous Communities. But the government's own current pages (espanadigital.gob.es, mineco.gob.es), read directly, instead name PERTE and Retech, with espanadigital.gob.es explicitly denying co-governance is one of the two. Both framings are recorded in the entity, unresolved. | **Open — needs the original July 2022 press materials to adjudicate** |
| [[ES-INCIBE]] / [[ES-CCN]] → [[ES-LCGC]] | Reporting describes an institutional dispute over a draft allocation of competences. **A dispute is not a relationship**, and the law is not in force. | Open (deliberate) |
| [[ES-ENI]] ↔ [[ES-ENS]] | Consistently presented together in Spanish practice; no source read establishes a relationship between the instruments. | Open |
| [[ES-DATOS-GOB-ES]] → Red.es | Red.es operates the portal but was not an entity — a single mention of its promoting role was too thin. | ✅ **Resolved 2026-08-26** — [[ES-RED-ES]] created as its own entity, sourced to both sides' own pages; datos.gob.es now carries the `maintained-by` edge. |

### The one asserted link that needs scrutiny

| Link | Concern | Status |
|---|---|---|
| [[ES-INE]] → [[EU-EUROSTAT]] | The sources describe a **three-party structure** — the European Statistical System comprises Eurostat *and* the member states' statistical offices — not a bilateral relationship. The Atlas records `related-to` at `source: interpretation`, `confidence: low`, and states the gap in the `evidence` string. **The correct fix is an `EU-ESS` entity** with `part-of` edges from Eurostat and from all national offices; it was deliberately not created inside a country batch. That single entity would connect four national statistical offices at once. | **Open — modelling, high value** |

### Factual gaps — Spain

| Entity | Question | Status |
|---|---|---|
| [[ES-AESIA]] | **No BOE citation for Real Decreto 729/2023**, the decree that creates it — no search result returned the BOE identifier. | ✅ **Resolved 2026-08-26** — BOE-A-2023-18911, found via protecciondata.es and confirmed by reading boe.es directly. |
| [[ES-NTI-RISP]] | The DCAT-AP-ES model is described as **in administrative processing**, so the `based-on` descent from [[EU-DCAT-AP]] may not yet be in force. Recorded at `confidence: low` with `valid_from: null`. | Open — confirmed still accurate on re-verification 2026-08-26. |
| [[ES-LCGC]] | No BOE citation exists to give — the instrument is a draft. Its passage would also make the Centro Nacional de Ciberseguridad modellable. | Open |
| [[ES-ENI]] | Legal base not modelled: sources say it was established by article 42 of Ley 11/2007, an act since replaced by the 2015 administrative-procedure legislation. The chain from the current base was not established, and the repealed act was not asserted as its parent. | **Partly resolved 2026-08-27** — anabad.org, read directly, gives the current statutory anchor: the ENI's existence is contemplated in Article 156 of Ley 40/2015 (the act that replaced the 2007 legislation). No typed edge added, since neither the ontology nor the source cleanly distinguishes "contemplated by" from "derived from" — recorded in prose on the entity instead. |
| [[ES-LOPDGDD]] | **The `Ley Orgánica` rank is not modelled.** Spain's constitutional hierarchy distinguishes organic from ordinary laws, and only the organic rank lets its Title X bind. `type: law` flattens it — as it already flattens *Gesetz*/*Verordnung*, *wet*/*koninklijk besluit* and *loi*/*ordonnance*. No field was added: five countries have been modelled without one, and adding it would require re-reading every instrument in the Atlas. | Open (ontology question) |
| [[ES-LOPDGDD]] | **Partial implementation is not expressible.** Title X on digital rights does not descend from any EU instrument; the single `implements-requirement-from` edge is whole-entity to whole-entity and silent about it. No partial-implementation type proposed on one example. | Open (modelling) |
| [[ES-AEAD]] | `supersedes` records the succession but cannot say it was a **transformation** — same functions and remit under a new legal form — rather than an abolition and replacement. Not worth a new relationship type on one example. | Open (modelling) |
| [[ES-CLAVE]] | Operator, legal basis, the relationship between Cl@ve PIN and Cl@ve Permanente, and the status of any Spanish digital identity wallet are all unrecorded. | Open — unchanged on re-verification 2026-08-27; that pass closed the eIDAS-citation gap (see refused-links table above) without touching this one. |
| Spanish organic law on AI | Sources refer to one landing the AI Act domestically with sanctions and sandboxes, at a stage they describe inconsistently. **Not created** — the Atlas already carries one instrument whose sources contradict each other and does not need a second on weaker evidence. | Open |
| Ley 39/2015 / Ley 40/2015 | Spain's electronic-administration acts. Well sourced but not modelled in this batch; they are the current legal base for much of what [[ES-AEAD]] does. | Open |

## UN-connection batch (2026-08-16)

### The island is connected

`UN → anything` was 0 through five country batches. It is now `EU → UN` = 4
and `UN → national` = 5, with 14 entities added and 7 rewired.

**Nothing about the sourcing standard changed.** Every previously-refused
edge was refused correctly; what was missing was the node it should have
pointed at. [[EU-ESS]] and [[UN-UNSC]] are those nodes, and creating them
made five statistics edges statable on evidence that was already available.

### A record that was wrong for three batches

| Claim | Reality |
|---|---|
| *"Three/four national statistical offices sit in the Atlas and none connects upward"* — repeated in this file, `candidates.md` and three batch entries | **[[NL-CBS]] already had `participates-in` → [[EU-EUROSTAT]]**, added in an early batch with ESS-membership reasoning in its evidence string |

The claim was never checked against the entity files; it was carried forward
from batch to batch. It is corrected here, and the NL-CBS edge has been
repointed to [[EU-ESS]] with the other four. **Worth a lesson: cluster
narratives in this file are prose, and prose does not get validated.**

### Newly opened — two EU↔UN interactions the vocabulary cannot express

| Interaction | Why it could not be modelled | Status |
|---|---|---|
| **UNESCO–European Commission agreement** on AI ethics implementation | A funding-and-cooperation agreement to help *other* countries implement the Recommendation. The Commission is not adopting or implementing it. No type says "has an agreement with" | Open (vocabulary) |
| **The 2023 EU voluntary review** submitted to UN SDG monitoring | A one-off report submitted to a UN process. `references` is the nearest type and would misstate it | Open (vocabulary) |

**Two examples is the threshold `metadata/relationship-types.md` §2.3 sets
for proposing a new type.** Deliberately not proposed by a batch that could
not read the sources.

### Newly opened — soft law is indistinguishable from binding law

[[UN-AARHUS]] is a convention that binds its Parties. The
[[UN-AI-ETHICS-RECOMMENDATION]] is a non-binding UNESCO recommendation.
Nothing in the Atlas's metadata distinguishes them.

This is **the same missing property** the Spain batch found from the other
direction, where `type: law` flattened Spain's constitutional `Ley Orgánica`
rank. Two independent batches have now hit it. No field was added: six
batches have run without one and populating it honestly would mean
re-reading every instrument.

### Still open after the batch

| Item | Why it stayed open |
|---|---|
| [[EU-INSPIRE]] → the UN-GGIM structure | A EuroGeographics presentation *about* UN-GGIM given to an INSPIRE audience is evidence the communities talk, not that the instruments relate. The geospatial cluster has its UN parent and no European edge |
| Any EU/national reference to a **UN/CEFACT** standard | Searched; nothing found. [[UN-CEFACT]] is attached to [[UN-UNECE]] and connects to the European layer not at all |
| **EuroGeographics** | Probably the missing European node, playing [[EU-ESS]]'s role for geospatial. Every source found is its own site or trade press — creating it on that basis would repeat the error this batch existed to correct |
| [[UN-FPOS]] → national statistical legislation | Untouched. The batch connected the *organisational* statistics layer; the **legislative** one ([[NL-WET-CBS]], [[DE-BSTATG]]) still has no UN link |
| [[EU-AI-ACT]] → [[UN-AI-ETHICS-RECOMMENDATION]] | The dates line up — UNESCO 2021, [[ES-AESIA]] 2023, AI Act 2024 — and **nothing read says they relate**. Chronology is not causation, and this was the batch's most attractive available error |
| [[EU-SDG-INDICATORS]] `applies-in` | Not asserted. An indicator set is not an instrument that applies in a member state, and no national SDG indicator set is modelled for any of the five countries |

### Typing questions opened

| Entity | Question |
|---|---|
| [[UN-CES]] | Typed `programme`. It is a standing intergovernmental conference with a Bureau, so `organisation` is arguable; typed `programme` because it is convened *by* [[UN-UNECE]] rather than existing beside it, the same reading applied to [[UN-GGIM]] |
| [[INTL-OECD-CSSP]] | The sources give **two names and two acronyms** — *committee on statistics and statistical policy* (CSSP) and *statistics committee* (CSTAT) — and differ on whether Eurostat represents "the EU" or "the European Commission". Recorded at `confidence: low` with both names. **No OECD source is cited at all**; the committee is described only by a participant |

## Basisregistraties batch (2026-08-16)

### The headline: the Atlas cannot express how data moves

Ten base registries, three organisations and a rewired stelsel entity were
added. The batch's finding is not about the Netherlands — it is about the
relationship vocabulary.

**Five sourced connections could not be recorded**, in three distinct
shapes:

| Shape | Examples | Why no edge |
|---|---|---|
| **Authorised use** ("afnemer") | [[NL-BELASTINGDIENST]] uses [[NL-WOZ]]; [[NL-RDW]] receives [[NL-BRP]] data | No type says "is an authorised user of". `applies-to` inverts it, `depends-on` overstates it |
| **Key-sharing coupling** | [[NL-BRK]] products carry the KvK number from [[NL-NHR]]; [[NL-BAG]] ↔ [[NL-BRP]] via documented RvIG guidance | No type for "carries the identifier of". `references` implies citation, `derived-from` is plainly wrong |
| **`Authentiek gegeven`** | the legal status that makes a base registry authoritative — data others must use and may not re-determine | No metadata field at all |

Taken together: **the Atlas models what entities *are* and what they
*descend from*, and has almost no vocabulary for how data actually moves
between them.** For a system whose whole purpose is data movement, that is
the honest result.

With the UN batch's two (the UNESCO–Commission agreement and the EU
voluntary review), **five sourced connections are now unmodelled for want of
a type** — well past the §2.3 threshold for proposing one.

### Dutch municipalities are unmodelled — and this one is not the `level` gap

| Register | Who actually holds the data | What the graph shows |
|---|---|---|
| [[NL-BAG]] | municipalities | [[NL-KADASTER]] (national facility) |
| [[NL-BGT]] | **seven** categories of bronhouder, organised in SVB-BGT | [[NL-KADASTER]] (national facility) |
| [[NL-WOZ]] | municipalities determine the values | [[NL-WAARDERINGSKAMER]] (functional manager) |

Unlike the German Länder, Belgian Regions and Spanish Comunidades
Autónomas, **the `level` vocabulary is not the obstacle** — `local` exists.
The obstacle is that there is no obvious entity to create: there are
hundreds of municipalities, and one node for "the municipalities" would be
an invention. [[NL-VNG]] is their association, which is a different thing.

Also unmodelled: **SVB-BGT** (the BGT bronhouders' cooperative, named in one
source), **Rijkswaterstaat, ProRail, Defence and RVO** as BGT bronhouders,
and **Digimelding**, the stelsel's error-reporting facility.

### Every register carries one `maintained-by`, and three of them shouldn't

The stelsel's own documentation describes **four roles** — initiator,
supervisor, provider, holder — and says one organisation can be several at
once. The Atlas has one type. Where the roles diverge, the caveat is written
into the relationship's **own `evidence` string**, so it is visible in the
graph data rather than only in prose. That is the mitigation, not a fix.

### Statutes named but not modelled

Nine registers have a statutory basis; only [[NL-BRP]] carries a
`governed-by` edge, to the pre-existing [[NL-WET-BRP]]. The Wet BAG, Wet
BGT, Wet BRO, Wet WOZ and AWR Chapter IVA are named in descriptions and
**have no entities**. Creating six Dutch statutes would be a legislation
batch; doing half would leave the layer inconsistent.

⚠ **[[NL-BRT]] has no sourced statute at all** — the only one of the ten.

### Typing question

| Entity | Question |
|---|---|
| The ten registers | Typed `platform` — *"a concrete technical platform or system"* (`metadata/ontology.md` §1). A basisregistratie is arguably a **dataset with a legal status** rather than a platform; the *landelijke voorziening* is the platform. `framework` fits the stelsel but not a single register, and there is no `register` or `dataset` type. Applied consistently to all ten so at least the set is coherent |

### Still open

- **[[NL-FDS]] ↔ the stelsel.** Whether the Federatief Datastelsel extends,
  replaces or sits beside it is unestablished, as it has been since Batch 2.
  Untouched by this batch.
- **[[NL-BRO]] is phased.** `status: active` is correct — the Act is in
  force — but sources say implementation is *in phases*. No status value
  covers "in force and partially implemented".
- **[[NL-BRO]]'s predecessors** DINO and BIS are described as things the
  register *builds on*, which is weaker than supersession. Neither is
  modelled and no `supersedes` was asserted.
- **[[NL-BRV]] holds personal data** and is therefore in scope for
  [[EU-GDPR]] and [[NL-UAVG]]. Nothing read says so, so nothing is asserted
  — an obviously-true statement kept out until a source states it.

## Poland batch — sixth country (2026-08-16)

### Both untested assumptions held

Poland acceded in **2004**, in a different enlargement from the five western
European states before it. `progress/backlog.md` asked whether the EU layer
is the right regional parent for such a state and whether `applies-in` is
the right attachment mechanism. **Both held**, with no ontology, schema,
folder, validation or generator change and no `PL-EU-*` entity.

### The new questions are about *time*, and neither is expressible

| Question | Case | Why it cannot be recorded |
|---|---|---|
| An instrument in force **after a Commission letter of formal notice** | [[PL-KSC]] — NIS2 amendment in force 3 Apr 2026. **Corrected 2026-08-26**: this row previously said Poland was "referred" to the CJEU; the Commission's own page instead shows a letter of formal notice, the *first* infringement stage — earlier than [[ES-LCGC]]'s reasoned opinion, not later as previously implied | `status: active` is correct and carries none of it. Neither the formal notice nor the reasoned-opinion stage is in the structured data |
| A national system **subject to a requirement it cannot meet** | [[PL-MOBYWATEL]] is reported architecturally incompatible with eIDAS 2.0 and unable to serve as an EUDI Wallet | No type expresses a failed obligation. `implements-requirement-from` asserts the opposite; `governed-by` implies it works. Recorded as `related-to` at `confidence: low` with the substance in the evidence string |

**The eIDAS2 edge is the sixth sourced connection the vocabulary cannot
express** — after the register batch's three (authorised use, key-sharing
couplings, `authentiek gegeven`) and the UN batch's two (cooperation acts).
It is also the first eIDAS2 link of any kind in the Atlas, after four
batches recorded that none existed.

### Closed by Poland

| Item | How |
|---|---|
| **The 2016-act trap has a documented answer** | Poland had the identical 2016 open data act that caught Belgium and France, and [[PL-OTWARTE-DANE]] **explicitly and fully repeals it**. Four of six countries closed; the two open gaps now have a known shape — repeal (Poland) or amendment in place (Spain) |
| **Best-sourced [[EU-ESS]] membership** | [[PL-GUS]] describes the ESS on its own pages and states its Eurostat obligation, where the other four attach on the composition rule. Five offices; **France is the only modelled country without one** |

### Refused / not modelled — Poland

| Item | Why |
|---|---|
| **CSIRT MON** | [[PL-ABW]] and [[PL-NASK]] cover CSIRT GOV and CSIRT NASK respectively (confirmed 2026-08-26, cross-referenced back to [[PL-KSC]] which had gone stale on this point). Only CSIRT MON remains unmodelled, because Poland's Ministry of National Defence is not an Atlas entity |
| **Agencja Informatyzacji** | The body a draft law would create from [[PL-COI]]. Does not exist; same refusal as Spain's Centro Nacional de Ciberseguridad |
| **GIODO** | The predecessor DPA. **Narrower as of 2026-08-26**: UODO's own annual report calls the President its legal successor ("następcą prawnym"), stronger language than "took over only part of its competencies." Still no entity created — GIODO's own site no longer resolves (DNS failure) |
| **Krajowe Ramy Interoperacyjności**, a Polish DCAT profile, the Act on Public Statistics | All named in sources, none researched. |

### Factual gaps — Poland

| Entity | Question | Status |
|---|---|---|
| [[PL-ODO]] | ~~No Dz.U. or ISAP citation~~ — **narrower 2026-08-26**: two of three sources now read directly (UODO's own annual report, politykabezpieczenstwa.pl), but ISAP's own text remains genuinely CAPTCHA-blocked and no Dz.U. citation was obtained. Substantive GDPR-specification provisions still not established | Open |
| [[PL-KSC]] | ~~The CJEU proceedings rest on industry commentary~~ — **resolved 2026-08-26 by correction**: the claim itself was wrong (see above), not merely under-sourced. The corrected claim (letter of formal notice) is confirmed by the European Commission's own page | **Closed — corrected** |
| [[PL-MOBYWATEL]] | The **eIDAS 2.0 incompatibility rests on press reporting only** — confirmed still true 2026-08-26 after reading a second press source (biznesinfo.pl) in more technical detail; still no ministry or Commission document found. This is why the edge is `confidence: low` | **Open — priority** |
| [[PL-DANE-GOV-PL]] | ⚠ **Not one source is the portal's own site** — dane.gov.pl's own homepage remains a JavaScript application with no static content an automated fetch can retrieve. | **Partly resolved 2026-08-27** — the operator gap is closed: gov.pl's own Ministry of Digitisation page, found via search and read directly, names the Minister of Digitisation as responsible for the system and gives an approximate launch date (since May 2014, not a specific day). The portal's own site remains unreachable. |
| Institutional transformations | Three now touched in two countries — Spain's completed, Poland's COI one **pending**, Poland's GIODO one **narrower but still unmodelled** (UODO's own report now calls it a legal succession). Only the Spanish one is modelled as a succession. Worth handling deliberately rather than case by case | Open (modelling) |

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

## Intelligence and security services (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[DE-UKR]] | **Which instrument constitutes the Unabhängiger Kontrollrat now?** | Sources say its provisions were to be removed from [[DE-BNDG]] in implementation of the Bundesverfassungsgericht's decision of 28 September 2022. Where they were relocated could not be established, so this is the **only oversight body in the batch with no `governed-by` edge**, and the entity carries `confidence: low`. | 2026-08-18 | **Partially resolved, 2026-08-22.** de.wikipedia.org's UKR article names the destination: a dedicated "Gesetz über den Unabhängigen Kontrollrat". Whether the transfer out of the BND-Gesetz has actually completed is still not established — the article describes the plan, not a commencement date for the new act — so `governed-by` remains unasserted. `confidence` raised to `medium` on the strength of what is now sourced. |
| [[DE-UKR]] | Has the bill extending its remit to [[DE-BFV]] been enacted? | Two political-press reports describe a government bill. Only the [[DE-BND]] edge is asserted. If enacted, a second `applies-to` follows. | 2026-08-18 | Open |
| [[FR-CNCTR]] / France | **The délégation parlementaire au renseignement is not modelled.** | France currently appears in the Atlas with independent legality control and **no parliamentary control**, which is not an accurate picture of French oversight. Germany, the UK and Poland all have their parliamentary body modelled. | 2026-08-18 | Open — known gap |
| [[FR-CNCTR]] | DNRED and TRACFIN — two of the six *premier cercle* services — are absent. | The CNCTR's four `applies-to` edges understate its remit by two. Both are customs and financial bodies whose primary function is not intelligence, so this is a scoping decision rather than an oversight. | 2026-08-18 | Open — scoping |
| [[FR-DGSI]] | Does [[FR-LIL]] Title IV name the DGSI as a controller? | The `governed-by` edge is carried at **`confidence: low`**: the sources describe the state-security and defence regime and name CRISTINA, a file of the DGSI's predecessor, rather than naming the service. It is the weakest of the batch's cross-cluster bridges. | 2026-08-18 | Open |
| [[DE-G10]] | The **G10-Kommission** is not modelled. | It authorises measures under the Artikel 10-Gesetz and is distinct from [[DE-PKGR]] and [[DE-UKR]]. Germany therefore shows two oversight bodies where it has at least three. | 2026-08-18 | Open |
| [[GB-IPCO]] | The IPA's **"double lock"** and the Judicial Commissioners are not modelled. | This is the UK's nearest analogue to [[NL-TIB]]'s binding prior review, and the batch's comparison of authorisation models is incomplete without it. No source read describes the mechanism. | 2026-08-18 | Open |
| [[GB-MI5]] | **Defence Intelligence** has no avowal act and was not researched. | The UK appears with three services where France has four and Poland four. | 2026-08-18 | Open |
| [[BE-WIV-1998]] | The **BIM-wet of 4 February 2010** and the **BIM-commissie** are not modelled. | Belgium appears with an organic act and an oversight act and **no authorisation regime**, which is not a complete picture. | 2026-08-18 | Open |
| [[BE-COMITE-I]] | **OCAD/OCAM** is not modelled. | The 1991 act was amended on 10 July 2006 to place OCAD under the joint supervision of Comité P and Comité I. The arrangement is recorded in prose and not in the graph. | 2026-08-18 | Open — scoping |
| [[PL-ABW]] | **CBA** is not modelled, and its current status was not established. | The sources name it among the five services under the College for Special Services and within [[PL-KSS]]'s remit. | 2026-08-18 | Open |
| [[PL-KSS]] | Does Poland have an **independent legality-review body** comparable to [[FR-CNCTR]] or [[NL-TIB]]? | Not researched. Poland currently shows parliamentary oversight with no independent counterpart, which may or may not reflect Polish law. | 2026-08-18 | Open |
| [[PL-USKWSWW-2006]] | **No official Polish government URL** could be found. | Its Dz.U. reference, consolidation and amendment history are all unestablished — in sharp contrast to [[PL-UABWAW-2002]], which both agencies publish. | 2026-08-18 | Open |
| [[DE-BVERFSCHG]], [[DE-MADG]] | **No Gesetze-im-Internet URL** was returned by search. | Their dates, structure and amendment history are unestablished, unlike [[DE-BNDG]] and [[DE-PKGRG]]. | 2026-08-18 | Open |
| [[ES-LEY-11-2002]] | **No BOE URL** was returned by search. | A commercial legal database stood in for the official gazette on the act that creates [[ES-CNI]] — while [[ES-LO-2-2002]], passed the same day, does have its BOE citation. | 2026-08-18 | ✅ **Resolved** — BOE-A-2002-8628 now cited and read directly. |
| [[NL-TWCO]] | What **are** the deviations from the [[NL-WIV-2017]] regime, and how do [[NL-TIB]]'s and [[NL-CTIVD]]'s remits change? | The sources describe the act's purpose, not its provisions. Neither oversight entity carries a relationship to this act as a result. | 2026-08-18 | Open |
| [[NL-TWCO]] | Can the four-year expiry be extended? | `end_date` is deliberately **null**: the sources give a rule ("four years after entry into force"), not a date, and say nothing about extension. Computing 2028-07-01 and presenting it as sourced would be the Atlas doing arithmetic. | 2026-08-18 | Open |
| [[DE-BNDG]] | What did the **2021 and 2023 amendments** change? | The Bundestag's archive records both. Neither's content was established. | 2026-08-18 | Open |
| [[ES-CNI]] | **CIFAS** and the police/Guardia Civil information services are not modelled. | Sources mention a common inspection regime covering them. Spain appears as a one-service country, which is true of the CNI's civilian/military scope but not of the whole Spanish intelligence landscape. | 2026-08-18 | Open |

## Norway, Switzerland and Ireland (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NO]] | **The EEA Agreement and JCD No 154/2018 are not entities.** | Norway's entire route to EU instruments is recorded in prose because there is nothing in the graph to point at. Creating either would turn the batch's central finding into a relationship. **Highest-value follow-up from this batch** | 2026-08-18 | **Open — next** |
| [[NO-SSB]] | On what basis does an EEA EFTA statistical office participate in European statistical cooperation? | Five Atlas offices are `part-of` [[EU-ESS]]; [[GB-ONS]] reaches [[UN-CES]]. SSB has neither, because the ESS is defined as a partnership with member-state institutes. The third pattern is real and unstated | 2026-08-18 | Open |
| [[NO-DATATILSYNET]] | What standing do EEA EFTA authorities have on [[EU-EDPB]]? | The sources say cooperation runs through "EEA-specific channels" without saying what that means for Board participation. `participates-in` is therefore not asserted | 2026-08-18 | Open |
| [[NO-KARTVERKET]] | Was **INSPIRE** incorporated into the EEA Agreement, and by which Norwegian act does it take effect? | Cannot be answered by assuming the member-state answer — that is the whole point of the [[NO]] anchor | 2026-08-18 | Open |
| [[NO-ID-PORTEN]] | Was **eIDAS** incorporated into the EEA Agreement, and is ID-porten a notified scheme? | Neither established. [[ES-CLAVE]] already carries `confidence: low` for confusing an eIDAS *node* with a notified scheme; repeating that across an EEA boundary would be worse | 2026-08-18 | Open |
| [[NO-ALTINN]] | **Who operates Altinn?** | Digdir's own page lists the solutions it operates and Altinn is not among them; it appears instead among solutions Digdir *modernises*. Historically Brønnøysundregistrene. No `maintained-by` edge asserted | 2026-08-18 | ✅ **Partly resolved — 2026-08-22.** altinn.no's own site footer identifies Digdir's own address and organisation number as publisher. `maintained-by` NO-DIGDIR now asserted at `confidence: low` (`source: interpretation`) — a footer is not the same claim as an explicit operating statement, and whether Brønnøysundregistrene retains any role was not resolved. |
| [[NO-NSM]] | Its statutory basis — the **sikkerhetsloven** — is not an entity. | NSM carries no `governed-by` edge as a result. One source calls NSM part of the secret services; that phrasing is not in the government sources and the Atlas will not classify on it | 2026-08-18 | ✅ **Resolved (the classification question) — 2026-08-22.** NSM's own website states directly that NSM, together with Etterretningstjenesten and PST, forms Norway's three intelligence, surveillance and security services — no longer resting on an encyclopaedia entry. The statutory-basis question is narrowed but still open: snl.no names "sikkerhetsloven av 1998," but NSM's own site separately lists a newer "Digitalsikkerhetsloven," and which is current was not resolved; still no `governed-by` edge. |
| Norway | **Etterretningstjenesten and PST are not modelled.** | Norway has a national security authority and no intelligence services, three days after a batch that gave seven countries both | 2026-08-18 | Open |
| [[CH-REVDSG]], [[CH-EMBAG]] | **No Fedlex citation anywhere in the Swiss set.** | [[CH-REVDSG]] carries the batch's most comparative weight — the `aligned-with` argument — on a KMU-portal page, a university blog and a vendor guide | 2026-08-18 | ✅ **Partly resolved — 2026-08-22.** Both now cite Fedlex directly (`eli/cc/2022/491/de` and `eli/cc/2023/682/de`), found via outbound links on kmu.admin.ch's and bfs.admin.ch's own pages. Fedlex renders client-side in JavaScript, so neither citation could be read past retrieval — the same tooling limit already logged for PDFs. |
| [[CH]] | The **EU–Switzerland adequacy decision** is not an entity. | The Atlas holds [[EU-UK-ADEQUACY]]; the same kind of Commission act covers Switzerland, and the whole revDSG revision was aimed at preserving it | 2026-08-18 | Open |
| [[CH-BACS]] | What is the statutory basis of the **24-hour reporting duty** in force since 1 April 2025? | Understood to be the Information Security Act (ISG), not researched. The duty matches [[EU-NIS2]]'s without Switzerland being bound by it, and **no relationship is asserted** — resemblance is not derivation | 2026-08-18 | Open |
| [[CH-OPENDATA-SWISS]] | Does [[CH-EMBAG]] govern the portal? | The act creates the legal basis for open government data; this is the federal OGD portal. No source read connects them **by name**. An entity pair this obvious is exactly where a repository starts inventing edges | 2026-08-18 | ✅ **Resolved — 2026-08-22.** bfs.admin.ch's own "Open Government Data (OGD)" page states directly that the OGD office operating opendata.swiss does so "gemäss dem [EMBAG]." `governed-by` now asserted. |
| [[CH-DVS]] | Legal form, governance, and relationship to [[CH-EMBAG]]. | `coverage: low`; only its own site was returned. It is constituted jointly across Confederation, cantons and communes — filed `level: national` because that is the closest available value, **not because it is accurate** | 2026-08-18 | Open — and see the `level: local` design item. Re-checked 2026-08-22: DVS's relationship to EMBAG remains unsourced (its blog post is evidence of interest, not of a role under the act), and the January 2022 operational-start date could not be independently re-confirmed either. |
| [[IE-TAILTE]] | **Was the merger confirmed, and when?** | `confidence: low`, `start_date` null. Neither citation is a government legal source. The weakest entity in the batch | 2026-08-18 | ✅ **Resolved — 2026-08-22.** en.wikipedia.org's Ordnance Survey Ireland article states it directly: dissolved 1 March 2023, folded into Tailte Éireann along with the Property Registration Authority and the Valuation Office. `confidence` raised to medium, `start_date` set. |
| [[IE-NCS-BILL]] | **Has it been enacted?** | `status: proposed` as at 18 August 2026, on a source reporting a Q3 2026 planning assumption. May already be stale. Its final content and even its short title are unsettled | 2026-08-18 | **Open — still not enacted as at 2026-08-22**, and the situation escalated: the European Commission sent a reasoned opinion on 7 May 2025, then referred Ireland and three other member states to the CJEU in July 2026. |
| [[IE-NSAI]] | Is NSAI a member of CEN, CENELEC and ISO? | Almost certainly, and **not asserted**: the CEN-CENELEC members page was returned by search and not read, so the Atlas has a URL that probably lists NSAI and no confirmation. [[GB-BSI]] carries five such edges and is the most connective UK entity | 2026-08-18 | ✅ **Partly resolved — 2026-08-22.** The old CEN-CENELEC URL had moved (404); its replacement (`standards.cencenelec.eu/ords/f?p=CEN:5`) confirms the composition rule, and `participates-in` [[EU-CEN]]/[[EU-CENELEC]] edges — already described in this entity's own prose but missing from its structured data — are now asserted. **ISO membership remains unconfirmed and unasserted.** |
| [[UN-AARHUS]] | Ireland's ratification date and terms. | The other six member states carry `applies-in`; Ireland does not, because this batch did not gather the evidence for a mixed agreement | 2026-08-18 | Open |
| [[IE-DATA-GOV-IE]] | Ireland's **Open Data Directive transposition** (an S.I.) was not identified. | Ireland joins Belgium, France and Spain on that list — four countries is a batch of its own | 2026-08-18 | ✅ **Resolved before this row was last updated** — the entity itself already names [[IE-PSI-REGULATIONS-2021]] (S.I. No. 376/2021). Both entities re-verified 2026-08-22 confirm the instrument's exact dates directly from its text. |
| [[IE-DPA-2018]] | The **Law Enforcement Directive** (2016/680) is still not an Atlas entity. | Part 5 of the Irish Act transposes it, and it is one of the two legal bases of [[EU-UK-ADEQUACY]]. Queued since the UK batch and now blocking a second entity | 2026-08-18 | Open |

## Data spaces (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-MANUFACTURING-DATA-SPACE]] / [[DE-MANUFACTURING-X]] | Is the German initiative part of, feeding into, or independent of the common European manufacturing data space? | They occupy the same sector, and the EU data space's named deployments (UNDERPIN, SM4RTENANCE) are not connected to Manufacturing-X by any source read. Same sector is not a relationship | 2026-08-18 | Open |
| [[EU-PUBLIC-ADMIN-DATA-SPACE]] | How does it relate to [[EU-INTEROPERABLE-EUROPE-ACT]], [[EU-EIF]] and [[EU-SDG]]? | This is the data space closest to the Atlas's own subject matter — 232 entities carry [[DOMAIN-GOVERNMENT]] — and the entity where drawing unsourced edges would be most tempting. None is asserted | 2026-08-18 | Open |
| [[EU-FINANCIAL-DATA-SPACE]] | **What are the other two components?** | The sources name FIDA as one of three and do not name the rest. An entity whose own description admits it is one-third specified | 2026-08-18 | Open |
| [[EU-FINANCIAL-DATA-SPACE]] | **FIDA** is not an entity, nor is **PSD2**. | FIDA is the only named legislative component of any of the fourteen apart from the EHDS Regulation | 2026-08-18 | Open |
| [[EU-CULTURAL-HERITAGE-DATA-SPACE]] | **Europeana** and the Europeana Foundation are not modelled. | The operator of the data space, holding 60M+ items — the batch's most conspicuous missing organisation. The **Europeana Data Model** would also connect to the metadata layer around [[INTL-DCAT]] | 2026-08-18 | **Open — next** |
| [[EU-CULTURAL-HERITAGE-DATA-SPACE]] | Cooperation with [[EU-MEDIA-DATA-SPACE]] and [[EU-TOURISM-DATA-SPACE]] | The sources say it "will explore opportunities for cooperation" with both. Intent is not connection, so no edge is asserted from either side | 2026-08-18 | Open |
| [[EU-TOURISM-DATA-SPACE]], [[EU-MEDIA-DATA-SPACE]], [[EU-SKILLS-DATA-SPACE]], [[EU-PUBLIC-ADMIN-DATA-SPACE]] | Deployment projects, governance, operators, scope. | All four are `coverage: low`, created for completeness of the fourteen. Their thinness is the honest state | 2026-08-18 | Open |
| [[EU-EOSC]] | Does the **EOSC Federation** admit non-member states? | Its federated design is the closest thing in the Atlas to what [[NO]] and the EEA states would need. Not researched | 2026-08-18 | Open |
| [[EU-EOSC]] | The **EOSC Association** is a distinct body from the Federation and from the Commission's EU Node, and is not modelled. | Three things share the name EOSC and only one is an entity | 2026-08-18 | Open |
| [[EU-SKILLS-DATA-SPACE]] | **ESCO**, **Europass** and the **European Skills Agenda** are not modelled. | The existing EU skills-data machinery this data space presumably builds on. Presuming is not sourcing | 2026-08-18 | Open |
| [[INTL-IDS-RAM]] | The **IDS Connector** is not modelled. | It is the central technical component — a security gateway with Base, Trust and Trust+ profiles, the last protecting against manipulation by malicious administrators. `technology` is a type the Atlas defines and still does not use | 2026-08-18 | Open — and see the unused-type item |
| [[INTL-IDS-RAM]] | Version. | The entity describes **IDS-RAM 3.0** (April 2019), the version search returned. Version 4 exists and was not established | 2026-08-18 | Open |
| [[INTL-IDSA]] | Membership, given by one source as 133 companies, is unverified; the **Eclipse Dataspace Connector** implementations are unmodelled | | 2026-08-18 | Open |
| [[DE-MANUFACTURING-X]] | **Factory-X**, **Aerospace-X**, **energy data-X** and **Plattform Industrie 4.0** are not modelled. | Named in the sources as lighthouse projects, siblings and the concept base | 2026-08-18 | Open |
| [[EU-CEEDS]] | **INSIEME** and the six Horizon Europe energy data space projects are not modelled; nor is Germany's **ENDA**. | The concrete deployment layer beneath the data space | 2026-08-18 | Open |

## Portugal, Luxembourg and Czechia (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[LU-CNPD]] | **Luxembourg's GDPR implementation act** — the date (1 August 2018) is now sourced, via an ELI URL linked from CNPD's own "Législation" page (2026-08-25), but the act's official title and text are still unread: `legilux.public.lu` is a JavaScript single-page application with no static content. | Luxembourg is the **only member state in the Atlas** with no national GDPR instrument. Ten others have one | 2026-08-18; date sourced 2026-08-25 | **Open — narrower** |
| [[CZ-NUKIB]] | **NIS2 transposition not identified** for Czechia. | Czechia's cyber security act No 181/2014 is also unmodelled. Portugal's own gap (PT-CNCS) was closed 2026-08-26: [[PT-DECRETO-LEI-125-2025]], in force since 3 April 2026 | 2026-08-18; PT closed 2026-08-26 | Open — Czechia only |
| [[LU-CTIE]] | **Luxembourg's NIS2 competent authority and CSIRT** are unmodelled. | CTIE secures the State's own infrastructure, which is a different job from supervising a country's essential entities. GOVCERT.LU was not researched | 2026-08-18 | Open |
| [[CZ-UNMZ]] | **ČAS is not modelled.** | Czechia splits standardisation: ÚNMZ holds the membership, ČAS does the technical committees, drafting and publication. The body that actually produces ČSN standards is absent from the graph | 2026-08-18 | Open |
| [[LU-DATA-PUBLIC]] | **No custodian modelled.** | [[LU-CTIE]] is the obvious operator and it is not sourced. Portugal's and Czechia's equivalent gaps (PT-DADOS-GOV, CZ-DATA-GOV) were both closed by 2026-08-26 | 2026-08-18; PT and CZ closed | Open — Luxembourg only |
| [[CZ-ZAKON-60-2026]] | What does the act contain beyond [[CZ-DIA]]'s role? | `coverage: low`. What "controlled access" covers, which data, what rights it creates — all unestablished. `start_date` is deliberately null: the sources give the Sb. citation, not a date of effect | 2026-08-18 | Open |
| [[CZ-DIA]] | **Act No 12/2020** on the right to digital services, DIA's constituting statute, is not modelled. | DIA carries `implements` [[CZ-ZAKON-60-2026]] but no `governed-by` edge to the act that created it | 2026-08-18 | Open |
| [[LU]] | Should hosting an EU institution be modelled at all? | The Court of Justice, the Court of Auditors, the EIB and [[EU-PUBLICATIONS-OFFICE]] are seated in Luxembourg and **no relationship is asserted**. Modelling it would make every host state look like a participant in what it hosts. Recorded as a deliberate design position, not a gap | 2026-08-18 | **Closed — by decision** |
| [[LU-ILNAS]] | Its **accreditation** (OLAS) and market-surveillance functions are unmodelled. | Two-thirds of what the institute does | 2026-08-18 | Open |
| [[PT-AMA]] | **ePortugal**, the **Chave Móvel Digital**, the **Cartão de Cidadão** and the **iAP** are unmodelled. | Portugal's identity means would be the [[EU-EIDAS]] counterparts; the iAP is its interoperability platform | 2026-08-18 | Open |
| Standards bodies generally | The membership counts in the Atlas are what is **sourced**, not what is true. | [[LU-ILNAS]] and [[GB-BSI]] show five, [[PT-IPQ]] three, most others two — because the CEN membership rule was the only source available for the four created in the structural-fixes batch. The column invites a comparison it cannot fully support | 2026-08-18 | Open |

## Research-queue batch (2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-OPEN-DATA-DIRECTIVE]] | **The Atlas cannot model enforcement against a member state.** | Nineteen member states faced infringement proceedings over this directive and four — Belgium, Bulgaria, Latvia and the **Netherlands** — were referred to the Court of Justice in February 2023. There is no entity type for an infringement procedure, no relationship type for "was referred to the Court over", and no Court of Justice entity. A reader sees that [[NL-WHO]] was amended in 2024 and cannot see why | 2026-08-18 | **Open — ontology gap** |
| Belgium, France, Spain | **Open Data Directive transpositions still unidentified.** | All three amended existing law rather than passing a standalone act, which is why they are harder to find than Ireland's S.I. Down from five countries to three | 2026-08-18 | **Open — next** |
| [[PT-LEI-26-2016]] | ~~Which amendment transposed the Directive, and when?~~ **Resolved 2026-08-26**: Lei n.º 68/2021, of 26 August, confirmed by reading the Diário da República's own text directly. | Closes the gap; `valid_from: 2021-08-26` is now sourced rather than null | 2026-08-18; resolved 2026-08-26 | **Closed** |
| [[PT-LEI-26-2016]] | A general European survey places Portugal among the **standalone-legislation** countries; the Portugal-specific sources describe an amendment. | The Atlas follows the specific source. Re-reading the primary text this pass (the amending act itself) confirms the amendment pattern directly, not just via secondary description — the general survey appears to be wrong about Portugal | 2026-08-18; re-confirmed 2026-08-26 | **Closed — conflict resolved toward the specific source** |
| [[EU-OPEN-DATA-DIRECTIVE]] | **Commission Implementing Regulation (EU) 2023/138** on high-value datasets is not modelled. | It applies across the Union and is named by the Portuguese sources. A gap affecting every member state, not one | 2026-08-18 | Open |
| [[EU-PSI-DIRECTIVE]] | **Directive 2013/37/EU**, the amending directive, is not modelled. | Its content was not established, and an entity for an amendment that was itself repealed would add a node and no clarity | 2026-08-18 | Open — scoping |
| [[EU-EN-16931]] | **CEN/TC 434** is not modelled, nor the **UBL and CII syntax bindings** or the CIUS mechanism. | The committee is a committee, not a body — the same reasoning that keeps the Czech NCKB out. The syntax bindings are what make the semantic model usable | 2026-08-18 | Open — scoping |
| [[EU-EN-16931]] | Other national **CIUSes** — Italy's, France's, the Peppol BIS profile. | [[DE-XRECHNUNG]] is the only one modelled, which makes the German case look unique when it is one of several | 2026-08-18 | Open |
| [[IE-PSI-REGULATIONS-2021]] | The Atlas's `type: law` **flattens primary and secondary legislation.** | This is a statutory instrument; [[IE-DPA-2018]] is an Act of the Oireachtas. Both are `law`, and only the names and the entity bodies record the difference | 2026-08-18 | Open — ontology |
| Poland | **CSIRT MON** is still unmodelled. | [[PL-NASK]] and [[PL-ABW]] cover CSIRT NASK and CSIRT GOV; the third national CSIRT sits at the Ministry of National Defence, which is not an Atlas entity | 2026-08-18 | Open |

## The Dutch register statutes (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-BRI]] | **Chapter IVA of the AWR** — no citable identifier found for it as a distinct instrument. | The one register of ten still without a `governed-by` edge. The sources name the chapter; the Atlas has no way to cite a chapter of an act as an entity, and creating a `NL-AWR` for the whole Algemene wet inzake rijksbelastingen would overstate what the register rests on | 2026-08-18 | **Open — and an ontology question** |
| [[NL-KADASTER]] | The **Organisatiewet Kadaster** (BWBR0006463) is not modelled. | It constitutes the Dienst voor het kadaster en de openbare registers as a body, where [[NL-KADASTERWET]] governs the registers. The cleanest body/registers statute pair in the Atlas, with only one half modelled | 2026-08-18 | Open |
| All seven new statutes | The **Besluit** and **Regeling** instruments beneath each act are not modelled. | [[NL-WET-BRO]]'s are the best evidenced (BWBR0040205, BWBR0040482). A consistent scoping decision rather than an oversight, recorded so it is not mistaken for one | 2026-08-18 | Open — scoping |
| [[NL-WET-BAG]] | The **original** commencement date. | `start_date` is null: the sources give the 2017 amending act (Stb. 2017, 60) in force 1 July 2018, not the original act's commencement | 2026-08-18 | ✅ **Resolved — re-verification pass, 2026-08-21.** The original act's own "Origineel opschrift en aanhef" on `wetten.overheid.nl` reads "Wet van 24 januari 2008"; `start_date` is now `2008-01-24`. |
| [[NL-WET-BRO]] | The **2024 amendment** on bronhouderschap of models and quality control. | Recorded by the Tweede Kamer as a pending change; its content and status were not established | 2026-08-18 | Open |
| [[NL-NHR]] | **BRIS** and the Company Law Directive are not modelled. | The Dutch commercial register is part of an EU-wide interconnection system, and the Atlas shows it as purely national | 2026-08-18 | Open |
| All seven new statutes | **No statute text was read.** | `wetten.overheid.nl` is blocked by this environment's egress proxy. Every entity is keyed on a BWBR identifier confirmed by search and not retrieved — and a search for the Kadasterwet's identifier returned BWBR0007376, which is the **Archiefwet 1995**. A wrong identifier resolves to a real but unrelated act, so these seven should be verified first when retrieval is possible | 2026-08-18 | ✅ **Resolved — re-verification pass, 2026-08-21.** All seven statute texts were read from `wetten.overheid.nl` (egress now open). BWBR0004541 is confirmed as the Kadasterwet's own identifier, not the Archiefwet's. Two corrections found: [[NL-KADASTERWET]]'s "Kadasterwet 1989" alternative name was not attested (removed) and [[NL-WET-BGT]]'s third commencement stage was mis-dated 30 April 2018 instead of the correct 1 July 2018. All seven now `verification: primary-source`. |

## Candidate-clearing batch, 2026-08-21

| Entity / topic | Question | Why it's unresolved | Noted by / date | Status |
|---|---|---|---|---|
| [[LI-DSG]] | Is it *based on* the German BDSG, or only described that way? | The sources say the Liechtenstein act is "modelled after" the German Federal Data Protection Act rather than Swiss law. `based-on` claims the legislature adapted a specific text; a law-firm commentary characterising legislative style is not that. Recorded in prose on the entity and no edge asserted | Candidate batch / 2026-08-21 | Open |
| [[EU-VOLUNTARY-REVIEW-2023]] | What date did the Commission adopt COM(2023) 700 final? | The sources give the HLPF presentation window (10–20 July 2023) and the document reference, and no adoption date. `start_date` is `null` rather than a plausible-looking guess | Candidate batch / 2026-08-21 | Open |
| [[EU-EMSWE]] | Are the SafeSeaNet codes and the IMO GISIS port facility codes Atlas subjects? | They are named in the same provision as [[UN-LOCODE]] and neither is modelled. The IMO is not in the Atlas at all; creating it to carry one code list would be the thin entity the taxonomy threshold prevents | Candidate batch / 2026-08-21 | Open (scope) |
| [[EU-EUROGEOGRAPHICS]] | Which of the 63 member organisations are in the Atlas? | Five are attached — [[NL-KADASTER]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[GB-OS]], [[IE-TAILTE]] — on the sourced composition rule, not on a member list. The list itself is on a blocked host, so whether other Atlas organisations qualify is unchecked | Candidate batch / 2026-08-21 | Open (egress) |
| [[EU-REG-223-2009]] | Should the three instruments it repealed be modelled? | Regulation (EC, Euratom) No 1101/2008, Council Regulation (EC) No 322/97 and Council Decision 89/382/EEC are all repealed and none is an entity, so no `supersedes` edge is asserted. Three pre-2009 nodes carrying one edge each is probably not worth it, but the omission is a real one | Candidate batch / 2026-08-21 | Open (scope) |

## Rest-of-world country-anchor batch, 2026-08-27

Eighteenth verification-gap push: the 25 single-entity "rest of world" country anchors (added outside the European country batches, each carrying exactly one relationship) were the last multi-country tail of the ongoing re-verification series. Two families:

- **17 Council of Europe members/near-members** — [[AD]], [[AL]], [[AM]], [[AZ]], [[BA]], [[BY]], [[GE]], [[MC]], [[MD]], [[ME]], [[MK]], [[RS]], [[RU]], [[SM]], [[TR]], [[UA]], [[VA]] — all promoted to `verification: primary-source`. `coe.int` and ISO's OBP both proved genuinely, domain-wide blocked (403) — the OBP is a JavaScript application with no static content to fetch — so all 17 rest on two Wikipedia articles read directly instead: the general "Council of Europe" article and the dedicated "Member states of the Council of Europe" article, whose own accession table supplied an exact date for every member (previously each entity carried only a bare year "from general reference knowledge"). **One correction**: [[TR]] previously said Türkiye joined the Council of Europe in 1949 — the Council's own founding year — when the table gives Türkiye's actual accession as **13 April 1950**. The nine EU-candidate countries in this set ([[AL]], [[BA]], [[GE]], [[MD]], [[ME]], [[MK]], [[RS]], [[TR]], [[UA]]) keep their existing candidacy years as prior knowledge, not independently re-confirmed to a specific month/day this pass — `enlargement.ec.europa.eu`'s own page was read but its content did not cleanly map to per-country candidacy-granted dates.
- **8 Convention 108 non-Council-of-Europe parties** — [[AR]], [[CV]], [[MU]], [[MX]], [[MA]], [[SN]], [[TN]], [[UY]] — all stay `search-only`. Wikipedia's Convention 108 article was read directly and confirms all eight by name in its own words, but ISO's OBP is confirmed blocked (403) and the WTO PDF citation is confirmed genuinely unreadable (an image-based scan with no extractable text) — one of three sources read is not a majority, the same honest call made for [[FR-DGSI]] and others earlier in this series.

Every one of the 25 entities' `last_verified` was updated regardless of promotion outcome, and every caveat/body text was rewritten to match its frontmatter — no entity was left with a stale "not read, environment blocks retrieval" claim once its sources had actually been attempted this pass.

## NL Batch 1 — Basic-registers/geospatial cluster re-verification (2026-08-27)
Nineteenth verification-gap push (one of three concurrent NL batches):
re-verified all 22 entities in the basisregistraties/geospatial cluster —
12 platforms ([[NL-BAG]], [[NL-BGT]], [[NL-BRI]], [[NL-BRK]], [[NL-BRO]],
[[NL-BRP]], [[NL-BRT]], [[NL-BRV]], [[NL-NHR]], [[NL-WOZ]], [[NL-PDOK]],
[[NL-NDW]]), 6 organisations ([[NL-KADASTER]], [[NL-RVIG]],
[[NL-BELASTINGDIENST]], [[NL-WAARDERINGSKAMER]], [[NL-RDW]],
[[NL-NATIONAAL-ARCHIEF]]), 3 legislation ([[NL-WET-BRP]],
[[NL-ARCHIEFWET-1995]], [[NL-ARCHIEFWET-2026]]) and 1 standard
([[NL-NEN-3610]]). **All 22 promoted to `verification: primary-source`** —
every one reached a genuine majority of its cited sources read directly,
several after finding replacement sources via WebSearch for originals that
proved dead.
**Confirmed-dead/blocked sources, by kind (noted explicitly on each
affected entity rather than silently dropped):**
- `digitaleoverheid.nl`'s per-register subpages are **inconsistently
  bot-walled**: the `/bgt/`, `/bro/`, `/brp/` and `/brt/` subpages rendered
  real content on the first attempt, but `/bri/`, `/brv/`, `/hr/`, `/brk/`
  and the `rollen-stelsel-basisregistraties/` page returned a
  "please wait while your request is being verified" challenge page on
  every attempt (two attempts each for several). Affects [[NL-BRI]],
  [[NL-BRV]], [[NL-NHR]], [[NL-KADASTER]], [[NL-BELASTINGDIENST]],
  [[NL-RDW]]. Genuinely blocked, not merely unread.
- Two Waarderingskamer PDF catalogues (`Catalogus-Basisregistratie-WOZ`,
  `Catalogus-WOZ-gegevens-voor-afnemers`) fetch as raw binary with no
  extractable text — the same "image/binary PDF" failure mode logged
  elsewhere in this series. Affects [[NL-WOZ]] and
  [[NL-WAARDERINGSKAMER]].
- `waarderingskamer.nl/voor-gemeenten/gegevensbeheer/lv-woz` returned
  HTTP 503 both times it was fetched. `waarderingskamer.nl`'s IMWOZ page
  returned HTTP 404. `docs.geostandaarden.nl`'s NEN 3610 Linked Data
  profile page returned HTTP 404. `wetgevingskalender.overheid.nl`
  returned HTTP 503.
**Replacement sources found via WebSearch, closing five otherwise-stuck
entities to genuine majorities:**
- [[NL-WAARDERINGSKAMER]] — all four original sources proved unreadable
  (see above); five `waarderingskamer.nl`/`rijksoverheid.nl` pages
  (`over-ons`, `wie-zijn-wij`, `wat-wij-doen`, `ons-toezicht`, the
  rijksoverheid contactgids entry) were found and read directly, giving a
  5-of-9 majority. Also newly confirmed: it is a **zelfstandig
  bestuursorgaan (zbo)** under the Ministerie van Financiën, and its tasks
  derive specifically from **Article 4 of the Wet WOZ** — added as a new
  `applies-to` relationship, previously absent.
- [[NL-KADASTER]] — `nl.wikipedia.org/wiki/Kadaster_(Nederland)` added to
  replace two dead originals (digitaleoverheid.nl bot-walled, NORA Online
  404), also supplying a founding date (**1 October 1832**, as Dienst voor
  het kadaster en de openbare registers) and zbo status since 1994 that the
  entity did not carry before.
- [[NL-BRV]] — RDW's own kentekenregister page and the Wegenverkeerswet
  1994's official text (`wetten.overheid.nl/BWBR0006622`) added to replace
  two bot-walled digitaleoverheid.nl pages.
- [[NL-NHR]] — the Handelsregisterwet 2007's official text
  (`wetten.overheid.nl/BWBR0021777`) added, closing the gap this entity
  previously flagged as **the one register in the batch with no statutory
  basis modelled at all**.
- [[NL-BRT]] / [[NL-BRK]] — the Kadasterwet's official text
  (`wetten.overheid.nl/BWBR0004541`) read directly for both, confirming
  Article 1a establishes the BRK and BRT registrations in the same
  sentence — closing [[NL-BRT]]'s own previously-flagged gap as the only
  register with no statute confirmed at all.
**Two substantive corrections found by reading primary text, not just
re-confirming search-derived claims:**
1. [[NL-BRO]] — [[NL-TNO]]'s Geologische Dienst Nederland became the BRO's
   **official manager on 1 January 2022**, not at the register's 2018
   commencement as the entity previously implied continuously. Confirmed
   by reading `geologischedienst.nl`'s own 2022 announcement directly.
   Geonovum is also confirmed as standards **trekker (lead)**, not merely
   a publisher — its own page states this in those words.
2. [[NL-ARCHIEFWET-2026]] — **major status update**. This was carried as a
   `status: planned` bill with `confidence: low`. Reading its own
   Staatsblad publication directly (`zoek.officielebekendmakingen.nl/stb-2026-149.html`)
   confirms it was **signed 13 May 2026 and published as Stb. 2026, 149 on
   19 June 2026** — enacted, not merely progressing through parliament.
   Its own Article 12.14 defers the exact entry-into-force date to a royal
   decree not yet issued; **1 January 2027 is the intended date given by
   secondary official sources (nationaalarchief.nl, rijksoverheid.nl), not
   yet fixed in the Act's own text** — recorded as such rather than stated
   as settled. The prior three-way naming ambiguity ("Archiefwet 2026" vs
   "Archiefwet 2021" vs "Nieuwe Archiefwet 20xx") is now resolved in the
   Atlas's favour: the Staatsblad citation itself is dated 2026, supporting
   the existing `NL-ARCHIEFWET-2026` ID and name. `confidence` raised
   `low` → `medium` accordingly; `status` stays `planned` since the Act is
   not yet in force and the Atlas's `status` vocabulary has no
   "enacted, not yet commenced" value.
**Two-stage BAG–BRP coupling, previously described as one arrangement**
([[NL-BAG]], [[NL-BRP]], [[NL-RVIG]]): reading RvIG's own coupling-guidance
pages directly reveals a one-time technical coupling in 2011–2012 and a
separate **mandatory, ongoing** coupling in force since January 2024 (BAG
identification codes required on every current address, point/reference
addresses banned outright, monthly Kwaliteitsmonitor compliance reporting)
— considerably stronger than the general description these three entities
previously carried.
**Remaining open items for this batch:**
- [[NL-KADASTER]]'s `participates-in` [[EU-EUROGEOGRAPHICS]] edge was not
  re-verified this pass — `eurogeographics.org` was not re-fetched, so the
  edge stands at its prior `confidence: medium` on the sourced-composition
  basis recorded earlier in this series (see the candidate-clearing batch
  above).
- [[NL-BAG]]'s NDFR consolidated-text source and [[NL-BGT]]'s
  Tweede Kamer document were not re-fetched — both entities already reach
  a majority without them.
- [[NL-BELASTINGDIENST]]'s specific list of WOZ-consuming taxes (income
  tax's owner-occupied-home allowance, corporate income tax, gift and
  inheritance tax, the landlord levy) is **not independently re-confirmed**
  this pass: `cbs.nl`'s own WOZ page, read directly, names municipalities
  and CBS as WOZ stakeholders but not the Belastingdienst or water boards
  specifically. Flagged in the entity's own text rather than silently
  repeated as newly verified.
- The "afnemer" (authorised-user) relationship gap already logged
  extensively elsewhere in `discovery/unresolved.md` for this cluster
  (BAG→BRP, RDW→BRP, Belastingdienst→WOZ) remains open — this pass did not
  attempt to resolve the underlying ontology question, only to re-verify
  the sourcing of what is currently modelled.
All 22 entities' `last_verified` set to 2026-08-27 regardless of outcome;
every "Sourcing caveat" banner and stale "NOT READ — search-only" evidence
string in this batch's files was rewritten to match its new frontmatter —
none left drifting from the promoted state.

## NL Batch 2 — Intelligence/security + interoperability cluster re-verification (2026-08-27)
Second of three parallel NL re-verification batches (22 entities: intelligence/
security services and their governing law, cybersecurity organisations and
legislation, standards/architecture organisations, and the enterprise/
reference-architecture framework family). All 22 were promoted from
`search-only`/`unverified` to **`verification: primary-source`**, each on a
genuine majority of directly-read sources, except [[NL-WBNI]] (kept at
`search-only` — see below).
**Two genuine factual corrections found and fixed:**
- [[NL-TNO-WET]] / [[NL-TNO]] — the entity previously described "the TNO-wet"
  as the act of 30 October 1930 (in force 1 May 1932). Reading
  `wetten.overheid.nl`'s own statute text directly (BWBR0003906) shows the
  **currently operative** TNO-wet is a wholly different, later act — the Wet
  van 19 december 1985 (Stb. 1985, 762), in force 1 May 1986 — which
  **replaced** the 1930 act. [[NL-TNO-WET]] now describes the 1985/1986 act
  (`start_date` corrected to `1986-05-01`); [[NL-TNO]]'s own `start_date`
  stays `1932-05-01` (the organisation's continuous founding), with the
  statutory recasting explained in prose on both entities. The 1930 act is
  not itself modelled.
- [[NL-CBW]] / [[NL-WBNI]] — the previous pass recorded `NL-CBW` as
  `status: planned`, written one day before its stated 15 August 2026
  entry-into-force date, unable to confirm the date would hold. It held:
  `ncsc.nl` and `nctv.nl`, both read directly and both dated after that
  date, confirm in their own words the Cbw **is** in force. `NL-CBW` is
  promoted to `status: active`; `NL-WBNI` is correspondingly moved from
  `status: active` to `status: superseded`. [[NL-NCSC]]'s relationship to
  `NL-CBW` is upgraded from `interpretation`/`confidence: low` to
  `fact`/`confidence: high`: `ncsc.nl`'s own Cbw page states directly that
  registered organisations connect to the NCSC "als jouw sectorale CSIRT" —
  the designation-gap flagged by the previous pass (and originally by the
  Belgium batch) is closed for the NCSC's own role, though the Cbw still
  distributes competent-authority roles sector-by-sector rather than
  concentrating them all in the NCSC.
**Two dead-link recoveries** (per the alternate-source-search discipline):
[[NL-EAR]]'s two `earonline.nl` sources now fail DNS resolution entirely
(not merely blocked); replaced with `roraonline.nl`'s own "Status en beheer
EAR" page and `noraonline.nl`'s own EAR wiki entry, both read directly and
between them giving a **more precise** founding date (10 June 2014, via
ICBR, replacing an earlier architecture called MARIJ) than the dead pages
ever cited. [[NL-BIO]]'s `bio-overheid.nl` (homepage and BIO2 PDF) returned
HTTP 403 on every attempt; `certificeringsadvies.nl`, found via WebSearch,
supplied equivalent BIO2 content (scope, ISO basis, September 2025
version-change date) and was read directly, reaching a genuine majority
(3 of 5 listed sources) alongside the two originally-cited pages that were
readable.
**[[NL-WBNI]] stays `search-only`, deliberately** — the one entity in this
batch not promoted. Both its cited sources (`ncsc.nl`, `nctv.nl`) were read
directly, a formal 2-of-2 majority, but both describe the Cbw/NIS2 side of
the supersession, not the Wbni's own text, commencement date, or its
relationship to the original NIS Directive. Reading them confirmed the
*supersession date* (useful for correcting `status` above) but not the
entity's *own* claims, so promotion was not taken on a technicality. A
`wetten.overheid.nl` BWBR citation for the Wbni itself was not located this
pass — worth a targeted search next time, following the same approach that
found BWBR0039896 (Wiv 2017) and BWBR0003906 (TNO-wet).
**One unconfirmed claim downgraded**: [[NL-NEN]]'s body text previously
stated NEN "was a co-founder of ISO in 1947" as fact. None of the three
sources read this pass (nen.nl, the NORA wiki, Dutch Wikipedia) states this,
and a targeted search found nothing beyond the uncontroversial founding
years of each organisation separately (NEN 1916, ISO 1947). Recorded in
prose as unconfirmed rather than repeated or silently deleted.
**Two composition-rule inferences upgraded to sourced fact** by finding the
composing body's own membership list, rather than relying on "N members,
therefore probably this one too": [[NL-SURF]]'s GÉANT membership (GÉANT's
own membership page names SURF explicitly, with named representatives) and
[[NL-NEN]]'s CEN participation (nen.nl's own page states outright "NEN is
lid van... CEN en ISO").
**wetten.overheid.nl is not blocked** — confirmed directly this pass on
three different statutes (Wiv 2017, TWCO's implementation decree citations,
TNO-wet). The Wiv 2017 entity's previous sourcing caveat asserting this
environment blocks that host is now corrected; its own official citation
page (BWBR0039896) has been added as this entity's primary source. Worth
flagging for the other two concurrent NL batches and for any entity
elsewhere in the Atlas still carrying that caveat unchallenged.
**Remaining open gaps carried forward, not resolved this pass**:
- [[NL-WBNI]]'s own statutory text and BWBR identifier (see above).
- [[NL-AIVD]]'s `irp.fas.org` source and [[NL-TIB]]'s Eerste Kamer keyword
  page were not re-fetched (majority already reached without them).
- The **1930 TNO-wet** (predecessor to the current 1985/1986 act) is not
  itself an Atlas entity; whether it warrants one for temporal completeness,
  matching the Atlas's WOB/WOO and Archiefwet 1995/2026 pattern, is an open
  modelling question.
- **VNG Realisatie** and **Edustandaard's Architecture Council** remain
  unmodelled, so [[NL-GEMMA]]'s and [[NL-ROSA]]'s `maintained-by` edges stay
  simplified/unasserted respectively — unchanged from the previous pass,
  now re-confirmed rather than newly discovered.
- [[NL-UAVG]]'s `autoriteitpersoonsgegevens.nl` source returned HTTP 403
  on every attempt (genuine block, not silently dropped); the official
  Staatsblad 2018, 144 text was read directly instead and is the stronger
  citation regardless.

## NL Batch 3 — Data/open-government/statistics cluster re-verification (2026-08-27)
Twenty-one entities re-verified: 4 organisations ([[NL-AP]], [[NL-CBS]],
[[NL-IPO]], [[NL-UVW]]), 5 legislation ([[NL-WDO]], [[NL-WHO]], [[NL-WOB]],
[[NL-WOO]], [[NL-WET-CBS]]), 2 platforms ([[NL-DATA-OVERHEID]], [[NL-NTM]]),
4 frameworks ([[NL-BASISREGISTRATIES]], [[NL-BOMOS]], [[NL-ISHARE]],
[[NL-PETRA]]), 3 standards ([[NL-ADR]], [[NL-DCAT-AP-NL]],
[[NL-DIGIKOPPELING]]) and 3 strategies ([[NL-DATA-AGENDA-OVERHEID]],
[[NL-DIGIBETER]], [[NL-NDS]]).
**20 of 21 promoted to `verification: primary-source`.** Only
[[NL-BASISREGISTRATIES]] stayed at `search-only` — exactly 3 of 6 cited
pages were read directly (the other three, all on `digitaleoverheid.nl`,
returned a genuine JavaScript bot-verification challenge on every attempt,
confirmed by retrying and by a PDF alternate that returned unparseable
binary); half is not a majority, so it was not promoted despite the effort.
**A domain-wide finding**: `digitaleoverheid.nl` (Ministerie van BZK) is
**genuinely and repeatedly bot-walled** to WebFetch across this entire
batch — every single fetch attempt against it, across roughly ten distinct
URLs and two dozen attempts, returned the same "One moment, please...
Please wait while your request is being verified..." challenge page, never
real content. This affected [[NL-WDO]], [[NL-IPO]], [[NL-UVW]],
[[NL-BASISREGISTRATIES]], [[NL-DIGIBETER]] and [[NL-NDS]]'s originally-cited
sources. Two exceptions worth flagging for whoever next touches this
domain: `digitaleoverheid.nl/nederlandse-digitaliseringsstrategie-nds/`,
`digitaleoverheid.nl/nieuws-nds/nieuwe-kabinet-duidelijk-de-nds-gaat-door/`
and `digitaleoverheid.nl/overzicht-van-alle-onderwerpen/kabinetsbeleid-digitalisering/`
**did** load successfully — so the block is not domain-wide in the literal
sense, just extremely frequent on this domain's older/deeper URL paths.
Where blocked, this pass followed the brief's instruction to search for
alternate primary sources rather than stall — `wetten.overheid.nl` (the
Wdo's own statutory text), `noraonline.nl`, `ibestuur.nl`, Wikipedia,
`geobasisregistraties.nl` and `hetwaterschapshuis.nl` all substituted
successfully in different entities.
**`parlementairemonitor.nl` is confirmed to have ceased operations
in 2024.** Every URL on that domain cited by [[NL-DATA-AGENDA-OVERHEID]] and
[[NL-DIGIBETER]] now either redirects to a generic "about the monitor"
page or serves one — never the indexed parliamentary document. One redirect
(`vkwwhns8u3zz` → `kst-26643-597.html`) led to a genuinely useful
`officielebekendmakingen.nl` replacement; the other three citations on this
domain across both entities are now dead ends with no automatic redirect
target, and were replaced with independently-found Kamerstuk/news
alternates. **Anyone else in the Atlas citing `parlementairemonitor.nl`
should assume the same and re-source, not just re-fetch.**
**Genuine corrections made, not just confirmations:**
- [[NL-WHO]]'s previously-unresolved entry-into-force date (19 June 2024 vs.
  2 August 2024) is resolved — both figures were real, but described
  different things (commencement date vs. a later news announcement date).
  `start_date` is now `2024-06-19`.
- [[NL-ISHARE]]'s `references` [[INTL-IDS-RAM]] relationship overstated a
  2022 IDSA/iSHARE **collaboration** ("complete each other," each retaining
  distinct roles) as IDSA **incorporating** iSHARE. Corrected to
  `aligned-with`, evidence rewritten from IDSA's own article.
- [[NL-PETRA]]'s acronym is now confirmed likely wrong: the entity's own
  title uses "Provinciale **Enterprise** Referentie Architectuur," but its
  one source (read directly this pass) expands PETRA only as "Provinciale
  Referentie Architectuur" — no "Enterprise" anywhere. Not renamed (outside
  this pass's scope; the fuller name might be sourced elsewhere and simply
  didn't surface), but flagged here for whoever next touches this entity.
- [[NL-DIGIBETER]]'s `status: unknown` is resolved to `superseded`:
  `digitaleoverheid.nl`'s own current policy-overview page (read directly)
  frames "NL Digibeter (2018-2020)" in the past tense, followed by a
  previously-unknown **"Werkagenda Waardengedreven Digitaliseren
  (2022-2024)"** — not yet an Atlas entity — and then [[NL-NDS]] (2025),
  which the same page states explicitly "does not replace but connects
  existing plans." `successor` is left `null` on [[NL-DIGIBETER]] rather
  than pointed at [[NL-NDS]], since the actual intervening strategy isn't
  modelled yet. **New research-queue item**: create a
  `NL-WERKAGENDA-WAARDEGEDREVEN-DIGITALISEREN` (or similar) entity to fill
  this gap and let a real `supersedes` chain be built.
- [[NL-NDS]]'s continuation under the post-2025 cabinet — genuinely
  uncertain in the prior text — is now confirmed: a March 2026 article
  (`digitaleoverheid.nl/nieuws-nds/...`, found via search, read directly)
  states "The programme continues and retains the same name," now
  co-led by **EZK** (not previously in this Atlas as an organisation
  entity — queued) alongside [[NL-BZK]].
- [[NL-CBS]] / [[NL-WET-CBS]]'s enactment date is confirmed as **20 November
  2003** (title of the act itself, corroborated by search against
  Staatsblad 2003, 516) — one of eerstekamer.nl's own summarised dates
  suggested 18 December 2003, which on inspection is more likely an Eerste
  Kamer procedural date than the act's own dating; the act's own title is
  treated as authoritative.
- [[NL-NTM]]'s EU legal basis was previously **explicitly left unnamed**
  ("no source located... named the instrument"). This pass names it:
  Directive 2010/40/EU (the ITS Directive), confirmed by reading the
  European Commission's own National Access Points page directly, plus
  NTM's own current site at `toegangspuntmobiliteit.nl` (an apparent
  rebrand of the `ntm.ndw.nu` domain, which returned only a bare page title
  on fetch this pass — effectively dead for content purposes without being
  a hard 404).
**Still open after this pass:**
- [[NL-BASISREGISTRATIES]]'s remaining three digitaleoverheid.nl sources —
  next attempt should try archive.org/Wayback Machine snapshots, not
  repeat the same live fetch.
- [[NL-DATA-OVERHEID]]'s operator is narrowed (Logius / KOOP, both under
  BZK) but not conclusively named by any page read directly.
- [[NL-DATA-AGENDA-OVERHEID]] ↔ [[NL-IBDS]] relationship: still no source
  states whether the IBDS extends or replaces this agenda.
- The "Werkagenda Waardengedreven Digitaliseren (2022-2024)" gap above.
- [[NL-DIGIKOPPELING]]'s comply-or-explain-list membership lost its sole
  supporting citation (`vngrealisatie.nl`, now HTTP 404) and needs a
  replacement source, not just re-confirmation.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see the batch's own completion report for results.
