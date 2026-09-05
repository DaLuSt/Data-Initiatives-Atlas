# Research Queue

> **This is a list of open work.** Items are removed when they close — the
> record of what was closed, and why, lives in `progress/completed.md` and on
> the entities themselves. Nothing here is struck through, because struck-out
> rows made the queue longer every time it got shorter.
>
> **Largest open items:** the Comunidades Autónomas, the sixteen Land
> INSPIRE transposition acts and the sixteen Land data protection
> authorities — all unblocked (`level: subnational`) and unstarted,
> each large enough to warrant its own dedicated pass. DKE closed
> 2026-09-04, along with OSLO/Digitaal Vlaanderen — see the pickups
> below. [[PL-PESEL]], Poland's population register, is
> modelled as of 2026-08-22 — the second research-queue pickup.
> **2026-08-30 pickup (sixth):** closed six items in one pass — see
> `progress/completed.md`-style detail preserved in git history.
> **2026-09-04 pickup (seventh):** closed five items and narrowed a sixth —
> two new German entities, [[DE-FIM]] (closing a gap [[DE-FITKO]]'s own
> file explicitly declined to close) and [[DE-BMV]] (resolving the
> BMDV/BMV/BMDS naming split flagged on [[DE-MOBILITHEK]]), plus a prose
> note on BMWK's rename to BMWE; a new [[NL-DIGIMELDING]] entity, one of
> the Stelsel van Basisregistraties' four system facilities; and
> [[PL-MOBYWATEL]]'s eIDAS2 relationship, upgraded from press-reporting-only
> to a directly-read Ministry of Digital Affairs statement that corrects
> the framing from "incompatible failure" to "parallel purpose-built app."
> Estonia's Open Data Directive transposition was narrowed to a specific,
> dated candidate instrument but not closed — every direct-fetch attempt
> failed. Two further queue rows were found already closed and removed as
> housekeeping: the operator of [[PL-DANE-GOV-PL]] (resolved 2026-08-27).
> **2026-09-04 pickup (eighth):** closed three more items. A full refresh
> of `domains/domain-cybersecurity.md` — stale since the Netherlands/Poland
> gap it recorded had already closed — found the domain had nearly tripled
> in scope unnoticed, from six countries to fourteen, and corrected a
> genuine error along the way: the page had Poland "before the CJEU" for
> its NIS2 delay, but the primary source names **Ireland**, not Poland, as
> the state actually referred. A new [[AT-EGOVG]] entity closed the
> Austrian identity-legislation gap, and reading all four candidate
> statutes directly on `ris.bka.gv.at` found a narrower story than the
> queue recorded — one statute grants the E-ID function, not four. A new
> [[IT-CIE]] entity closed Italy's CIE/CNS gap the same way: one CAD
> article creates both credentials, so one entity, not two.
> **2026-09-04 pickup (ninth):** closed Spain's Ley 39/2015 and 40/2015
> legal-basis gap with two new entities. [[ES-LEY-40-2015]] turned out to
> govern two Spanish agencies, not one: reading [[ES-AEAD]]'s and
> [[ES-AESIA]]'s own founding decrees directly found both are the same
> "agencia estatal" legal form under this one law, cited by different
> article ranges. The Spanish AI organic law was sharpened rather than
> closed: it is now a Proyecto de Ley before Congress with a BOCG
> citation, but government and legal-sector sources still disagree on
> which body holds authority — [[ES-AESIA]] alone, or a separate
> General Directorate of AI plus eight market-surveillance authorities —
> so no entity was created, the same discipline [[FR-NIS2-LOI]] set.
> **2026-09-04 pickup (tenth):** closed Belgium's entire Regions cluster
> in one pass, the largest single ontology-driven gap the Atlas had
> recorded. Four new entities — [[BE-DIGITAAL-VLAANDEREN]] (Flanders),
> [[BE-AGENCE-NUMERIQUE]] (Wallonia), [[BE-PARADIGM]] (Brussels-Capital,
> formerly CIRB/CIBG since 1987) and [[BE-OSLO]], the Flemish semantic-
> interoperability standard Digitaal Vlaanderen maintains — close what
> `discovery/unresolved.md` had called "the Atlas's best-evidenced
> ontology defect" before `level: subnational` resolved it on
> 2026-08-21. Also created [[BE-STATISTIEKWET-1962]], closing the
> "Belgian statistics act" gap [[BE-STATBEL]]'s own file had deliberately
> deferred, with a `governed-by` edge added. `countries/be/be.md` and
> `countries/be/index.md` had two separate stale claims corrected: one
> banner still said no Belgian Region was modelled, and the anchor's own
> "no sub-national level was invented" line was three weeks out of date.
> **2026-09-04 pickup (eleventh):** closed three more Poland items —
> [[PL-KRI]] (Krajowe Ramy Interoperacyjności, the sixth national
> interoperability framework with no sourced [[EU-EIF]] descent),
> [[PL-DCAT-AP-PL]] (a fifth national DCAT-AP child) and
> [[PL-USTAWA-STATYSTYCE-1995]] (closing [[PL-GUS]]'s legal-basis gap
> with a `governed-by` edge, the same pattern just used on
> [[BE-STATBEL]]). **CSIRT MON and GIODO remain queued** — both are
> genuinely blocked, not under-researched: CSIRT MON's parent ministry
> is not an Atlas entity, and GIODO's own site returns a DNS failure.
> **2026-09-04 pickup (twelfth):** closed France's four remaining
> "référentiels" items in one pass. [[FR-ORDONNANCE-2005-1516]] closes
> [[FR-RGI]]'s own legal-basis gap and turned out, on a direct read of
> its implementing decree, to also found [[FR-RGS]] — one ordinance,
> two référentiels, at different articles. [[FR-RGS]] itself is
> co-maintained by [[FR-DINUM]] and [[FR-ANSSI]] "en co-construction,"
> in ANSSI's own words. [[FR-RGAA]] rests on a different legal parent
> (the 2005 disability-rights law) but the same DINUM stewardship.
> [[FR-ORDONNANCE-2010-1232]] closes [[EU-INSPIRE]]'s "ordonnance number
> unestablished" gap for France. Also found: `legifrance.gouv.fr`,
> recorded as genuinely bot-walled in the 2026-08-26 France
> re-verification pass, answered two direct fetches normally this pass
> — noted as a correction on `countries/fr/index.md` rather than quietly
> overwritten. "France Identité" was removed as a closed decision
> (recorded in prose on [[FR-FRANCECONNECT]] already; nothing further to
> research).
> **2026-09-04 pickup (thirteenth):** closed [[DE-DKE]], one of
> Germany's largest remaining gaps — the electrotechnical-standards
> counterpart to [[DE-DIN]], founded 1970 as a joint DIN/VDE body,
> Germany's national member in [[EU-CENELEC]], IEC and (for
> telecommunications) ETSI. Also reclassified two large Germany items —
> the sixteen Land INSPIRE transposition acts and the sixteen Land data
> protection authorities — from `Blocked` to `Next`: both were blocked
> on the `level` ontology question, resolved 2026-08-21 by
> `level: subnational`, but the finding was never carried back to these
> rows until now. Neither was picked up this pass; both are large enough
> to warrant their own dedicated batch, the same treatment given the
> Comunidades Autónomas.
> **2026-09-04 pickup (fourteenth):** closed seven Netherlands
> "Other queued research" items in one pass, mostly Batch 1/2 vintage.
> [[NL-CIO-RIJK]] and [[NL-ACICT]] are both now entities;
> [[NL-VNG-REALISATIE]] closes a double-need — its own row and
> [[NL-GEMMA]]'s `maintained-by` simplification, now re-pointed.
> [[NL-WATERSCHAPSHUIS]] and [[NL-SIDN]] close two more. [[NL-CCS]]
> turned out to be a genuine correction rather than a simple gap: reading
> the actual 2015 abolition bill directly found the CCS was not merely
> unmodelled but **abolished** on 1 January 2017, so it is recorded
> `status: superseded` rather than active. The long-open "which ministry
> oversees CBS" naming question is closed in prose on [[NL-CBS]]
> (Ministerie van Economische Zaken en Klimaat, confirmed via
> `organisaties.overheid.nl`) without creating a ministry entity.
> **2026-09-04 pickup (fifteenth):** closed a further six Netherlands
> items, four of them Batch 2 vintage. [[NL-DANS]], [[NL-RIVM]] and
> [[NL-NWO]] are now entities — NWO's own site names it the joint parent
> of DANS, closing that pairing in one pass. [[NL-EDUSTANDAARD]] closes
> the gap [[NL-ROSA]]'s own file had already sourced but left
> unasserted for want of the entity. Two rows turned out to be stale
> housekeeping rather than open research: the "10 individual
> basisregistraties" (both duplicate rows) were already fully
> enumerated on [[NL-BASISREGISTRATIES]]'s own `related_entities`, and
> `DOMAIN-HEALTH`/`DOMAIN-EDUCATION` already exist and are in active use
> — both removed without new entities.
> **2026-09-04 pickup (sixteenth):** closed three more Netherlands
> items and narrowed a fourth. [[NL-DIGIGO]] closes the gap [[NL-DSGO]]'s
> own file had already sourced but could not turn into an edge; the
> `produces` edge lives on [[NL-DIGIGO]]'s side, per the Atlas's
> no-stored-inverse convention. [[NL-ENSIA]] closes the accountability-
> system gap paired with [[NL-BIO]]. The Programmaraad turned out to be
> Geonovum's own internal governance body, not a separate organisation —
> closed as a non-entity finding on [[NL-GEONOVUM]]'s own file rather
> than modelled. Topsector Logistiek was narrowed, not closed: iSHARE's
> own official history page does not corroborate the secondary sources'
> attribution to it, and the programme itself is too broad a policy
> initiative to model accurately in this pass.
>
> **2026-09-05 pickup (seventeenth):** closed two more Netherlands items.
> [[NL-WILMA]] completes the NORA reference-architecture family for the
> water authorities, `based-on` [[NL-NORA]], confirmed on NORA's own wiki
> page; [[NL-NORA]]'s own family table and prose were updated to reflect
> all three sourced descendants (GEMMA, ROSA, WILMA). [[NL-NOIV]] — the
> historical Nederland Open in Verbinding action plan and programme office
> (2007–2011) — closes the "BOMOS custody" question's historical half:
> reading BOMOS's own founding PDF directly shows NOiV's programmabureau,
> not just the 2006 Forum Standaardisatie working group, convened the
> community that produced BOMOS version 1; [[NL-BOMOS]]'s own file was
> updated with that finding.
>
> **2026-09-05 pickup (eighteenth):** closed the Netherlands' CER
> transposition and its coordinating authority in one pass.
> [[NL-WWKE]] (Wet weerbaarheid kritieke entiteiten) mirrors [[NL-CBW]]'s
> own pattern exactly — same 15 April 2026 Tweede Kamer approval, same
> 15 August 2026 entry into force, `implements-requirement-from`
> [[EU-CER]] — confirmed by reading `nctv.nl`'s and `rijksoverheid.nl`'s
> own pages directly. [[NL-NCTV]] closes the other half of the "NCSC /
> NCTV" row: [[NL-NCSC]] was already modelled, and NCTV — the Ministry of
> Justice and Security's counter-terrorism/cybersecurity/national-security
> coordinator — is now an entity in its own right, with a `part-of`
> [[NL]] anchor edge since no Ministry-of-Justice-and-Security entity
> exists yet to carry a more specific one.
>
> **2026-09-05 pickup (nineteenth):** created
> [[EU-INTEROPERABLE-EUROPE-BOARD]], closing two duplicate queue rows.
> Reading the Board's own governance page on
> `interoperable-europe.ec.europa.eu` directly confirms it is
> `governed-by` [[EU-INTEROPERABLE-EUROPE-ACT]] and `influences`
> [[EU-EIF]] — shaping the framework's next revision is one of its stated
> tasks. This **partially** answers the EIF/Act relationship both of
> those entities' own files had flagged as open: it tells us the Board
> works on the EIF's revision, not whether the Act gives the EIF itself
> legal force, which stays open and queued.
>
> **The `level` vocabulary is no longer a blocker.** `level: subnational` was
> added 2026-08-21 and the three Belgian sub-federal ODD instruments are
> modelled under it. OSLO/Digitaal Vlaanderen and the Comunidades Autónomas
> became ordinary research the same day. `level: local` remains unused and
> still gates the Dutch municipalities, which is a different question — what
> to create, not what to call it.
>
> **No longer blocked on egress — but not every host cooperates.** Outbound
> HTTPS opened 2026-08-21 and `tools/reverify.py` read its first live pages,
> moving 21 entities to `verification: primary-source` (batch 1). 414 of 516
> entities remain `search-only`/`unverified`. `eur-lex.europa.eu`,
> `www.iso.org`, `www.coe.int` and `unece.org` answer every automated fetch
> with a bot-defense challenge page rather than content — an environment
> hard limit independent of the egress policy — so skip entities citing only
> those hosts. See `docs/re-verification.md` §"A machine-corroborated pass"
> and `discovery/reverification-allowlist.md` for the rest.

