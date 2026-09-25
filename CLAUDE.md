# Autonomous Knowledge Graph Agent — Operating Model

This file is the entry point for any Claude Code session — human-driven or
scheduled — working on this repository. It is intentionally short: the
repository already has a mature, working architecture (see below), and this
file's job is to point into it and set the priority order, not to duplicate
or compete with it.

**First rule: this repository is the persistent memory.** A new session has
no access to any previous conversation. Everything a future session needs —
current state, open questions, what was tried and failed, what's next — must
already be a file here. If you learn something worth keeping, write it down
before you finish, in the place described below, not just in your final
chat message.

## What already exists — use it, don't reinvent it

| Need | Where it lives |
|---|---|
| Project overview, entity/connection counts, sourcing model | `README.md` |
| Contribution mechanics, batch workflow, style rules | `CONTRIBUTING.md` |
| Entity types, geographic model, design decisions | `metadata/ontology.md` |
| Relationship vocabulary and when to use each type | `metadata/relationship-types.md` |
| Domain list and legislation classification | `metadata/taxonomy.md` |
| Frontmatter field reference | `metadata/metadata-schema.md` |
| Entity file skeleton | `templates/entity-template.md` |
| **Current work in progress** | `progress/current-batch.md` |
| **Full historical batch log** | `progress/completed.md` |
| **Forward plan / what's not done yet** | `progress/backlog.md` |
| **Open questions on existing entities** (facts that couldn't be verified, plausible-but-unsourced relationships, known egress blocks and their workarounds) | `discovery/unresolved.md` |
| **Weak/unresearched leads** not yet worth an entity | `discovery/candidates.md` |
| **Specific, scoped research leads** ready to become an entity | `discovery/research-queue.md` |
| **Suspected duplicate entities** | `discovery/duplicates.md` |
| Which source domains are reachable/blocked, re-verification targets | `discovery/reverification-allowlist.md` (generated — regenerate with `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`, never hand-edit) |
| Validation | `validation/run_all.py` (5 checks), `tools/test_build_graph.py` (unit tests), `tools/build_graph.py --check` |
| Graph generation | `tools/build_graph.py` → `site/graph.json` / `site/details.json` |
| Human-attention flags this agent can't safely resolve alone | `.agent/needs-human/` (see below — the one genuinely new mechanism this file adds) |

**Do not create a parallel state system.** There is no `.agent/state.yaml`,
no `discovery/candidates/` directory, no `entities/` folder — those were an
earlier, generic proposal for this repository; the actual repository grew
its own equivalents (the table above) before this file existed, and they are
what's authoritative. Extend them. The one piece that genuinely doesn't
exist yet is `.agent/needs-human/` — see the section below.

## Priority order for autonomous work

Each session should read the table above, then pick work in this order:

1. **Finish incomplete work.** Check `progress/current-batch.md`'s Status
   line. If a previous session left something mid-flight, continue it
   before starting anything new.
2. **Close `discovery/unresolved.md` rows.** This is almost always where
   the highest-value work is: an open, specific, falsifiable question about
   an existing entity. Read a row, research it with primary sources, either
   close it (edit the entity, remove the row) or narrow it (record what's
   now known, what still isn't). See "Research rules" below before writing
   anything.
3. **Work `discovery/candidates.md` / `discovery/research-queue.md`.** Turn
   a scoped lead into a real, sourced entity, or fold it into an existing
   one. If both files say "nothing queued" (check before assuming there's
   nothing to do — they are sometimes fully empty, which is a legitimate
   state, not a bug), move on to graph completion.
4. **Graph completion.** Existing entities with missing relationships,
   thin sourcing, or an obvious connection to something researched this
   session. Improve what exists before adding isolated new nodes.
5. **Quality.** Duplicates (`discovery/duplicates.md`), broken links,
   inconsistent frontmatter, stale generated files, contradictions between
   sibling entities. `validation/run_all.py` catches structural issues
   automatically; this priority is for the things it can't check.
6. **New discovery.** Only once the above is genuinely exhausted, go
   looking for new candidates and add them to `discovery/candidates.md` —
   don't turn every new lead straight into a fully-researched entity in the
   same pass unless it's small.

Do not ask a human which of these to do next when the repository already
answers the question. Pick the highest-priority item with real available
work and do it.

## Research rules (non-negotiable)

- **No hallucinated knowledge.** Never invent an organisation, law,
  standard, relationship, date, URL, or identifier. If it can't be
  established, say `unknown` or leave the row in `discovery/unresolved.md`
  with what was checked and what would resolve it.
- **Primary sources first.** Government sites, official legislation,
  official international-organisation pages, standards bodies, official
  programme sites — in that rough order. A search-engine summary is a
  lead, not evidence; open and read the actual page before citing it.
- **Every relationship needs a reason to exist as a typed edge, not just
  plausibility.** See `metadata/relationship-types.md` §2.3 for the
  "every entity reaches its scope anchor" rule and the "record the edge
  once, on one side" convention — do not duplicate an edge on both
  entities it connects.
- **Check for duplicates before creating an entity**: search by name,
  known abbreviations, alternate spellings, and check whether it might
  already exist filed under a different folder/type.
- **A smaller, accurate graph beats a larger, invented one.**

## Git workflow

This repository already has a working, PR-based flow — use it exactly, do
not push directly to `main`:

1. `git fetch origin main` (and the shared working branch if one already
   exists remotely — see the note on stale branches below).
2. Branch off `origin/main`.
3. Make the change (usually: edit/create entity files, edit
   `discovery/unresolved.md`, regenerate `site/graph.json`/`site/details.json`
   via `tools/build_graph.py`).
4. Validate locally: `python3 tools/build_graph.py`, then
   `python3 validation/run_all.py`, then `python3 tools/test_build_graph.py`.
   All three must be clean (0 errors; the handful of pre-existing `http://`
   warnings in `validate_sources.py` are known and not a regression signal)
   before committing.
5. Commit with a clear message describing the actual change, ending with:
   ```
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```
6. Push the branch, open a PR against `main` describing what changed and
   why, with a short test-plan checklist.
7. **Check for real, independent CI before merging — but know when it
   won't appear.** `.github/workflows/validate.yml` runs the same three
   checks independently on every PR, and when a PR was opened by a human
   or by a session authenticated as a normal user/OAuth app (not a GitHub
   Actions job token), that check genuinely fires — wait for it
   (`get_check_runs`, not `get_status`, which does not see Actions
   results) and require it green before merging.
   **Exception, and it matters:** if this session is itself running
   inside a GitHub Actions job (the scheduled `autonomous-agent.yml`
   workflow) and used that job's own `GITHUB_TOKEN` to push/open the PR,
   GitHub's recursion-prevention rule means `validate.yml` will **not**
   fire on that PR at all — don't wait for a check that will never
   appear. In that specific case, step 4's local validation (identical
   checks, run directly) is the authoritative gate instead.
8. **If the gate (real CI, or local validation when CI can't fire per
   above) passes: squash-merge.** If it fails: do not force-merge. Fix and
   re-push once. If it fails again, or the failure isn't something you can
   safely diagnose, stop and write a `.agent/needs-human/` entry instead of
   retrying indefinitely.
9. Sync local `main` (`git fetch && git reset --hard origin/main`), delete
   the local feature branch.

**Stale shared branches**: if a prior autonomous run's branch still exists
on the remote at an already-merged (now-stale) tip, don't force-push over
it. Recreate the local branch from the remote's actual tip, merge
`origin/main` into it (a normal merge, not a rebase — resolve any conflict
in generated files, `site/graph.json`/`site/details.json`, by regenerating
them with `tools/build_graph.py` rather than hand-editing), then continue.

**Never commit directly to `main`, and never `git add .` blindly.** If an
autonomous run is interrupted (timeout, crash) with uncommitted changes
still in the working tree, the recovery step must isolate that work onto
its own branch and open a PR for it — never force it onto `main`, where it
could silently overwrite a human's concurrent commit. See
`.github/workflows/autonomous-agent.yml`'s final step for how this is
implemented.

## Human intervention: `.agent/needs-human/`

When a decision genuinely can't be made safely from the evidence — two
plausible readings with no way to pick, a source that contradicts another
already-cited one, a fact that would require inventing something to
resolve — do not guess and do not leave it silently unresolved either.
Create a file under `.agent/needs-human/` (one per issue, named
`<short-slug>.md`) containing:

```markdown
# <short question>

## Context
<which entity/row this concerns, and why it matters>

## Evidence found
<what was checked, quoting the relevant bit of each source>

## Possible interpretations
<the genuinely live options>

## Why this can't be decided safely from here
<the specific gap — not just "I'm not sure">

## Recommended next research
<what a human, or a future session with different access, could check>
```

Commit it as part of the same PR as any other work from that session. A
human clears it by resolving the question (updating the entity/row and
deleting the file, or leaving instructions for the next session) — the
agent should never delete its own `needs-human` files.

## Session shape (for a scheduled/unattended run)

```
Read progress/current-batch.md and discovery/unresolved.md
        ↓
Resume incomplete work, or pick the next item per the priority order above
        ↓
Research (primary sources only) → edit entity files / discovery files
        ↓
Rebuild the graph, validate locally (three checks above)
        ↓
Commit → push → open PR → wait for CI → merge on green
        ↓
Update progress/current-batch.md (and progress/backlog.md if a whole
planned item closed) so the next session doesn't repeat the work
        ↓
More time/budget left and more real work available? Continue.
Otherwise: checkpoint and stop cleanly.
```

Stop when: the runner's time budget is nearly exhausted, no genuine work
remains at any priority level, or something requires
`.agent/needs-human/`. Before stopping, make sure the last piece of work is
either fully merged or safely isolated on its own branch/PR — never leave
important work only in an uncommitted working tree.

## Safety boundaries

Never: fabricate a source, entity, date, or relationship; delete large
parts of the repository without being asked; rewrite Git history; force-push
to `main`; bypass the validation gate; commit secrets; silently discard
what looks like a human's in-progress or uncommitted change (stash and flag
it instead — see the Git Safety Protocol a human operator's own tooling
already enforces). When genuinely uncertain, preserve what's there and
write a `.agent/needs-human/` entry rather than guessing.
