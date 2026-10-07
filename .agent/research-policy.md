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
- **A refusal for want of a source is not the same as a fact being
  unknowable.** Before declining, look for the instrument that created the
  thing and for its statement of the rule; the source is often there. It held
  four times: the national data protection authorities' seat at the
  [[EU-EDPB]] was in [[EU-GDPR]] Article 68(3) (a member state with more than
  one authority appoints a joint representative), which unblocked
  [[DE-BFDI]]; [[IE-NSAI]]'s CEN membership followed from CEN-CENELEC's own
  statement of the rule (its national members are the standardisation bodies of
  the 27 EU countries) without reading a member list the Atlas cannot retrieve;
  the 2030 Agenda was "nothing found" until the search was for the resolution,
  A/RES/70/1 ([[UN-2030-AGENDA]]); and the EEA supervisory authorities' seat at
  the Board is stated in [[INTL-EEA-JCD-154-2018]] for [[IS-PERSONUVERND]] and
  [[LI-DATENSCHUTZSTELLE]]. (Moved here from `discovery/candidates.md` on
  2026-10-03.)
- **"Blocked" depends on the tool, the URL form and the day; test before
  you write a source off.** Tested on 2026-10-07: from the sandbox, `curl` cannot
  connect to EUR-Lex (the NIM page), gets 403 from Légifrance and `efta.int`, and
  reads `legislation.gov.uk` and `bfdi.bund.de` normally. The fetch tool
  (`WebFetch`) read the EUR-Lex national-measures page for a directive
  (`legal-content/EN/NIM/?uri=CELEX:32019L1024`), a Légifrance law
  (`legifrance.gouv.fr/loda/id/...`), a legislation.gov.uk Act page and the
  `efta.int` homepage. The fetch tool still gets 403 from `unece.org`,
  `unctad.org`, `iso.org` and `coe.int`, cannot fetch `web.archive.org` at all, and
  returns only a JavaScript notice for Fedlex (whose English PDFs, by their
  filestore URL, curl can download). Pages over about 100,000 characters are cut
  off: read on with the tool's `offset`. The per-host rows are
  `discovery/unresolved.md` #220, #222, #223 and #225. A failure on one form of a
  URL is not proof of a block, and a success on one page does not make the whole
  host reachable.
