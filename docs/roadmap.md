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

It was set up by the owner on 2026-10-07 and made public. Setting one up is a few
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
