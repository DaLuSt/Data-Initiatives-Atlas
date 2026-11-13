# Repository scan, 2026-11-13

A full pass over the repository looking for what could be better, in the widest sense: the data,
the sourcing, the tooling, the workflows, the site and the documents. This page is the record of
what was measured and where each finding went. It is a snapshot; the findings live in the places
named in the last column, and that is where they get closed.

**Method.** `python3 tools/check_all.py` (17 of 17 checks pass, so nothing here is a validation
failure); `validation/run_all.py` for its warnings; `site/graph.json` and its `stats` and `facets`
for the graph numbers; a scan of every entity's frontmatter and body for the counts below; a read of
the workflows, the tools, `site/index.html` and the documents. The numbers can be re-measured the
same way. Nothing was fetched from the web for the scan itself.

## What is in good shape

- Validation is clean, the graph build is deterministic, and every tool that posts or talks to an
  outside service has offline tests.
- All 1,286 entities are `verification: primary-source`; none has a degree below 3; no suspected
  duplicates were found (25 names or aliases are shared, all between different countries' bodies or
  laws, for example three "Data Protection Act 2018").
- 2,476 of 2,518 typed relationships are sourced facts; 42 are labelled interpretations.
- `last_verified` is never older than 2026-08-14, and `tools/verification_age.py` reports all ok.

## Findings and where they went

| # | Finding (measured 2026-11-13) | Kind | Recorded in |
|---|---|---|---|
| 1 | 184 entities cite Wikipedia (211 citations), often as a stand-in for a host that was blocked at the time | Sourcing | Roadmap [#767](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/767) |
| 2 | 64 entities say a source was read through a summarising tool; 447 say part of a source was not read | Sourcing | Roadmap [#768](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/768) |
| 3 | 92 entities are not linked from their own country's `index.md` (DE 20, NL 16, ES 15, GB 11, BE 7, FR 7); no check catches it | Data, tooling | Roadmap [#769](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/769) |
| 4 | 43 of 279 national laws have no link of any kind to an organisation; 104 have no typed relationship to one | Data | Roadmap [#770](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/770) |
| 5 | EU core instruments and bodies that existing entities point at are not entities: the Digital Services Act, the Digital Markets Act, the ePrivacy Directive, the Cyber Resilience Act, DORA, the European Data Innovation Board, the AI Office, data.europa.eu, the Once-Only Technical System | Coverage | Roadmap [#771](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/771); nine rows in `discovery/research-queue.md` |
| 6 | The site has no Open Graph or Twitter tags, no canonical link, no structured data, no sitemap or robots file, while LinkedIn posts now link to it | Site | Roadmap [#772](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/772) |
| 7 | Seven of ten workflows have no job timeout; actions are pinned by tag, not commit; the three LinkedIn workflows repeat steps; no code scanning; two tools have no tests | Infrastructure | Roadmap [#773](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/773) |
| 8 | 369 of 2,518 typed relationships are `related-to`; 234 entities have only `related-to` or `part-of` going out; 848 of 1,286 entities are `coverage: low` and 2 are `high` | Depth | Roadmap [#774](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/774) |
| 9 | 73 laws are `adopted` with no `start_date`; 701 `active` entities have none either | Data | Roadmap [#775](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/775) |
| 10 | `docs/performance.md` was measured at 855 entities; the graph is half as large again (1,286) | Site | A comment on roadmap #508 (the site at 200 countries) |
| 11 | `discovery/research-queue.md` held two leads and also said "Nothing is currently queued"; `state.yaml` said 0 queued and 1 candidate where there were 2 | Bookkeeping | Fixed in the same pull request |
| 12 | `docs/credentials.md` opened with "Nothing here is built yet", which stopped being true in October | Documents | Fixed in the same pull request |
| 13 | LinkedIn idea post 2 said the Atlas holds nine EU adequacy decisions; it holds eleven (Switzerland and the United Kingdom were already there), and six, not five, date from the old Directive | Documents | A separate pull request that waits for the owner, because it changes text the scheduled workflow posts |
| 14 | Four `superseded` entities have no `successor` (`NL-NOIV`, `NL-CCS`, `GB-DSIT`, the Dutch Werkagenda) and nine sources are cited over plain `http` | Data | Already reported by `validation/run_all.py` as warnings; no new item |
| 15 | Two pull requests of this session that touch workflows and the LinkedIn tools (#764, #766) were opened with auto-merge on, against step 7 of `.agent/operating-model.md`, which asks for the owner's word first | Process | `.agent/run-history/2026-11-13-repo-scan.yaml`; told to the owner. Both pipelines are off by default and nothing was posted |

## What was looked at and left alone

- **English names** (992 entities have no `name_en`): most names are English already; the rest is roadmap #446.
- **The regional layer and schema questions**: roadmap #539, #457, #506 and #513 already hold them.
- **Accessibility and real-device testing**: roadmap #497 and #452.
- **The 92 open rows of `discovery/unresolved.md`**: 9 were last touched in August, 14 in September, 54 in October and 15 in November; each is already matched to a roadmap item in `docs/roadmap.md`.
