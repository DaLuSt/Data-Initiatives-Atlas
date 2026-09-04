# Research Queue

> **This is a list of open work.** Items are removed when they close — the
> record of what was closed, and why, lives in `progress/completed.md` and on
> the entities themselves. Nothing here is struck through, because struck-out
> rows made the queue longer every time it got shorter.
>
> **Largest open items:** the Comunidades Autónomas, now unblocked and
> unstarted; OSLO/Digitaal Vlaanderen; and DKE, Germany's last unmodelled
> `Next`-flagged gap. [[PL-PESEL]], Poland's population register, is
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
| The sixteen Land INSPIRE transposition acts | Jointly with [[DE-GEOZG]] they constitute Germany's transposition. **Blocked on the `level` ontology question**, not on sourcing | Blocked | Germany batch |
| Land data protection authorities | [[DE-BFDI]] covers federal bodies only; sixteen Land authorities cover the rest. Same blocker | Blocked | Germany batch |
| Individual XÖV standards | XPersonenstand, XMeld, XBau, XPlanung and others. Only [[DE-XRECHNUNG]] is modelled. Creating one entity per standard would inflate the layer without adding structure (brief §1) | Later | Germany batch |
| DKE | German electrotechnical standards commission, [[DE-DIN]]'s counterpart towards [[EU-CENELEC]] | Later | Germany batch |
| National Gaia-X hubs | Germany's and Austria's hubs are cited as sources on [[EU-GAIA-X]]. A `DE-GAIA-X-HUB` would be a legitimate national entity, not a duplicate — but nothing beyond website existence was established | Later | Germany batch |
| Mobility Data Marketplace (MDM) | Replaced by [[DE-MOBILITHEK]] as National Access Point. **No superseded entity created** — unlike [[DE-IWG]], nothing beyond the replacement is established | Later | Germany batch |
| Bundesdruckerei; ITZBund | Federal printing/eID body and the federal IT service centre. ITZBund is already cited as a source on [[DE-XOEV]] | Later | Germany batch |
| OZG-Änderungsgesetz | A substantial amending act, deliberately **not** given its own entity — doing so would force the same `supersedes` compromise as [[DE-NIS2UMSUCG]] → [[DE-BSIG]]. Revisit if an amendment relationship type is added | Blocked | Germany batch |
| Lenkungsgremium GDI-DE | Governing committee of [[DE-GDI-DE]]; would be reachable only from that one entity | Later | Germany batch |

## Belgium — queued from the third-country batch (2026-08-15)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **OSLO and Digitaal Vlaanderen** | A major European semantic-interoperability programme, entirely unmodelled. **No longer blocked**: `level: subnational` was added 2026-08-21 and the three Belgian sub-federal ODD instruments are modelled under it. This is now ordinary research | Next | Belgium batch; unblocked 2026-08-21 |
| Agence du Numérique; Paradigm; the Regions and Communities | Same blocker | Blocked | Belgium batch |
| The other five public service integrators | BELGIF names six; only [[BE-KSZ]] is modelled | Later | Belgium batch |
| Belgian eID / itsme; eHealth platform; Kruispuntbank van Ondernemingen | Belgium's digital identity and registry infrastructure, none modelled. itsme is one of Europe's more distinctive national identity schemes | Later | Belgium batch |
| Belgian statistics act | No statutory basis for [[BE-STATBEL]] was found | Later | Belgium batch |

## France — queued from the fourth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| RGS and RGAA | France's security and accessibility reference frameworks, siblings of [[FR-RGI]] | Later | France batch |
| France Identité | Recorded in prose on [[FR-FRANCECONNECT]]; not its own entity | Later | France batch |
| Ordonnance n° 2005-1516 | Legal basis of [[FR-RGI]]; not modelled | Later | France batch |
| Ordonnance of 21 October 2010 | France's INSPIRE transposition, cited on [[EU-INSPIRE]]'s `applies-in`; its number was not established so no entity was created | Later | France batch |