Confirmed-relevant areas that are known to need research but haven't been
worked yet, beyond the batch plan itself (`progress/backlog.md`). Use this
for gaps discovered mid-batch that fall outside the current batch's scope,
so they aren't lost.

**See also `discovery/reverification-allowlist.md`** — the generated list of
every host the Atlas cites, which is the worklist for the re-verification
pass and the allowlist to request if outbound HTTPS is restricted.

---

## Batch 1 — Netherlands: Core Data Governance (re-verified 2026-08-21)

Batch 1 was completed on 2026-08-14 from search-engine results only, then
link-checked by hand on 2026-08-20, then content-verified with pages
actually read on 2026-08-21 once outbound HTTPS opened. All twelve core
entities (Forum Standaardisatie, IBDS, FDS, NORA, Common Ground, MIDO, BZK,
VNG, ICTU, OBDO, GDI, Pas toe of leg uit) carry `verification:
primary-source`. What follows is what the 2026-08-21 pass actually found,
per area — kept rather than deleted wholesale, because two of the open
questions it closed turned into real corrections.

**IBDS/FDS — closed, with a status correction.** The exact presentation
date to the Tweede Kamer (18 November 2021) is now confirmed on two
independent sources. The IBDS→FDS relationship moved from an Atlas
interpretation to a sourced fact: noraonline.nl states the IBDS develops
the FDS directly. **The February 2026 OBDO adoption of the Afsprakenstelsel
Federatief Datastelsel — previously an unconfirmed search result — is now
confirmed on digitaleoverheid.nl**, and [[NL-FDS]]'s `status` has been
corrected from `planned` to `active` accordingly. FDS's typing
(`framework` vs `initiative`) stays genuinely open: noraonline.nl attests
both readings on the same page.

