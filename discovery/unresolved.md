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
| [[NL-BASISREGISTRATIES]] | Who owns/governs the stelsel, and how does it relate to [[NL-FDS]]? | Both address reuse and sharing of authoritative public-sector data. Whether FDS extends, replaces or sits beside the basisregistraties stelsel is unestablished, and matters for the coherence of the Dutch data-governance model. | Batch 2 / 2026-08-14 | Open |
| [[NL-WDO]] | Does the Wdo transpose obligations from eIDAS or another EU instrument? | `region` is currently `null` (treated as purely national), but its subject matter overlaps EU digital identity law. Re-examine when eIDAS is added in Batch 8. | Batch 3 / 2026-08-14 | Open |
| [[NL-DATA-AGENDA-OVERHEID]] | Relationship to [[NL-IBDS]] | **Narrowed 2026-08-27**: the publication date (March 2019, exact day disputed by five days across two directly-read sources) and the successor chain are now resolved. The two cover overlapping ground; no relationship is asserted between them because none has been sourced; guessing would violate the provenance rules. | Batch 1 / 2026-08-14 | Open |

## Batch 4 — standards and architecture

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-PETRA]] | Almost everything: maintainer, relationship to NORA, even the acronym's expansion | **Weakest entity in the Atlas.** Rests on a single sentence in one Wikipedia article. Included because Batch 4's scope names PETRA explicitly. The `organisations: [NL-IPO]` association is an Atlas assumption, not sourced. | Batch 4 / 2026-08-14 | Open |
| [[NL-NEN-3610]] | Is Geonovum the maintainer, or only the point of contact for application? | **Narrowed 2026-08-27**: `confidence` raised from `low` to `medium`, but the split stands — Geonovum's own words describe it as *aanspreekpunt* (point of contact), weaker than `maintained-by`, while NEN's own publisher role was not itself confirmed by any page read. Custody remains genuinely split between the two. | Batch 4 / 2026-08-14 | Open |

## Batch 5 — domains and data ecosystems

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-HEALTH-RI]] | Should Health-RI be split into an organisation and an infrastructure? | The name denotes both, and sources use it for both. Modelled as one `data-space` because the infrastructure has no proper name of its own. | Batch 5 / 2026-08-14 | Open (modelling) |
| [[NL-NDW]] | Is NDW a platform or an organisation? | Typed `platform` for its primary function, but it is a partnership of 19 governments with its own entry in the government organisation register. | Batch 5 / 2026-08-14 | Open (modelling) |
| [[NL-PDOK]] | Precise establishment date in 2013 | `start_date: 2013-01-01` is a placeholder for "in 2013". Same pattern as [[NL-ISHARE]]; [[NL-RORA]] resolved its own instance of this problem on 2026-08-27 by moving to `start_date: null` per the convention question below. | Batch 5 / 2026-08-14 | Open |
| Placeholder `start_date` convention | Should "year known, date unknown" be recorded as `YYYY-01-01` or left null? | Used on three entities ([[NL-PDOK]], [[NL-ISHARE]], and partially [[NL-DSGO]]). A January-1st placeholder is indistinguishable from a real 1 January date, which is a genuine data-quality problem. **[[NL-RORA]] answered this in practice (2026-08-27): `null` rather than a padded date, with the reasoning documented on the entity** — but no schema-wide convention or `date_precision` field has been added, so the other entities still carry the ambiguous placeholder. | Batch 5 / 2026-08-14 | **Open (schema question)** |

## Batch 7 — EU core initiatives

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[NL-WDO]] | *(updated)* Does the Wdo transpose eIDAS? | **Batch 7 update:** [[EU-EIDAS2]] is probably a red herring — the Wdo came into force July 2023, before eIDAS 2.0 entered into force in May 2024. If the Wdo transposes anything it is more likely the original eIDAS Regulation (910/2014), which is not yet an entity. | Batch 3; updated Batch 7 | Open (narrowed) |
| [[EU-DIGITAL-DECADE]] | Should Decision (EU) 2022/2481 be a separate `legislation/` entity? | The Atlas models the programme, not the establishing Decision. | Batch 7 / 2026-08-14 | Open (modelling) |
| "Digital sovereignty" | Is there a distinct EU digital-sovereignty initiative warranting an entity? | Named in Batch 7's scope, but sources treat it as a framing within [[EU-DIGITAL-DECADE]] rather than a named initiative with its own governance. **No entity created.** | Batch 7 / 2026-08-14 | Open (scope) |
| EU AI strategy | Is there a distinct EU AI *strategy* entity, separate from the AI Act? | Named in Batch 7's scope. Searches returned mostly AI-and-cybersecurity material, not a clearly identifiable standalone strategy document. **No entity created** rather than inventing one. | Batch 7 / 2026-08-14 | Open (scope) |

## Batch 8 — EU legislation

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-EIF]] / [[EU-INTEROPERABLE-EUROPE-ACT]] | How do the Act and the Framework relate? | **Closed 2026-09-05**: Regulation (EU) 2024/903's own Official Journal text, read directly, Article 6(1): "The Board shall develop a European Interoperability Framework (EIF). It shall submit the EIF to the Commission for adoption." The Act establishes the legal mechanism by which the EIF is created and revised. [[EU-EIF]] now carries `governed-by` the Act. One root, not two | Batch 8 / 2026-08-14 | Closed |
| [[EU-EIDAS]] | The regulation's own content and dates | Created in Batch 8 purely so the [[NL-WDO]] question is expressible. Its only source is the amending regulation. | Batch 8 / 2026-08-14 | Open |
| [[NL-WDO]] | *(updated)* Does the Wdo transpose eIDAS 910/2014? | **Batch 8 update:** eIDAS 2.0 ruled out on dates (Wdo July 2023 precedes it). Original eIDAS is the plausible candidate but nothing sources the transposition. `region` stays `null`. | Batch 3; updated Batch 7, 8 | Open (narrowed) |
| [[EU-SDG]] | The once-only principle mechanism, and the Dutch implementation | Relevance was assessed on the once-only principle, but that mechanism was not researched, and no Dutch counterpart is modelled. | Batch 8 / 2026-08-14 | Open |

## Batches 9–10 — EU organisations, standards and data spaces

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-EHDS]] → [[NL-HEALTH-RI]] | Will Health-RI be the Dutch health data access body? | The EHDS requires member states to designate HDABs during 2027–2029. Health-RI is the obvious candidate but nothing sources it, and the designation phase had not begun. Confirming it completes an EU-regulation → national-infrastructure chain. | Batch 10 / 2026-08-14 | **Open — high value** |
| [[EU-EMDS]] → [[NL-NTM]] | Does the mobility data space build on the national access point network? | **Narrowed 2026-09-05**: the EU-level half is now sourced — transport.ec.europa.eu's own page states the EMDS "will take account of" the ITS Directive's National Access Points mechanism, recorded as `references` → [[EU-ITS-DIRECTIVE]]. No source names [[NL-NTM]] or any specific national NAP, so the country-level link stays an association only. | Batch 10 / 2026-08-14 | Open |
| [[EU-DSSC-BLUEPRINT]] ↔ Dutch afsprakenstelsels | Do [[NL-FDS]], [[NL-DSGO]], [[NL-ISHARE]] and [[NL-HEALTH-RI]] map onto the Blueprint's rulebook model? | The resemblance is striking and entirely unsourced. Confirming it would connect the Dutch and EU data-space layers structurally rather than thematically. | Batch 10 / 2026-08-14 | **Open — structural** |
| [[EU-EHDS]] | Should the regulation be split from the data space? | Modelled as one entity, matching [[NL-BIO]] and [[NL-HEALTH-RI]]. Reg. (EU) 2025/327 is substantial legislation and may warrant its own entity. No EUR-Lex citation was located either. | Batch 10 / 2026-08-14 | Open (modelling) |
| [[EU-SEMIC]], [[EU-DSSC]] | Are these organisations, programmes, or something else? | SEMIC is described as an "action"; DSSC's legal form is unclear. `organisation` is the best available fit for both, with reservations. | Batches 9–10 | Open (modelling) |
| [[EU-PARLIAMENT]] / [[EU-COUNCIL]] | Should legislative adoption be modelled? | Currently **not** — it would add 32 edges conveying one fact already implied by entity type. If wanted, do it systematically with a dedicated relationship type. | Batch 9 / 2026-08-14 | Open (modelling) |
| Directorates-General | Which DGs are relevant, and should they be entities? | DG CONNECT is named once as a DCAT-AP co-initiator. No DG research was done; none created. | Batch 9 / 2026-08-14 | Open |

## Batches 6, 11, 15 — validation findings

| Entity / topic | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| 40 entities with no provenanced relationship | Are these legitimately terminal or under-linked? | Many are terminal by nature (legislation nothing implements). Worth reviewing when sources are available. Was 35 before the Germany batch; 10 of the 37 German entities are in this category. | Batch 15; recounted 2026-08-15 | Open |

## Batches 12–14 — UN and international

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[INTL-IETF]] | Everything beyond its category | Single indirect source (an academic toolkit listing eight SDOs); no ietf.org citation, no IETF standard modelled. Yet IETF RFCs underpin the HTTPS/DNSSEC/mail standards on [[NL-PAS-TOE-OF-LEG-UIT]]. | Batch 13 / 2026-08-14 | **Narrowed 2026-08-28** — the sourcing half is closed: three ietf.org/datatracker.ietf.org pages, read directly, confirm the IETF-ISOC relationship in the primary documents' own words. Still open: no IETF RFC is modelled as a standard, so the real connection to [[NL-PAS-TOE-OF-LEG-UIT]]'s HTTPS/DNSSEC/mail requirements stays queued rather than asserted. |
| [[INTL-ISO-IEC-27002]] | Cited URL points at **edition 2 (2013)**, a superseded edition | The current edition is 27002:2022, which is what BIO2 references. The ISO OBP link located resolves to the older edition and older title. | Batch 14 / 2026-08-14 | **Narrowed 2026-09-05** — the correct edition-3 standard number (`iso.org/standard/75652.html`, March 2022) is now known and added to `sources`, corroborated by reading en.wikipedia.org's own article directly. iso.org itself is confirmed domain-wide blocked to this environment's fetch tooling, so nobody has read the edition-3 page's own content; the original edition-2 citation stays rather than being replaced. |
| [[NL-BIO]] → ISO editions | Is NEN-EN-ISO/IEC 27001:**2023** the same standard as ISO/IEC 27001:**2022**? | BIO2 cites the NEN-EN adoption years; the ISO editions differ by one year. Almost certainly the Dutch/European adoption of the same standard, but the equivalence is **inferred, not sourced**. | Batch 14 / 2026-08-14 | Open |
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
| [[DE-MDS]] → [[EU-EMDS]] | Same refusal Batch 10 made for [[EU-EMDS]] → [[NL-NTM]]. **Two national mobility data spaces now sit unconnected to their apparent European parent** | Closes both at once | Open |
| [[DE-REGMOG]] → [[EU-SDG]] | Once-only is the SDG Regulation's organising idea and RegMoG is Germany's once-only vehicle, but RegMoG is domestic register law and no source connects them | — | Open |
| [[EU-GAIA-X]] → [[EU-COMMON-DATA-SPACES]] / [[EU-DSSC-BLUEPRINT]] | Plainly part of the same European effort; the Commission source cited is *about* Gaia-X, not a statement of relationship | — | Open |

