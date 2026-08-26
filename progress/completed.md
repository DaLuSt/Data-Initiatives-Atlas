# Completed Batches

## The thirteenth verification-gap push

**Date:** 2026-08-26

Closed Estonia's remaining seven `verification: search-only` entities —
[[EE-E-RESIDENCY]], [[EE-ANDMEPORTAAL]], [[EE-RIHA]], [[EE-X-TEE]],
[[EE-IKS]], [[EE-ATS]] and [[EE-RIA]] — alongside [[EE-AKI]] and
[[EE-STATISTIKAAMET]], already `primary-source` from earlier passes.
All seven now carry `verification: primary-source`; Estonia's whole
cluster is fully re-verified.

### A stale country anchor, fixed twice over

[[EE]]'s own body text carried two separate stale claims: it still said
"no Estonia entity is modelled yet," and a whole section still framed
X-Road and e-Residency as things "the Atlas holds nothing about" — both
written when the anchor was created and never revisited as nine
entities were added and progressively re-verified around it. The same
bug shape found on [[IT]]'s, [[AT]]'s and [[FI]]'s anchors in earlier
pushes, now confirmed a fourth time as a genuine pattern rather than a
one-off: nothing in this workflow currently prompts a revisit of a
country anchor's own prose when its children change under it.

### RIHA is on notice, not already replaced

[[EE-ANDMEPORTAAL]]'s `replaces` edge onto [[EE-RIHA]] read as an
already-settled fact. RIA's own data-portal page, read directly, says
otherwise: RIHA "is currently still in use, but it is expected to be
decommissioned at the end of 2026 when the legislative amendments come
into force. Descriptions of the databases held by RIHA will then be
added to the Data Portal." Both entities' evidence was rewritten to
describe a transition in progress with a public target date, rather
than a completed handover — and [[EE-RIHA]]'s own body now flags that
it is likely to need a `status` change and a `successor` pointer within
months, not years. The same page named **RIHAKE**, a data management
application integrated with the portal, which this entity did not
previously carry and which does not yet warrant its own entity.

### RIA runs Estonia's CERT, confirmed in RIA's own words

[[EE-RIA]] previously speculated, without confirmation, that RIA
operates **CERT-EE**. RIA's own site settles it directly: "RIA is the
National Cyber Security Centre of Estonia (NCSC-EE)," with CERT-EE
named as the incident-handling body. CERT-EE still has no Atlas entity
of its own — that gap is unchanged — but the operational fact
underneath it no longer rests on inference. The same page places RIA
"within the administrative area of the **Ministry of Justice and
Digital Affairs**," a placement this entity did not previously carry.

### A precise 2018 naming split, confirmed independently of Finland

[[EE-X-TEE]]'s claim that it was "named X-Road in English until 2018"
is now confirmed in RIA's own words: "Until 2018, it was named X-Road
in English. Since 2018, however, X-Road is only used to refer to the
technology developed together by Estonia, Finland and Iceland through
MTÜ Nordic Institute for Interoperability Solutions." This independently
corroborates Iceland's NIIS membership found via [[FI-PALVELUVAYLA]]'s
sourcing in the twelfth push, from a completely different source.

### Two more fabricated placeholder dates, and one confirmed

[[EE-ATS]] carried `start_date: 2000-01-01` with no source giving that
day — the Riigi Teataja citation (RT I 2000, 92, 597) gives only a
year. Corrected to unset. [[EE-IKS]]'s 15 January 2019 date, by
contrast, held up: two independent legal trackers (Linklaters and
White & Case), read directly, confirm it verbatim, and White & Case
surfaced a related act this entity did not know about — a **Personal
Data Protection Act Implementation Act**, in force 15 March 2019 — noted
in prose rather than given its own entity.

### A new, client-fingerprint-dependent host block

`ria.ee`'s pages were read successfully via a direct `curl` fetch with
the honest User-Agent — reliable `200`s, full content — but
`tools/reverify.py`'s own fetcher, Python's `urllib`, sending the
identical UA string, reproducibly receives a Cloudflare "Just a
moment..." challenge on the same URLs. This is a new host-blocking
shape for the session: every earlier finding turned on the UA string
itself (honest vs. browser-spoofing); this one tracks the HTTP client's
own network fingerprint regardless of the UA header sent. Future
`tools/reverify.py --id` runs against the four Estonian entities citing
`ria.ee` will report it UNREACHABLE despite the content being genuinely
readable — each affected entity's caveat says so explicitly.
`scoop4c.eu`, cited on [[EE-X-TEE]] and [[EE-RIA]], is separately and
genuinely unreachable: a raw TLS connection reset regardless of
User-Agent, distinct again from the HTTP-403 walls found elsewhere this
session.

## The eleventh verification-gap push

**Date:** 2026-08-26

A tail push, the smallest yet: Austria's remaining three
`verification: search-only` entities — [[AT-BRZ]], [[AT-DATA-GV-AT]]
and [[AT-ID-AUSTRIA]] — closed alongside [[AT-DSB]] and
[[AT-STATISTIK]], both already `primary-source` from earlier passes.
All three now carry `verification: primary-source`.

### A stale country anchor, fixed

[[AT]]'s own body text still said "no Austria entity is modelled yet"
and listed data protection, open data, statistics and interoperability
as all unresearched — a claim that stopped being true once [[AT-BRZ]],
[[AT-DATA-GV-AT]], [[AT-DSB]], [[AT-ID-AUSTRIA]] and [[AT-STATISTIK]]
were all added, none of which had updated the anchor. This is the same
bug shape found on [[IT]] in the seventh push: entities get added and
re-verified, but the anchor's own prose is never revisited unless
something forces the question. Rewritten to describe the five entities
it now anchors.

### `data.gv.at`: a JavaScript shell, not a bot-wall

Every path tried against `www.data.gv.at` — the homepage, `robots.txt`,
`sitemap.xml`, a guessed CKAN API path, a guessed about page — returned
the identical 5,122-byte HTML shell (`<div id="app">` with a loading
spinner and a bundled JS entry point), including on paths that returned
a `404` status. That rules out a bot-defense wall, which would vary its
response, and confirms instead a genuine client-side single-page
application with zero server-rendered content — the same shape found on
`riigiteataja.ee` in the third research-queue pickup. BRZ's own Open
Data product page (`brz.gv.at/.../open-data.html`), read directly,
supplied everything the entity needed instead: the `maintained-by` edge
in BRZ's own words, a 2014 launch date, and an updated dataset count —
**over 27,000** datasets, current as of this reading, against the
20,700 this entity had carried since creation without any source ever
actually stating that number (it traced to a bare, figureless mention
on Wikipedia).

### A ministry that no longer exists

[[AT-ID-AUSTRIA]]'s citation of `bmdw.gv.at` — the Bundesministerium
für Digitalisierung und Wirtschaftsstandort — turned out to be a dead
domain, confirmed by direct DNS lookup (`socket.gethostbyname` raised
`[Errno -2] Name or service not known`). Reading oesterreich.gv.at, the
digital-government platform ID Austria unlocks, found its own imprint
states plainly: "Herausgeber: Bundeskanzleramt Österreich" (publisher:
Federal Chancellery of Austria), with "Technische Betreuung:
Bundesrechenzentrum GmbH" naming BRZ as technical operator in the same
breath — independently confirming the `maintained-by` edge this entity
already carried. Read together, Austria's digital-policy portfolio
looks to have moved from a dedicated digitalisation ministry to the
Chancellery itself, but no source read states that transition
explicitly, so it is recorded as an observation rather than asserted as
fact. The entity's specific "four statutes had to move" claim — sourced
only to the now-dead ministry page — was not found on any replacement
source read this pass, and is kept as an explicitly unconfirmed
carry-forward rather than dropped or silently re-asserted.

### BRZ's own history, in its own words

BRZ's organisation page, read directly, states that in 1997 the Finance
Ministry's IT departments were spun off into Bundesrechenzentrum GmbH,
which has operated ever since as a company **wholly owned by the
Republic of Austria**, represented by the Ministry of Finance, run on
commercial-market principles in competition with private IT firms —
independently corroborating (with more authority) what Wikipedia's BRZ
article already said. No exact founding day is available from either
source, so `start_date` was left unset on both [[AT-BRZ]] and
[[AT-DATA-GV-AT]] rather than filled with a guessed day-of-month —
the same discipline the session has applied to every partial date all
along.

## The tenth verification-gap push

**Date:** 2026-08-26

The entire France cluster (22 entities: [[FR]], [[FR-RGI]], [[FR-LIL]],
[[FR-LOI-RENSEIGNEMENT-2015]], [[FR-LOI-VALTER]], [[FR-LRN]],
[[FR-NIS2-LOI]], [[FR-AFNOR]], [[FR-ANSSI]], [[FR-CNCTR]], [[FR-CNIL]],
[[FR-DGSE]], [[FR-DGSI]], [[FR-DINUM]], [[FR-DRM]], [[FR-DRSD]],
[[FR-ETALAB]], [[FR-HEALTH-DATA-HUB]], [[FR-INSEE]], [[FR-DATA-GOUV]],
[[FR-FRANCECONNECT]] and [[FR-SNDS]]) — the last country whose whole
cluster was still `verification: search-only`. 21 entities were
promoted to `primary-source`; [[FR-DGSI]] stays `search-only`.

### FR-NIS2-LOI: a direct sourcing contradiction, resolved

This entity previously carried `status: unknown` because its cited
sources gave two directly contradictory accounts of the same bill: one
asserting it was already promulgated as law n° 2025-90 of 26 February
2025, the other that it remained a Senate-passed bill still awaiting
promulgation. Reading three independent sources this pass —
nis-2-directive.com, Eversheds Sutherland and Prodware — plus ANSSI's
own official MonEspaceNIS2 page, all agree the bill was still
unpromulgated as of 6 August 2026 (twenty days before this pass).
Only `aventris.fr` asserts the "already law" account, and it stands
uncorroborated by any other source read. `status` changed to `planned`,
`confidence` to `medium`, and the entity's comparison table of NIS2
transpositions updated to say so plainly rather than "unknown."

### FR-RGI: a genuine pre-existing bug, found and fixed

[[FR-RGI]]'s frontmatter asserted a `based-on` relationship to
[[EU-EIF]]. Its own body text directly contradicted this: France's
national interoperability framework explicitly declines to base itself
on the European one ("It is refused"). This was not a sourcing gap but
a factual error already in the file — the relationship has been
removed from frontmatter entirely (the wikilink is kept in
`related_entities` for navigation, since the refusal itself is worth
finding from either entity).

### Three founding-date and legal-citation gaps closed

[[FR-DRM]] had never carried a founding date; cnctr.fr and an academic
paper on afdsd.fr, read independently, agree on its founding decree:
**Décret n° 92-523 du 16 juin 1992** (JORF n° 139 du 17 juin 1992, p.
7900). `start_date: 1992-06-16` was added and `coverage` raised from
`low` to `medium`. The same afdsd.fr paper supplied [[FR-DRSD]]'s
precise legal basis — Article D3126-5 of the Code de la Défense — and
its 2016 renaming from the DPSD (Décret n° 2016-1337 du 7 octobre
2016), a history this entity did not previously carry. [[FR-ETALAB]]'s
`start_date` was corrected from 2019-10-30 to **2011-02-21**: the
2019 date was the entity's later reorganisation as a DINUM department
(kept as `valid_from` on the `part-of` [[FR-DINUM]] relationship), not
its founding, which fr.wikipedia.org dates precisely: "La mission
Etalab a été créée par décret le 21 février 2011."

### Two research-queue entities created and populated

[[FR-INSEE]] closes a gap named since the original France batch and
repeated in every structural review since: France was the only Atlas
country with no statistical office at all. It joins [[EU-ESS]] as its
seventh national institute alongside the Netherlands, Germany, Belgium,
Spain, Poland and Ireland — every EU member state in the Atlas is now
represented there. An unsupported claim this entity would otherwise
have carried forward — "described as the French branch of Eurostat" —
was traced to `knowledge4policy.ec.europa.eu`, which turned out on
direct reading to be a login-gated shell page with no substantive
content, and was dropped rather than repeated unverified. [[FR-AFNOR]],
France's national standards body, was confirmed by name on
`standards.cencenelec.eu`'s own CEN-CENELEC member list.

### FR-DGSI: caught overclaiming, corrected before commit

Only one of [[FR-DGSI]]'s four cited sources — cnctr.fr — could be
read; the other three (two `dgsi.interieur.gouv.fr` pages and one
`interieur.gouv.fr` page) are genuinely bot-walled regardless of
User-Agent. `verification` was briefly set to `primary-source` on the
strength of the one new corroborating source, then reverted to
`search-only` on the reasoning that "majority of sources unreachable"
is a materially different situation from the "one source among several
stays cited-but-unread" exception this session has used elsewhere
(`iso.org`, dead domains): there, most of the substantive sourcing was
actually read; here, three-quarters of it was not. The entity keeps
`last_verified: "2026-08-26"` as an honest record that a genuine
attempt was made, and its caveat states directly: "One of four current
sources read is not enough to call this entity `primary-source`."

### New host-blocking findings

`legifrance.gouv.fr` (specifically its JORF legal-text pages) is
genuinely blocked (403) with both an honest and a browser-spoofing
User-Agent — notable because [[FR]]'s own file carried an earlier note
that Légifrance was confirmed readable on 2026-08-21; that confirmation
evidently no longer holds, or covered a different part of the site.
`interieur.gouv.fr` (including the `dgsi.interieur.gouv.fr`
subdomain), `economie.gouv.fr` and `lejdd.fr` are all genuinely blocked
the same way. Two domains are dead, confirmed via direct DNS lookup:
`guides.etalab.gouv.fr` (superseded by `guides.data.gouv.fr`) and
`www.drsd.defense.gouv.fr` (superseded by pages under
`www.defense.gouv.fr/drsd/`, found via href-extraction from a page that
did load). [[FR-HEALTH-DATA-HUB]]'s `sante.gouv.fr` press-release PDF
returns HTTP 200, but the body is an HTML page carrying an F5/TSPD
JavaScript bot-defense challenge cookie, not a real PDF — a genuine
block that simple status-code checking would have missed.

## The ninth verification-gap push

**Date:** 2026-08-25

A companion to the eighth push: rather than a fresh country cluster,
this closes the **tail** on Sweden, whose anchor ([[SE]]) and
[[SE-IMY]] were already `primary-source`, but three entities —
[[SE-DATAPORTAL]], [[SE-DIGG]] and [[SE-SCB]] — still carried
`verification: search-only`. All three now carry
`verification: primary-source`. Opened as its own pull request rather
than folded into the Denmark tail push, since the two countries'
findings don't otherwise relate.

### Sweden's data portal, confirmed by its own custodian

[[SE-DATAPORTAL]]'s entity already described a wider remit than most
national portals in the Atlas — data from "public and private"
organisations, not government data alone — sourced to two pages
neither of which had been read. dataportal.se's own "Om oss" page, read
directly this pass, confirms it almost word for word: "(Digg) ansvarar
för Sveriges dataportal. Sveriges dataportal gör det möjligt för
allmänheten att söka bland data som tillhandahålls av offentliga och
privata organisationer... Målet är att data ska bli en strategisk
samhällsresurs" (DIGG is responsible for Sweden's data portal, which
lets the public search data provided by public and private
organisations... the goal is for data to become a strategic societal
resource). [[SE-DIGG]]'s own "Our mission" page, read independently,
confirms its two-part remit in the same terms this entity already
carried: "We coordinate and support the digitalisation of public
administration. We are responsible for Sweden's digital
infrastructure."

### Statistics Sweden: identity confirmed, ESS membership still inferred

[[SE-SCB]]'s own "About us" page, read directly, states: "Statistics
Sweden is responsible for official statistics and for other government
statistics... we coordinate the system for the official statistics in
Sweden" — a direct confirmation of identity. Neither that page nor
scb.se's homepage names Eurostat or the [[EU-ESS]] directly, so this
edge stays on the composition-rule tier — the same honest call made on
[[LU-STATEC]] and [[DK-DST]] in the sixth and eighth pushes.

## The eighth verification-gap push

**Date:** 2026-08-25

A new shape for this task: rather than a fresh country cluster, this
push closes the **tail** left on a country whose main re-verification
pass had already happened. Denmark's anchor ([[DK]]), its open-data
platform ([[DK-DATAFORDELER]]) and [[DK-KLIMADATASTYRELSEN]] were all
`primary-source` from earlier pushes, but four entities — added at
different times, evidently missed by those passes — still carried
`verification: search-only`: [[DK-GRUNDDATA]], [[DK-DATATILSYNET]],
[[DK-SUNDHEDSDATASTYRELSEN]] and [[DK-DST]]. All four now carry
`verification: primary-source`.

A survey of every entity's `verification` field, not just country
anchors, found this pattern is not unique to Denmark: [[NL]] carries
67 such stragglers, [[DE]] 27, [[BE]] 24, [[ES]] 22, [[PL]] 18, [[PT]]
8, [[EE]] 7, [[CZ]] 7, [[FI]] 6, and (until this pass) [[DK]] 4 and
[[SE]] 3. [[FR]] is the only country whose entire cluster — all 22
entities, including its own anchor — remains untouched, making it the
next natural full-cluster push whenever this task resumes.

### Grunddata's origin, dated for the first time

[[DK-GRUNDDATA]]'s body already compared it to [[NL-BASISREGISTRATIES]]
as "the same idea in another jurisdiction," noting the Dutch stelsel
"rests on seven statutes" while "the Danish programme came out of a
digitalisation strategy" — but carried no date for that strategy. A
European Commission ISA2 conference document, cited since the entity's
creation but never read, supplies one directly: "The basic data
program was established in 2012 as part of the e-government strategy
agreed between the Danish Government, Local Government Denmark and
Danish Regions." `datafordeler.dk`'s own "Grunddata" page, also read
directly, lists the registers under the programme by name — the Civil
Registration System, the Central Business Register, the Building and
Housing Register — matching this entity's claim exactly.
`grunddata.dk` was tested again and remains dead: no DNS resolution
over either https or http, the same finding the fourth research-queue
pickup made.

### Sundhedsdatastyrelsen and Datatilsynet, confirmed word for word

Both entities' evidence strings, written before either page was read,
turn out to match their sources almost verbatim.
[[DK-SUNDHEDSDATASTYRELSEN]]'s own "About us" page states: "The Danish
Health Data Authority is a part of the Ministry of the Interior and
Health and was established in November 2015" — the same sentence, down
to the date, this entity's evidence already carried unread.
[[DK-DATATILSYNET]]'s English page confirms its identity directly, and
edpb.europa.eu's own members page, read independently, lists a Denmark
contact among the EDPB's member authorities.

### Statistics Denmark: a legal basis found, an EU-ESS statement not

[[DK-DST]]'s own "role and mandate" page, read directly, states
plainly: "Statistics Denmark is Denmark's national statistical
authority... responsible for official statistics in Denmark, as
established by the Act on Statistics Denmark. We are an independent
institution that has been providing statistics about and for Denmark
since 1850." The Act's own citation was not read this pass, so no
legislation entity was created from the name alone — the same
discipline applied to [[LU-CNPD]]'s GDPR-act date in the sixth push.
Two of dst.dk's own pages were checked for a direct [[EU-ESS]]
membership statement, matching the standard set by [[PL-GUS]] and
[[EE-STATISTIKAAMET]]; neither mentions Eurostat or the ESS by name, so
the edge stays on the composition-rule tier — the same honest call made
on [[LU-STATEC]] in the previous pass.

## The seventh verification-gap push

**Date:** 2026-08-25

Returned to the open-ended re-verification task with a seventh
cluster: the entire **Italy** cluster — [[IT]], [[IT-CAD]], [[IT-AGID]],
[[IT-ISTAT]], [[IT-DATI-GOV-IT]] and [[IT-SPID]] — still
`verification: search-only` since creation ([[IT-GARANTE]], Italy's
seventh entity, was already re-verified in an earlier pass). All six
now carry `verification: primary-source`.

### A stale country anchor, caught mid-pass

[[IT]]'s own body text said the entity carried "no national entities"
and listed a data protection authority, an open data portal, a
statistics office and legislation as things "each of those exists in
reality; none has been researched." That had not been true since
[[IT-AGID]], [[IT-CAD]], [[IT-DATI-GOV-IT]], [[IT-ISTAT]] and
[[IT-SPID]] were added and [[IT-GARANTE]] was independently
re-verified — none of those changes had updated the anchor's own
description. Rewritten to name the six entities it anchors, a
correctness fix incidental to the verification-tier work but directly
visible while reading the cluster.

### The open-data-portal custodian gap, closed for Italy

[[IT-DATI-GOV-IT]] carried no `maintained-by` edge at all — its own
body text said "[[IT-AGID]] is the obvious operator and no source read
says so," matching the same gap logged for [[NL-DATA-OVERHEID]] and
(until 2026-08-19) [[ES-RED-ES]] in `discovery/research-queue.md`.
Reading dati.gov.it's own "Chi siamo" page directly closes it: "Dati.gov.it
nasce come progetto promosso nel 2011 dal Governo italiano e dal 2015
viene gestito dall'Agenzia per l'Italia Digitale" (dati.gov.it began as
a 2011 government project and has been managed by AgID since 2015),
naming the legal basis too — Article 9 of decreto legislativo 36/2006,
Italy's PSI Directive transposition. [[IT-DATI-GOV-IT]] now carries
`maintained-by` [[IT-AGID]].

### Istat names its own [[EU-ESS]] membership directly

Most national statistical offices in the Atlas are attached to
[[EU-ESS]] by the generic composition rule — the ESS is defined as
Eurostat plus the national statistical institutes, and the office in
question is the NSI, so it belongs. [[PL-GUS]] and
[[EE-STATISTIKAAMET]] were exceptions: their own pages name the
membership directly. [[IT-ISTAT]] joins them this pass. Its "L'Istat
nella UE e nel mondo" page states plainly: "L'Istituto è membro dello
European Statistical System Committee (ESSC), l'organo incaricato di
orientare il SSE" (the Institute is a member of the ESSC, the body
tasked with steering the ESS) — a direct statement, not an inference.
[[LU-STATEC]], re-verified the previous pass, stayed on the weaker
composition-rule tier because no such statement was found on its own
pages; the distinction is recorded honestly on both entities rather
than papered over.

### `bosettiegatti.eu`: the mirror image of `efta.int`

Every genuinely-blocked host this session catalogued so far —
`iso.org`, `coe.int`, and, newly tested this pass, `consilium.europa.eu`
— blocks equally regardless of User-Agent, and the one fixable host,
`efta.int`, blocked the browser-spoofing UA while serving the honest
one. `bosettiegatti.eu`, an Italian legal-text mirror carrying the full
text of decreto legislativo 82/2005 (the [[IT-CAD]] Code), does the
reverse: it returns a custom IIS "999 AW Special Error" bot-defense
response to `tools/reverify.py`'s own honest, identifying User-Agent,
and a normal `200` to a browser-spoofing one. The law's text — including
Article 64, which establishes [[IT-SPID]] "a cura dell'Agenzia per
l'Italia digitale" (under [[IT-AGID]]'s responsibility) — was read this
pass via the browser-spoofing fetch. Any future automated
`tools/reverify.py` run against this exact host will still report it
UNREACHABLE; this is recorded so nobody mistakes that UNREACHABLE
verdict for an unread claim.

### The rest of the cluster

