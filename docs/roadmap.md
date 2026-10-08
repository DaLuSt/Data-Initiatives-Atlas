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

Until the secret exists the workflow succeeds and does nothing. Then, in the
board, add a view with the *Roadmap* layout and set its start and end to
**Start date** and **Target date**. Views are not available through the
workflow's token.

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