### Factual gaps

| Entity | Question | Status |
|---|---|---|
| [[DE-DATENSTRATEGIE]] | Is it still in force after the creation of [[DE-BMDS]] and the [[DE-MODERNISIERUNGSAGENDA-BUND]]? | **Narrowed 2026-09-04**: the adoption-date half is closed — Bundestag Drucksache 20/8260, read directly, gives a documented chain (BMDV letter 29 August 2023; Drucksache itself 1 September 2023; first Bundestag debate 28 September 2023), explaining why secondary sources disagreed. `start_date` is now set to 2023-09-01. The still-in-force question remains genuinely open: no source read states whether the 2023 strategy remains in force, has been absorbed into the newer agenda, or has been superseded | Open |
| [[DE-DIGITALSTRATEGIE]] | `status: unknown`. Its 2025 horizon has passed; sources suggest targets were missed; **no source states it was completed, superseded or extended** | Open |
| [[DE-OZG]] | The act's **own enactment date was never established** — every source concerns the 2024 amendment or the programme. Widely known to be 2017, which is exactly why it is not recorded | Open |
| [[DE-IWG]] | Nothing established beyond its replacement by [[DE-DNG]]. All three sources are about the DNG. Which PSI directive it transposed is unknown | Open |
| [[DE-BMI]] | Its `produces` relationships are historical: [[DE-BMDS]] took digital competences from six departments in May 2025 | **Narrowed 2026-09-05**: the name question is closed — de.wikipedia.org, read directly, confirms Chancellor Merz ordered the renaming back to *Bundesministerium des Innern* by decree on 6 May 2025, the same date as the DE-BMDS/DE-BMV split. The historical-relationships question stands | Open |
| [[DE-MODERNISIERUNGSAGENDA-FOEDERAL]] | The **five fields of action are not recorded** — no source read names them | Open |
| [[DE-IT-ARCHITEKTURRICHTLINIEN]] | The **content** of the guidelines is unknown; only existence, custody, governance and version 1.9.0 are recorded | Open |
| [[DE-DCAT-AP-DE]] | The 28 June 2018 IT-Planungsrat resolution rests on a single secondary statement; no decision document cited | Open |
| [[DE-CATENA-X]] | No catena-x.net source; described entirely through Fraunhofer institutes and trade press | Open |
| [[NL-CBW]] | `start_date: 2026-08-15` — **today**. The entity's own body asks a reader after that date to verify and, if confirmed, move it to `active` and [[NL-WBNI]] to `superseded`. Not done: it cannot be verified without page retrieval | **Open — actionable the moment egress is available** |

## Belgium batch — third country (2026-08-15)

### The federal modelling gap is general, and Belgium sharpens it

| Topic | Question | Why it matters | Status |
|---|---|---|---|
| **No sub-national level — confirmed general** | Germany found no term fits a Land. Belgium finds the term that *would* fit is **already taken**: `level: regional` means supra-national in this Atlas ([[EU]] carries it). | The cost was concrete and large: **OSLO**, Digitaal Vlaanderen, the Agence du Numérique and Paradigm were unmodelled. Two federal states, two different failure modes, same root cause. | **Resolved 2026-08-21** — `level: subnational` was added to the schema, a genuine ontology change rather than a Belgium-specific workaround. [[BE-OSLO]], [[BE-DIGITAAL-VLAANDEREN]], [[BE-AGENCE-NUMERIQUE]] and [[BE-PARADIGM]] were modelled under it (research-queue pickup, 2026-09-04). Still open: no Community-level (as opposed to Region-level) digital-policy body has been researched |
| Multilingual names | Belgium has three official languages; `name` uses the Dutch form where the sources found were Dutch, French in `alternative_names`. | A sourcing artefact presented as a naming decision. `FOD BOSA`/`SPF BOSA` and `KSZ`/`BCSS` are equally official. The Atlas has no multilingual name field and did not gain one. | Open (ontology) |
| `level: sectoral` for nationally-constituted bodies | [[BE-KSZ]] joins [[NL-NICTIZ]] and [[NL-ROSA]] in being recorded `sectoral` — a national body whose authority is bounded to one sector. | The convention is now used four times across three countries on precedent alone. It should be written into `metadata/taxonomy.md` or abandoned. | Open (ontology) |

### Refused links — Belgium

| Link | Why refused | Status |
|---|---|---|
| [[BE-STATBEL]] → [[EU-EUROSTAT]] / [[UN-FPOS]] | Nothing found. ⚠ **The claim that "none connects upward" was wrong when written and was repeated for three batches** — [[NL-CBS]] already carried a `participates-in` edge to Eurostat, with ESS-membership reasoning in its evidence. Corrected in the UN batch. | ✅ **Partly resolved — UN batch, 2026-08-16.** Statbel is now `part-of` [[EU-ESS]]. ⚠ **The re-verification pass of 2026-08-26 found the same wrong claim still standing in [[BE-STATBEL]]'s own body prose**, ten days after the frontmatter was corrected — a second instance of the frontmatter/body drift bug also found on [[BE-APD]]. Corrected this pass; Wikipedia additionally corroborates with "Statbel serves as Belgium's official representative to Eurostat." The [[UN-FPOS]] half is still open. |
| [[BE-KSZ]] → [[EU-SDG]] | The KSZ predates the regulation by 28 years and no source connects them — the same refusal made for [[DE-REGMOG]]. | Open |
| [[BE-BOSA]] → [[BE-BELGIF]] | BELGIF is sourced as co-owned by the federal state, Regions and Communities — precisely not something BOSA owns. | Open (deliberate) |

### Factual gaps — Belgium

| Entity | Question | Status |
|---|---|---|
| [[BE-NIS2-WET]] | No Belgisch Staatsblad ELI URI cited; publication and entry-into-force dates rest on CCB reporting. | **Closed 2026-09-05**: `ejustice.just.fgov.be/eli/wet/2024/04/26/2024202344/justel`, read directly, confirms the act's own title, 17 May 2024 publication and official number 2024202344, matching the four secondary sources already cited. CCB's own three pages remain bot-walled, but the ELI URI gap is closed. |
| [[BE-KSZ-WET]] | Only two sources, one of them the KSZ's page about its own founding act. Act content unknown. | Partly resolved — re-verification pass, 2026-08-26. The KSZ's own page, read directly, quotes Article 1 verbatim. Remaining act content (governance, funding) still unknown; still only two sources. |
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
| [[FR-FRANCECONNECT]] → [[EU-EIDAS]] / [[EU-EIDAS2]] | Nothing read mentions eIDAS or cross-border recognition, even though a national identity federation is precisely what eIDAS governs. The eIDAS2 wallet deadline (end 2026) is now four months away and **no country in the Atlas is linked to it**. | **Open — becoming time-critical** |
| [[FR-NIS2-LOI]] → [[EU-CER]] | The vehicle is sourced as transposing REC, NIS2 and DORA together, but the instrument's own status is unresolved; the relationship would inherit that. | Open (deliberate) |
| [[FR-DATA-GOUV]] → [[FR-LRN]] | Portal and open-data act, obviously related, nowhere stated. Same call as the German and Belgian equivalents — now made four times. | Open |

### Factual gaps — France

| Entity | Question | Status |
|---|---|---|
| [[FR-NIS2-LOI]] | **Sources directly contradict each other**: one says transposition is by Law n° 2025-90 of 26 February 2025; another says the bill was adopted by the Senate on 12 March 2025 and awaits promulgation, expected mid-2026. | **Closed 2026-09-05** — resolved 2026-08-26 but this row was never removed: three independent sources including ANSSI's own page contradict the single uncorroborated aventris.fr claim, which is not recorded as fact. `status: planned`. **Re-checked 2026-09-05** against the Assemblée nationale's own dossier législatif page, read directly, which confirms the same status and adds the entity's first official-record citation. |
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

### Refused links — Spain

