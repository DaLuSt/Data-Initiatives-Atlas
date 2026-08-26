# Current Batch

**Status:** No batch in progress. **The twelfth verification-gap push**
completed on 2026-08-26 — closing Finland's tail. Full detail moved to
`progress/completed.md`; summary below. `discovery/reverification-allowlist.md`
ranks the next re-verification targets, and `discovery/research-queue.md`
carries the rest of the research backlog.

**Tail pushes, not fresh clusters.** Countries whose anchor and most
entities are `primary-source` can still carry a handful of
`verification: search-only` stragglers — entities added or left behind
after the country's main re-verification pass. [[DK]] (4) and [[SE]]
(3) were closed by the eighth and ninth pushes; [[FR]]'s entire cluster
(22 entities, one straggler — [[FR-DGSI]]) was closed by the tenth;
[[AT]] (3) was closed by the eleventh; [[FI]] (6) was closed by the
twelfth. `NL` (67), `DE` (27), `BE` (24), `ES` (22), `PL` (18), `PT` (8),
`EE` (7) and `CZ` (7) still carry tail entities — `EE` and `CZ` are now
the joint-smallest remaining, next in line.

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
[[EE-STATISTIKAAMET]]). `www.iso.org` and `www.coe.int` were tested
with an honest User-Agent (fifth verification-gap push, and again in
the sixth push on [[LU]] and [[LU-ILNAS]]) and remain genuinely
blocked — a real Cloudflare/bot-wall block, not a User-Agent artefact.
`unece.org` was re-tested with an honest User-Agent in the candidates
pickup and remains genuinely blocked (403) — unlike `efta.int`, this
one really is closed. `eur-lex.europa.eu` and
`europarl.europa.eu` are confirmed **not** blocked — both were read
directly and successfully in the fourth verification-gap push (NO,
NO-PERSONOPPLYSNINGSLOVEN, INTL-EEA-AGREEMENT, INTL-EEA-JCD-154-2018),
matching the same false-blocked finding earlier pushes made for
`legislation.gov.uk`. `eur-lex.europa.eu` does occasionally return an
empty AWS WAF challenge response (`202`, `x-amzn-waf-action: challenge`)
on a given request — the candidates pickup hit this once and got the
real page on a bare retry, so treat a single `202` there as a flake to
retry, not a block. `grunddata.dk`, cited on [[DK-DATAFORDELER]] and
[[DK-GRUNDDATA]], no longer resolves at all (checked https and http) —
a dead domain, not a bot-wall, found in the fourth research-queue
pickup, and reconfirmed dead in the eighth push. `consilium.europa.eu`
was tested for the first time this session in the seventh push and is
genuinely blocked (403) even with an honest User-Agent. `bosettiegatti.eu`,
an Italian legal-text mirror cited on the Italy cluster, is the
**first host found doing the reverse of `efta.int`**: it returns a
custom IIS "999" bot-defense error to the honest, identifying
User-Agent `tools/reverify.py` sends, but serves the page normally
(`200`) to a browser-spoofing one — found in the seventh
verification-gap push, researching [[IT-CAD]]. `legifrance.gouv.fr`
(specifically its JORF text pages), `interieur.gouv.fr` (including the
`dgsi.interieur.gouv.fr` subdomain), `economie.gouv.fr` and `lejdd.fr`
were all tested with both an honest and a browser-spoofing User-Agent
in the tenth push and are genuinely blocked (403) either way — note
that this contradicts an earlier note elsewhere in the repo that
Légifrance was confirmed readable on 2026-08-21; that confirmation
evidently no longer holds, or covered different pages.
`guides.etalab.gouv.fr` and `www.drsd.defense.gouv.fr` no longer
resolve at all (checked via direct DNS lookup) — dead domains,
superseded respectively by `guides.data.gouv.fr` and pages under
`www.defense.gouv.fr/drsd/`. `sante.gouv.fr`'s Health Data Hub PDF
returns HTTP 200 but the body is actually an HTML page carrying an
F5/TSPD JavaScript bot-defense challenge, not a real PDF — a genuine
block, not a parsing failure.

## The twelfth verification-gap push — 2026-08-26

Closed Finland's tail: [[FI-SUOMI-FI]], [[FI-PALVELUVAYLA]],
[[FI-SECONDARY-USE-ACT]], [[FI-TILASTOKESKUS]], [[FI-DVV]] and
[[FI-FINDATA]] — the six entities still `verification: search-only`
after [[FI-TIETOSUOJA]] had already been re-verified in an earlier
pass. All six now carry `verification: primary-source`.

**A stale country anchor, fixed.** [[FI]]'s own body text still said no
Finland entity was modelled — the same bug shape found on [[IT]] and
[[AT]] in earlier pushes.

