# Mission

The Data Initiatives Atlas is an open, connected knowledge graph of
data/digital/governance initiatives — laws, organisations, standards,
platforms, data spaces and programmes — spanning national, EU, UN and
international scope. `README.md` has the full project overview and
current entity/connection counts; this file is about *why* Claude Code
sessions work on it and what "good" looks like for that work.

## Primary objective

Grow and improve the graph — more entities, richer relationships, better
sourcing — **without ever trading accuracy for size**. A smaller, fully
sourced graph is strictly better than a larger one with invented or
unverifiable content. See `.agent/research-policy.md` for the
non-negotiable rules that follow from this.

## What "done" looks like for a unit of work

A piece of work (an entity added, a relationship typed, a
`discovery/unresolved.md` row closed or narrowed) is done when:

1. Every factual claim has a real source, read directly, cited in the
   entity's `sources:` frontmatter.
2. The change passes all three local validation checks (see
   `.agent/quality-policy.md`) with zero errors.
3. Anything learned that doesn't belong in an entity file — a source
   block found, a question narrowed but not closed, a decision made and
   why — is written into the right `discovery/` or `.agent/` file before
   the session ends. See `.agent/operating-model.md`'s "First rule."
4. The change is merged (or safely isolated on its own branch/PR if the
   session was interrupted) — never left only in an uncommitted working
   tree.

## Why sessions work this way

There is no scheduled or unattended agent: the earlier workflow that ran one
(`autonomous-agent.yml`) was removed on 2026-10-08, because the owner does not
plan to run it. Every session is started by a person and follows the same
research and git discipline a human contributor does. `CONTRIBUTING.md`
describes that discipline; `AGENTS.md` and the rest of `.agent/` give a
session the memory and the rules. Speed is a means of getting more sourced,
accurate work done, not licence to relax the sourcing bar — see
`.agent/research-policy.md`.
