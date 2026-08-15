# Research Queue

Confirmed-relevant areas that are known to need research but haven't been
worked yet, beyond the batch plan itself (`progress/backlog.md`). Use this
for gaps discovered mid-batch that fall outside the current batch's scope,
so they aren't lost.

---

## Batch 1 — Netherlands: Core Data Governance (COMPLETED search-only; needs re-verification)

Batch 1 was completed on 2026-08-14 from search-engine results only. The
session's network egress policy blocked all direct page retrieval, so no
authoritative source was read. This trade-off was raised and then accepted
explicitly; every resulting entity carries `verification: search-only` and
`confidence: low`/`medium`.

**The URLs below are now cited as `sources:` on the Batch 1 entities, but
none of them have been read.** They remain listed here as the worklist for
the re-verification pass: fetch each, confirm or correct the claims in the
corresponding entity, then set `verification: primary-source`,
`last_verified`, and per-source `accessed:` dates.

Find all affected entities with: `grep -rl "verification: search-only" .`

### Forum Standaardisatie / open standards

| Candidate source | URL | Verified? |
|---|---|---|
| Lijst open standaarden | https://www.forumstandaardisatie.nl/open-standaarden | No |
| 'Pas toe of leg uit'-standaarden (verplicht) | https://www.forumstandaardisatie.nl/open-standaarden/verplicht | No |
| 'Pas toe of leg uit'-beleid | https://www.forumstandaardisatie.nl/pas-toe-leg-uit-beleid | No |
| Toetsingsprocedure en criteria voor de lijst open standaarden | https://www.forumstandaardisatie.nl/toetsingsprocedure-en-criteria-voor-de-lijst-open-standaarden | No |
| Open Standaarden (Digitale Overheid) | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/open-standaarden/ | No |

### Interbestuurlijke Datastrategie (IBDS) / Federatief Datastelsel (FDS)

| Candidate source | URL | Verified? |
|---|---|---|
| Interbestuurlijke Datastrategie (IBDS) — Digitale Overheid | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/data/interbestuurlijke-datastrategie/ | No |
| Interbestuurlijke Datastrategie (IBDS) — NORA Online | https://www.noraonline.nl/wiki/Interbestuurlijke_Datastrategie_(IBDS) | No |
| Realisatie IBDS — Digitale Overheid | https://www.digitaleoverheid.nl/community/realisatie-ibds/ | No |
| Beleidsevaluatie Interbestuurlijke Datastrategie — Eindrapport (open.overheid.nl) | https://open.overheid.nl/documenten/1edd5ed4-98e8-442e-bcd2-f6ec3f27a754/file | No |
| IBDS / Federatief Datastelsel presentatie (Forum Standaardisatie, Dag van de Interoperabiliteit 2024) | https://www.forumstandaardisatie.nl/sites/default/files/BFS/8-Bijeenkomsten/20241015-Dag-van-de-interoperabiliteit/presentaties/Presentatie-Federatief-Datastelsel-en-resultaten-Mentimeter.pdf | No |

Open questions to resolve when researching: the exact date the IBDS was
presented to the Tweede Kamer; the current status of the IBDS (is it still
running, or superseded/absorbed?); the governance status of the Federatief
Datastelsel and whether a formal "Afsprakenstelsel Federatief Datastelsel"
has been adopted and when; whether FDS is best typed as `framework`,
`initiative` or `programme`.

### NORA

| Candidate source | URL | Verified? |
|---|---|---|
| NORA Online — Positionering NORA | https://www.noraonline.nl/wiki/Positionering_NORA | No |
| NORA — Digitale Overheid | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/nora/ | No |
| Overheidsarchitectuur NORA — ICTU | https://www.ictu.nl/diensten/dienstenoverzicht/overheidsarchitectuur-nora/ | No |
| Architectuur Digitale Overheid — NORA Online | https://www.noraonline.nl/wiki/Architectuur_Digitale_Overheid | No |

