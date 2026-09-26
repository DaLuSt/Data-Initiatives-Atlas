# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-09-26

## Why this exists

**0 of the Atlas's 723 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **2550 source URLs** across **746 hosts**, collapsing to **540 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

A domain here is an **allowlist pattern**, not a URL. Most of them also happen to serve a website at the apex; one does not. The `Example host` column is a real host the Atlas cites under that domain, so every row offers something that can actually be opened.

| Domain | URLs | Entities | Example host | Opened | Content confirmed |
|---|---|---|---|---|---|
| `europa.eu` | 346 | 201 | `certification.enisa.europa.eu` | ✅ opens | ✅ 2026-08-21 |
| `wikipedia.org` | 204 | 178 | `cs.wikipedia.org` | ✅ opens |  |
| `gouv.fr` | 71 | 27 | `aide.monespacenis2.cyber.gouv.fr` | ✅ opens |  |
| `gov.pl` | 68 | 27 | `api.dane.gov.pl` | ✅ opens |  |
| `iso.org` | 65 | 61 | `www.iso.org` | ✅ opens | ✅ 2026-08-21 |
| `coe.int` | 55 | 43 | `edoc.coe.int` | ✅ opens | ✅ 2026-08-21 |
| `overheid.nl` | 53 | 37 | `data.overheid.nl` | ✅ opens |  |
| `digitaleoverheid.nl` | 46 | 32 | `www.digitaleoverheid.nl` | ✅ opens |  |
| `bund.de` | 42 | 23 | `bmds.bund.de` | ✅ opens | ✅ 2026-08-21 |
| `gob.es` | 39 | 19 | `administracion.gob.es` | ⚠ namespace only — no site at the apex |  |
| `government.nl` | 39 | 39 | `www.government.nl` | ✅ opens |  |
| `un.org` | 36 | 20 | `docs.un.org` | ✅ opens |  |
| `legislation.gov.uk` | 34 | 27 | `www.legislation.gov.uk` | ✅ opens |  |
| `boe.es` | 33 | 26 | `www.boe.es` | ✅ opens |  |
| `admin.ch` | 27 | 11 | `www.bfs.admin.ch` |  |  |
| `rijksoverheid.nl` | 24 | 20 | `www.rijksoverheid.nl` | ✅ opens |  |
| `noraonline.nl` | 23 | 21 | `www.noraonline.nl` |  |  |
| `openjustice.be` | 22 | 18 | `etaamb.openjustice.be` |  |  |
| `forumstandaardisatie.nl` | 21 | 14 | `www.forumstandaardisatie.nl` |  |  |
| `belgium.be` | 20 | 12 | `bosa.belgium.be` | ✅ opens |  |

**`Opened` and `Content confirmed` are different claims.** The first says the citation points somewhere real. The second says the pages were read and the information on them confirmed correct, which is the only thing that licenses `verification: primary-source`. See `docs/re-verification.md` §"A link check is not a content check".

### What the 2026-08-20 check found, and what it did not

The repository owner opened all nineteen. Eighteen resolved to what the Atlas claims. **`gob.es` did not — and that is a defect in this report, not in any citation.**

Spain's government namespace has **no apex site**: `gob.es` resolves to no address at all, unlike `gov.uk` and `gov.pl`, which are both real websites as well as namespaces. Every Spanish host the Atlas actually cites — `datos.gob.es`, `administracion.gob.es`, `digital.gob.es`, `espanadigital.gob.es` and the rest — resolves and works. Hence the `Example host` column.

What the check **does** establish is that these citations point somewhere real. It does **not** establish that any entity's dates, identifiers, relationships or evidence strings are supported by the page cited — that is the content check, and it is what `verification: primary-source` records.

**So no entity's `verification` changed on 2026-08-20.** That came later: on **2026-08-21** the repository owner confirmed `bund.de`, `coe.int`, `europa.eu`, `iso.org`, `legifrance.gouv.fr` at the content tier — read, and the information on them correct. Every entity whose sources lie **entirely** within those five domains moved to `verification: primary-source`. Entities with only some sources there did not, because the unconfirmed source could be the one carrying the claim.

Two things about that list are worth stating precisely:

- **`legifrance.gouv.fr`, not `gouv.fr`.** The confirmation names one host under the French government namespace. This table collapses all of `gouv.fr` into one row — `cyber.gouv.fr`, `numerique.gouv.fr`, `data.gouv.fr` and the rest — so that row is **not** marked confirmed, and it should not be.
- **The Legifrance confirmation moved no entity.** Five entities cite it and every one of them also cites something unconfirmed, so none qualified. That is the partial-coverage rule doing its job rather than a defect: a confirmation is not required to yield anything.

**Also checked, outside the table above:** `bundestag.de`, `cencenelec.eu`, `gov.cz`, `gov.pt`, `public.lu`, `unece.org` — the other government namespaces among the Atlas's citations. All serve a site at the apex, which settles the question `gob.es` raised: it is the **sole exception**, not the first of several.

## Institutional domains

Government, EU, UN and standards-body sources — the ones that carry evidential weight.

**Reachability sweep, 2026-08-20: 52 of 52 resolve.** Every domain below was resolved at both the apex and `www.`, and none is a dead namespace — `gob.es` remains the only one of those in the Atlas.

Three resolve at `www.` but not at the apex: `coe.int`, `gesetze-im-internet.de`, `verwaltungsvorschriften-im-internet.de`. That is not a defect — the Atlas cites `www.` or `rm.` hosts under all three — but it is recorded so that nobody repeats the `gob.es` inference from an apex that does not answer.

This is the **weakest** of the three checks named in this file: it establishes that a host exists, and nothing about what it serves. It is also the only one that runs without egress, and it is what would have caught `gob.es` before a human had to.

```
agov.ch
artificialintelligenceact.eu
belgif.be
belgium.be
bio-overheid.nl
blog.gov.uk
bund.de
cencenelec.eu
coe.int
data.gov.uk
destatis.de
digitaleoverheid.nl
efta.int
eftacourt.int
eftasurv.int
egovernment.de
europa.eu
fitko.de
forumstandaardisatie.nl
gchq.gov.uk
gdi-de.org
geonovum.nl
gesetze-im-internet.de
gov.be
gov.cn
gov.cz
gov.ie
gov.it
gov.ng
gov.pl
gov.pt
gov.scot
gov.uk
govcert.lu
govdata.de
government.is
government.nl
internationaldataspaces.org
intnet.eu
iso.org
it-planungsrat.de
itu.int
itzbund.de
just.fgov.be
koopoverheid.nl
ksz-bcss.fgov.be
legislation.gov.uk
loc.gov
logius.nl
ncsc.gov.uk
nih.gov
noraonline.nl
ons.gov.uk
open-government-deutschland.de
overheid.nl
rijksoverheid.nl
service.gov.uk
statbel.fgov.be
statisticsauthority.gov.uk
trade.gov
un.org
verwaltungsvorschriften-im-internet.de
w3.org
who.int
wipo.int
wired-gov.net
```

## Remaining domains

Trade press, law firms, encyclopedias and vendor pages. Lower value, but cited somewhere in the Atlas — several entities rest on them entirely and say so in their own bodies.