**NORA — closed, and answered a separately-flagged high-value question.**
BZK-as-owner and ICTU-as-manager are now confirmed a second time via
Kamerstuk 26643-128 (the 2008 Kabinetsbesluit inzake ICT), which also
answered `discovery/unresolved.md`'s "is NORA the Dutch NIF" question:
[[NL-NORA]] now carries `based-on` → [[EU-EIF]], sourced to that decree,
scoped narrowly to the cross-border-interoperability portion of NORA rather
than a blanket NIF designation.

**MIDO/OBDO — closed, with a placeholder date corrected.** The two
"Additional sources" Staatscourant items below turned out to be exactly
what they were suspected to be: Stcrt. 2018, 9728 is [[NL-OBDO]]'s founding
Instellingsbesluit (19 January 2018, now `start_date`); Stcrt. 2022, 18861
is the 2022 amendment introducing MIDO's multi-year programming, so
[[NL-MIDO]]'s `start_date` moved from a `2022-01-01` placeholder to the
decree's actual signing date, **12 July 2022**. Two sources cited on
2026-08-20 (a digitaleoverheid.nl OBDO dossier page, and the "Voortgang
MIDO" timeline page) now 404 — the site was reorganised sometime after the
link check. No replacement URLs were found; both entities remain fully
corroborated by their other sources.

**Common Ground — attempted, not closed.** vng.nl returned `403 Forbidden`
to every fetch attempt during this pass (`Request forbidden by
administrative rules`) — a rate-limit or bot-defense response distinct from
the four hosts known to be permanently bot-walled (see the top of this
file), since one vng.nl path answered normally earlier in the same session
before the block kicked in. Common Ground's current programme status and
its typing (`initiative` vs `framework`/`programme`) remain open; retry
vng.nl on a future pass, ideally spaced out rather than in a burst.

Find all affected entities with: `grep -rl "verification: search-only" .`

### Forum Standaardisatie / open standards

| Candidate source | URL | Verified? |
|---|---|---|
| Lijst open standaarden | https://www.forumstandaardisatie.nl/open-standaarden | ✅ 2026-08-20 |
| 'Pas toe of leg uit'-standaarden (verplicht) | https://www.forumstandaardisatie.nl/open-standaarden/verplicht | ✅ 2026-08-20 |
| 'Pas toe of leg uit'-beleid | https://www.forumstandaardisatie.nl/pas-toe-leg-uit-beleid | ✅ 2026-08-20 |
| Toetsingsprocedure en criteria voor de lijst open standaarden | https://www.forumstandaardisatie.nl/toetsingsprocedure-en-criteria-voor-de-lijst-open-standaarden | ✅ 2026-08-20 |
| Open Standaarden (Digitale Overheid) | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/open-standaarden/ | ✅ 2026-08-20 |

### Interbestuurlijke Datastrategie (IBDS) / Federatief Datastelsel (FDS)

| Candidate source | URL | Verified? |
|---|---|---|
| Interbestuurlijke Datastrategie (IBDS) — Digitale Overheid | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/data/interbestuurlijke-datastrategie/ | ✅ 2026-08-20 |
| Interbestuurlijke Datastrategie (IBDS) — NORA Online | https://www.noraonline.nl/wiki/Interbestuurlijke_Datastrategie_(IBDS) | ✅ 2026-08-20 |
| Realisatie IBDS — Digitale Overheid | https://www.digitaleoverheid.nl/community/realisatie-ibds/ | ✅ 2026-08-20 |
| Beleidsevaluatie Interbestuurlijke Datastrategie — Eindrapport (open.overheid.nl) | https://open.overheid.nl/documenten/1edd5ed4-98e8-442e-bcd2-f6ec3f27a754/file | ✅ 2026-08-20 |
| IBDS / Federatief Datastelsel presentatie (Forum Standaardisatie, Dag van de Interoperabiliteit 2024) | https://www.forumstandaardisatie.nl/sites/default/files/BFS/8-Bijeenkomsten/20241015-Dag-van-de-interoperabiliteit/presentaties/Presentatie-Federatief-Datastelsel-en-resultaten-Mentimeter.pdf | ✅ 2026-08-20 |

✅ Resolved 2026-08-21: presentation date (18 November 2021), current status
(active, per the 2026 evaluation report), and the Afsprakenstelsel's
February 2026 adoption — see the summary above and [[NL-IBDS]] / [[NL-FDS]].
**Still open:** whether FDS is best typed as `framework`, `initiative` or
`programme` — noraonline.nl attests both readings on the same page.

### NORA

| Candidate source | URL | Verified? |
|---|---|---|
| NORA Online — Positionering NORA | https://www.noraonline.nl/wiki/Positionering_NORA | ✅ 2026-08-20 |
| NORA — Digitale Overheid | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/ | ✅ 2026-08-20 |
| Overheidsarchitectuur NORA — ICTU | https://www.ictu.nl/diensten/dienstenoverzicht/overheidsarchitectuur-nora/ | ✅ 2026-08-20 |
| Architectuur Digitale Overheid — NORA Online | https://www.noraonline.nl/wiki/Architectuur_Digitale_Overheid | ✅ 2026-08-20 |

✅ Resolved 2026-08-21: BZK-opdrachtgever and ICTU-beheerder confirmed a
second time via Kamerstuk 26643-128, which also answered the separately
flagged EU-EIF → NORA question — see the summary above and [[NL-NORA]].
**Still open:** NORA's current version number, and NORA's formal relationship
to GEMMA/EAR/ROSA/PETRA (only GEMMA carries a sourced `based-on` link).

### Common Ground

| Candidate source | URL | Verified? |
|---|---|---|
| Common Ground — VNG | https://vng.nl/onderwerpen/common-ground | ✅ 2026-08-20 |
| Programma Common Ground — VNG | https://vng.nl/projecten/programma-common-ground | ✅ 2026-08-20 |
| Realisatiekoers Common Ground Informatiesamenleving (21 mei 2025) | https://vng.nl/sites/default/files/2025-05/20250521-08b-realisatiekoers-common-ground.pdf | ✅ 2026-08-20 |

**Still open — vng.nl blocked this pass** (see summary above): current
programme status; whether Common Ground is best typed as `initiative`,
`framework` or `programme`; its formal relationship to GEMMA and to the FDS.

### MIDO (Meerjarenprogramma Infrastructuur Digitale Overheid)

| Candidate source | URL | Verified? |
|---|---|---|
| Wat is het MIDO? | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/wat-is-het-mido/ | ✅ 2026-08-20 |
| Governance MIDO | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/governance/ | ✅ 2026-08-20 |
| Kabinetsbeleid MIDO | https://www.digitaleoverheid.nl/mido/kabinetsbeleid/ | ✅ 2026-08-20 |
| Voortgang MIDO (tijdlijn) | https://www.digitaleoverheid.nl/mido/voortgang-mido/ | ✅ 2026-08-20 |
| Sturing van de ontwikkeling van de digitale overheid — NORA Online | https://www.noraonline.nl/wiki/Sturing_van_de_ontwikkeling_van_de_digitale_overheid | ✅ 2026-08-20 |

✅ Resolved 2026-08-21: MIDO's precise start date (12 July 2022, not just
"2022") and its legal basis in the OBDO's amended Instellingsbesluit — see
the summary above and [[NL-MIDO]]. The office-holder question is **closed
by decision**: the Atlas deliberately does not model who currently holds the
bewindspersoon role (see `discovery/unresolved.md`). The relationship
between MIDO, the GDI and the Meerjarenvisie Digitale Overheid is recorded
in [[NL-MIDO]]'s body as three components of the same programme.