Open questions: confirm BZK is opdrachtgever and ICTU is beheerder;
confirm current NORA version and its relationship to GEMMA/EAR/ROSA/PETRA
(the latter are Batch 4 scope but the relationship should be captured).

### Common Ground

| Candidate source | URL | Verified? |
|---|---|---|
| Common Ground — VNG | https://vng.nl/onderwerpen/common-ground | No |
| Programma Common Ground — VNG | https://vng.nl/projecten/programma-common-ground | No |
| Realisatiekoers Common Ground Informatiesamenleving (21 mei 2025) | https://vng.nl/sites/default/files/2025-05/20250521-08b-realisatiekoers-common-ground.pdf | No |

Open questions: current programme status; whether Common Ground is best
typed as `initiative`, `framework` or `programme`; its formal relationship
to GEMMA and to the FDS.

### MIDO (Meerjarenprogramma Infrastructuur Digitale Overheid)

| Candidate source | URL | Verified? |
|---|---|---|
| Wat is het MIDO? | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/wat-is-het-mido/ | No |
| Governance MIDO | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/mido/governance/ | No |
| Kabinetsbeleid MIDO | https://www.digitaleoverheid.nl/mido/kabinetsbeleid/ | No |
| Voortgang MIDO (tijdlijn) | https://www.digitaleoverheid.nl/mido/voortgang-mido/ | No |
| Sturing van de ontwikkeling van de digitale overheid — NORA Online | https://www.noraonline.nl/wiki/Sturing_van_de_ontwikkeling_van_de_digitale_overheid | No |

Open questions: confirm MIDO's start year; confirm the OBDO's composition
and its advisory relationship to the responsible bewindspersoon (the search
result named a specific serving State Secretary, which is exactly the kind
of time-sensitive fact that must be read from the source, not inferred);
confirm the relationship between MIDO, the GDI and the Meerjarenvisie
Digitale Overheid.

### Additional sources located during Batch 1

| Candidate source | URL | Relevant to |
|---|---|---|
| Overheidsbreed Beleidsoverleg Digitale Overheid (OBDO) | https://www.digitaleoverheid.nl/dossiers/regie-op-gegevens/dossierpostcontext/overheidsbrede-beleidsoverleg-digitale-overheid-obdo/ | NL-OBDO |
| Governance Digitale Overheid (VNG) | https://vng.nl/artikelen/governance-digitale-overheid | NL-OBDO, NL-VNG |
| Staatscourant 2018, 9728 | https://zoek.officielebekendmakingen.nl/stcrt-2018-9728.html | NL-OBDO / NL-FORUM-STANDAARDISATIE instellingsbesluit (suspected) |
| Staatscourant 2022, 18861 | https://zoek.officielebekendmakingen.nl/stcrt-2022-18861.html | NL-OBDO / NL-FORUM-STANDAARDISATIE instellingsbesluit (suspected) |
| Forum Standaardisatie — Over ons | https://www.forumstandaardisatie.nl/over-ons | NL-FORUM-STANDAARDISATIE |
| Contactgegevens Stichting ICTU | https://organisaties.overheid.nl/27912852/Stichting_ICTU | NL-ICTU |
| Rapport Governance ICTU (Eerste Kamer) | https://www.eerstekamer.nl/overig/20220816/toelichting_op_governance_ictu/document | NL-ICTU |
| 5.2 Logius — Memorie van toelichting | https://www.rijksfinancien.nl/memorie-van-toelichting/2022/owb/vii/onderdeel/1060049 | NL-LOGIUS, NL-BZK |
| NL DIGITAAL: Data Agenda Overheid (PDF) | https://zoek.officielebekendmakingen.nl/blg-876545.pdf | NL-DATA-AGENDA-OVERHEID |
| Kabinetsbeleid Digitalisering | https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/kabinetsbeleid-digitalisering/ | NL-DIGIBETER successor question |

---

## Other queued research