| Link | Why refused | Status |
|---|---|---|
| [[ES-ENI]] → [[EU-EIF]] | Nothing read mentions the EIF or the NIF concept. **Refused for the third time** (Germany, France, now Spain), and for the same reason each time: the pattern makes it look expected, which is not evidence. [[EU-EIF]] now has five countries and one national-framework link. | Open |
| [[ES-CLAVE]] → [[EU-EIDAS]] / [[EU-EIDAS2]] | An `implements-requirement-from` edge exists at `confidence: low`, but its two now-read specific sources (eidas.redsara.es, viafirma.com) confirm the general Spanish eIDAS node and that DNIe (not Cl@ve) is the notified scheme — neither states that administrations integrate via Cl@ve. **The eIDAS2 wallet deadline is now roughly four months away and no country in the Atlas is linked to it.** [[FR-FRANCECONNECT]] predicted this would become a factual question; it now is one. | **Open — time-critical, re-checked 2026-08-27** |
| [[ES-ESPANA-DIGITAL-2026]] → [[EU-DIGITAL-DECADE]] | Nothing read connects them, though the strategy is aligned with the Recovery Plan. Same refusal as [[NL-DIGIBETER]] and [[DE-DIGITALSTRATEGIE]] — three national strategies, three refusals. | Open |
| [[ES-ESPANA-DIGITAL-2026]] — which two axes? | **Genuine source conflict, found 2026-08-27.** Widely-syndicated coverage (and this entity's own prior description) names the two new cross-cutting axes as public-private collaboration and co-governance with the Autonomous Communities. But the government's own current pages (espanadigital.gob.es, mineco.gob.es), read directly, instead name PERTE and Retech, with espanadigital.gob.es explicitly denying co-governance is one of the two. Both framings are recorded in the entity, unresolved. | **Open — needs the original July 2022 press materials to adjudicate** |
| [[ES-INCIBE]] / [[ES-CCN]] → [[ES-LCGC]] | Reporting describes an institutional dispute over a draft allocation of competences. **A dispute is not a relationship**, and the law is not in force. | Open (deliberate) |
| [[ES-ENI]] ↔ [[ES-ENS]] | Consistently presented together in Spanish practice; no source read establishes a relationship between the instruments. | Open |

### Factual gaps — Spain

| Entity | Question | Status |
|---|---|---|
| [[ES-NTI-RISP]] | The DCAT-AP-ES model is described as **in administrative processing**, so the `based-on` descent from [[EU-DCAT-AP]] may not yet be in force. Recorded at `confidence: low` with `valid_from: null`. | Open — confirmed still accurate on re-verification 2026-08-26. |
| [[ES-LCGC]] | No BOE citation exists to give — the instrument is a draft. Its passage would also make the Centro Nacional de Ciberseguridad modellable. | Open |
| [[ES-ENI]] | Legal base not modelled: sources say it was established by article 42 of Ley 11/2007, an act since replaced by the 2015 administrative-procedure legislation. The chain from the current base was not established, and the repealed act was not asserted as its parent. | **Partly resolved 2026-08-27** — anabad.org, read directly, gives the current statutory anchor: the ENI's existence is contemplated in Article 156 of Ley 40/2015 (the act that replaced the 2007 legislation). No typed edge added, since neither the ontology nor the source cleanly distinguishes "contemplated by" from "derived from" — recorded in prose on the entity instead. |
| [[ES-LOPDGDD]] | **The `Ley Orgánica` rank is not modelled.** Spain's constitutional hierarchy distinguishes organic from ordinary laws, and only the organic rank lets its Title X bind. `type: law` flattens it — as it already flattens *Gesetz*/*Verordnung*, *wet*/*koninklijk besluit*, *loi*/*ordonnance*, and (per `discovery/candidates.md` §6, folded in here 2026-09-05) [[IE-PSI-REGULATIONS-2021]] vs. the Irish Act, and [[INTL-EEA-JCD-154-2018]] — a Joint Committee *decision* filed as a `law` alongside ordinary statutes. No field was added: five countries have been modelled without one, and adding it would require re-reading every instrument in the Atlas. This is a taxonomy change (`metadata/taxonomy.md`, `metadata/schema.json`) touching every legislation entity, not a single new type — genuinely large. | Open (ontology question, large) |
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
| [[EU-INSPIRE]] → the UN-GGIM structure | A EuroGeographics presentation *about* UN-GGIM given to an INSPIRE audience is evidence the communities talk, not that the instruments relate. The geospatial cluster has its UN parent and no European edge. **Retired from `discovery/candidates.md` §1 as a candidate, 2026-09-05, after a fourth independent attempt across four separate passes still found no source stating the relationship directly** — an MDPI article's specific-sounding claim (a UN-GGIM: Europe working group selecting themes "from the list of the INSPIRE annexes") 403'd on every attempt; the current un-ggim-europe.org homepage, its "Implementing UN-GGIM's frameworks in Europe" working-group page, and its 2026-2030 work plan PDF (unreadable binary) were all checked directly and none mentions INSPIRE; three specific Working Group A recommendation PDFs found by search all 404. Left here as the permanent record of a plausible-looking edge that four attempts could not source, rather than kept as an active candidates.md lead. |
| Any EU/national reference to a **UN/CEFACT** standard | Searched; nothing found. [[UN-CEFACT]] is attached to [[UN-UNECE]] and connects to the European layer not at all |
| **EuroGeographics** | Probably the missing European node, playing [[EU-ESS]]'s role for geospatial. Every source found is its own site or trade press — creating it on that basis would repeat the error this batch existed to correct |
| [[UN-FPOS]] → national statistical legislation | **Closed, negative, 2026-09-05.** Both national statutes' own consolidated texts ([[NL-WET-CBS]], [[DE-BSTATG]]) were read directly for this exact question; neither mentions the UN or the Fundamental Principles. No edge asserted for either. |
| [[EU-AI-ACT]] → [[UN-AI-ETHICS-RECOMMENDATION]] | The dates line up — UNESCO 2021, [[ES-AESIA]] 2023, AI Act 2024 — and **nothing read says they relate**. Chronology is not causation, and this was the batch's most attractive available error |
| [[EU-SDG-INDICATORS]] `applies-in` | Not asserted. An indicator set is not an instrument that applies in a member state, and no national SDG indicator set is modelled for any of the five countries |

### Typing questions opened

| Entity | Question |
|---|---|
| [[UN-CES]] | Typed `programme`. It is a standing intergovernmental conference with a Bureau, so `organisation` is arguable; typed `programme` because it is convened *by* [[UN-UNECE]] rather than existing beside it, the same reading applied to [[UN-GGIM]] |
| [[INTL-OECD-CSSP]] | The sources give **two names and two acronyms** — *committee on statistics and statistical policy* (CSSP) and *statistics committee* (CSTAT) — and differ on whether Eurostat represents "the EU" or "the European Commission". | **Narrowed 2026-09-05**: the OECD's own committee page (oecdgroups.oecd.org, BodyID 7229), read directly, closes the "no OECD source cited" half and confirms "CSSP" as the official name — it does not mention "CSTAT" at all, which corroborates one name but does not disprove the other. `confidence` raised to `medium`. The EU-vs-Commission representation question is unchanged |

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
source), and **Rijkswaterstaat, ProRail, Defence and RVO** as BGT
bronhouders. **Digimelding**, the stelsel's error-reporting facility, is
now [[NL-DIGIMELDING]] (research-queue pickup, 2026-09-04).

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
| [[PL-MOBYWATEL]] | Does a national digital identity system's inability to satisfy a coming requirement have a relationship type? | **Closed as a sourcing question, 2026-09-04**: a research-queue pickup found the Ministry of Digital Affairs' own gov.pl press release, closing the "press reporting only" gap and raising confidence to `medium` — and correcting the framing, since the ministry describes a separate, purpose-built wallet planned for end-2026 rather than mObywatel failing to comply. **Still open as a modelling question**: no relationship type expresses "an obligation not yet met" — `related-to` is the closest available and understates it, the sixth such vocabulary gap this project has found. | **Open — vocabulary** |
| [[PL-DANE-GOV-PL]] | ⚠ **Not one source is the portal's own site** — dane.gov.pl's own homepage remains a JavaScript application with no static content an automated fetch can retrieve. | **Partly resolved 2026-08-27** — the operator gap is closed: gov.pl's own Ministry of Digitisation page, found via search and read directly, names the Minister of Digitisation as responsible for the system and gives an approximate launch date (since May 2014, not a specific day). The portal's own site remains unreachable. |
| Institutional transformations | Three now touched in two countries — Spain's completed, Poland's COI one **pending**, Poland's GIODO one **narrower but still unmodelled** (UODO's own report now calls it a legal succession). Only the Spanish one is modelled as a succession. Worth handling deliberately rather than case by case | Open (modelling) |

## Factual details flagged in entity bodies

