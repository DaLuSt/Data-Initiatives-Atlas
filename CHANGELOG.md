# Changelog

What changed in each release of the Atlas. Entries are written by
`tools/release.py` into a release pull request (see
[`metadata/versioning.md`](metadata/versioning.md)); the newest is first. The
Atlas has two version numbers: a **schema version** (SemVer) for the data model
and a dated **data release** (`YYYY.MM.N`) for each snapshot.

<!-- releases:start -->

## Data release 2026.10.5 — 2026-10-26

**Schema 1.0.0** (unchanged)

In the Atlas at this release: 1,032 entities (+56), 2,167 typed relationships (+223), 114 countries (+0).

### Data

- Housekeeping: two closed Horizon projects completed; closing rule and auto-merge fallback documented (#691)
- Housekeeping: warnings 26 to 13, docs current, run-history closed; regions #552, #554, #556, #557, #558 closed (#689)
- Regions (#558): the Pacific Islands Forum, its 2050 Strategy, the Lagatoi Declaration and its personal information policy (#688)
- Regions (#554): the SCO, its information security expert group and the 2009 agreement (#687)
- Regions (#551): CEMAC and its directive on the rights of users of electronic communications (#686)
- Regions (#550): COMESA, the EGEE-ICT programme and its draft data protection model law (#685)
- Regions (#553): the GCC and its 2023 personal information protection framework (#684)
- Regions (#545): the Pacific Alliance and its Regional Digital Market roadmap (#683)
- Regions (#547): HIPCAR and its privacy and data protection model legislation (#682)
- Regions (#556): APEC's Privacy Framework and Roadmap, and the Global CBPR Forum and its Declaration (#681)
- Regions (#552): SADC, its data protection model law and its 2001 ICT declaration (#680)
- Regions (#557): ASEAN's Framework on Personal Data Protection and Framework on Digital Data Governance (#679)
- Regions (#549): ECOWAS and its 2010 Supplementary Act on personal data protection (#678)
- Regions (#548): the African Union, the Malabo Convention, the Data Policy Framework and the Digital Transformation Strategy (#677)
- Regions (#547): the OECS, its Revised Treaty, the Regional Data Governance Council and the statistics strategy (#676)
- Regions (#547): CARICOM, its Secretariat's data protection rules, the CTU and the Single ICT Space (#675)
- Regions (#545): MERCOSUR, its electronic commerce subgroup and the 2021 e-commerce agreement (#673)
- Regions (#544): the USMCA, its digital trade chapter and the Free Trade Commission (#672)
- Regions (#543): the Black Sea Economic Cooperation organisation and its ICT work (#669)

### Tooling

- Housekeeping: #510 age rule and report for last_verified; run-history closed (#671)
- CI: run the browser suite as two parallel shards (#670)

### Documentation

- Housekeeping: performance re-measured at 1,032 entities, C9 re-measured, status lines current (#690)
- Regions (#540-#544): closed, with the gaps recorded in row #256 (#674)

### Housekeeping

- 1 pull request that only record progress in the repository's own files (#668)

### Roadmap items completed

- Next regions: Australia and New Zealand (Oceania), regional bodies and instruments (#558)
- Next regions: South-eastern Asia (Asia), regional bodies and instruments (#557)
- Next regions: Eastern Asia (Asia), regional bodies and instruments (#556)
- Next regions: Central Asia (Asia), regional bodies and instruments (#554)
- Next regions: Southern Africa (Africa), regional bodies and instruments (#552)
- Next regions: Northern America (Americas), regional bodies and instruments (#544)
- Next regions: Eastern Europe (Europe), regional bodies and instruments (#543)
- Next regions: Southern Europe (Europe), regional bodies and instruments (#542)
- Next regions: Northern Europe (Europe), regional bodies and instruments (#541)
- Next regions: Western Europe (Europe), regional bodies and instruments (#540)
- Annual re-verification: how old may `last_verified` get, and who checks (#510)
- Next countries, group 02 of 14 (10): Benin, Botswana, Egypt, +7 (#471)
- Thin domains: 13 of 20 domains appear in only one or two countries (#450)

## Data release 2026.10.4 — 2026-10-19

**Schema 1.0.0** (unchanged)

In the Atlas at this release: 976 entities (+121), 1,944 typed relationships (+240), 114 countries (+25).

### Schema

- Close rows #5 and #19 of unresolved.md; keep the Lower Saxony question as row #243 (#635)
- Data spaces (#500): what country means for an initiative that operates across borders; row #8 closed (#633)
- EU Directorates-General and the adoption step (#509): rule, DG EMPL, rows #15 and #16 closed (#632)

### Site and features

- Site (#508): an overview as the first screen, and the force layout stored at build time (#655)
- Countries (#479): Australia and Panama; force-layout limit raised to 1,100 (#654)
- Site: hover card inside a landmark (axe), contrast checks for it, and a status-line hint (#648)
- Hover card: an entity's core information on hover and focus (#640) (#642)
- Scale check at 194 countries: a Find a country box and the findings (#508) (#628)

### Data

- Countries (#480): Côte d'Ivoire; re-check (#502): NL-BRO (#663)
- Regions (#541): the Nordic Council of Ministers and its 2025-2030 digitalisation programme (#665)
- Countries (#477): Costa Rica and Burkina Faso (#662)
- Countries (#478, #483): Zimbabwe and Cameroon (#661)
- Countries (#481, #483): Ghana and Colombia (#660)
- Countries (#482, #483): China and Tanzania (#659)
- Countries (#481, #482, #483): Brazil, Japan and Malaysia (#657)
- Countries (#478): New Zealand, Peru, Ecuador and Trinidad and Tobago (#656)
- Countries (#475, #476): Nigeria and Pakistan, from official sites (#653)
- Countries (#474, #476): Vanuatu, Barbados, Seychelles and Bolivia, each from an official page (#652)
- Housekeeping and #450: tag Poland's NIS2 act with its six added sectors; docs counts (#651)
- Re-check (#502): PL-KSC was signed with a Constitutional Tribunal referral; the Spanish AI bill's stage (#650)
- UK (#459): BS 10012, the British Standard for personal information management, withdrawn in April 2026 (#647)
- Regions (#541-#543): the Union for the Mediterranean's digital declaration and the CIS Assembly's model code (#638)
- Regions (#542, #543): CEFTA's digital decisions and the Eurasian Economic Union's e-signature rules (#636)

### Tooling

- Release review (#498): count from the previous preparation, not its tag; one line for housekeeping (#631)
- CI speed: one list of checks, shared builds in the tests, cancel superseded PR runs (#629)
- Load time: measure it, set a budget, guard the file sizes (#507) (#627)
- LinkedIn workflow: read the data release without PyYAML (#624)

### Documentation

- Housekeeping: run-history closed, roadmap and build-output docs current (#664)
- Roadmap: the world-map decision is #645 (2026.12); #508 waits on it (#646)
- Board token variables set: record it and close #496's plan (#644)
- Roadmap: add the hover card (#640) to the 2026.11 plan (#641)
- Housekeeping: close the open run-history entries; map row #246 (#639)
- Housekeeping: close the open run-history entries, correct the regions count, map rows #244 and #245 (#637)
- Housekeeping and a docs check: README tree, roadmap plan, workflows page, test commands and statuses brought up to date (#634)
- Housekeeping: close the #507, #508 and CI-speed entries; record the world-map decision (#630)
- Housekeeping: release 2026.10.3, the LinkedIn fix and the late schedule (#625)

### Housekeeping

- 3 pull requests that only record progress in the repository's own files (#649, #643, #626)

### Roadmap items completed

- Hover card: show an entity's core information when the pointer rests on it (#640)
- EU institutions: the Directorates-General and the legislative-adoption step (#509)
- Load time on slow networks: the size of graph.json and details.json (#507)
- Review the release cadence and the changelog after the first three data releases (#498)
- Plan for the PROJECT_TOKEN expiring: rotation steps and a visible failure (#496)

## Data release 2026.10.3 — 2026-10-12

**Schema 1.0.0** (unchanged)

In the Atlas at this release: 855 entities (+110), 1,704 typed relationships (+128), 89 countries (+31).

### Highlights

- Coverage grows from 58 to 89 countries, each added from official sources; what could not be read is recorded openly.
- The site is more accessible: an accessibility statement, a barrier-report form, a working "Skip to content" link and contrast fixes.

### Schema

- Netherlands registers (#458, #536): decisions, NL-AWR, NL-DEFENSIE (#609)
- Germany (#535): RegMoG register count traced to the § 91a register; KoSIT and BundID decided (#608)
- Types (#499): one rule for records that fit two types, and a decision for each (#604)
- Scope edges (#461): marked in the graph, counted, and hideable on the site (#601)
- Owner decisions: decline a code field (#449), membership dates follow the Union's list (#533) (#594)
- Consistency decisions (#461): GDPR authority edge, own-country applies-in, unknown domains held by a test (#593)

### Site and features

- Country group 3 (#472): Canada, Sri Lanka, Gabon, São Tomé and Príncipe, The Gambia, Malawi (#615)
- Accessibility audit (#497): contrast and target-size fixes, the report, an updated statement (#590)
- Add ACCESSIBILITY.md and an accessibility-barrier form; make "Skip to content" skip to the visible main area (#532)
- Site: a mistyped or truncated address no longer reports "graph could not be loaded"; source links accept only http(s) (#523)

### Data

- Country group 7 (#476): Jamaica (#621)
- Statistics bodies (#459), third pass: Sweden's ROS and Germany's Statistischer Beirat (#620)
- Country group 6 (#475): United Arab Emirates and Singapore (#619)
- Country group 5 (#474): add Kyrgyzstan (#618)
- Country group 5 (#474): South Africa and Republic of Korea (#617)
- Country group 4 (#473): Chile, Togo, Ethiopia, Paraguay (#616)
- Country group 2 (#471): eight countries from their own government pages (#614)
- Statistics oversight (#459), second pass: Austria's Statistikrat and Ireland's NSB (#613)
- Statistics oversight bodies (#459): ESGAB, its Decision, and the French ASP (#612)
- Country group 1 (#470): Haiti and Timor-Leste (#611)
- UN and EU links (#537): the AI Act and INSPIRE read in full; the UN-GGIM Europe link found (#607)
- eIDAS (#534): the regulation's own text, and the Wdo answer from the Eerste Kamer dossier (#606)
- Re-check (#502): the Irish cyber bill, and the Spanish organic AI bill now sourced (#602)
- English names (#446): five more, from the bodies' own English pages read on a runner (#600)
- Regions (#540): the Benelux Union and its 2016 Digital Benelux declaration (#599)
- Thin domains (#450): social security, built environment and education (#598)
- Thin domains (#450): seven sectors tagged from the annexes of the German, Belgian and Luxembourg NIS2 acts (#597)
- Thin domains (#450): Austria's Umweltinformationsgesetz (#596)
- Thin domains (#450): environment and finance deepened with four national instruments (#595)
- Country group 1 (#470): anchors and a first sourced slice for Kenya, the Philippines, Uzbekistan, Nepal and Somalia (#591)
- English names for BOSA and data.gov.be, read on a runner (#446) (#587)
- UK: add the Office for Statistics Regulation and OS of Northern Ireland (#459); EU-EIDAS2 amends EU-EIDAS (#527) (#570)
- Roadmap 2026.11: Node 24 actions, one shared set of checks for PRs and deploys, succession links, data-correction form (#531)
- Validation: fix a crash on an impossible date and close seven gaps found by injecting defects (#524)

### Tooling

- Optimisations: count updater with a CI check, stale row-reference warning, page text in the reader's log, a split unresolved table (#605)
- Tests: parse the entity files once per run in test_build_graph.py (82 s to 42 s) (#592)
- Draft issue: remind the owner to post on the LinkedIn Page by hand (#589)
- Browser suite: repair tools/test_ui.mjs and run it in CI as a separate job (#526) (#584)
- Validators: an unknown country, successor or previous_version now fails run_all.py (#528) (#585)
- Board token watch: expiry warning, failure on a missing or expired token, one issue (#496) (#583)
- Read pages on a runner: a workflow and tool for hosts only a runner can read (#446, #495) (#582)
- Probe results (#495): which blocked hosts a runner can read; same-text shell detection (#581)
- Host probe: which hard-to-read sources can a GitHub runner read (#495) (#579)
- LinkedIn workflow: show the text on the run's summary page (#577)
- LinkedIn: the posting tool and the approval-gated workflow (#515) (#576)
- LinkedIn auth: paste mode for Codespaces (#515) (#575)
- LinkedIn: the authorisation script, tested, with run instructions (#515) (#574)
- Actions: Bump the actions group across 1 directory with 2 updates (#569)
- Validation: Update pyyaml requirement from >=6.0 to >=6.0.3 in /validation in the validation-dependencies group (#568)
- Add Dependabot for Actions and the validation dependency, and a pull request template (#567)
- Release PR: start the required validate check on the release branch (#566)
- Branching: remove the autonomous-agent workflow, move the per-PR log out of state.yaml, document the branch and merge rules (#564)
- Release changelog: file metadata/rank-basis.md under Data, not Schema (#521)
- LinkedIn draft: list Site, Data and Schema changes only, and use a Highlights section when there is one (#519)

### Documentation

- Drafts for the LinkedIn Page: an introduction post and the latest release (#588)
- LinkedIn: record the decision for the own developer app (#515) (#572)
- Plans for the PROJECT_TOKEN expiry (#496) and the LinkedIn developer app (#515) (#562)
- Housekeeping and the release plan: record #530 to #532, and a month-by-month table in docs/roadmap.md (#538)

### Housekeeping

- English names, fifth pass (#446): no new names; rule for the long tail (#610)
- Re-checks (#501, #502): what a runner read of twelve standards-body pages and a round of searches did and did not settle (#603)
- Operating model: turn on auto-merge on each pull request that does not need the owner's word (#586)
- Operating model: record the owner's standing permission to merge own PRs when CI is green (#580)
- Housekeeping: record #571 and #572 as merged (#573)
- Housekeeping: record #567, #568, #569 and #570 as merged (#571)
- Housekeeping: record #538 and #562 as merged (#563)
- Housekeeping: record #525 and the four roadmap issues from the checks audit (#526-#529) (#530)
- Housekeeping: record #522, #523 and #524 and the site QA and checks audit in state.yaml and run-history (#525)
- Housekeeping: record #520 and #521 in state.yaml and run-history (#522)
- Housekeeping: record #516, #517 and #519 and the 2026.10.2 release in state.yaml and run-history (#520)

### Roadmap items completed

- EU and UN links that have never been sourced: INSPIRE and UN-GGIM, the AI Act and the UNESCO recommendation (#537)
- Netherlands: the base registries' remaining edges (vehicle register and the GDPR, the Besluit/Regeling layer, Defence) (#536)
- The eIDAS cluster: the regulation's own text, and whether the Dutch Wdo transposes it (#534)
- Decide the date the six founding EU members are keyed on (1957 signature or 1958 entry into force) (#533)
- Make the deploy workflow run the same checks as the pull-request workflow (#529)
- Move the three generator-only checks into the validators so both say the same thing (#528)
- Two successors that do not link back: add the reverse link, or a check that notices (#527)
- Repair the browser test suite (tools/test_ui.mjs) and run a smoke version of it in CI (#526)
- Post new data releases to LinkedIn automatically, after the owner approves (needs a LinkedIn app) (#515)
- Decide the type of records that fit two types (Dutch frameworks and platforms, SEMIC, DSSC, UN-CES, JTC 1) (#499)
- Read the blocked sources: run re-verification on GitHub's own runners (#495)
- A "data correction" issue template for readers who find a wrong claim (#494)
- Move the GitHub Actions to versions that run on Node 24 (#493)
- Consistency checks: GDPR supervisory authorities, applies-in to one's own country, domain facets, anchor edges (#461)
- Netherlands: how to model authentic data, municipalities and registers (#458)
- Close the remaining gaps in the constitutional-rank designations (#449)

## Data release 2026.10.2 — 2026-10-08

**Schema 1.0.0** (unchanged)

In the Atlas at this release: 745 entities (+5), 1,576 typed relationships (+11), 58 countries (+0).

### Site and features

- List view: download the rows on screen as CSV (#456)
- Explorer: stop animating the rings out from the origin (no more invalid-endpoint warnings) (#455)

### Data

- Record what the fetch tool and curl can and cannot read (EUR-Lex, Légifrance and others) (#466)
- Rank basis: close the Portuguese and UK gaps, leave the IT-CAD form question for you (#465)
- UK: the Gas and Electricity Markets Authority, Civil Aviation Authority and Drinking Water Quality Regulator for Scotland as NIS competent authorities (roadmap #459) (#491)
- France: FR-LRN implements-requirement-from the Open Data Directive (EUR-Lex register); EuroGeographics related-to INSPIRE (roadmap #460) (#490)
- English names: 26 more name_en values from the bodies' own English sites and official translations (roadmap #446) (#486)
- Docs sweep: correct README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY and countries/README (#484)
- UK: the Information Commission succeeds the ICO (30 Sep 2026); add the Re-use of PSI Regulations 2015; GOV.UK sources for DCMS and DSIT (#468)

### Tooling

- Releases: open an issue with a LinkedIn post draft when a release is published (#514)
- Roadmap board: a workflow that keeps the Project board in step with the roadmap issues (#488)

### Documentation

- Roadmap: link the public Project board; record #467 and #468 (#469)
- Roadmap docs: exact steps for setting up the Project board; record why the agent cannot (#464)

### Housekeeping

- Housekeeping: record #492 and #514, the longer-term roadmap and the LinkedIn draft in state.yaml and run-history (#516)
- Housekeeping: record #489, #490 and #491 in state.yaml and run-history (#492)
- Housekeeping: record #487 and #488 and the first board sync in state.yaml and run-history (#489)
- Housekeeping: record #485 and #486 in state.yaml and run-history (#487)
- Housekeeping: record #469 and #484 in state.yaml and run-history (#485)
- Housekeeping: record #463-466 in state.yaml and run-history (#467)
- Housekeeping: record #454, #455, #456 and #462 in state.yaml and run-history (#463)
- Reconcile progress/backlog.md: 39 items done or superseded, 30 open items pointed to roadmap issues #457-461 (#462)
- Housekeeping: record #441, #442 and the first release (#453) in state.yaml and run-history (#454)

### Roadmap items completed

- Reconcile progress/backlog.md with the current state of the Atlas (#448)
- Explorer logs "edge has invalid endpoints" warnings when the depth changes (#447)
- CSV export of the List view (#445)
- Set up the roadmap Project board (#444)
- Review and merge the first release pull request (#443)

## Data release 2026.10.1 — 2026-10-06

**Schema 1.0.0**

In the Atlas at this release: 740 entities, 1,565 typed relationships, 58 countries.

This is the first tagged release. The changes before it are not listed here: they are in the git history (`git log`) and, from 2026-09-26, in `.agent/run-history/`. Schema changes before versioning are listed in `metadata/versioning.md`.

<!-- releases:end -->
