# Roadmap

The roadmap is a set of **GitHub issues labelled `roadmap`**, shown on a
**Project board**, with each item aimed at a **data release**. It sits beside,
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

The Project board has four columns: **Backlog** (not scheduled), **Next**
(aimed at the coming release), **In progress**, **Done**. The board's built-in
workflows move an issue to *Done* when it closes and add new `roadmap` issues to
*Backlog*. Setting the board up is a few clicks in the GitHub UI, because
creating a Project needs permissions that the repository's automation does not
have:

1. Create a Project (Projects tab, *New project*, Board layout) named *Atlas roadmap*.
2. In the project's *Workflows*: enable *Item added to project* (Status = Backlog)
   and *Item closed* (Status = Done); enable *Auto-add to project* for this
   repository with the filter `is:issue label:roadmap`.
3. Link the project to the repository.

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
