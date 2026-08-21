# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-08-21

## Why this exists

**435 of the Atlas's 516 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **1677 source URLs** across **550 hosts**, collapsing to **399 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

A domain here is an **allowlist pattern**, not a URL. Most of them also happen to serve a website at the apex; one does not. The `Example host` column is a real host the Atlas cites under that domain, so every row offers something that can actually be opened.

| Domain | URLs | Entities | Example host | Opened | Content confirmed |
|---|---|---|---|---|---|
| `europa.eu` | 233 | 146 | `data.europa.eu` | ✅ opens | ✅ 2026-08-21 |
| `wikipedia.org` | 90 | 90 | `cs.wikipedia.org` | ✅ opens |  |
| `iso.org` | 67 | 64 | `www.iso.org` | ✅ opens | ✅ 2026-08-21 |
| `coe.int` | 52 | 42 | `rm.coe.int` | ✅ opens | ✅ 2026-08-21 |
| `gouv.fr` | 44 | 16 | `aide.monespacenis2.cyber.gouv.fr` | ✅ opens |  |
| `bund.de` | 41 | 23 | `bmds.bund.de` | ✅ opens | ✅ 2026-08-21 |
| `digitaleoverheid.nl` | 40 | 28 | `www.digitaleoverheid.nl` | ✅ opens |  |
| `gov.pl` | 40 | 18 | `archiwum.giodo.gov.pl` | ✅ opens |  |
| `government.nl` | 39 | 39 | `www.government.nl` | ✅ opens |  |
| `gob.es` | 33 | 18 | `administracion.gob.es` | ⚠ namespace only — no site at the apex |  |
| `overheid.nl` | 27 | 20 | `data.overheid.nl` | ✅ opens |  |
| `unece.org` | 21 | 9 | `aarhusclearinghouse.unece.org` | ✅ opens |  |
| `un.org` | 20 | 12 | `docs.un.org` | ✅ opens |  |
| `belgium.be` | 18 | 10 | `bosa.belgium.be` | ✅ opens |  |
| `cencenelec.eu` | 17 | 10 | `standards.cencenelec.eu` | ✅ opens |  |
| `legislation.gov.uk` | 16 | 15 | `www.legislation.gov.uk` | ✅ opens |  |
| `rijksoverheid.nl` | 16 | 12 | `www.rijksoverheid.nl` | ✅ opens |  |
| `admin.ch` | 15 | 8 | `www.bfs.admin.ch` |  |  |
| `bundestag.de` | 15 | 11 | `dserver.bundestag.de` | ✅ opens |  |
| `boe.es` | 15 | 13 | `www.boe.es` | ✅ opens |  |

**`Opened` and `Content confirmed` are different claims.** The first says the citation points somewhere real. The second says the pages were read and the information on them confirmed correct, which is the only thing that licenses `verification: primary-source`. See `docs/re-verification.md` §"A link check is not a content check".

### What the 2026-08-20 check found, and what it did not

The repository owner opened all nineteen. Eighteen resolved to what the Atlas claims. **`gob.es` did not — and that is a defect in this report, not in any citation.**

Spain's government namespace has **no apex site**: `gob.es` resolves to no address at all, unlike `gov.uk` and `gov.pl`, which are both real websites as well as namespaces. Every Spanish host the Atlas actually cites — `datos.gob.es`, `administracion.gob.es`, `digital.gob.es`, `espanadigital.gob.es` and the rest — resolves and works. Hence the `Example host` column.

What the check **does** establish is that these citations point somewhere real. It does **not** establish that any entity's dates, identifiers, relationships or evidence strings are supported by the page cited — that is the content check, and it is what `verification: primary-source` records.

**So no entity's `verification` changed on 2026-08-20.** That came later: on **2026-08-21** the repository owner confirmed `bund.de`, `coe.int`, `europa.eu`, `iso.org`, `legifrance.gouv.fr` at the content tier — read, and the information on them correct. Every entity whose sources lie **entirely** within those five domains moved to `verification: primary-source`. Entities with only some sources there did not, because the unconfirmed source could be the one carrying the claim.

Two things about that list are worth stating precisely:

- **`legifrance.gouv.fr`, not `gouv.fr`.** The confirmation names one host under the French government namespace. This table collapses all of `gouv.fr` into one row — `cyber.gouv.fr`, `numerique.gouv.fr`, `data.gouv.fr` and the rest — so that row is **not** marked confirmed, and it should not be.
- **The Legifrance confirmation moved no entity.** Five entities cite it and every one of them also cites something unconfirmed, so none qualified. That is the partial-coverage rule doing its job rather than a defect: a confirmation is not required to yield anything.

**Also checked, outside the table above:** `gov.cz`, `gov.pt`, `public.lu` — the other government namespaces among the Atlas's citations. All serve a site at the apex, which settles the question `gob.es` raised: it is the **sole exception**, not the first of several.

## Institutional domains

Government, EU, UN and standards-body sources — the ones that carry evidential weight.

**Reachability sweep, 2026-08-20: 52 of 52 resolve.** Every domain below was resolved at both the apex and `www.`, and none is a dead namespace — `gob.es` remains the only one of those in the Atlas.

Three resolve at `www.` but not at the apex: `coe.int`, `gesetze-im-internet.de`, `verwaltungsvorschriften-im-internet.de`. That is not a defect — the Atlas cites `www.` or `rm.` hosts under all three — but it is recorded so that nobody repeats the `gob.es` inference from an apex that does not answer.

This is the **weakest** of the three checks named in this file: it establishes that a host exists, and nothing about what it serves. It is also the only one that runs without egress, and it is what would have caught `gob.es` before a human had to.

```
artificialintelligenceact.eu
belgif.be
belgium.be
bio-overheid.nl
blog.gov.uk
bund.de
cencenelec.eu
coe.int
destatis.de
digitaleoverheid.nl
efta.int
europa.eu
fitko.de
forumstandaardisatie.nl
gchq.gov.uk
gdi-de.org
geonovum.nl
gesetze-im-internet.de
gov.be
gov.cz
gov.ie
gov.it
gov.pl
gov.pt
gov.scot
gov.uk
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
ksz-bcss.fgov.be
legislation.gov.uk
loc.gov
logius.nl
ncsc.gov.uk
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
wipo.int
```

## Remaining domains

Trade press, law firms, encyclopedias and vendor pages. Lower value, but cited somewhere in the Atlas — several entities rest on them entirely and say so in their own bodies.