| Entity | Question | Noted by / date | Status |
|---|---|---|---|
| [[NL-PAS-TOE-OF-LEG-UIT]] | Is the procurement threshold €50,000, and is that figure current? | **Closed 2026-09-05**: forumstandaardisatie.nl's own Definitions section, read directly, confirms €50,000 exactly ("ten minste € 50.000"). `confidence` raised to `high` | Batch 1 / 2026-08-14 | Closed |
| [[NL-FORUM-STANDAARDISATIE]] | Exact 2006 establishment date and instrument reference | **Narrowed 2026-09-05**: the College Standaardisatie half is now answered — [[NL-OBDO]]'s own sourcing (roraonline.nl, read directly) traces its tasks transferred to the Nationaal Beraad Digitale Overheid (end of 2014) and on to the OBDO (8 March 2018), so the College no longer performs the function. The Forum's own exact 2006 establishment date and instrument reference is still unsourced. | Batch 1 / 2026-08-14 | Open |
| [[NL-OBDO]] | Precise boundary between the OBDO's advisory role and its decision-making role | **Narrowed 2026-09-05**: both Staatscourant items are now confirmed rather than "likely" — Stcrt. 2018, 9728 read directly is the *Instellingsbesluit Sturing Digitale Overheid* (19 January 2018), and Stcrt. 2022, 18861 is confirmed as a 12 July 2022 *amending* decree, not a separate instellingsbesluit. The advisory/decision-making boundary itself is still not stated in the decree text as read. | Batch 1 / 2026-08-14 | Open |
| [[NL-GDI]] | Does "GDI" expand to *Generieke* or *Gezamenlijke* Digitale Infrastructuur? Search results used both. | **Closed 2026-09-05**: digitaleoverheid.nl's own dedicated GDI page, read directly, uses only "Generieke." "Gezamenlijke" traces to a single 2017 iBestuur opinion piece proposing a deliberate rename, never adopted — not a genuine alternate name. | Batch 1 / 2026-08-14 | Closed |

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
| [[DE-UKR]] | Has the bill extending its remit to [[DE-BFV]] been enacted? | Two political-press reports describe a government bill. Only the [[DE-BND]] edge is asserted. If enacted, a second `applies-to` follows. | 2026-08-18 | Open |
| [[FR-CNCTR]] / France | **The délégation parlementaire au renseignement is not modelled.** | France currently appears in the Atlas with independent legality control and **no parliamentary control**, which is not an accurate picture of French oversight. Germany, the UK and Poland all have their parliamentary body modelled. | 2026-08-18 | Open — known gap |
| [[FR-CNCTR]] | DNRED and TRACFIN — two of the six *premier cercle* services — are absent. | The CNCTR's four `applies-to` edges understate its remit by two. Both are customs and financial bodies whose primary function is not intelligence, so this is a scoping decision rather than an oversight. | 2026-08-18 | Open — scoping |
| [[FR-DGSI]] | Does [[FR-LIL]] Title IV name the DGSI as a controller? | The `governed-by` edge is carried at **`confidence: low`**: the sources describe the state-security and defence regime and name CRISTINA, a file of the DGSI's predecessor, rather than naming the service. It is the weakest of the batch's cross-cluster bridges. | 2026-08-18 | Open |
| [[GB-MI5]] | **Defence Intelligence** has no avowal act and was not researched. | The UK appears with three services where France has four and Poland four. | 2026-08-18 | Open |
| [[BE-WIV-1998]] | The **BIM-wet of 4 February 2010** and the **BIM-commissie** are not modelled. | Belgium appears with an organic act and an oversight act and **no authorisation regime**, which is not a complete picture. | 2026-08-18 | Open |
| [[BE-COMITE-I]] | **OCAD/OCAM** is not modelled. | The 1991 act was amended on 10 July 2006 to place OCAD under the joint supervision of Comité P and Comité I. The arrangement is recorded in prose and not in the graph. | 2026-08-18 | Open — scoping |
| [[PL-ABW]] | **CBA** is not modelled, and its current status was not established. | The sources name it among the five services under the College for Special Services and within [[PL-KSS]]'s remit. | 2026-08-18 | Open |
| [[PL-KSS]] | Does Poland have an **independent legality-review body** comparable to [[FR-CNCTR]] or [[NL-TIB]]? | Not researched. Poland currently shows parliamentary oversight with no independent counterpart, which may or may not reflect Polish law. | 2026-08-18 | Open |
| [[PL-USKWSWW-2006]] | **No official Polish government URL** could be found. | **Narrowed 2026-09-05**: `eli.gov.pl`'s own legislative-identifier API, read directly, confirms the act's title and existence, and its Dz.U. citation (2006 Nr 104 poz. 709) is now known via the ISAP document ID — but `isap.sejm.gov.pl` itself remains genuinely CAPTCHA-blocked, so consolidation and amendment history are still unread. | 2026-08-18 | Open — narrower |
| [[DE-BVERFSCHG]], [[DE-MADG]] | **No Gesetze-im-Internet URL** was returned by search. | **Narrowed 2026-09-05**: a fresh search located both. BVerfSchG's own text was read directly (gesetze-im-internet.de, `Ausfertigungsdatum: 20.12.1990`); MADG's official URL 503'd, so a bundestag.github.io mirror substituted, independently confirming the same 20.12.1990 date. Both `start_date` fields are now sourced. Their structure and amendment history beyond the enactment date remain unread. | 2026-08-18 | Open — narrower |
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
| [[NO-NSM]] | Its statutory basis — the **sikkerhetsloven** — is not an entity. | NSM carries no `governed-by` edge as a result. One source calls NSM part of the secret services; that phrasing is not in the government sources and the Atlas will not classify on it | 2026-08-18 | ✅ **Resolved (the classification question) — 2026-08-22; which act is current resolved 2026-09-05.** NSM's own website states directly that NSM, together with Etterretningstjenesten and PST, forms Norway's three intelligence, surveillance and security services. lovdata.no's own text of LOV-2018-06-01-24, read directly, confirms the 2018 Act (in force 1 January 2019) repealed the 1998 Act snl.no had named — so the current statute is now known, though it remains uncreated as an Atlas entity and no `governed-by` edge is asserted. |
| Norway | **Etterretningstjenesten and PST are not modelled.** | Norway has a national security authority and no intelligence services, three days after a batch that gave seven countries both | 2026-08-18 | Open |
| [[CH-REVDSG]], [[CH-EMBAG]] | **No Fedlex citation anywhere in the Swiss set.** | [[CH-REVDSG]] carries the batch's most comparative weight — the `aligned-with` argument — on a KMU-portal page, a university blog and a vendor guide | 2026-08-18 | ✅ **Partly resolved — 2026-08-22.** Both now cite Fedlex directly (`eli/cc/2022/491/de` and `eli/cc/2023/682/de`), found via outbound links on kmu.admin.ch's and bfs.admin.ch's own pages. Fedlex renders client-side in JavaScript, so neither citation could be read past retrieval — the same tooling limit already logged for PDFs. |
| [[CH]] | The **EU–Switzerland adequacy decision** is not an entity. | The Atlas holds [[EU-UK-ADEQUACY]]; the same kind of Commission act covers Switzerland, and the whole revDSG revision was aimed at preserving it | 2026-08-18 | Open |
| [[CH-BACS]] | What is the statutory basis of the **24-hour reporting duty** in force since 1 April 2025? | **Narrowed 2026-09-05**: an independent legal publication (Bratschi AG, read directly) names the precise basis — Article 74a of the Informationssicherheitsgesetz (ISG), with operational detail in the accompanying Cybersecurity Ordinance (CSV). The ISG is still not an Atlas entity, so no `governed-by` edge is asserted. The duty matches [[EU-NIS2]]'s without Switzerland being bound by it, and **no relationship to NIS2 is asserted** — resemblance is not derivation | 2026-08-18 | Open |
| [[CH-DVS]] | Legal form, governance, and relationship to [[CH-EMBAG]]. | `coverage: low`; only its own site was returned. It is constituted jointly across Confederation, cantons and communes — filed `level: national` because that is the closest available value, **not because it is accurate** | 2026-08-18 | Open — and see the `level: local` design item. Re-checked 2026-08-22: DVS's relationship to EMBAG remains unsourced (its blog post is evidence of interest, not of a role under the act), and the January 2022 operational-start date could not be independently re-confirmed either. |
| [[IE-NCS-BILL]] | **Has it been enacted?** | Its final content and even its short title are unsettled | 2026-08-18 | **Open — still not enacted as at 2026-09-05** (re-checked against The Irish Times, 24 August 2026, read directly), and the situation keeps escalating: reasoned opinion 7 May 2025, CJEU referral July 2026, and now an initial €2.8 million penalty plus daily fines. |
| [[UN-AARHUS]] | Ireland's ratification date and terms. | The other six member states carry `applies-in`; Ireland does not, because this batch did not gather the evidence for a mixed agreement | 2026-08-18 | Open |
| [[IE-DPA-2018]] | The **Law Enforcement Directive** (2016/680) is still not an Atlas entity. | Part 5 of the Irish Act transposes it, and it is one of the two legal bases of [[EU-UK-ADEQUACY]]. Queued since the UK batch and now blocking a second entity | 2026-08-18 | Open |

## Data spaces (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-MANUFACTURING-DATA-SPACE]] / [[DE-MANUFACTURING-X]] | Is the German initiative part of, feeding into, or independent of the common European manufacturing data space? | They occupy the same sector, and the EU data space's named deployments (UNDERPIN, SM4RTENANCE) are not connected to Manufacturing-X by any source read. Same sector is not a relationship | 2026-08-18 | Open |
| [[EU-PUBLIC-ADMIN-DATA-SPACE]] | How does it relate to [[EU-INTEROPERABLE-EUROPE-ACT]], [[EU-EIF]] and [[EU-SDG]]? | This is the data space closest to the Atlas's own subject matter — 232 entities carry [[DOMAIN-GOVERNMENT]] — and the entity where drawing unsourced edges would be most tempting. None is asserted | 2026-08-18 | Open |
| [[EU-FINANCIAL-DATA-SPACE]] | **What are the other two components?** | The sources name FIDA as one of three and do not name the rest. An entity whose own description admits it is one-third specified | 2026-08-18 | Open |
| [[EU-FINANCIAL-DATA-SPACE]] | **PSD2** is not an entity. | **Narrowed 2026-09-05**: FIDA is now modelled as [[EU-FIDA]] (COM(2023) 360, proposed 28 June 2023, still in trilogue), sourced from direct reads of the Commission's own FIDA page and EUR-Lex. PSD2, the backdrop FIDA is contrasted against, remains unmodelled. | 2026-08-18 | Open |
| [[EU-CULTURAL-HERITAGE-DATA-SPACE]] | Cooperation with [[EU-MEDIA-DATA-SPACE]] and [[EU-TOURISM-DATA-SPACE]] | The sources say it "will explore opportunities for cooperation" with both. Intent is not connection, so no edge is asserted from either side | 2026-08-18 | Open |
| [[EU-TOURISM-DATA-SPACE]], [[EU-MEDIA-DATA-SPACE]], [[EU-PUBLIC-ADMIN-DATA-SPACE]] | Deployment projects, governance, operators, scope. | All three are `coverage: low`, created for completeness of the fourteen. Their thinness is the honest state. **Narrowed 2026-09-05**: the fourth, [[EU-SKILLS-DATA-SPACE]], now has one of its two named deployment projects modelled as [[EU-DS4SKILLS]]; the other, EDGE-Skills, remains unmodelled | 2026-08-18 | Open |
| [[EU-EOSC]] | Does the **EOSC Federation** admit non-member states? | Its federated design is the closest thing in the Atlas to what [[NO]] and the EEA states would need. Not researched | 2026-08-18 | Open |
| [[EU-SKILLS-DATA-SPACE]] | **ESCO**, **Europass** and the **European Skills Agenda** are not modelled. | **Closed, negative, 2026-09-05**: checked directly against [[EU-DS4SKILLS]]'s own sources (HaDEA's announcement, ds4skills.eu) rather than left as a presumption. Neither ESCO, Europass nor the European Skills Agenda is mentioned by either source. Still unmodelled, but no longer presumed connected | 2026-08-18 | Closed — negative finding |
| [[INTL-IDS-RAM]] | The **IDS Connector** is not modelled. | It is the central technical component — a security gateway with Base, Trust and Trust+ profiles, the last protecting against manipulation by malicious administrators. `technology` is a type the Atlas defines and still does not use | 2026-08-18 | Open — and see the unused-type item |
| [[INTL-IDS-RAM]] | Version. | The entity describes **IDS-RAM 3.0** (April 2019), the version search returned. Version 4 exists and was not established | 2026-08-18 | Open |
| [[INTL-IDSA]] | Membership, given by one source as 133 companies, is unverified; the **Eclipse Dataspace Connector** implementations are unmodelled | | 2026-08-18 | Open |
| [[DE-MANUFACTURING-X]] | **Factory-X**, **Aerospace-X**, **energy data-X** and **Plattform Industrie 4.0** are not modelled. | Named in the sources as lighthouse projects, siblings and the concept base | 2026-08-18 | Open |
| [[EU-CEEDS]] | **INSIEME** and the six Horizon Europe energy data space projects are not modelled; nor is Germany's **ENDA**. | The concrete deployment layer beneath the data space | 2026-08-18 | Open |

## Portugal, Luxembourg and Czechia (batch of 2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[CZ-NUKIB]] | **NIS2 transposition not identified** for Czechia. | Czechia's cyber security act No 181/2014 is also unmodelled. Portugal's own gap (PT-CNCS) was closed 2026-08-26: [[PT-DECRETO-LEI-125-2025]], in force since 3 April 2026 | 2026-08-18; PT closed 2026-08-26 | Open — Czechia only |
| [[LU-CTIE]] | **Luxembourg's NIS2 competent authority and CSIRT** are unmodelled. | **Narrowed 2026-09-05**: now named and sourced — ILR (competent authority for most sectors, CSSF for banking), GOVCERT.LU (public-sector CSIRT) and CIRCL (private-sector/municipal CSIRT), transposed by a Law of 5 May 2026. None created as entities yet — that would be at least four new nodes. | 2026-08-18 | Open — narrower |
| [[CZ-UNMZ]] | **ČAS is not modelled.** | Czechia splits standardisation: ÚNMZ holds the membership, ČAS does the technical committees, drafting and publication. The body that actually produces ČSN standards is absent from the graph | 2026-08-18 | Open |
| [[LU-DATA-PUBLIC]] | **No custodian modelled.** | [[LU-CTIE]] is the obvious operator and it is not sourced. Portugal's and Czechia's equivalent gaps (PT-DADOS-GOV, CZ-DATA-GOV) were both closed by 2026-08-26 | 2026-08-18; PT and CZ closed | Open — Luxembourg only |
| [[CZ-ZAKON-60-2026]] | What does the act contain beyond [[CZ-DIA]]'s role? | `coverage: low`. What "controlled access" covers, which data, what rights it creates — all unestablished. `start_date` is deliberately null: the sources give the Sb. citation, not a date of effect | 2026-08-18 | Open |
| [[CZ-DIA]] | **Act No 12/2020** on the right to digital services, DIA's constituting statute, is not modelled. | DIA carries `implements` [[CZ-ZAKON-60-2026]] but no `governed-by` edge to the act that created it | 2026-08-18 | Open |
| [[PT-AMA]] | **ePortugal**, the **Chave Móvel Digital**, the **Cartão de Cidadão** and the **iAP** are unmodelled. | Portugal's identity means would be the [[EU-EIDAS]] counterparts; the iAP is its interoperability platform | 2026-08-18 | Open |
| Standards bodies generally | The membership counts in the Atlas are what is **sourced**, not what is true. | [[LU-ILNAS]] shows six (updated 2026-08-25, was five when this row was written), [[GB-BSI]] five, [[PT-IPQ]] three, most others two — because the CEN membership rule was the only source available for the four created in the structural-fixes batch. The column invites a comparison it cannot fully support | 2026-08-18 | Open |