```
activemind.de
ad4gd.eu
admin.ch
administration-numerique-suisse.ch
adn.be
adviescollegeicttoetsing.nl
aecc.eu
aepd.es
afdsd.fr
afnor.org
aftermarket-trends.de
agoria.be
aip-bg.org
aivd.nl
akademicka.pl
akdb.de
aki.ee
alston.com
altinn.no
ambitcompliance.ie
anabad.org
anwalt.org
aoc.cat
aoshearman.com
app.ch
april.org
araba.eus
arena2036.de
arnoldporter.com
arslege.pl
assemblee-nationale.fr
atlassian.net
automotiveit.eu
autoriteitpersoonsgegevens.nl
aventris.fr
axesor.es
b3-it.de
banquedesterritoires.fr
basisregistratieondergrond.nl
bayern.de
be.brussels
belastingdienst.nl
bestmag.co.uk
bho-legal.com
binnenlandsbestuur.nl
bipt.be
bitbw.de
biznesinfo.pl
blog.google
bmv.de
boe.es
bosa.be
bosettiegatti.eu
bpb.de
brandenburg.de
bratschi.ch
bremen.de
brreg.no
bsigroup.com
bundesaerztekammer.de
bundesdruckerei.de
bundesfinanzministerium.de
bundesrechnungshof.de
bundesregierung.de
bundestag.de
bundeswirtschaftsministerium.de
buzer.de
capgemini.com
catena-x.net
cbs.nl
ccdr-n.pt
cci-paris-idf.fr
cci.fr
ceeds.energy
cepal.org
certificeringsadvies.nl
ciberseguridad.blog
ciberseguridad.com
circl.lu
cleartax.com
cliffordchance.com
cloix-mendesgil.com
cms.law
cnctr.fr
cndp.ma
cni.es
cnil.fr
cnpd.pt
com.mx
comiteri.be
commport.com
communicatierijk.nl
comunidad.madrid
cso.ie
cssf.lu
ctivd.nl
cuatrecasas.com
cyberfortgroup.com
czso.cz
d-velop.de
dagdok.org
data-spaces-symposium.eu
datactivist.coop
datafordeler.dk
dataguidance.com
dataport.de
dataportal.se
dataportals.org
dataprotection.ie
dataspace-culturalheritage.eu
datastelsel.nl
datatilsynet.dk
datatilsynet.no
datenschutzstelle.li
datopian.com
dcat-ap.de
de.digital
decideo.fr
defensie.nl
dejure.org
deloitte.com
dena.de
deployemds.eu
deploytour.eu
dfg.de
dfn.de
diariodeleon.es
digdir.no
digg.se
digid.nl
digigo.nu
digital.swiss
digitale-verwaltung-schweiz.ch
digitale-verwaltung.de
digst.dk
din.de
dinoloket.nl
dke.de
dlapiper.com
dlapiperdataprotection.com
dma.org.uk
dnb.de
dnb.nl
dnielectronico.es
dnv.de
dre.pt
drupal.org
ds4skills.eu
dsgvo-gesetz.de
dssc.eu
dst.dk
dvv.fi
e-estonia.com
e-recht24.de
ecija.com
ecp.nl
edibasics.com
edustandaard.nl
eerstekamer.nl
eng.it
eos-utvalget.no
eosc.eu
epc.ac.uk
epic.org
errin.eu
esdn.eu
etsi.org
eubelius.com
eucrim.eu
eurogeographics.org
europadecentraal.nl
europalov.no
europeana.eu
europeansources.info
euskadi.eus
eversheds-sutherland.com
expressodasilhas.cv
ey.com
factory-x.org
fas.org
financialafrik.com
findata.fi
finreg360.com
forschungsinformationssystem.de
forsvaret.no
fraunhofer.de
gabler.de
gaia-x-hub.de
gaia-x.at
gaia-x.eu
garanteprivacy.it
gasteizhoy.com
gdpr-info.eu
gdprhub.eu
gdprregulation.eu
geant.net
geant.org
gegevensbeschermingsautoriteit.be
geheimdienste.org
gematik.de
geobasisregistraties.nl
geologischedienst.nl
geonorge.no
georgetown.edu
geostandaarden.nl
gipuzkoa.net
github.com
github.io
globalpolicywatch.com
glomas.de
gob.ar
gob.es
gouv.fr
gouvernement.lu
grunddata.dk
gub.uy
gv.at
haufe.de
health-ri.nl
heise.de
hessen.de
hetwaterschapshuis.nl
hoganlovells.com
hunton.com
hypotheses.org
iapp.org
ibestuur.nl
ibpt.be
ibsa.brussels
ico.org.uk
ictoblog.nl
ictu.nl
ietf.org
ifm.com
ilr.lu
imo.org
imy.se
incibe.es
inclusiveias.com
indicators.be
ine.es
ine.pt
informationssicherheitsbeauftragter-dresden.de
ing-ism.de
insee.fr
insieme.energy
investigatorypowerstribunal.org.uk
ipco.org.uk
ipo.nl
ipq.pt
irishstatutebook.ie
irishtimes.com
ishare.eu
issuu.com
istat.it
isvs.cz
it.nrw
italia.it
iteh.ai
itpatagonia.com
its-mobility.de
itwiz.pl
izfe.eus
jonesday.com
jtc1info.org
juntadeandalucia.es
juridicas.com
kadaster.nl
kalaidos-fh.ch
kartverket.no
kbvg.nl
klimadatastyrelsen.dk
komora.cz
kpmglaw.be
kvk.nl
legalgeek.pl
legiscope.com
lejdd.fr
lemauricien.com
lexgo.be
lexisnexis.co.uk
lexisnexis.com
lexlege.pl
likumi.lv
linklaters.com
lovdata.no
lsm.lv
lydian.be
manufacturingdataspace-csa.eu
mbkaya.com
medialaws.eu
mgm-tp.com
mobilithek.info
mobility-data-space.de
mobility-dataspace.eu
moirouxavocats.com
myilr.lu
mynewsdesk.com
naegele.law
nask.pl
nationaalarchief.nl
nationaalgroeifonds.nl
nbn.be
ncsc.nl
nctv.nl
ndfr.nl
ndw.nu
ne-mo.org
nen.nl
netzpolitik.org
netzwoche.ch
nfdi.de
nictiz.nl
niedersachsen.de
niis.org
nis-2-directive.com
nisd2.eu
njb.nl
nsai.ie
nsi.bg
nsm.no
nwo.nl
odissei-data.nl
odoserwis.pl
oecd.org
officielebekendmakingen.nl
oiger.de
om.nl
omega-x.eu
oneid.uk
ontolocy.com
opendata.swiss
openjustice.be
openkritis.de
opennederland.nl
ordnancesurvey.co.uk
osborneclarke.com
osce.org
pap-mediaroom.pl
parldigi.ch
parlementairemonitor.nl
parliament.uk
pdok.nl
peppol.eu
peppol.org
personalausweisportal.de
personuvernd.is
piwikpro.de
pkn.pl
plan.be
plattform-i40.de
politykabezpieczenstwa.pl
prebes.be
privacy-web.nl
privacyworld.blog
prodwaregroup.com
prometheus-x.org
prosoz.de
protecciondata.es
protecciondatos-lopd.com
psp.cz
pst.no
pubaffairsbruxelles.eu
public.lu
publicapis.io
publictechnology.net
quality.de
rdw.nl
red.es
redsara.es
reedsmith.com
regjeringen.no
rehm-verlag.de
rhein-zeitung.de
ria.ee
rijksbegroting.nl
rijksfinancien.nl
rijkswaterstaat.nl
rivm.nl
rlp.de
roraonline.nl
rtp.pt
rvig.nl
sachsen-anhalt.de
safeonweb.be
sapo.pt
scb.se
sciencedirect.com
scoop4c.eu
secjur.com
security-insider.de
securitymadein.lu
senat.fr
service-architecture.com
sgrs.be
sidn.nl
simontbraun.eu
smartcountry.berlin
snl.no
springerprofessional.de
ssb.no
stat.ee
stat.fi
statistik.at
stcpservicos.pt
stm.fi
sundhedsdatastyrelsen.dk
suomi.fi
surf.nl
sva.nl
svb-bgt.nl
tailte.ie
taylorwessing.com
taz.de
tcontas.pt
techzine.nl
telusio.com
tems-dataspace.eu
theinvoicinghub.com
theodi.org
thinkdigitalpartners.com
tib-ivd.nl
tietosuoja.fi
toegangspuntmobiliteit.nl
trecom.pl
tweedekamer.nl
twobirds.com
uef.fi
ugr.es
ukauthority.com
ukrat.de
un-dco.org
un-ggim-europe.org
unamur.be
unctad.org
une.org
unece.org
unesco.org
unesco.org.uk
unfpa.org
ungeneva.org
unievanwaterschappen.nl
unizar.es
unmz.cz
unsceb.org
urbact.eu
uv.es
vbo-feb.be
vdek.com
viafirma.com
vlaamsartsensyndicaat.be
vlaanderen.be
vlex.be
vng.nl
vngrealisatie.nl
voelkerrechtsblog.org
vorwaerts.de
vsse.be
waarderingskamer.nl
walhalla.de
wallonie.be
webmanagercenter.com
whitecase.com
wikidata.org
wikipedia.org
wikitoki.org
wikixl.nl
williamfry.com
wrangu.com
wto.org
wur.nl
x-road.global
xoev.de
zakonyprolidi.cz
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

