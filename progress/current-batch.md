# Current Batch

**Status:** No batch in progress. **The third verification-gap push**
completed on 2026-08-22. Full detail moved to `progress/completed.md`;
summary below. 346 entities remain `verification: search-only`/`unverified`
(171 now `primary-source`); `discovery/reverification-allowlist.md` ranks
the next targets. Skip entities citing only `eur-lex.europa.eu`,
`www.iso.org`, `www.coe.int` or `unece.org` — those hosts return a
bot-defense challenge page to every fetch in this environment, egress
policy notwithstanding.

## Third push — 2026-08-22

Closed out the **entire Swiss cluster** (9 entities, plus [[CH]] itself)
— every `country: CH` entity now carries `verification: primary-source`.

Highlights: closed the long-standing "no Fedlex citation" gap on
[[CH-REVDSG]] and [[CH-EMBAG]] by finding the real ELI URLs via outbound
links on official government pages (Fedlex itself renders client-side in
JavaScript, so neither could be read past retrieval — a tooling limit,
not a sourcing gap); found and sourced a genuinely new connection,
[[CH-OPENDATA-SWISS]] `governed-by` [[CH-EMBAG]], via bfs.admin.ch's own
statement that its OGD office operates the portal pursuant to the Act —
closing a gap both entities had explicitly flagged as self-evident but
unsourced; caught and corrected a wrong alternative name ([[CH-DVS]]'s
Italian abbreviation was "AND" and should have been "ADS"); and learned
that a claim attested only in a page's `<title>` tag does not count as
confirmation once checked against `tools/reverify.py`'s own extraction
(which strips `<head>`) — re-sourced the affected names via other-language
pages or Wikipedia infoboxes rather than dropping them. Full write-up in
`progress/completed.md` under "The third verification-gap push".

## Earlier pushes

- **Second push** (2026-08-22): the entire UK cluster (17 entities),
  [[EU-UK-ADEQUACY]], and the entire Ireland cluster (7 entities) — 24
  entities moved. See "The second verification-gap push".
- **First push** (2026-08-22, merged as PR #54): 37 entities across four
  German and UK clusters. See "The verification-gap multi-batch push".