## Research-queue batch (2026-08-18)

| Entity | Question | Why it matters | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-OPEN-DATA-DIRECTIVE]] | **The Atlas cannot model enforcement against a member state.** | Nineteen member states faced infringement proceedings over this directive and four — Belgium, Bulgaria, Latvia and the **Netherlands** — were referred to the Court of Justice in February 2023. There is no entity type for an infringement procedure, no relationship type for "was referred to the Court over". A reader sees that [[NL-WHO]] was amended in 2024 and cannot see why | 2026-08-18 | **Narrowed 2026-09-05** — the missing node now exists ([[EU-CJEU]], confirmed via curia.europa.eu's own page, from `discovery/candidates.md` §6). Creating the Court did not create the edge: the Atlas still has no entity type for an individual infringement procedure and no relationship type for "was referred to the Court over", so the specific February 2023 referral is still not itself expressible. **Open — the node exists; the procedure-level type and relationship do not** |
| Belgium, France, Spain | **Open Data Directive transpositions still unidentified.** | All three amended existing law rather than passing a standalone act, which is why they are harder to find than Ireland's S.I. Down from five countries to three | 2026-08-18 | **Open — next** |
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
| [[NL-WET-BRO]] | The **2024 amendment** on bronhouderschap of models and quality control. | Recorded by the Tweede Kamer as a pending change; its content and status were not established | 2026-08-18 | Open |
| [[NL-NHR]] | **BRIS** and the Company Law Directive are not modelled. | The Dutch commercial register is part of an EU-wide interconnection system, and the Atlas shows it as purely national | 2026-08-18 | Open |

## Candidate-clearing batch, 2026-08-21

| Entity / topic | Question | Why it's unresolved | Noted by / date | Status |
|---|---|---|---|---|
| [[EU-VOLUNTARY-REVIEW-2023]] | What date did the Commission adopt COM(2023) 700 final? | **Closed 2026-09-05**: EUR-Lex's own text, read directly via its TXT/HTML URL form (the form that finally returned content), gives the document's own header as "Brussels, 15.5.2023." `start_date` set to 2023-05-15; `confidence` raised to `high` | Candidate batch / 2026-08-21 | Closed |
| [[EU-EMSWE]] | Are the SafeSeaNet codes and the IMO GISIS port facility codes Atlas subjects? | They are named in the same provision as [[UN-LOCODE]] and neither is modelled. The IMO is not in the Atlas at all; creating it to carry one code list would be the thin entity the taxonomy threshold prevents | Candidate batch / 2026-08-21 | **Resolved 2026-09-05** — `imo.org`'s own page, read directly, confirmed IMO's substantive mandate as a full UN specialised agency, clearing the bar this row itself said "one code list" would not clear. [[UN-IMO]] and [[UN-IMO-GISIS]] now exist; the SafeSeaNet codes themselves remain unmodelled |
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
entity's *own* claims, so promotion was not taken on a technicality.
**Both gaps since closed**: a targeted search (2026-08-28) found
`wetten.overheid.nl`'s BWBR0041515, the Wbni's own text, promoting the
entity to `primary-source`; a further targeted search (2026-09-05) found
the commencement decree itself (Staatsblad 2018, 389), which states
verbatim "Met ingang van 9 november 2018 treden in werking: a. de Wet
beveiliging netwerk- en informatiesystemen..." — closing the
previously-unconfirmed `start_date` lead. `start_date` set to 2018-11-09;
`confidence` raised to `high`.
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
  previously-unknown "Werkagenda Waardengedreven Digitaliseren
  (2022-2024)" and then [[NL-NDS]] (2025), which the same page states
  explicitly "does not replace but connects existing plans." **Closed
  2026-09-05**: the intervening strategy is now
  [[NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN]], published 4 November
  2022 by State Secretary Van Huffelen. [[NL-DIGIBETER]]'s `successor` now
  points to it (rather than skipping ahead to [[NL-NDS]]), and it carries
  its own `supersedes` edge back to [[NL-DIGIBETER]] — the real chain the
  prior pass called for.
- [[NL-NDS]]'s continuation under the post-2025 cabinet — genuinely
  uncertain in the prior text — is now confirmed: a March 2026 article
  (`digitaleoverheid.nl/nieuws-nds/...`, found via search, read directly)
  states "The programme continues and retains the same name," now
  co-led by [[NL-EZK]] (modelled since; not an Atlas entity at the time
  of this pass) alongside [[NL-BZK]].
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
- [[NL-DIGIKOPPELING]]'s comply-or-explain-list membership lost its sole
  supporting citation (`vngrealisatie.nl`, now HTTP 404) and needs a
  replacement source, not just re-confirmation.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see the batch's own completion report for results.

## Germany cluster re-verification (2026-08-28)
All 26 remaining `search-only` Germany entities — 3 data spaces
([[DE-CATENA-X]], [[DE-MANUFACTURING-X]], [[DE-MDS]]), 2 frameworks
([[DE-IT-ARCHITEKTURRICHTLINIEN]], [[DE-IT-GRUNDSCHUTZ]]), 1 initiative
([[DE-GDI-DE]]), 6 pieces of legislation ([[DE-BSIG]], [[DE-GEOZG]],
[[DE-IWG]], [[DE-NIS2UMSUCG]], [[DE-OZG]], [[DE-REGMOG]]), 8 organisations
([[DE-BSI]], [[DE-DESTATIS]], [[DE-DFN]], [[DE-DIN]], [[DE-FITKO]],
[[DE-IT-PLANUNGSRAT]], [[DE-KOSIT]], [[DE-NFDI]]), 2 platforms
([[DE-GOVDATA]], [[DE-MOBILITHEK]]), 3 standards ([[DE-DCAT-AP-DE]],
[[DE-XOEV]], [[DE-XRECHNUNG]]) and 1 strategy ([[DE-DIGITALSTRATEGIE]]) —
were re-verified against primary sources and **all 26 were promoted to
`verification: primary-source`**. This is the whole remaining Germany
country cluster in one pass; [[DE-BDSG]] had already been promoted
separately and was read but not edited.
**A domain-wide finding**: `bmi.bund.de` and `digitale-verwaltung.de` (both
Bundesministerium des Innern properties) returned **HTTP 400 Bad Request on
every attempt this pass** — a consistent, if unexplained, block rather than
a transient failure — affecting [[DE-OZG]], [[DE-REGMOG]] and [[DE-FITKO]]'s
originally-cited sources. `geant.org` and `about.geant.org` (GÉANT
Association) returned HTTP 403 on every attempt, affecting [[DE-DFN]].
Where blocked, this pass followed the brief's instruction to search for
alternate primary sources rather than stall: dedicated Wikipedia articles
(often not previously cited at all) repeatedly supplied exactly the missing
fact — a founding/enactment date, a legal-basis citation, an EU-directive
link — that the blocked government page would have. This is the single
most effective technique across the batch: **five entities'
previously-`null` `start_date` fields were filled this pass**
([[DE-OZG]]: 2017-08-18; [[DE-IWG]]: 2006-12-19; [[DE-KOSIT]]: 2010-09-24;
[[DE-CATENA-X]] deliberately kept `null` — see below; [[DE-NFDI]]:
2020-10-01), each from a dedicated source found by searching further, not
guessed.
**Genuine corrections and closures, not just confirmations:**
- [[DE-XRECHNUNG]]'s previously flagged sharpest gap — no sourced link to
  [[EU-EN-16931]] despite XRechnung being, "in the ordinary understanding
  of the field," a German CIUS of it — is **closed**. Three independently
  read sources (a dedicated Wikipedia article, ClearTax's own explainer,
  and the European Commission's own digital-building-blocks CIUS-compliance
  page) confirm the relationship in their own words. `countries/de/index.md`'s
  "Where an EU instrument has a German implementing act" table gained a row
  for it.
- [[DE-IWG]] went from "nearly empty" (`confidence: low`, no enactment date,
  a frontmatter/body contradiction — the frontmatter already carried an
  `implements-requirement-from` → [[EU-PSI-DIRECTIVE]] relationship that the
  body text flatly denied existed) to reasonably well-sourced: a dedicated
  Wikipedia article on the IWG itself (not previously cited — the entity's
  three original sources were all about its successor DNG) supplied the
  enactment date, the entry-into-force date, and confirmation of the EU
  directive it transposed, resolving the contradiction in the frontmatter's
  favour.
- [[DE-BSIG]] gained a genuine enactment date (20 August 2009, for the
  current BSI-Gesetz superseding the 1991 BSI-Errichtungsgesetz) from the
  BSI's own "Auftrag" page, not previously cited at all despite this being
  a BSI-published law.
- [[DE-DIN]]'s previously-flagged gap ("DIN's own site is not cited") is
  closed — `din.de`'s own history page gives an exact founding date
  (22 December 1917, not just "1917") and the specific 1975 agreement
  recognising DIN as Germany's national standards body.
- [[DE-IT-GRUNDSCHUTZ]]'s equivalent gap ("no bsi.bund.de IT-Grundschutz
  page is cited") is closed the same way, via two `bsi.bund.de` pages found
  by a targeted search after the entity's original sources returned only
  Wikipedia and consultancy explainers.
- [[DE-CATENA-X]]'s `start_date` (previously a fabricated-looking
  `2021-01-01` for what sources only supported as "2021") was **corrected
  to `null`** rather than kept: this pass found the association was founded
  in May 2021 and its research consortium ran August 2021–July 2024, but no
  source gives an exact day for either, so the padded date was removed and
  the real precision described in prose instead.
- [[DE-CATENA-X]] also now carries a **contested-status finding**: its own
  operator (catena-x.net) calls the network "fully operational," while a
  directly-read WirtschaftsWoche investigation calls it "the greatest IT
  hot air of German industry" and reports finding no concrete operating
  examples after two and a half years of trying. Both are recorded rather
  than one being smoothed over.
- [[DE-GEOZG]]'s official `gesetze-im-internet.de` text returned HTTP 503 on
  three separate attempts (genuinely persistent, not the single transient
  503 the brief warned about) and could not be read directly even this
  pass; two independent legal-database mirrors (`dejure.org`, `buzer.de`)
  substituted by quoting the statute's own preamble and citation, which is
  what let this entity reach `primary-source` despite the official site
  staying unreachable.
