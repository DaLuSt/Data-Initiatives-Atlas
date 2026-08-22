# Current Batch

**Status:** No batch in progress. **The first research-queue pickup**
completed on 2026-08-22 — a new kind of push, creating entities rather
than re-verifying them. Full detail moved to `progress/completed.md`;
summary below. `discovery/reverification-allowlist.md` ranks the next
re-verification targets, and `discovery/research-queue.md` carries the
rest of the research backlog.

**Corrected guidance on what is actually blocked, found during the
research-queue pickup:** `efta.int` is **not** bot-walled — it returns a
403 to a browser-spoofing User-Agent but real content (200) to an
honest, identifying one, the same kind `tools/reverify.py` sends. Earlier
guidance here said it was blocked outright and was wrong, discovered
while researching the EFTA/EEA institutions. `www.iso.org`, `www.coe.int`
and `unece.org` remain untested against an honest User-Agent and are
still treated as blocked. `eur-lex.europa.eu` and `europarl.europa.eu`
are confirmed **not** blocked — both were read directly and successfully
in the fourth push (NO, NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT,
INTL-EEA-JCD-154-2018), matching the same false-blocked finding earlier
pushes made for `legislation.gov.uk`.

## First research-queue pickup — 2026-08-22

Picked up the "Next"-priority research-queue item carried since the
Norway batch and widened twice since: the **EFTA Surveillance
Authority**, the **EFTA Court** and the **EEA Joint Committee**, the
three EEA institutions [[NO]], [[INTL-EFTA]] and [[INTL-EEA-AGREEMENT]]
had all separately named as "not modelled". All three are now Atlas
entities — [[INTL-EFTA-SURVEILLANCE-AUTHORITY]], [[INTL-EFTA-COURT]] and
[[INTL-EEA-JOINT-COMMITTEE]] — anchored to [[INTL-EEA-AGREEMENT]] rather
than [[INTL-EFTA]], since their jurisdiction is exactly the three EEA
EFTA states and excludes Switzerland, EFTA's fourth member.

[[INTL-EFTA]] itself was promoted from `search-only` to `primary-source`
in the same pass, on the strength of its own "About EFTA" page — the
significant finding of this push: `efta.int`, believed bot-walled since
the third push, actually serves content fine once fetched with an
honest User-Agent instead of a browser-spoofing one. That correction is
recorded above and on the four entities it touches. Full write-up in
`progress/completed.md` under "The first research-queue pickup".

## Earlier pushes

- **Fourth push** (2026-08-22): the entire Norway cluster (10 entities:
  [[NO]], seven `country: NO` entities, and the two EEA connective
  entities [[INTL-EEA-AGREEMENT]] and [[INTL-EEA-JCD-154-2018]]). A
  significant finding on [[NO-NSM]] — its own official website states
  directly that NSM is one of Norway's three intelligence, surveillance
  and security services; found `participates-in` [[UN-GGIM]] on
  [[NO-KARTVERKET]]; fixed a factual error on [[NO-DIGDIR]]. See "The
  fourth verification-gap push".
- **Third push** (2026-08-22): the entire Swiss cluster (9 entities plus
  CH) — closed the "no Fedlex citation" gap on CH-REVDSG/CH-EMBAG, found
  CH-OPENDATA-SWISS `governed-by` CH-EMBAG, corrected a wrong alternative
  name on CH-DVS. See "The third verification-gap push".
- **Second push** (2026-08-22): the entire UK cluster (17 entities),
  [[EU-UK-ADEQUACY]], and the entire Ireland cluster (7 entities) — 24
  entities moved. See "The second verification-gap push".
- **First push** (2026-08-22, merged as PR #54): 37 entities across four
  German and UK clusters. See "The verification-gap multi-batch push".