All candidate sources this batch located are now on their target entities'
frontmatter (checked 2026-08-21): [[NL-OBDO]], [[NL-FORUM-STANDAARDISATIE]]
and [[NL-ICTU]] cite them and are `primary-source`; [[NL-LOGIUS]],
[[NL-DATA-AGENDA-OVERHEID]] and [[NL-DIGIBETER]] cite them too but are
still `search-only` — reading those three is a re-verification task for a
future pass, not a source-discovery one, so it belongs in
`discovery/reverification-allowlist.md`'s worklist rather than here.

---

## Germany — queued from the second-country batch (2026-08-15)

Every German entity in the Atlas is `verification: search-only`. The items
below are things **not created**, with the reason. Nothing here was omitted
by accident.

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| The sixteen Land INSPIRE transposition acts | Jointly with [[DE-GEOZG]] they constitute Germany's transposition. **No longer blocked**: `level: subnational` was added 2026-08-21. Sixteen is a large batch — like the Comunidades Autónomas, a candidate for its own dedicated pass rather than a quick pickup | Next | Germany batch; unblocked 2026-08-21, noted 2026-09-04 |
| Land data protection authorities | [[DE-BFDI]] covers federal bodies only; sixteen Land authorities cover the rest. **No longer blocked**: same `level: subnational` resolution. Also a large batch | Next | Germany batch; unblocked 2026-08-21, noted 2026-09-04 |
| Individual XÖV standards | XPersonenstand, XMeld, XBau, XPlanung and others. Only [[DE-XRECHNUNG]] is modelled. Creating one entity per standard would inflate the layer without adding structure (brief §1) | Later | Germany batch |
| National Gaia-X hubs | Germany's and Austria's hubs are cited as sources on [[EU-GAIA-X]]. A `DE-GAIA-X-HUB` would be a legitimate national entity, not a duplicate — but nothing beyond website existence was established | Later | Germany batch |
| Mobility Data Marketplace (MDM) | Replaced by [[DE-MOBILITHEK]] as National Access Point. **No superseded entity created** — unlike [[DE-IWG]], nothing beyond the replacement is established | Later | Germany batch |
| Bundesdruckerei; ITZBund | Federal printing/eID body and the federal IT service centre. ITZBund is already cited as a source on [[DE-XOEV]] | Later | Germany batch |
| OZG-Änderungsgesetz | A substantial amending act, deliberately **not** given its own entity — doing so would force the same `supersedes` compromise as [[DE-NIS2UMSUCG]] → [[DE-BSIG]]. Revisit if an amendment relationship type is added | Blocked | Germany batch |
| Lenkungsgremium GDI-DE | Governing committee of [[DE-GDI-DE]]; would be reachable only from that one entity | Later | Germany batch |