**Still open after this pass:**
- The German batch's principal ontology finding — the `level` vocabulary
  has no term between `national` and `local`, so the 16 Länder, their 16
  INSPIRE transposition acts, and Land-hosted bodies like [[DE-KOSIT]] are
  not representable — is **unchanged** by this pass. It surfaced again on
  [[DE-GEOZG]], [[DE-GDI-DE]] and [[DE-KOSIT]] and remains the batch's
  clearest unresolved modelling question.
- [[DE-NIS2UMSUCG]] `supersedes` [[DE-BSIG]] is still recorded at
  `confidence: low` for want of an amendment-lineage relationship type.
  This pass's direct reading (Deloitte's and OpenKRITIS's own pages) *
  reinforces* rather than resolves the underlying tension — both sources
  independently describe the mechanism as a comprehensive in-place revision
  rather than a repeal-and-replace, which is exactly what `supersedes`
  overstates.
- [[DE-MANUFACTURING-X]] ↔ [[EU-MANUFACTURING-DATA-SPACE]] and
  [[DE-MDS]]/[[DE-MOBILITHEK]] ↔ [[EU-EMDS]]: still no source, even after
  this pass's added fetches, names the European-level parent for either
  German data space. Both remain visible, logged gaps rather than asserted
  relationships.
- [[DE-DESTATIS]] ↔ [[EU-EUROSTAT]]: narrowed but not closed. This pass
  confirmed `part-of` [[EU-ESS]] directly on Destatis's own site (which now
  names the European Statistical System explicitly, closing that half of
  the gap), but no page read names Eurostat by name on a Destatis page, so
  the direct Destatis↔Eurostat edge — sitting alongside the still-open
  [[UN-UNSD]] ↔ [[EU-EUROSTAT]] gap — stays unasserted. (The
  [[UN-FPOS]] ↔ [[NL-WET-CBS]] gap referenced here in earlier passes is
  now closed, negative — 2026-09-05.)
- [[DE-DIGITALSTRATEGIE]] stays `status: unknown`: its 2025 horizon has
  passed, a "2. Fortschrittsbericht" (October 2024) surfaced in search
  suggests it was still being actively tracked at that point, but no source
  read states whether [[DE-MODERNISIERUNGSAGENDA-BUND]] or [[DE-BMDS]]
  formally supersedes it, so no `successor` is recorded.
- `bmi.bund.de` and `digitale-verwaltung.de` are confirmed **consistently**
  blocked to WebFetch this pass (HTTP 400 on every URL tried, across
  multiple entities and multiple attempts) — worth flagging for whoever
  next touches a German entity citing either domain, the same way the
  Netherlands batch flagged `digitaleoverheid.nl`'s bot wall.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see this batch's own completion report for results.

## EU legislation/data-spaces cluster re-verification (2026-08-28)
Batch scope: the 8 EU data-space entities and 12 EU legislation entities
listed in this batch's assignment (all `EU-*` files under `data-spaces/`
and `legislation/`). 17 of 20 promoted from `verification: search-only` to
`primary-source` on a genuine majority of directly-read sources each; two
(`EU-EMSWE`, `EU-CH-ADEQUACY`) already partly promoted in an interrupted
prior attempt were re-confirmed and completed; one (`EU-SDG`) stays at
`search-only` — see below.
**A significant, corrected factual error:** [[EU-DIGITAL-OMNIBUS]]'s
identifying CELEX/COM number was wrong. It carried `COM(2025) 836` and a
CELEX citation for that number, but COM(2025) 836 is a **distinct sibling
proposal** — the "Digital Omnibus on AI" — not the DGA/Open-Data-Directive/
GDPR proposal this entity actually describes (that one is **COM(2025)
837**). Both proposals were published the same day, 19 November 2025, and
diverged sharply in outcome: COM(2025) 836 has since been **adopted** as
**Regulation (EU) 2026/1744**, published in the Official Journal 24 July
2026 and in force from 27 July 2026, deferring the AI Act's Annex III
high-risk deadline from 2 August 2026 to 2 December 2027. COM(2025) 837
(the entity this Atlas actually models as `EU-DIGITAL-OMNIBUS`) remains
under negotiation as of the most recent tracker update (24 July 2026) this
pass could read. The corrected relationship: `EU-DIGITAL-OMNIBUS` does
**not** amend [[EU-AI-ACT]] — that erroneous edge (asserted only in body
prose, not as a frontmatter relationship) has been removed from
`legislation/eu-ai-act.md` and `legislation/eu-digital-omnibus.md`, both
corrected in this pass, and from `regions/eu/index.md`.
**Closed 2026-09-05.** Regulation (EU) 2026/1744 ("Digital Omnibus on AI")
is now [[EU-DIGITAL-OMNIBUS-AI]], `amends` [[EU-AI-ACT]]. EUR-Lex's own
text — unreadable to this Atlas's fetch tooling when this gap was first
found — was read directly via its TXT/HTML URL form, which also corrected
the regulation's own adoption date: **8 July 2026**, not the 29 June 2026
date a WebSearch cross-check had previously supplied.
**Two SWD citation errors, corrected:** four data-space entities
(`EU-CEEDS`, `EU-CULTURAL-HERITAGE-DATA-SPACE`, `EU-EOSC`,
`EU-MANUFACTURING-DATA-SPACE`) cited a source titled "SWD(2024) 21
final" pointing at
`digital-strategy.ec.europa.eu/en/library/staff-working-document-data-spaces`
— that URL is actually the Commission's **first** staff working document
on data spaces (SWD(2022) 45 final, 23 February 2022), not the second
(SWD(2024) 21 final, 24 January 2024, at
`.../library/second-staff-working-document-data-spaces`). All four
corrected to the right URL, confirmed by reading the corrected page
directly.
**A new, thin relationship added:** [[EU-GREEN-DEAL-DATA-SPACE]]
`references` [[EU-INSPIRE]], sourced from the Commission's own Environment
page ("integrates with existing frameworks like the INSPIRE Directive,
under revision for Q4 2025 adoption"). No detail on the integration
mechanism was found, and the claimed INSPIRE revision itself was not
researched — flagged as thin rather than dropped.
**A previously-unrecorded application date:** [[EU-EMSWE]] (European
Maritime Single Window environment, Regulation (EU) 2019/1239, adopted 20
June 2019) does not actually become applicable until **15 August 2025**,
confirmed by reading the Commission's own DG MOVE page directly. The prior
text carried only the 2019 adoption date with no application-date
milestone at all — the kind of gap that matters most on a staged-timetable
instrument.
**EUR-Lex is comprehensively unreachable to this pass's fetch tooling.**
Every attempt across all 20 files — different CELEX renderings, ELI
records, LEGISSUM summaries, the homepage itself — returned either empty
content or (rarely) an outright error, never actual legal text. This
matches the block already documented in `EU-CH-ADEQUACY`'s and
`EU-EMSWE`'s pre-existing text from an earlier pass ("retrieval is blocked
by the network egress proxy"). Every promoted entity in this batch was
promoted on alternate primary/secondary sources (Commission policy pages,
the European Parliament's own Legislative Observatory, national
government mirrors of adopted EU texts such as legislation.gov.uk, ENISA,
EMSA, Wikipedia) rather than on EUR-Lex itself — EUR-Lex citations are
kept in every `sources:` list as the nominally-authoritative-but-unread
citation rather than dropped.
**[[EU-SDG]] stays at `search-only`** — the one entity in this batch that
could not be promoted despite genuine, repeated effort. Both original
sources failed (EUR-Lex empty; `europeansources.info` aborted mid-fetch
twice). Six alternates were then tried: the Commission's current
single-digital-gateway policy page (404 — appears retired/moved), `cep.eu`
(covers only the 2017 pre-regulation proposal stage), `monitoraggio.sdg.
gov.it` (HTTP 403), Your Europe's citizen portal (no mention of the
regulation), the eIDAS policy page (wrong topic), and a Dutch
parliamentary-monitor mirror (wrong topic). None yielded a readable page
about this specific regulation. A plausible Commission policy page for
this regulation should exist and is worth a fresh search in a future pass
— it may simply have moved to a URL not surfaced by this pass's searches.
**A structural gap noticed but not acted on** (out of this pass's file
scope): `regions/eu/index.md`'s legislation section does not mention
[[EU-INSPIRE]], [[EU-EINVOICING-DIRECTIVE]], or
[[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]] at all, despite all three being
established EU-level legislation entities with existing relationships
(national implementations, standards-chain links). This pass added only
small `✅` annotations to lines already mentioning its 20 entities per its
instructions, and did not add new lines for entities absent from the
index — flagged here rather than done, so the index's maintainers can
decide where these three belong structurally.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see this batch's own completion report for results.

## EU organisations/standards cluster re-verification (2026-08-28)
Re-verified all 13 assigned entities (organisations/eu-cen.md,
eu-cenelec.md, eu-edpb.md, eu-eurogeographics.md, eu-gaia-x.md, eu-geant.md,
eu-semic.md; standards/eu-dcat-ap.md, eu-en-16931.md;
frameworks/eu-dssc-blueprint.md, eu-ess.md; publications/eu-egov-benchmark.md,
eu-voluntary-review-2023.md). 11 of 13 promoted `search-only` →
`primary-source`; two open items below.
**Still open after this pass:**
- [[EU-GEANT]] stays at `search-only`. All three originally cited pages
  (geant.org, about.geant.org, compendium.geant.org) 403 or return an empty
  JS shell to automated fetches — this looks like bot-protection across the
  whole geant.org family of domains, not a dead link, and the same block
  hit dfn.de and eduroam.org when tried as further alternates. Three
  alternates were read directly instead (Wikipedia, a CORDIS project
  record, an archived GÉANT3+ partners page), landing exactly at a 50/50
  split of the six sources now listed — the discipline's own borderline
  case, so it was left unpromoted rather than forced. A future pass should
  try geant.org via a different fetch path (e.g. an authenticated tool) or
  look for a readable mirror of the current compendium.
- [[EU-GAIA-X]]: no source read (this pass or before) states an
  institutional relationship to [[EU-COMMON-DATA-SPACES]] or
  [[EU-DSSC-BLUEPRINT]], despite obvious thematic overlap — the Commission's
  own "Mobility Data" page (read this pass) treats a Gaia-X-affiliated
  private initiative as an existing ecosystem to "build upon," which is
  proximity, not a stated relationship. Still queued for a future pass with
  a more targeted search (e.g. Commission communications specifically
  naming Gaia-X as part of the data-spaces programme).
