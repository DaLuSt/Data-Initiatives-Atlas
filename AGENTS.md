# Autonomous Knowledge Graph Agent — Operating Model

This file is the entry point for any Claude Code session — human-driven
or scheduled — working on this repository. It is intentionally short: the
detail lives in `.agent/` and in the repository's own existing files (see
below), and this file's job is to point into them, not duplicate them.

**First rule: this repository is the persistent memory.** A new session
has no access to any previous conversation. Everything a future session
needs — current state, open questions, what was tried and failed, what's
next — must already be a file here. If you learn something worth
keeping, write it down before you finish, in the place described below,
not just in your final chat message.

## Start here, every session

1. Read **`.agent/state.yaml`** — the authoritative live snapshot (entity
   count, last merged work, open-item counts).
2. Read **`.agent/current-task.yaml`** — if it names an in-flight task,
   resume it before starting anything new.
3. If idle, pick the next item per `.agent/operating-model.md`'s
   priority order.

## The `.agent/` directory

| File | What it holds |
|---|---|
| `.agent/mission.md` | Why this agent exists, the primary objective, what "done" looks like |
| `.agent/operating-model.md` | Priority order for picking work, the full git workflow, session shape, `.agent/needs-human/` |
| `.agent/research-policy.md` | Non-negotiable sourcing rules — no hallucination, primary sources first, dedup |
| `.agent/quality-policy.md` | Validation requirements and safety boundaries |
| **`.agent/state.yaml`** | **Authoritative current status — read first** |
| **`.agent/current-task.yaml`** | **Authoritative in-flight task, if any — read second** |
| `.agent/run-history/` | One structured log entry per run, from 2026-09-26 onward |
| `.agent/needs-human/` | Decisions a session couldn't safely make alone |

## What already exists in the repository — use it, don't reinvent it

| Need | Where it lives |
|---|---|
| Project overview, entity/connection counts, sourcing model | `README.md` |
| Contribution mechanics, batch workflow, style rules | `CONTRIBUTING.md` |
| Entity types, geographic model, design decisions | `metadata/ontology.md` |
| Relationship vocabulary and when to use each type | `metadata/relationship-types.md` |
| Domain list and legislation classification | `metadata/taxonomy.md` |
| Frontmatter field reference | `metadata/metadata-schema.md` |
| Entity file skeleton | `templates/entity-template.md` |
| Historical batch narrative (human-readable, no longer the live-status source) | `progress/current-batch.md`, `progress/completed.md` |
| Forward plan / what's not done yet | `progress/backlog.md` |
| **Open questions on existing entities** (facts that couldn't be verified, plausible-but-unsourced relationships, known egress blocks and their workarounds) | `discovery/unresolved.md` |
| **Weak/unresearched leads** not yet worth an entity | `discovery/candidates.md` |
| **Specific, scoped research leads** ready to become an entity | `discovery/research-queue.md` |
| **Suspected duplicate entities** | `discovery/duplicates.md` |
| Which source domains are reachable/blocked, re-verification targets | `discovery/reverification-allowlist.md` (generated — regenerate with `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`, never hand-edit) |
| Validation | `validation/run_all.py` (5 checks), `tools/test_build_graph.py` (unit tests), `tools/build_graph.py --check` |
| Graph generation | `tools/build_graph.py` → `site/graph.json` / `site/details.json` |

**Do not create a second parallel state system on top of this one.**
`.agent/state.yaml` and `.agent/current-task.yaml` are now the
authoritative live-status files (decided 2026-09-26, reversing an
earlier version of this file that held the opposite view while the
repository's `progress/`/`discovery/` files served that role alone).
Extend the structure above; don't invent a third place to track status.
