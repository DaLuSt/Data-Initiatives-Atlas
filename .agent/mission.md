# Mission

The Data Initiatives Atlas is an open, connected knowledge graph of
data/digital/governance initiatives — laws, organisations, standards,
platforms, data spaces and programmes — spanning national, EU, UN and
international scope. `README.md` has the full project overview and
current entity/connection counts; this file is about *why* an autonomous
agent works on it and what "good" looks like for that work.

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

## Why this runs autonomously

The scheduled workflow (`.github/workflows/autonomous-agent.yml`) exists
so the graph keeps growing between human sessions, using the same
research and git discipline a human contributor follows —
`CONTRIBUTING.md` describes that discipline for a human; `AGENTS.md` and
the rest of `.agent/` describe it for an unattended agent. Autonomy is a
means of getting more sourced, accurate work done, not licence to relax
the sourcing bar — see `.agent/research-policy.md`.
