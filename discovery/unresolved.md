# Unresolved

Open questions the Atlas cannot currently answer with confidence: a fact
that couldn't be verified, a relationship that seems plausible but isn't
directly sourced, a status that couldn't be confirmed. Never guess to close
one of these — resolve it with a real source, or leave it open.

## Cross-cutting

| Entity / topic | Question | Why it's unresolved | Noted by / date | Status |
|---|---|---|---|---|
| All unread-source entities (**200 of 206**: 197 `search-only` + 3 `unverified` ([[NL]], [[EU]], [[UN]]); regenerate the count with `python tools/source_hosts.py`) | Every factual claim | The environment's network egress policy blocks all direct page retrieval (`EGRESS_BLOCKED` for forumstandaardisatie.nl, digitaleoverheid.nl, noraonline.nl, vng.nl, logius.nl, eur-lex.europa.eu, wikipedia.org and every other host tested). Batch 1 was completed from search-engine results on explicit instruction, with the trade-off accepted knowingly. Every entity carries `verification: search-only`. | Batch 1 / 2026-08-14 | **Open — needs full re-verification pass** |

To find every affected entity: `grep -rl "verification: search-only" .`

**The worklist for closing this is generated:**
`discovery/reverification-allowlist.md` lists every host the Atlas cites,
derived from the entity files by `tools/source_hosts.py`. Page retrieval is
blocked by an **environment-level egress policy** — the proxy answers
`403 to CONNECT` — which no change inside a session can lift. The allowlist
is what to request.

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

## Batches 6, 11, 15 — validation findings

| Entity / topic | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| **The UN layer is unconnected** | Nothing links the 9 UN entities to any EU or NL entity | The brief's target architecture is UN → EU → National → Sector. What exists is a connected EU↔NL graph plus a **separate, unattached UN component**. The single most significant structural gap in the Atlas. | Batch 15 / 2026-08-14 | ✅ **Resolved — UN-connection batch, 2026-08-16.** `EU → UN` is now 4 and `UN → national` is 5. The diagnosis in `discovery/candidates.md` held: in every cluster the refused edge pointed at a node that did not exist. Creating [[EU-ESS]], [[UN-UNSC]], [[UN-UNECE]] and [[UN-CES]] made the statistics edges statable, and [[UN-AARHUS]] → [[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]] gave the first complete UN → EU → national chain. **No sourcing standard was lowered and no relationship type was added.** |
| [[UN-UNSD]] → [[EU-EUROSTAT]] | Is the European Statistical System part of the global statistical system? | Would close most of the UN-layer gap on its own. Plainly true in substance; **no source read says it**. | Batch 13; confirmed Batch 15 | ✅ **Resolved differently — UN batch, 2026-08-16.** The edge as posed was never correct: UNSD is a secretariat and Eurostat does not relate to it directly. Eurostat `participates-in` [[UN-UNSC]] and [[UN-CES]] — forums, sourced to Eurostat's own cooperation page — and [[UN-UNSD]] is `governed-by` the Commission. **Three refusals of this row were right.** |
| [[UN-FPOS]] → [[NL-WET-CBS]] | Does Dutch statistical legislation align with the Fundamental Principles? | Countries are tracked on exactly this. Would give a UN → national chain. | Batch 12; confirmed Batch 15 | Open |
| [[NL]], [[EU]], [[UN]] anchors | Do their cited URLs exist? | **Written in Batch 0 from background knowledge, never confirmed by search or fetch** — the brief says never invent URLs. Now marked `verification: unverified`, worse than the `search-only` majority. Self-inflicted, caught by the Batch 6 audit. | Batch 6 / 2026-08-14 | **Open — priority** |
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
| [[DE-BFDI]] → [[EU-EDPB]] | [[NL-AP]] carries exactly this link. German representation on the EDPB (federal vs Land authorities) is precisely the detail that must not be guessed | A free DE→EU edge | Open |
| [[DE-BUNDID]] → [[EU-EIDAS2]] / [[EU-EUDI-WALLET]] | eIDAS2 requires wallets by end-2026 and BundID is the obvious German starting point; no source connects them | Will matter within months | Open |
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
| [[DE-BDSG]] | **All four sources are commercial legal publishers.** No Gesetze-im-Internet or BGBl citation, for the entity carrying the most structural weight in the batch | **Open — priority** |
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
| [[BE-HERGEBRUIK-WET]] → [[EU-OPEN-DATA-DIRECTIVE]] | **Chronologically impossible**: the act is 2016, the directive 2019/1024. Sources say it aligns with the earlier PSI Directive, which is not an Atlas entity. **Belgium's actual Open Data Directive transposition was not identified.** The sharpest pattern-matching trap in the batch — the shape of the Atlas made a wrong answer attractive. | **Open — priority** |
| [[BE-NIS1-WET]] → [[EU-NIS]] | Near-certain, and [[EU-NIS]] *is* an Atlas entity so the link has somewhere to point — but every source cited is about the successor act and none states what the 2019 act transposed. Would give a second `EU-NIS` → national descent. | **Open — one page read** |
| [[BE-APD]] → [[EU-EDPB]] | No source read mentions the EDPB. Three national DPAs now sit in the Atlas and **only [[NL-AP]] connects to the Board** — a sourcing artefact, not a fact about European data protection governance. | Open |
| [[BE-STATBEL]] → [[EU-EUROSTAT]] / [[UN-FPOS]] | Nothing found. ⚠ **The claim that "none connects upward" was wrong when written and was repeated for three batches** — [[NL-CBS]] already carried a `participates-in` edge to Eurostat, with ESS-membership reasoning in its evidence. Corrected in the UN batch. | ✅ **Partly resolved — UN batch, 2026-08-16.** Statbel is now `part-of` [[EU-ESS]]. The [[UN-FPOS]] half is still open. |
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
| [[BE-NIS2-WET]] | No Belgisch Staatsblad ELI URI cited; publication and entry-into-force dates rest on CCB reporting. | Open |
| [[BE-KSZ-WET]] | Only two sources, one of them the KSZ's page about its own founding act. Act content unknown. | Open |
| [[BE-STATBEL]] | **No statutory basis found** — no Belgian equivalent of [[DE-BSTATG]] or [[NL-WET-CBS]], so no `governed-by` is recorded. | Open |
| [[BE-HERGEBRUIK-WET]] | Scope, obligations and relationship to the current EU regime all unknown. | Open |

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
| [[FR-CNIL]] → [[EU-EDPB]] | No source read mentions the EDPB. **Four national DPAs now sit in the Atlas and only [[NL-AP]] connects to the Board** — the clearest single example in the Atlas of a sourcing artefact masquerading as structure. Four pages would close it. | **Open — cheap, high value** |
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
| [[ES-CLAVE]] → [[EU-EIDAS]] / [[EU-EIDAS2]] | Nothing read mentions eIDAS or cross-border recognition. **The eIDAS2 wallet deadline is now roughly four months away and no country in the Atlas is linked to it.** [[FR-FRANCECONNECT]] predicted this would become a factual question; it now is one. | **Open — time-critical** |
| [[ES-AEPD]] → [[EU-EDPB]] | No source read mentions the Board. **Five national DPAs, one sourced link.** Five page reads would fix four edges. | **Open — cheap, high value** |
| [[ES-ESPANA-DIGITAL-2026]] → [[EU-DIGITAL-DECADE]] | Nothing read connects them, though the strategy is aligned with the Recovery Plan. Same refusal as [[NL-DIGIBETER]] and [[DE-DIGITALSTRATEGIE]] — three national strategies, three refusals. | Open |
| [[ES-INCIBE]] / [[ES-CCN]] → [[ES-LCGC]] | Reporting describes an institutional dispute over a draft allocation of competences. **A dispute is not a relationship**, and the law is not in force. | Open (deliberate) |
| [[ES-ENI]] ↔ [[ES-ENS]] | Consistently presented together in Spanish practice; no source read establishes a relationship between the instruments. | Open |
| [[ES-DATOS-GOB-ES]] → Red.es | Red.es operates the portal but is not an entity — a single mention of its promoting role is too thin. **This portal therefore has no `maintained-by` edge**, unlike [[NL-DATA-OVERHEID]] and [[DE-GOVDATA]]. | Open |

