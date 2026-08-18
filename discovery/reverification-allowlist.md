# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-08-18

## Why this exists

**305 of the Atlas's 312 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **1024 source URLs** across **380 hosts**, collapsing to **279 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

| Domain | URLs | Entities |
|---|---|---|
| `europa.eu` | 88 | 53 |
| `wikipedia.org` | 62 | 62 |
| `bund.de` | 41 | 23 |
| `digitaleoverheid.nl` | 40 | 28 |
| `gov.pl` | 40 | 18 |
| `gouv.fr` | 36 | 13 |
| `gob.es` | 28 | 14 |
| `un.org` | 17 | 10 |
| `belgium.be` | 17 | 9 |
| `unece.org` | 17 | 7 |
| `rijksoverheid.nl` | 16 | 12 |
| `bundestag.de` | 15 | 11 |
| `legislation.gov.uk` | 15 | 14 |
| `boe.es` | 14 | 12 |
| `iso.org` | 14 | 12 |
| `overheid.nl` | 13 | 13 |
| `eerstekamer.nl` | 12 | 12 |
| `forumstandaardisatie.nl` | 12 | 5 |
| `vng.nl` | 11 | 7 |
| `fitko.de` | 11 | 6 |

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
gov.pl
gov.scot
gov.uk
govdata.de
government.nl
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
aepd.es
afdsd.fr
aftermarket-trends.de
agoria.be
aivd.nl
akademicka.pl
alston.com
anabad.org
anwalt.org
aoshearman.com
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
buzer.de
cbs.nl
cci-paris-idf.fr
cci.fr
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
datopian.com
dcat-ap.de
de.digital
decideo.fr
defensie.nl
deloitte.com
diariodeleon.es
digigo.nu
digitale-verwaltung.de
dlapiper.com
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
epc.ac.uk
errin.eu
esdn.eu
eubelius.com
eucrim.eu
eurogeographics.org
europadecentraal.nl
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
gegevensbeschermingsautoriteit.be
geheimdienste.org
geobasisregistraties.nl
geologischedienst.nl
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
incibe.es
ine.es
informationssicherheitsbeauftragter-dresden.de
ing-ism.de
investigatorypowerstribunal.org.uk
ipco.org.uk
ipo.nl
ishare.eu
its-mobility.de
itwiz.pl
jtc1info.org
juntadeandalucia.es
juridicas.com
kadaster.nl
kbvg.nl
legalgeek.pl
legiscope.com
lejdd.fr
lexisnexis.co.uk
lexisnexis.com
lexlege.pl
medialaws.eu
mobilithek.info
mobility-data-space.de
mobility-dataspace.eu
moirouxavocats.com
nationaalarchief.nl
nationaalgroeifonds.nl
ncsc.nl
nctv.nl
ndfr.nl
ndw.nu
nen.nl
netzpolitik.org
nictiz.nl
niedersachsen.de
nis-2-directive.com
nisd2.eu
njb.nl
odoserwis.pl
oecd-ilibrary.org
oecd.org
officialstatistics.org
officielebekendmakingen.nl
om.nl
oneid.uk
ontolocy.com
openjustice.be
openkritis.de
opennederland.nl
ordnancesurvey.co.uk
osborneclarke.com
pap-mediaroom.pl
parlementairemonitor.nl
parliament.uk
pdok.nl
personalausweisportal.de
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
rehm-verlag.de
rijksbegroting.nl
rijksfinancien.nl
rlp.de
roraonline.nl
rvig.nl
sachsen-anhalt.de
safeonweb.be
secjur.com
security-insider.de
sgrs.be
smartcountry.berlin
springerprofessional.de
surf.nl
sva.nl
taylorwessing.com
taz.de
tcontas.pt
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
xoev.de
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