## Spain — queued from the fifth-country batch (2026-08-16)

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| **Spanish organic law on artificial intelligence** | Sources refer to one landing the AI Act domestically with sanctions and sandboxes, at a stage they describe inconsistently. Not created — the Atlas already carries one instrument whose sources conflict ([[FR-NIS2-LOI]]) and does not need a second on weaker evidence | Next | Spain batch |
| **Ley 39/2015 and Ley 40/2015** | Spain's common administrative procedure and public-sector legal regime acts — the current legal base for much of what [[ES-AEAD]] does, and the successors to Ley 11/2007 which established [[ES-ENI]] | Next | Spain batch |
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
| **Krajowe Ramy Interoperacyjności** | Poland's national interoperability framework — the sixth national NIF, and the sixth potential [[EU-EIF]] descent | Later | Poland batch |
| **A Polish DCAT application profile** | [[EU-DCAT-AP]] has four national children; whether Poland has a fifth was not researched | Later | Poland batch |
| **Ustawa o statystyce publicznej (1995)** | [[PL-GUS]]'s legal basis, named and dated, not modelled — same treatment as the Dutch and Spanish statutes | Later | Poland batch |
| **GIODO** | The predecessor data protection authority. Whether the succession to [[PL-UODO]] can be modelled depends on establishing what happened to the competencies the President did **not** take over | Later | Poland batch |
| **Agencja Informatyzacji** | Would replace [[PL-COI]]. **Blocked** — the draft law is in consultation and the body does not exist | Blocked | Poland batch |

