# Current Batch

**Batch 1 — Netherlands: Core Data Governance**

**Status:** Started 2026-08-14. **Blocked on source access.**

## What happened

Research began on the Batch 1 scope (Forum Standaardisatie, IBDS,
Federatief Datastelsel, NORA, Common Ground, MIDO, Data Agenda Overheid,
NL DIGIbeter and related programmes). It could not be completed to the
Atlas's evidence standard.

The working environment's network egress policy blocks all direct page
retrieval. Every host tested returned `EGRESS_BLOCKED`, including
`forumstandaardisatie.nl`, `digitaleoverheid.nl`, `noraonline.nl`,
`vng.nl`, `eur-lex.europa.eu` and `wikipedia.org`. Only web *search* was
reachable (it is served through the Anthropic API rather than direct
egress), which returns titles, URLs and snippet-derived summaries.

The brief's research-quality rules (§21) state plainly: *"Do not use search
snippets as evidence."* Creating entities whose `sources:` list cites pages
that were never actually read — with an `accessed:` date asserting
otherwise — would be precisely the failure mode the Atlas exists to avoid,
and every later batch would inherit it.

## What was delivered instead

No entity files were created. Per §21 (*"If information cannot be verified:
Do not guess. Record it in discovery/unresolved.md."*):

- `discovery/research-queue.md` — populated with the Batch 1 target list and
  ~20 candidate authoritative source URLs confirmed by search to exist,
  each explicitly marked unverified, plus the specific open questions to
  resolve per entity.
- `discovery/unresolved.md` — the blocker itself, plus three specific
  factual claims that surfaced in search results and must not be recorded
  until read from a primary source.

## What unblocks this

Direct outbound HTTPS access to public government/EU/standards-body
domains, so `WebFetch` can actually read the sources listed in
`discovery/research-queue.md`. The environment's network policy is set when
the environment is created — see
https://code.claude.com/docs/en/claude-code-on-the-web.

Once retrieval works, Batch 1 can be completed directly from the queued URL
list without repeating the discovery pass.

## Next

Awaiting a decision on how to proceed (restore network access and do Batch 1
properly, or explicitly lower the evidence bar for this batch). See
`progress/backlog.md` for the remaining plan.
