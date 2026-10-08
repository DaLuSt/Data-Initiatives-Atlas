# Roadmap

The roadmap is a set of **GitHub issues labelled `roadmap`**, shown on the
public **[Atlas roadmap board](https://github.com/users/DaLuSt/projects/1)**, with each item aimed at a **data
release**. It sits beside,
not instead of, the repository's research notes:

| Where | What it holds |
|---|---|
| **Roadmap issues** (label `roadmap`) | A deliverable someone could finish in a few pull requests, with an outcome and an owner-visible status |
| `progress/backlog.md` | The detailed batch-by-batch plan and the reasoning behind it (history, not status) |
| `discovery/unresolved.md` | Open questions about existing entities; never guess to close one |
| `discovery/candidates.md`, `research-queue.md` | Unsourced leads and scoped research leads |

An issue links to the note it comes from; the note does not need to link back.

## Labels

`roadmap` on every item, plus one area label:

| Label | For |
|---|---|
| `area:data` | New or corrected entities and relationships |
| `area:site` | The interactive site and its features |
| `area:schema` | The data model (a schema version bump, see `metadata/versioning.md`) |
| `area:research` | Sourcing and verification work, including re-verification |
| `area:infra` | Tooling, CI, releases |

## Milestones are data releases

A milestone is named after the month it is aimed at, in the form the data
release uses (`2026.11`). The release that month closes the milestone. An item
with no milestone is not scheduled. Moving an item between milestones is how the
plan changes; there is no other schedule.

## The board

The [Project board](https://github.com/users/DaLuSt/projects/1) has four columns, the values of its **Status** field:
**Backlog** (not scheduled), **Next** (aimed at the coming release),
**In Progress** and **Done**, plus a second view, a table grouped by milestone,
named *By release*. The board's built-in workflows move an issue to *Done*
when it closes and add new `roadmap` issues to *Backlog*.

A workflow keeps it in step with the issues (next section). It was set up by
the owner on 2026-10-07 and made public. Setting one up is a few
minutes in the GitHub UI: Projects v2 can only be created through GitHub's
GraphQL API or the web UI, and the agent's environment blocks GraphQL and every
path outside this repository. The steps, for rebuilding it:

1. <https://github.com/DaLuSt?tab=projects> → *New project* → *Board* → *Atlas roadmap*.
2. *Settings → Status*: rename *Todo* to *Backlog*, add *Next* after it, keep
   *In Progress* and *Done*.
3. *Workflows*: *Item added to project* → Status *Backlog*; *Item closed* → Status
   *Done*; *Auto-add to project* → this repository, filter
   `is:issue label:roadmap`.
4. Add the issues that already exist (auto-add only catches new ones): *+ Add item*,
   paste `repo:DaLuSt/Data-Initiatives-Atlas label:roadmap is:open`, select all.
5. *New view → Table*, group by *Milestone*, name it *By release*.
6. Optionally make the board public and link it to the repository.

### Automatic sync

`.github/workflows/project-board.yml` runs `tools/project_board.py` whenever a
`roadmap` issue is opened, closed, reopened, labelled, unlabelled or moved to
another milestone, and every Monday as a safety net. One run:

- adds every `roadmap` issue that is not on the board yet;
- sets **Status** to *Done* for a closed issue, and to *Backlog* for an open one
  that has no status; *Next* and *In Progress* are the owner's choices and are
  never overwritten;
- sets **Start date** (first day of the milestone's month) and **Target date**
  (the milestone's due date), which is what the Roadmap (timeline) layout draws
  bars from; an issue with no milestone keeps the dates it has;
- creates the two date fields if the board lacks them.

It never removes an item and never edits an issue. The agent cannot do this
itself, because its environment blocks GraphQL; the workflow runs on GitHub's
side.

**One-time setup (owner).**

1. Create a *classic* personal access token with the `project` scope only
   (<https://github.com/settings/tokens>; a user-owned project cannot be edited
   with the built-in `GITHUB_TOKEN` or a fine-grained token). Give it an expiry
   and note the date: when it expires the workflow fails and the board stops
   updating.
2. Store it as a **repository secret** named `PROJECT_TOKEN` (repository
   *Settings → Secrets and variables → Actions → New repository secret*), not in
   the Claude environment.
3. *Actions → Roadmap board → Run workflow* with *dry_run* ticked and read the
   log. It lists what it would change and changes nothing.
4. Run it again with *dry_run* unticked. After that, events keep it current.

The token expires: the plan for renewing it and for noticing a failure is in
[`credentials.md`](credentials.md) (issue #496). Until the secret exists the workflow succeeds and does nothing. Then, in the
board, add a view with the *Roadmap* layout and set its start and end to
**Start date** and **Target date**. Views are not available through the
workflow's token.

## The plan at a glance (snapshot, 2026-10-08)

This is a reading of the milestones on one day, to show roughly what is aimed at
which release. The live version is the milestones and the board; this table ages.
Each month is one data release. The country groups (the `Next countries` items under
#451) are a placeholder pace of one group per month: they are the part of the plan
most likely to move. From 2027.01 the plan also adds the regional layer (#539, the 22 UN
sub-regions, two per month, ending 2027.11): each sub-region's regional bodies and
instruments, not the country anchors. A month with many items is not a promise that all of them fit.

| Release | Data and research | Site and tooling | Decisions and schema |
|---|---|---|---|
| **2026.10** (now) | Weekly release pull requests continue; LinkedIn post drafts open as issues | Board sync, shared checks, Node 24 actions and the accessibility statement are done | |
| **2026.11** | #446 English names for the last records; #459 UK gaps; #527 successor links | | |
| **2026.12** | #495 read the blocked sources on GitHub's runners | #526 repair the browser tests; #496 token expiry plan; #452 test with real visitors | #533 founding-six date; #449 rank gaps; #450 which thin domains to deepen |
| **2027.01** | regions: #540 W Europe and #541 N Europe; #470 countries, group 1; #502 re-check Q1 | #497 accessibility audit; #515 LinkedIn auto-post (needs a LinkedIn app); #528 checks into the validators; #498 release cadence review | |
| **2027.02** | regions: #542 S Europe and #543 E Europe; #471 countries, group 2; #534 eIDAS cluster; #535 Germany's three questions | | #499 records that fit two types; #457 vocabulary decisions |
| **2027.03** | regions: #544 N America and #545 S America; #472 countries, group 3; #500 data spaces; #501 standards bodies; #460 coverage gaps | | |
| **2027.04** | regions: #546 C America and #547 Caribbean; #473 countries, group 4; #503 re-check Q2 | #507 load time on slow networks | #506 multilingual names; #458 Dutch registers and authentic data |
| **2027.05** | regions: #548 N Africa and #549 W Africa; #474 countries, group 5; #536 Dutch registry edges; #537 EU and UN links | | |
| **2027.06** | regions: #550 E Africa and #551 Middle Africa; #475 countries, group 6 | #508 the site at 200 countries | #509 EU institutions; #461 consistency checks |
| **2027.07** | regions: #552 S Africa and #553 W Asia; #476 countries, group 7; #504 re-check Q3 | #510 annual re-verification policy | |
| **2027.08** | regions: #554 C Asia and #555 S Asia; #477 countries, group 8 | | #511 UN system and development banks |
| **2027.09** | regions: #556 E Asia and #557 SE Asia; #478 countries, group 9 | #512 linked-data export (a proposal) | |
| **2027.10** | regions: #558 Australia and NZ and #559 Melanesia; #479 countries, group 10; #505 re-check Q4 | | |
| **2027.11** | regions: #560 Micronesia and #561 Polynesia (#539, the umbrella for the regions, closes); #480 countries, group 11 | | |
| **2027.12** | #481 countries, group 12 | | |
| **2028.01** | #482 countries, group 13 | | #513 is a schema 2.0 needed? |
| **2028.02** | #483 countries, group 14; #451 (the umbrella for all the country groups) closes | | |

**Dependencies worth knowing.** #495 (blocked sources) comes before the research items
that were stopped by a blocked page (#534, #535, #537). #458 (Dutch modelling) comes before
#536. #457 and #499 (vocabulary and types) come before #513 (does the schema need a major
version). The accessibility audit (#497) rewrites `ACCESSIBILITY.md`.
The regional layer (#539) needs the owner's answer on whether regions are blocs only (the
recommendation) before #540 starts; #511 (UN system) holds the UN regional commissions.

### Where each open question in `discovery/` lives

Every open row of `discovery/unresolved.md` was read on 2026-10-08. Rows that are recorded
declines (#229, #230, #231, #232) or deliberate non-assertions (#88, #97, #116) need no work.

| Rows | Roadmap item |
|---|---|
| #2 | #533 |
| #4, #70, #179, #216 to #225 (blocked sources) | #495, then the items that were waiting on a page |
| #8, #43, #66, #120, #124, #125 | #500 |
| #9 | #506 |
| #11 | #449 |
| #12, #31, #144 | #458, #536 |
| #13, #44, #53, #54, #92, #93, #153, #154 | #457 |
| #15, #16 | #509 |
| #17, #18, #226 | #535 |
| #19 to #27, #29, #32 | #499 |
| #35, #36 | #534 |
| #90, #91, #95, #117, #139 | #502 to #505 (quarterly re-checks) |
| #141, #150 | #536 |
| #168 | #511 |
| #174, #227 | #537 |
| #187, #200, #209 | #501 |
| #233 | #446 |
| #234 | #459 |
| #5 | mostly done (the `subnational` level exists and is used for Belgium, Germany and Spain); the row is a candidate for closing |

`discovery/candidates.md` C9 (thin domains) is #450 and C10 (countries) is #451 and its
fourteen groups; `discovery/research-queue.md` and `discovery/duplicates.md` are empty.

## How an item gets done

- Work happens in ordinary pull requests. The pull request that finishes an
  item says `Closes #N` in its body, so the issue closes when it merges.
- Autonomous sessions pick work by `.agent/operating-model.md`'s priority order;
  a roadmap item the owner has put in *Next* comes first.
- The release pull request lists every closed `roadmap` issue since the last
  release under *Roadmap items completed* (`metadata/versioning.md`).

## Proposing an item

Open an issue with the *Roadmap item* template. Say what is true when it is
done, and why it matters; link the backlog entry, `unresolved.md` row or finding
it came from.