### The one asserted link that needs scrutiny

| Link | Concern | Status |
|---|---|---|
| [[ES-INE]] → [[EU-EUROSTAT]] | The sources describe a **three-party structure** — the European Statistical System comprises Eurostat *and* the member states' statistical offices — not a bilateral relationship. The Atlas records `related-to` at `source: interpretation`, `confidence: low`, and states the gap in the `evidence` string. **The correct fix is an `EU-ESS` entity** with `part-of` edges from Eurostat and from all national offices; it was deliberately not created inside a country batch. That single entity would connect four national statistical offices at once. | **Open — modelling, high value** |

### Factual gaps — Spain

| Entity | Question | Status |
|---|---|---|
| [[ES-AESIA]] | **No BOE citation for Real Decreto 729/2023**, the decree that creates it — no search result returned the BOE identifier. First thing to fetch for this entity. | Open |
| [[ES-NTI-RISP]] | The DCAT-AP-ES model is described as **in administrative processing**, so the `based-on` descent from [[EU-DCAT-AP]] may not yet be in force. Recorded at `confidence: low` with `valid_from: null`. | Open |
| [[ES-LCGC]] | No BOE citation exists to give — the instrument is a draft. Its passage would also make the Centro Nacional de Ciberseguridad modellable. | Open |
| [[ES-ENI]] | Legal base not modelled: sources say it was established by article 42 of Ley 11/2007, an act since replaced by the 2015 administrative-procedure legislation. The chain from the current base was not established, and the repealed act was not asserted as its parent. | Open |
| [[ES-LOPDGDD]] | **The `Ley Orgánica` rank is not modelled.** Spain's constitutional hierarchy distinguishes organic from ordinary laws, and only the organic rank lets its Title X bind. `type: law` flattens it — as it already flattens *Gesetz*/*Verordnung*, *wet*/*koninklijk besluit* and *loi*/*ordonnance*. No field was added: five countries have been modelled without one, and adding it would require re-reading every instrument in the Atlas. | Open (ontology question) |
| [[ES-LOPDGDD]] | **Partial implementation is not expressible.** Title X on digital rights does not descend from any EU instrument; the single `implements-requirement-from` edge is whole-entity to whole-entity and silent about it. No partial-implementation type proposed on one example. | Open (modelling) |
| [[ES-AEAD]] | `supersedes` records the succession but cannot say it was a **transformation** — same functions and remit under a new legal form — rather than an abolition and replacement. Not worth a new relationship type on one example. | Open (modelling) |
| [[ES-CLAVE]] | Operator, legal basis, the relationship between Cl@ve PIN and Cl@ve Permanente, and the status of any Spanish digital identity wallet are all unrecorded. | Open |
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