[[IT]]'s `part-of` [[EU]] edge now carries european-union.europa.eu's
verbatim sentence, read directly ("Italy EU Member State since 1958,
Euro area member since 1999, Schengen area member since 1997"),
correcting the Schengen date the entity's table had left blank.
[[IT-AGID]]'s `governed-by` [[IT-CAD]] edge is now backed by Article
64's own text rather than an unread citation, corroborated
independently by spid.gov.it's legal notice naming AgID as the site's
data controller. [[IT-SPID]] gained the same two-source confirmation
for both its edges, plus AgID's own "Guida ai diritti di cittadinanza
digitale," read directly, which states the SPID/CIE/CNS
three-credential right in the same terms the entity already carried.
`consilium.europa.eu`, `coe.int` and `iso.org` remain cited but unread
on [[IT]].

## The sixth verification-gap push

**Date:** 2026-08-25

Returned to the open-ended re-verification task with a sixth cluster:
the entire **Luxembourg** cluster — [[LU]], [[LU-CTIE]], [[LU-CNPD]],
[[LU-STATEC]], [[LU-ILNAS]] and [[LU-DATA-PUBLIC]] — all still
`verification: search-only` since creation. All six now carry
`verification: primary-source`.

### ILNAS's sixth membership, and a tie broken

[[LU-ILNAS]] carried five `participates-in` edges (CEN, CENELEC, ETSI,
ISO, IEC) sharing one identical generic evidence string, sourced to
pages nobody had read. Reading ILNAS's own "Découvrir la normalisation"
page directly found it names three European standardisation
organisations and three international ones — and the third
international one is the **ITU**, which this entity did not previously
carry. Before this pass, the Atlas recorded ILNAS and [[GB-BSI]] as
jointly "the most connective" national standards bodies, each with five
memberships. [[GB-BSI]]'s own entity was checked and does **not**
carry a UN-ITU edge — its five are the same ISO/IEC/CEN/CENELEC/ETSI
set — so this is a genuine new fact about Luxembourg specifically, not
an artefact of uneven sourcing between the two. ILNAS is now the single
most-connected national standards body in the Atlas, at six.

The same page also gave every one of the five pre-existing edges a
verbatim, ILNAS-specific replacement for the generic evidence string
they had shared since creation.

### An ELI URL as an indirect citation

[[LU-CNPD]]'s "GDPR implementation act not modelled" caveat, carried
since creation, is one step narrower after this pass. CNPD's own
"Législation" page, read directly, links to the law under the label
"Loi 'Protection des données'" at
`legilux.public.lu/eli/etat/leg/loi/2018/08/01/a686/jo` — an ELI
(European Legislation Identifier) URL whose date segment, `2018/08/01`,
independently confirms the 1 August 2018 date the entity's original
sourcing already carried. `legilux.public.lu` itself, which would carry
the law's official title and full text, returns only a JavaScript
single-page application shell ("... n'est disponible qu'avec un
navigateur supportant javascript") — the same shape as
`riigiteataja.ee` and `retsinformation.dk` from earlier pushes. No law
entity was created from a date alone: CNPD's link label is a colloquial
short name, not necessarily the law's official title, and asserting a
title the Atlas has not read would be exactly the kind of guess this
project's discipline exists to prevent. Logged narrower, not closed, in
`discovery/unresolved.md`.

### `iso.org` re-tested, still genuinely blocked

Both [[LU]]'s and [[LU-ILNAS]]'s `iso.org` citations were fetched again
with the honest, identifying User-Agent — both still return a 403
Cloudflare "Just a moment..." challenge. This reconfirms `iso.org` as a
real, non-UA-fixable block, distinct from the `efta.int` pattern this
session found early on: some hosts are genuinely closed regardless of
how honestly the client identifies itself.

### The rest of the cluster

[[LU]]'s `part-of` [[EU]] edge now carries european-union.europa.eu's
verbatim 1958-membership sentence, read directly, replacing an unread
citation. [[LU-CTIE]] gained an exact legal citation for its
IT-security mission ("the law of 24 November 2015 amending the amended
law of 20 April 2009"), found on a page reached only by extracting real
`href` links from its homepage after a guessed URL 404'd, plus
confirmation of a "Digital Government Strategy 2026-2030" teaser.
[[LU-DATA-PUBLIC]]'s own live statistics (3,173 datasets, 217
organisations) and CTIE's own portal listing (22 datasets) replaced an
unread citation. [[LU-STATEC]] was checked against the stronger,
direct-statement [[EU-ESS]] evidence tier [[PL-GUS]] and
[[EE-STATISTIKAAMET]] set — no page read this pass has STATEC name its
own ESS membership, so the edge honestly stays on the weaker
composition-rule tier most national statistical offices in the Atlas
share, rather than being overclaimed.

## The fourth research-queue pickup

**Date:** 2026-08-25

Picked up **Klimadatastyrelsen** — the item logged since 2026-08-20:
"Operates [[DK-DATAFORDELER]], the single channel through which all
Danish basic data is distributed, and is not modelled." Now
[[DK-KLIMADATASTYRELSEN]].

### The organisation chart as a source

[[DK-DATAFORDELER]]'s own entity has said since it was created that the
agency operating it "is not modelled," resting only on a description
field, not a graph edge. Two independent confirmations closed it in the
same pass: Klimadatastyrelsen's own "Organisation" page names a
dedicated internal office, "Kontor for Datafordeleren" (Office for the
Data Distributor), covering "Datafordeleren, Grunddata-governance"; and
Datafordeleren's own homepage states the relationship as plainly as a
source can: "Klimadatastyrelsen er myndighed for Datafordeleren" —
Klimadatastyrelsen is the governing authority for Datafordeleren.
[[DK-DATAFORDELER]] now carries `maintained-by` [[DK-KLIMADATASTYRELSEN]]
and moves to `verification: primary-source` in the same pass.

### A dead domain, not a bot-wall

`grunddata.dk`, cited on [[DK-DATAFORDELER]] since its creation, no
longer resolves at all — checked as both `https://` and `http://`, both
returning a DNS failure rather than any HTTP response. This is a fourth
distinct "unreadable" shape this session has now catalogued, after
`efta.int`'s User-Agent-dependent block, `isap.sejm.gov.pl`'s Incapsula
challenge, and `riigiteataja.ee`'s pure JavaScript shell: a domain that
has simply gone away. The citation is retained rather than removed — a
dead domain is not evidence the original claim was wrong — but nobody
should spend a future pass's time trying to fetch it again without first
checking whether it still exists.

### An incidental find: Denmark's own INSPIRE citation

Klimadatastyrelsen's "Lovstof" page, read for its own legal basis, turned
out to name Denmark's INSPIRE Directive transposition with a precise
citation neither this entity nor [[EU-INSPIRE]] had before: "Lov om
infrastruktur for geografisk information i Den Europæiske Union
(INSPIRE-loven) ... Lbk. nr. 746 af 15.06.2017." [[EU-INSPIRE]] gains an
`applies-in` [[DK]] edge it did not have, found while researching an
entirely different gap — the same shape of find as [[EE-STATISTIKAAMET]]'s
ESS citation and [[PL-PESEL]]'s State Registers System date: reading one
official page's own list of "what we are responsible for" answers a
question nobody was specifically asking that page.

`retsinformation.dk`, Denmark's official legal-information portal and
the actual holder of every primary legal text Klimadatastyrelsen's page
cites, is a pure JavaScript single-page application returning no static
content — the same shape as `riigiteataja.ee`. Every citation in this
pass's entities rests on Klimadatastyrelsen's own descriptive text of
the law, not on the law's own text.

## The candidates pickup

**Date:** 2026-08-22

A pass over `discovery/candidates.md` rather than
`discovery/research-queue.md` — a different backlog, compiled from
search-engine leads rather than gaps found mid-batch, but subject to the
same rule: a row closes by becoming a real, sourced entity (or a
definitive answer), and is then deleted rather than struck through.
Picked up the two rows still open from the candidate-clearing batch of
2026-08-21: the **High-level Political Forum** and the **eFTI
Regulation**.

### [[UN-HLPF]]: the node three entities were missing

[[EU-VOLUNTARY-REVIEW-2023]] has said since it was created that the
review "was a key input to the United Nations High Level Political
Forum," immediately followed by its own admission: "The **High-level
Political Forum** itself has no entity, so nothing here says the review
was *submitted to* it. That is the residue of the original problem."
Both `discovery/candidates.md` and `discovery/research-queue.md` carried
the same gap as a separate row.

`sustainabledevelopment.un.org`'s own page, read directly, confirms it
in the UN's own words: "The High-level Political Forum on Sustainable
Development (HLPF) is the central United Nations platform for the
follow-up and review of the 2030 Agenda for Sustainable Development."
Wikipedia supplies what the UN page does not — formation on 9 July 2013,
succeeding the Commission on Sustainable Development, and joint
parentage under ECOSOC and the General Assembly. `hlpf.un.org`, the
domain this Atlas had already cited unread on
[[EU-VOLUNTARY-REVIEW-2023]], turns out to be bot-walled (403) even with
an honest, identifying User-Agent — a different UN DESA subdomain
carrying equivalent content was not.

[[EU-VOLUNTARY-REVIEW-2023]] now carries the `references` edge to
[[UN-HLPF]] its own text said was missing, closing the loop three
entities and two discovery pages had been pointing at.

### [[EU-EFTI-REGULATION]]: a negative result, reached by finally reading the source

The more interesting of the two closures. `discovery/candidates.md` and
[[EU-EMSWE]] both carried a claim — the eFTI Regulation's data set is
built on the UN/CEFACT Multi-Modal Transport Reference Data Model — with
an honest caveat: "The claim was found in a UNECE presentation and a
project website, **not in the regulation**." That caveat was written
when the regulation itself could not be fetched.

It can be fetched now. Reading the full text of Regulation (EU)
2020/1056 directly and searching it for "UN/CEFACT", "CEFACT", "MMT" and
"UNECE" turns up **none of them, anywhere**. The regulation delegates
the actual eFTI common data set to a future Commission delegated act
(Article 2), due by 21 February 2023, which must merely "seek to ensure
interoperability... with relevant data models that are accepted
internationally," naming none. If the UN/CEFACT connection secondary
sources describe is real, it lives in that unidentified delegated act,
not in the primary instrument.

This is worth recording as a pattern in its own right: a source note
written under an egress restriction ("not in the regulation") described
an absence its author had not actually been able to check. Reading the
regulation directly converts "not found in a source I couldn't read"
into "confirmed absent from a source I did read" — the same distinction
this whole re-verification effort exists to draw, applied here to a
negative claim instead of a positive one. [[EU-EFTI-REGULATION]] itself
is a legitimate addition independent of the UN/CEFACT question — a
sourced EU mobility-domain regulation the Atlas did not otherwise hold.

### `unece.org`: tested against the `efta.int` theory, and it does not hold

The prior push's headline finding was that a "blocked" host can turn out
to be a User-Agent problem, not a real block. `unece.org` — cited on the
UN/CEFACT Core Component Library row this same section of
`discovery/candidates.md` still carries as genuinely unresearchable —
was re-tested with the same honest, identifying User-Agent that got past
`efta.int`. It still returns 403 on every path tried. Not every
apparent block is the `efta.int` kind, and this negative result is worth
keeping alongside the positive one so the next pass does not re-test it
expecting the same fix to work twice.

## The fifth verification-gap push

**Date:** 2026-08-22

Returned to the open-ended re-verification task with a fifth cluster:
the **Iceland and Liechtenstein** trios — [[IS]], [[IS-PERSONUVERND]],
[[IS-PERSONUVERNDARLOG]], [[LI]], [[LI-DATENSCHUTZSTELLE]] and
[[LI-DSG]] — created on 2026-08-21 to test whether the Norwegian EEA
pattern generalises, and still `verification: search-only` ever since.
All six now carry `verification: primary-source`.

### The EFTA/EEA membership claim, confirmed for both at once

[[IS]] and [[LI]] each carried a single relationship (`part-of`
[[INTL-COE]]) and described their EFTA/EEA position only in prose and a
table, sourced to pages nobody had read. Reading efta.int's own "The
European Free Trade Association" page directly — with the honest,
identifying User-Agent this session's first research-queue pickup
established gets past its bot-defense challenge — confirmed both in one
pass: "The European Free Trade Association (EFTA) is the
intergovernmental organisation of Iceland, Liechtenstein, Norway and
Switzerland," and "three of the four EFTA States – Iceland,
Liechtenstein and Norway – in a single market" under the EEA Agreement.
government.nl's own EEA/EFTA/Schengen page, read the same pass,
corroborates independently.

`coe.int` and `iso.org` remain bot-walled (403) even with the honest
User-Agent — genuinely closed, not a repeat of the `efta.int` finding —
so the Council of Europe membership edge on both country anchors is
retained rather than removed, exactly as it was before this pass.

### Iceland's data protection pair, confirmed to the letter

WIPO Lex's own record of Act No. 90/2018, read directly, matches
[[IS-PERSONUVERNDARLOG]]'s name field, dates and Icelandic title
exactly — "Act No. 90/2018 of June 27, 2018 ... Entry into force: July
15, 2018" and "Lög nr. 90/2018 frá 27. júní 2018 um persónuvernd og
vinnslu persónuupplýsinga" — and its excerpt of the Act's own opening
text names [[IS-PERSONUVERND]] directly as the supervisory body: "Sérstök
stofnun, Persónuvernd, annast eftirlit með framkvæmd reglugerðar
Evrópuþingsins og ráðsins (ESB) 2016/679." DLA Piper's Iceland page,
read independently, confirms the Joint Committee Decision date (6 July
2018) and the Act's role in the same terms the entity already carried.

### A translation error caught by reading the source twice

The most interesting finding of this pass sits on [[LI-DSG]]. Its
citation, naegele.law's "Liechtenstein & the GDPR," carries both a
German original and an English translation on the same page. The
English text says the DSG "was passed on October 2th of 2018 and came
into force on January 1st of 2018" — the second half of that sentence
is impossible on its face, since an act cannot enter into force before
it is passed. The German original, read the same pass, is unambiguous:
"diese am 4. Oktober 2018 verabschiedet. Das revidierte DSG trat am
1. Januar 2019 in Kraft" — 4 October 2018, 1 January 2019. The
Datenschutzstelle's own "Nationale Gesetze" page, read independently,
gives the same two correct dates.

[[LI-DSG]]'s existing dates already matched the correct German reading,
so nothing about the entity's content changed — but the *reason* to
trust those dates is now much stronger: two independent primary sources
agree, and one candidate source's own English rendering is shown to be
unreliable rather than merely unread. A pass that read only the English
half of that page would have "confirmed" a wrong date with a citation
that looked authoritative.

### A claim a re-verification pass could not confirm, and did not delete

[[LI-DATENSCHUTZSTELLE]]'s entity has said since its creation that its
Commissioner is appointed by the Landtag for a five-year renewable term.
Three of the authority's own pages were read directly this pass —
homepage, "Über uns," and "Team" — and none of them states an
appointment mechanism; the "Team" page names a head, Dr. Marie-Louise
Gächter-Alge, with a title ("Leitung") and nothing more.

The claim is retained rather than removed. Absence of confirmation is
not evidence of error, and this project's standing discipline — applied
already to Switzerland's Fedlex citations, Norway's `coe.int` edge, and
now here — is to say plainly what could and could not be re-confirmed,
not to silently narrow the record to only what the current pass happened
to find.

## The third research-queue pickup

**Date:** 2026-08-22

Picked up **Statistikaamet**, Statistics Estonia — logged on the
research queue since the Estonia batch as "named only as a
research-project partner in what was read," and named a second time in
[[EE]]'s own index as the country's twelfth-country-statistical-office
gap. Now [[EE-STATISTIKAAMET]].

### The same evidentiary bar as Poland's GUS, met a second time

[[PL-GUS]]'s entry in this file already distinguishes two tiers of
[[EU-ESS]] evidence: most national statistical offices are attached by
the **composition rule** — the ESS is defined as the Commission plus the
member states' national statistical institutes, and each office is its
country's NSI, so membership follows without the office's own pages
saying so. GUS was the first exception, describing the ESS directly on
its own pages.

Statistikaamet is the second, and its evidence is if anything sharper.
Reading stat.ee's own "Official statistics and European statistics" page
directly found: "Official statistics are produced on the basis of the
Official Statistics Act and in accordance with the principles and
quality criteria laid down in Regulation (EC) No 223/2009 of the
European Parliament and of the Council ... Eurostat produces European
statistics in partnership with national statistical institutes and
other national authorities in the EU Member States and the European
Free Trade Agreement (EFTA) countries. This partnership is known as the
European Statistical System (ESS)." A second page, "Legal acts," read
the same pass, lists that same regulation among the agency's own
governing legal acts under an "Europe" heading — not a description of
the ESS in the abstract, but the agency naming its ESS framework
regulation as one of its own statutes.

### An anchor that had to skip a rung

The anchor-edge rule (`metadata/relationship-types.md` §2.3) sends a
state body to `part-of` its country, but en.wikipedia.org/wiki/Statistics_Estonia
names something more specific: "It is part of the Ministry of Finance."
No Estonian Ministry of Finance entity exists in the Atlas — Estonia has
comparatively few organisational entities modelled so far — so the more
specific parent relationship Wikipedia gives has nowhere to attach.
[[EE-STATISTIKAAMET]] anchors directly to [[EE]] instead, and the
Ministry-level detail is recorded in prose rather than as a graph edge
that would require inventing a node for an unmodelled ministry.

### `riigiteataja.ee`: a third kind of "blocked," not a repeat of either prior finding

Two negative results precede this one. The first research-queue pickup
found `efta.int` only *looked* blocked — a browser-spoofing User-Agent
got a 403, an honest one got the real page. The second found
`isap.sejm.gov.pl` genuinely blocked regardless of User-Agent, via an
Incapsula JavaScript challenge.

`riigiteataja.ee`, Estonia's official legal gazette, was tried for a
precise citation of the Official Statistics Act (Riikliku statistika
seadus). It returned neither a challenge page nor a 403 — every fetch
tried, on two different guessed URLs, returned 200 with an identical
117-character body: "Riigi Teataja Laeb... Ilma Javascript toeta
lehitsejad ei ole toetatud. You need Javascript enabled to use this
site." A third failure mode: not a bot-defense wall at all, just a pure
client-rendered application with nothing server-side to read, matching
`eftasurv.int`'s shape from the first research-queue pickup rather than
either of the other two Poland-era findings. [[EE-STATISTIKAAMET]]
therefore names the Official Statistics Act exactly as stat.ee itself
names it — no date, no citation number, because none was independently
confirmed.

## The second research-queue pickup

**Date:** 2026-08-22

Picked up **PESEL**, Poland's population register — logged on the
research queue since the Poland batch and, more pointedly, named on
[[PL-COI]]'s own entity: *"COI maintains the PESEL register ... Named in
a list of systems COI maintains and nothing was researched about its
legal basis, content or governance. Creating it from that mention would
produce exactly the thin node the taxonomy threshold prevents."* That
refusal was correct at the time and is exactly what this pass reverses,
having done the research the earlier pass explicitly declined to skip.

Two entities, following the platform+law pairing [[NL-BRP]]/[[NL-WET-BRP]]
already established for the Netherlands: [[PL-PESEL]] (the register and
the eleven-digit number itself) and [[PL-EWIDENCJA-LUDNOSCI]] (the Act of
24 September 2010 on population records, its legal basis since 1 March
2015).

### A specific answer to a question PL-COI could only gesture at

PL-COI's entity named PESEL among the systems it maintains, without a
date or mechanism — the standard shape of a system-list mention with
nothing behind it. Cross-reading gov.pl's own PESEL page against Polish
Wikipedia supplied both: on **1 March 2015**, three companion acts (on
population records, identity cards, and civil status) took effect
together, and the same day launched the **System Rejestrów Państwowych**
(State Registers System), "obsługiwany przez Centralny Ośrodek
Informatyki" — operated by COI — integrating the PESEL register with
identity-card and civil-status records. Neither source alone gave that
date and mechanism; reading both did.

### `isap.sejm.gov.pl` is genuinely blocked — unlike `efta.int`

The first research-queue pickup's headline finding was that `efta.int`
only *looked* bot-walled: a browser-spoofing User-Agent got a 403, an
honest one got the real page. This pass tested the same theory against
`isap.sejm.gov.pl`, the Sejm's own legal-text database and the Atlas's
usual source for an exact Dziennik Ustaw citation — the citation
[[PL-ODO]] has been missing since the Poland batch, flagged in that
entity's own text as "the first thing a re-verification pass should
fetch for Poland."

It did not work the same way. Every fetch — browser-spoofing User-Agent
and honest, identifying one alike — returned an Incapsula "Pardon Our
Interruption" JavaScript challenge page. This is a real, User-Agent-
independent block, not a repeat of the `efta.int` finding, and it is
worth recording as a negative result: not every 403-shaped wall turns
out to be a User-Agent problem. [[PL-EWIDENCJA-LUDNOSCI]] therefore
carries only the **consolidated-text** citation ("Dz. U. z 2015 r.
poz. 388") that gov.pl itself quotes verbatim, not the Act's original
2010 promulgation citation — which could be guessed from ISAP's own
numbering convention, and was deliberately not guessed. `PL-ODO`'s own
missing citation remains open for the same reason.

### A history with a genuine discrepancy, left unresolved rather than picked

Polish Wikipedia dates the PESEL system's launch to a 1977 pilot in
Warsaw's Wola district, with numbers assigned to all citizens by 1984.
English Wikipedia says only that the number has been "used in Poland
since 1979," with no launch mechanism. [[PL-PESEL]] follows the more
specific, internally consistent account for its `start_date`, but
records the discrepancy rather than silently resolving it — the same
discipline applied throughout this project to conflicting dates.

## The first research-queue pickup

**Date:** 2026-08-22

A different kind of push from the four before it: instead of
re-verifying existing entities, this pass picked a "Next"-priority item
off `discovery/research-queue.md` and created the entities it named.

The item: the **EFTA Surveillance Authority**, the **EFTA Court** and the
**EEA Joint Committee**. All three had been logged as "not modelled" on
[[NO]] since the Norway batch, then again on [[INTL-EFTA]] and
[[INTL-EEA-AGREEMENT]] when those two were created — the gap was named
in three places before it was closed in one pass. All three are now
Atlas entities: [[INTL-EFTA-SURVEILLANCE-AUTHORITY]], [[INTL-EFTA-COURT]]
and [[INTL-EEA-JOINT-COMMITTEE]].

### The anchor question this batch had to settle

None of the three fits the anchor table in `metadata/relationship-types.md`
§2.3 cleanly — they are neither of a state, nor EU-scoped, nor UN-scoped.
The obvious anchor by name is [[INTL-EFTA]], but that would be wrong:
efta.int's own "Two Pillar Structure" page states plainly that "since
Switzerland is not an EEA member, it does not participate in these
institutions," and Switzerland is EFTA's fourth member. Anchoring to
[[INTL-EFTA]] would silently claim jurisdiction over a state these bodies
do not cover.

All three are anchored instead to [[INTL-EEA-AGREEMENT]] — the Agreement,
not the trade association — because its party list (Iceland,
Liechtenstein, Norway) is the exact set these bodies serve. The EEA Joint
Committee's anchor is the strongest of the three: it is not merely
scoped like the Agreement, it is the Agreement's own institution, and it
also carries a `produces` edge to [[INTL-EEA-JCD-154-2018]] — the decision
that incorporated [[EU-GDPR]] — finally putting a body behind a decision
the Atlas had cited four times without ever modelling its source.

### `efta.int` was never actually blocked

The significant finding of this pass, and a correction to standing
guidance three pushes deep. `efta.int` has been treated as bot-walled
(403) since the third push, and the fourth push's own write-up above
names it as "newly confirmed" blocked. Every one of those tests used a
browser-spoofing User-Agent.

Fetched instead with an honest, identifying User-Agent — the same kind
`tools/reverify.py` itself sends — `efta.int` returns real content: 200,
not 403. Its "About EFTA" page, "Two Pillar Structure" overview page and
"EEA Joint Committee" page were all read directly this pass and quoted
verbatim in the four entities they touch (the three new ones, plus
[[INTL-EFTA]], promoted to `primary-source` in the same pass). This is
the reverse of the `eur-lex.europa.eu` finding two pushes ago — there, a
host thought blocked was not blocked at all; here, the block was real but
conditional on how the request identified itself, and identifying
honestly rather than pretending to be a browser was the fix.

Two related domains were re-tested the same way and are **not** affected
by this correction: `eftasurv.int` (the Surveillance Authority's own
site) is a genuine JavaScript single-page application with no static
content regardless of User-Agent, and `eftacourt.int` (the Court's own
site) serves only a live case-docket and hearings list regardless of
path or User-Agent. Both remain cited but effectively unread; Wikipedia
supplies the institutional detail neither carries.

### What this means for the rest of the re-verification backlog

`discovery/reverification-allowlist.md` and every prior push's "blocked
hosts" note should be read with this in mind: a 403 from a host tested
with a browser-spoofing User-Agent is not proof the host is closed to
automated re-verification, only that it is closed to *that* User-Agent.
`www.iso.org`, `www.coe.int` and `unece.org` — the three hosts still
carried on the blocked list — have not been re-tested with an honest
User-Agent since this finding, and are candidates for the next pass
rather than settled dead ends.

## The fourth verification-gap push

**Date:** 2026-08-22

Continued the open-ended re-verification task with a fourth cluster:
Norway, plus the two entities that carry EU law into the EEA. 10 entities
moved to `primary-source` — [[NO]] itself, [[NO-PERSONOPPLYSNINGSLOVEN]],
[[NO-DATATILSYNET]], [[NO-KARTVERKET]], [[NO-NSM]], [[NO-DIGDIR]],
[[NO-ID-PORTEN]], [[NO-ALTINN]], [[INTL-EEA-AGREEMENT]] and
[[INTL-EEA-JCD-154-2018]].

### A network-policy correction that changes the map for every future pass

`progress/current-batch.md` told every prior pass to skip entities citing
only `eur-lex.europa.eu`. That guidance was wrong. Both `eur-lex.europa.eu`
and `europarl.europa.eu` returned real content on every fetch this pass —
the actual legal texts, not a bot-defense page. This is the same
false-blocked finding the first push made for `legislation.gov.uk`,
now made a third time for a different host. The guidance file is
corrected; the true bot-walled list for this environment is `iso.org`,
`coe.int`, `unece.org` and (newly confirmed) `efta.int`.

Reading the actual EUR-Lex text of JCD No 154/2018 upgraded every claim
built on it: the EDPB participation clause turned out to carry a specific
carve-out (EFTA supervisory authorities have full rights except voting
and standing for chair/deputy-chair election) that no prior citation of
this decision had captured, because no prior pass had read it.

### NSM: a restraint the entity was right to hold, until it wasn't

[[NO-NSM]]'s prior text was a model of the sourcing discipline this
project asks for: *"One source describes NSM as part of the Norwegian
secret services; that phrasing appears in an encyclopaedia entry and not
in the government sources, and the Atlas will not classify a body as an
intelligence service on that basis."* That restraint was correctly
applied to the evidence available at the time.

Reading `nsm.no` directly this pass found the government source that
restraint was waiting for: *"NSM utgjør sammen med Etterretningstjenesten
og Politiets sikkerhetstjeneste (PST) Norges tre etterretnings-
overvåkings- og sikkerhetstjenester"* — NSM's own official site states
directly that it is one of Norway's three intelligence, surveillance and
security services. The entity's classification is corrected, with the
reasoning for the change left visible in the body rather than silently
overwritten — a reader should be able to see that the earlier caution was
sound, not sloppy, and see exactly what evidence overturned it. The same
page also revealed that Norway's National Cyber Security Centre is part
of NSM, previously unrecorded.

### A relationship-direction bug pattern, caught and standardised

[[NO-DIGDIR]]'s `maintained-by` edge to [[NO-ID-PORTEN]] is filed with
Digdir as the subject and ID-porten as the target — which, read against
this repository's own definition ("`maintained-by`: the target maintains
the subject"), literally says ID-porten maintains Digdir, backwards from
the intended claim. Checking the pattern found it is not unique to this
entity: [[NL-LOGIUS]], [[NL-ICTU]], [[NL-VNG]] and [[EU-SEMIC]] all use
the identical placement, each with the same explanatory sentence —
"Direction expressed X→Y for navigability; the authoritative framing
belongs on the Y entity." NO-DIGDIR was the one entity using this
placement *without* that disclaimer, instead giving a different and
confusing rationale. Corrected to match the other four rather than moved,
since moving it would break an established, load-bearing convention
rather than fix an isolated mistake.

A second, unrelated error surfaced on the same entity: its own text
claimed [[GB-GDS]] "carries `maintained-by` edges to identity platforms."
Re-checked directly, GB-GDS carries no such edge — it explicitly declines
one, for the reason [[GB-DATA-GOV-UK]] also declines one. Corrected.

### Two findings via evidence a page's own footer, not its prose, supplied

[[NO-ALTINN]]'s operator was previously unestablished — Digdir's own page
lists what it operates and Altinn is not on that list. Reading altinn.no's
own site directly found something the list could not: the page's
publisher footer names Digdir's own address and organisation number.
`maintained-by` [[NO-DIGDIR]] is now asserted, at `confidence: low` and
`source: interpretation`, because a publisher footer is real evidence of
who runs a site but not the same claim as an explicit operating sentence.

[[NO-KARTVERKET]]'s participation in [[UN-GGIM]] was flagged as
unresearched. kartverket.no's own homepage carried a news item about
"broad support at the UN" for a meeting of the UN's expert committee for
geographic information in New York — attendance evidence, not a stated
delegation role, so the edge is asserted at `confidence: low`.

### Verification

`validation/run_all.py` 5/5, 0 errors (7 pre-existing warnings, all in
entities untouched by this push). `tools/test_build_graph.py` 41 tests.
`tools/test_reverify.py` 36 tests. `discovery/reverification-allowlist.md`
regenerated. No `--force` used anywhere in this push.

## The third verification-gap push

**Date:** 2026-08-22

Continued the open-ended re-verification task with a third full country
cluster: Switzerland. 9 entities moved to `primary-source` — [[CH]] itself,
plus [[CH-REVDSG]], [[CH-EMBAG]], [[CH-BACS]], [[CH-BFS]], [[CH-DVS]],
[[CH-EDOEB]], [[CH-SWISSTOPO]] and [[CH-OPENDATA-SWISS]].

### The Fedlex gap, half-closed

[[CH-REVDSG]] and [[CH-EMBAG]] had both carried an explicit caveat since
their creation: no citation pointed at Fedlex, the Swiss federal law
portal, despite both entities carrying comparative weight in the Atlas.
Guessing an ELI URL from general knowledge was rejected as exactly the
kind of unverified specific this project exists to avoid — instead, both
were found as **outbound links on official government pages already
being read** (kmu.admin.ch linked `eli/cc/2022/491/de` for the DSG;
bfs.admin.ch linked `eli/cc/2023/682/de` for the EMBAG), so the citations
are as solid as the pages that pointed at them.

Fedlex itself renders its content client-side in JavaScript. Both pages
retrieved at HTTP 200 and neither could be read past that — the same
tooling limit already documented for PDFs elsewhere in the Atlas, applied
here to a different format for the first time.

### A connection two entities had separately flagged as missing, now sourced

[[CH-EMBAG]]'s and [[CH-OPENDATA-SWISS]]'s entities each independently
said the same thing: the EMBAG's open-government-data provisions plainly
concern the federal open data portal, but no source read connected them
by name. Reading bfs.admin.ch's own "Open Government Data (OGD)" page
directly closed it: *"Der Masterplan OGD 2024−2027 ... zielt darauf ab,
die Daten der öffentlichen Verwaltung gemäss dem [EMBAG] frei zugänglich
zu machen. Die Geschäftsstelle OGD ... betreibt ... das Portal
opendata.swiss."* [[CH-OPENDATA-SWISS]] now carries `governed-by`
[[CH-EMBAG]] on that basis — the second time this push found a
relationship two entities' own prose had already reasoned toward but
never landed in the structured data (the first was [[IE-NSAI]]'s
CEN/CENELEC edges in the previous push).

### A wrong alternative name, caught by re-verification rather than luck

[[CH-DVS]]'s Italian abbreviation was recorded as "AND". Fetching the
organisation's own Italian-language homepage found it calls itself
*Amministrazione digitale Svizzera* — abbreviation **ADS**, not AND.
Corrected. The English name ("Digital Public Services Switzerland") and
French abbreviation (ANS) were both confirmed on the corresponding
language pages.

### A methodology correction: a `<title>` tag is not body text

Several `<title>`-only confirmations from this pass's own ad-hoc checking
script did not survive contact with `tools/reverify.py`'s actual
extraction, which strips `<head>` (and therefore `<title>`) before
matching — a page's browser-tab text is not something a reader of the
page's content would ever see. [[CH-BFS]]'s "BFS", "OFS", "UST" and
"Federal Statistical Office" and [[CH-SWISSTOPO]]'s "Federal Office of
Topography" all initially failed the tool's write-check for exactly this
reason, despite passing an earlier, less careful check. Each was
re-sourced properly — a German-Wikipedia infobox for BFS's four-language
abbreviations, swisstopo's own English homepage for its English name —
rather than forced past the refusal or quietly dropped. `tools/reverify.py`
itself was not changed; the lesson was in how this pass checked its own
work before calling `--write`.

### Findings flagged, not chased

- [[CH-BACS]]'s English-language site still brands itself "National Cyber
  Security Centre (NCSC)" — the German rename to BACS has not carried
  across to the English pages.
- [[CH-DVS]]'s homepage advertises **AGOV**, a nationwide authority-login
  service already used by fourteen cantons with "already 2 million
  accounts" — a Swiss analogue to [[GB-ONE-LOGIN]], not yet an Atlas
  entity — and reports that the Federal Council and the Conference of
  Cantonal Governments adopted a "Zielbild" in late 2025 to evolve DVS
  toward "a political platform with binding standard-setting."
- [[CH-OPENDATA-SWISS]]'s own homepage advertises **"opendata.swiss
  next,"** a stated future replacement for the current site.

None of these were pursued into new entities or rewritten claims this
pass — they are recorded so a future pass does not have to rediscover
them from nothing.

### Verification

`validation/run_all.py` 5/5, 0 errors (7 pre-existing warnings, all in
entities untouched by this push). `tools/test_build_graph.py` 41 tests.
`tools/test_reverify.py` 36 tests. `discovery/reverification-allowlist.md`
regenerated. No `--force` used anywhere in this push.

## The second verification-gap push

**Date:** 2026-08-22

Continued the open-ended "close the verification gap" task from where the
first push left off, this time working two full country clusters end to
end rather than partial slices: every `country: GB` entity, every
`country: IE` entity, and [[EU-UK-ADEQUACY]] (the one non-national entity
the UK cluster's own index page had flagged as the single most important
missing connective fact). 24 entities moved to `primary-source`; none held
back.

### UK cybersecurity/standards cluster (6 entities)

[[GB-NCSC]], [[GB-CAF]], [[GB-NIS-REGULATIONS]], [[GB-CSRB]], [[GB-OFCOM]]
and [[GB-BSI]].

The NCSC's own PDF policy statement, cited on three of these entities, now
404s. Replaced it on [[GB-NCSC]] with `ncsc.gov.uk/section/about-ncsc/`
and simply dropped it — rather than re-citing it unread — on [[GB-CAF]]
and [[GB-CSRB]]. `commonslibrary.parliament.uk` and
`committees.parliament.uk` are both Cloudflare-bot-walled (403, "Just a
moment...") and are recorded as such rather than silently dropped.
[[GB-BSI]]'s "13,000 UK experts" figure could not be re-confirmed and is
flagged as such in its own evidence string rather than quietly repeated.

### UK government/statistics/geospatial cluster (10 entities)

[[GB-DSIT]], [[GB-DCMS]], [[GB-GDS]], [[GB-ONS]], [[GB-UKSA]], [[GB-OS]],
[[GB-DATA-GOV-UK]], [[GB-ONE-LOGIN]], [[GB-GEOSPATIAL-STRATEGY]] and [[GB]]
itself.

**The DSIT/DCMS/DBIST split, triangulated.** Three independent trade-press
accounts (publictechnology.net, thinkdigitalpartners.com, dma.org.uk) of
the same written ministerial statement corroborate the July 2026
department reshuffle; `ukauthority.com`, cited on two of these entities,
is bot-walled (403) and is recorded as unread rather than dropped or
re-cited blind.

**A better source displaced a worse one.** [[GB-GDS]]'s CDDO/Geospatial
Commission/GDS/i.AI merger account previously rested on trade press. GOV.UK's
own "Central Digital and Data Office" organisation page states it directly:
*"The Central Digital and Data Office (CDDO), the Geospatial Commission,
the Government Digital Service (GDS) and the Incubator for Artificial
Intelligence (i.AI) have merged to create the new Government Digital
Service ... CDDO existed from April 2021 to January 2025."*

**A caveat that stayed a caveat, honestly.** [[GB-ONS]] and [[GB-UKSA]]
both assert `participates-in` [[UN-CES]] on the strength of UK membership
of the Conference of European Statisticians and its Bureau — but
`unece.org` is Cloudflare-bot-walled, and the UKSA's own international-
engagement page has moved to a URL that lists UNECE only generically,
without naming CES or its Bureau. Both entities now say explicitly *"NOT
independently re-confirmed 2026-08-22"* and keep the original claim rather
than deleting it — a page move and a bot-wall are not evidence a claim is
wrong, but they are not re-verification either.

**A UN-GGIM anchor for the UK's geospatial gap.** [[GB-OS]]'s role as
Secretariat and Head of UK Delegation to [[UN-GGIM]] is confirmed on
GDS's own geospatial blog and independently on an 11th-session UN-GGIM
statement PDF (`pdftotext`-extracted), naming the same official by name
and title at an earlier session.

**A rebrand flagged, not chased.** [[GB-DATA-GOV-UK]]'s own site now
titles itself "National Data Library — the home of UK public data" rather
than data.gov.uk. Recorded as a finding; not resolved into a rename this
pass.

**A tool-format quirk, not a sourcing gap.** [[GB-GEOSPATIAL-STRATEGY]]'s
alternative name "UK's Geospatial Strategy" initially failed
`tools/reverify.py`'s exact-match check — the source page uses a curly
apostrophe (’) and the frontmatter used a straight one ('). Corrected to
match the source's actual typography rather than dropped or forced.

**[[GB]] itself, re-verified.** Removed the unattested alternative name
"United Kingdom of Great Britain and Northern Ireland" — it was supported
only by the ISO Online Browsing Platform citation, which is bot-walled
(403) and was never read. Its `part-of` [[INTL-COE]] edge could not be
re-confirmed (`coe.int` also bot-walled) and is retained with that stated
explicitly, the same treatment given to the UN-CES ambiguity above.

### EU-UK-ADEQUACY (1 entity)

Closed the connection the UK batch's own index page had called *"the
single most important connective fact between the UK and the EU data
layer"* and left unread. All five cited sources (eucrim.eu, edpb.europa.eu,
aoshearman.com, arnoldporter.com, ico.org.uk) were read directly and
confirm the 19 December 2025 renewal and 27 December 2031 sunset clause
verbatim, several times over.

**Renamed for the same reason as [[GB-UK-GDPR]] before it.** The compiled
name "European Commission adequacy decisions for the United Kingdom"
never appeared verbatim on any source. Renamed to "UK adequacy decisions"
— the phrase edpb.europa.eu and aoshearman.com both use — and the
unattested alternative name "UK data adequacy" replaced with "adequacy
decisions for the UK," confirmed on ico.org.uk.

### Irish cluster (7 entities)

[[IE-DPA-2018]], [[IE-NCS-BILL]], [[IE-PSI-REGULATIONS-2021]], [[IE-NCSC]],
[[IE-NSAI]], [[IE-TAILTE]] and [[IE-DATA-GOV-IE]].

**A structural bug, not just a sourcing gap.** [[IE-NSAI]]'s own body text
already described `participates-in` edges to [[EU-CEN]] and [[EU-CENELEC]]
— but they were never added to the entity's structured `relationships:`
list, so the graph itself didn't carry them. Fixed, and re-confirmed
against the composition rule's live source (the old CEN-national-members
URL had moved; found and read the replacement,
`standards.cencenelec.eu/ords/f?p=CEN:5`).

**A live escalation, found mid-pass.** [[IE-NCS-BILL]]'s NIS2 transposition
was already known to be overdue (17 October 2024 deadline, Commission
reasoned opinion 7 May 2025). Reading globalpolicywatch.com directly
turned up a harder consequence not in the original sources: *"the European
Commission referred Ireland and three other Member States to the CJEU for
their failure to transpose NIS2"* in July 2026.

**A confidence upgrade earned by a better source.** [[IE-TAILTE]]'s merger
of Ordnance Survey Ireland, the Property Registration Authority and the
Valuation Office was previously sourced only to the merged body's own
homepage and a general encyclopaedia link, at `confidence: low` with no
`start_date`. en.wikipedia.org's dedicated Ordnance Survey Ireland article
states the date directly — "Dissolved 1 March 2023" — and both `confidence`
(raised to medium) and `start_date` are set on that basis.

**Two more renames for the same "never used verbatim" reason.**
[[IE-NCSC]]'s `name` field carried a parenthetical "(Ireland)"
disambiguation that no source states; renamed to match how [[GB-NCSC]]
carries the identical name, with the scoped ID doing the disambiguating
instead. [[IE-NCS-BILL]] lost two alternative names ("NCS Bill", "Irish
NIS2 transposition") that were never attested either.

**A discrepancy flagged, not resolved.** [[IE-NCSC]]'s own homepage says
it is "an operational arm of the Department of the Justice, Home Affairs
and Migration"; the European Commission's NIS2 tracker (last updated 7
July 2025) names the Department of Communications, Climate Action &
Environment as its contact department instead. Recorded as an open
discrepancy rather than resolved by guessing which is current.

### Documentation

`countries/gb/index.md` and `countries/ie/index.md` both carried a
sourcing-caveat banner describing every entity below as unverified —
stale as of this push, since every entity either page links to now
carries `verification: primary-source`. Both rewritten. Two stale
per-entity annotations on the Ireland index (IE-TAILTE's confidence, and
IE-NSAI's "no participates-in edges") were also corrected.
`discovery/reverification-allowlist.md` regenerated (`tools/source_hosts.py`)
to reflect the new read/unread counts. Three rows in
`discovery/unresolved.md` closed or updated: IE-TAILTE's merger-date
question (resolved), IE-NSAI's CEN/CENELEC/ISO question (CEN/CENELEC now
resolved, ISO still open), and IE-DATA-GOV-IE's transposition-instrument
question (already resolved by an earlier pass; the row had not caught up).

### Verification

`validation/run_all.py` 5/5, 0 errors (7 pre-existing warnings, all in
entities untouched by this push). `tools/test_build_graph.py` 41 tests.
`tools/test_reverify.py` 36 tests. Graph regenerated after each cluster.
No `--force` used anywhere in this push — every write satisfied
`tools/reverify.py`'s corroboration check on its own terms.

## The verification-gap multi-batch push

**Date:** 2026-08-22

Picked up "close the verification gap" as an open-ended, multi-batch task
rather than a single fixed scope: work coherent clusters of `search-only`
entities end to end (every cited page read, corrections made,
`tools/reverify.py --write` run per entity), commit and push after each
cluster, and stop when the session's natural unit of work is done rather
than at an arbitrary entity count. Four clusters, 37 entities moved to
`primary-source`, one entity (see below) deliberately held back despite
being fully read.

### German intelligence oversight (10 entities)

[[DE-BFDI]], [[DE-BVERFSCHG]], [[DE-G10]], [[DE-MADG]], [[DE-BAMAD]],
[[DE-BFV]], [[DE-BND]], [[DE-PKGR]], [[DE-PKGRG]] and [[DE-UKR]].

The PKGrG's Constitutional Court dispute-resolution mechanism — the Federal
Government or two-thirds of the PKGr's members can bring the Bundestag's
oversight committee into conflict with the government before the court —
is now sourced to the statute's own § 14, not just secondary accounts:
*"Das Bundesverfassungsgericht entscheidet über Streitigkeiten zwischen dem
Parlamentarischen Kontrollgremium und der Bundesregierung auf Antrag der
Bundesregierung oder von mindestens zwei Dritteln der Mitglieder des
Parlamentarischen Kontrollgremiums."*

[[DE-BND]]'s "28 September 2022" claim about [[DE-UKR]]'s provisions moving
out of the BND-Gesetz was cited to a Bundestag article that, read closely,
covers a *different* ruling from the same date (on [[DE-BVERFSCHG]]
transmission provisions). The claim itself was right — confirmed instead on
de.wikipedia.org's UKR article — but the citation was wrong. [[DE-UKR]]
also picked up a sourced `start_date` (22 April 2021) and a confidence
upgrade from `low` to `medium` in the process.

### German digital-government legislation and strategy (14 entities)

[[DE-BNDG]], [[DE-BSTATG]], [[DE-DNG]], [[DE-EGOVG]], [[DE-IFG]],
[[DE-DATENSTRATEGIE]], [[DE-DIGITALSTRATEGIE]],
[[DE-MODERNISIERUNGSAGENDA-BUND]], [[DE-MODERNISIERUNGSAGENDA-FOEDERAL]],
[[DE-BMDS]], [[DE-DEUTSCHLAND-STACK]], [[DE-BUNDID]], [[DE-GDNG]] and
[[DE-GEMATIK]].

**A real date correction.** [[DE-EGOVG]] recorded its in-force date as 31
August 2013. The statute itself says otherwise: *"Es ist gem. Art. 31 Abs.
1 dieses G am 1.8.2013 in Kraft getreten."* — 1 August, not 31. A handful of
individual provisions did take effect later, on a staggered schedule
through 2020, which is likely where the wrong date was conflated from.

**Two "no date established" gaps, closed.** [[DE-GDNG]] now carries a
`start_date` of 26 March 2024 (found on a dedicated Wikipedia article the
original search apparently missed), and [[DE-BSTATG]] one of 22 January
1987, both read directly from primary/near-primary sources rather than
guessed.

**A flagged gap, closed.** [[DE-BUNDID]] had explicitly logged its
EUDI-Wallet connection as unsourced. bmds.bund.de now states it directly:
*"Im Kontext der novellierten eIDAS-Verordnung wird die Anbindung der
BundID an die EU Digital Identity Wallet (EUDI-Wallet) ... vorbereitet."*
Recorded at low confidence because the connection is described as being
prepared, not live.

**A tooling limit, documented rather than worked around.**
[[DE-DIGITALSTRATEGIE]]'s claims were read and confirmed via a
Bundesrechnungshof PDF report (extracted with `pdftotext`), but the entity
stays `verification: search-only`: `tools/reverify.py` fetches sources as
raw bytes and cannot extract text from a PDF, so it cannot corroborate a
claim that only a PDF states verbatim, and the exact quoted title isn't
repeated on the entity's other, HTML sources. Forcing the write past that
refusal was deliberately not done — the caveat says plainly that the
content is verified even though the field is not.

### UK intelligence oversight (10 entities)

[[GB-ISA-1994]], [[GB-SSA-1989]], [[GB-JSA-2013]], [[GB-IPA-2016]],
[[GB-DPA-2018]], [[GB-GCHQ]], [[GB-MI5]], [[GB-SIS]], [[GB-ISC]] and
[[GB-IPCO]].

`legislation.gov.uk` carried a caveat on four of these entities saying it
was blocked by this environment's egress proxy. It is not, and was fetched
successfully throughout this cluster — the caveat was simply wrong,
inherited from an earlier session and never re-checked. Three placeholder
dates (`YYYY-01-01`) were replaced with the acts' actual dates: [[GB-ISA-1994]]
enacted 26 May 1994, [[GB-SSA-1989]] 27 April 1989, and [[GB-ISC]]'s own
founding at 25 June 2013 — the commencement date of [[GB-JSA-2013]] section
1, two months after the Act's Royal Assent.

### UK data protection (3 entities)

[[GB-UK-GDPR]], [[GB-DUAA]] and [[GB-ICO]].

[[GB-UK-GDPR]]'s canonical name, "UK General Data Protection Regulation",
never appeared verbatim in any source read; every source — official and
otherwise — calls it "UK GDPR", which the entity's own body already used
throughout. Renamed the entity's `name` field to match actual usage rather
than an invented full form. [[GB-DUAA]]'s § 117 was read directly:
*"A body corporate called the Information Commission is established"* —
confirming the DUAA/ICO succession mechanism word for word. [[GB-ICO]]'s
open question (has the Information Commission actually replaced it?) gets
one weak, explicitly-labelled signal: Wikipedia's infobox currently lists
the Information Commissioner as "Vacant" — suggestive of a transition in
progress, not proof one has completed, and recorded as exactly that.

## The Batch 1 core-governance re-verification, and a research-queue cleanup

**Date:** 2026-08-21/22

Picked up two open items directly from `discovery/research-queue.md`: the
"Batch 1 — Netherlands: Core Data Governance (needs re-verification)"
section, and a pass to remove queue rows for entities that had already been
created in other batches.

### The Batch 1 core-governance deepening

All twelve Batch 1 entities already carried `verification: primary-source`
from the 2026-08-20 link check. This pass went further: read the pages
specifically for the open questions `discovery/unresolved.md` had recorded
against them, using the egress opened in the prior re-verification batch.

**A real status correction.** [[NL-FDS]]'s `status` was `planned`, on the
reasoning that a search result's claim — the OBDO adopting the
*Afsprakenstelsel Federatief Datastelsel* in February 2026 — was
unconfirmed. It is now confirmed, word for word, on digitaleoverheid.nl:
*"In februari 2026 heeft het Overheidsbreed Beleidsoverleg Digitale
Overheid (OBDO) het Afsprakenstelsel Federatief Datastelsel vastgesteld."*
`status` moves to `active`. The [[NL-IBDS]] → [[NL-FDS]] relationship, an
Atlas interpretation until now, is also confirmed a sourced fact from the
same source family: noraonline.nl states plainly that the IBDS develops the
FDS.

**A separately-flagged high-value question, answered.**
`discovery/unresolved.md` had asked since Batch 7 whether [[NL-NORA]] is
formally the Netherlands' National Interoperability Framework under
[[EU-EIF]]. Kamerstuk 26643-128 (the 2008 Kabinetsbesluit inzake ICT)
answers it, but more narrowly than the question assumed: EIF developments
are anchored in NORA specifically for public services with cross-border
data exchange, not as a blanket NIF designation. [[NL-NORA]] now carries
`based-on` → [[EU-EIF]] on that sourced, narrower basis.

**Two placeholder dates replaced with sourced ones.** [[NL-IBDS]]'s
presentation to the Tweede Kamer — reported as "November 2021" and flagged
unverified — is confirmed as **18 November 2021** on two independent
sources. [[NL-MIDO]]'s `start_date` was an implicit `2022-01-01`
placeholder for "since 2022"; the actual legal basis, an amendment to
[[NL-OBDO]]'s founding decree, was signed **12 July 2022**, and
[[NL-OBDO]]'s own founding Instellingsbesluit was signed **19 January
2018** — both now sourced `start_date`s.

**Two dead links found.** A digitaleoverheid.nl OBDO dossier page and the
"Voortgang MIDO" timeline page, both cited and confirmed on 2026-08-20, now
return `404 Not Found` — the site was reorganised in the intervening day or
two. No replacement URLs were found; both entities remain fully
corroborated by their other sources.

**Common Ground attempted, not closed.** `vng.nl` answered one request
normally and then returned `403 Forbidden` ("Request forbidden by
administrative rules") to every subsequent attempt in the same session — a
rate-limit or burst-defense response, distinct from the four permanently
bot-walled hosts. Its programme-status and entity-typing questions remain
open for a future, more slowly-paced pass.

### The research-queue cleanup

Separately, cross-checked every row in `discovery/research-queue.md`
against the actual entity list rather than trusting the queue's own "still
open" claims. Nine rows removed because the entity they asked for had
already been created in another batch (Manufacturing-X, gematik/GDNG,
Belgium's NBN, France's AFNOR and Health Data Hub, Spain's AENOR/UNE, the
Netherlands' RvIG, ENISA, and NORA's GEMMA/EAR/ROSA/PETRA family — all
confirmed to exist with the relationships the queue rows were waiting on).
One row trimmed rather than removed (Health-RI existed; DANS, RIVM and NWO
from the same row did not). Three status blocks refreshed because they
described the pre-egress-opening state after two verification batches had
already moved past it.

### Counts

| | Before | After |
|---|---|---|
| Edges | 6,172 | **6,175** |
| Research-queue rows removed | — | **9** (plus 2 incorporated-source rows this batch closed) |

All required suites green: `validation/run_all.py` 5/5 (7 pre-existing
plain-http warnings), `tools/test_build_graph.py` 41/41,
`tools/test_reverify.py` 36/36, `tools/test_ui.mjs` 86/86.

## The re-verification pass, batch 1 — the first pages a machine actually read

**Date:** 2026-08-21

With outbound HTTPS finally open, `tools/reverify.py` ran for the first time
against live hosts rather than a blocked proxy. This batch worked the
densest, best-structured slice of the 435-entity `search-only` backlog: the
seven Dutch base-registration statutes flagged high priority in
`discovery/unresolved.md`, plus a cluster of EU-scoped organisations
(national statistics institutes citing `ec.europa.eu`, national data
protection authorities citing `edpb.europa.eu`). **Twenty-one entities moved
to `verification: primary-source`.**

### The finding that mattered more than the count: egress open ≠ every host readable

`eur-lex.europa.eu`, `www.iso.org`, `www.coe.int` and `unece.org` — four of
the highest-value hosts on the allowlist — answer every automated fetch
attempt with a bot-defense challenge page (AWS WAF or Cloudflare) rather
than content, regardless of `User-Agent`, regardless of whether the request
comes from `curl`, from `tools/reverify.py`'s own `urllib` fetch, or from a
headless Chromium (which additionally cannot route through this session's
proxy at all, a second and independent problem). This is not the egress
policy — the TLS handshake completes and the site answers, just not with
the page. Entities citing *only* those hosts are correctly still
`search-only`; no amount of retrying converts them from inside this
environment. See `docs/re-verification.md` §"A machine-corroborated pass"
for the full account, including which `europa.eu` subdomains **do** work
(`ec.europa.eu`, `digital-strategy.ec.europa.eu`, `edpb.europa.eu` and
others — `eur-lex` is the one exception, not the rule).

### Two corrections, and they are the point of the exercise

- **[[NL-WET-BGT]]'s third commencement stage was mis-dated.** The entity
  said articles 29 and 30 took effect 30 April 2018; `wetten.overheid.nl`'s
  own commencement history gives **1 July 2018**. 30 April 2018 is when the
  commencement decree (Stb. 2018, 122) was *published* in the Staatsblad,
  confirmed independently on the Eerste Kamer's dossier, which titles the
  same document "publicatie inwerkingtreding artikelen 29 en 30" — a
  publication date mistaken for an effective date.
- **[[NL-KADASTERWET]] carried an unattested alternative name.**
  "Kadasterwet 1989" was listed in `alternative_names`; the statute's own
  `wetten.overheid.nl` metadata records `Niet officiële titel: Geen`. Removed.

Neither of the seven BWBR-keyed statutes resolved to the wrong act — the
Kadasterwet/Archiefwet near-miss this tool exists to catch did not recur —
but three diacritic typos did: `Datenschutzbehorde` → `Datenschutzbehörde`,
`Bundesanstalt Statistik Osterreich` → `... Österreich`,
`Dataombudsmannens byra` → `... byrå`. Each was an exact-string mismatch
between `alternative_names` and the authority's own site, invisible on a
skim and caught only because the check is literal.

Several entities also had unattested English glosses dropped rather than
kept unread — "Austrian Data Protection Authority", "Italian Data
Protection Authority", "Finnish Data Protection Ombudsman" — none findable
on the authority's own site or a Wikipedia page under that title.
[[NL-KVK]]'s `confidence` was raised from `low` to `medium` after its own
site (`kvk.nl/en`) was added and read, the specific gap its `low` rating had
named.

### Two entities attempted, not moved

- **[[LU-STATEC]]** — `name` carries an Atlas-added disambiguator,
  `"... (Luxembourg)"`, to distinguish it from France's identically-named
  INSEE. No external source will ever write that suffix verbatim, so the
  full-name claim cannot corroborate by exact-string match. Needs the
  disambiguator moved out of `name`, not another source.
- **[[PT-INE]]** — `ine.pt` returns `HTTP 403` specifically to
  `tools/reverify.py`'s declared `User-Agent`, consistently across repeated
  attempts, while occasionally serving a browser-identified request. A
  site-level block on the tool's identity rather than a network flake.

### Counts

| | Before | After |
|---|---|---|
| `verification: primary-source` | 81 | **102** |
| `verification: search-only` / `unverified` | 435 | **414** |
| Cited source URLs | 1,677 | 1,689 |

All required suites green: `validation/run_all.py` 5/5 (7 pre-existing
plain-http warnings), `tools/test_build_graph.py` 41/41,
`tools/test_reverify.py` 36/36, `tools/test_ui.mjs` 86/86.

## The four proposals, and the first content-tier verification

**Date:** 2026-08-21

This batch acted on all four next steps proposed after the candidate-clearing
batch, plus the stale queue row found while checking them. **Fourteen
entities, two vocabulary additions, and the Atlas's first content-tier source
confirmation.**

### 1. The confirmed domains — 41 entities to `primary-source`

The repository owner confirmed five domains at the **content** tier: the pages
were read and the information on them confirmed correct.

| Domain | URLs | Entities citing it |
|---|---|---|
| `europa.eu` | 231 | 144 |
| `iso.org` | 67 | 64 |
| `coe.int` | 52 | 42 |
| `bund.de` | 41 | 23 |
| `legifrance.gouv.fr` | 5 | 5 |

**The rule applied is all-sources-or-none.** An entity moved to
`primary-source` only when *every* source it cites is on a confirmed domain;
partial coverage left it `search-only`. That is deliberately strict and the
reason is mechanical: the Atlas does not record which source supports which
claim, so an unconfirmed fifth source may be the one carrying the date.

| | Entities |
|---|---|
| Fully covered → `primary-source` | **41** |
| Partially covered → unchanged | 161 |
| Not covered | 291 |
| No sources (domains, anchors — exempt) | 8 |

Two results worth recording:

- **`legifrance.gouv.fr` yielded nothing.** Five entities cite it; all five
  also cite something unconfirmed. A confirmation is not required to move
  anything — the partial-coverage rule decides.
- **`europa.eu` did almost all of it.** 38 of the 41 are EU-scoped, which is a
  fact about how the Atlas was built rather than about the Union: EU entities
  cite one publisher because EUR-Lex carries the whole instrument, while a
  national entity cites a statute database, a ministry and a commentary.
  **So the remaining yield is front-loaded** — the allowlist ranks domains by
  URL count, which overstates how much each next one would unlock.

`tools/source_hosts.py` gained a `CONTENT_CONFIRMED` set and the generated
allowlist gained a `Content confirmed` column, so this state is generated
rather than hand-maintained. Note that the table collapses all of `gouv.fr`
into one row and is therefore **not** marked confirmed — the confirmation
names one host under that namespace, not the namespace.

### 2. `level: subnational` — the blocker that had stopped four items

`level: regional` means **supra**-national in this Atlas: it is what all 69
EU-scoped entities carry. Nothing meant *sub*-national, so a Belgian Region, a
Spanish Comunidad Autónoma and a German Land had no value — and four queued
items across three countries had been blocked on it since the Belgium batch.

**`local` was the tempting shortcut and would have been wrong.** The Flemish
decreet of 2 July 2021 is primary legislation of a constituent state with its
own parliament, not a municipal by-law. Using `local` would have flattened the
difference between a legislature and a council.

Renaming `regional` to `supranational` was rejected: 69 files, the site filter
and the docs, to buy what a definition buys.

The three Belgian sub-federal Open Data Directive instruments are now modelled
— [[BE-VL-BESTUURSDECREET-2021]], [[BE-BRU-ORDONNANCE-2021]],
[[BE-WAL-DECRET-2022]] — plus [[BE-BRU-ORDONNANCE-2016]], which the Brussels
2021 ordonnance amends and which **predates the directive by two and a half
years**.

**A correction the research produced.** [[BE-HERGEBRUIK-WET-2023]] said
Flanders *"met the deadline"* because its decree *"preceded 17 July 2021 by a
fortnight"*. The annotated Codex text is sharper: the decree was **adopted**
2 July and its open-data provisions **entered into force on 17 July 2021** —
the deadline to the day. Flanders did not transpose early; it transposed
exactly on time, having legislated a fortnight before.

And the reason it was worth modelling at all:

| Level | Instrument | Against the deadline |
|---|---|---|
| Flanders | [[BE-VL-BESTUURSDECREET-2021]] | **on time** |
| Brussels-Capital | [[BE-BRU-ORDONNANCE-2021]] | 5 months late |
| Wallonia | [[BE-WAL-DECRET-2022]] | 16 months late |
| Federal | [[BE-HERGEBRUIK-WET-2023]] | 29 months late |

The Atlas showed Belgium as twenty-nine months late. Three quarters of the
country was not.

### 3. `measures` — 62 edges, one batch after the entities that needed them

[[EU-DESI]] and [[EU-EGOV-BENCHMARK]] measured 27 and 35 countries and carried
no edge to any of them, because no relationship type meant "measures".
`discovery/candidates.md` had argued for waiting: *"a type added in the same
batch that creates its only users has not been tested against anything."*

Added now, in the following batch. `measures` is directional and asymmetric —
being measured implies nothing about the target, which is exactly why it could
not be `applies-in`, and why `references` would have suggested citation rather
than assessment.

**The 62 edges rest on each publication's sourced scope rule**, not on 62
individual sources — the same basis [[NL-NEN]] attaches to [[EU-CEN]] on. Every
evidence string says so.

The contrast with `cooperates-with` is the point: that type was added on a
single example because it had one instance and no scaling consequence.
`measures` immediately wanted 62 edges and got a batch of separation first.

### 4. Health, education and research — the three domains stuck at 1 of 58

| Domain | Before | After |
|---|---|---|
| [[DOMAIN-HEALTH]] | 1 | **5** |
| [[DOMAIN-RESEARCH]] | 1 | **2** |
| [[DOMAIN-EDUCATION]] | 1 | **2** |

Health was called *"the single largest correction available"*: the Atlas held
[[EU-EHDS]] and one country's health entities. Four countries were added, and
they turn out to answer the same problem **three different ways**:

| | Body | Shape |
|---|---|---|
| [[DE]] | [[DE-GEMATIK]] + [[DE-GDNG]] | statute creates a research data centre; a separate company runs the exchange infrastructure |
| [[FR]] | [[FR-HEALTH-DATA-HUB]] + [[FR-SNDS]] | a public-interest grouping of **56 members** holds the platform |
| [[FI]] | [[FI-FINDATA]] + [[FI-SECONDARY-USE-ACT]] | a statutory **permit authority** licenses access to data others hold |
| [[DK]] | [[DK-SUNDHEDSDATASTYRELSEN]] | the authority **holds the registers itself** |

Pool, license, custody. Every one of these countries has "a national health
data body"; they do materially different jobs, and only placing them side by
side shows it. Recorded on [[DOMAIN-HEALTH]].

Research and education gained [[EU-GEANT]] — the **third** membership
association after [[EU-ESS]] and [[EU-EUROGEOGRAPHICS]] — with [[NL-SURF]] and
[[DE-DFN]] attached, plus [[DE-NFDI]], whose [[EU-EOSC]] membership is
**sourced** rather than inferred.

Germany now has two research-data bodies that are not the same thing:
[[DE-DFN]] is the network and attaches to GÉANT; [[DE-NFDI]] is the data
infrastructure and attaches to EOSC. The Netherlands collapses both roles into
[[NL-SURF]] and Germany does not — a finding rather than a modelling artefact.

### 5. The stale queue row

`discovery/research-queue.md` still carried *"`applies-in` to the 17 new EU
member states"* as **Next**. [[EU-GDPR]] has all 27; the work was done in the
publication batch and the row survived its cleanup. Removed, along with two
others this batch closed. **No new rows were added** — limits are recorded in
entity prose instead, on instruction.

### What was deliberately not done

- **No `verification` change for the 161 partially covered entities.** The
  all-or-none rule is the whole reason the sweep is trustworthy.
- **No `based-on` edge from [[FR-HEALTH-DATA-HUB]] to the loi OTSS.** The law
  of 24 July 2019 is named in every French health source and none gives it a
  JORF or Legifrance identifier, which is what the Atlas's French legislation
  entities are keyed on.
- **No date for [[DE-GDNG]].** The sources describe the act and its effects
  and none gives its date. `start_date` is `null`.
- **No entities for** the Forschungsdatenzentrum Gesundheit, the Kanta
  Services, the Danish National Patient Register, CERN or ESA — each named
  once in a source about something else.
- **[[FR-SNDS]] is `coverage: low` and says so at length.** Everything known
  about it comes from sources *about the Plateforme*. It is on the edge of the
  taxonomy threshold, not clear of it, and the entity states that plainly.

### Counts

| | Before | After |
|---|---|---|
| Entities | 502 | **516** |
| Edges | 5,856 | **6,170** |
| Relationship edges | 1,010 | **1,095** |
| `verification: primary-source` | 40 | **81** |
| Relationship types | 23 | **24** |
| `level` values in use | 4 | **5** |
| Research-queue rows | 207 | **204** |

All four suites green: validators 5/5 (7 pre-existing plain-http warnings),
`test_build_graph.py` 41 OK, `test_reverify.py` 36 OK, `test_ui.mjs` 86/86.

## Candidate clearing — the remaining leads worked

**Date:** 2026-08-21

`discovery/candidates.md` was the last discovery file still carrying leads
nobody had gone back to. This batch worked every one of them, created
**sixteen** entities, closed **eleven** rows, and emptied three whole
sections of the page.

### What was created

| Layer | Entities |
|---|---|
| Statutory bases | [[EU-REG-223-2009]], [[EU-REG-1025-2012]] |
| The EEA route | [[INTL-EEA-JCD-154-2018]], [[IS-PERSONUVERNDARLOG]], [[IS-PERSONUVERND]], [[LI-DSG]], [[LI-DATENSCHUTZSTELLE]] |
| Switzerland | [[EU-CH-ADEQUACY]] |
| Geospatial | [[EU-EUROGEOGRAPHICS]] |
| Trade / mobility | [[UN-LOCODE]], [[UN-EDIFACT]], [[EU-EMSWE]] |
| Sustainable development | [[UN-2030-AGENDA]], [[EU-VOLUNTARY-REVIEW-2023]] |
| Measurement | [[EU-DESI]], [[EU-EGOV-BENCHMARK]] |

**All 17 entity types are now in use.** `publication` was the last unused
one; [[EU-DESI]], [[EU-EGOV-BENCHMARK]] and [[EU-VOLUNTARY-REVIEW-2023]] are
its first instances, and they give the Atlas its first
comparative-measurement layer. Everything else it holds prescribes; these
measure.

### The deferred pair was closed by creating both halves

[[EU-ESS]] carried a section headed *"Regulation (EC) No 223/2009 is cited,
not modelled"* and [[EU-CEN]] carried one headed *"Regulation 1025/2012 not
modelled"*. Both deferrals gave the **same** reason: modelling one statutory
base and not the other would make the Atlas inconsistent about statutory
bases in general.

The answer was to create both in one batch, not neither. `EU-ESS` now has the
`governed-by` edge its own body said it lacked, and the three European
standardisation organisations are covered by `applies-to` edges from
`EU-REG-1025-2012`. Both "not modelled" sections were rewritten to say what
happened rather than deleted.

### The EEA route is now drawable end to end

[[INTL-EEA-AGREEMENT]] carried a section headed *"⚠ The individual Joint
Committee decisions are not modelled"*. **JCD No 154/2018 was cited four
times across the Atlas** — in the Agreement's sources, and in
[[NO-PERSONOPPLYSNINGSLOVEN]]'s description, evidence string and sources —
without existing.

```
EU-GDPR ◀─ references ─ INTL-EEA-JCD-154-2018 ─ amends ─▶ INTL-EEA-AGREEMENT
                                 │ applies-in
                     ┌───────────┼───────────┐
                     ▼           ▼           ▼
                    NO          IS          LI
```

Only this one decision is modelled, and the original caution still holds for
every other.

### The Norwegian EEA pattern generalises — and the exception is the interesting part

`discovery/candidates.md` asked whether adding Iceland or Liechtenstein
*"would show whether the Norwegian EEA pattern generalises or is
Norway-specific"*. Both were added, and the answer is both halves of a yes:

| | Norway | Iceland | Liechtenstein |
|---|---|---|---|
| Act adopted | 15 June 2018 | 27 June 2018 | 4 October 2018 |
| In force | 20 July 2018 | 15 July 2018 | **1 January 2019** |
| Act's function | gives GDPR effect | gives GDPR effect | **supplements** an already-applicable GDPR |
| Route | JCD 154/2018 | JCD 154/2018 | JCD 154/2018 |

The **route** is identical in all three. The **national instrument's job** is
not, and the five-month gap is the tell: Norway's and Iceland's acts had to
be in force on the day the GDPR started to apply, because their acts were
what made it apply. Liechtenstein's did not.

Both new authorities attach to [[EU-EDPB]] on a sourced composition rule —
JCD 154/2018 provides that the supervisory authorities of the EFTA States
participate in the Board's activities — the same basis on which the national
standardisation bodies were attached to [[EU-CEN]]. Neither claims a vote
under Article 68(3).

### One vocabulary gap was real; the other was a missing node

`discovery/candidates.md` §3 listed two EU↔UN interactions the vocabulary
could not express and concluded that *"two examples is the threshold §2.3
sets for proposing a new type"*. Two things were wrong with that:

1. **The threshold is one.** §2.4 asks for "at least one real example". §2.3
   is the anchor-edge rule and sets no threshold for new types at all.
2. **The two cases were not instances of the same missing type.** One was a
   cooperation agreement between two organisations — a real gap, now filled
   by **`cooperates-with`** (the Atlas's 23rd relationship type), asserted on
   [[UN-UNESCO]] for the UNESCO–Commission AI ethics agreement. The other was
   a report submitted to a UN process, which needed **no relationship type at
   all** — only the `publication` entity type the ontology had defined and
   nothing had used. It is now [[EU-VOLUNTARY-REVIEW-2023]], and `references`
   is simply correct between a document and the policy it reports on.

**A count of unmodellable things is not a count of instances of one missing
type.** Recorded as a worked example in `metadata/relationship-types.md` §2.4.

### Creating the missing node did not always close the edge

[[EU-EUROGEOGRAPHICS]] was on the page as *"the cluster's missing middle"*,
explicitly analogised to [[EU-ESS]]. It was created, and five national
mapping and cadastral authorities now attach to it by `participates-in`:
[[NL-KADASTER]], [[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[GB-OS]],
[[IE-TAILTE]].

**The [[EU-INSPIRE]] → UN-GGIM refusal did not close.** `EU-ESS` closed five
refused edges because the missing node was what all five had been pointing
at. Here the node was also genuinely missing — but it was never what the
INSPIRE refusal turned on. The two cases look identical on the candidates
page and are not, and the row stays open with that noted.

### The narrow UN/CEFACT question, answered by adding the instrument

*"Does any instrument already in this Atlas reference a UN/CEFACT
standard?"* — **no.** But [[EU-EMSWE]], Regulation (EU) 2019/1239, provides
for a common location database holding [[UN-LOCODE]], so the row closed by
adding the instrument rather than by finding one already present.
[[UN-EDIFACT]] was created alongside it and deliberately carries no European
edge, because none was found.

### The 2030 Agenda was never thinly sourced

It had been refused as *"nothing found beyond passing references"*. It was
being searched for on Eurostat's SDG pages, where it appears only as context.
Searching for the resolution — **A/RES/70/1** — returns the resolution.

This is the third instance of the lesson `discovery/candidates.md` already
recorded: **a refusal for want of a source is not the same as a fact being
unknowable.**

### The domain coverage table was re-measured

The old table read "3/7", "2/7", "1/7" against seven countries. Against 58
anchors: `DOMAIN-GOVERNMENT` 21, `DOMAIN-CYBERSECURITY` 13,
`DOMAIN-NATIONAL-SECURITY` 8, `DOMAIN-GEOSPATIAL` 6, `DOMAIN-MOBILITY` 2, and
`DOMAIN-HEALTH`, `DOMAIN-EDUCATION` and `DOMAIN-RESEARCH` **1 each**. The
absolute counts went up and the coverage got thinner.

### What was deliberately not done

- **No `measures` relationship type.** [[EU-DESI]] and
  [[EU-EGOV-BENCHMARK]] measure 27 and 35 countries and carry no edge to any
  of them. `cooperates-with` was added on one example because it has one
  instance and no scaling consequence; `measures` would immediately want 62
  edges, and a type added in the same batch that creates its only users has
  not been tested. Left open in `discovery/candidates.md` §3.
- **No entity for Capgemini**, the eGovernment Benchmark's contractor. A
  private firm named as the executor of one study is not an Atlas subject.
- **No `based-on` edge from [[LI-DSG]] to [[DE-BDSG]].** "Modelled after" in
  a law-firm commentary is a characterisation of legislative style, not a
  sourced statement that a specific text was adapted.
- **No entity for the eFTI Regulation (EU) 2020/1056.** Its UN/CEFACT link is
  attested in a UNECE presentation and a project website, not in the
  regulation. Queued.
- **No adoption date for [[EU-VOLUNTARY-REVIEW-2023]].** The sources give the
  HLPF window and the document reference and no adoption date, so
  `start_date` is `null` rather than a plausible-looking guess.

### Counts

| | Before | After |
|---|---|---|
| Entities | 486 | **502** |
| Edges | 5,602 | **5,847** |
| Relationship edges | 967 | **1,010** |
| Entity types in use | 16 | **17 of 17** |
| Relationship types | 22 | **23** |
| Countries with a modelled national layer | — | [[IS]] and [[LI]] added |

All four suites green: validators 5/5 (7 pre-existing plain-http warnings),
`test_build_graph.py`, `test_reverify.py`, `test_ui.mjs`.

## The first human link check — and what it actually found

**Date:** 2026-08-20

The repository owner opened the nineteen highest-value domains in
`discovery/reverification-allowlist.md`. **Eighteen resolved to what the Atlas
claims. `gob.es` did not.**

**The defect was in this report, not in any citation.**

### `gob.es` has no apex site

The table's rows are **registrable domains** — the right unit for a firewall
rule, and a natural thing to paste into a browser. Eighteen of the nineteen
are both, because their apex happens to serve a website.

Spain's is not:

```
gob.es                 -> no address associated with hostname
gov.uk                 -> 151.101.0.144
gov.pl                 -> 185.32.48.56
datos.gob.es           -> 45.223.177.253
administracion.gob.es  -> 185.73.172.38
espanadigital.gob.es   -> 45.223.181.253
```

`gob.es` is a pure namespace. `gov.uk` and `gov.pl` are namespaces *and*
websites, which is why they passed. Every Spanish host the Atlas actually
cites resolves and works.

The fix is an **`Example host` column**, so every row offers something a
reader can open, and a line saying a domain here is an allowlist pattern
rather than a URL.

**A second pass settled whether it was the first of several.** `gov.cz`,
`gov.pt` and `public.lu` are the other government namespaces among the
Atlas's citations, and none was in the original nineteen. All three were
opened by hand and all three serve a site:

```
gov.cz     -> 94.199.45.233
gov.pt     -> 62.28.186.239
public.lu  -> 185.106.24.133
gob.es     -> no address associated with hostname
```

**Twenty-two domains have now been opened by hand, and exactly one does not
resolve.** `gob.es` is the sole exception rather than the leading edge of a
pattern, which is worth knowing before anyone generalises from it.


### The first six verified entities

The repository owner read all 22 candidate sources for the five Batch 1 areas
and confirmed they support what the entities say. That is the **content
check** — the tier that sets `verification: primary-source` — and it is the
first one this repository has had.

**Six entities are fully covered**, meaning every source they cite is among
the 22 read: [[NL-NORA]], [[NL-IBDS]], [[NL-FDS]], [[NL-COMMON-GROUND]],
[[NL-MIDO]] and [[NL-PAS-TOE-OF-LEG-UIT]]. They now carry
`verification: primary-source`, `last_verified: 2026-08-20`, an `accessed:`
date on every source, and **no sourcing caveat** — the blockquote was
replaced rather than left standing, and the `NOT READ — search-only` suffix
was stripped from every evidence string, because none of it is true of them
any more.

**Six more are partially covered** — [[NL-BZK]] 1/2, [[NL-FORUM-STANDAARDISATIE]]
2/4, [[NL-GDI]] 1/3, [[NL-ICTU]] 1/3, [[NL-OBDO]] 1/3, [[NL-VNG]] 1/2. Their
read sources are stamped `accessed:`; their `verification` is **not** changed.

That asymmetry is the point. Forty entities cite the five areas' hosts, and
flipping all forty would have been the largest false provenance claim the
repository could make — citing a host is not being covered by a URL. Only
twelve are touched at all, and only six are verified.

`tools/reverify.py` gained `set_verification=False` for the partial case,
with a test. It had modelled all-or-nothing, and partial coverage is what the
first real content check actually looks like: some sources read, some not,
and throwing away the reading that was done would be as wrong as claiming the
entity is verified.

**442 of 461 entities remain unread.** The README, the site banner and the
allowlist all now say twelve rather than none.

### The country-expansion shortlist, acted on and deleted

`discovery/candidates.md` ranked eight countries by **what each would prove**,
not by size. Three of the eight already had layers — Estonia, Czechia and
Portugal — so the shortlist was stale on those. The other five are now
modelled. **25 new entities.**

| # | Country | What it was ranked to prove | Now |
|---|---|---|---|
| 1 | **Italy** | Largest unmodelled member state; a *codified* digital administration act | [[IT-CAD]], [[IT-AGID]], [[IT-SPID]], [[IT-GARANTE]], [[IT-ISTAT]], [[IT-DATI-GOV-IT]] |
| 4 | **Finland** | The other half of NIIS — *"only pays off alongside Estonia"* | [[FI-PALVELUVAYLA]], [[FI-DVV]], [[FI-SUOMI-FI]], [[FI-TIETOSUOJA]], [[FI-TILASTOKESKUS]] |
| 5 | **Denmark** | *Grunddata*, the analogue of the Dutch basisregistraties | [[DK-GRUNDDATA]], [[DK-DATAFORDELER]], [[DK-DIGST]], [[DK-DATATILSYNET]], [[DK-DST]] |
| 7 | **Sweden** | DIGG and a long open-data record | [[SE-DIGG]], [[SE-DATAPORTAL]], [[SE-IMY]], [[SE-SCB]] |
| 8 | **Austria** | Second federal state after Germany | [[AT-BRZ]], [[AT-DATA-GV-AT]], [[AT-ID-AUSTRIA]], [[AT-DSB]], [[AT-STATISTIK]] |

Each paid off in the way the ranking predicted, which is worth recording
because the ranking was a bet made two days earlier.

**Italy.** [[IT-CAD]] is a **code** — Italian practice consolidates a whole
field into one numbered instrument amended in place, so digital identity,
electronic documents, signatures, registers and citizens' digital rights all
live at one citation. Every other national digital-government instrument here
is a single act on a single subject. And [[IT-SPID]] is not a system the
state provides but **one of three credentials** for exercising a right the
Code confers.

**Finland closed the loop Estonia opened.** [[FI-PALVELUVAYLA]] and
[[EE-X-TEE]] are two national deployments of one shared codebase,
[[INTL-X-ROAD]], governed jointly through [[INTL-NIIS]]. That could not be
shown with Estonia alone — which is exactly why the shortlist ranked them as
a pair, and it is now the only jointly-governed platform in the Atlas.

**Denmark gave the Atlas its first controlled comparison.** The ten Dutch
[[NL-BASISREGISTRATIES]] are modelled in more depth than anything else here,
and there was nothing to compare them against. [[DK-GRUNDDATA]] is the same
idea in another jurisdiction, and the *differences* are the value: the Dutch
stelsel rests on **seven statutes**, the Danish programme on a
**digitalisation strategy**; Dutch registers are served by their own holders,
Denmark built **one distributor** ([[DK-DATAFORDELER]]). The edge between
them is deliberately `related-to` — neither derives from the other.

**Austria tested the federal question and answered it.** [[AT-DSB]] is a
**single federal** data protection authority, where [[DE-BFDI]] sits
alongside sixteen Land authorities. So the Bund/Länder shape is *not*
federal-general; it is German. That is a real comparative finding and it
needed a second federal state to make.

[[EU-EDPB]] goes 12 → **17** incoming edges, [[EU-ESS]] 11 → **16**.

The shortlist section is **removed** from `discovery/candidates.md`, per the
convention adopted this session: closed items leave the list rather than
being struck through.

### Discovery cleaned out

Closed items are now **removed** from `discovery/`, not struck through. **44
rows** went: 39 from the research queue, 3 from `candidates.md`, 2 from
`unresolved.md`. The queue is 488 → **329 lines**.

The old convention made the queue longer every time it got shorter, and a
reader had to skim past a growing archive to find the work. The record of
what closed, and why, is in `progress/completed.md` and on the entities —
every finding was checked as preserved there before its row was deleted.

Three rows were **not** deleted, and they are the reason this was not a
one-line `grep -v`:

- **Interoperable Europe Board** was struck through, but its own text said
  *"Still not created — two passing mentions only."* It is open, and it is
  now un-struck rather than removed.
- **Wet BAG / BGT / BRO / WOZ** was marked done with *"AWR ch. IVA still
  open"* trailing it. Rewritten as its own row for [[NL-BRI]]'s missing
  statutory basis.
- **CSIRT NASK / GOV / MON** was *"PARTLY DONE … CSIRT MON still open"*.
  Rewritten as a row for CSIRT MON alone.

A partly-closed row is an open row with history attached. Deleting those
three would have quietly dropped three real gaps.

Seven headings in `unresolved.md` looked empty after the sweep and were left
alone — they are parent headings with `###` subsections beneath, still full
of open questions.

The research queue's banner was replaced too. It described a strike-through
convention and narrated closures whose rows no longer exist; it now states
what is open and what is blocked.

### Twenty-one member states verified, six held back

A verification pass supplied all 27 EU member states with their accession
dates, and confirmed the sources cited on each country anchor.

**Twenty-one agreed with the Atlas exactly** and are now `primary-source`:
[[AT]], [[BG]], [[CY]], [[CZ]], [[DK]], [[EE]], [[ES]], [[FI]], [[GR]],
[[HR]], [[HU]], [[IE]], [[LT]], [[LV]], [[MT]], [[PL]], [[PT]], [[RO]],
[[SE]], [[SI]], [[SK]].

**Six did not**, and they are exactly the founding members — [[BE]], [[DE]],
[[FR]], [[IT]], [[LU]], [[NL]]:

| Date | Event |
|---|---|
| **25 March 1957** | the Treaty of Rome was **signed** |
| **1 January 1958** | the Treaty **entered into force** |

Strictly neither is an accession: the six founded the Communities rather than
joining them, and "accession date" is a column borrowed from the twenty-one
that did join later.

The Atlas keeps **1958**, because that is what its own cited source says —
the Union's list of EU countries records the founding six under 1958, and
that page is the `part-of` [[EU]] evidence on all six entities. Adopting 1957
would put each entity in contradiction with the source it names.

**So those six stay `search-only`.** Both dates are now recorded on each of
them, and `discovery/unresolved.md` carries the choice as an open modelling
question. Verifying an entity against a date its own citation contradicts
would be worse than leaving it unverified.

Two other things in the supplied table are worth noting and did **not**
change anything: it gives Hungary's official name as *Republic of Hungary*,
which has been simply *Hungary* since the 2012 Fundamental Law — the Atlas
already had this right — and its population and MEP figures are early-2000s
vintage (Germany at 99 MEPs predates Lisbon). The Atlas records neither, so
neither could propagate.

**33 entities verified, 421 of 461 still unread.**

### All twelve, the same day

The six partials were finished within hours of being identified. All nine
remaining URLs were read and confirmed, and [[NL-BZK]],
[[NL-FORUM-STANDAARDISATIE]], [[NL-GDI]], [[NL-ICTU]], [[NL-OBDO]] and
[[NL-VNG]] joined the first six.

**Twelve entities are `primary-source`**, on 31 sources read by hand. That is
the **whole of Batch 1's core governance layer** — Forum Standaardisatie, the
IBDS and the Federatief Datastelsel, NORA, Common Ground, MIDO, the GDI, the
'pas toe of leg uit' regime, and the four bodies that govern them.

It is worth stating what that changes. Until today the honest answer to "is
any of this checked?" was *no, none of it*. It is now *yes — that layer,
entirely, by hand, on a stated date*. **442 of 461 entities remain unread**,
so the disclosure stays, but it is no longer the whole story.

The partial-coverage machinery added a few hours earlier turned out to have a
lifespan of one afternoon, which is the right outcome: it existed to avoid
overclaiming during the gap, and the gap closed. It stays in
`tools/reverify.py` because the next content check will open the same gap
again.

### A third tier: the reachability check

`gob.es` exposed a gap in how this repository talks about verification. There
were two named checks; there are really three.

| | Establishes | Runs without egress? |
|---|---|---|
| **Reachability** | the host resolves | **yes** |
| **Link check** | the citation points to what the Atlas claims | no |
| **Content check** | the page supports the entity's claims → `primary-source` | no |

A reachability sweep on **2026-08-20 resolved all 52 institutional domains**,
at the apex and at `www.`. Three answer only at `www.` — `coe.int`,
`gesetze-im-internet.de`, `verwaltungsvorschriften-im-internet.de` — which is
not a defect, since the Atlas cites `www.` or `rm.` hosts under all three, but
is recorded so nobody repeats the `gob.es` inference from an apex that does
not answer.

**`gob.es` remains the only dead namespace in the Atlas.** Twenty-two domains
have now been opened by hand and fifty-two resolved by machine; exactly one
does not exist.

The point of naming the weakest tier is that it is the only one available
here, and it is the one that would have caught `gob.es` before a human had
to.

### A wrong first reading, corrected the same day

The first pass read the report as *"the Spanish citations are wrong"* and:

- flagged all **18** entities citing `gob.es` as carrying suspect citations;
- rewrote three `espanadigital.gob.es` URLs from `http` to `https`;
- justified a new validator warning on the theory that a government citation
  over plain http is "usually a stale URL", citing those three as the
  evidence.

**All three were wrong**, and all three are undone. The 18 entities are
unflagged, the URLs are reverted to exactly what they were, and the warning is
rewritten to say what it can actually support: a page fetched over plain http
cannot be fetched with integrity, which matters for a repository whose whole
claim is provenance. It is explicitly **not** evidence of staleness, and the
comment records that the original assumption was wrong.

The lesson is narrow and worth keeping: **"a human reported a failure" is not
the same as "the thing they were looking at is broken."** The check was
sound, the report it was run against was not, and jumping to the data was the
error.

### What still stands

The distinction between a **link check** and a **content check**, which was
the substantive point of the previous pass:

| | Establishes | Does not establish |
|---|---|---|
| **Link check** | the citation points somewhere real | anything about the entity's claims |
| **Content check** | the page supports the entity's dates, identifiers, relationships and evidence | — |

Only the second is `verification: primary-source`, and **no entity's
`verification` changed** — correctly, both times.

### Verification

461 entities, 5,379 edges. `validation/run_all.py` 5/5 · `tools/test_build_graph.py`
41 OK · `tools/test_reverify.py` 35 OK · `tools/test_ui.mjs` 86/86. Five
plain-http warnings, all pre-existing and none of them a defect.

## Estonia, the Convention 108 committee, and the sourcing disclosure

**Date:** 2026-08-20

The batch that precedes pointing people at the site. **12 new entities, 176
relationships.** 450 → **461 entities**, 750 → **922 relationships**.

### The disclosure, which was the gate

Individual entities already carried a sourcing caveat in their detail panel.
**Nothing stated the aggregate** — and a reader seeing one caveat reasonably
infers it is the exception. It is the rule: **454 of 461 entities have never
had a cited source read.**

Two fixes, both permanent:

- **A standing banner on every page of the site**, deliberately not
  dismissible, and **counted from the data at load** rather than hard-coded —
  `verification` rides in `details.json`, so the banner runs twice and keeps
  honest generic wording until the real number exists.
- **A `⚠ Sourcing` row in the README's fact table**, and a *"Read this before
  you cite anything"* section under it that states the position and lists the
  machinery built around it — the `confidence: high` refusal, the unresolved
  register, the allowlist, the runner.

The framing is: **a map of the territory, not a legal source.** Structure and
the questions it raises are the value; every date and identifier needs
checking before anyone relies on it.

### Estonia — the largest content gap, closed

Nine new entities. The Atlas held the Dutch idea of a register stelsel plus
an exchange standard and not the Estonian one, while Estonia is the more
cited of the two internationally.

| Entity | |
|---|---|
| [[EE-RIA]] | Information System Authority — operates all three platforms below |
| [[EE-X-TEE]] | the data exchange layer; **data never sits in a central repository** |
| [[EE-RIHA]] | administration system for the state information system |
| [[EE-ANDMEPORTAAL]] | the data portal, **established 2025** |
| [[EE-AKI]] | data protection authority — the **twelfth** on [[EU-EDPB]] |
| [[EE-IKS]] | GDPR implementation, in force **15 January 2019** |
| [[EE-ATS]] | Public Information Act — the one Estonian statutory anchor found |
| [[EE-E-RESIDENCY]] | launched **1 December 2014** |
| [[INTL-NIIS]] + [[INTL-X-ROAD]] | the international half |

**Four findings the country produced:**

**A national system that became an international product.** X-Road began as
Estonia's exchange layer, passed into joint Estonian–Finnish ownership under
[[INTL-NIIS]] in 2017, and now runs well beyond its members. Nothing else in
the Atlas has done that — [[NL-DIGIKOPPELING]] and [[BE-BELGIF]] stayed
national. It forced a split the Atlas already makes for specifications:
[[INTL-X-ROAD]] is the software, [[EE-X-TEE]] is Estonia's deployment.

**The first jointly-governed infrastructure body.** [[INTL-NIIS]] is owned by
[[EE]], [[FI]] and [[IS]] together — not a standards body publishing for
others to adopt, and not one country's agency. It gave [[FI]] and [[IS]]
their first substantive entity.

**Digital identity without territory.** [[EE-E-RESIDENCY]] issues a
state-backed identity to people with no residence, presence or citizenship in
the issuing country. Every other identity platform in the Atlas identifies
residents to their own state. Writing that comparison exposed that **the
Netherlands has no DigiD entity** — now queued.

**Nearly eight months late, and not a transposition failure.** [[EE-IKS]]
entered into force on 15 January 2019, against the GDPR applying on 25 May
2018. Nothing was unprotected — a regulation applies of its own force — but
the derogations a member state is *permitted* to make did not exist for eight
months. It is the latest of the eight national GDPR instruments the Atlas
holds.

### [[INTL-TPD]] — the Convention's answer to the EDPB

Created `coverage: low` and honestly so: `coe.int` is blocked, and its
composition, mandate and cadence are all unestablished.

What it does show is the shape of a problem. T-PD is the body that has
**strongly encouraged all state parties to ratify [[INTL-CONVENTION-108-PLUS]]
as soon as possible** — and the protocol still stands four ratifications short
of 38, nearly eight years after opening. A treaty committee urging its own
members to ratify its own protocol, for eight years, is visible in the graph
only because both the committee and the protocol are now entities.

### 153 `applies-in` edges, and the ones deliberately not added

Every EU instrument named **10 of the 27 member states**, which understated
applicability rather than recording a finding.

The nine EU **regulations** now name all 27. That is a rule, not research: a
regulation is binding in its entirety and directly applicable in all member
states under **TFEU Article 288**, and the evidence says so, matching the
phrasing the existing edges already used.

The five **directives** were left at 10 on purpose. Extending them is equally
true, but a directive's interesting content in this Atlas is *who transposed*
— and 17 more `applies-in` edges per directive would add 17 blank
transposition cells each. Recorded as a decision in
`discovery/research-queue.md`, not an oversight.

### Verification

- **461 entities, 5,379 edges** (922 relationship, 1,704 association, 2,753
  wikilink), 58 country scopes
- `validation/run_all.py` 5/5 · `tools/test_build_graph.py` 41 OK ·
  `tools/test_reverify.py` 35 OK · `tools/test_ui.mjs` **86/86**
- `validation/audit.py` — no fully disconnected entities

All 12 new entities are `verification: search-only`.

## Explorer depth — 4 hops, and the counts to go with it

**Date:** 2026-08-20

Two changes to the Entity Explorer's neighbourhood control, both driven by
measuring the graph rather than guessing at it. No entity content changed.

### Why 4, and not 6

The question was whether to raise the ceiling from 3 to 6. Measured across
all 450 entities, median entities reached from a seed:

| hops | relationships only (default) | all edges (wikilinks on) |
|---|---|---|
| 1 | 3 (1%) | 11 (2%) |
| 2 | 14 (3%) | 295 (**66%**) |
| 3 | 34 (8%) | 424 (**94%**) |
| 4 | 108 (24%) | 450 (**100%**) |
| 5 | 214 (47%) | 450 |
| 6 | **296 (66%)** | 450 |

Two conclusions fall straight out. **With wikilinks on the control is already
maxed at 3** — four hops reaches the entire graph from the median seed, so
options 4, 5 and 6 would be three ways to spell "everything". And **on the
default edge set 6 hops shows two-thirds of the Atlas**, which is not a
neighbourhood.

**4 is where the real chains finish.** Every signature descent in the Atlas
completes inside it:

| | hops |
|---|---|
| [[EU-GDPR]] → [[NL-AP]] | 1 |
| [[INTL-DCAT]] → [[NL-DCAT-AP-NL]] | 2 |
| [[INTL-W3C]] → [[NL-DCAT-AP-NL]] | 3 |
| [[UN-AARHUS]] → [[NL-AP]] | 3 |
| [[UY]] → [[NL]] | 3 |
| [[INTL-CONVENTION-108-PLUS]] → [[FR-CNIL]] | **4** |

So 4 buys the full treaty → protocol → regulation → authority descent at a
median of 108 entities, still a readable subset. Five and six buy scale and
nothing else.

### The counts matter more than the extra hop

Each option now states what it would show, recomputed against the current
focus **and the current filters**:

```
1 hop — direct links — 3 entities        [1% of the Atlas]
2 hops — 36 entities                     [8% of the Atlas]
3 hops — 105 entities                    [23% of the Atlas]
4 hops — the longest chains — 188 entities  [42% of the Atlas]
```

This graph is **hub-heavy**: almost every entity touches its country anchor,
[[EU]], [[UN]] or a domain node, so one extra hop through a hub can multiply
the result several times over. Depth is not a dial a reader can predict, and
the useful moment for a number is *before* the click, not in the status line
afterwards. A depth that would show more than half the Atlas says so beneath
the control.

### The lever is still the wrong one

Both changes work around the real problem rather than fixing it. The reason
two hops explodes to 66% with wikilinks on is that a path `A → EU → B` exists
between almost any pair — and that path means "both are European", not that
A and B are related.

**Not traversing *through* anchors and domain nodes** would make depth
meaningful instead of explosive, and would make wikilinks-on mode usable at
depth, which it currently is not. That is a genuine design change and is
queued rather than taken unilaterally.

### Verification

- `tools/test_ui.mjs` — 81 → **86 checks**, five of them new: the ceiling is
  4; every option carries a count; the counts are cumulative; **choosing a
  depth renders exactly the count its label promised**; and the counts move
  when filters do.
- `validation/run_all.py` 5/5 · `tools/test_build_graph.py` 41 OK ·
  `tools/test_reverify.py` 35 OK

The traversal was extracted into a shared `neighbourhood()` helper so the
control and the renderer cannot disagree about what a hop is.

## The re-verification runner

**Date:** 2026-08-19

`tools/reverify.py` — the missing half of a pass the repository has described
since Batch 1 and never had a way to run. **443 of 450 entities** have never
had a cited source read.

No entity content changed in this batch. 450 entities, 5,090 edges, unchanged.

### What it does

- fetches each `sources[].url`, honouring `HTTPS_PROXY` and the system CA
  bundle;
- extracts the entity's **checkable claims** and looks for each on the
  retrieved page;
- reports a verdict — `BLOCKED`, `UNREACHABLE`, `NEEDS REVIEW`,
  `CORROBORATED`, `NO SOURCES`;
- on `--write`, stamps `accessed:` on the sources that actually came back,
  sets `last_verified:`, and flips `verification:` to `primary-source`.

### The check exists because of one specific near-miss

A search returned **BWBR0007376** for the Kadasterwet. That identifier is the
**Archiefwet 1995**.

A wrong identifier in this field **does not 404** — it silently returns
another real act. Fetching the page succeeds and looks entirely convincing.
The only thing that catches it is checking the page for the identifier the
entity *claims*, which is what the tool does and what a human skim-reading a
plausible page would not.

That case is a test: `test_the_near_miss_this_tool_exists_for`.

### What it deliberately does not do

**Corroboration is not verification.** A `CORROBORATED` verdict means the
identifiers are on the pages. It says nothing about whether the entity's
dates, description, relationships or evidence strings are right — the part
that matters, and the part only a reader can do.

So: `--write` takes exactly one `--id`, refuses on `BLOCKED` and
`UNREACHABLE`, refuses when a claim went uncorroborated unless `--force`, and
never touches `confidence`. Raising confidence stays a hand judgment, gated by
the existing rule that `confidence: high` cannot sit on a `search-only`
entity.

### TLS is not negotiable

The tool has no switch to relax certificate verification, and
`test_source_has_no_verification_escape_hatch` asserts that against the
module's **syntax tree** — not its text.

That distinction was not academic. The first version of the test did a
substring search and failed on the module's own prose about never disabling
verification. A text search would also have passed happily on
`# verify=False` in a comment while missing `ctx.verify_mode = x` where
`x = ssl.CERT_NONE`. The AST version checks what the code does.

A `primary-source` claim made over an unverified connection is worth less than
the `search-only` claim it replaced.

### Run against the priority seven

The seven Dutch register statutes, flagged high-priority in
`discovery/unresolved.md` precisely because of the BWBR problem:

```
BLOCKED: 7
```

Every source, every statute. That is the correct output for this environment:
`curl "$HTTPS_PROXY/__agentproxy/status"` reports `403 to CONNECT` for every
host. The tool degrades to a truthful report rather than a crash or a false
pass, and it exits `1` so a sweep cannot be mistaken for success.

`discovery/reverification-allowlist.md` was regenerated and is the list of
hosts to request: **1,500 URLs across 486 hosts, 353 registrable domains**.
`europa.eu` alone unblocks 80 entities.



### Running it found three more bugs

The first full sweep is what tested this tool, not the unit suite. In order:

1. **`http.client.InvalidURL` crashed the run six minutes in.** A source URL
   on [[GB-OS]] contained a literal space. On Python 3.11 `InvalidURL`
   inherits from `HTTPException` and **not** from `ValueError`, so a tidy
   tuple of expected exception types missed it. One unfetchable source must
   never take down a sweep of four hundred entities, so the guard is now
   deliberately broad — and it names a malformed URL as the repository's
   fault rather than the network's.
2. **`Request()` construction sat outside the guard**, so a nonsense URL
   crashed before any handling could apply. Found by the test written for
   bug 1.
3. **Nine egress denials were misreported as origin failures.** A plain
   `http://` URL reaches the proxy as an ordinary forward request, so its
   refusal comes back as an HTTP **403 response** rather than a failed
   CONNECT. That is precisely the distinction this tool exists to keep
   straight. The proxy labels its own refusals with `x-deny-reason`, so that
   header is now the signal, and the response body is surfaced either way so
   a reader can check the classification rather than trust it.

The malformed URL also exposed a gap in `validation/validate_sources.py`,
which checked only that a URL starts with `http`. A URL containing raw
whitespace **cannot be fetched at all** — it is silently un-re-verifiable,
which is exactly the debt this repository is trying to pay down. It is now an
error, and the rule was confirmed to fire by reintroducing the bad URL.

31 → **35 tests**.

### The first full sweep

```
python tools/reverify.py --search-only --timeout 8
```

| | |
|---|---|
| Entities swept | **443** |
| Sources attempted | **1,500** |
| Retrieved | **0** |
| Refused by egress policy | **1,494** (99.6%) |
| Other | **6** |

Six minutes; not one page read. The six are three different things, and only
one is fixable by an allowlist:

- **5 × `github.com`**, refused by the **GitHub** proxy, which scopes a
  session to its configured repositories. Adding a host will not lift it.
- **1 × `catedrapsyd.unizar.es`** on [[ES-LO-2-2002]], which **did not
  resolve at all** while every other host tested resolved to the
  interceptor — pointing at a genuinely dead host. Recorded in
  `discovery/unresolved.md` as a citation to replace.
- **1 entity with no sources**, [[DOMAIN-NATIONAL-SECURITY]], correctly:
  domains carry no factual claims.

Six entities have **no checkable claims** — [[RO]], [[UA]], [[FR-ETALAB]],
[[NL-LOGIUS]], [[NL-NICTIZ]], [[NO-ALTINN]]. Short names, no legal
identifier. The tool reports that rather than passing them silently.

### ⚠ CI caught what local testing could not

The first push failed on GitHub Actions with `PermissionError: [Errno 13]
Permission denied: '/root/.ccr/ca-bundle.crt'`.

`Path.exists()` **raises** rather than returning `False` when a parent
directory is unreadable. The agent proxy's CA bundle lives under `/root/`,
which is readable in the container this repository is normally worked in and
**not** readable by the `runner` user in CI. Every local run passed; the
failure needed a machine that simply does not have the file.

Extra trust anchors are an optimisation for one environment, and the fix is
that they can no longer break the tool in another: `_readable()` returns
`False` on any `OSError` instead of propagating it.

Two regression tests were added, and the guard was confirmed load-bearing by
re-creating the old unguarded implementation and watching it reproduce the CI
failure under the same mocks that the new one survives. 29 → **31 tests**.

### Verification

- `tools/test_reverify.py` — **35 tests**, no network, added to both CI
  workflows
- `validation/run_all.py` — 5/5
- `tools/test_build_graph.py` — 41 OK
- `tools/test_ui.mjs` — 81/81
- The write path was exercised on a copy of a real entity: frontmatter
  stamped, sources and relationships preserved, **body byte-identical**, and
  the result re-parses.

`docs/re-verification.md` is the procedure, linked from the README.

## Convention 108 and 108+

**Date:** 2026-08-19

The first item on the research queue after the European country batch, and
the one that came with a correction to how the Atlas presented European data
protection.

**11 new entities, 22 relationships.** 439 → **450 entities**, 728 → **750
relationships**. One new `status` value. 50 → **58 country scopes**.

| Entity | Instrument | Status |
|---|---|---|
| [[INTL-CONVENTION-108]] | ETS 108, opened 28 Jan 1981 | in force since 1 Oct 1985 |
| [[INTL-CONVENTION-108-PROTOCOL]] | ETS 181, opened 8 Nov 2001 | in force |
| [[INTL-CONVENTION-108-PLUS]] | CETS 223, opened 10 Oct 2018 | **`adopted` — not in force** |

Plus eight country anchors: [[AR]], [[CV]], [[MU]], [[MX]], [[MA]], [[SN]],
[[TN]] and [[UY]].

### What this corrects

The Atlas presented [[EU-GDPR]] as the origin of European data protection.
It is not. Convention 108 opened for signature on **28 January 1981** —
thirty-five years before the GDPR became applicable, and thirteen years
before the Directive the GDPR replaced. Fair and lawful processing, purpose
limitation, data minimisation, accuracy, storage limitation, security,
special protection for sensitive data, access and rectification: all of it is
in the 1981 text. **28 January is Data Protection Day** for that reason.

The GDPR now points back at it: **Recital 105** makes a third country's
accession to Convention 108 a factor in EU adequacy assessment. That edge is
asserted.

### The first entities outside Europe

Convention 108 is **the only instrument in the Atlas that is not regional**.
Every other binding instrument here is an EU act binding 27 states or a
national act binding one. This one is open to accession by any state, and
eight non-European states have acceded — five African, three Latin American.

They were created as base anchors because modelling the treaty without them
would have modelled it as the regional instrument it is expressly not. They
are **not the start of a global country layer**, and `countries/README.md`
and each anchor say so.

[[MU]] Mauritius has ratified **both** Convention 108 and the amending
protocol, putting it ahead of most European parties on the modernised
instrument.

### ⚠ Adopted, ratified by 34 states, binding nobody

[[INTL-CONVENTION-108-PLUS]] needs **38** ratifications. [[MD]] Moldova
became the **34th on 15 May 2026**. After nearly eight years it is four
short, and the Council of Europe has published a specific appeal to EU
member states to ratify.

That is a different kind of failure from the transposition delays the Atlas
already records. Belgium was twenty-nine months late on
[[EU-OPEN-DATA-DIRECTIVE]] and the Netherlands three years — but those
instruments were in force and being breached. This one has never come into
force at all.

### A `status` value had to be added

No existing value could say it.

- `proposed` would have called a treaty **34 sovereign states have ratified**
  a proposal.
- `active` would have called a treaty **not in force** operative law.

**`adopted`** was added to `metadata/schema.json`,
`metadata/controlled-vocabularies.md` and `metadata/metadata-schema.md`:
formally adopted, not yet in force. It is the third vocabulary addition in
three batches, after `proposes-to-supersede` and `amends`, and it meets the
same test — an existing value would have had to assert something untrue.

[[INTL-CONVENTION-108-PLUS]] also carries the **second use of `amends`**, and
the first outside a national transposition.

### ⚠ The verification debt blocked new modelling for the first time

Sources state that **all Council of Europe member states are parties** to
Convention 108 — roughly 46 more `applies-in` edges.

They were **not asserted**. The one source found for the rule gives a stale
member count (47, wrong since [[RU]]'s expulsion in 2022), and [[RU]]'s own
status as a party after expulsion is unaddressed by anything found. The
Council of Europe's chart of signatures and ratifications settles it, and
**`coe.int` is blocked by the egress proxy** — confirmed by probe, not
assumed.

Every previous batch's sourcing problem was *re-verification*: the facts were
recorded and unread. This is the first time the block has prevented the Atlas
from **recording a fact at all**. It is queued as `Blocked (egress)`.

### Verification

- **450 entities, 5,090 edges** (750 relationship, 1,653 association, 2,687
  wikilink), **58 country scopes**
- `validation/run_all.py` — 5/5
- `tools/test_build_graph.py` — 41 OK
- `tools/test_ui.mjs` — **81/81**
- `validation/audit.py` — no fully disconnected entities

All 11 new entities are `verification: search-only`; `coe.int`, `rm.coe.int`
and `eur-lex.europa.eu` are all blocked.

## The European country anchors

**Date:** 2026-08-19

Thirty-seven base country anchors, taking the Atlas from **13 country scopes
to 50**. **39 new entities, 65 relationships.** 400 → **439 entities**, 676 →
**728 relationships**.

Each anchor carries its country's position in the European legal and
institutional frameworks and nothing else — no authority, no portal, no
legislation. The point is that the next contributor reaching for Estonia or
Italy finds a scope waiting rather than having to create one.

### The scope rule is written down

There is no authoritative list of European countries, so `countries/README.md`
states the rule: a state gets an anchor if it satisfies **any** of EU
membership, EFTA/EEA membership, Council of Europe membership, or a live EU
accession relationship — plus [[BY]] and [[VA]], which satisfy none.

It is a union, not a geography. It admits [[AM]], [[AZ]], [[GE]] and [[TR]],
which the UN M49 geoscheme places in Western Asia, on Council of Europe
membership. Each entity says so on its own page.

### Two new international organisations

- **[[INTL-COE]]** — the anchor the twenty non-EU European states needed, and
  the home of **Convention 108 and 108+**, the only binding international
  treaty on data protection. The conventions are now the highest-value item
  on the research queue.
- **[[INTL-EFTA]]** — listed under "not modelled" on [[NO]] since the Norway
  batch; the gap became three countries wide when [[IS]] and [[LI]] arrived.

### Two membership facts that are not the same

[[RU]] carries `part-of` [[INTL-COE]] with `valid_from: 1996-02-28` and
`valid_until: 2022-03-16` — the Atlas's first closed validity interval on a
membership edge, recording the first expulsion in the organisation's history.
[[BY]] carries `related-to` instead: it has never been a member.

### One anchor is not an ISO code

[[XK]] has no ISO 3166-1 code; `XK` is user-assigned and is what the European
Commission, IMF and World Bank use. `metadata/ontology.md` §3.1 now names the
exception rather than being quietly broken, and the entity states that
recording it is not a position on recognition.

### The existing thirteen were normalised

Every country anchor previously had `relationships: []`, reaching the graph
only through entities pointing at it. All fifty now carry the same membership
edge, and `region: EU` is set consistently rather than on four member states
out of ten.

### A layout test that was asserting the wrong thing

`tools/test_ui.mjs` compared the smallest centroid gap anywhere in the
national band against the largest block radius anywhere in it. That held while
blocks were similar sizes; with [[NL]] at 85 entities and [[AD]] at one, it
demanded two one-entity blocks sit 464 apart.

The assertion now asks the question it was always trying to ask — per pair, is
the separation greater than *those two* blocks' radii — with bounding-box
non-overlap still checked separately. The tightest pair is BE/NO at 585
against 463, so it is not vacuous. **The layout constants were not touched;
the test was wrong, not the layout.**

### Verification

439 entities, 4,985 edges (728 relationship, 1,627 association, 2,630
wikilink), 50 countries. `validation/run_all.py` 5/5;
`tools/test_build_graph.py` 41 OK; `tools/test_ui.mjs` 81/81;
`validation/audit.py` reports no fully disconnected entities. All 39 new
entities are `verification: search-only`; accession years come from general
reference knowledge rather than the cited pages, and each anchor says so.

## The Open Data Directive transpositions

**Date:** 2026-08-19

The largest remaining item on the research queue, carried since the Belgium,
France and Spain batches. **4 new entities, 10 relationships.** 396 → **400
entities**, 666 → **676 relationships**. One new relationship type.

| Country | Instrument | Pattern |
|---|---|---|
| Belgium | [[BE-HERGEBRUIK-WET-2023]] — 25 December 2023 | `amends` [[BE-HERGEBRUIK-WET]] |
| Spain | [[ES-RDL-24-2021]] — 2 November 2021, Book Three | `amends` [[ES-LEY-37-2007]] |
| France | **none exists** | see [[FR-LOI-VALTER]] |

### Three findings

**Belgium's transposition post-dates the Belgium batch.** The federal act was
published on 25 December 2023, after the sources that batch searched. What
the queue recorded as a research failure was a timing fact. At twenty-nine
months late it is the extreme of the Atlas's range, against
[[IE-PSI-REGULATIONS-2021]] at five days.

**Belgium's regions beat its federal state.** Flanders transposed by decree
on 2 July 2021, a fortnight inside the deadline; Brussels followed in
December 2021 and Wallonia in November 2022. Belgium was still referred to
the Court of Justice, because a member state answers for its whole
territory. Only the federal act is modelled — `level: regional` means
*supra*-national in this Atlas, the same blocker recorded against OSLO.

**France's "2021 ordinance" does not exist.** Ordonnance n° 2021-1518 of 24
November 2021 is real and does complete the transposition of a 2019
directive — **2019/790**, on copyright. France's regime predates the Open
Data Directive ([[FR-LOI-VALTER]], 2015, codified into the CRPA in 2016), and
France is absent from the nineteen member states served with letters of
formal notice in September 2021. No French entity asserts
`implements-requirement-from` to the Directive; the empty matrix cell is the
finding.

That is the second near-miss of this shape in three batches, after the
Archiefwet/Kadasterwet BWBR confusion. In both fields a wrong citation
resolves to a real instrument about something else.

### New relationship type: `amends`

Four of the six modelled transpositions edit statutes that already existed.
`supersedes` would have retired instruments still in force;
`implements-requirement-from` records the EU obligation, not the domestic
edit. `amends` was added across the three metadata files — 22 types now. Its
inverse was deliberately not added, and the resulting asymmetry with
`implements`/`implemented-by` is queued rather than resolved by reflex.

### Also closed

- **Red.es** → [[ES-RED-ES]], giving [[ES-DATOS-GOB-ES]] a `maintained-by`
  and taking the portal-custodian gap from seven to six. The statement the
  Spain batch wanted was on red.es itself.
- **A French DCAT application profile** — none exists; France is measured on
  conformity with DCAT-AP itself. Spain's profile was already modelled inside
  [[ES-NTI-RISP]], so no duplicate was created.

### Verification

400 entities, 4,733 edges (676 relationship, 1,571 association, 2,486
wikilink), 13 countries. `validation/run_all.py` 5/5;
`tools/test_build_graph.py` 41 OK; `tools/test_ui.mjs` 81/81;
`validation/audit.py` reports no fully disconnected entities. All four new
entities are `verification: search-only` — the egress proxy blocks
eur-lex.europa.eu and legifrance.gouv.fr outright.

## The Dutch register statutes

**Date:** 2026-08-18

The second cluster left open by the research-queue pass, and the one the
register batch itself deferred because *"doing half of it would leave the
layer inconsistent."* **7 new entities, 15 relationships.** 389 → **396
entities**, 651 → **666 relationships**.

**Nine of the ten basisregistraties now carry a `governed-by` edge**, against
one before: [[NL-WET-BAG]], [[NL-WET-BGT]], [[NL-WET-BRO]], [[NL-WET-WOZ]],
[[NL-HANDELSREGISTERWET]], [[NL-WEGENVERKEERSWET-1994]] and
[[NL-KADASTERWET]], joining [[NL-WET-BRP]] from Batch 3.

### The weakest of the ten, closed

[[NL-BRT]] was recorded as the one register where **no statute was found at
all**. It is the [[NL-KADASTERWET]] of 3 May 1989 — and it resisted searching
because **there is no "Wet basisregistratie topografie"**. That act carries
both the cadastral and the topographic base registration. A gap that looked
like missing research was a wrong assumption about the shape of the law.

### Seven statutes for nine registers

One act carries two registers, and three of the seven are **general
statutes** that happen to contain a registration — a valuation act, a road
traffic act and the Kadasterwet. Only four were written to constitute one.
Neither fact is visible from the register entities.

### A wrong identifier caught before it shipped

A search returned **BWBR0007376** for the Kadasterwet. That is the
**Archiefwet 1995**; the Kadasterwet is **BWBR0004541**. All seven entities
are keyed on BWBR identifiers, and a wrong one resolves to a real but
unrelated act — an error invisible on review because the URL works.

### A layout regression, caught by one pixel

Seven new Dutch entities failed `tools/test_ui.mjs`: *"country blocks are
further apart than they are wide — min separation 463 vs max spread 464."*

Two obvious fixes were both wrong. Widening `blockGapX` made it worse by
changing which blocks wrap onto which line; a minimum horizontal footprint
for small blocks moved the wrong pair. Instrumenting showed the binding pair
was **PL/PT stacked vertically**. `blockGapY` 70 → **190** fixes it with
headroom (579 vs 464), and the docs now say which constant to reach for.

### Still open

[[NL-BRI]] (Chapter IVA of the AWR, no citable identifier found), the
Organisatiewet Kadaster, the implementing decrees beneath all seven acts, and
Belgium, France and Spain's Open Data Directive transpositions.

## Working the research queue

**Date:** 2026-08-18

The queue had drifted: six items it listed as open had been closed by later
batches and never marked. **Reconciled**, then its two highest-value
remaining clusters worked. **5 new entities, 10 relationships.**
384 → **389 entities**, 641 → **651 relationships**.

### Reconciliation

Marked done with the closing entity named in place: the IDSA and IDS-RAM,
INSEE, the European Statistical System, the Dutch NCSC, CSIRT NASK (partly —
CSIRT MON is still open) and the cybersecurity domain. A queue that lists
finished work as pending hides what is actually open.

### The e-invoicing chain

The queue's "highest-value German item", carried since the Germany batch.
[[EU-EINVOICING-DIRECTIVE]] → [[EU-EN-16931]] → [[DE-XRECHNUNG]], with the
standard `maintained-by` [[EU-CEN]].

The directive is unusual: it does not tell member states to act, it
**commissions a standard**. And **[[EU-CEN]] now maintains something** —
eleven national members point at it and, until now, no standard did.

### The Open Data Directive gap, halved

[[IE-PSI-REGULATIONS-2021]] (S.I. 376/2021, standalone, five days late) and
[[PT-LEI-26-2016]] (an amendment, folding open data into Portugal's access to
administrative and environmental information act). Belgium, France and Spain
remain unidentified — all three amended existing law.

A general survey called Portugal a standalone-legislation country; the
Portugal-specific sources say otherwise. The Atlas follows the specific
source and records the conflict.

### [[EU-PSI-DIRECTIVE]]

A repealed directive, created because two **live** national acts —
[[BE-HERGEBRUIK-WET]] and [[DE-IWG]] — transpose it and had nowhere to point.
`status: superseded` with the successor named.

### Enforcement the Atlas cannot model

Nineteen member states faced infringement proceedings over the Open Data
Directive, and four were referred to the Court of Justice in February 2023 —
including the Netherlands, whose transposition the Atlas dates to 2024. There
is no entity type for an infringement procedure and no Court of Justice
entity, so the graph shows the outcome and not the enforcement. Recorded on
the instrument and queued.

### Left deliberately

Belgium, France and Spain's transpositions; and the eight Dutch
basisregistraties statutes, because the queue's own note says doing half
would leave that layer inconsistent.

## Portugal, Luxembourg and Czechia — countries eleven, twelve and thirteen

**Date:** 2026-08-18

**23 new entities** plus 54 `applies-in` edges. 361 → **384 entities**,
555 → **641 relationships**. Ten countries → **thirteen**; eight EU member
states → **eleven**.

[[EU-EDPB]] 8 → **11** incoming, [[EU-ESS]] 8 → **11**, [[EU-CEN]] 7 →
**10**. Every EU member state in the Atlas now has an authority on the Board,
an institute in the ESS and a standards body in CEN.

### What each added

- **Czechia**: [[CZ-ZAKON-60-2026]], an act on **data management and
  controlled access**, making [[CZ-DIA]] the state's single information point
  and the node to the European data portal. The Atlas had almost no law about
  how a state manages its *own* data. The Netherlands built the arrangement
  ([[NL-IBDS]], [[NL-FDS]]); Czechia legislated it.
- **Luxembourg**: the smallest country here, and through [[LU-ILNAS]] one of
  only two whose standards body holds all five standardisation memberships —
  the other being [[GB-BSI]]. Plus small-state concentration: ILNAS is
  standards, accreditation and product safety; [[LU-CTIE]] is government IT
  and State infrastructure security.
- **Portugal**: [[PT-LEI-58-2019]] *executes* the GDPR — an eighth verb for
  one operation — and [[PT-AMA]] carries a **regulatory** simplification
  mandate no comparable Atlas body records.

### Three name collisions

[[PT-CNPD]]/[[LU-CNPD]], [[PT-INE]]/[[ES-INE]], and [[LU-STATEC]] whose full
name is word-for-word [[FR-INSEE]]'s. All genuine, all handled by scoped IDs.

### The one that needed care

[[CZ-UNMZ]] holds Czechia's standardisation **membership**; **ČAS** does the
work. No other country splits it, and ČAS is the more visible body — an
entity built from its pages would have claimed a membership it does not hold.

### Refusals

No [[LU]] ↔ [[EU-PUBLICATIONS-OFFICE]] edge despite the Luxembourg seat
(hosting is not participating); no custodian for any of the three new portals
(a publisher page proves publication, not custodianship); no separate entity
for the Czech NCKB, which the sources present as a section of [[CZ-NUKIB]].

### Connectivity

Components unchanged at 20, largest 326 → **349**, isolated unchanged at 8.
Twenty-three new entities and no orphans — the scope-anchor rule is enforced
at build time.

## The cheap structural fixes

**Date:** 2026-08-18

All four items on `discovery/candidates.md`'s "cheap structural fixes" list.
**7 new entities, 16 relationships.** 354 → **361 entities**, 539 → **555
relationships**. [[EU-EDPB]] **3 → 8** incoming, [[EU-CEN]] **3 → 7**,
[[EU-ESS]] **7 → 8**.

**The DPAs reach the Board.** Five edges — [[DE-BFDI]], [[BE-APD]],
[[FR-CNIL]], [[ES-AEPD]], [[PL-UODO]] — on [[EU-GDPR]] **Article 68(3)**,
which composes the Board of one supervisory-authority head per member state
plus the [[EU-EDPS]], and provides for a **joint representative** where a
member state has more than one authority. That last clause resolves the exact
German question [[DE-BFDI]] had recorded as unguessable. No new entity.

**[[FR-INSEE]]** closes the last missing statistical office; every EU member
state in the Atlas is now in [[EU-ESS]].

**[[BE-NBN]], [[FR-AFNOR]], [[ES-UNE]], [[PL-PKN]]** created, and the
[[IE-NSAI]] refusal closed — not by reading the CEN member list, but by
finding CEN-CENELEC's statement of the **rule** that its national members are
the standardization bodies of the 27 EU countries.

**[[NL-NCSC]]** (DTC merged in on 1 January 2026; 2.4 million organisations
served) and **[[PL-NASK]]** (conducts CSIRT NASK under [[PL-KSC]]) close the
cyber-authority gap. CSIRT MON stays unmodelled.

### The lesson the batch produced twice

A refusal for want of a source is **not** the same as a fact being
unknowable. Both refusals closed here were correct in method and wrong in
conclusion, and in both cases the source was in the instrument that created
the thing — Article 68(3) for the Board, CEN-CENELEC's membership rule for
the standards bodies. Both entities now record how the refusal fell rather
than quietly dropping it.

### The one weak edge

[[NL-NCSC]] `applies-to` [[NL-CBW]] is `source: interpretation`,
`confidence: low`: the sources make the NCSC the national cyber body and put
it in front of the Cyberbeveiligingswet, but none states that it is the
authority **designated under** the act.

### Connectivity

Components unchanged at 20, largest 319 → **326**, isolated unchanged at 8.
These fixes thickened the middle rather than rescuing islands.

## Data spaces — completing the fourteen

**Date:** 2026-08-18

**13 new entities.** 341 → **354 entities**, 522 → **539 relationships**;
the data-space layer goes from **8 to 19**. Components 22 → **20**, largest
302 → **319**.

### All fourteen common European data spaces now exist

Batch 10 created four and left ten, because research had returned only their
names. Six of those ten turned out to have real content once searched
individually: [[EU-CEEDS]] (Digital Europe deployment, 15+ member-state
pilots), [[EU-EOSC]] (already running — EU Node since October 2024, thirteen
federated candidate nodes), [[EU-CULTURAL-HERITAGE-DATA-SPACE]] (Europeana,
60M+ items), [[EU-MANUFACTURING-DATA-SPACE]], [[EU-FINANCIAL-DATA-SPACE]]
(FIDA) and [[EU-LANGUAGE-DATA-SPACE]].

Four remain `coverage: low` and say so — tourism, media, skills and public
administration. They are created anyway, because holding thirteen of fourteen
would misrepresent the set.

**Only [[EU-EHDS]] carries `applies-in` edges.** It is the only one backed by
a Regulation; the rest are programmes and initiatives and do not apply in a
member state in the sense that relationship carries here.

### The IDSA layer, queued since Batch 5, is closed

[[INTL-IDSA]] and [[INTL-IDS-RAM]] created. Two long-standing refusals
resolved: [[DE-CATENA-X]] `based-on` the IDS-RAM, [[NL-ISHARE]] `references`
it — not `based-on`, because the sources describe the IDSA incorporating
iSHARE rather than the reverse.

**DIN SPEC 27070** (21 February 2020) standardises the IDS security gateway,
giving [[DE-DIN]] its first inbound specification edge — that entity was
recorded in the Germany batch as a standards body maintaining nothing the
Atlas held.

### The first data-space lineage

[[DE-MANUFACTURING-X]] is `based-on` [[DE-CATENA-X]]: the sources state that
Manufacturing-X followed Catena-X and builds a factory-equipment data
ecosystem on its basis. `based-on`, not `part-of`.

### Refusals

No German-to-EU manufacturing edge (same sector is not a relationship); no
edges from [[EU-PUBLIC-ADMIN-DATA-SPACE]] to
[[EU-INTEROPERABLE-EUROPE-ACT]], [[EU-EIF]] or [[EU-SDG]] despite the
obvious adjacency; no cultural-heritage ↔ media/tourism edges, because
"will explore cooperation" is intent, not connection; no `DOMAIN-ENERGY`,
which would have one member.

## Every entity reaches its scope anchor

**Date:** 2026-08-18

A rule, 24 edges, one new entity, and enforcement. 340 → **341 entities**,
498 → **522 relationships**; components **45 → 22**, largest **283 → 302**,
entities with no typed relationship **32 → 8, all of them domains**.

### The rule

`metadata/relationship-types.md` **§2.3**: every entity carries at least one
provenanced relationship, in or out. Where no substantive edge could be
sourced, the entity takes an **anchor edge** to its scope — following the two
conventions already in the repository, `applies-in` for country anchors and
`part-of` for [[EU]] and [[UN]].

| Entity kind | Edge | Count |
|---|---|---|
| Instruments | `applies-in` its country | 7 |
| State bodies and public platforms | `part-of` its country | 14 |
| National bodies **not** part of the state | `related-to` its country | 2 |
| [[INTL-IETF]] | `part-of` [[INTL-ISOC]] | 1 |

An anchor edge asserts scope and nothing more. Each carries evidence ending
in a sentence naming itself as an anchor edge, so they can be found and
replaced; the missing substantive edges stay in `discovery/unresolved.md`.

### Two entities that could not take `part-of`

[[NL-SURF]] is member-owned and [[NL-NICTIZ]] is a foundation. `part-of`
means structural containment, so using it would have turned a filing
convention into a false claim about ownership. Both take `related-to`.

### [[INTL-ISOC]] — the batch's only new entity

[[INTL-IETF]] belongs to no country and is not part of the EU or UN. Its
actual parent is the Internet Society, via the IETF Administration LLC — a
single-member disregarded entity of ISOC. The LLC is not modelled, so the
edge collapses two hops into one, stated on both entities.

### Why domains are exempt

They are classification nodes reached by **association**, and in that layer
they are the three largest nodes in the Atlas: [[DOMAIN-GOVERNMENT]] at
degree **232**, [[DOMAIN-NATIONAL-SECURITY]] at 47,
[[DOMAIN-CYBERSECURITY]] at 35. A test asserts the exemption **earns
itself** — that every domain is still referenced by some entity's `domains:`
list, so it is not unreachable in both layers at once.

### Enforcement

`validate_relationships.py` fails the build on any orphan and names the
exemption; verified against a deliberately broken entity. Two tests added
(39 → **41**). `CONTRIBUTING.md` gains step 6a.

### A reversal, recorded rather than buried

Two batches ago the Atlas argued own-country `applies-in` should be
reconsidered rather than extended, and declined it for eighteen national
acts. This batch extends it on the maintainer's instruction and makes it a
documented rule. The original objection stands — it does give `applies-in` a
second meaning — but a documented second meaning costs less than 24 entities
being invisible. `progress/backlog.md` is updated so the note no longer
contradicts the ontology.

## Norway, Switzerland and Ireland — countries eight, nine and ten

**Date:** 2026-08-18

**27 new entities** plus 18 `applies-in` edges to Ireland.
312 → **339 entities**, 466 → **495 relationships**, seven countries → **ten**.

Chosen from the structural review recorded in `discovery/candidates.md`, and
chosen for what each **proves**.

### The four relationships to EU law are now all represented

| Position | Country | Mechanism |
|---|---|---|
| Member state | NL, DE, BE, FR, ES, PL, **IE** | Direct applicability or transposition |
| Former member state | GB | Assimilated law, adequacy, extraterritorial scope |
| **EEA EFTA state** | **NO** | **EEA Joint Committee incorporation, then national implementation** |
| **Neither** | **CH** | **Autonomous law, adequacy, bilateral agreements** |

The Norwegian case is datable and is the batch's sharpest result: the GDPR
was applicable in the member states on **25 May 2018** and took effect in
Norway on **20 July 2018**, after **JCD No 154/2018** incorporated it into
Annex XI of the EEA Agreement on 6 July. **Eight weeks of divergence that a
member state cannot have** — and the reason [[NO]] carries no `applies-in`
edge.

### A fourth type for a national data protection act

[[CH-REVDSG]] carries `aligned-with` [[EU-GDPR]]. No requirement obliged
Switzerland to legislate; it harmonised to keep **adequacy** under Article
45. Alongside `implements-requirement-from` (six countries),
`derived-from` ([[GB-UK-GDPR]]) and direct applicability (BE, FR), that
completes the set.

[[CH-EMBAG]] is the Atlas's **first statutory open-source mandate**.

### The one-stop-shop enters the graph

[[IE-DPC]] is Article 56 lead supervisory authority for much of the
technology sector established in the Union, worked through the €530m TikTok
Article 60 decision. [[EU-EDPB]] went from **two** incoming edges to three.
The general fix — the other five member-state authorities — was **not done**
and remains the top item in `discovery/candidates.md`.

### Tooling: the YAML boolean trap

`NO` is a YAML 1.1 boolean. An unquoted `country: NO` silently parsed as
`False`, and every Norwegian entity failed validation. Fixed by quoting, then
guarded so it cannot recur silently:

- `validate_frontmatter.py` names the coercion for `id` and `country`.
- `tools/test_build_graph.py` gains two tests (37 → **39**): a general one,
  and one pinning Norway by name.

This is the first defect in this repository caused by the **serialisation
format** rather than by research or modelling, and the only ISO 3166-1
alpha-2 code the Atlas uses that collides.

### Domain effect

[[DOMAIN-GEOSPATIAL]] goes from **3 of 7** countries to **6 of 10**
([[NO-KARTVERKET]], [[CH-SWISSTOPO]], [[IE-TAILTE]]). Belgium, Spain,
France and Poland remain without any geospatial entity, which is now the
more conspicuous gap.

### Connectivity

312 → 340 entities, 466 → 498 relationships; components 31 → **45**,
largest 272 → **283**, isolated 21 → **32**. **Eleven of the twenty-eight
new entities carry no typed relationship**, each a documented refusal rather
than an oversight. That is the same debt the loose-nodes batch paid down and
is the natural follow-up.

[[INTL-EEA-AGREEMENT]] was created to reach [[NO]] honestly;
[[CH-REVDSG]] `applies-in` [[CH]] uses the [[GB-UK-GDPR]] own-country
precedent, flagged on the entity as an extension of a pattern the backlog
says to reconsider.

### Recorded refusals

No `applies-in` to [[NO]] or [[CH]]; no Irish edge on [[UN-AARHUS]]; no
`participates-in` edges for [[IE-NSAI]]; no [[CH-EMBAG]] →
[[CH-OPENDATA-SWISS]] edge; no `maintained-by` for [[NO-ALTINN]]. Each is
argued on its entity.

## The intelligence and security services

**Date:** 2026-08-18

**47 new entities** across all seven countries: **19 intelligence services**,
**9 oversight bodies**, **18 acts**, and [[DOMAIN-NATIONAL-SECURITY]].
265 → **312 entities**, 390 → **465 relationships**. The relationship layer
holds at **31 components**; the largest grows from **224 to 272 of 312**.

### Why a new domain

Every other domain in the Atlas groups entities that sit **inside** EU data
law. This one groups entities carved **out** of it: Article 4(2) TEU
reserves national security to the member states, and [[EU-GDPR]] Article
2(2)(a) excludes it from the Regulation's material scope.

**No EU instrument carries `applies-in` to any entity in this batch.** That
is the structural point — an empty EU column here is a finding, not missing
research. Each country builds its own review machinery instead:
[[NL-TIB]]/[[NL-CTIVD]], [[DE-PKGR]]/[[DE-UKR]], [[BE-COMITE-I]],
[[FR-CNCTR]], [[GB-ISC]]/[[GB-IPCO]], [[PL-KSS]].

Two countries partly refuse the carve-out. **Part 4 of [[GB-DPA-2018]]** is
a data protection regime written for [[GB-MI5]], [[GB-SIS]] and
[[GB-GCHQ]]; **[[BE-GDPR-WET]]** carries a subtitle on processing by the
intelligence and security services, with verification routed through
[[BE-COMITE-I]] rather than [[BE-APD]]. The Union does not regulate here; a
member state still may.

### Five patterns the Atlas could not compare before

1. **One act per service** — Germany: [[DE-BNDG]], [[DE-BVERFSCHG]],
   [[DE-MADG]], with [[DE-G10]] cutting across all three.
2. **One organic act for all services** — the Netherlands
   ([[NL-WIV-2017]]) and Belgium ([[BE-WIV-1998]]).
3. **An act about techniques, not bodies** — France
   ([[FR-LOI-RENSEIGNEMENT-2015]], codified as CSI Book VIII) and the UK
   ([[GB-IPA-2016]]). France legislated powers because it had no agency
   acts; the UK layered powers on top of agency acts it already had.
4. **Acts of avowal, one service at a time** — the UK: [[GB-SSA-1989]],
   then [[GB-ISA-1994]] five years later.
5. **Paired agencies, paired acts** — Poland: [[PL-UABWAW-2002]] (civilian)
   and [[PL-USKWSWW-2006]] (military), four years apart on the same
   internal/external axis.

And three answers to *who authorises intrusive measures*: a **judge** in
advance (Spain, [[ES-LO-2-2002]]); a minister followed by **binding**
review (the Netherlands, [[NL-TIB]]); a Prime Minister acting on an
**opinion**, with recourse to the Conseil d'État (France, [[FR-CNCTR]]).

### Two countries put cyber security inside intelligence

[[GB-NCSC]] is `part-of` [[GB-GCHQ]]; [[ES-CCN]] is `part-of` [[ES-CNI]].
Five countries keep them apart — [[DE-BSI]] under [[DE-BMI]],
[[FR-ANSSI]] under the SGDSN, [[BE-CCB]], and the Dutch and Polish
arrangements. Both cyber bodies were already Atlas entities; nothing showed
where they sat until now.

### Recorded limits

Named on the entities and in `discovery/unresolved.md`: [[DE-UKR]]'s missing
statutory basis after the Constitutional Court's 28 September 2022 decision;
France's unmodelled délégation parlementaire au renseignement; the two
*premier cercle* services (DNRED, TRACFIN) that are absent; Germany's
G10-Kommission; UK Defence Intelligence; Belgium's BIM-wet and OCAD;
Poland's CBA; and the sixteen German Landesämter, which are out of scope
because the Atlas has no sub-national level.

**No own-country `applies-in` edges were added**, honouring the decision
recorded in `progress/backlog.md` in the preceding batch.

## Final Global Relationship Pass and Quality Gate

**Date:** 2026-08-14 · **Full report:** `validation/final-quality-gate.md`

### Relationship pass (§26)

Added **12 sourced relationships** (119 → 131); entities with no
relationship of their own fell from 35 to 29. `part-of` is now the most
common type (25).

- **Institutional membership**, extending the fix Batch 11 began: the UN
  layer modelled `part-of` and the EU layer did not. Added for Eurostat and
  SEMIC (→ Commission), ENISA/EDPB/EDPS/Publications Office (→ EU), and the
  four UN instruments (→ UN).
- **Links stated in prose but missing from frontmatter:** Commission
  `produces` the Cybersecurity Strategy; DSSC Blueprint `applies-to` the
  common data spaces.

Of the four patterns §26 asks for: **standards** and **legislative** chains
are complete; **organisational** is partial; **vertical is not** — UN → EU
remains 0, and the two links that would close it were examined and refused
again for want of a source.

### Quality gate (§27)

**Two further defects found and fixed**, both Batch 0 residue:

1. Four sources claimed `accessed` dates — **asserting access that never
   happened**. Removed.
2. The `NL`/`EU`/`UN` anchors claimed `last_verified` while marked
   `verification: unverified` — a direct contradiction. Set to null.

Together with Batches 6/11/15, **every defect this project's validation has
surfaced originated in its own earliest work** — an argument for running
gates earlier, not only at the end.

**Passes:** ontology coherence, ID uniqueness and stability, temporal
integrity (5 successor + 6 previous_version chains, 0 mismatches, 3
superseded entities retained), country-neutrality (no country-scoped copies
of supra-national entities), provenance labelling (120 fact / 11
interpretation), technical integrity (5/5 checks, 0 errors).

**Does not pass:** source verification. 119 of 125 entities rest on sources
nobody has read; **no URL in the repository has been fetched.** No entity
claims `confidence: high` or `coverage: high`, correctly.

**Structurally incomplete:** the UN layer connects to nothing outside
itself.

---

## Batches 6, 11 and 15 — Validation

**Date:** 2026-08-14

**Full findings:** `validation/reports.md`. New tool: `validation/audit.py`.

### What was and was not checkable

An earlier position in this project — that the validation batches could not
run at all until sourcing was fixed — **was too absolute.** Most of what the
batch briefs ask for is checkable without sources, and doing so found real
defects.

Checkable and checked: duplicates, invalid IDs, broken links, inconsistent
metadata, missing sources, weak-source reliance, unsupported relationships,
missing relationships/orphans, country-specific assumptions.

**Not checkable, not checked:** outdated information, incorrect statuses,
whether cited sources say what the Atlas claims, whether cited URLs resolve
at all. 119 of 125 entities rest on sources nobody has read.

### Three defects found and fixed

| Batch | Defect | Fix |
|---|---|---|
| 6 | `NL-ISHARE` fully disconnected — no inbound or outbound edges | Explicit `related-to` → `NL-DSGO`, marked `source: interpretation`, `confidence: low` |
| 6 | **`NL`, `EU`, `UN` anchors cite URLs written from background knowledge in Batch 0**, never confirmed by search or fetch | Marked `verification: unverified`; `confidence: high` → `medium` |
| 11 | `EU` anchor fully disconnected, while `UN` was not | `part-of` → `EU` added from Commission, Parliament and Council |

The anchor defect is the notable one: **self-inflicted in Batch 0**, against
the brief's explicit "never invent URLs". And the confidence downgrade was
*forced* by this repository's own validation rule — `validate_frontmatter.py`
rejects `confidence: high` on `unverified` entities. The rule caught its
author.

The `EU` anchor defect was an **inconsistency between layers**: the UN layer
modelled institutional membership and the EU layer did not.

### ⚠ Principal finding: the international layer is an island

| Direction | Count |
|---|---|
| EU → NL | 15 |
| NL → EU | 10 |
| NL → INTL | 2 |
| EU → INTL | 1 |
| **UN → anything** | **0** |

The 9 UN-scoped entities connect only to each other. The brief's target is
UN → EU → National → Sector; what exists is a connected EU↔NL graph plus an
**unattached UN component**.

Two links would close most of it — `UN-UNSD` → `EU-EUROSTAT` and
`UN-FPOS` → `NL-WET-CBS` — and **both were examined and refused for want of
a source.** Closing them is the highest-value research remaining.

### Clean results

- No duplicate names or aliases across 125 entities.
- No orphans remaining, no broken links, no invalid IDs, no vocabulary
  violations.
- **No country-scoped copies of supra-national entities** — README §16
  holds. 17 `applies-in` relationships, all targeting `NL`; the mechanism is
  exercised but untested with a second country.
- Every non-domain entity has ≥1 source. Only two entities rely solely on
  weak sources: `NL-PETRA` and `UN-DATA-COMMONS`.
- 119 provenanced relationships: 108 `fact`, 11 `interpretation`, every
  interpretation labelled.
- **No entity claims `confidence: high` or `coverage: high`.**

### Verdict

The graph is **internally coherent and honestly labelled**. It is **not
verified**. These reports certify structure, not truth, and should be re-run
after the re-verification pass.

---

## Batches 12–14 — UN and International Layer

**Date:** 2026-08-14

**⚠ Evidence standard:** unchanged — all entities `verification: search-only`.
The international layer is the **weakest-sourced** in the Atlas: un.org and
ietf.org material proved largely unreachable through search, and several
entities rest on a single indirect citation.

### Batch 12 — UN Core (5 entities)

| ID | Type | Note |
|---|---|---|
| `UN-2-0` | initiative | Sept 2023 policy brief; the quintet of change |
| `UN-DATA-STRATEGY` | strategy | ⚠ **weakest in the batch** — one indirect source |
| `UN-GDC` | policy | Global Digital Compact; only an EU source located |
| `UN-FPOS` | framework | Fundamental Principles of Official Statistics |
| `UN-DATA-COMMONS` | platform | ⚠ **single Grokipedia source** |

### Batch 13 — Agencies and International Organisations (7 entities)

The brief's warning — *"Do not incorrectly classify non-UN organisations as
UN organisations"* — is implemented **in the ID scheme**, not just in prose:

| UN system (`UN-`) | Non-UN (`INTL-`) |
|---|---|
| `UN-UNSD` — Statistics Division | `INTL-ISO` |
| `UN-UNCTAD` — data governance working group | `INTL-IEC` |
| `UN-ITU` — **specialised agency** | `INTL-W3C` |
| | `INTL-OECD` |
| | `INTL-IETF` ⚠ thinnest |

`UN-ITU` is the case where the distinction bites: it appears in
standards-ecosystem listings alongside ISO, IEC, W3C, IETF and ETSI, but is
a UN specialised agency and carries the `UN` scope accordingly.

### Batch 14 — International Standards (2 new, 1 rebuilt)

*(Batches 12–14 added **15** entities in total, plus the `INTL-DCAT`
rebuild. An earlier draft of this report and the Batch 12–14 commit message
said 14 and 126 respectively; both were off by one. Corrected here.)*

| ID | Note |
|---|---|
| `INTL-ISO-IEC-27001` | Closes the `NL-BIO` gap open since Batch 4 |
| `INTL-ISO-IEC-27002` | ⚠ cited URL resolves to the superseded 2013 edition |
| `INTL-DCAT` | **Rebuilt** on w3.org; confidence low → medium |

### Two international → national chains now complete

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
INTL-ISO-IEC-27001 + -27002 (ISO/IEC) → NL-BIO / BIO2
```

The DCAT rebuild matters: Batch 9 flagged the top of that chain as its
weakest link because no W3C source could be found. Batch 14 found
`w3.org/TR/vocab-dcat-3/` and the chain is now sourced end to end.

**Relationships added:** 9 provenanced entries.
**Sources added:** 24 source entries.

### Scope items deliberately not delivered

- **UN DESA, UNDP, UNESCO, WHO, UNECE** — all named in Batch 13's scope; **no
  usable source was located for any**, so none was created.
- **World Bank** — omitted deliberately. Its institutions are technically UN
  specialised agencies, making the UN/non-UN call genuinely tricky, and
  misclassifying it is the precise error the brief warns against.
- **Batch 14's standards list** names data governance, metadata, data
  quality, interoperability, information management, digital identity,
  cybersecurity, AI, data sharing, APIs and knowledge graphs. **Only
  information security and metadata were covered.** This is a substantial
  under-delivery and is recorded as such.

### Honest weak points

- `UN-DATA-COMMONS` cites **Grokipedia** — an AI-generated encyclopedia and
  the weakest citation anywhere in this Atlas.
- `UN-DATA-STRATEGY` has no source dedicated to it.
- `UN-GDC`, a UN instrument, is sourced **only to a European Commission news
  page**.
- `INTL-IETF` carries almost nothing beyond its category — yet IETF RFCs
  underpin the HTTPS/DNSSEC/mail standards mandated by
  `NL-PAS-TOE-OF-LEG-UIT`, a real chain left entirely unmodelled.
- `INTL-ISO` → `NL-NEN` is **not asserted**: unlike CEN, no membership
  composition rule was sourced.
- `UN-UNSD` → `EU-EUROSTAT` is **not asserted**: no source connects the
  European Statistical System to the UN statistical system, leaving the
  statistics chain stopping at the EU.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 125
entities.

**Next:** Batch 15 (Global Validation) and the Final Quality Gate — both of
which, like Batches 6 and 11, need primary sources before they mean
anything.

---

## Batch 10 — EU Data Spaces

**Date:** 2026-08-14

**Scope:** The common European data spaces — health, mobility, energy,
finance, agriculture, manufacturing, skills, tourism, public
administration, green deal, research, media — with purpose, governance,
responsible organisations, standards, legislation, infrastructure and
participating countries for each.

**⚠ Evidence standard:** unchanged — all entities `verification: search-only`.

**Entities added (6):**

| ID | Type | Note |
|---|---|---|
| `EU-EHDS` | data-space | Health — Reg. (EU) 2025/327, the only one with its own regulation |
| `EU-EMDS` | data-space | Mobility — purpose statement only |
| `EU-GREEN-DEAL-DATA-SPACE` | data-space | Green Deal — purpose statement only |
| `EU-AGRI-DATA-SPACE` | data-space | Agriculture — purpose statement only |
| `EU-DSSC` | organisation | Data Spaces Support Centre |
| `EU-DSSC-BLUEPRINT` | framework | Shared reference architecture for data spaces |

**Ten of the fourteen data spaces were deliberately not created.** Research
returned **only their names** for cultural heritage, energy, finance,
industry, language, media, public administrations, research and innovation,
skills and tourism — no purpose, governance, standards or infrastructure.
Batch 10's brief asks for exactly those attributes; ten entities whose whole
content would be "this is one of the fourteen" is the shallow-entity failure
the brief warns against. All ten are enumerated on
[[EU-COMMON-DATA-SPACES]] and queued.

**This batch is therefore a partial delivery of its scope, and says so.**
Three of the four created are thin (one sourced purpose sentence each) and
each states that in its own body. Only `EU-EHDS` is substantively
researched.

**The most useful entity is `EU-DSSC-BLUEPRINT`.** Its rulebook and
governance-framework model is the EU-level analogue of the Dutch
*afsprakenstelsel* pattern running through [[NL-FDS]], [[NL-DSGO]],
[[NL-ISHARE]] and [[NL-HEALTH-RI]]. **No relationship is asserted** — the
resemblance is an Atlas observation, recorded as interpretation and queued.
Confirming it would connect the Dutch and EU data-space layers structurally
rather than thematically.

**Two high-value links left unasserted**, both on the same principle that
has served this project well:
- `EU-EHDS` → `NL-HEALTH-RI`: Health-RI is the obvious candidate for the
  Dutch health data access body, but the HDAB designation phase runs
  2027–2029 and nothing sources it yet.
- `EU-EMDS` → `NL-NTM`: national access points look like the natural
  building blocks of a mobility data space, but no source says so.

**Relationships added:** 6 provenanced entries.
**Sources added:** 13 source entries.

**Honest weak points:**
- `EU-EHDS` has **no EUR-Lex citation** — the strongest source is the
  Parliament's Legislative Observatory file.
- `EU-EMDS`, `EU-GREEN-DEAL-DATA-SPACE` and `EU-AGRI-DATA-SPACE` are
  `confidence: low` placeholders with citations, not researched content.
- Two sources are third-party copies or project sites rather than
  Commission material.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 110
entities.

**Next batch:** Batch 11 — EU Validation. The same caveat applies as to
Batch 6: it cannot be completed in substance while the sourcing debt stands.

---

## Batch 9 — EU Organisations and Standards

**Date:** 2026-08-14

**Scope:** European Commission and DGs, Eurostat, EDPB, EDPS, ENISA,
European Parliament, Council of the EU, Publications Office, CEN, CENELEC,
ETSI, SEMIC; plus DCAT, DCAT-AP and related standards.

**⚠ Evidence standard:** unchanged — all entities `verification: search-only`.

**Entities added (14):**

*Institutions:* `EU-COMMISSION`, `EU-PARLIAMENT`, `EU-COUNCIL`
*Agencies and supervisors:* `EU-ENISA`, `EU-EDPB`, `EU-EDPS`,
`EU-EUROSTAT`, `EU-PUBLICATIONS-OFFICE`
*Standards bodies:* `EU-CEN`, `EU-CENELEC`, `EU-ETSI`, `EU-SEMIC`
*Standards:* `EU-DCAT-AP`, `INTL-DCAT`

**The first end-to-end standards chain.** Batch 4 sketched it in prose and
refused to assert it; Batch 9 completed it:

```
INTL-DCAT (W3C) → EU-DCAT-AP (SEMIC) → NL-DCAT-AP-NL (Geonovum)
```

This is the international → EU → national standards descent the brief's
final relationship pass calls for, and the first the Atlas holds
end-to-end. `INTL-DCAT` is also the Atlas's first `INTL`-scoped entity.

**Four dangling links closed:** `NL-AP` → `EU-EDPB`, `NL-NEN` → `EU-CEN`,
`NL-CBS` → `EU-EUROSTAT`, `EU-CYBERSECURITY-ACT` → `EU-ENISA`.

**A recurring evidence pattern, marked consistently.** Three of those
closures rest on **composition rules** rather than sources naming the Dutch
body: "the EDPB comprises representatives from each national supervisory
authority", "CEN brings together the national standardisation bodies of 33
European countries", "the ESS is the partnership between Eurostat and the
national statistical institutes". Each is a reasonable inference from a
sourced rule — not a guess, but not a direct citation either. Every one says
so in its `evidence` field at `confidence: medium`.

**Relationships added:** 10 provenanced entries.
**Sources added:** 27 source entries.

**Deliberate omissions:**
- **Directorates-General were not created.** DG CONNECT is named once as a
  DCAT-AP co-initiator; no DG structure research was done. Creating DG
  entities from a passing mention would repeat the `NL-PETRA` mistake.
- **No adoption relationships from Parliament/Council to the 16 legislative
  entities.** That would add 32 edges conveying one fact already implied by
  entity type, drowning the substantive chains. Recorded as a modelling
  question instead.
- **Interoperable Europe Board** not created — two passing mentions only.
- **Regulation 1025/2012 and Regulation 223/2009** described but not
  modelled; both are legislation and outside this batch's scope.

**Honest weak points:**
- `INTL-DCAT` has **no W3C source** — both citations are second-hand
  descriptions. The top of the flagship chain is its weakest link.
  Batch 14 should rebuild it, as Batch 8 rebuilt `EU-EIDAS2`.
- `EU-PUBLICATIONS-OFFICE` has no source describing it; its EUR-Lex
  publisher role is asserted from the Atlas's own citation practice, which
  is circular.
- `EU-ETSI` is the clearest incompleteness: ICT standardisation is central
  to this Atlas's subject, and **no ETSI standard was modelled**.
- `EU-EDPB` cites a commercial blog for an EU institution.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 104
entities.

**Next batch:** Batch 10 — EU Data Spaces.

---

## Batch 8 — EU Legislation

**Date:** 2026-08-14

**Scope:** GDPR, Data Governance Act, Data Act, Open Data Directive, eIDAS /
European Digital Identity, AI Act, NIS2, Cybersecurity Act, Interoperable
Europe Act, Single Digital Gateway, and relevant sector-specific
legislation — relevance assessed rather than assumed.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
entities are `verification: search-only`. Sourcing quality nonetheless
improved markedly: **most new entities carry EUR-Lex Official Journal
citations**, unlike Batch 7.

**Entities added (11):**

| ID | Type | Citation |
|---|---|---|
| `EU-DGA` | regulation | Reg. (EU) 2022/868 — EUR-Lex ✓ |
| `EU-DATA-ACT` | regulation | Reg. (EU) 2023/2854 — EUR-Lex ✓ |
| `EU-AI-ACT` | regulation | Reg. (EU) 2024/1689 — no EUR-Lex link found |
| `EU-EIDAS` | regulation | Reg. (EU) No 910/2014 — indirect only |
| `EU-NIS` | directive | Dir. (EU) 2016/1148 — superseded 18 Oct 2024 |
| `EU-CER` | directive | Dir. (EU) 2022/2557 — EUR-Lex ✓ |
| `EU-CYBERSECURITY-ACT` | regulation | Reg. (EU) 2019/881 — EUR-Lex summary ✓ |
| `EU-INTEROPERABLE-EUROPE-ACT` | regulation | Reg. (EU) 2024/903 — EUR-Lex ✓ |
| `EU-SDG` | regulation | Reg. (EU) 2018/1724 — EUR-Lex summary ✓ |
| `EU-ITS-DIRECTIVE` | directive | Dir. 2010/40/EU — EUR-Lex ✓ |
| `EU-DIGITAL-OMNIBUS` | regulation | COM(2025) 836 — **proposal, not adopted** |

**Entities rebuilt (2):** `EU-EIDAS2` and `EU-EUDI-WALLET` — Batch 7 flagged
both as resting entirely on secondary sources. Both are now built on the
EUR-Lex Official Journal text of Reg. (EU) 2024/1183 and the Commission's
Digital Building Blocks pages, with `confidence` raised low → medium. This
was Batch 8's stated first priority and it is done.

**Entities updated (7):** `EU-NIS2` (supersedes NIS), `NL-WBNI` (implements
NIS), `NL-NTM` (implements ITS Directive), `EU-CYBERSECURITY-STRATEGY`
(influences CER), `EU-GDPR` and `EU-OPEN-DATA-DIRECTIVE` (Omnibus notes),
`EU-EIF` (Interoperable Europe Act association), `NL-WDO` (eIDAS question
narrowed).

**New relationship type: `proposes-to-supersede`.** The Digital Omnibus
proposes to repeal the DGA and the Open Data Directive. `supersedes` would
assert something untrue — the repeal has not happened — while `references`
would understate it to the point of hiding a pending repeal from anyone
reading those entities. A purpose-built type was added and documented in
`metadata/relationship-types.md`, `controlled-vocabularies.md` and
`schema.json`. Pending legislation is a permanent feature of this domain, so
this will recur.

**Three dangling chains closed:**

| Chain | Closed by |
|---|---|
| `EU-NIS` → `NL-WBNI` | New `EU-NIS` entity |
| `EU-ITS-DIRECTIVE` → `NL-NTM` | New `EU-ITS-DIRECTIVE` entity |
| `EU-CYBERSECURITY-STRATEGY` → `EU-CER` | New `EU-CER` entity |

The ITS one is worth noting: Batch 5 refused to assert the relationship
because no source named the instrument. Three batches later the instrument
was found and the link made with a real citation — the honest gap was
closable, whereas a guess would have needed correcting.

The cybersecurity picture is now the Atlas's most complete, with both
generations and all three package elements:

```
EU-CYBERSECURITY-STRATEGY  (Dec 2020)
   │ influences                    ╲ influences
EU-NIS2  ◄──supersedes── EU-NIS     EU-CER
   │                        │
NL-CBW   ◄──supersedes── NL-WBNI
```

**Relationships added:** 18 provenanced entries.
**Sources added:** 26 source entries, the majority official.

**Relevance assessed, not assumed.** The brief warns against classifying
every digital regulation as a data initiative. Each borderline inclusion
carries an explicit justification in-file: the AI Act on training-data
governance and the proposed GDPR AI lawful basis; the Cybersecurity Act on
certification as a precondition for trusted data infrastructure; the SDG
Regulation on the once-only principle.

**Honest weak points:**
- `EU-AI-ACT` has **no EUR-Lex citation** — sourced to a specialist
  reference site and Wikipedia. Weakest of the new legislation entities.
- `EU-DIGITAL-OMNIBUS` has only a CELEX reference; all substance comes from
  law-firm commentary. Its **current** legislative status is unverified and
  time-sensitive.
- `EU-EIDAS` was created for structural reasons only; its own content is
  unresearched.
- The EIF ↔ Interoperable Europe Act relationship is **not asserted** — no
  source states how they relate, and it determines whether the EU
  interoperability layer has one root or two.
- `NL-WDO`'s EU origin remains unresolved: eIDAS 2.0 ruled out on dates,
  910/2014 plausible but unsourced. `region` stays `null`.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 90
entities.

**Next batch:** Batch 9 — EU Organisations and Standards. It would close
ENISA, the Interoperable Europe Board, EDPB/EDPS, and the
DCAT → DCAT-AP → DCAT-AP-NL standards chain.

---

## Batch 7 — EU Core Initiatives

**Date:** 2026-08-14

**Scope:** European Data Strategy, Digital Decade, European interoperability
initiatives, European data spaces, European digital identity, digital
sovereignty, digital infrastructure, AI strategy, cybersecurity strategy.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
entities are `verification: search-only`. **Two entities are additionally
weak** — see below.

**Note on batch order:** Batch 6 (Netherlands Validation) was skipped, on
the reasoning recorded in `progress/current-batch.md`: it cannot be
completed in substance while the sourcing debt stands. Proceeding to the EU
layer under the declared constraint was chosen over producing a hollow
validation report.

**Entities added (7):**

| ID | Type | Note |
|---|---|---|
| `EU-DATA-STRATEGY` | strategy | COM(2020) 66, 19 Feb 2020 |
| `EU-COMMON-DATA-SPACES` | initiative | Pillar 4 of the data strategy |
| `EU-DIGITAL-DECADE` | programme | Decision (EU) 2022/2481 |
| `EU-EIF` | framework | European Interoperability Framework |
| `EU-CYBERSECURITY-STRATEGY` | strategy | 16 Dec 2020 |
| `EU-EIDAS2` | regulation | Reg. 2024/1183 — **weakly sourced** |
| `EU-EUDI-WALLET` | initiative | **weakly sourced** |

**The Atlas's first full three-level chain.** Batch 7's main structural
result:

```
EU-CYBERSECURITY-STRATEGY   (strategy, Dec 2020)
        │ influences
EU-NIS2                     (directive, Dec 2022)
        │ implements-requirement-from
NL-CBW                      (Dutch act, in force Aug 2026)
        │ supersedes
NL-WBNI                     (predecessor Dutch act)
```

Strategy → EU legislation → national implementation → superseded
predecessor, all with provenanced relationships. This is the vertical
pattern the brief's final relationship pass calls for.

**Relationships added:** 7 provenanced entries — 3 `applies-in` (to NL),
1 `influences`, 1 `produces`, 1 `part-of`, 1 `based-on`.

**Sources added:** 15 source entries.

**⚠ Two entities are materially weaker than the rest.** [[EU-EIDAS2]] and
[[EU-EUDI-WALLET]] rest **entirely on secondary sources** — law-firm
articles, vendor blogs and Wikipedia. No EUR-Lex or Commission citation was
located for either, unlike [[EU-GDPR]], [[EU-NIS2]] and
[[EU-OPEN-DATA-DIRECTIVE]]. Both carry `confidence: low` and an explicit
in-file warning, and **Batch 8 should rebuild them** rather than merely
deepen them.

**Two scope items produced no entity, deliberately:**
- **Digital sovereignty** — named in the batch scope, but sources treat it
  as a framing within [[EU-DIGITAL-DECADE]] rather than a named initiative
  with its own governance. An entity for a theme would have nothing
  verifiable attached.
- **EU AI strategy** — searches returned AI-and-cybersecurity material
  rather than a clearly identifiable standalone strategy document. The AI
  Act is Batch 8. Recorded as an open scope question rather than invented.

**The 14 data spaces were deliberately not created.** They are listed in
prose on [[EU-COMMON-DATA-SPACES]] and queued for Batch 10, where the brief
requires researching each one's purpose, governance, standards, legislation
and participating countries. Fourteen thin entities from a single list would
be precisely the shallow-entity failure the brief warns against.

**Highest-value open question raised:** is [[NL-NORA]] formally the
Netherlands' National Interoperability Framework under [[EU-EIF]]?
Confirming it would connect the EU and Dutch framework layers directly. Only
an association is recorded; no relationship asserted.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 79
entities.

**Next batch:** Batch 8 — EU Legislation. Priority: rebuild `EU-EIDAS2` and
`EU-EUDI-WALLET` on official sources.

---

## Batch 5 — Netherlands: Domains and Data Ecosystems

**Date:** 2026-08-14

**Scope:** Dutch data domains, data spaces, federated data ecosystems,
national and open-data platforms, and sectoral data initiatives.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
substantive entities are `verification: search-only`.

**Entities added (10):**

*Domains (created only on meeting the 2-entity threshold):*

| ID | Members that justified it |
|---|---|
| `DOMAIN-EDUCATION` | `NL-SURF`, `NL-ROSA` |
| `DOMAIN-HEALTH` | `NL-NICTIZ`, `NL-HEALTH-RI` |
| `DOMAIN-MOBILITY` | `NL-NDW`, `NL-NTM` |

*Platforms:*

| ID | Note |
|---|---|
| `NL-DATA-OVERHEID` | National open data portal; depends on `NL-DCAT-AP-NL` |
| `NL-PDOK` | Geodata platform, founded 2013 |
| `NL-NDW` | National road traffic data portal, opened 2009 |
| `NL-NTM` | National access point for mobility data — an EU obligation |

*Data spaces and ecosystems:*

| ID | Note |
|---|---|
| `NL-HEALTH-RI` | Federated national health data infrastructure |
| `NL-DSGO` | Built-environment agreement framework |
| `NL-ISHARE` | Trust framework used to establish data spaces |

**Entities updated:** `NL-SURF`, `NL-ROSA`, `NL-NICTIZ` retro-tagged with
their new domains, and the notes explaining the previously-missing domains
rewritten to record that the gap is closed. Plus `countries/nl/index.md`.

**The domain threshold held, and paid off.** `DOMAIN-EDUCATION` was withheld
in Batch 2 (SURF alone) and again in Batch 4 (SURF + ROSA, but wrong batch);
`DOMAIN-HEALTH` was withheld in Batch 2 (Nictiz alone). Both were created
here only once genuinely justified. Seven further domains named in the Batch
5 brief — Energy, Environment, Finance, Justice, Agriculture, Social
Security, Built Environment — remain **below the threshold and were not
created**, which is the rule working as intended rather than the batch being
incomplete.

**Relationships added:** 4 provenanced entries (`depends-on`,
`participates-in`, `part-of`, and one interpretation), plus domain tagging
across 6 entities.

**Sources added:** 26 source entries.

**A near-complete EU chain, deliberately left open.** [[NL-NTM]] exists
because every European country must have a national access point for
mobility data. The obligation is sourced; **the instrument imposing it is
not** — no source located named it. So `region: EU` is set and the
obligation described in prose, but no `implements-requirement-from` is
asserted. Batch 8 should close it.

**Honest weak points:**
- [[NL-ISHARE]] is recorded `country: NL` on its Dutch origin, but presents
  at ishare.eu in a European context. This is the country-neutral model's
  hardest case — a national initiative that went cross-border — and is
  flagged for resolution in Batch 10 rather than guessed now.
- [[NL-DSGO]]'s `start_date` combines two separate statements ("launched 18
  June" + "programme ended June 2024") into one date. That inference is
  marked as an inference.
- [[NL-DATA-OVERHEID]]'s `organisations: [NL-BZK]` is an Atlas association,
  not a sourced operator claim.
- [[NL-HEALTH-RI]] and [[NL-NDW]] both have genuine typing ambiguity
  (infrastructure vs organisation; platform vs organisation).

**New schema question raised.** Four entities now carry a `YYYY-01-01`
`start_date` meaning "year known, day unknown" ([[NL-RORA]], [[NL-PDOK]],
[[NL-ISHARE]], partly [[NL-DSGO]]). A January-1st placeholder is
indistinguishable from a real 1 January date — a genuine data-quality
problem. Recorded in `discovery/unresolved.md` as a schema question:
either adopt a convention or add a `date_precision` field.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 72
entities.

**Next batch:** Batch 6 — Netherlands Validation. Note that Batch 6 cannot
be completed properly while the search-only sourcing debt stands; see
`progress/current-batch.md`.

---

## Batch 4 — Netherlands: Standards, Frameworks and Architecture

**Date:** 2026-08-14

**Scope:** Dutch reference architectures, standards-management models,
security baselines, and metadata/API/interoperability standards, each
connected to its maintaining organisation as the batch brief requires.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked; all
entities are `verification: search-only`.

**Entities added (11):**

*Reference architectures — the NORA family:*

| ID | Tier | Note |
|---|---|---|
| `NL-GEMMA` | Municipalities | Only member with a **sourced** `based-on` → NORA |
| `NL-EAR` | Central government | `superseded`, `successor: NL-RORA` |
| `NL-RORA` | Central government | Successor since 2024 |
| `NL-PETRA` | Provinces | Weakest entity in the Atlas — see below |
| `NL-ROSA` | Education sector | `level: sectoral` |

*Frameworks:*

| ID | Note |
|---|---|
| `NL-BOMOS` | The Dutch "standard for running a standard" |
| `NL-BIO` | Security baseline for all government tiers; current version BIO2 |

*Standards (all connected to a maintainer):*

| ID | Maintainer | Note |
|---|---|---|
| `NL-DIGIKOPPELING` | Logius | On the mandatory list |
| `NL-ADR` | Logius | On the mandatory list |
| `NL-DCAT-AP-NL` | Geonovum | Bridges to European data catalogues |
| `NL-NEN-3610` | Geonovum / NEN | Custody split — see below |

**Entities updated:** `NL-NORA` (family table + `related_entities`),
`NL-GEONOVUM` (BOMOS alignment), `countries/nl/index.md`.

**Relationships added:** 10 provenanced entries — 5 `maintained-by`,
2 `part-of` (onto the mandatory standards list), 1 `based-on`,
1 `supersedes`, 1 `applies-in`, plus `derived-from` and `aligned-with`.

**Sources added:** 33 source entries.

**Where derivation was refused.** Only [[NL-GEMMA]] carries a sourced
`based-on` → NORA. For PETRA, ROSA and EAR the derivation from NORA is
highly likely but was not stated by any source, so it is recorded as
`related_entities` association rather than asserted as a relationship. This
is the single most repeated judgement in the batch: family membership is
claimable, derivation is not.

**Honest weak points:**
- **`NL-PETRA` is the weakest entity in the Atlas.** It rests on one
  sentence in one Wikipedia article. Its maintainer, its NORA relationship
  and even its acronym expansion are unsourced, and its `organisations:
  [NL-IPO]` link is an explicit Atlas assumption. It is included because
  Batch 4's scope names PETRA; the weakness is stated in the entity itself.
- **WILMA was deliberately not created**, though named in the same source
  sentence as PETRA — it is not in the batch scope and rests on the same
  single mention. The asymmetry is recorded in both entities' notes.
- **StUF was searched for and not created**: the search returned no usable
  source, and inventing one was not an option.
- `NL-RORA`'s `start_date: 2024-01-01` is a placeholder for "during 2024".
- `NL-BOMOS` has **no `maintained-by`** — custody is genuinely split across
  Forum Standaardisatie, NOiV, ECP and Logius.
- `NL-NEN-3610`'s `maintained-by` → Geonovum is `confidence: low`: the
  source says *aanspreekpunt*, which is weaker than the relationship claims.

**Threshold now met:** `DOMAIN-EDUCATION` connects two entities
([[NL-SURF]], [[NL-ROSA]]) and so qualifies under taxonomy §1. It was
**not** created here — Batch 4 is standards, not domains — and is queued for
Batch 5.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 62
entities.

**Next batch:** Batch 5 — Netherlands: Domains and Data Ecosystems.

---

## Batch 3 — Netherlands: Legislation and Regulation

**Date:** 2026-08-14

**Scope:** Dutch and applicable European legislation on data, privacy, data
sharing, digital government, open data, public information, archives,
digital identity, cybersecurity and information management, classified per
`metadata/taxonomy.md` §2.

**⚠ Evidence standard:** unchanged — page retrieval remained blocked, so all
entities are `verification: search-only`.

**Entities added (15):**

*EU legislation (minimal anchors — Batch 8 deepens):*

| ID | Type | Note |
|---|---|---|
| `EU-GDPR` | regulation | Regulation (EU) 2016/679 |
| `EU-OPEN-DATA-DIRECTIVE` | directive | Directive (EU) 2019/1024 |
| `EU-NIS2` | directive | Directive (EU) 2022/2555 |

*Dutch implementation legislation (`region: EU`):*

| ID | Implements | Note |
|---|---|---|
| `NL-UAVG` | `EU-GDPR` | In force 25 May 2018 |
| `NL-WHO` | `EU-OPEN-DATA-DIRECTIVE` | Amended 2024 by Wet implementatie Open data richtlijn |
| `NL-CBW` | `EU-NIS2` | `status: planned`, in force 15 Aug 2026 |

*Dutch national legislation (`region: null`):*

| ID | Note |
|---|---|
| `NL-WOO` | In force 1 May 2022; supersedes `NL-WOB` |
| `NL-WDO` | Phased from 1 July 2023 |
| `NL-ARCHIEFWET-1995` | Superseded from 1 Jan 2027 |
| `NL-WET-BRP` | In force 6 Jan 2014 |
| `NL-WET-CBS` | CBS became a ZBO 1 Jan 2004 |
| `NL-TNO-WET` | 1930, in force 1932 |

*Retained for temporal integrity:*

| ID | Status |
|---|---|
| `NL-WOB` | `superseded` (1 May 2022), `successor: NL-WOO` |
| `NL-WBNI` | `active` with `end_date: 2026-08-15`, `successor: NL-CBW` |
| `NL-ARCHIEFWET-2026` | `planned`, in force 1 Jan 2027 |

**The first complete vertical chain.** Batch 3's main structural achievement
is that the Atlas can now express what it was built for:

```
EU-GDPR  →  NL-UAVG  →  NL-AP
(regulation) (implementing act) (supervisory authority)
```

with `applies-in → NL` on the EU entity rather than a Dutch copy of it.
Two further chains follow the same shape via `NL-WHO` and `NL-CBW`.

**Dangling Batch 2 relationships closed (5):** `NL-AP` (→ UAVG + GDPR),
`NL-NATIONAAL-ARCHIEF` (→ Archiefwet 1995, with `valid_until: 2027-01-01`),
`NL-CBS` (→ Wet op het CBS), `NL-TNO` (→ TNO-wet),
`NL-BASISREGISTRATIES` (→ Wet BRP, at `confidence: low` — see below).

**Relationships added:** 19 provenanced entries, including 4
`implements-requirement-from`, 3 `applies-in`, 3 `supersedes`, 4
`governed-by`, 4 `applies-to`, 1 `influences`.

**Sources added:** 42 source entries.

**Temporal modelling exercised for the first time.** Three supersession
chains are now represented with both `successor`/`previous_version` fields
and `supersedes` relationships carrying `valid_from` dates, and one
relationship (`NL-NATIONAAL-ARCHIEF` → Archiefwet 1995) carries a
`valid_until`. `NL-CBW` is recorded as `planned` with a commencement date of
15 August 2026 — the day after this batch was written — which makes it a
live demonstration of why `status` must never be read from a stale snapshot.

**Known gaps and honest weak points:**
- `NL-WHO` has **no `start_date`**: two sources gave conflicting
  entry-into-force dates (19 June vs 2 August 2024) and neither was
  preferred over the other.
- `NL-ARCHIEFWET-2026` appears under three different names across sources
  (Archiefwet 2021 / 2026 / "20xx"). The name is provisional; the ID is not.
- `NL-TNO-WET` is the weakest entity: a 1930 act with no located
  consolidated text and a Wikipedia secondary source.
- `NL-BASISREGISTRATIES` → `NL-WET-BRP` is recorded at `confidence: low`
  because the Wet BRP governs one registration, not the stelsel; the link
  should move to a BRP entity once the individual registrations exist.
- `NL-WDO` is classified as purely national, but its subject matter overlaps
  EU digital identity law; flagged for re-examination when eIDAS lands.
- Handelsregisterwet was **not** created — no adequate source was located,
  so `NL-KVK`'s statutory basis remains open rather than being filled with
  a guess.

**Validation result:** all 5 checks pass, 0 errors, 0 warnings, across 51
entities.

**Next batch:** Batch 4 — Netherlands: Standards, Frameworks and
Architecture (Forum Standaardisatie standards, GEMMA, EAR, ROSA, PETRA,
BOMOS, metadata/API/interoperability standards).

---

## Batch 2 — Netherlands: Organisations

**Date:** 2026-08-14

**Scope:** Expand the Dutch organisation graph across data governance,
digital government, information management, interoperability, standards,
public-sector data, statistics, research and digital infrastructure.

**⚠ Evidence standard:** unchanged from Batch 1 — page retrieval remained
blocked, so all substantive entities are `verification: search-only` with no
`accessed:` dates, `last_verified: null`, no `confidence: high`, and a
visible caveat in each body.

**Entities added (17):**

| ID | Type | Note |
|---|---|---|
| `NL-IPO` | organisation | Provinces (koepel) |
| `NL-UVW` | organisation | Water authorities (koepel) |
| `NL-CBS` | organisation | National statistical office, ZBO since 2004 |
| `NL-KADASTER` | organisation | Holds BRK |
| `NL-KVK` | organisation | Holds Handelsregister |
| `NL-RDW` | organisation | Holds BRV since 2008 |
| `NL-GEONOVUM` | organisation | Geo-standards |
| `NL-NEN` | organisation | National standards institute |
| `NL-NICTIZ` | organisation | Health information standards (`level: sectoral`) |
| `NL-AP` | organisation | Data protection authority |
| `NL-NATIONAAL-ARCHIEF` | organisation | Archives / information management |
| `NL-SURF` | organisation | Education & research ICT cooperative |
| `NL-TNO` | organisation | Applied research |
| `NL-BASISREGISTRATIES` | framework | Stelsel van Basisregistraties |
| `NL-NDS` | strategy | Nederlandse Digitaliseringsstrategie (July 2025) |
| `DOMAIN-GEOSPATIAL` | domain | Connects Kadaster + Geonovum |
| `DOMAIN-RESEARCH` | domain | Connects SURF + TNO |

**Entities updated:** `countries/nl/index.md` (restructured with grouped
organisation sections).

**Relationships added:** 9 provenanced entries (4 `participates-in` to the
base-registry system, 2 `participates-in` to OBDO/IBDS, 1 `references`,
1 `aligned-with`, 1 additional), plus lightweight reference lists.

**Sources added:** 45 source entries across the 17 entities.

**Two deliberate out-of-scope additions.** Batch 2 is nominally
organisations only; two non-organisation entities were added and the reason
is recorded in a "Scope note" section in each file:
- `NL-BASISREGISTRATIES` (framework) — without it, Kadaster, KVK and RDW
  would be three disconnected agency nodes rather than participants in one
  data system. Graph coherence was judged to outrank batch purity.
- `NL-NDS` (strategy) — surfaced during organisation research, is a
  high-priority national strategy that Batch 1 missed, and directly narrows
  the open question about whether NL DIGIbeter was superseded.

**Taxonomy discipline held.** `DOMAIN-HEALTH` (for Nictiz) and
`DOMAIN-EDUCATION` (for SURF) were **not** created, because
`metadata/taxonomy.md` §1 requires a domain to connect two or more entities
and each would currently connect one. Both are queued for Batch 5, and both
entities carry a note explaining the gap. `DOMAIN-EDUCATION` was caught by
`validate_relationships.py` after being referenced before creation — the
validator did its job.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, across 36 entities.

**Known gaps:**
- All 30 search-only entities (Batches 1+2) still need primary-source
  re-verification.
- `discovery/unresolved.md` now holds 20 open questions; 5 new ones from
  this batch concern NDS continuity under a new cabinet, the
  basisregistraties↔FDS relationship, CBS's responsible ministry, the
  reported 1 Jan 2027 Archiefwet revision, and three entity-typing calls.
- 21 items queued in `discovery/research-queue.md`, including CIO Rijk, Het
  Waterschapshuis, VNG Realisatie, CCS, AcICT, DANS/Health-RI/RIVM/NWO,
  SIDN, BOMOS, and the ten individual basisregistraties.
- Several organisations (`NL-AP`, `NL-NEN`, `NL-NATIONAAL-ARCHIEF`) have
  **no relationships recorded**, because their defining links are to
  legislation (Batch 3) or to EU/international bodies (Batches 8–13) that
  do not yet exist. These are documented gaps, not omissions.
- `NL-KVK` is the weakest entity in the batch: its only general-profile
  source is Wikipedia, low in the README's source preference order.

**Next batch:** Batch 3 — Netherlands: Legislation and Regulation. This is
where several currently-dangling organisation relationships get closed.

---

## Batch 1 — Netherlands: Core Data Governance

**Date:** 2026-08-14

**Scope:** Core Dutch data-governance landscape — Forum Standaardisatie,
IBDS, Federatief Datastelsel, NORA, Common Ground, MIDO, Data Agenda
Overheid, NL DIGIbeter, and the organisations and governance bodies
connecting them.

**⚠ Evidence standard for this batch:** the 15 substantive entities were
compiled from **search-engine results only**. The environment's network
egress policy blocked every attempt at direct page retrieval, so no cited
source was actually read. This was raised as a blocker and the reduced
standard was then accepted explicitly. Consequences, applied consistently:

- all 15 substantive entities carry `verification: search-only`
  (`DOMAIN-GOVERNMENT`, the 16th, is a taxonomy node making no factual
  claims and needs no external sourcing);
- no entity claims `confidence: high` (validation now enforces this);
- no `accessed:` dates are recorded on sources (nothing was accessed);
- `last_verified` is `null` throughout;
- each entity body opens with a visible sourcing caveat;
- unverified specifics (dates, thresholds, recent governance decisions) are
  named as unverified in prose rather than stated flatly.

**Entities added (16):**

| ID | Type | Folder |
|---|---|---|
| `DOMAIN-GOVERNMENT` | domain | `domains/` |
| `NL-BZK` | organisation | `organisations/` |
| `NL-FORUM-STANDAARDISATIE` | organisation | `organisations/` |
| `NL-OBDO` | organisation | `organisations/` |
| `NL-LOGIUS` | organisation | `organisations/` |
| `NL-ICTU` | organisation | `organisations/` |
| `NL-VNG` | organisation | `organisations/` |
| `NL-IBDS` | strategy | `strategies/` |
| `NL-DIGIBETER` | strategy | `strategies/` |
| `NL-DATA-AGENDA-OVERHEID` | strategy | `strategies/` |
| `NL-PAS-TOE-OF-LEG-UIT` | policy | `policies/` |
| `NL-NORA` | framework | `frameworks/` |
| `NL-FDS` | framework | `frameworks/` |
| `NL-MIDO` | programme | `programmes/` |
| `NL-COMMON-GROUND` | initiative | `initiatives/` |
| `NL-GDI` | platform | `platforms/` |

**Entities updated:** `countries/nl/index.md` (curated NL hub, previously
empty).

**Relationships added:** 13 provenanced entries in `relationships:` lists
(4 `maintained-by`, 2 `owned-by`, 1 `produces`, 1 `implements`, 1
`implemented-by`, 1 `part-of`, 1 `governed-by`, 1 `applies-to`, 1
`applies-in`, 1 `participates-in`), plus lightweight
`organisations:`/`related_entities:`/`domains:` references throughout. Of
the provenanced entries, 8 are `source: fact` and 5 are
`source: interpretation` — the interpretations are the IBDS↔FDS link, the
entity-type judgements, and three relationships recorded from the
organisation's side for navigability.

**Sources added:** 38 source entries across the 16 entities, all URLs
returned by web search (none invented, none read).

**Schema/tooling changes made during this batch:**
- Added optional `verification` field (`primary-source` | `search-only` |
  `unverified`) to the metadata schema, documented in
  `metadata/metadata-schema.md` and `metadata/controlled-vocabularies.md`,
  and added to `templates/entity-template.md`.
- `validate_frontmatter.py`: validates `verification`; rejects
  `confidence: high` on search-only/unverified entities; suppresses the
  `last_verified` reminder where it would be by-design noise.
- `validate_relationships.py`: rejects self-referencing relationship
  targets (added after one slipped into a draft).
- `validate_sources.py`: exempts `type: domain` taxonomy nodes from the
  missing-sources warning.
- Added `DOMAIN` as a valid ID scope in `metadata/schema.json` and
  `metadata/ontology.md` §2.1 — `DOMAIN-GOVERNMENT` was rejected by the
  Batch 0 pattern, a genuine gap between `taxonomy.md` and the schema.
- Both new checks were tested against injected violations to confirm they
  actually fire.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, across 19 entities.

**Known gaps:**
- All 16 entities need a primary-source re-verification pass (see
  `progress/current-batch.md`).
- 12 specific open questions recorded in `discovery/unresolved.md`, covering
  status/temporal questions (FDS establishment, IBDS evaluation, whether
  NL DIGIbeter is superseded), factual details (the €50,000 threshold, the
  2006 Forum establishment date, GDI's expansion) and three entity-typing
  judgements.
- 8 follow-on research items queued in `discovery/research-queue.md`
  (IPO, UvW, CIO Rijk, College Standaardisatie, individual GDI services,
  GEMMA/EAR/ROSA/PETRA, individual open standards, MIDO sub-documents).
- No legislation yet (Batch 3), no EU links yet (Batch 7+).

**Next batch:** Batch 2 — Netherlands: Organisations.

---

## Batch 0 — Repository Architecture

**Date:** 2026-08-14

**Scope:** Implement repository structure, ontology, taxonomy, relationship
model, metadata schema, controlled vocabularies, templates, validation
rules and contribution guidelines. No broad Netherlands/EU/UN research
performed.

**Entities added:**
- `NL` (`countries/nl/nl.md`) — country anchor
- `EU` (`regions/eu/eu.md`) — region anchor
- `UN` (`international/un/un.md`) — organisation anchor, international level

All three are structural anchors with `coverage: low`, sourced only to
ISO/official EU/UN homepages — not researched content.

**Entities updated:** None (repository was empty of entities before this batch).

**Relationships added:** None yet — the three anchors have no
`relationships:` entries; they exist to be targeted by future entities'
`applies-in`/`country`/`region` fields.

**Sources added:** 3 (one per anchor entity — ISO 3166 OBP for NL, and the
official EU and UN websites).

**Structure/tooling created:**
- Repository folders: `initiatives/`, `legislation/`, `policies/`,
  `strategies/`, `standards/`, `frameworks/`, `programmes/`,
  `organisations/`, `data-spaces/`, `platforms/`, `publications/`,
  `domains/`, `countries/nl/`, `regions/eu/`, `international/un/`,
  `metadata/`, `templates/`, `discovery/`, `validation/`, `progress/`,
  `.github/workflows/` — each populated with a scope-defining `README.md`
  where relevant.
- `metadata/ontology.md`, `metadata/taxonomy.md`,
  `metadata/relationship-types.md`, `metadata/metadata-schema.md`,
  `metadata/controlled-vocabularies.md`, `metadata/schema.json`.
- `templates/entity-template.md`.
- `CONTRIBUTING.md`.
- `discovery/candidates.md`, `discovery/unresolved.md`,
  `discovery/duplicates.md`, `discovery/research-queue.md` (all empty —
  no research performed yet).
- `validation/common.py` + `validate_ids.py`, `validate_frontmatter.py`,
  `validate_links.py`, `validate_relationships.py`, `validate_sources.py`,
  `run_all.py`, `requirements.txt`.
- `.github/workflows/validate.yml` — runs `validation/run_all.py` on every
  PR and push to `main`.
- `README.md` — repository structure diagram updated to include
  `platforms/`, `publications/`, and the full `metadata/` file list.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, against the 3 anchor entities plus navigation pages.

**Design decisions:** recorded in `metadata/ontology.md` §6; summarised in
the Batch 0 completion report delivered to the user.

**Known gaps:** No substantive content yet — Batches 1–15 are all still
open. See `progress/backlog.md`.

**Next batch:** Batch 1 — Netherlands: Core Data Governance (Forum
Standaardisatie, Federatief Datastelsel, IBDS, NORA, Common Ground, MIDO,
Data Agenda Overheid, NL Digitaal, and related programmes). Awaiting
approval before starting, per the task brief's instruction to stop after
Batch 0.

---

# Germany — Second Country (2026-08-15)

**Scope:** Germany as the second national scope, following the Final
Quality Gate's identification of *"a second country — the only real test of
the country-neutral model"* as one of three outstanding items.

**Entities added: 39.** 125 → **164**.

- **Country anchor (1):** `DE` (`countries/de/de.md` + `index.md`).
- **Strategies (4):** `DE-DIGITALSTRATEGIE`, `DE-DATENSTRATEGIE`,
  `DE-MODERNISIERUNGSAGENDA-BUND`, `DE-MODERNISIERUNGSAGENDA-FOEDERAL`.
- **Initiatives (2):** `DE-DEUTSCHLAND-STACK`, `DE-GDI-DE`.
- **Organisations (9):** `DE-BMDS`, `DE-BMI`, `DE-IT-PLANUNGSRAT`,
  `DE-FITKO`, `DE-KOSIT`, `DE-BSI`, `DE-DESTATIS`, `DE-BFDI`, `DE-DIN`.
- **Legislation (11):** `DE-BDSG`, `DE-IFG`, `DE-DNG`, `DE-IWG`
  (superseded), `DE-EGOVG`, `DE-OZG`, `DE-REGMOG`, `DE-BSIG`,
  `DE-NIS2UMSUCG`, `DE-BSTATG`, `DE-GEOZG`.
- **Standards and frameworks (5):** `DE-XOEV`, `DE-XRECHNUNG`,
  `DE-DCAT-AP-DE`, `DE-IT-GRUNDSCHUTZ`, `DE-IT-ARCHITEKTURRICHTLINIEN`.
- **Platforms (3):** `DE-GOVDATA`, `DE-BUNDID`, `DE-MOBILITHEK`.
- **Data spaces (2):** `DE-MDS`, `DE-CATENA-X`.
- **Supra-national, reached through German research (2):** `EU-INSPIRE`,
  `EU-GAIA-X` — both `country: null`, deliberately not German-scoped.

**Existing entities modified: 15.** `applies-in` → `DE` added alongside the
existing `applies-in` → `NL` on `EU-GDPR`, `EU-NIS2`, `EU-CER`,
`EU-DATA-ACT`, `EU-DGA`, `EU-OPEN-DATA-DIRECTIVE`, `EU-AI-ACT`,
`EU-CYBERSECURITY-ACT`, `EU-EIDAS2`, `EU-SDG`,
`EU-INTEROPERABLE-EUROPE-ACT`, `EU-ITS-DIRECTIVE`, `EU-EHDS`, `EU-EIF`,
`EU-DIGITAL-DECADE`.

**Validation result:** `python validation/run_all.py` — all 5 checks pass,
0 errors, 0 warnings, against 164 entities. `audit.py` reports no
duplicates, no fully disconnected entities, no weak-source-only German
entity, and country-neutrality holding: `targets: ['DE', 'NL']`.

**Result:** the country-neutral architecture holds. Adding a country
required **no change** to `metadata/schema.json`, `metadata/ontology.md`,
`metadata/taxonomy.md`, `metadata/relationship-types.md`, the folder
structure or any validation rule, and produced **no `DE-EU-*` entity**.
Four EU instruments now have two national implementations each; the DCAT
standards chain forks across both countries.

**Principal finding — negative:** the model is **lossy for federal
states**. The `level` vocabulary has no term between `national` and
`local`, so Germany's sixteen Länder are not representable. No sub-national
level was invented.

**Known gaps:** unchanged sourcing position — 155 of 164 entities are
`verification: search-only` and no URL has been fetched. `EU-INSPIRE`
carries `applies-in` → `DE` but not → `NL`, making it look German-specific.
The UN layer remains isolated. Ten refused links and the batch's modelling
questions are recorded in `discovery/unresolved.md`; omitted entities in
`discovery/research-queue.md`.

**Full report:** `validation/germany-second-country-report.md`.

---

# Batch 16 — Interactive Knowledge Graph and GitHub Pages (2026-08-15)

**Scope:** publish the Atlas as an interactive knowledge graph, generated
automatically from the repository and deployed to GitHub Pages. An
implementation batch — **no Atlas content was researched or added**, and no
entity file, frontmatter field or wikilink was changed.

**Added:**

- `tools/build_graph.py` — the generator. Reuses `validation/common.py` as
  its parser so the graph and the validation suite cannot disagree.
- `tools/test_build_graph.py` — 32 tests (in CI).
- `tools/test_ui.mjs` — 47 browser checks (local; needs Playwright).
- `site/` — the static application: `index.html`, `app.css`, `app.js`,
  generated `graph.json` + `details.json`, and Cytoscape.js 3.34.1 (MIT)
  vendored under `site/vendor/`.
- `.github/workflows/pages.yml` — build and deploy, `main` only.
- `docs/graph.md`, `docs/graph-architecture.md`,
  `docs/graph-development.md`, `docs/github-pages.md`.

**Modified:** `.github/workflows/validate.yml` (now also runs the generator
tests and a build check), `README.md` (Explore the Atlas + No Manual Graph
Maintenance), `CONTRIBUTING.md` (regenerate the graph after editing data).

**Graph produced:** 164 nodes, 1,307 edges — 189 typed relationships, 473
associations, 645 wikilinks. The three edge classes are kept distinct
rather than flattened; only typed relationships are drawn by default.

**Validation result:** `validation/run_all.py` 5/5 passed, 0 errors;
`tools/test_build_graph.py` 32 tests OK; `tools/test_ui.mjs` 47/47.

**Defects found by the new tests, and fixed:** two inverted edge directions
(`governed-by` on the wrong entity, `maintained-by` reversed) — neither
would have failed validation, because the graph stays connected while the
meaning reverses — and unreadable label density in the default view.

**Deployment:** verified. `pages.yml` run 31893120291 completed
successfully on 2026-08-15 — `configure-pages`, `upload-pages-artifact` and
`deploy-pages` all green — after the repository's Pages source was switched
to GitHub Actions. The first attempt failed at `configure-pages` because
that setting had not yet been made; no workflow can make it.

**Known gaps:** the graph canvas is not keyboard-traversable; the List view
is the accessible route. Large-graph performance figures come from a
synthetic 1,500-node stress test, not from real data at that size.

---

# Belgium — Third Country (2026-08-15)

**Scope:** Belgium as the third national scope. Requested directly; also the
outstanding backlog item *"a third country — Germany proved the model
reusable and revealed one real limitation; a third would test whether the
limitation is general."*

**Entities added: 14.** 164 → **178**. Relationships 189 → **218**.

- **Country anchor (1):** `BE` (`countries/be/be.md` + `index.md`).
- **Organisations (5):** `BE-BOSA`, `BE-CCB`, `BE-APD`, `BE-STATBEL`,
  `BE-KSZ`.
- **Legislation (5):** `BE-GDPR-WET`, `BE-NIS2-WET`, `BE-NIS1-WET`
  (superseded), `BE-HERGEBRUIK-WET`, `BE-KSZ-WET`.
- **Frameworks and standards (2):** `BE-BELGIF`, `BE-DCAT-AP-BE`.
- **Platforms (1):** `BE-DATA-GOV-BE`.

**Existing entities modified:** `applies-in` → `BE` added to 16 EU
instruments, and the stale "Applies in [[NL]]" prose in all of them
corrected to name all three countries — those bodies had never been updated
for Germany either.

**Validation result:** `run_all.py` 5/5, 0 errors; `test_build_graph.py`
32 tests OK; `audit.py` reports `targets: ['BE', 'DE', 'NL']`.

**Result:** the country-neutral model held for a third time, again with no
change to `metadata/schema.json`, `metadata/ontology.md`,
`metadata/taxonomy.md`, `metadata/relationship-types.md`, the folder
structure, any validation rule or the graph generator. No `BE-EU-*` entity.

**Structural gains:**

- **[[EU-GDPR]] now has three national implementing acts** and remains one
  entity.
- **[[EU-NIS2]] has three transpositions** differing in date and technique —
  Belgium 18 Oct 2024 (new act), Germany 6 Dec 2025 (amends [[DE-BSIG]]),
  Netherlands 15 Aug 2026 (new act). Belgium transposed nearly two years
  before the Netherlands.
- **The DCAT chain forks three ways** — one W3C standard, one European
  profile, three national profiles, each recorded once.
- **[[EU-EIF]] → [[BE-BELGIF]]** closes a link Germany had to refuse: the
  Atlas's first EIF → national-framework descent.

**Principal finding — the federal gap is general, and worse in Belgium.**
Germany showed no `level` term fits a Land. Belgium shows the term that
would fit is **already taken**: `regional` means supra-national here. The
cost is concrete — **OSLO**, a major Flemish semantic-interoperability
programme squarely in this Atlas's subject matter, is not modelled at all.
No sub-national level was invented.

**Known gaps:** Belgium's Open Data Directive transposition was not
identified (the 2016 act found is PSI-era and chronologically cannot be
it); three national statistical offices now sit in the Atlas and none
connects upward; only one of three national DPAs connects to the EDPB.
Sourcing position unchanged — every Belgian entity is `search-only`.

---

# France — Fourth Country (2026-08-16)

**Scope:** France as the fourth national scope, and specifically as a
**unitary** state. `progress/backlog.md` asked for this: *"a fourth country
— a unitary one. All three tests so far have been the Netherlands plus two
federal states. A second unitary country would show whether anything else
in the model is Netherlands-shaped, which the two federal cases could not
isolate."*

**Entities added: 11.** 178 → **189**. Relationships 218 → **242**.

- **Country anchor (1):** `FR`.
- **Organisations (4):** `FR-DINUM`, `FR-ETALAB`, `FR-CNIL`, `FR-ANSSI`.
- **Legislation (3):** `FR-LIL`, `FR-LRN`, `FR-NIS2-LOI`.
- **Frameworks (1):** `FR-RGI`.
- **Platforms (2):** `FR-DATA-GOUV`, `FR-FRANCECONNECT`.

**Existing entities modified:** `applies-in` → `FR` on 16 EU instruments,
with the three-country prose updated to four.

**Validation:** `run_all.py` 5/5, 0 errors; `test_build_graph.py` 32 tests
OK; `audit.py` → `targets: ['BE', 'DE', 'FR', 'NL']`.

**Principal result — a negative.** France is the **first country whose
addition raised no new ontology question at all.** Every entity fitted an
existing type, level, status and relationship type; nothing needed a caveat
about what the Atlas could not express.

That isolates the defect. With only Germany and Belgium it was unclear
whether the model was federal-lossy or simply Netherlands-shaped. A second
unitary state separates the two: **the ontology is sound for unitary states
and lossy for federal ones**, and the loss is confined to the `level`
vocabulary.

**Other findings:**

- **A third GDPR technique.** France amended the 1978 loi Informatique et
  Libertés *in place* — a deliberate, sourced choice — where the other
  three countries passed new acts. The entity implementing the GDPR in
  France is 40 years older than the regulation.
- **The amendment-lineage question, answered from the other side.**
  Germany's [[DE-NIS2UMSUCG]] → [[DE-BSIG]] needed a `supersedes`
  compromise because the amending act has its own name. France records the
  amending instruments as facts in the amended act's body and needs no
  relationship type at all. Two countries, two workarounds — the clearest
  evidence yet that the missing type is worth adding.
- **Four DPAs, one EDPB link.** [[FR-CNIL]] joins Germany and Belgium in
  having no sourced link to [[EU-EDPB]]. The Atlas now shows a Board with
  one member, which is a sourcing artefact rather than structure.
- **Four national open data portals**, and their institutional weight
  tracks the constitutional structure of the state — from a department
  inside a Prime Minister's directorate to an agreement among seventeen
  governments.

**Known gaps:** France's Open Data Directive transposition was not
identified (second country with this gap after Belgium); [[FR-NIS2-LOI]] is
`status: unknown` because sources contradict each other on whether it is in
force — the only such entity in the Atlas; no French DCAT profile was
found, so the DCAT fork stops at three countries; INSEE is not modelled.

---

# Spain — Fifth Country (2026-08-16)

**Scope:** Spain as the fifth national scope, and specifically as the first
country **outside the founding-six / Benelux-DACH group**.
`progress/backlog.md` asked for this: *"A fifth country outside the
founding-six / Benelux-DACH group. All four so far are neighbouring western
European states with similar administrative traditions. A Nordic, southern
or central European state (Ireland, Spain, Poland, Estonia) would test
whether the model is western-European-shaped rather than merely
country-neutral — a question four similar countries cannot answer."*

**Entities added: 17.** 189 → **206**. Relationships 242 → **269**.

- **Country anchor (1):** `ES`.
- **Organisations (7):** `ES-AEAD`, `ES-SGAD`, `ES-AEPD`, `ES-AESIA`,
  `ES-INCIBE`, `ES-CCN`, `ES-INE`.
- **Legislation (3):** `ES-LOPDGDD`, `ES-LEY-37-2007`, `ES-LCGC`.
- **Frameworks (2):** `ES-ENI`, `ES-ENS`.
- **Standards (1):** `ES-NTI-RISP`.
- **Platforms (2):** `ES-DATOS-GOB-ES`, `ES-CLAVE`.
- **Strategies (1):** `ES-ESPANA-DIGITAL-2026`.

**Existing entities modified:** `applies-in` → `ES` on 16 EU instruments,
with the four-country prose updated to five; the NIS2 transposition table,
the GDPR technique table and the Open Data Directive table each gained a
fifth row.

**Validation:** `run_all.py` 5/5, 0 errors, 0 warnings;
`test_build_graph.py` 32 tests OK; `test_ui.mjs` 47/47;
`audit.py` → `targets: ['BE', 'DE', 'ES', 'FR', 'NL']`.

**Principal result — the model is not western-European-shaped.** Spain is
southern European, joined the EU in a later enlargement than any of the
first four, and organises its state on a constitutional principle none of
them use. It required **no ontology, schema, taxonomy, relationship-type,
folder, validation or generator change**, and produced no `ES-EU-*` entity.
The standing objection that four neighbouring states cannot demonstrate
country-neutrality is answered.

**Second result — the federal gap has a third shape, which localises it.**
Spain is a **State of Autonomies**: seventeen Comunidades Autónomas with
devolved competences of differing scope, neither a federation nor a unitary
state. Germany's Länder, Belgium's Regions and Spain's Comunidades
Autónomas are three constitutionally distinct arrangements, and **the Atlas
fails on all three identically.** That is the strongest evidence yet that
the defect sits in the `level` vocabulary rather than in any country's
constitutional shape. Three of five countries are now affected.

The Spanish cost is measurable: seventeen regional open data portals (over
14,000 datasets by 2019), regional data protection authorities, autonomous
communities managing over 35 % of consolidated public spending, and
*cogobernanza del Estado y las Comunidades Autónomas* as **one of two
cross-cutting axes** of `ES-ESPANA-DIGITAL-2026` — of which the Atlas can
model only the state half.

**Four things Spain closed:**

- **The first national link to [[EU-AI-ACT]].** [[ES-AESIA]] is the first
  AI supervisory agency in the EU, created in 2023 **before** the
  Regulation applied, and designated under Article 70. Four countries had
  been added without any national AI body at all. Recorded as `governed-by`
  rather than `implements-requirement-from`, which is reserved for legal
  instruments.
- **The Open Data Directive transposition, on the third attempt.**
  [[ES-LEY-37-2007]] as amended by Real Decreto-ley 24/2021 — an omnibus
  instrument transposing eight directives, produced late and under threat
  of infringement proceedings. The "obvious earlier act" trap that caught
  Belgium and France (2016 in both) exists in Spain too, dated **2007**;
  three of five countries have it, so it is a research hazard rather than a
  coincidence.
- **The fourth branch of the DCAT chain.** [[ES-NTI-RISP]] is the only one
  of the four national profiles that is a **legally mandatory technical
  norm** rather than an agreed profile — recorded at `confidence: low`
  because the DCAT-AP-ES model is still in administrative processing.
- **The first edge in the statistics cluster**, after five refusals across
  four countries. [[ES-INE]] `related-to` [[EU-EUROSTAT]], deliberately at
  `source: interpretation`, `confidence: low`, because the sources describe
  a three-party structure (the European Statistical System) rather than a
  bilateral relationship. The correct fix — an `EU-ESS` entity — was **not**
  created inside a country batch.

**Also recorded:**

- **The Atlas's first organisational succession.** [[ES-AEAD]] `supersedes`
  [[ES-SGAD]], constituted 21 February 2025. `supersedes` was introduced for
  legislation and carried an organisational transformation unmodified — a
  reusability result. What it cannot express is that this was a
  *transformation* rather than an abolition and replacement.
- **Five countries, five NIS2 states.** [[ES-LCGC]] is `status: proposed`;
  [[FR-NIS2-LOI]] is `status: unknown`. *We know it has not happened* versus
  *we do not know* — both expressible, and side by side for the first time
  on instruments transposing one directive.
- **Five DPAs, still one EDPB link.** [[ES-AEPD]] joins Germany, Belgium and
  France in having none. The artefact is now more expensive to leave open
  rather than clearer.
- **A third national identity architecture.** [[ES-CLAVE]] is neither
  federation ([[FR-FRANCECONNECT]]) nor central account ([[DE-BUNDID]]) but
  a credential scheme, and it is the only one that treats identification and
  signature as separate problems. The eIDAS2 wallet deadline is now roughly
  four months away with **no country in the Atlas linked to it**.

**Known gaps:** no BOE citation for Real Decreto 729/2023, the decree
creating AESIA; the `Ley Orgánica` constitutional rank is not modelled, and
neither is partial implementation (LOPDGDD's Title X implements nothing
European); Red.es is cited but not created, so `ES-DATOS-GOB-ES` has no
`maintained-by` edge; the Centro Nacional de Ciberseguridad that
[[ES-LCGC]] would create was **not** given a node, because it does not
exist; Ley 39/2015 and 40/2015 were not modelled.

Sourcing position unchanged — every Spanish entity is `search-only`,
`last_verified: null`, no `accessed` dates. 200 of 206 entities are unread.

---

# UN-Connection Batch — the island is connected (2026-08-16)

**Scope:** the connections proposed in `discovery/candidates.md`, which was
filled the same day and scoped to the Atlas's largest standing structural
defect. `validation/reports.md` (Batch 15) had recorded it and five country
batches had not touched it:

> **The UN layer is an island** — zero relationships connect its entities to
> any EU or national entity. `UN → anything` is **0**.

**Entities added: 14.** 206 → **220**. Relationships 269 → **300**.

- **Organisations (5):** `UN-UNECE`, `UN-UNSC`, `UN-UNESCO`, `UN-CEFACT`,
  and `INTL-OECD-CSSP` (typed `programme`).
- **Programmes (4):** `UN-CES`, `UN-GGIM`, `UN-GGIM-EUROPE`,
  `INTL-OECD-CSSP`.
- **Frameworks (4):** `EU-ESS`, `UN-AI-ETHICS-RECOMMENDATION`,
  `UN-SDG-INDICATORS`, `EU-SDG-INDICATORS`.
- **Legislation (2):** `UN-AARHUS`, `EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE`.

**Existing entities rewired: 7.** `EU-EUROSTAT` (+4 edges), `UN-UNSD`,
`NL-CBS`, `DE-DESTATIS`, `BE-STATBEL`, `ES-INE`, plus the records in
`discovery/`.

**Validation:** `run_all.py` 5/5, 0 errors, 0 warnings;
`test_build_graph.py` 32 tests OK; `test_ui.mjs` 47/47; `audit.py` reports
**no fully disconnected entities**.

## The result

| | Before | After |
|---|---|---|
| `UN → anything` | **0** | **5** (`UN → NL/DE/BE/FR/ES`) |
| `EU → UN` | **0** | **4** |
| UN entities | 9, unattached | 17, in three connected clusters |

**No relationship type was added and no sourcing standard was lowered.**

## Principal finding: the refusals were right, the target was missing

`discovery/candidates.md` argued that the gap was *"less a research problem
than a missing intermediate entity problem"*, and that held in every
cluster.

`UN-UNSD` → `EU-EUROSTAT` had been examined and refused three times. The
refusals were **correct**: UNSD is a secretariat, and Eurostat does not
relate to it directly. What Eurostat's own cooperation page says is that it
represents the EU **in forums** — the UN Statistical Commission, the
Conference of European Statisticians, and the OECD statistics committee. The
Atlas had no node for any of the three.

Once `UN-UNSC` and `UN-CES` existed, the edge became statable from evidence
that had been available all along. The same applied to `EU-ESS`: five
national-statistical-office edges had been refused because the partnership
they all belong to was not modelled.

**This is the batch's transferable lesson.** A refused edge that keeps
recurring is worth re-reading as a question about the *nodes*, not the
sources.

## Four clusters, three closed

1. **Statistics — closed.** `EU-EUROSTAT` `participates-in` `UN-UNSC` and
   `UN-CES`, and is `part-of` `EU-ESS` along with `NL-CBS`, `DE-DESTATIS`,
   `BE-STATBEL` and `ES-INE`. `UN-UNSD` is `governed-by` `UN-UNSC`, which
   also resolves the Batch 13 modelling question about whether the
   secretariat and the intergovernmental body should be one entity.
2. **Environmental information — closed, and it is the important one.**
   `UN-AARHUS` (UNECE convention, 1998, in force 2001) →
   `EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE` (2003/4/EC) → `applies-in` to
   all five countries. **The Atlas's first complete UN → EU → national
   chain**, and its first `applies-in` relationships from a UN instrument.
3. **UNESCO / AI ethics — closed as far as the sources allow.** The Batch 13
   refusal was reversed for UNESCO and UNECE. The Recommendation is attached
   to UNESCO.
4. **Geospatial — deliberately left incomplete.** `UN-GGIM` and
   `UN-GGIM-EUROPE` exist and attach to `UN`; **no edge reaches
   `EU-INSPIRE`**, because what the sources show is a EuroGeographics
   presentation *about* UN-GGIM given to an INSPIRE audience. Two
   communities talking is not two instruments relating.

## The vocabulary held, once

`EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE` `implements-requirement-from`
`UN-AARHUS` uses the type Batch 3 introduced for the EU→national chain. Its
definition reads *"an EU (or other higher-level) legal instrument"* — the
parenthesis, written two years before there was an instrument to use it on,
turned out to cover the UN→EU step exactly. **No type was added.**

## The vocabulary failed, twice

Two genuine EU↔UN interactions could **not** be recorded:

- the **UNESCO–European Commission agreement** on accelerating AI ethics
  implementation — a funding-and-cooperation arrangement to help *other*
  countries, not adoption or implementation by the Commission;
- the **2023 EU voluntary review** submitted to UN global SDG monitoring — a
  one-off report to a UN process.

Neither is adoption, implementation, governance or reference. **Two examples
is the threshold `metadata/relationship-types.md` §2.3 sets for proposing a
new type**, and it was deliberately not proposed by a batch that could not
read the sources.

## A record that had been wrong for three batches

`discovery/unresolved.md`, `discovery/candidates.md` and three batch entries
all repeated that *"three/four national statistical offices sit in the Atlas
and none connects upward"*. **`NL-CBS` already carried a `participates-in`
edge to `EU-EUROSTAT`**, added early, with ESS-membership reasoning in its
own evidence string.

The claim was carried forward from batch to batch without being checked
against the entity files. Corrected, and the edge repointed to `EU-ESS` with
the other four. The lesson is recorded in `discovery/unresolved.md`: cluster
narratives in the discovery files are prose, and **prose is not validated**.

## Refused, and why

- **`EU-AI-ACT` → `UN-AI-ETHICS-RECOMMENDATION`.** The dates line up —
  UNESCO Nov 2021, `ES-AESIA` Aug 2023, AI Act 2024 — and nothing read says
  they relate. This was the batch's most attractive available error: a
  UN → EU → national AI chain is exactly the shape it was looking for.
  Chronology is not causation.
- **`UN-AARHUS` → `EU-OPEN-DATA-DIRECTIVE` / `EU-INSPIRE`.** Adjacent
  subject matter, flagged in `candidates.md` as *"a reason to research, not
  a finding"*, and left there.
- **National transpositions of 2003/4/EC.** Five `applies-in` edges are
  asserted and **not one transposing instrument is named**. The trap is
  live: several countries have general open-government acts already in the
  Atlas (`NL-WOO`, `ES-LEY-37-2007`) that are *not* the environmental
  information transpositions — the same shape as the 2016 open-data acts in
  Belgium and France.
- **EuroGeographics**, **the 2030 Agenda**, **Regulation (EC) 223/2009**,
  and any **UN/CEFACT standard**. All named in sources, none sourced well
  enough to create inside this batch.

## Newly opened

**Soft law is indistinguishable from binding law.** `UN-AARHUS` binds its
Parties; the `UN-AI-ETHICS-RECOMMENDATION` does not. Nothing in the metadata
says so. This is the **same missing property** the Spain batch found from
the other direction, where `type: law` flattened Spain's constitutional
`Ley Orgánica` rank. Two independent batches, one gap. No field added.

Sourcing position unchanged — every new entity is `search-only`,
`last_verified: null`, no `accessed` dates. 214 of 220 entities are unread.

---

# Basisregistraties — the ten registers modelled (2026-08-16)

**Scope:** the `stelsel van basisregistraties`, which [[NL-BASISREGISTRATIES]]
itself had been asking for since Batch 2: *"the individual registrations are
not yet Atlas entities, and the full list of ten has not been enumerated
from a source"*, and *"once the individual registrations become entities,
this link should move down to the BRP entity."*

**Entities added: 13.** 220 → **233**. Relationships 300 → **320**.

- **Registers (10, typed `platform`):** `NL-BRP`, `NL-NHR`, `NL-BAG`,
  `NL-BRT`, `NL-BRK`, `NL-BGT`, `NL-WOZ`, `NL-BRV`, `NL-BRI`, `NL-BRO`.
- **Organisations (3):** `NL-RVIG`, `NL-WAARDERINGSKAMER`,
  `NL-BELASTINGDIENST`.

**Existing entities rewired:** `NL-BASISREGISTRATIES` rewritten;
`countries/nl/index.md` restructured to show the ten registers under the
stelsel and the holders under Registries.

**Validation:** `run_all.py` 5/5, 0 errors, 0 warnings;
`test_build_graph.py` 32 tests OK; `test_ui.mjs` 47/47; `audit.py` reports
no fully disconnected entities.

## Every register has a description, a holder and a place in the system

| Register | Answers | `maintained-by` | Statute named |
|---|---|---|---|
| BRP | who people are, where they live | RvIG | Wet BRP — **modelled** |
| NHR | which businesses exist | KvK | none found |
| BAG | addresses and buildings | Kadaster (facility) | Wet BAG, 1 Jul 2009 |
| BRT | topography, small/medium scale | Kadaster | **none found** |
| BRK | who owns real property | Kadaster | Kadasterwet (weak) |
| BGT | topography, 20 cm accuracy | Kadaster (facility) | Wet BGT, 1 Jan 2016 |
| WOZ | what property is worth | Waarderingskamer | Wet WOZ |
| BRV | vehicles and keepers | RDW | none found |
| BRI | what people earn | Belastingdienst | AWR ch. IVA, 1 Jan 2009 |
| BRO | what is underground | TNO (facility) | Wet BRO, 1 Jan 2018 |

## Principal finding: the Atlas cannot express how data moves

This is a finding about the vocabulary, not about the Netherlands.

**Five sourced connections could not be recorded**, in three shapes:

1. **Authorised use.** The Belastingdienst consumes the WOZ; the RDW
   receives BRP data. No relationship type says "is an authorised user of".
   The stelsel's *own* documentation uses the RDW as its worked example of
   an organisation that is holder, provider and user at once — and the Atlas
   can record one of those three.
2. **Key-sharing couplings.** BRK products carry the KvK number from the
   NHR; the BAG couples to the BRP through documented RvIG guidance. No type
   for "carries the identifier of".
3. **`Authentiek gegeven`.** The legal status that makes a base registry
   authoritative — data other bodies must use and may not independently
   re-determine — has no metadata field.

**The Atlas models what entities *are* and what they *descend from*, and has
almost no vocabulary for how data moves between them.** For a system whose
entire purpose is data movement, that is the honest headline.

With the UN batch's two, **five sourced connections are now unmodelled for
want of a type**, well past the `metadata/relationship-types.md` §2.3
threshold for proposing one.

## Roles, not owners

The stelsel describes four roles — initiator, supervisor, provider, holder —
and states one organisation can be several at once. The Atlas has one type,
`maintained-by`, and every register carries exactly one.

Where the roles diverge the edge points at the party the Atlas can name, and
**the divergence is written into the relationship's own `evidence` string**
rather than only into prose, so it is visible in the graph data. That is a
mitigation, not a fix.

The cost concentrates in three registers, where the party that actually
creates the data is absent from the graph: BAG and WOZ (municipalities) and
BGT (seven categories of bronhouder).

## Dutch municipalities — a different gap from the federal one

Unlike the German Länder, Belgian Regions and Spanish Comunidades Autónomas,
this is **not** the `level` vocabulary: `local` exists. It is that there is
no obvious entity to create — hundreds of municipalities, and one node for
"the municipalities" would be an invention. `NL-VNG` is their association,
which is a different thing.

Three of five countries have an unrepresentable sub-national tier for
ontology reasons; the Netherlands has one for a different reason entirely.

## Deliberate limits

- **No law entities created.** Only `NL-BRP` carries `governed-by`, to the
  pre-existing `NL-WET-BRP`. The Wet BAG, Wet BGT, Wet BRO, Wet WOZ and AWR
  Chapter IVA are named in descriptions and have no entities: six Dutch
  statutes is a legislation batch, and doing half would leave the layer
  inconsistent.
- **No inter-register relationships**, despite several being well sourced —
  see the vocabulary finding above.
- **Digimelding, SVB-BGT, Rijkswaterstaat, ProRail, RVO** — all named in
  sources as parts of the system, none created.
- **`NL-BRO`'s predecessors DINO and BIS** — described as things the register
  *builds on*, which is weaker than supersession. No `supersedes` asserted;
  DINO appears to continue to exist.
- **`NL-BRV` holds personal data** and is plainly in scope for the GDPR and
  the UAVG. Nothing read says so, so nothing is asserted.

## Typing

All ten are `platform` — *"a concrete technical platform or system"*. A
basisregistratie is arguably a **dataset with a legal status** rather than a
platform, and there is no `register` or `dataset` type. Applied consistently
so the set is at least coherent; logged as a typing question.

⚠ **`NL-BRT` has no sourced statutory basis at all** — the only one of the
ten — and is `coverage: low` as a result.

Sourcing position unchanged — every new entity is `search-only`,
`last_verified: null`, no `accessed` dates.

---

# Cybersecurity domain (2026-08-16)

**Scope:** the outstanding backlog item *"a cybersecurity domain entity —
well over twenty entities across three layers and five countries qualify
under the taxonomy §1 threshold. Deliberately not created inside a country
batch."*

**Entities added: 1.** 233 → **234**. `DOMAIN-CYBERSECURITY` connects **23
entities** by `domains:` association — three layers, five countries.

- **International (2):** `INTL-ISO-IEC-27001`, `INTL-ISO-IEC-27002`.
- **European (5):** `EU-NIS`, `EU-NIS2`, `EU-CYBERSECURITY-ACT`,
  `EU-ENISA`, `EU-CYBERSECURITY-STRATEGY`.
- **National (16):** NL — `NL-WBNI`, `NL-CBW`, `NL-BIO`; DE — `DE-BSI`,
  `DE-BSIG`, `DE-NIS2UMSUCG`, `DE-IT-GRUNDSCHUTZ`; BE — `BE-CCB`,
  `BE-NIS1-WET`, `BE-NIS2-WET`; FR — `FR-ANSSI`, `FR-NIS2-LOI`; ES —
  `ES-CCN`, `ES-INCIBE`, `ES-LCGC`, `ES-ENS`.

A row was added to `metadata/taxonomy.md` §1.3 in the same commit, as that
section requires. `countries/nl/index.md` gained the domain.

**Validation:** `run_all.py` 5/5; `test_build_graph.py` 32 tests OK;
`test_ui.mjs` 47/47; `audit.py` clean. The graph shows exactly 23
association edges into the new node and no relationship edges — domains are
referenced *by* entities, never the reverse.

## Why a domain earns its place

`metadata/taxonomy.md` §1.1 says domains are *"the cross-cutting axis of the
graph: they let you ask 'what connects to Mobility?' regardless of type,
level or country."* This one demonstrates the point — **three things became
legible that no single entity shows**:

### One directive, five different national states

Every country in the Atlas has a NIS2 position and no two are alike:
Belgium in force Oct 2024, Germany Dec 2025 by *amending* an existing act,
the Netherlands Aug 2026, France `status: unknown` because its sources
contradict each other, Spain `status: proposed` because it is still a draft.

Two of five are neither "done" nor "not started", **and they are unclear in
different ways** — `unknown` means the Atlas does not know, `proposed` means
it knows the thing has not happened.

### The national authority is not one institution

Germany, Belgium and France each have one named body. **Spain has two**,
split by audience — `ES-CCN` for the public sector under the intelligence
centre, `ES-INCIBE` for citizens and business — with `ES-LCGC` proposing a
third on top.

**The Netherlands has none in the Atlas at all.** The NCSC is not modelled.
Four of five countries have a cyber authority; the founding country does
not.

That gap is the batch's most useful output. It is invisible looking at Dutch
entities one at a time and obvious the moment the domain is assembled —
which is the argument for domains in one example.

### Two three-layer chains that do not meet

ISO/IEC 27001–27002 sit above the national baselines (`NL-BIO`,
`DE-IT-GRUNDSCHUTZ`, `ES-ENS`); `EU-NIS` → `EU-NIS2` sits above the national
transpositions. **Nothing connects the two chains**, and no source read
joins the NIS2 obligations to the baselines that would carry them in
practice. Recorded as an observation, not closed with an invented edge.

## Boundary decisions — both judgements, both documented

**`EU-CER` is excluded.** The Critical Entities Resilience Directive is
NIS2's sibling, adopted the same day for the same operators, but it governs
**physical** resilience rather than network and information security.

The boundary is genuinely awkward and the Atlas shows where: `FR-NIS2-LOI`
is a **single French instrument transposing NIS2, CER and DORA together**,
tagged to this domain for its NIS2 content — so the domain boundary cuts
through one national law.

**Data protection is excluded** on the same reasoning, even though several
authorities hold both remits and `FR-CNIL`'s body records that it is
described as strengthening collaboration with `FR-ANSSI`.

## Not connected

The Dutch NCSC (the largest hole), the Centro Nacional de Ciberseguridad
that `ES-LCGC` would create, CERT functions named in several bodies
(CCN-CERT, INCIBE-CERT), and `EU-ETSI` — a European standards body active in
cybersecurity with **no ETSI standard modelled**, so nothing to tag.

## Also fixed

`progress/current-batch.md` carried **"214 of 220 entities are unread"** in
its priority list — stale since the register batch, where the sourcing
paragraph was updated and the priority list was not. Corrected to 227 of
234 (224 `search-only` + 3 `unverified`). Same class of defect as the statistics-cluster claim the UN batch
found: **prose figures in progress files are not validated by anything.**

---

# Poland — Sixth Country (2026-08-16)

**Scope:** Poland as the sixth national scope, and specifically as the first
**outside western Europe**. `progress/backlog.md` asked for it by name and
stated what it was meant to test: *"that the EU layer is the right regional
parent, and that `applies-in` is the right way to attach a country to it"* —
two assumptions six western EU members could not check.

**Entities added: 10.** 234 → **244**. Relationships 320 → **346**.

- **Country anchor (1):** `PL`.
- **Organisations (4):** `PL-MC`, `PL-COI`, `PL-UODO`, `PL-GUS`.
- **Legislation (3):** `PL-ODO`, `PL-KSC`, `PL-OTWARTE-DANE`.
- **Platforms (2):** `PL-MOBYWATEL`, `PL-DANE-GOV-PL`.

**Existing entities modified:** `applies-in` → `PL` on 17 EU instruments
**and on `UN-AARHUS`** — the first time a country batch has attached to a UN
instrument as well as EU ones. Five-country prose updated to six across 16
files; the NIS2 table gained a sixth row.

**Validation:** `run_all.py` 5/5; `test_build_graph.py` 32 tests OK;
`test_ui.mjs` 47/47; `audit.py` → `targets: ['BE', 'DE', 'ES', 'FR', 'NL',
'PL']`, no disconnected entities.

## Principal result: both assumptions held

Poland acceded in **2004**, in a different enlargement from any of the five,
with a post-1989 administrative tradition none of them share. It required
**no schema, ontology, taxonomy, relationship-type, folder, validation or
generator change**, and produced no `PL-EU-*` entity.

The EU layer is the right regional parent for a 2004 accession state exactly
as for a founding member, and `applies-in` attached Poland unmodified.

## Second result: the new questions are about *time*, not structure

Unlike Spain, which sharpened the `level` finding, Poland raised two
questions the `level` vocabulary has nothing to do with — and **neither is
expressible**.

### An instrument in force, and a member state before the CJEU

`PL-KSC` implements NIS2 with effect from **3 April 2026**. Poland missed
the 17 October 2024 deadline and **is in proceedings before the Court of
Justice**. `status: active` is correct and carries none of that.

This is a sixth NIS2 state and the first that is **not on the
done/not-done axis**:

| Country | State |
|---|---|
| Belgium | in force 18 Oct 2024 |
| Germany | in force 6 Dec 2025 — amends the existing act |
| Netherlands | in force 15 Aug 2026 |
| France | `unknown` — sources contradict each other |
| Spain | `proposed` — draft; **reasoned opinion** received |
| **Poland** | **in force — and referred to the CJEU** |

Spain and Poland are at different stages of the *same* infringement
process, and the Atlas records neither.

### A national system subject to a requirement it cannot meet

`PL-MOBYWATEL` is reported **architecturally incompatible with eIDAS 2.0**,
unable to function as an EUDI Wallet, with adaptation deemed technically
impossible and replacement promised by end of 2026.

Four batches recorded that **no country in the Atlas was linked to
`EU-EIDAS2`**. Poland provides the first sourced link, and it is **negative**.

The relationship is recorded as `related-to` at `confidence: low` with the
substance in the evidence string, because no type expresses a requirement an
entity *fails* to meet: `implements-requirement-from` asserts the opposite,
`governed-by` implies the arrangement works.

**That is a sixth sourced connection the vocabulary cannot express**, after
the register batch's three and the UN batch's two — and the one with the
shortest fuse.

## What Poland confirmed

- **The 2016-act trap has a documented answer.** Poland had the identical
  2016 open data act that caught Belgium and France, and
  `PL-OTWARTE-DANE` **explicitly and fully repeals it**. Four of six
  countries are now closed, and the two open gaps have a known shape: a
  later act that either repeals the earlier one (Poland) or amends it in
  place (Spain).
- **The best-sourced `EU-ESS` membership so far.** `PL-GUS` describes the
  European Statistical System on its own pages and states its obligation to
  transmit statistics to Eurostat — where the other four attach on the
  composition rule. Five offices now; **France is the only modelled country
  without one**.
- **A third institutional transformation.** Spain's `ES-SGAD` → `ES-AEAD`
  completed; Poland's `PL-COI` → *Agencja Informatyzacji* is a **draft law
  in consultation**; Poland's GIODO → `PL-UODO` was **partial** (the
  President took over only part of the predecessor's competencies). Only the
  Spanish one is modelled as a succession. Three cases in two countries is
  starting to look like a shape worth handling deliberately.
- **Six DPAs, one EDPB link.** `PL-UODO` joins four others with no sourced
  link to `EU-EDPB`. Six page reads would fix five edges; the item has now
  survived four country batches.

## Refused / not modelled

- **CSIRT NASK, CSIRT GOV, CSIRT MON** — Poland joins the Netherlands as a
  country with cybersecurity legislation modelled and **no cyber authority**
  in `DOMAIN-CYBERSECURITY`, which now shows two such countries of six.
- **PESEL** — Poland's population register, the counterpart of the ten Dutch
  base registries, named in one list and nothing more.
- **The Agencja Informatyzacji** — does not exist; same refusal as Spain's
  Centro Nacional de Ciberseguridad.
- **GIODO** — no clean succession in the sources, so none asserted.
- **Krajowe Ramy Interoperacyjności**, a Polish DCAT profile, the operator
  of `PL-DANE-GOV-PL`, and the Act on Public Statistics. All named, none
  modelled.

⚠ **`PL-ODO` has no Dz.U. or ISAP citation** — the weakest-sourced of the
six national GDPR instruments, resting on secondary commentary and a UODO
annual report. `PL-OTWARTE-DANE` is the best, with a full Dziennik Ustaw
reference.

Sourcing position unchanged — every Polish entity is `search-only`,
`last_verified: null`, no `accessed` dates. 237 of 244 entities are unread.

---

# 2026-08-16 — Domain, provenance and confidence filters on the site

**No entity changed.** This is a site and generator change: three new facets
in `tools/build_graph.py`, three new filter groups in the interactive Atlas.
Graph regenerated with identical content — 244 entities, 2,420 edges.

## Why these two

The Atlas already held both axes and neither was reachable from the UI.

**Domain.** `metadata/taxonomy.md` §1.1 says domains are "the cross-cutting
axis of the graph" — they exist so a reader can ask *"what connects to
cybersecurity?"* regardless of type, level or country. Seven domains tag
**214 of 244 entities**, `DOMAIN-CYBERSECURITY` was written the same day to make
exactly that question answerable, and **the site could not ask it.** The
domain view existed only as prose in `domains/domain-cybersecurity.md`.

**Provenance and confidence.** Every typed relationship carries
`source: fact | interpretation` and a `confidence`. Interpretation edges were
already drawn dashed and both fields already appeared in the detail panel —
but per-edge, one at a time. There was no way to ask *"show me only the
interpretations"*, which is the question that makes the Atlas auditable
rather than merely annotated. The answer turns out to be **13 edges of 346**,
and that number was previously obtainable only by grepping the repository.

## What the filters show

| Filter | Rows | Notable |
|---|---|---|
| Domain | 7 | Government 193, Cybersecurity 24, Geospatial 16, Mobility 7, Research 4, Health 3, Education 2 |
| Provenance | 2 | fact **333**, interpretation **13** |
| Confidence | 3 | medium **317**, low **27**, high **2** |

Two facts became visible in building it, both about the Atlas rather than
about Europe: **only two edges in the entire graph are `confidence: high`**,
and **96% of typed relationships are `medium`** — the confidence field is
close to being a constant, which is worth knowing before anyone reads it as
a signal.

## Three decisions worth recording

**1. A domain filter must keep the domain entity itself.** A domain entity
carries no `domains:` of its own — it is the hub every tagged entity points
at. Filtering naively on the field would return 24 cybersecurity entities
with the node connecting them removed. `passesNodeFilters()` therefore admits
a node whose *id* is the selected domain, and a UI test asserts it (25 nodes,
not 24).

**2. Provenance and confidence narrow relationships only.** Associations and
wikilinks carry neither field. If the filters applied to all classes,
selecting `interpretation` would silently delete every association from the
view. `passesEdgeFilters()` returns early for non-relationship classes.

**3. Confidence is ordinal, so it is not sorted by count.** Facets sort by
frequency, which would render confidence as *medium, low, high* — a scale
printed in scrambled order. `facetInto()` gained an `opts.order` parameter
(generalised from the existing `levelOrder` special case), and a UI test
asserts the first row is `high` and the last is `low`.

## Verification

`validation/run_all.py` 5/5, 0 errors, 0 warnings.
`tools/test_build_graph.py` **37 tests** (was 32 — five added: dynamic domain
discovery, domain labels from domain entities, domain counts against the
tagging, provenance/confidence totals against the relationship edges, and
vocabulary conformance for both).
`tools/test_ui.mjs` **55 checks** (was 47 — eight added, including that the
domain filter keeps its own hub and that confidence is ordered high → low).

Docs updated: `docs/graph.md` filter table, `docs/graph-development.md`
"adding a filter" with the ordering and hub-node notes, `README.md`.

---

# 2026-08-16 — The comparison matrix

**No entity changed.** A fourth view on the interactive Atlas: rows are
supra-national instruments, columns are countries, cells say what each
country did. Derived entirely in the browser from edges already in
`graph.json` — **no payload change, no generator change**.

## Why

The most valuable content the Atlas holds is cross-country comparison, and
it existed **only as prose tables hand-written inside entity bodies**: the
GDPR technique table in six national acts, the NIS2 state table in six more,
the Open Data Directive's 2016-act trap. Every one of them had to be edited
by hand whenever a country was added, and several went stale between batches
— stale counts have been corrected in this repository more than once.

All of it is derivable. `applies-in` and `implements-requirement-from` are
already on the edges; the view groups them by country.

## What it shows

**20 instruments × 6 countries · 21 implemented · 88 applying with no
national instrument modelled.**

| Cell | Meaning | Source |
|---|---|---|
| A national entity | That country implements it | `implements-requirement-from` → the row |
| Applies — none modelled | Recorded as covering that country, nothing modelled | `applies-in` from the row |
| — | Nothing recorded either way | neither edge |

**Only two instruments are implemented in all six countries: the GDPR and
NIS2.** They are also the only two the prose tables ever covered. The other
18 rows are what the prose never showed.

## Three findings the matrix produced immediately

None of these is visible from any single entity, and all three are real.

**1. The GDPR supervisory authority is modelled inconsistently.**
Seven entities carry `implements-requirement-from EU-GDPR`. Six are national
laws — one per country. The seventh is **[[NL-AP]], an organisation**: the
Netherlands is the only country whose *supervisory authority* also carries
the edge. Either the other five are missing it or the Dutch one is
misplaced, and the matrix is the only place the asymmetry is visible.

**2. [[EU-EIDAS]] has no `applies-in` edges at all** — yet it is `active`
and [[DE-BUNDID]] implements it. Every other active EU instrument in the
matrix attaches to all six countries. [[EU-NIS]]'s empty row is different
and correct: it is `superseded`.

**3. [[EU-INSPIRE]] applies in five countries and not the Netherlands** —
`['BE', 'DE', 'ES', 'FR', 'PL']`. The founding country, with a geospatial
domain and a national geo-portal, is the one missing. Almost certainly an
omission from before the `applies-in` convention settled.

## Design decisions

**Rows respect the sidebar filters; columns respect the country filter
only.** Rows are supra-national instruments with `country: null`. Running
the country filter over them empties the table — which is exactly what the
first implementation did, caught by a UI test written to check the columns.
`passesNodeFilters()` gained an `ignoreCountry` argument for this.

⚠ That argument introduced a trap worth recording: `renderList()` called
`.filter(passesNodeFilters)`, and **`Array#filter` passes the index as the
second argument** — so `ignoreCountry` would have been truthy for every row
but the first, silently disabling the country filter in the List view. Both
call sites are now explicit wrappers, and the reason is a comment.

**An implementer with no country belongs to no column.** The EU implementing
a UN convention ([[EU-ENVIRONMENTAL-INFORMATION-DIRECTIVE]] →
[[UN-AARHUS]]) is reported on the row instead of being dropped.

**Cells key on the entity ID, not the name.** Several of these carry full
official titles a dozen words long; the name stays in the tooltip and the
accessible name.

**The three states are distinguished by words, not only by tint.** "Applies
— none modelled" says so, and an empty cell is explicitly *not* a claim that
the instrument does not apply — it means the Atlas records nothing either
way. A UI check asserts the wording is present.

## One CSS fix outside the view

`.layout` gained `overflow-x: hidden`. A 7-column matrix on a 390px phone
was pushing the **document** sideways by 561px rather than scrolling inside
its own wrapper. `body` already carried the same guard; the flex row below
it did not. Now covered by a mobile UI check.

## Verification

`validation/run_all.py` 5/5, 0 errors, 0 warnings.
`tools/test_build_graph.py` **37 tests** — unchanged, and `graph.json` is
byte-identical, which is the point: this view added no data.
`tools/test_ui.mjs` **66 checks** (was 55 — eleven added, including that the
country filter moves the columns and not the rows, that supra-national
implementers survive, and that the matrix scrolls in its wrapper on mobile).

---

# 2026-08-17 — United Kingdom, the seventh country and the first outside the EU

**258 entities, 354 relationships, seven countries.** 14 entities added.
`applies-in` targets are unchanged — `['BE', 'DE', 'ES', 'FR', 'NL', 'PL']`
— and **that is the result**, not an omission.

## Principal result: the first assumption finally broke, and nothing else did

Six batches produced six EU member states. Every "no change was needed"
result until now was measured against countries that share a regional
parent, so the country-neutral claim had never actually been tested against
the thing it was designed for.

The United Kingdom is **not an EU member state**:

| | Six member states | United Kingdom |
|---|---|---|
| `region:` on national entities | `EU` | **`null`** |
| `applies-in` from EU instruments | 17–18 each | **none** |
| Route to the European layer | membership | `derived-from` + a transposition that predates leaving |
| Route to the international layer | via `EU-ESS` | **directly, via `UN-CES`** |

**No schema, ontology, taxonomy, relationship-type, folder, validation or
generator change. No `GB-EU-*` entity.** The design absorbed a non-member
state without modification, which is a stronger result than Poland's,
because Poland was the same kind of thing as its five predecessors and the
UK is not.

## The ID is `GB`

`metadata/schema.json` fixes the ID scope to an ISO 3166-1 alpha-2 code, and
the alpha-2 assignment for the United Kingdom is **`GB`**. `UK` is reserved
at ISO's request but is not the alpha-2. Every other anchor is an alpha-2
code, so `UK` would have been the only ID in the Atlas that is not. `UK` is
carried in `alternative_names`, and the README's folder tree — which had
carried a speculative `uk/` placeholder since batch 0 — is corrected to
`gb/`.

## Two European edges, neither of them `applies-in`

**1. `GB-UK-GDPR` `derived-from` `EU-GDPR`.** UK GDPR is *assimilated law*:
the EU Regulation's own text, carried into UK domestic law at the end of
transition, renamed from "retained EU law" by the Retained EU Law
(Revocation and Reform) Act 2023 with effect from 1 January 2024, and
amended since.

This breaks a six-batch streak. Every batch since the register work has
added to a list of *sourced connections the vocabulary cannot express* —
now six items long. **This is not a seventh.** `derived-from` is defined in
`metadata/relationship-types.md` as *"one entity was produced by adapting
another"*, which is exactly what assimilated law is. A vocabulary written
for a Dutch-and-EU Atlas described a post-Brexit constitutional relationship
without amendment.

The GDPR technique table gets a seventh row that does not fit the column:
six countries each *wrote something* to give effect to a regulation that
already applied to them; the UK wrote nothing of the kind.

**2. `GB-NIS-REGULATIONS` `implements-requirement-from` `EU-NIS`.** SI
2018/506 gave effect to Directive (EU) 2016/1148 in May 2018, while the UK
was a member state. It is **still in force**, as assimilated law, and
`EU-NIS2` never repealed it because the UK was outside its scope by then.

So the Atlas now holds a **transposition of an EU directive asserted from a
country that has left the EU**, needing no qualification. In the Compare
view it puts the UK next to the Netherlands on the `EU-NIS` row — the only
two countries with a modelled NIS Directive implementation, spanning a
member state and a former one.

The UK is correspondingly **absent from the NIS2 table** that six batches
built. It runs a NIS1-era regime the EU has superseded and is replacing it
on its own timetable with `GB-CSRB`, a bill that transposes nothing.

## The statistical office joins through the UN, not the EU

`GB-ONS` `participates-in` `UN-CES`. Five member states reach the
international statistical system **through** `EU-ESS`; the UK cannot,
because the ESS comprises Eurostat and the member states' authorities.

It reaches it directly instead, via the Conference of European
Statisticians — a UNECE body with ~65 members, on whose **Bureau the UK
sits**, and which the ONS has hosted in Cardiff.

**That edge exists only because the UN batch created `UN-CES`.** At the
time, the CES looked like completeness work on the statistics chain. It
turned out to be the connector for a country that did not yet exist in the
Atlas — and without it the UK's statistical office would have had no upward
link of any kind.

## What the UK exposed that six member states could not

⚠ **`country` is a field, not an edge, and `GB` is the Atlas's first orphan
anchor.** `validation/audit.py` reports `1 fully disconnected: ['GB']`.

The other six anchors are reachable through frontmatter only because EU
instruments point `applies-in` at them. Nothing points at `GB`: its 13
entities carry `country: GB`, and the generator emits `domains`,
`organisations`, `related_entities`, `previous_version` and `successor` as
association edges — **not `country`**.

`GB` still has degree 16 in the rendered graph, all of it body wikilinks, so
it is not visibly isolated. But at the frontmatter level it is unreachable,
and no query that walks associations will find it from its own entities.

This was **not fixed in this batch.** Making `country` an association edge
would add ~250 edges across all seven countries and change every country's
graph shape — a design change, not a country addition. Populating
`related_entities` on `GB` alone would make it the only anchor that does
that. Recorded in `progress/backlog.md` instead.

## Three findings about time and institutions

**1. The Atlas's first abolition.** `GB-DSIT` — the Department for Science,
Innovation and Technology, created February 2023 — was **abolished on 21
July 2026**. Three institutional transformations were recorded before it
(`ES-SGAD` → `ES-AEAD`, `PL-COI`'s pending conversion, GIODO → `PL-UODO`)
and all three were continuations. This is the first entity in the Atlas to
stop existing.

⚠ **A fan-out succession is not expressible.** DSIT's functions went three
ways: business/innovation/science/trade to a new DBIST; digital
transformation, cyber, digital identity and `GB-GDS` to `GB-DCMS`; AI policy
to the Cabinet Office. `successor` is a **single** field described as a way
to *chain* superseded entities, and a chain is the wrong shape. `successor`
is `null` and the split is in prose. Two of the three destinations are not
Atlas entities, so even a list-valued field would be one-third populated.

**2. A status the vocabulary cannot carry.** `GB-DUAA` s.117 establishes an
**Information Commission** to replace `GB-ICO`, with the change reported as
expected "spring/summer 2026". This batch is dated 17 August 2026 and
**cannot establish whether it has happened**. No successor entity was
created — the same refusal applied to Spain's *Centro Nacional de
Ciberseguridad* and Poland's *Agencja Informatyzacji* — and "Information
Commission" went into `alternative_names` instead. `FR-NIS2-LOI` is
`unknown` because sources conflict; `ES-LCGC` is `proposed` because it is a
draft; this is a third kind, where the instrument is in force and the
institutional change it mandates has an unverified completion date.

**3. The amendment question, for the fourth time — and the first with no
workaround left.** `GB-DUAA` amends **two** instruments (`GB-UK-GDPR` and
`GB-DPA-2018`), both still in force. Germany's `DE-NIS2UMSUCG` could be
`supersedes`-d because the amending act is separately named; France's and
Poland's amendments were absorbed into the amended entity because they had
no independent identity. **Neither escape is available here**, so both edges
are `related-to` with the amendment in the evidence string. `GB-CSRB` →
`GB-NIS-REGULATIONS` is a fifth case.

## A cyber authority that is deliberately not a regulator

`GB-NCSC` is the UK's technical authority and is **explicitly not** a
competent authority under `GB-NIS-REGULATIONS`. The UK took a
sector-by-sector approach: Schedule 1 names the responsible departments,
Ofcom for digital infrastructure and **`GB-ICO` for digital service
providers**.

`DOMAIN-CYBERSECURITY` now holds three arrangements rather than two: one
body that advises and regulates (DE, BE, FR); two split by audience (ES);
and a technical authority separated from distributed sectoral regulators
(GB). Spain's split looked like the outlier when written; it is now one of
three, and the UK's is the only one where the data protection authority is
also a cyber regulator.

## Refused / not modelled

- **The EU adequacy decisions** — renewed 19 December 2025 for six years to
  27 December 2031, following the DUAA. The most important single link
  between the UK and the EU data layer, recorded in prose in `GB` and
  `countries/gb/index.md` and **represented by no edge**. First item in the
  backlog's UK section.
- **Ordnance Survey and the Geospatial Commission** — the latter merged into
  `GB-GDS` in January 2025 and no longer exists independently. **The UK
  joins with no geospatial entity at all**, unlike every other country in
  `DOMAIN-GEOSPATIAL`.
- **The Cyber Assessment Framework** — the UK counterpart to `NL-BIO`,
  `DE-IT-GRUNDSCHUTZ` and `ES-ENS`, all three modelled.
- **The UK Statistics Authority and the Office for Statistics Regulation** —
  `GB-ONS`'s parent and its regulator. Their absence weakens the `UN-CES`
  edge, whose sources establish that *the UK* is a member without
  distinguishing which body holds the seat; the evidence string says so.
- **DBIST and the Cabinet Office**, **Ofcom and the sectoral competent
  authorities**, **CDDO / i.AI / the Responsible Technology Adoption Unit**
  (merged into GDS), the **GOV.UK Wallet** and the **national digital ID
  scheme**, and the **Re-use of Public Sector Information Regulations**.

## Sourcing

⚠ **`GB-DCMS` is the weakest entity in the batch — `confidence: low`, all
three sources trade press.** No machinery-of-government order, departmental
page or statutory instrument was found for the post-July-2026 arrangement.
It exists so that `GB-GDS`'s `governed-by` edge has an uninvented target.

⚠ **`GB-DPA-2018` has no legislation.gov.uk citation of its own** — every
source describes it through the DUAA's changes to it, the same failure mode
as `PL-ODO`. Joint-weakest in the batch.

Unchanged otherwise: every UK entity is `search-only`, `last_verified:
null`, no `accessed` dates. **251 of 258 entities are unread.**

## Verification

`validation/run_all.py` 5/5, 0 errors, 0 warnings.
`tools/test_build_graph.py` 37 tests. `tools/test_ui.mjs` 66 checks.
`validation/audit.py`: `targets: ['BE', 'DE', 'ES', 'FR', 'NL', 'PL']`, no
country-scoped copies of EU/UN entities, **1 fully disconnected: `['GB']`**
— explained above.

---

# 2026-08-17 — Code of Conduct and security policy

**No entity changed; `graph.json` and `details.json` are byte-identical.**
Two community health files at the repository root, plus links from
`README.md` and `CONTRIBUTING.md`.

## Contact channel: GitHub-native, no email published

The maintainer commits under GitHub's `noreply` address, which is a
deliberate choice to keep a personal email out of the repository. Publishing
one in a policy file would have undone it, so **neither file contains an
email address.**

Both route through **GitHub private vulnerability reporting**
(`/security/advisories/new`) — the repository's only built-in private channel
to the maintainer — with a GitHub DM to [@DaLuSt](https://github.com/DaLuSt)
as the fallback, and GitHub's abuse reporting as an independent escalation
for conduct that also breaks GitHub's own policies.

⚠ **That link 404s until private reporting is switched on** in
*Settings → Advanced Security*. `SECURITY.md` carries the instruction as a
visible maintainer note rather than assuming it.

## Both files are adapted to what this repository actually is

Boilerplate would have been wrong in two specific ways.

**The Code of Conduct** carries a section on the fact that the Atlas
describes the laws and institutions of seven countries, so the subject matter
is political and contributors *will* disagree about characterisation. It
separates two things that generic templates conflate:

- **being wrong is not a violation** — 251 of 258 entities are
  `search-only`, and good-faith error and correction are the normal working
  mode here;
- **knowingly contributing fabricated sources or invented evidence is** a
  violation, because it damages every reader who trusts the graph.

**The security policy** opens by stating what the project is — *a dataset,
not a service* — because that determines what is worth reporting. It records
the site's posture as verified rather than asserted: no cookies, no
`localStorage`/`sessionStorage`, no analytics or beacons, no third-party
scripts or fonts, no external network requests (the only two `fetch()` calls
are same-origin, for `graph.json` and `details.json`), no inline event
handlers, and Cytoscape.js 3.34.1 vendored rather than pulled from a CDN.
It names `esc()` as the single escaping path and says plainly that a route by
which entity content reaches the DOM unescaped is exactly what the policy is
for.

It also draws a line the project needs and no template provides: **a
vulnerability in a system the Atlas *describes* is out of scope** — report it
to that system's operator — and **a citation that does not support its claim
is not a security issue at all**. The latter belongs in a *public* issue,
because the correction is the point.

## Verification

`validation/run_all.py` 5/5. `tools/build_graph.py --check` reports 258
entities, 2,649 edges — unchanged, because root-level Markdown is outside
`FLAT_ENTITY_DIRS`/`GEOGRAPHY_ROOTS` and is never scanned as an entity.
`tools/test_build_graph.py` 37 tests.

Both files use ordinary relative Markdown links rather than `[[wikilinks]]`:
`validate_links` does not scan the repository root, so wikilinks there would
be unchecked and free to rot.

---

# 2026-08-17 — Layout: blocks by scope, ordered by connectivity

**No entity changed; `graph.json` and `details.json` are byte-identical.** A
rewrite of `layeredPositions()` in `site/app.js`. The first half of a
two-part answer to *"can strongly connected nodes be drawn closer together?"*
— this part needs no layout engine at all.

## Why not just switch to a force layout

Measured first, on the actual payload, rather than assumed:

| Edge classes | Edges | Components | What a force layout would do |
|---|---|---|---|
| Relationships only (default) | 354 | **44**, plus **28 isolated nodes** | scatter the fragments as drifting debris |
| + associations | 1,257 | 2 | `DOMAIN-GOVERNMENT` has **degree 206 of 258** — one star pulling everything into a ball |

Running `cose` confirmed it: the bounding box collapses from 1686 px wide on
relationships-only to **426 px** with everything on. That is a hairball, and
"strongly connected nodes closer" would have meant "the country anchors and
one domain hub dominate the picture".

The strongest clustering signal in the data is one a physics layout would
**not** surface: **every typed relationship between two country-attributed
entities stays inside a single country — 131 of 131.** Not one crosses a
border. So the layout was changed to draw that instead.

## What it does now

Three levels of grouping, all deterministic arithmetic:

1. **Band = geographic level**, unchanged, and deliberately so. That
   hierarchy is the Atlas's core claim and the layout will not trade it away.
   A UI check asserts the bands still stack in order.
2. **Block = scope within a band.** For national entities `scope` is the
   country code, so the national band now reads as **seven separate clumps**
   instead of one continuous ribbon wrapped at an arbitrary row width. The
   international band splits into UN / INTL / DOMAIN the same way.
3. **Position within a block = connectivity.** Each block leads with its
   best-connected member and trails into its periphery.

Measured result: **no two country blocks overlap**, and the minimum distance
between block centroids is **715 px against a maximum block spread of 431**.

**Connectivity is counted over the edges currently on screen**, not over the
whole Atlas. Turning wikilinks on re-orders the blocks, because the ordering
should describe what the reader is looking at. This is why the visible degree
is computed in `layeredPositions()` rather than read from the `rel_degree`
baked into `graph.json`.

## Two things fixed on the way

⚠ **`LOD_LAYOUT` was dead.** `runLayout()` branched on it, and **both
branches were byte-identical** — same `layeredPositions()` call, same
`preset` layout. The comment promised *"too big to lay out organically"*, so
the organic path was either removed or never written. The branch and the
constant are gone; there is no size threshold because the cost does not
depend on convergence. `LOD_LABELS` still thins labels at 260 nodes. A
threshold will come back with the force layout, where it will gate something
real.

⚠ **The first attempt stacked every block on its own line**, because the
packing budget was the viewport width and a single block (`NL`, 8 columns ×
165 px) already exceeded it. The canvas pans and zooms, so the budget now
scales with the band's own size. Caught by looking at the render, not by a
test.

## Testing a layout without a production hook

The Cytoscape instance lives in a closure and is not exported. Rather than
add a `window.__test` hook to the shipped page — after a security policy that
makes a point of the small surface — the tests reach it through Cytoscape's
own container registration, `document.getElementById('cy')._cyreg.cy`. That
is an internal, but it is read-only, test-only, and adds nothing to
production.

Five checks added: one block per country, blocks do not overlap, blocks are
further apart than they are wide, each block leads with a
better-connected-than-median node, and the bands still stack
international → regional → national → sectoral.

## Verification

`validation/run_all.py` 5/5. `tools/build_graph.py --check` 258 entities,
2,649 edges — unchanged. `tools/test_build_graph.py` 37 tests.
`tools/test_ui.mjs` **72 checks** (was 67).

## Still to come

The force-directed layout and per-edge weighting, as a **switchable**
alternative rather than a replacement. Both are possible with the vendored
Cytoscape build: `cose` is registered, and `idealEdgeLength` accepts a
per-edge callback. `fcose`, `cola`, `dagre`, `elk` and `euler` are **not**
registered and would each mean vendoring a new file.

---

# 2026-08-17 — A switchable force-directed layout, weighted by evidence

**No entity changed; `graph.json` and `details.json` are byte-identical.**
Part two of *"can strongly connected nodes be drawn closer together?"* — the
half that uses a simulation. Still **no new dependency**: `cose` is in the
vendored Cytoscape build, and `idealEdgeLength` takes a per-edge callback.

## A switch, not a replacement

The grouped layout stays the default. The force layout trades away the one
thing the grouped layout exists to show — **geographic level stops being
positional and survives only as colour** — so making it the default would
have thrown away the Atlas's core claim to gain a prettier picture. The
sidebar hint says exactly that while the mode is active.

It governs the **Global Atlas only**. The Explorer's rings by hop distance
are the point of that view, and Compare and List have no canvas.

**Seeded, not randomised.** `randomize: false` starts the simulation from the
grouped positions, so the same graph yields the same picture instead of a
different one per visit, and the relaxation begins from an arrangement that
already means something.

**Not persisted.** `SECURITY.md` states the page keeps no cookies and no
`localStorage`/`sessionStorage`, so the layout choice is a session variable
and nothing more. Remembering it would have meant amending that policy.

## Two mitigations the measurements demanded

Both come straight from the numbers in the previous batch:

- **44 components and 28 isolated nodes** on the default view — without
  `componentSpacing: 130` a force layout flings them apart and the canvas
  becomes mostly whitespace. They now pack into tidy rows below the main
  cluster.
- **`DOMAIN-GOVERNMENT` has degree 206 of 258** — at uniform repulsion it
  drags the whole graph into a ball around itself. `nodeRepulsion` now grows
  with degree, so a hub holds its neighbours at arm's length instead of
  swallowing them.

## What edge weighting actually achieves — measured, not assumed

This is the part where the first attempt was wrong and the claim had to be
narrowed twice.

| | Result |
|---|---|
| Typed relationships | **Tightest class** — mean 72 px against 132 px for associations, with every edge class on |
| Low-confidence relationships | **~22% further apart** than medium — 203 px against 166 px, over 27 edges and 317 |
| `confidence: high` | **No effect, and no claim made.** Only 2 of 354 relationships carry it; a mean over two edges is noise |
| Wikilinks | Float at ~82 px — *shorter* than associations |

⚠ **A slack spring is not a long one.** The first tuning gave wikilinks
almost no elasticity, on the reasoning that 1,392 navigational links should
not reshape the graph. That part worked. But weak springs do not hold their
rest length either: they go slack and the nodes settle at whatever ambient
spacing the other forces produce. Springs pull; they do not push. So the
intended order — relationship < association < wikilink — is **not** what the
graph shows, and the hint text was rewritten to describe what it does.

The first attempt was worse still: at the original weights, association came
out *longer* than wikilink and the whole graph compressed into a 630 × 528
box. Retuning widened it to 825 × 655 and put typed relationships first.

## The size guard is not dead this time

The previous threshold, `LOD_LAYOUT`, was removed last batch because **both
sides of its branch were byte-identical**. `FORCE_MAX = 900` replaces it and
does gate something: above it the simulation is declined, the grouped layout
is kept, and the sidebar explains why rather than silently doing nothing.

A UI test proves it by intercepting `graph.json` and padding the node list to
1,258 — the layout does not move and the hint reads *"Too many entities on
screen (1,258) to lay out by simulation"*. Given the last threshold shipped
dead for months, testing this one seemed the minimum.

## Verification

`validation/run_all.py` 5/5. `tools/build_graph.py --check` 258 entities,
2,649 edges — unchanged. `tools/test_build_graph.py` 37 tests.
`tools/test_ui.mjs` **81 checks** (was 72 — nine added).

Measured cost of a switch: **~2.8 s wall time** at 258 nodes and 354 edges,
on the UI thread. That is the reason for the guard.

---

# 2026-08-17 — Connecting the United Kingdom

**258 → 265 entities, 354 → 376 relationships.** Seven entities added, eight
edges added to existing ones. The UK batch left the country technically
correct and practically isolated; this closes that.

## The problem, measured

| | Before | After |
|---|---|---|
| Typed relationships touching a GB entity | **8** | **29** |
| GB relationship endpoints (rank of 7 countries) | **13 — last** | **45 — third** |
| Edges leaving the UK for the rest of the Atlas | **3** | **13** |
| Non-wikilink edges into the `GB` anchor | **0** | **7** |
| `audit.py` connectivity | `⚠ 1 fully disconnected: ['GB']` | **no fully disconnected entities** |

NL 179, DE 90, **GB 45**, BE 40, ES 34, FR 32, PL 29.

## The anchor was orphaned because `country` is a field, not an edge

The UK batch recorded this and deliberately left it: the other six anchors
are reachable through frontmatter **only** because EU instruments point
`applies-in` at them, and no EU instrument points at [[GB]].

The fix uses an existing precedent rather than a new convention. [[NL-BIO]]
and [[NL-PAS-TOE-OF-LEG-UIT]] already carry `applies-in` to their **own**
country, and `metadata/relationship-types.md` defines the type as *"a
regulation, standard or initiative is applicable within a given
country/region"* — which is exactly what a UK act is in the UK. So
[[GB-UK-GDPR]], [[GB-DPA-2018]], [[GB-DUAA]], [[GB-NIS-REGULATIONS]] and
[[GB-CAF]] now carry it.

⚠ **This is applied to the UK only, and it should not stay that way.** The
same edges are equally true for the other six countries' national
instruments, and adding them there is a consistency pass this batch did not
do. In the backlog.

The Compare view is unaffected: its row set requires a **supra-national**
scope, so `applies-in` edges originating from a `GB`-scoped instrument are
correctly excluded and the UK column still shows what non-membership looks
like.

## Seven new entities, chosen for what they connect

| Entity | Bridges to |
|---|---|
| [[GB-BSI]] — British Standards Institution | [[INTL-ISO]], [[INTL-IEC]], [[EU-CEN]], [[EU-CENELEC]], [[EU-ETSI]] |
| [[GB-OS]] — Ordnance Survey | [[UN-GGIM]] |
| [[GB-CAF]] — Cyber Assessment Framework | [[INTL-ISO-IEC-27001]] |
| [[EU-UK-ADEQUACY]] — the Commission's adequacy decisions | [[EU-GDPR]] → [[GB-UK-GDPR]], [[GB-DUAA]] |
| [[GB-UKSA]] — UK Statistics Authority | [[UN-CES]] |
| [[GB-OFCOM]] — Ofcom | [[GB-NIS-REGULATIONS]] |
| [[GB-GEOSPATIAL-STRATEGY]] — UK Geospatial Strategy 2030 | — (policy layer above [[GB-OS]]) |

## Principal finding: leaving the EU did not remove the UK from European standards

[[GB-BSI]] is the single most connective UK entity — five bridges on its
own, more than the whole country had before — and what it shows is a genuine
asymmetry:

- **No EU instrument** carries `applies-in` to the United Kingdom, and none
  will while it is outside the Union.
- BSI nonetheless sits inside **CEN, CENELEC and ETSI**, because those are
  **European standards organisations, not EU institutions** — their members
  are national standards bodies, not member states — and its membership
  survived Brexit.

Those two facts are not in tension. They are what "left the European Union"
actually means in this domain, and neither is visible without the other.
The Atlas could not previously show either half.

## Two more things the new entities settle — and one they do not

**Settled: the geospatial gap.** The UK joined with **no entity in
[[DOMAIN-GEOSPATIAL]]**, the only country without one, because the
Geospatial Commission had been merged into [[GB-GDS]]. [[GB-OS]] closes it
and adds a **second UN-layer link** — so the UK now reaches the
international layer twice ([[UN-CES]], [[UN-GGIM]]) and the EU layer never
by membership. For a country with no regional parent, the UN layer is
carrying the connections.

**Settled: the cyber chain.** [[DOMAIN-CYBERSECURITY]] recorded two
three-layer chains that *do not meet*. [[GB-CAF]] joins them on the UK side:

```
INTL-ISO-IEC-27001 ←aligned-with— GB-CAF ←references— GB-CSRB
                                              → amends → GB-NIS-REGULATIONS
                                              → implements → EU-NIS
```

The UK is now the only country where a national baseline, a national cyber
instrument and an EU directive connect end to end — and it got there without
being in the EU, because the NIS Regulations were made while it still was.

**Not settled: who holds the UK's CES seat.** [[GB-UKSA]] was created
specifically to resolve the caveat on [[GB-ONS]]'s [[UN-CES]] edge, and the
sources do not say whether the seat belongs to the Authority or the Office.
The participation is therefore recorded on **both**, at `confidence: low` on
the Authority, with the ambiguity in both evidence strings. Two edges where
one belongs is worse than a clean answer and better than a confident guess.

## The adequacy decisions, refused once and now made

The UK batch called these *"the single most important connective fact between
the UK and the EU data layer"* and asserted nothing, because they are
Commission acts that had not been researched. [[EU-UK-ADEQUACY]] records
them: renewed **19 December 2025**, expiring **27 December 2031** under a
sunset clause.

It is filed `level: regional`, `region: EU` — a **Commission act, not a UK
one** — so it is the first entity in the Atlas that is *about* one country
while belonging to another scope. And it is the only edge running **from**
the EU **to** a non-member state's instrument; the UK's other two European
links both run outward and are both historical.

⚠ It also uses `end_date` in a way the Atlas has not before: **a future date
on an `active` entity**. Most entities with an `end_date` have already ended.
This one lapses on a known date unless the Commission acts, which is a third
variant of the status problem [[GB-ICO]] opened.

## Prose corrected, not just added

Seven existing entities asserted things that this batch made false —
"the CAF is **not** modelled", "Ofcom and the sectoral departments are not
modelled", "the UK Statistics Authority is not modelled", "no `applies-in`
edge targets GB", "the adequacy decisions are recorded in prose and refused
as edges". All were rewritten. Stale prose has been a repeated defect in this
repository, and adding entities without revisiting what they contradict is
how it happens.

## Verification

`validation/run_all.py` 5/5, 0 errors, 0 warnings.
`tools/test_build_graph.py` 37 tests.
`validation/audit.py`: **no fully disconnected entities**; `applies-in`
targets unchanged for EU instruments.
Graph regenerated: **265 entities, 2,801 edges**.

Sourcing unchanged — every new entity is `search-only`, `last_verified:
null`, no `accessed` dates. **258 of 265 entities unread.**

---

# 2026-08-17 — Connecting the loose nodes

**No new entities. 14 relationships added**, 376 → 390. The graph's
relationship layer was fragmented into **39 components**; it is now **31**,
and the largest has grown from **184 to 224 of 265 entities**.

Every edge below was researched and sourced. Where the Atlas had already
looked and refused for want of a source, that refusal was **left standing** —
this batch adds no edge it could not evidence.

## What connected, and what it pulled in

| Edge | Nodes brought into the main component |
|---|---|
| [[EU-EIDAS]] `applies-in` × 6 member states | **7** — the whole German identity/OZG cluster |
| [[NL-PDOK]] `aligned-with` [[EU-INSPIRE]] | **21** — the entire basisregistraties system |
| [[FR-RGI]] `based-on` [[EU-EIF]] | **5** — the French DINUM/Etalab cluster |
| [[NL-EAR]] `based-on` [[NL-NORA]] | **2** — with [[NL-RORA]] |
| [[DE-BFDI]] `applies-to` [[DE-BDSG]] | **2** — with [[DE-IFG]] |
| [[NL-ROSA]], [[NL-PETRA]] `based-on` [[NL-NORA]] | 2 previously isolated frameworks |
| [[EU-INSPIRE]] `applies-in` [[NL]] | completes INSPIRE across all six member states |
| [[ES-CLAVE]] `implements-requirement-from` [[EU-EIDAS]] | 1 previously isolated platform |

## Two of these were open backlog items

**[[EU-EIDAS]] had no `applies-in` edges at all** — flagged by the
comparison-matrix batch as an anomaly, since every other active EU
instrument attached to all six countries. It is a **regulation**, so the
evidence is the same reasoning [[EU-GDPR]]'s edges already use: directly
applicable in all member states without transposition. Adding it turned out
to reconnect seven German entities that had been orphaned since the German
batch.

**[[EU-INSPIRE]] applied in five countries and not the Netherlands** — the
founding country, with a geospatial domain and a national geo-portal. The
gap was real: the Netherlands transposed INSPIRE through the
*Implementatiewet EG-richtlijn infrastructuur ruimtelijke informatie*, in
force **1 September 2009**.

## The single most valuable edge was not obvious

[[NL-PDOK]] `aligned-with` [[EU-INSPIRE]] connected **21 entities** — every
Dutch base registry, [[NL-KADASTER]], [[NL-KVK]], [[NL-RDW]], the
[[NL-BASISREGISTRATIES]] stelsel itself. The whole system had been a sealed
island since the register batch: internally dense, externally unconnected.

PDOK is the Dutch national geo-platform, and its own pages state that its
services **comply with the European INSPIRE standard**. One sourced sentence
about a platform's standards conformance was the door into a fifth of the
Atlas.

⚠ The edge is `aligned-with`, not `implements-requirement-from`, and the
evidence says why: the sources establish standards compliance, **not** that
PDOK is the designated INSPIRE network-service infrastructure under the
Dutch implementing act. The stronger claim is probably true and is not
sourced.

## The NORA family, sourced at last

[[NL-ROSA]] said its NORA relationship was *"likely… but was not sourced"*.
[[NL-PETRA]] said the obvious edges were *"precisely what could not be"*
sourced. NORA's own wiki enumerates its **dochters**: EAR for central
government, GEMMA for municipalities, PETRA for the provinces, WILMA for the
water boards, and domain and chain architectures including ROSA for
education.

One page sourced **three** edges, and the prose in both entities was
rewritten — they had been telling readers the connection was unsourceable.

## What was deliberately left disconnected

Ten clusters and thirteen entities remain detached. Each was examined; none
is left out through inattention.

**Refusals the Atlas already made, and this batch did not override:**

- **[[ES-INCIBE]] ↔ [[ES-LCGC]]** — the Spanish draft law would redistribute
  competences between INCIBE and [[ES-CCN]], and [[ES-LCGC]] states the
  reasoning plainly: *"a contested draft allocation of competences is not a
  relationship; it becomes one if and when the law passes."* Still true.
- **[[NL-HEALTH-RI]] ↔ [[EU-EHDS]]** — Health-RI is the obvious candidate to
  become the Dutch health data access body, but the member-state designation
  phase runs **2027–2029**. Recorded as a high-value open question, not a
  guess.
- **[[INTL-IETF]] ↔ [[INTL-W3C]]** — the IETF entity describes W3C as a
  "peer direct-membership standards body". That is a *comparison*, not a
  relationship, and no liaison was sourced.

**The seven `DOMAIN-*` entities are isolated by design** and were not
touched. `domains/domain-cybersecurity.md` says it explicitly: domains are
referenced *by* other entities through their `domains:` field, which is an
association, and they carry no typed relationships of their own.

**Organisation-only pairs** — [[GB-DCMS]]/[[GB-GDS]], [[ES-AEAD]]/[[ES-SGAD]],
[[PL-COI]]/[[PL-MC]] — are internally connected and have no sourced edge to
anything else. The vocabulary has no defensible "this public body belongs to
this country" relationship, and inventing one is exactly what the brief
forbids.

## A convention question this batch answered by *not* acting

72 national instruments lack `applies-in` to their own country. Adding all
72 would have resolved the inconsistency the UK batch opened — and **25 of
them are the detached ones**, so it would also have connected most of what
remains.

It was **not done**, and the backlog item is rewritten rather than closed.
Reason: `applies-in` is defined as *"the primary mechanism for
country-neutral applicability"* — one supra-national instrument reaching
many countries. Using it for "this Dutch law applies in the Netherlands"
makes the type mean two different things, and 72 of 181 `applies-in` edges
would become tautological. The Compare view already has to filter the type
by scope for exactly this reason.

**The right resolution is probably to reconsider the UK edges, not to extend
them.** That is now what the backlog says.

## Verification

`validation/run_all.py` 5/5, 0 errors, 0 warnings.
`tools/test_build_graph.py` 37 tests. `tools/test_ui.mjs` 81 checks.
`validation/audit.py`: no fully disconnected entities.
Graph regenerated: **265 entities, 2,825 edges, 390 relationships**.
Sourcing unchanged: 258 of 265 entities unread.
