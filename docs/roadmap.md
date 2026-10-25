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

## The plan at a glance (snapshot, 2026-10-24)

This is a reading of the milestones on one day, to show roughly what is aimed at
which release. The live version is the milestones and the board; this table ages.
Each month is one data release. The country groups (the `Next countries` items under
#451) are a placeholder pace of one group per month: they are the part of the plan
most likely to move. From 2027.01 the plan also adds the regional layer (#539, the 22 UN
sub-regions, two per month, ending 2027.11): each sub-region's regional bodies and
instruments, not the country anchors. A month with many items is not a promise that all of them fit.

**Done so far (39 items, 2026-10-07 to 2026-10-24):** the first release and the board (#443, #444);
CSV export and the Explorer fix (#445, #447); the backlog reconciled (#448); the constitutional-rank gaps and the
founding-six date (#449, #533); the consistency checks (#461) and the move of the generator-only checks into the
validators (#528); the Dutch registers (#458, #536); the eIDAS cluster (#534); the EU and UN links (#537); the
Node 24 actions, the data-correction form and the same checks for deploys (#493, #494, #529); the blocked sources
read on runners (#495); the browser tests (#526); successor links (#527); automatic LinkedIn posts (#515); the
types decision (#499); load time (#507); the release review (#498); the Directorates-General (#509); the hover card with an entity's core information (#640); the board token's expiry plan (#496); the age rule and report for `last_verified` (#510); thin domains (#450, built environment stays at 2 countries and is recorded in `discovery/candidates.md` C9); country group 2 (#471, two countries unreadable: row #237); and the regional items for Western, Northern, Southern and Eastern Europe and Northern America (#540 to #544, closed with what could not be read in row #256); and the regional items for Southern Africa, Central Asia, Eastern Asia, South-eastern Asia and Australia and New Zealand (#552, #554, #556, #557, #558, closed with what could not be read in row #271).
Part of #500 (what `country` means) and of #508 (the Country filter, the overview as the first screen, and the force layout stored at build time) is done; the rest of each is below. The country groups have each had a first slice; how many of the 193 UN member states still have no anchor is in `discovery/candidates.md` C10 (it was 97 anchors on 2026-10-16 and about 114 a day later). The groups' issues stay open for the countries whose laws could not be read.

| Release | Data and research | Site and tooling | Decisions and schema |
|---|---|---|---|
| **2026.11** | #446 English names for the last records; #459 UK gaps | #578 renew the LinkedIn token |  |
| **2026.12** | | #645 the world map: decide what it is for, then make it usable | The owner's choice among three options (#645) |
| **2027.01** | #470 countries, group 1; #502 re-check Q1 | #497 manual accessibility checks |  |
| **2027.02** | #535 Germany's § 91a question | #452 test with real visitors and devices | #457 vocabulary decisions |
| **2027.03** | regions: #545 S America; #472 countries, group 3; #460 coverage gaps; #500 data spaces (three parts left); #501 standards bodies |  |  |
| **2027.04** | regions: #546 C America and #547 Caribbean; #473 countries, group 4; #503 re-check Q2 |  | #506 multilingual names |
| **2027.05** | regions: #548 N Africa and #549 W Africa; #474 countries, group 5 |  |  |
| **2027.06** | regions: #550 E Africa and #551 Middle Africa; #475 countries, group 6 | #508 the site at 200 countries (map decision open) |  |
| **2027.07** | regions: #553 W Asia; #476 countries, group 7; #504 re-check Q3 |  |  |
| **2027.08** | regions: #555 S Asia; #477 countries, group 8 |  | #511 UN system and development banks |
| **2027.09** | #478 countries, group 9 | #512 linked-data export (a proposal) |  |
| **2027.10** | regions: #559 Melanesia; #479 countries, group 10; #505 re-check Q4 |  |  |
| **2027.11** | regions: #560 Micronesia and #561 Polynesia; #480 countries, group 11; #539 the regional layer (umbrella) |  |  |
| **2027.12** | #481 countries, group 12 |  |  |
| **2028.01** | #482 countries, group 13 |  | #513 is a schema 2.0 needed? |
| **2028.02** | #483 countries, group 14; #451 the country groups (umbrella) |  |  |

**Dependencies worth knowing.** #457 (vocabulary decisions) comes before #513 (does the schema need a
major version). The manual accessibility checks (#497) update `ACCESSIBILITY.md`. #508 waits for the owner's
decision on the world map (#645, `.agent/needs-human/world-map-fit.md`). The regional layer (#539) needs the owner's
answer on whether regions are blocs only (the recommendation) before #540 starts; #511 (UN system) holds the UN
regional commissions. #578 (the LinkedIn token) needs the owner.

### Where each open question in `discovery/` lives

Every open row of `discovery/unresolved.md` was matched to an item on 2026-10-13. Rows that are
recorded declines (#229, #230, #231, #232) or deliberate non-assertions (#88, #97, #116) need no work.

| Rows | Roadmap item |
|---|---|
| #43, #66, #120, #124, #125 | #500 (row #8, what `country` means, is decided) |
| #4, #70, #179, #216 to #220, #222 to #225 (blocked sources) | the items that were waiting on a page; #495 found what a runner can read (row #235 records it) |
| #9 | #506 |
| #11 | declined by the owner on 2026-10-09; the row keeps the unranked instruments |
| #12 | the Dutch registers, decided in #458 and #536; the row keeps the vocabulary questions |
| #13, #44, #53, #54, #92, #93, #153, #154 | #457 |
| #90, #91, #117, #139 | #502 to #505 (quarterly re-checks) |
| #168 | #511 |
| #187, #200, #209 | #501 |
| #226 | #535 |
| #243 | none yet (Lower Saxony: Dataport and IT.Niedersachsen; a source is needed) |
| #244 | #542 (CEFTA's digital instruments: what is left unread) |
| #245 | #543 (the Eurasian Economic Union's digital instruments: what is left unread) |
| #246 | #542, #543 (the Union for the Mediterranean and the CIS Assembly: what is left unread; the bodies looked at with nothing found) |
| #233 | #446 |
| #234 | #459 |
| #236 to #242, #247 to #253 | #470 to #483 (the countries of each group whose laws were not read) |
| #254 | #544 (closed; the USMCA's unread chapters and the 2026 joint review) |
| #255, #265 | #545 (MERCOSUR and the Pacific Alliance; the Andean Community is not modelled) |
| #256, #271 | the closed regional items #540 to #544, #552, #554, #556, #557, #558: what was left when each was closed |
| #257, #258, #264 | #547 (CARICOM, the OECS and HIPCAR; the Association of Caribbean States is unread) |
| #259, #260, #267, #268 | #548 to #551 (the African Union, ECOWAS, COMESA and the EGEE-ICT draft, CEMAC) |
| #261 to #263, #269 | #554, #556, #557, #552 (closed: ASEAN, APEC and the Global CBPR Forum, the SCO, SADC) |
| #266 | #553 (the GCC) |
| #270 | #558 to #561 (the Pacific Islands Forum; #558 closed) |

`discovery/candidates.md` C9 (thin domains) is #450 and C10 (countries) is #451 and its
fourteen groups; `discovery/research-queue.md` and `discovery/duplicates.md` are empty.

## How an item gets done

- Work happens in ordinary pull requests. The pull request that finishes an
  item says `Closes #N` in its body, so the issue closes when it merges.
- An exploratory item (a region, a country group) is closed when **every lead named in its
  issue has been looked at** and what could not be read is recorded in a row of
  `discovery/unresolved.md`, linked from the closing comment (rows #256 and #271 are the
  model). That is a statement about leads, not about every instrument being read; the
  comment says which lead, if any, was not looked at, and the issue can be reopened.
- Sessions pick work by `.agent/operating-model.md`'s priority order;
  a roadmap item the owner has put in *Next* comes first.
- The release pull request lists every closed `roadmap` issue since the last
  release under *Roadmap items completed* (`metadata/versioning.md`).

## Proposing an item

Open an issue with the *Roadmap item* template. Say what is true when it is
done, and why it matters; link the backlog entry, `unresolved.md` row or finding
it came from.
