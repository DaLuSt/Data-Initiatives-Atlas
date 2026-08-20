# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-08-20

## Why this exists

**454 of the Atlas's 461 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **1529 source URLs** across **492 hosts**, collapsing to **359 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

| Domain | URLs | Entities | Link check |
|---|---|---|---|
| `europa.eu` | 190 | 118 | ✅ 2026-08-20 |
| `wikipedia.org` | 85 | 85 | ✅ 2026-08-20 |
| `iso.org` | 67 | 64 | ✅ 2026-08-20 |
| `coe.int` | 52 | 42 | ✅ 2026-08-20 |
| `bund.de` | 41 | 23 | ✅ 2026-08-20 |
| `digitaleoverheid.nl` | 40 | 28 | ✅ 2026-08-20 |
| `gov.pl` | 40 | 18 | ✅ 2026-08-20 |
| `gouv.fr` | 39 | 14 | ✅ 2026-08-20 |
| `government.nl` | 39 | 39 | ✅ 2026-08-20 |
| `gob.es` | 33 | 18 | ⚠ inaccurate — 2026-08-20 |
| `overheid.nl` | 27 | 20 | ✅ 2026-08-20 |
| `belgium.be` | 18 | 10 | ✅ 2026-08-20 |
| `un.org` | 17 | 10 | ✅ 2026-08-20 |
| `unece.org` | 17 | 7 | ✅ 2026-08-20 |
| `cencenelec.eu` | 17 | 10 | ✅ 2026-08-20 |
| `rijksoverheid.nl` | 16 | 12 | ✅ 2026-08-20 |
| `bundestag.de` | 15 | 11 | ✅ 2026-08-20 |
| `boe.es` | 15 | 13 | ✅ 2026-08-20 |
| `legislation.gov.uk` | 15 | 14 | ✅ 2026-08-20 |
| `admin.ch` | 13 | 7 |  |

### What the link check is, and what it is not

On **2026-08-20** the repository owner manually opened the highest-value domains above and reported that every one resolved to what the Atlas claims it does, **except `gob.es`**.

That is a **link check**, and it is the first primary-source signal of any kind this repository has had. It establishes that the citations point somewhere real. It does **not** establish that any entity's dates, identifiers, relationships or evidence strings are supported by the page cited — that is the content check, and it is what `verification: primary-source` records.

**So no entity's `verification` changed.** Every entity in the Atlas remains `search-only`. Conflating the two would be the exact overclaim the field exists to prevent.

## Institutional domains

Government, EU, UN and standards-body sources — the ones that carry evidential weight.

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
bpb.de
brandenburg.de
bsigroup.com
bundesrechnungshof.de
bundesregierung.de
bundestag.de
bundeswirtschaftsministerium.de
buzer.de
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
dataportals.org
dataprotection.ie
dataspace-culturalheritage.eu
datatilsynet.no
datopian.com
dcat-ap.de
de.digital
decideo.fr
defensie.nl
deloitte.com
diariodeleon.es
digdir.no
digigo.nu
digital.swiss
digitale-verwaltung-schweiz.ch
digitale-verwaltung.de
dlapiper.com
dlapiperdataprotection.com
dma.org.uk
dnb.de
dnb.nl
dnv.de
dsgvo-gesetz.de
dssc.eu
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
finreg360.com
forschungsinformationssystem.de
fraunhofer.de
gabler.de
gaia-x-hub.de
gaia-x.at
gaia-x.eu
gdpr-info.eu
gdprhub.eu
gdprregulation.eu
gegevensbeschermingsautoriteit.be
geheimdienste.org
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
haufe.de
health-ri.nl
hessen.de
hoganlovells.com
hypotheses.org
iapp.org
iberley.es
ibpt.be
ico.org.uk
ictu.nl
ietf.org
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
stcpservicos.pt
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
trecom.pl
tweedekamer.nl
twobirds.com
ugr.es
ukauthority.com
un-dco.org
un-ggim-europe.org
unctad.org
une.org
unece.org
unesco.org
unesco.org.uk
ungeneva.org
unievanwaterschappen.nl
unizar.es
unmz.cz
unsceb.org
urbact.eu
vbo-feb.be
vlex.be
vng.nl
vngrealisatie.nl
vorwaerts.de
vsse.be
waarderingskamer.nl
walhalla.de
whitecase.com
wikipedia.org
williamfry.com
wto.org
xoev.de
zakonyprolidi.cz
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