```
activemind.de
ad4gd.eu
admin.ch
aepd.es
afdsd.fr
afnor.org
aftermarket-trends.de
agoria.be
aivd.nl
akademicka.pl
aki.ee
alston.com
altinn.no
anabad.org
anacom.pt
anwalt.org
aoshearman.com
app.ch
april.org
arena2036.de
arnoldporter.com
arslege.pl
atlassian.net
automotiveit.eu
autoriteitpersoonsgegevens.nl
aventris.fr
b3-it.de
banquedesterritoires.fr
basisregistratieondergrond.nl
bayern.de
belastingdienst.nl
bho-legal.com
bipt.be
biznesinfo.pl
bmv.de
boe.es
bosa.be
bosettiegatti.eu
bpb.de
brandenburg.de
bsigroup.com
bundesaerztekammer.de
bundesrechnungshof.de
bundesregierung.de
bundestag.de
bundeswirtschaftsministerium.de
buzer.de
capgemini.com
cbs.nl
cci-paris-idf.fr
cci.fr
ceeds.energy
ciberseguridad.blog
ciberseguridad.com
cliffordchance.com
cloix-mendesgil.com
cms.law
cnctr.fr
cni.es
cnil.fr
cnpd.pt
comiteri.be
communicatierijk.nl
cso.ie
ctivd.nl
cuatrecasas.com
cyberfortgroup.com
czso.cz
d-velop.de
dagdok.org
data-spaces-symposium.eu
datactivist.coop
datafordeler.dk
dataportal.se
dataportals.org
dataprotection.ie
dataspace-culturalheritage.eu
datatilsynet.dk
datatilsynet.no
datenschutzstelle.li
datopian.com
dcat-ap.de
de.digital
decideo.fr
defensie.nl
deloitte.com
dfg.de
dfn.de
diariodeleon.es
digdir.no
digg.se
digigo.nu
digital.swiss
digitale-verwaltung-schweiz.ch
digitale-verwaltung.de
digst.dk
dlapiper.com
dlapiperdataprotection.com
dma.org.uk
dnb.de
dnb.nl
dnv.de
dsgvo-gesetz.de
dssc.eu
dst.dk
dvv.fi
e-estonia.com
e-recht24.de
earonline.nl
ecija.com
ecp.nl
ecs-org.eu
edustandaard.nl
eerstekamer.nl
eosc.eu
epc.ac.uk
epic.org
errin.eu
esdn.eu
eubelius.com
eucrim.eu
eurogeographics.org
europadecentraal.nl
europeana.eu
europeansources.info
eversheds-sutherland.com
ey.com
fas.org
febis.org
findata.fi
finreg360.com
forschungsinformationssystem.de
fraunhofer.de
gabler.de
gaia-x-hub.de
gaia-x.at
gaia-x.eu
garanteprivacy.it
gdpr-info.eu
gdprhub.eu
gdprregulation.eu
geant.org
gegevensbeschermingsautoriteit.be
geheimdienste.org
gematik.de
geobasisregistraties.nl
geologischedienst.nl
geonorge.no
geostandaarden.nl
github.com
github.io
globalpolicywatch.com
glomas.de
gob.es
gouv.fr
gouvernement.lu
grokipedia.com
grunddata.dk
gv.at
haufe.de
health-ri.nl
hessen.de
hoganlovells.com
hypotheses.org
iapp.org
iberley.es
ibpt.be
ibsa.brussels
ico.org.uk
ictu.nl
ietf.org
imy.se
incibe.es
ine.es
ine.pt
informationssicherheitsbeauftragter-dresden.de
ing-ism.de
insee.fr
investigatorypowerstribunal.org.uk
ipco.org.uk
ipo.nl
ipq.pt
irishstatutebook.ie
ishare.eu
istat.it
isvs.cz
its-mobility.de
itwiz.pl
jtc1info.org
juntadeandalucia.es
juridicas.com
kadaster.nl
kalaidos-fh.ch
kartverket.no
kbvg.nl
legalgeek.pl
legiscope.com
lejdd.fr
lexisnexis.co.uk
lexisnexis.com
lexlege.pl
linklaters.com
lovdata.no
medialaws.eu
mobilithek.info
mobility-data-space.de
mobility-dataspace.eu
moirouxavocats.com
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
nsm.no
oa.pt
odoserwis.pl
oecd-ilibrary.org
oecd.org
officialstatistics.org
officielebekendmakingen.nl
om.nl
oneid.uk
ontolocy.com
opendata.swiss
openjustice.be
openkritis.de
opennederland.nl
ordnancesurvey.co.uk
osborneclarke.com
pap-mediaroom.pl
parldigi.ch
parlementairemonitor.nl
parliament.uk
pdok.nl
personalausweisportal.de
personuvernd.is
pgdlisboa.pt
piwikpro.de
pkn.pl
plattform-i40.de
politykabezpieczenstwa.pl
privacyworld.blog
prodwaregroup.com
prosoz.de
protecciondata.es
protecciondatos-lopd.com
pubaffairsbruxelles.eu
public.lu
publictechnology.net
quality.de
rdw.nl
red.es
regjeringen.no
rehm-verlag.de
ria.ee
rijksbegroting.nl
rijksfinancien.nl
rlp.de
roraonline.nl
rvig.nl
sachsen-anhalt.de
safeonweb.be
scb.se
sciencedirect.com
scoop4c.eu
secjur.com
security-insider.de
senat.fr
sgrs.be
smartcountry.berlin
snl.no
springerprofessional.de
ssb.no
stat.fi
statistik.at
stcpservicos.pt
stm.fi
sundhedsdatastyrelsen.dk
suomi.fi
surf.nl
sva.nl
tailte.ie
taylorwessing.com
taz.de
tcontas.pt
techzine.nl
telusio.com
theinvoicinghub.com
theodi.org
thinkdigitalpartners.com
tib-ivd.nl
tietosuoja.fi
trecom.pl
tweedekamer.nl
twobirds.com
uef.fi
ugr.es
ukauthority.com
un-dco.org
un-ggim-europe.org
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
vbo-feb.be
vdek.com
vlaanderen.be
vlex.be
vng.nl
vngrealisatie.nl
vorwaerts.de
vsse.be
waarderingskamer.nl
walhalla.de
wallonie.be
whitecase.com
wikipedia.org
williamfry.com
wto.org
xoev.de
zakonyprolidi.cz
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

