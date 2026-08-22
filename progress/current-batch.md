# Current Batch

**Status:** No batch in progress. **The fifth verification-gap push**
completed on 2026-08-22. Full detail moved to `progress/completed.md`;
summary below. `discovery/reverification-allowlist.md` ranks the next
re-verification targets, and `discovery/research-queue.md` carries the
rest of the research backlog.

**Corrected/added guidance on what is actually blocked:** `efta.int` is
**not** bot-walled — it returns a 403 to a browser-spoofing User-Agent
but real content (200) to an honest, identifying one, the same kind
`tools/reverify.py` sends (found in the first research-queue pickup).
`isap.sejm.gov.pl` — the Sejm's legal-text database — **is** genuinely
blocked: an Incapsula JavaScript challenge page regardless of
User-Agent, browser-spoofing or honest alike (found in the second
research-queue pickup, researching [[PL-PESEL]]). `riigiteataja.ee`,
Estonia's official legal gazette, is likewise genuinely blocked — a
plain JavaScript single-page application with no static content at all
(found in the third research-queue pickup, researching
[[EE-STATISTIKAAMET]]). `www.iso.org`, `www.coe.int` and `unece.org`
remain untested against an honest User-Agent and are still treated as
blocked. `eur-lex.europa.eu` and
`europarl.europa.eu` are confirmed **not** blocked — both were read
directly and successfully in the fourth verification-gap push (NO,
NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT, INTL-EEA-JCD-154-2018),
matching the same false-blocked finding earlier pushes made for
`legislation.gov.uk`.

## Fifth verification-gap push — 2026-08-22

Re-verified the entire **Iceland and Liechtenstein clusters** (6
entities: [[IS]], [[IS-PERSONUVERND]], [[IS-PERSONUVERNDARLOG]], [[LI]],
[[LI-DATENSCHUTZSTELLE]] and [[LI-DSG]]) — the two EEA EFTA states added
alongside Norway's cluster to test whether the Norwegian EEA pattern
generalises, still `search-only` since they were created. All six now
carry `verification: primary-source`.

`efta.int`'s own "European Free Trade Association" page and
government.nl's EEA/EFTA/Schengen page were both read directly and
confirm both countries' EFTA and EEA membership verbatim. WIPO Lex's own
record of Iceland's Act No. 90/2018 matches the entity's name, dates and
Icelandic title exactly, and quotes the Act's own text naming
Persónuvernd as the supervisory body. `coe.int` and `iso.org` remain
bot-walled (403) even with an honest User-Agent and stay cited but
unread on both country anchors' single relationship.

**A translation-error finding on [[LI-DSG]].** naegele.law's English
translation of Liechtenstein's DSG dates contains two typos — "October
2th" and "in force ... January 1st of 2018" (impossible, since an act
cannot enter into force before it is passed) — that its own German
original does not: "4. Oktober 2018" and "1. Januar 2019". The
Datenschutzstelle's own "Nationale Gesetze" page independently confirms
the German dates. The entity follows the corrected dates, which were
already what it had recorded before this pass.

**A claim retained, not confirmed.** [[LI-DATENSCHUTZSTELLE]]'s claim
that its Commissioner is appointed by the Landtag for a five-year
renewable term appears on none of the authority's own pages read this
pass (its "Team" page names a head with no appointment mechanism given)
and is retained rather than removed, per the project's standing rule
that a re-verification pass without a reason to think a claim wrong
does not delete it.

## Earlier pushes

- **Third research-queue pickup** (2026-08-22): [[EE-STATISTIKAAMET]],
  Statistics Estonia, the twelfth national statistical office in the
  Atlas — an [[EU-ESS]] member on the same strong-evidence standard
  [[PL-GUS]] set. Found `riigiteataja.ee` genuinely bot-walled (see
  above). See "The third research-queue pickup".
- **Second research-queue pickup** (2026-08-22): [[PL-PESEL]] and
  [[PL-EWIDENCJA-LUDNOSCI]], Poland's population register and its 2010
  legal basis — closing a gap [[PL-COI]] had named as "in a list of
  systems and nothing more." Found `isap.sejm.gov.pl` genuinely
  bot-walled (see above). See "The second research-queue pickup".
- **First research-queue pickup** (2026-08-22): the EFTA Surveillance
  Authority, the EFTA Court and the EEA Joint Committee — three EEA
  institutions [[NO]], [[INTL-EFTA]] and [[INTL-EEA-AGREEMENT]] had all
  separately named as "not modelled" — anchored to
  [[INTL-EEA-AGREEMENT]] rather than [[INTL-EFTA]] since their
  jurisdiction excludes Switzerland. Found that `efta.int` is not
  actually bot-walled (see above). See "The first research-queue
  pickup".
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
