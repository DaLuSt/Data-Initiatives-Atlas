# Research Policy (non-negotiable)

These rules apply to every entity, relationship, and claim added to the
Atlas, by a human or an autonomous session alike. `CONTRIBUTING.md` has
the mechanics of adding an entity; this file is about what makes a claim
fit to add at all.

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
- **A discrepancy between sources is data, not noise.** Record it (which
  source says what) rather than silently picking one side — see
  `discovery/unresolved.md` for many examples, and
  `.agent/operating-model.md`'s `.agent/needs-human/` section for when a
  discrepancy can't be resolved safely from the evidence at all.
- **Never let a blocked source become an excuse to guess.** A domain
  returning 403/503/an empty JS shell is an egress problem, logged in
  `discovery/unresolved.md`'s "Known source-access blocks" table (with
  any workaround subdomain/URL form found) — it is never a reason to
  assert something unverified instead.