- [[EU-EGOV-BENCHMARK]]: this pass found that the 2025 edition's own
  headline EU publications (op.europa.eu, digital-strategy.ec.europa.eu's
  2025-specific library page) describe the study's scope as "the 27
  European Union Member States (EU27)" and do not themselves name the
  eight non-EU countries the entity's `measures` edges also cover — a
  narrower framing than the general DESI-comparison page's "35 countries."
  A 2025-dated Norway factsheet (found via search, not fetched) confirms
  Norway was still measured, so that edge stays at `confidence: medium`;
  the other seven non-EU countries' edges were lowered to `confidence: low`
  pending an edition-specific source naming each one. A future pass could
  try fetching individual 2025 country factsheets for Switzerland, Albania,
  Montenegro, North Macedonia, Serbia and Türkiye directly.
- [[EU-VOLUNTARY-REVIEW-2023]]: **closed 2026-09-05** — EUR-Lex's own text
  of COM(2023) 700 final, unreadable across several URL forms in this
  pass, was successfully read via its TXT/HTML URL form in a later pass:
  the document's own header reads "Brussels, 15.5.2023," matching its
  companion SWD(2023) 700 and resolving the two-candidate-date question.
  `start_date` set to 2023-05-15.
- [[EU-EUROGEOGRAPHICS]]: its third cited source (an EEA page) is now dead
  — 302s to a eurogeographics.org URL that 404s — and could not be
  replaced with an equally authoritative third source this pass; two of
  three (both eurogeographics.org's own pages) were enough for a majority,
  but a replacement third source would strengthen this further. Also
  corrected a stale membership figure: eurogeographics.org's own current
  homepage states 60 organisations across 44 countries, not the 63/46
  previously recorded, which could not be re-confirmed from any source
  this pass.
- Several EUR-Lex pages were unreadable this pass despite multiple URL
  forms tried (plain TXT, ALL, TXT/HTML, and ELI views) — affecting
  [[EU-ESS]]'s citation of Regulation (EC) No 223/2009 and (at the time)
  [[EU-VOLUNTARY-REVIEW-2023]]'s citation of COM(2023) 700 final, the
  latter since read successfully via its TXT/HTML form (see above). Both
  entities were still promoted to `primary-source` on the strength of
  other sources reaching a genuine majority, but a working EUR-Lex fetch
  path would be a general win across this cluster.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see this session's own report for results.

## INTL standards-body cluster re-verification (2026-08-28)
Re-verified 16 entities: international (non-UN) standards bodies and
treaties, plus [[DOMAIN-NATIONAL-SECURITY]]. Eleven entities promoted to
`primary-source`: [[DOMAIN-NATIONAL-SECURITY]], [[INTL-IDSA]],
[[INTL-IEC]], [[INTL-IETF]], [[INTL-ISO]], [[INTL-ISOC]], [[INTL-NIIS]],
[[INTL-W3C]], [[INTL-X-ROAD]], [[INTL-IDS-RAM]] and
[[INTL-ISO-IEC-27001]]. Five stayed `search-only`: [[INTL-COE]],
[[INTL-OECD]], [[INTL-CONVENTION-108]], [[INTL-CONVENTION-108-PROTOCOL]]
and [[INTL-CONVENTION-108-PLUS]].
**Three domains confirmed fully, independently blocked, not just
`coe.int`.** Every path tried against `coe.int` and `rm.coe.int` (treaty
pages, member-state pages, news announcements, the bare homepage) returned
HTTP 403, consistent with prior passes. This pass additionally confirmed
the same domain-wide 403 block on **`iso.org`** (every path tried:
`/standard/27001`, `/standard/iso-iec-27000-family`, `/about-us.html`,
`/home.html`, `/news`) and on **`oecd.org`** (both cited pages plus the
bare homepage). `commonslibrary.parliament.uk` also 403'd on two separate
tries. Wikipedia articles were substituted and read directly wherever
possible to partially compensate (ISO, IEC, ISO/IEC 27001, ISO/IEC 27000
family, OECD, Council of Europe all corroborated this way), which is what
pushed the three ISO-family entities over a genuine majority despite
`iso.org` itself staying unread throughout — but for COE, OECD and the
Convention 108 family, one substitute source wasn't enough to reach
majority against 4-6 cited sources, so those five stay `search-only`.
**Open item**: if a future pass can reach `iso.org`,
`oecd.org` or `coe.int` directly (different retrieval path/tool), these
five entities are worth revisiting — the underlying facts were not found
to be wrong anywhere, only unconfirmed by the organisations' own pages.
**Two dead/unreadable citations found and documented, not silently
dropped:**
- `dataprotection.govmu.org`'s Mauritius CETS-223-ratification communiqué
  (cited on [[INTL-CONVENTION-108]]'s Mauritius `applies-in` relationship,
  and referenced in [[INTL-CONVENTION-108-PLUS]]'s body prose) now returns
  HTTP 404 — gone, not blocked. The Mauritius ratification-of-the-amending-
  protocol claim is flagged unconfirmed in both files rather than restated
  as settled.
- The WTO PDF cited on [[INTL-CONVENTION-108]]
  (`wto.org/english/res_e/reser_e/2_ssophie_trade_dialogues_wto.pdf`) fetches
  successfully but returns unreadable binary/compressed content to the
  retrieval tool — a tool limitation on that specific PDF's encoding, not a
  site block. Same issue hit the [[INTL-IDS-RAM]] 3.0 PDF
  (an Illustrator/Photoshop-authored PDF whose text layer didn't extract);
  two other IDSA pages covered the same content there, which is why
  IDS-RAM still reached a majority and Convention 108 did not.
**One factual correction on [[INTL-X-ROAD]]:** the previous pass's claim
that Japan was "among the adopters" of X-Road does not survive a direct
read. x-road.global's own history page (read directly) lists Finland, the
Faroe Islands, El Salvador, Iceland, Åland and Ukraine as adopters/partners
and does not mention Japan; Wikipedia's X-Road article likewise says
nothing about Japan. The claim is dropped rather than repeated. The
specific "2018" date for the X-tee/X-Road naming split was similarly
downgraded to unconfirmed — the underlying distinction is well
corroborated, but no page read this pass states the year.
**Still open after this pass:**
- [[INTL-COE]]'s member-count and Russia-post-expulsion-party-status
  questions (already flagged by a prior pass) remain open; `coe.int`
  staying blocked means the Council of Europe's own chart of ratifications
  still cannot be checked directly.
- The five entities that stayed `search-only` above would all benefit from
  one more successfully-read source apiece — they are one source short of
  a majority in three of the five cases (COE 1/5 with substitute, OECD 1/3
  with substitute, Convention-108-Protocol 1/3), not zero.
- ISO/IEC JTC 1 itself remains unmodelled (flagged by a prior pass on
  [[INTL-IEC]]); this pass did not change that assessment.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see this batch's completion report for results.

## UN bodies cluster re-verification (2026-08-28)
Re-verified all 20 assigned UN-scope entities (organisations, programmes,
frameworks, standards, legislation, a platform, a policy and a strategy —
everything under UN organs, UNECE subsidiaries, UNESCO's AI ethics
instrument, UN-GGIM and its European committee, and the 2030 Agenda/SDG
indicator chain). **17 of 20 promoted to `verification: primary-source`.**
Three stayed at `search-only`: [[UN-CES]], [[UN-EDIFACT]] and
[[UN-UNCTAD]] — in each case fewer than half of the entity's cited sources
could be genuinely read even after seeking alternates, so they were left
honestly unpromoted rather than forced across the line.
**A domain-wide finding, the same shape as the `digitaleoverheid.nl` block
prior batches hit**: `unece.org` is **broadly 403-blocked this session** —
confirmed by testing the bare root domain (`unece.org/`), which itself
403s, not just the specific deep-linked pages originally cited. This
affected [[UN-AARHUS]], [[UN-CEFACT]], [[UN-UNECE]], [[UN-CES]],
[[UN-EDIFACT]] and [[UN-LOCODE]]'s originally-cited sources — six of this
batch's twenty entities. `unctad.org` showed the same pattern for
[[UN-UNCTAD]] (three different pages on the domain all 403'd, not just the
one cited). Per this batch's instruction, alternates were sought and
substituted where they could be found and genuinely read: Wikipedia (UNECE,
UN/CEFACT, UN/LOCODE, EDIFACT, Aarhus Convention, UN Statistical
Commission, ITU), the OSCE Aarhus Centres' page, `legislation.gov.uk`'s
retained-EU-law mirror of Regulation (EU) 2019/1239 (used in place of a
`eur-lex.europa.eu` fetch that returned empty content on every attempt),
`service-architecture.com` and Nigeria's NEPC trade-agency page (both for
UN/CEFACT), and CEPAL's own page (for UN-GGIM's exact founding date). This
closed six of those seven entities to a genuine majority; only
[[UN-EDIFACT]] and [[UN-CES]] (of the `unece.org`-affected group, alongside
[[UN-UNCTAD]]) could not find enough alternates to cross 50%.
**Two entities were substantively rebuilt on real primary sources this
pass, not just re-confirmed:**
- [[UN-DATA-COMMONS]]'s sole prior citation was a Grokipedia page (already
  flagged as the weakest citation in the Atlas) that now also 403s. A
  targeted search located `un.org/en/desa/un-data-commons-for-the-sdgs` — a
  dedicated UN DESA page for this exact platform that had simply never
  been found in the original research, not a page that became newly
  available. It and Google's own blog announcement of the September 2024
  expansion are both read directly. This also corrected the launch date:
  the platform launched **4 October 2023** (at the SDG Summit, with
  Google.org), and the September 2024 event the prior text described as
  "the" launch was actually a later expansion to add WHO, ILO and UNICEF.
  `confidence` moves from `low` to `medium`.
- [[UN-DATA-STRATEGY]]'s sole prior citation was the UN 2.0 quintet PDF,
  which never actually named the strategy — a documented placeholder, not
  a broken link. Two dedicated `un.org/en/content/datastrategy` pages were
  found and read directly, confirming the strategy's real title ("...for
  Action by Everyone, Everywhere, with Insight, Impact and Integrity"), its
  eight priority areas, and — genuinely correcting the prior framing — that
  it was approved around **April 2020**, three years *before* [[UN-2-0]]'s
  September 2023 policy brief. The strategy predates and is drawn upon by
  UN 2.0's data capability; it was not produced by or for UN 2.0, as the
  prior wording could be read to imply.
**Other genuine corrections and new facts, not just confirmations:**
- [[UN-GGIM]]'s `start_date` moves from the `2011-07-01` placeholder to the
  confirmed **2011-07-27**: CEPAL's own page (a UN regional commission,
  read directly) names ECOSOC resolution 2011/24 and the exact date. This
  is a genuine sourced correction, not a fabrication — the source itself
  gives the day, unlike the UN anchor entity's own founding date, which
  stays `null` because its source gives only a year.