## Belgium — queued from the third-country batch (2026-08-15)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| The other five public service integrators | BELGIF names six; only [[BE-KSZ]] is modelled | Later | Belgium batch |
| Belgian eID / itsme; eHealth platform; Kruispuntbank van Ondernemingen | Belgium's digital identity and registry infrastructure, none modelled. itsme is one of Europe's more distinctive national identity schemes | Later | Belgium batch |

## France — queued from the fourth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|

## Spain — queued from the fifth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **Spanish organic law on artificial intelligence** — sharpened, not closed | Now a Proyecto de Ley Orgánica before Congress (BOCG Serie A No. 97-1, published 12 June 2026), approved for submission by the Council of Ministers 26 May 2026, confirmed by reading lamoncloa.gob.es directly. Still not created: that same government source names [[ES-AESIA]] as "the central body," while secondary reporting on the bill's own Congress text describes a separate General Directorate of Artificial Intelligence as notifying authority and eight state-level market surveillance authorities — a genuine contradiction, not yet resolved by reading the bill's own BOCG text | Next | Spain batch; sharpened research-queue pickup / 2026-09-04 |
| **Spain's INSPIRE transposition** | [[EU-INSPIRE]] now carries `applies-in` → `ES` with no transposing instrument identified | Later | Spain batch |
| **INCIBE's founding instrument** | Its legal form, its relationship to the earlier INTECO, and how INCIBE-CERT relates to CCN-CERT are all unrecorded. [[ES-INCIBE]] is `coverage: low` because of it | Later | Spain batch |
| **Cl@ve's legal basis and operator** | Plus the relationship between Cl@ve PIN and Cl@ve Permanente, and the status of any Spanish digital identity wallet under [[EU-EIDAS2]] | Later | Spain batch |
| **Centro Nacional de Ciberseguridad** | Would be created by [[ES-LCGC]]. **Deliberately not modelled** — it does not exist, and a node for it would be indistinguishable in the graph from a body that does | Blocked | Spain batch |
| **The Comunidades Autónomas** | Seventeen regional open data portals, regional data protection authorities, and the co-governance half of [[ES-ESPANA-DIGITAL-2026]]. **No longer blocked**: `level: subnational` was added 2026-08-21. Seventeen is a large batch, so the sensible start is the two or three with their own DPAs | Next | Spain batch; unblocked 2026-08-21 |

## Basisregistraties — queued from the register batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **SVB-BGT** | Samenwerkingsverband Bronhouders voor de BGT — the cooperative organising seven categories of bronhouder into one national map. Named in one source | Later | Register batch |
| **Rijkswaterstaat, ProRail, RVO** | BGT and BRO bronhouders; none is an Atlas entity | Later | Register batch |
| **Dutch municipalities as entities** | They hold the [[NL-BAG]] and determine [[NL-WOZ]] values. `level: local` is the right value and remains unused; the open question is **what entity to create** — 342 municipalities individually is not obviously right, and one collective entity would misdescribe 342 separate controllers | Blocked (design) | Register batch |
| **DINO and BIS** | [[NL-BRO]]'s predecessors, described as registrations it *builds on*. Whether either continues to exist determines if `supersedes` is ever right | Later | Register batch |
| **Geonovum's role in BRO standards** | Geonovum publishes BRO geo-standards; whether it maintains them or publishes them for the programme was not established, so no relationship was asserted | Later | Register batch |

## Poland — queued from the sixth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **CSIRT MON** | Poland's military CSIRT, and the last of the three still unmodelled — [[PL-NASK]] carries CSIRT NASK and [[PL-ABW]] carries CSIRT GOV | Later | Poland batch; narrowed 2026-08-18 |
| **GIODO** | The predecessor data protection authority. Whether the succession to [[PL-UODO]] can be modelled depends on establishing what happened to the competencies the President did **not** take over | Later | Poland batch |
| **Agencja Informatyzacji** | Would replace [[PL-COI]]. **Blocked** — the draft law is in consultation and the body does not exist | Blocked | Poland batch |

