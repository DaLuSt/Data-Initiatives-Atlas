# Changelog

What changed in each release of the Atlas. Entries are written by
`tools/release.py` into a release pull request (see
[`metadata/versioning.md`](metadata/versioning.md)); the newest is first. The
Atlas has two version numbers: a **schema version** (SemVer) for the data model
and a dated **data release** (`YYYY.MM.N`) for each snapshot.

<!-- releases:start -->

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