- [[UN-UNSC]]'s founding year is **genuinely disputed across sources read
  this pass**: un.org/DESA's own page says 1947; Wikipedia and a WebSearch
  cross-check (Resolution 8(I)) say 1946, matching this entity's existing
  `start_date`. Left open rather than silently resolved either way —
  flagged in the entity's own body for whoever next has time to find the
  resolution text itself.
- [[UN-2-0]]'s previously-flagged "2021/09 file path vs. September 2023
  policy brief" oddity is resolved: un.org's *current* URL for the same
  policy brief sits under a `2023-09` path (found via WebSearch); the
  originally-cited `2021/09` PDF was simply a stale/different path, not
  evidence the quintet framing predates the brief.
- [[UN-CEFACT]]: Wikipedia (read directly) adds a founding year — 1996 —
  not previously recorded. Per the no-date-fabrication discipline, this is
  recorded in prose only; `start_date` stays `null` rather than being
  padded to `1996-01-01`.
- [[UN-GGIM-EUROPE]]'s own "About Us" page (read directly) states in its
  own words that it "is supported by EuroGeographics" and is headquartered
  in Brussels — the clearest first-party confirmation yet of a connection
  the entity's body had previously only inferred from a third-party
  conference presentation. EuroGeographics itself is still not created as
  an entity (outside this UN-cluster pass's scope), but the case for it is
  now stronger.
- [[UN-AI-ETHICS-RECOMMENDATION]]: two specific figures in the original
  description — "nearly thirty countries" using the Recommendation for
  national legislation, and the Global Forum being "hosted by Czechia and
  later Slovenia" — were **not** found on any UNESCO page read this pass.
  They are carried forward explicitly labelled as unconfirmed rather than
  silently repeated as verified.
- [[UN-AARHUS]]: a WebSearch surfaced a conflicting party count (47 Parties
  as of March 2025, vs. the entity's existing 49 Parties/April 2023) from
  search-snippet text only, not a directly-read primary page. The existing
  49/April-2023 figure is kept because it was the one actually confirmed by
  a direct fetch (Wikipedia); the possible more-recent 47 figure is noted
  in the entity's body for whoever next revisits it.
**Relationship-directionality check**: confirmed correct on all six
UNECE-subsidiary entities — [[UN-CEFACT]], [[UN-EDIFACT]] and [[UN-LOCODE]]
all carry `maintained-by`/`part-of` pointing at [[UN-UNECE]] (not the
reverse), [[UN-CES]] carries `part-of` [[UN-UNECE]], [[UN-AARHUS]] carries
`maintained-by` [[UN-UNECE]], and [[UN-GGIM-EUROPE]] carries `part-of`
[[UN-GGIM]]. No corrections needed here — the prior batches had already
modelled these correctly.
`international/un/index.md` was rewritten to reflect these results (freer
edit, per this batch's brief, since no sibling agent touches the UN
cluster this pass) — verification status and key dates are now annotated
per entity, and two new cross-level chains (UN-AARHUS → EU environmental
directive → six countries; UN-CEFACT → UN-LOCODE → EU-EMSWE) are shown
alongside the still-open statistics gap.
All three validation commands (`validation/run_all.py`,
`tools/build_graph.py`, `tools/test_build_graph.py`) were run after these
changes; see this batch's own completion report for results.

## Final verification-gap tail (2026-08-28)

The last 24 (of an original batch touching 25 files) entities remaining at
`verification: search-only` or unverified were re-checked in one pass, with
genuine fetch attempts against every cited source and honest promotion only
on a real majority read. 23 of 25 files were promoted to `primary-source`;
two stay honestly at `search-only`.

**Promoted this pass:**
- The eight non-European Convention 108 country anchors — [[AR]], [[CV]],
  [[MA]], [[MU]], [[MX]], [[SN]], [[TN]], [[UY]] — each by finding one new,
  genuinely readable source corroborating that country's own accession: the
  country's own government press release, its own data protection
  authority, or its own national press, in every case reaching 2 of 3
  sources read directly. Uruguay's is the strongest — its own regulator,
  the URCDP, independently confirming in its own words the "first
  non-European state" claim this Atlas previously carried unconfirmed.
- [[BE-BOSA]] and [[BE-DATA-GOV-BE]] — the confirmed CAPTCHA-walled
  `belgium.be`/`data.gov.be` domains were not re-attempted; instead the
  European Commission's own Interoperable Europe governance page, GitHub's
  Fedict organisation (a second repository, `Fedict/dcat`, plus the org's
  full repository listing), and an independent Drupal.org case study and
  lexgo.be legal-news article supplied enough new, genuinely-read material
  to cross a majority for both entities.
- [[FR-DGSI]] — Légifrance served DGSI's own founding decree (n° 2014-445)
  in full readable text, and the Sénat's own 2022-2023 intelligence
  oversight report gave independent budget/leadership corroboration.
  `interieur.gouv.fr` and DGSI's own site remain genuinely 403-blocked, but
  neither Légifrance nor the Sénat are part of that family.
- [[NL-WBNI]] — `wetten.overheid.nl`'s BWBR0041515 is the Wbni's own
  official text, resolving the entity's core problem (no source on the
  Wbni itself, only on its successor) in one fetch.
- [[NL-BASISREGISTRATIES]] — `web.archive.org` (this file's own flagged
  next step) turned out to be unreachable by this environment's tool at
  all, not merely slow or content-blocked; `rijksoverheid.nl` and
  Logius's own "Stelselvoorzieningen" page supplied the extra sources
  instead, breaking the exact-50% tie the entity was honestly left at.
- [[NL-DSGO]] and [[NL-HEALTH-RI]] — both genuinely first-pass
  verifications (never previously fetched). 3 of 4 and 3 of 3 sources read
  directly respectively. NL-DSGO's flagged "is the 18 June launch date
  actually 2024?" inference is now resolved: VNG's own article states the
  programme "is in 2021 gestart en is in juni 2024 geëindigd," confirming
  the year directly.
- [[EU-GEANT]] — a European Commission GN4-3N project success-story page
  gave substantial new, directly-read funding and scale detail (€50.5M EU
  funding, 14→40 country coverage, three exabytes/year), breaking the
  previous 3-of-6 tie.
- [[EU-SDG]] — the European Parliament's own Legislative Observatory
  (OEIL) worked where EUR-Lex would not, plus `legislation.gov.uk`'s
  retained-EU-law text of the regulation itself and the European
  Commission's own account of the Once-Only Technical System (resolving a
  previously-unconfirmed lead into a confirmed fact).
- [[INTL-COE]] — a second, distinct Wikipedia article ("Member states of
  the Council of Europe"), the EU's own EEAS page on its CoE relationship,
  the UK government's own CoE-delegation page, and a Georgetown Law
  Library research guide together gave a genuine majority, despite
  `coe.int` remaining domain-wide blocked throughout.
- [[INTL-CONVENTION-108]] and [[INTL-CONVENTION-108-PLUS]] — neither
  `coe.int`/`rm.coe.int` nor `web.archive.org` were reachable, so four to
  five independent legal/compliance explainer sources each (Georgetown Law
  Library, Wrangu, Ambit Compliance, Reed Smith for the base Convention;
  itpatagonia.com, Völkerrechtsblog, University of Namur, CIGI for the
  amending protocol) were used instead, each converging on the same
  custodianship and substantive facts the Atlas already carried.
- [[INTL-OECD]] — `oecd.org` (the main site) is domain-wide blocked, but a
  *different* OECD subdomain, `legalinstruments.oecd.org`, is not: its HTML
  page for OECD-LEGAL-0463 (the Council's own Recommendation on Enhancing
  Access to and Sharing of Data) was read directly in full, the first
  OECD-authored primary text this entity has ever carried. Belgium's
  foreign ministry's own OECD profile page supplied a second independent
  source.
- [[UN-CES]] — `unece.org` stayed blocked, but Bulgaria's National
  Statistical Institute (reporting its own CES attendance), a UK press
  item on a CES-adjacent UK-Eurostat cooperation signing, and the UN's own
  Indico event system (a UNOG-run domain distinct from `unece.org`)
  together gave a genuine majority.
- [[UN-EDIFACT]] — two independent EDI-industry pages (commport.com,
  edibasics.com) confirm UN/CEFACT's maintainer role in near-identical
  wording to each other (disclosed honestly as likely both echoing
  UNECE's own text, rather than hidden as three independent
  confirmations), pushing 1-of-3 to 3-of-5.

**Stayed at `search-only`, honestly, after genuine additional effort:**
- [[INTL-CONVENTION-108-PROTOCOL]] — one new source (an independent IT-law
  blog, mbkaya.com, quoting the Protocol's own preamble) was found and
  read, moving this entity from 1-of-3 to 2-of-4 — exactly the borderline
  the discipline calls out, not a majority. Two further candidates failed
  (IT Law Wiki/Fandom: HTTP 402 paywall; NADPA-RAPDP: HTTP 503). Left
  `search-only` rather than forced across a 50/50 split.
- [[UN-UNCTAD]] — `unctad.org` remains broadly blocked (three separate
  pages tried, all 403) and the UNSCEB PDF still 404s. Three general,
  independent sources were found and read directly this pass (Wikipedia,
  a Chinese diplomatic mission's UNCTAD page, an exam-prep site's UNCTAD
  overview), each confirming UNCTAD's general existence and founding — but
  **none mentions the specific fact this entity exists to record**, that
  UNCTAD's Commission on Science and Technology for Development hosts a
  working group on data governance. `sdg.iisd.org` and `dig.watch`, tried
  specifically for that claim, both 403'd. Promoting `verification` on
  generic corroboration while the substantive claim stays unconfirmed
  would be a hollow majority, so this entity is deliberately left at
  `search-only` — a case where source-count arithmetic and honest
  verification pull in different directions, and honesty wins.

**A tool-level finding, not a content finding, worth recording for future
passes**: `web.archive.org` / the Wayback Machine cannot be reached at all
by this environment's WebFetch tool this session — every attempt (multiple
distinct URLs, multiple entities, both a specific-snapshot pattern and a
CDX-style query) returned "Claude Code is unable to fetch from
web.archive.org" rather than any content-level response. This is different
from every other block recorded in this Atlas's research history, which are
all site-side (403, CAPTCHA, JS challenge, 404). Every entity in this pass
that was pointed at archive.org as a next step (NL-BASISREGISTRATIES,
EU-GEANT, INTL-COE, the Convention 108 family, INTL-OECD, UN-CES,
UN-EDIFACT, UN-UNCTAD) hit this same tool-level wall and had to be resolved
via alternate live sources instead. A future pass with a working
archive.org path could still be worth trying against the specific pages
this pass could not otherwise unblock (the three `digitaleoverheid.nl`
pages on NL-BASISREGISTRATIES, and the `coe.int` pages on the Convention
108 family), even though this pass reached a genuine majority for most of
them by other means.

All three validation commands (`validation/run_all.py`, `tools/build_graph.py`,
`tools/test_build_graph.py`) were run after these changes; see the final
summary for this pass for results.