## Other queued research

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| StUF (Standaard Uitwisselings Formaat) | VNG municipal exchange standard. Searched in Batch 4 but no usable source returned — deliberately not created | Batch 5+ | Batch 4 / 2026-08-14 |
| Remaining 'pas toe of leg uit' standards | Only Digikoppeling and ADR are modelled. The full mandatory + recommended lists (DNSSEC, DMARC, TLS, WCAG, SAML, OAuth profiles, …) are not enumerated | Batch 5+ | Batch 4 / 2026-08-14 |
| Wet bescherming persoonsgegevens (Wbp) | Predecessor regime replaced by GDPR/UAVG on 25 May 2018; needed for temporal completeness | Batch 4 or later | Batch 3 / 2026-08-14 |
| Aanpassingswet AVG (dossier 34.939) | Adjusted other Dutch legislation to the GDPR | Batch 4 or later | Batch 3 / 2026-08-14 |
| eIDAS → [[NL-WDO]] link | Both eIDAS entities now exist; eIDAS 2.0 ruled out on dates, but the transposition from 910/2014 remains **unsourced** and unasserted | Batch 9+ | Batch 3; updated Batch 8 |
| Wet elektronische publicaties; Wet politiegegevens; Telecommunicatiewet | Further Dutch legislation with data relevance, not assessed in Batch 3 | Batch 4 or later | Batch 3 / 2026-08-14 |
| ISO / IEC / CEN → [[NL-NEN]] links | NEN's most significant relationships; need the international standards bodies | Batch 9 / 13 | Batch 2 / 2026-08-14 |
| ISO/IEC 27001 & 27002 → [[NL-BIO]] link | BIO2 is explicitly based on NEN-EN-ISO/IEC 27001:2023 and 27002:2022; the `based-on` relationship is unassertable until those entities exist | Batch 14 | Batch 4 / 2026-08-14 |
| **W3C DCAT → EU DCAT-AP → [[NL-DCAT-AP-NL]] chain** | A clean international→EU→national standards descent, and one of the clearest demonstrations available of what the Atlas is for. Complete it when Batches 9 and 14 land | Batch 9, 14 | Batch 4 / 2026-08-14 |
| Topsector Logistiek | Originator of [[NL-ISHARE]]; needed to assert its `maintained-by`. **Attempted 2026-09-04**: secondary sources attribute iSHARE's origination to Topsector Logistiek via NLIP, but iSHARE's own official history page, read directly, does not name either — it credits unspecified "government and business organizations." Topsector Logistiek is also a broad national innovation-policy programme (one of ~9-10 Dutch "topsectoren"), not a narrow single-purpose body, so modelling it accurately would need more research than this pass gave it. No entity created; no `maintained-by` edge asserted | Batch 10 | Batch 5 / 2026-08-14; attempted research-queue pickup 2026-09-04 |
| DMI ecosystem; IDSA / IDS architecture | Named in iSHARE sources as data-space users of its trust framework | Batch 10 | Batch 5 / 2026-08-14 |
| Ministerie van Infrastructuur en Waterstaat; Rijkswaterstaat | Founding partners of [[NL-PDOK]] not yet modelled, making its founding collaboration look narrower than it was | Batch 5+ | Batch 5 / 2026-08-14 |
| Ministeries van VWS, EZK, OCW | Named partners of [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Groeifonds | Funds [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Wegenbestand (NWB) | Part of the [[NL-NDW]] expansion | Batch 5+ | Batch 5 / 2026-08-14 |
| ODISSEI | Research infrastructure organisation named alongside DANS/RIVM/NWO/SIDN, all now modelled; ODISSEI alone remains unresearched | Batch 5+ | Batch 2; carried |
| Free Flow of Non-Personal Data Regulation | Third repeal target of [[EU-DIGITAL-OMNIBUS]] | Batch 9 | Batch 8 / 2026-08-14 |
| EUR-Lex citation for the AI Act | [[EU-AI-ACT]] lacks an Official Journal link | Batch 9 | Batch 8 / 2026-08-14 |
| Dutch EUDI Wallet implementation | Every member state must provide one; no Dutch arrangement researched | Batch 9+ | Batch 8 / 2026-08-14 |
| **The 10 remaining common European data spaces** | Batch 10 created Health, Mobility, Green Deal and Agriculture. **Not created:** cultural heritage, energy, finance, industry, language, media, public administrations, research and innovation, skills, tourism — research returned only their names in the list of fourteen | Later | Batch 7; narrowed Batch 10 |
| UN DESA, UNDP, UNESCO, WHO, UNECE | Named in Batch 13's scope; **no usable source located for any**, so none created | Later | Batch 13 / 2026-08-14 |
| World Bank | Named in Batch 13's scope; omitted deliberately — its institutions are technically UN specialised agencies and misclassifying it is the specific error the brief warns against | Later | Batch 13 / 2026-08-14 |
| IEEE | Named in the standards-ecosystem source alongside ISO/IEC/ITU/IETF/W3C; not created | Later | Batch 13 / 2026-08-14 |
| ISO/IEC JTC 1 and SC 27 | Arguably the actual producer of the 27000-family standards | Later | Batch 14 / 2026-08-14 |
| Current-edition URL for ISO/IEC 27002:2022 | The cited ISO OBP link resolves to the superseded 2013 edition | Later | Batch 14 / 2026-08-14 |
| IETF RFCs behind [[NL-PAS-TOE-OF-LEG-UIT]] | HTTPS, DNSSEC, DMARC/SPF/DKIM, TLS all originate in IETF RFCs and are mandatory Dutch standards — a real international → national chain, entirely unmodelled | Later | Batch 13 / 2026-08-14 |
| OECD Privacy Guidelines / data governance recommendations | [[INTL-OECD]] exists but no OECD instrument is modelled | Later | Batch 13 / 2026-08-14 |
| ITU standards | [[UN-ITU]] exists but no ITU standard is modelled | Later | Batch 13 / 2026-08-14 |
| UNCTAD CSTD working group on data governance | May warrant an `initiative` entity if its outputs are substantive | Later | Batch 13 / 2026-08-14 |
| Data quality, information management, digital identity, AI, data sharing, API and knowledge-graph standards | Batch 14's scope lists all of these; **only information security (27001/27002) and metadata (DCAT) were covered** | Later | Batch 14 / 2026-08-14 |
| W3C source for DCAT | [[INTL-DCAT]] rests on second-hand descriptions; the top of the flagship standards chain | Batch 14 | Batch 9 / 2026-08-14 |
| W3C (the organisation) | Needed for [[INTL-DCAT]]'s `maintained-by` | Batch 13 | Batch 9 / 2026-08-14 |
| GeoDCAT-AP and StatDCAT-AP | Extensions of [[EU-DCAT-AP]]; GeoDCAT-AP would likely connect [[NL-GEONOVUM]]'s geo and metadata work | Later | Batch 9 / 2026-08-14 |
| ETSI standards | [[EU-ETSI]] exists but **no ETSI standard is modelled**, despite ICT standardisation being central to this Atlas | Later | Batch 9 / 2026-08-14 |
| EUR-Lex citation for EHDS Reg. (EU) 2025/327 | [[EU-EHDS]]'s strongest source is the Parliament's Legislative Observatory | Later | Batch 10 / 2026-08-14 |
| IDSA / IDS architecture | [[NL-ISHARE]]'s documented route into the EU data-space world | Later | Batch 5; carried |
| Environment / Energy / Agriculture domains | Still below the 2-entity threshold even after Batch 10 | Later | Batch 5; rechecked Batch 10 |
| EU AI strategy (if distinct from the AI Act) | Named in Batch 7 scope; no clearly identifiable standalone strategy document found | Batch 8 | Batch 7 / 2026-08-14 |
| Digital Europe Programme; EuroHPC | EU digital infrastructure funding instruments, not researched in Batch 7 | Batch 9 | Batch 7 / 2026-08-14 |
| Energy, Environment, Finance, Justice, Agriculture, Social Security, Built Environment domains | All named in the Batch 5 brief but each currently below the 2-entity threshold in taxonomy §1. Create as the ecosystems that would populate them are researched | Later | Batch 5 / 2026-08-14 |
| College Standaardisatie | Established in 2006 alongside Forum Standaardisatie; current status unknown — may be superseded, which would need a `supersedes` link | Batch 2 | Batch 1 / 2026-08-14 |
| Individual GDI services (DigiD, DigiD Machtigen, MijnOverheid, Digipoort) | Referenced by NL-GDI and NL-LOGIUS but not yet entities; decide whether they warrant separate entities | Batch 2 or 5 | Batch 1 / 2026-08-14 |
| Individual open standards on the 'pas toe of leg uit' list | Referenced by NL-PAS-TOE-OF-LEG-UIT | Batch 4 | Batch 1 / 2026-08-14 |
| Meerjarenvisie Digitale Overheid; GDI programmeringsplan | Named as MIDO components; may warrant entities or may be publications | Batch 4 | Batch 1 / 2026-08-14 |
| RedIRIS | Spain's research and education network, run by [[ES-RED-ES]] — the counterpart of [[NL-SURF]]. Named on Red.es's own pages; not modelled | Later | RQ3 batch / 2026-08-19 |
| ONTSI and the `.es` domain registry | The other two Red.es roles. ONTSI is an observatory (publications); the `.es` registry is naming-authority infrastructure with no Atlas counterpart yet | Later | RQ3 batch / 2026-08-19 |
| Ordonnance n° 2016-307 and décret n° 2021-1559 | The French codification instrument and the licence decree, recorded in prose on [[FR-LOI-VALTER]]. Both fall below the threshold the Atlas has used for `type: law`; revisit if the CRPA is ever modelled as an entity | Later | RQ3 batch / 2026-08-19 |
| An `amended-by` inverse | `amends` was added this batch as a single directed type. The graph shows incoming edges, so the inverse is readable without being stored — but `implements`/`implemented-by` exist as a pair, so the vocabulary is now inconsistent with itself | Later (design) | RQ3 batch / 2026-08-19 |
| The 37 base country anchors | Each of [[AD]], [[AL]], [[AM]], [[AT]], [[AZ]], [[BA]], [[BG]], [[BY]], [[CY]], [[DK]], [[EE]], [[FI]], [[GE]], [[GR]], [[HR]], [[HU]], [[IS]], [[IT]], [[LI]], [[LT]], [[LV]], [[MC]], [[MD]], [[ME]], [[MK]], [[MT]], [[RO]], [[RS]], [[RU]], [[SE]], [[SI]], [[SK]], [[SM]], [[TR]], [[UA]], [[VA]] and [[XK]] carries membership facts and nothing else — no DPA, no portal, no statistics office, no legislation | Later, one country at a time | European country batch / 2026-08-19 |
| Greece's `EL` / `GR` code split | The EU keys Greece as `EL`; ISO keys it as `GR`. The Atlas uses `GR`. Any future harvest of Eurostat or EUR-Lex data will not join without a mapping | Later (design) | European country batch / 2026-08-19 |
| Cyprus's suspended *acquis* | `applies-in` is a whole-country predicate; the *acquis* is suspended in the areas of [[CY]] not under the Republic's effective control. The Atlas cannot express this | Blocked (design) | European country batch / 2026-08-19 |
| **`applies-in` for the European parties to Convention 108** | Sources say all Council of Europe member states are parties — roughly 46 edges. **Blocked on reading `coe.int`'s chart of signatures and ratifications** — confirmed 2026-08-21 as a host-level bot-defense wall (Cloudflare challenge), not the egress policy; egress is open but this host still is not. The one source found for the rule gives a stale member count, and [[RU]]'s status as a party after its 2022 expulsion is unaddressed. The first time the sourcing debt has blocked *new* modelling rather than re-verification | Blocked (host) | Convention 108 batch / 2026-08-19; confirmed batch 1 / 2026-08-21 |
| The descent from ETS 181 to the national DPAs and to adequacy | [[INTL-CONVENTION-108-PROTOCOL]] required independent supervisory authorities in 2001 and introduced adequacy-based transfer rules. The Atlas holds eleven national DPAs and [[EU-UK-ADEQUACY]] and asserts no relationship to it, because no source read states the descent. Recorded in prose on that entity | Later | Convention 108 batch / 2026-08-19 |
| Argentina's and Uruguay's EU adequacy decisions | Both are recorded in prose on [[AR]] and [[UY]] and neither is an entity. They would connect the Convention 108 parties to the EU adequacy machinery the Atlas already holds through [[EU-UK-ADEQUACY]] | Later | Convention 108 batch / 2026-08-19 |
| Data Protection Day (28 January) | Marked across Europe as the anniversary of Convention 108's opening for signature. Recorded in prose on [[INTL-CONVENTION-108]]; whether an observance is an Atlas entity at all is an open question | Later (design) | Convention 108 batch / 2026-08-19 |
| Run the re-verification pass | `tools/reverify.py` exists and `docs/re-verification.md` is the procedure. **Egress opened 2026-08-21; batch 1 read live pages for the first time**, moving 21 entities to `primary-source`, including all seven Dutch register statutes. 414 of 516 entities remain — work `discovery/reverification-allowlist.md` in the order it ranks, skipping entities citing only `eur-lex.europa.eu`, `www.iso.org`, `www.coe.int` or `unece.org` (bot-defense walls, not egress) | Ongoing | Re-verification runner / 2026-08-19; batch 1 / 2026-08-21 |
| Identifier patterns `tools/reverify.py` does not yet know | It extracts BWBR, BOE, JORF, C/ETS, S.I., CELEX, Dz.U., Real Decreto, Ley, Lei and zákon citations. Norwegian, Swiss, German (Bundesgesetzblatt) and UK (`legislation.gov.uk` ELI) shapes are not covered, so entities keyed on those get names-only checking | Later | Re-verification runner / 2026-08-19 |
| The five `github.com` sources | Cited on [[BE-BELGIF]], [[EU-SEMIC]], [[BE-DCAT-AP-BE]] and [[EU-DCAT-AP]]. Refused by the **GitHub proxy**, which scopes a session to its configured repositories — a different policy from the egress allowlist, and one an allowlist entry will not lift. These five may never be re-verifiable from inside a session | Blocked (GitHub proxy) | Full sweep / 2026-08-19 |
| Six entities with no checkable claims | [[RO]], [[UA]], [[FR-ETALAB]], [[NL-LOGIUS]], [[NL-NICTIZ]], [[NO-ALTINN]] — short names and no legal identifier, so `tools/reverify.py` can only fetch their sources, not corroborate anything against them. Either richer `alternative_names` or acceptance that these are judgment-only entities | Later | Full sweep / 2026-08-19 |
| Hub-aware Explorer traversal | The neighbourhood control's depth is a blunt lever on a hub-heavy graph: a path `A → EU → B` exists between almost any pair and means only "both are European". Not traversing *through* anchor and `DOMAIN-*` nodes — or making that a toggle — would make deep hops meaningful and would make wikilinks-on mode usable at depth, which it is not today. Measured: median seed reaches 66% of the graph at 2 hops with wikilinks on | Later (design) | Explorer depth batch / 2026-08-20 |
| Estonia's Open Data Directive transposition — narrowed, not closed | WebSearch (2026-09-04) surfaced a specific, dated candidate: "Avaliku teabe seaduse muutmise seadus" (RT I, 30.11.2021, 3), reportedly adopted 17.11.2021 and in force 10.12.2021 to transpose Directive 2019/1024, corroborated independently by an EU Open Data Maturity factsheet characterising the PIA as Estonia's open-data legal framework. **Every direct-fetch attempt failed this pass** — `riigiteataja.ee` and `eelnoud.valitsus.ee` are JS-rendered with no static content, `rup.ee` returned 403, and both the koda.ee explanatory memorandum and the data.europa.eu factsheet PDFs returned only unreadable binary. No relationship asserted; the specific citation is a lead for the next attempt, not a sourced fact | Next | Estonia batch / 2026-08-20; narrowed research-queue pickup / 2026-09-04 |
| Estonian eID card and Mobile-ID | The identity infrastructure [[EE-E-RESIDENCY]] is built on, and the link to [[EU-EIDAS2]] and the European Digital Identity Wallet | Later | Estonia batch / 2026-08-20 |
| NIIS member vs partner status | Ukraine, the Faroe Islands and the Government of Åland are **partners** of [[INTL-NIIS]] rather than members. The relationship vocabulary has `part-of` and `participates-in` and no way to say "associate", so [[UA]]'s partnership is prose only | Later (design) | Estonia batch / 2026-08-20 |
| `applies-in` for the EU **directives** | The member-state completion pass extended the nine EU **regulations** to all 27 states, because a regulation's applicability follows from TFEU Article 288 and needs no country-specific source. The five directives — [[EU-NIS2]], [[EU-CER]], [[EU-INSPIRE]], [[EU-ITS-DIRECTIVE]], [[EU-OPEN-DATA-DIRECTIVE]] — still name 10 states each. Extending them is defensible but would show 17 blank transposition cells per directive, so it was left as a deliberate decision rather than a sweep | Next (design) | Member-state completion / 2026-08-20 |
| A content check to follow the link check | **Started 2026-08-21.** The repository owner confirmed `europa.eu`, `iso.org`, `coe.int`, `bund.de` and `legifrance.gouv.fr` at the content tier by hand (41 entities to `primary-source`); the same day, with egress open, `tools/reverify.py` did its own machine-corroborated reading (21 more entities, batch 1). 414 of 516 remain. See `docs/re-verification.md` §"The confirmed domains" and §"A machine-corroborated pass" | Ongoing | Manual link check / 2026-08-20; content check / 2026-08-21; reverify batch 1 / 2026-08-21 |
| PagoPA and the Piano triennale | Italy's payments platform and the three-year plan for public-administration IT, both named around [[IT-AGID]] and neither modelled | Later | Country expansion / 2026-08-20 |
| An Icelandic X-Road deployment | [[IS]] is the third member of [[INTL-NIIS]] and the only one with no national deployment modelled, now that [[EE-X-TEE]] and [[FI-PALVELUVAYLA]] both exist | Later | Country expansion / 2026-08-20 |
| Austria's federal digital policy ministry | [[AT-BRZ]] is a service provider rather than a policy agency, so it appears as the hub of the Austrian layer in a way that reflects what is modelled rather than how Austria is governed | Later | Country expansion / 2026-08-20 |
| Iceland and Liechtenstein beyond data protection | Both now have a national layer — a DPA and a data protection act each — and nothing else. [[IS]] is a member of [[INTL-NIIS]] with no X-Road deployment modelled; neither has a statistical office, a mapping authority or a cyber authority | Later | Candidate batch / 2026-08-21 |
| The other EEA Joint Committee decisions | [[INTL-EEA-JCD-154-2018]] is the only one modelled, created because four entities were describing it in prose. Every other EU act with effect in the EEA EFTA states reaches them the same way and the Atlas draws none of those routes | Later | Candidate batch / 2026-08-21 |
| Euro 7's implementing regulations (OBFCM/OBM data formats) | [[EU-EURO-7]] was added 2026-08-28 from the regulation's own text; secondary industry sources report two Commission implementing regulations (numbered 2025/1706 and 2025/1707 in commentary) specifying OBFCM and on-board-monitoring data formats and reporting procedures in detail. Neither was fetched or confirmed directly | Later | Euro 7 addition / 2026-08-28 |
| Regulation (EU) 2018/858 | The general EU vehicle type-approval framework regulation that [[EU-EURO-7]] amends per a secondary summary. Not itself an Atlas entity; no `amends` relationship asserted without reading its own text | Later | Euro 7 addition / 2026-08-28 |
| [[NL-RDW]]'s Euro 7 role | RDW is the Netherlands' general vehicle type-approval authority and would perform Euro 7 approvals once the regulation applies, but its own site describes its type-approval function in general terms only, without naming Euro 7. No relationship asserted | Later | Euro 7 addition / 2026-08-28 |