**A 2025 amendment neither entity knew about.** findata.fi's own
legislation page named an amending act — 1159/2025 — to
[[FI-SECONDARY-USE-ACT]] that came into force in two stages this year
(1 January and 1 May 2026). It introduced a distributed permit model
alongside [[FI-FINDATA]]'s centralised one: applicants may now apply
for permits separately from each data controller instead of routing
every multi-controller request through Findata. The University of
Eastern Finland's own library page independently flagged its English
translation of the Act as "not up-to-date" — a second, unconnected
signal pointing at the same staleness.

**Two fabricated placeholder dates, corrected.** Both
[[FI-SECONDARY-USE-ACT]] and [[FI-FINDATA]] carried `start_date:
2019-01-01` with no source giving that day — a guessed date, not a
sourced one. findata.fi's own pages give month-level dates instead: the
Act "entered into force in May 2019," and Findata itself — legally
established the same year — "will start operating in early 2020" per
its own 30 December 2019 launch announcement. Both entities now carry
`start_date: null` with the real, if imprecise, dates recorded in
prose.

**A precise chronology for the Finland/Estonia data-exchange
partnership.** [[FI-PALVELUVAYLA]] previously only knew "2017" for
NIIS's founding. Reading niis.org's own history page and
en.wikipedia.org's X-Road article together supplied a full chronology:
the 2013 Estonia-Finland Memorandum of Understanding (called "the
world's first digitally signed international agreement"), NIIS's
founding in June 2017, the MIT-licence release of X-Road's core on 3
October 2016, and the two countries' data exchange layers actually
connecting on 7 February 2018.

**[[FI-TILASTOKESKUS]]'s [[EU-ESS]] membership, upgraded to a direct
statement.** stat.fi's own "European Statistical System" page states
directly that Statistics Finland "produce[s] statistics for the policy
needs of the European Union... in accordance with... the European
Statistical System (ESS)" — the same strong-evidence tier set for
[[PL-GUS]], [[EE-STATISTIKAAMET]] and [[IT-ISTAT]].

## The eleventh verification-gap push — 2026-08-26

Closed Austria's tail: [[AT-BRZ]], [[AT-DATA-GV-AT]] and
[[AT-ID-AUSTRIA]], the three entities still `verification: search-only`
after [[AT-DSB]] and [[AT-STATISTIK]] had already been re-verified in
earlier passes. All three now carry `verification: primary-source`.

**A stale country anchor, fixed.** [[AT]]'s own body text still said no
Austria entity was modelled — the same bug found on [[IT]] in the
seventh push — a claim that stopped being true once five entities were
added and updated the anchor. Rewritten to describe the five it now
anchors.

**`data.gv.at` is a genuine JavaScript single-page application, not a
bot-wall.** Its homepage, robots.txt, and every path tried return the
same empty app shell (a `<div id="app">` with a loading spinner) —
including on paths that return `404`, the same shell comes back — with
no static content reachable at all, matching the `riigiteataja.ee`
pattern from the third research-queue pickup rather than a bot-defense
block. BRZ's own Open Data product page supplied everything needed
instead, including an updated dataset count (over 27,000, up from an
unsourced 20,700 this entity had carried since creation) and the 2014
launch date.

**A ministry that no longer exists, and where its portfolio went.**
`bmdw.gv.at` — the Bundesministerium für Digitalisierung und
Wirtschaftsstandort page [[AT-ID-AUSTRIA]] partly relied on — no longer
resolves at all, checked by direct DNS lookup. oesterreich.gv.at, the
digital-government platform ID Austria unlocks, states in its own
imprint that it is now published by the **Bundeskanzleramt** (Federal
Chancellery) directly, with BRZ named as technical operator. No source
read states the reorganisation explicitly, so it is reported as an
observation rather than asserted as fact. The specific "four statutes
had to move" claim this entity carried, sourced only to the now-dead
ministry page, was not found on any replacement source and is kept as
an explicitly unconfirmed carry-forward rather than dropped or
re-asserted.

**BRZ's own founding history, confirmed in its own words.** BRZ's
organisation page states directly that in 1997 the Finance Ministry's
IT departments were spun off into Bundesrechenzentrum GmbH, a company
still 100% state-owned and represented by the Ministry of Finance. No
exact founding day is given, so `start_date` was left unset rather than
guessed — the same discipline applied to `data.gv.at`'s 2014 launch
year.

## The tenth verification-gap push — 2026-08-26

Re-verified the entire France cluster (22 entities), the last country
whose whole cluster was still untouched. 21 entities promoted to
`verification: primary-source`; [[FR-DGSI]] stays `search-only` — only
one of its four cited sources (`cnctr.fr`) could be read, the other
three being genuinely blocked `interieur.gouv.fr`/`dgsi.interieur.gouv.fr`
pages, and a single reachable source among several is not enough to
justify promotion (contrast the "one dead/unread source among many"
exception used elsewhere this session for `iso.org` and similar).

**[[FR-NIS2-LOI]]'s direct sourcing contradiction, resolved.** The
entity previously carried `status: unknown` because its sources gave
two directly contradictory accounts — one asserting the bill was
already law (n° 2025-90 of 26 February 2025), the other that it
remained a Senate-passed bill awaiting promulgation. Three independent
sources plus ANSSI's own official MonEspaceNIS2 page, all read this
pass, agree the bill was still unpromulgated as of 6 August 2026; only
one uncorroborated source asserted the "already law" account. Status
changed to `planned`, confidence to `medium`.

**A genuine pre-existing bug found and fixed on [[FR-RGI]].** Its
frontmatter asserted a `based-on` [[EU-EIF]] relationship that the
entity's own body text explicitly refused. The relationship has been
removed.

**Three founding-date/legal-citation gaps closed.** [[FR-DRM]]'s
founding decree (16 June 1992, Décret n° 92-523) and [[FR-DRSD]]'s
precise legal basis (Article D3126-5, Code de la Défense) plus its 2016
renaming from the DPSD, both found via an academic paper on
`afdsd.fr`. [[FR-ETALAB]]'s actual founding date (21 February 2011) was
found via fr.wikipedia.org, correcting a previously wrong date that
conflated founding with its later 2019 DINUM-department reorganisation.

**Two new entities created from the research queue, now populated
rather than queued.** [[FR-INSEE]], the last Atlas country left without
a national statistical office, closing the [[EU-ESS]] gap named since
the France batch; [[FR-AFNOR]], the national standards body, confirmed
by name on `standards.cencenelec.eu`'s own member list. An unsupported
claim on [[FR-INSEE]] ("French branch of Eurostat") was traced to a
login-gated, content-free European Commission shell page and dropped
rather than carried forward unverified.

## Earlier pushes

- **Ninth push** (2026-08-25): closed Sweden's tail —
  [[SE-DATAPORTAL]], [[SE-DIGG]] and [[SE-SCB]]. Confirmed
  [[SE-DIGG]]'s custodianship of [[SE-DATAPORTAL]] almost word for
  word; kept [[SE-SCB]]'s [[EU-ESS]] membership on the composition-rule
  tier. See "The ninth verification-gap push".
- **Eighth push** (2026-08-25): closed Denmark's tail —
  [[DK-GRUNDDATA]], [[DK-DATATILSYNET]], [[DK-SUNDHEDSDATASTYRELSEN]]
  and [[DK-DST]]. Dated the Basic Data Programme to 2012 via a European
  Commission ISA2 document; found [[DK-DST]]'s legal basis named but not
  read; `grunddata.dk` reconfirmed dead. See "The eighth
  verification-gap push".
- **Seventh verification-gap push** (2026-08-25): the entire Italy
  cluster (6 entities). Fixed a stale country anchor still claiming
  Italy had "no national entities"; closed [[IT-DATI-GOV-IT]]'s
  custodian gap ([[IT-AGID]] since 2015); upgraded [[IT-ISTAT]]'s
  [[EU-ESS]] membership to a direct statement; found `bosettiegatti.eu`
  blocks the honest User-Agent but not a browser-spoofing one, the
  mirror image of the `efta.int` finding. See "The seventh
  verification-gap push".
- **Sixth verification-gap push** (2026-08-25): the entire Luxembourg
  cluster (6 entities). Found [[LU-ILNAS]]'s sixth standardisation
  membership (the ITU), breaking its tie with [[GB-BSI]], and sourced
  Luxembourg's GDPR act date via an ELI URL without creating a law
  entity from it. See "The sixth verification-gap push".
- **Fourth research-queue pickup** (2026-08-25): [[DK-KLIMADATASTYRELSEN]],
  which Datafordeleren's own homepage names directly as its operating
  authority — [[DK-DATAFORDELER]] promoted to `primary-source` in the
  same pass. An incidental find on [[EU-INSPIRE]]: Klimadatastyrelsen's
  own "Lovstof" page names Denmark's INSPIRE transposition act by its
  exact citation. `retsinformation.dk` confirmed a JavaScript
  single-page application with no static content. See "The fourth
  research-queue pickup".
- **Candidates pickup** (2026-08-22): [[UN-HLPF]] and
  [[EU-EFTI-REGULATION]], closing two `discovery/candidates.md` rows.
  UN-HLPF closed a gap [[EU-VOLUNTARY-REVIEW-2023]] named in its own
  text; EU-EFTI-REGULATION closed the other with a negative result —
  reading the Regulation's full text found no trace of the UN/CEFACT
  connection secondary sources claimed. See "The candidates pickup".
- **Fifth verification-gap push** (2026-08-22): the entire Iceland and
  Liechtenstein clusters (6 entities), added alongside Norway's to test
  whether the Norwegian EEA pattern generalises. Found a translation
  error on [[LI-DSG]]'s English-language source (two date typos its own
  German original didn't have) and confirmed `coe.int`/`iso.org`
  genuinely bot-walled. See "The fifth verification-gap push".
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
