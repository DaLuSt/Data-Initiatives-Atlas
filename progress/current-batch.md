# Current Batch

**Status:** No batch in progress. **The second verification-gap push**
completed on 2026-08-22. Full detail moved to `progress/completed.md`;
summary below. 355 entities remain `verification: search-only`/`unverified`
(162 now `primary-source`); `discovery/reverification-allowlist.md` ranks
the next targets. Skip entities citing only `eur-lex.europa.eu`,
`www.iso.org`, `www.coe.int` or `unece.org` — those hosts return a
bot-defense challenge page to every fetch in this environment, egress
policy notwithstanding.

## Second push — 2026-08-22

Closed out the **entire United Kingdom cluster** (17 entities: the
cybersecurity/standards group, the government/statistics/geospatial group,
and [[EU-UK-ADEQUACY]]) and the **entire Ireland cluster** (7 entities) —
every `country: GB` or `country: IE` entity, plus [[EU-UK-ADEQUACY]], now
carries `verification: primary-source`. 24 entities moved in total.

Highlights: found and fixed a structural bug on [[IE-NSAI]] (its own body
text described `participates-in` edges to [[EU-CEN]]/[[EU-CENELEC]] that
were missing from the structured data); upgraded [[IE-TAILTE]] from `low`
to `medium` confidence after Wikipedia supplied the exact merger date (1
March 2023); found a live escalation on [[IE-NCS-BILL]] not in the
original sources (the Commission referred Ireland to the CJEU over NIS2
in July 2026); renamed [[EU-UK-ADEQUACY]] and [[IE-NCSC]] where their
`name` fields were compiled descriptions never used verbatim on any
source, in favour of phrasing the sources actually use. Two claims
(GB-UKSA/GB-ONS's UN-CES seat-holder, and GB's own Council of Europe
membership) could not be re-confirmed this pass — both bot-walled hosts —
and are explicitly marked "not independently re-confirmed" rather than
silently dropped or re-asserted. Full write-up in `progress/completed.md`
under "The second verification-gap push".

## Previous push (2026-08-22, merged as PR #54)

Moved 37 entities across four German and UK clusters. Full write-up in
`progress/completed.md` under "The verification-gap multi-batch push".
