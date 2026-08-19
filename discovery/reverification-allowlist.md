# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-08-19

## Why this exists

**354 of the Atlas's 361 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **1181 source URLs** across **444 hosts**, collapsing to **327 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

| Domain | URLs | Entities |
|---|---|---|
| `europa.eu` | 127 | 73 |
| `wikipedia.org` | 64 | 64 |
| `bund.de` | 41 | 23 |
| `digitaleoverheid.nl` | 40 | 28 |
| `gov.pl` | 40 | 18 |
| `gouv.fr` | 36 | 13 |
| `gob.es` | 30 | 16 |
| `un.org` | 17 | 10 |
| `belgium.be` | 17 | 9 |
| `unece.org` | 17 | 7 |
| `iso.org` | 17 | 15 |
| `rijksoverheid.nl` | 16 | 12 |
| `bundestag.de` | 15 | 11 |
| `legislation.gov.uk` | 15 | 14 |
| `boe.es` | 14 | 12 |
| `admin.ch` | 13 | 7 |
| `overheid.nl` | 13 | 13 |
| `eerstekamer.nl` | 12 | 12 |
| `forumstandaardisatie.nl` | 12 | 5 |
| `cencenelec.eu` | 12 | 7 |

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
destatis.de
digitaleoverheid.nl
europa.eu
fitko.de
forumstandaardisatie.nl
gchq.gov.uk
gdi-de.org
geonovum.nl
gesetze-im-internet.de
gov.be
gov.ie
gov.pl
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
alston.com
altinn.no
anabad.org
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
comiteri.be
communicatierijk.nl
cso.ie
ctivd.nl
cuatrecasas.com
cyberfortgroup.com
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
e-recht24.de
earonline.nl
ecija.com
ecp.nl
edustandaard.nl
eerstekamer.nl
eosc.eu
epc.ac.uk
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
grokipedia.com
haufe.de
health-ri.nl
hessen.de
hoganlovells.com
hypotheses.org
iberley.es
ico.org.uk
ictu.nl
ietf.org
incibe.es
ine.es
informationssicherheitsbeauftragter-dresden.de
ing-ism.de
insee.fr
investigatorypowerstribunal.org.uk
ipco.org.uk
ipo.nl
irishstatutebook.ie
ishare.eu
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
nis-2-directive.com
nisd2.eu
njb.nl
nsai.ie
nsm.no
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
piwikpro.de
pkn.pl
plattform-i40.de
politykabezpieczenstwa.pl
privacyworld.blog
prodwaregroup.com
prosoz.de
protecciondata.es
protecciondatos-lopd.com
publictechnology.net
quality.de
rdw.nl
red.es
regjeringen.no
rehm-verlag.de
rijksbegroting.nl
rijksfinancien.nl
rlp.de
roraonline.nl
rvig.nl
sachsen-anhalt.de
safeonweb.be
sciencedirect.com
secjur.com
security-insider.de
sgrs.be
smartcountry.berlin
snl.no
springerprofessional.de
ssb.no
surf.nl
sva.nl
tailte.ie
taylorwessing.com
taz.de
tcontas.pt
techzine.nl
telusio.com
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
unsceb.org
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
xoev.de
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