## Other queued research

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| CIO Rijk | Named as an OBDO member; not yet researched | Batch 3 or later | Batch 1 / 2026-08-14 |
| Het Waterschapshuis | Develops and manages shared ICT facilities for the 21 water authorities; sourcing in Batch 2 was a single passing mention | Batch 3 or later | Batch 2 / 2026-08-14 |
| VNG Realisatie | VNG's implementation arm; not yet researched | Batch 3 or later | Batch 2 / 2026-08-14 |
| Centrale Commissie voor de Statistiek (CCS) | Statutory supervisor of the CBS under the Wet op het CBS | Batch 3 or later | Batch 2 / 2026-08-14 |
| Ministerie responsible for CBS (Economic Affairs) | Needed to complete CBS governance; Dutch ministry naming is volatile and must be read from a current source | Batch 3 or later | Batch 2 / 2026-08-14 |
| Adviescollege ICT-toetsing (AcICT) | ICT oversight body; surfaced in Batch 1 search results | Batch 3 or later | Batch 2 / 2026-08-14 |
| DANS, RIVM, NWO | Research/health data infrastructure organisations. [[NL-HEALTH-RI]] was created in the health/education/research domain batch (2026-08-21); these three were not | Batch 5 | Batch 2 / 2026-08-14 |
| SIDN | .nl registry / internet infrastructure | Batch 5 | Batch 2 / 2026-08-14 |
| Programmaraad (geo-standaarden) | Commissioning body for Geonovum's standards management | Batch 5+ | Batch 2 / 2026-08-14 |
| VNG Realisatie | Now doubly needed: maintains [[NL-GEMMA]], and [[NL-GEMMA]]'s `maintained-by` currently points at [[NL-VNG]] as a simplification | Batch 5+ | Batch 2; raised Batch 4 |
| WILMA (Waterschaps Informatie & Logisch Model Architectuur) | Water authorities' reference architecture; completes the NORA family. Not created in Batch 4 — single mention, and not named in the batch scope (unlike PETRA) | Batch 5+ | Batch 4 / 2026-08-14 |
| Edustandaard | Publishes/maintains [[NL-ROSA]]; its `maintained-by` link is unasserted without it | Batch 5+ | Batch 4 / 2026-08-14 |
| StUF (Standaard Uitwisselings Formaat) | VNG municipal exchange standard. Searched in Batch 4 but no usable source returned — deliberately not created | Batch 5+ | Batch 4 / 2026-08-14 |
| ENSIA | Accountability system paired with the BIO | Batch 5+ | Batch 4 / 2026-08-14 |
| NOiV programme bureau | Built BOMOS; appears historical. Needed to resolve BOMOS custody | Batch 5+ | Batch 4 / 2026-08-14 |
| Remaining 'pas toe of leg uit' standards | Only Digikoppeling and ADR are modelled. The full mandatory + recommended lists (DNSSEC, DMARC, TLS, WCAG, SAML, OAuth profiles, …) are not enumerated | Batch 5+ | Batch 4 / 2026-08-14 |
| The 10 individual basisregistraties | Still not enumerated (carried from Batch 2) | Batch 5 | Batch 2 / 2026-08-14 |
| The ten individual basisregistraties (BRK, BAG, BRP, Handelsregister, BRV, …) | Referenced by [[NL-BASISREGISTRATIES]]; the full list of ten has not been enumerated from a source | Batch 4 or 5 | Batch 2 / 2026-08-14 |
| `DOMAIN-HEALTH` | Needed by [[NL-NICTIZ]]; withheld because taxonomy §1 requires a domain to connect 2+ entities | Batch 5 | Batch 2 / 2026-08-14 |
| `DOMAIN-EDUCATION` | Needed by [[NL-SURF]]; withheld for the same reason | Batch 5 | Batch 2 / 2026-08-14 |
| Wet bescherming persoonsgegevens (Wbp) | Predecessor regime replaced by GDPR/UAVG on 25 May 2018; needed for temporal completeness | Batch 4 or later | Batch 3 / 2026-08-14 |
| Aanpassingswet AVG (dossier 34.939) | Adjusted other Dutch legislation to the GDPR | Batch 4 or later | Batch 3 / 2026-08-14 |
| Wet weerbaarheid kritieke entiteiten (CER implementation) | Passed alongside the Cyberbeveiligingswet; adjacent to but distinct from NIS2 | Batch 4 or later | Batch 3 / 2026-08-14 |
| NCSC / NCTV | Cybersecurity authorities named in Cyberbeveiligingswet sources | Batch 4 or later | Batch 3 / 2026-08-14 |
| eIDAS → [[NL-WDO]] link | Both eIDAS entities now exist; eIDAS 2.0 ruled out on dates, but the transposition from 910/2014 remains **unsourced** and unasserted | Batch 9+ | Batch 3; updated Batch 8 |
| Wet elektronische publicaties; Wet politiegegevens; Telecommunicatiewet | Further Dutch legislation with data relevance, not assessed in Batch 3 | Batch 4 or later | Batch 3 / 2026-08-14 |
| ISO / IEC / CEN → [[NL-NEN]] links | NEN's most significant relationships; need the international standards bodies | Batch 9 / 13 | Batch 2 / 2026-08-14 |
| ISO/IEC 27001 & 27002 → [[NL-BIO]] link | BIO2 is explicitly based on NEN-EN-ISO/IEC 27001:2023 and 27002:2022; the `based-on` relationship is unassertable until those entities exist | Batch 14 | Batch 4 / 2026-08-14 |
| **W3C DCAT → EU DCAT-AP → [[NL-DCAT-AP-NL]] chain** | A clean international→EU→national standards descent, and one of the clearest demonstrations available of what the Atlas is for. Complete it when Batches 9 and 14 land | Batch 9, 14 | Batch 4 / 2026-08-14 |
| Topsector Logistiek | Originator of [[NL-ISHARE]]; needed to assert its `maintained-by` | Batch 10 | Batch 5 / 2026-08-14 |
| digiGO | Initiator of [[NL-DSGO]]; needed to assert its `maintained-by` | Batch 10 | Batch 5 / 2026-08-14 |
| DMI ecosystem; IDSA / IDS architecture | Named in iSHARE sources as data-space users of its trust framework | Batch 10 | Batch 5 / 2026-08-14 |
| Ministerie van Infrastructuur en Waterstaat; Rijkswaterstaat | Founding partners of [[NL-PDOK]] not yet modelled, making its founding collaboration look narrower than it was | Batch 5+ | Batch 5 / 2026-08-14 |
| Ministeries van VWS, EZK, OCW | Named partners of [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Groeifonds | Funds [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Wegenbestand (NWB) | Part of the [[NL-NDW]] expansion | Batch 5+ | Batch 5 / 2026-08-14 |
| DANS, ODISSEI, RIVM, NWO, SIDN | Research/health/internet-infrastructure organisations still unqueued from Batch 2 | Batch 5+ | Batch 2; carried |
| Interoperable Europe Board | Adopts new EIF versions; needed to resolve the EIF/Act relationship | Batch 9 | Batch 7; carried |
| Free Flow of Non-Personal Data Regulation | Third repeal target of [[EU-DIGITAL-OMNIBUS]] | Batch 9 | Batch 8 / 2026-08-14 |
| Wet weerbaarheid kritieke entiteiten | Dutch CER transposition, approved 15 Apr 2026; should mirror [[NL-CBW]] → [[EU-NIS2]] | Batch 9+ | Batch 3; raised again Batch 8 |
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
| **Interoperable Europe Board** | Still not created — two passing mentions only | Later | Batch 7; carried |
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
| Austria's E-Government-Gesetz, Meldegesetz, Personenstandsgesetz and Passgesetz | All four were amended to introduce [[AT-ID-AUSTRIA]] and the oesterreich.gv.at platform. None is modelled, so the Austrian identity layer has a platform with no legal basis attached | Next | Country expansion / 2026-08-20 |
| Italy's CIE and CNS | [[IT-CAD]] admits three credentials for the citizen's right of digital access — [[IT-SPID]], the electronic identity card CIE, and the services card CNS. Only SPID is modelled | Next | Country expansion / 2026-08-20 |
| PagoPA and the Piano triennale | Italy's payments platform and the three-year plan for public-administration IT, both named around [[IT-AGID]] and neither modelled | Later | Country expansion / 2026-08-20 |
| An Icelandic X-Road deployment | [[IS]] is the third member of [[INTL-NIIS]] and the only one with no national deployment modelled, now that [[EE-X-TEE]] and [[FI-PALVELUVAYLA]] both exist | Later | Country expansion / 2026-08-20 |
| Austria's federal digital policy ministry | [[AT-BRZ]] is a service provider rather than a policy agency, so it appears as the hub of the Austrian layer in a way that reflects what is modelled rather than how Austria is governed | Later | Country expansion / 2026-08-20 |
| Iceland and Liechtenstein beyond data protection | Both now have a national layer — a DPA and a data protection act each — and nothing else. [[IS]] is a member of [[INTL-NIIS]] with no X-Road deployment modelled; neither has a statistical office, a mapping authority or a cyber authority | Later | Candidate batch / 2026-08-21 |
| The other EEA Joint Committee decisions | [[INTL-EEA-JCD-154-2018]] is the only one modelled, created because four entities were describing it in prose. Every other EU act with effect in the EEA EFTA states reaches them the same way and the Atlas draws none of those routes | Later | Candidate batch / 2026-08-21 |
| Euro 7's implementing regulations (OBFCM/OBM data formats) | [[EU-EURO-7]] was added 2026-08-28 from the regulation's own text; secondary industry sources report two Commission implementing regulations (numbered 2025/1706 and 2025/1707 in commentary) specifying OBFCM and on-board-monitoring data formats and reporting procedures in detail. Neither was fetched or confirmed directly | Later | Euro 7 addition / 2026-08-28 |
| Regulation (EU) 2018/858 | The general EU vehicle type-approval framework regulation that [[EU-EURO-7]] amends per a secondary summary. Not itself an Atlas entity; no `amends` relationship asserted without reading its own text | Later | Euro 7 addition / 2026-08-28 |
| [[NL-RDW]]'s Euro 7 role | RDW is the Netherlands' general vehicle type-approval authority and would perform Euro 7 approvals once the regulation applies, but its own site describes its type-approval function in general terms only, without naming Euro 7. No relationship asserted | Later | Euro 7 addition / 2026-08-28 |
| `domains/domain-cybersecurity.md` is stale | Its own narrative still says "The Netherlands and Poland — none in the Atlas at all. The Dutch NCSC is not modelled" and gives a 17-national-entity count — both wrong since [[NL-NCSC]] was verified into the Atlas in a later pass and [[EE-CERT-EE]] was added 2026-08-30. The whole page (tables, counts, the "three-layer chain" section) needs a fresh pass, not a spot fix | Next | Research-queue pickup / 2026-08-30 |