| Area / entity | Why it needs research | Suggested batch | Noted by / date |
|---|---|---|---|
| ~~Interprovinciaal Overleg (IPO)~~ | Added in Batch 2 as [[NL-IPO]] | — | Done |
| ~~Unie van Waterschappen (UvW)~~ | Added in Batch 2 as [[NL-UVW]] | — | Done |
| CIO Rijk | Named as an OBDO member; not yet researched | Batch 3 or later | Batch 1 / 2026-08-14 |
| Het Waterschapshuis | Develops and manages shared ICT facilities for the 21 water authorities; sourcing in Batch 2 was a single passing mention | Batch 3 or later | Batch 2 / 2026-08-14 |
| VNG Realisatie | VNG's implementation arm; not yet researched | Batch 3 or later | Batch 2 / 2026-08-14 |
| Centrale Commissie voor de Statistiek (CCS) | Statutory supervisor of the CBS under the Wet op het CBS | Batch 3 or later | Batch 2 / 2026-08-14 |
| Ministerie responsible for CBS (Economic Affairs) | Needed to complete CBS governance; Dutch ministry naming is volatile and must be read from a current source | Batch 3 or later | Batch 2 / 2026-08-14 |
| Adviescollege ICT-toetsing (AcICT) | ICT oversight body; surfaced in Batch 1 search results | Batch 3 or later | Batch 2 / 2026-08-14 |
| DANS, Health-RI, RIVM, NWO | Research/health data infrastructure organisations | Batch 5 | Batch 2 / 2026-08-14 |
| SIDN | .nl registry / internet infrastructure | Batch 5 | Batch 2 / 2026-08-14 |
| ~~BOMOS~~ | Added in Batch 4 as [[NL-BOMOS]] | — | Done |
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
| Handelsregisterwet | Statutory basis of the Handelsregister held by [[NL-KVK]]; not created in Batch 3 for lack of a located source | Batch 4 or later | Batch 2 / 2026-08-14 |
| ~~Archiefwet (and its revision)~~ | Added in Batch 3 as [[NL-ARCHIEFWET-1995]] and [[NL-ARCHIEFWET-2026]] | — | Done |
| ~~Wet op het Centraal bureau voor de statistiek~~ | Added in Batch 3 as [[NL-WET-CBS]] | — | Done |
| ~~TNO-wet (1930)~~ | Added in Batch 3 as [[NL-TNO-WET]] | — | Done |
| ~~EU-GDPR → [[NL-AP]] link~~ | Closed in Batch 3: [[NL-AP]] now links to both [[NL-UAVG]] and [[EU-GDPR]] | — | Done |
| Wet bescherming persoonsgegevens (Wbp) | Predecessor regime replaced by GDPR/UAVG on 25 May 2018; needed for temporal completeness | Batch 4 or later | Batch 3 / 2026-08-14 |
| Aanpassingswet AVG (dossier 34.939) | Adjusted other Dutch legislation to the GDPR | Batch 4 or later | Batch 3 / 2026-08-14 |
| ~~Original NIS Directive~~ | Added in Batch 8 as [[EU-NIS]]; the [[NL-WBNI]] chain is now closed | — | Done |
| Wet weerbaarheid kritieke entiteiten (CER implementation) | Passed alongside the Cyberbeveiligingswet; adjacent to but distinct from NIS2 | Batch 4 or later | Batch 3 / 2026-08-14 |
| Rijksdienst voor Identiteitsgegevens (RvIG) | Administers the BRP under [[NL-WET-BRP]] | Batch 4 or later | Batch 3 / 2026-08-14 |
| NCSC / NCTV | Cybersecurity authorities named in Cyberbeveiligingswet sources | Batch 4 or later | Batch 3 / 2026-08-14 |
| eIDAS → [[NL-WDO]] link | Both eIDAS entities now exist; eIDAS 2.0 ruled out on dates, but the transposition from 910/2014 remains **unsourced** and unasserted | Batch 9+ | Batch 3; updated Batch 8 |
| Wet elektronische publicaties; Wet politiegegevens; Telecommunicatiewet | Further Dutch legislation with data relevance, not assessed in Batch 3 | Batch 4 or later | Batch 3 / 2026-08-14 |
| ISO / IEC / CEN → [[NL-NEN]] links | NEN's most significant relationships; need the international standards bodies | Batch 9 / 13 | Batch 2 / 2026-08-14 |
| ISO/IEC 27001 & 27002 → [[NL-BIO]] link | BIO2 is explicitly based on NEN-EN-ISO/IEC 27001:2023 and 27002:2022; the `based-on` relationship is unassertable until those entities exist | Batch 14 | Batch 4 / 2026-08-14 |
| **W3C DCAT → EU DCAT-AP → [[NL-DCAT-AP-NL]] chain** | A clean international→EU→national standards descent, and one of the clearest demonstrations available of what the Atlas is for. Complete it when Batches 9 and 14 land | Batch 9, 14 | Batch 4 / 2026-08-14 |
| ~~`DOMAIN-EDUCATION`~~ | Created in Batch 5; [[NL-SURF]] and [[NL-ROSA]] tagged | — | Done |
| ~~`DOMAIN-HEALTH`~~ | Created in Batch 5; [[NL-NICTIZ]] and [[NL-HEALTH-RI]] tagged | — | Done |
| ~~Health-RI~~ | Added in Batch 5 as [[NL-HEALTH-RI]] | — | Done |
| Topsector Logistiek | Originator of [[NL-ISHARE]]; needed to assert its `maintained-by` | Batch 10 | Batch 5 / 2026-08-14 |
| digiGO | Initiator of [[NL-DSGO]]; needed to assert its `maintained-by` | Batch 10 | Batch 5 / 2026-08-14 |
| DMI ecosystem; IDSA / IDS architecture | Named in iSHARE sources as data-space users of its trust framework | Batch 10 | Batch 5 / 2026-08-14 |
| Ministerie van Infrastructuur en Waterstaat; Rijkswaterstaat | Founding partners of [[NL-PDOK]] not yet modelled, making its founding collaboration look narrower than it was | Batch 5+ | Batch 5 / 2026-08-14 |
| Ministeries van VWS, EZK, OCW | Named partners of [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Groeifonds | Funds [[NL-HEALTH-RI]] | Batch 5+ | Batch 5 / 2026-08-14 |
| Nationaal Wegenbestand (NWB) | Part of the [[NL-NDW]] expansion | Batch 5+ | Batch 5 / 2026-08-14 |
| ~~EU ITS Directive~~ | Added in Batch 8 as [[EU-ITS-DIRECTIVE]]; the [[NL-NTM]] chain is now closed | — | Done |
| DANS, ODISSEI, RIVM, NWO, SIDN | Research/health/internet-infrastructure organisations still unqueued from Batch 2 | Batch 5+ | Batch 2; carried |
| ~~Official EUR-Lex text for eIDAS 2.0~~ | Found in Batch 8; both entities rebuilt | — | Done |
| ~~Original eIDAS Regulation (910/2014)~~ | Added in Batch 8 as [[EU-EIDAS]] | — | Done |
| ~~CER Directive~~ | Added in Batch 8 as [[EU-CER]] | — | Done |
| ~~Interoperable Europe Act~~ | Added in Batch 8 as [[EU-INTEROPERABLE-EUROPE-ACT]] | — | Done |
| Interoperable Europe Board | Adopts new EIF versions; needed to resolve the EIF/Act relationship | Batch 9 | Batch 7; carried |
| ENISA | Established under [[EU-CYBERSECURITY-ACT]]; relationship unassertable without it | Batch 9 | Batch 8 / 2026-08-14 |
| Free Flow of Non-Personal Data Regulation | Third repeal target of [[EU-DIGITAL-OMNIBUS]] | Batch 9 | Batch 8 / 2026-08-14 |
| Wet weerbaarheid kritieke entiteiten | Dutch CER transposition, approved 15 Apr 2026; should mirror [[NL-CBW]] → [[EU-NIS2]] | Batch 9+ | Batch 3; raised again Batch 8 |
| EUR-Lex citation for the AI Act | [[EU-AI-ACT]] lacks an Official Journal link | Batch 9 | Batch 8 / 2026-08-14 |
| Dutch EUDI Wallet implementation | Every member state must provide one; no Dutch arrangement researched | Batch 9+ | Batch 8 / 2026-08-14 |
| **The 10 remaining common European data spaces** | Batch 10 created Health, Mobility, Green Deal and Agriculture. **Not created:** cultural heritage, energy, finance, industry, language, media, public administrations, research and innovation, skills, tourism — research returned only their names in the list of fourteen | Later | Batch 7; narrowed Batch 10 |
| ~~ENISA~~ | Added in Batch 9 as [[EU-ENISA]] | — | Done |
| ~~Interoperable Europe Board~~ | Still not created — two passing mentions only | Later | Batch 7; carried |
| W3C source for DCAT | [[INTL-DCAT]] rests on second-hand descriptions; the top of the flagship standards chain | Batch 14 | Batch 9 / 2026-08-14 |
| W3C (the organisation) | Needed for [[INTL-DCAT]]'s `maintained-by` | Batch 13 | Batch 9 / 2026-08-14 |
| GeoDCAT-AP and StatDCAT-AP | Extensions of [[EU-DCAT-AP]]; GeoDCAT-AP would likely connect [[NL-GEONOVUM]]'s geo and metadata work | Later | Batch 9 / 2026-08-14 |
| ETSI standards | [[EU-ETSI]] exists but **no ETSI standard is modelled**, despite ICT standardisation being central to this Atlas | Later | Batch 9 / 2026-08-14 |
| Regulation (EU) 1025/2012; Regulation (EC) 223/2009 | Legal bases of the ESOs and the European Statistical System; described but not modelled | Later | Batch 9 / 2026-08-14 |
| EUR-Lex citation for EHDS Reg. (EU) 2025/327 | [[EU-EHDS]]'s strongest source is the Parliament's Legislative Observatory | Later | Batch 10 / 2026-08-14 |
| IDSA / IDS architecture | [[NL-ISHARE]]'s documented route into the EU data-space world | Later | Batch 5; carried |
| Environment / Energy / Agriculture domains | Still below the 2-entity threshold even after Batch 10 | Later | Batch 5; rechecked Batch 10 |
| EU AI strategy (if distinct from the AI Act) | Named in Batch 7 scope; no clearly identifiable standalone strategy document found | Batch 8 | Batch 7 / 2026-08-14 |
| Digital Europe Programme; EuroHPC | EU digital infrastructure funding instruments, not researched in Batch 7 | Batch 9 | Batch 7 / 2026-08-14 |
| Energy, Environment, Finance, Justice, Agriculture, Social Security, Built Environment domains | All named in the Batch 5 brief but each currently below the 2-entity threshold in taxonomy §1. Create as the ecosystems that would populate them are researched | Later | Batch 5 / 2026-08-14 |
| College Standaardisatie | Established in 2006 alongside Forum Standaardisatie; current status unknown — may be superseded, which would need a `supersedes` link | Batch 2 | Batch 1 / 2026-08-14 |
| Individual GDI services (DigiD, DigiD Machtigen, MijnOverheid, Digipoort) | Referenced by NL-GDI and NL-LOGIUS but not yet entities; decide whether they warrant separate entities | Batch 2 or 5 | Batch 1 / 2026-08-14 |
| GEMMA, EAR, ROSA, PETRA | NORA's derived reference architectures; need `derived-from`/`based-on` links to NL-NORA | Batch 4 | Batch 1 / 2026-08-14 |
| Individual open standards on the 'pas toe of leg uit' list | Referenced by NL-PAS-TOE-OF-LEG-UIT | Batch 4 | Batch 1 / 2026-08-14 |
| Meerjarenvisie Digitale Overheid; GDI programmeringsplan | Named as MIDO components; may warrant entities or may be publications | Batch 4 | Batch 1 / 2026-08-14 |
