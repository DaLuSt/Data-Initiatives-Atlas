# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-08-16

## Why this exists

**227 of the Atlas's 233 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **757 source URLs** across **289 hosts**, collapsing to **211 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

| Domain | URLs | Entities |
|---|---|---|
| `europa.eu` | 87 | 52 |
| `digitaleoverheid.nl` | 40 | 28 |
| `wikipedia.org` | 36 | 36 |
| `bund.de` | 34 | 16 |
| `gouv.fr` | 27 | 9 |
| `gob.es` | 26 | 12 |
| `belgium.be` | 17 | 9 |
| `un.org` | 16 | 9 |
| `unece.org` | 14 | 5 |
| `rijksoverheid.nl` | 14 | 10 |
| `boe.es` | 12 | 10 |
| `overheid.nl` | 12 | 12 |
| `forumstandaardisatie.nl` | 12 | 5 |
| `iso.org` | 12 | 10 |
| `vng.nl` | 11 | 7 |
| `fitko.de` | 11 | 6 |
| `noraonline.nl` | 11 | 11 |
| `kadaster.nl` | 10 | 7 |
| `eerstekamer.nl` | 9 | 9 |
| `rvig.nl` | 8 | 4 |

## Institutional domains

Government, EU, UN and standards-body sources — the ones that carry evidential weight.

```
artificialintelligenceact.eu
belgif.be
belgium.be
bio-overheid.nl
bund.de
cencenelec.eu
destatis.de
digitaleoverheid.nl
europa.eu
fitko.de
forumstandaardisatie.nl
gdi-de.org
geonovum.nl
gesetze-im-internet.de
gov.be
gov.pl
govdata.de
government.nl
iso.org
it-planungsrat.de
itu.int
itzbund.de
just.fgov.be
ksz-bcss.fgov.be
legislation.gov.uk
logius.nl
noraonline.nl
open-government-deutschland.de
overheid.nl
rijksoverheid.nl
statbel.fgov.be
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
aftermarket-trends.de
agoria.be
anabad.org
anwalt.org
april.org
arena2036.de
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
bmv.de
boe.es
bosa.be
bpb.de
brandenburg.de
bundesrechnungshof.de
bundesregierung.de
bundestag.de
buzer.de
cbs.nl
cci-paris-idf.fr
cci.fr
ciberseguridad.blog
ciberseguridad.com
cloix-mendesgil.com
cni.es
cnil.fr
communicatierijk.nl
cso.ie
cuatrecasas.com
d-velop.de
dagdok.org
data-spaces-symposium.eu
datactivist.coop
dcat-ap.de
de.digital
decideo.fr
deloitte.com
diariodeleon.es
digigo.nu
digitale-verwaltung.de
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
eurogeographics.org
europadecentraal.nl
europeansources.info
eversheds-sutherland.com
ey.com
finreg360.com
forschungsinformationssystem.de
fraunhofer.de
gabler.de
gaia-x-hub.de
gaia-x.at
gaia-x.eu
gegevensbeschermingsautoriteit.be
geobasisregistraties.nl
geologischedienst.nl
geostandaarden.nl
github.com
github.io
glomas.de
gob.es
gouv.fr
grokipedia.com
haufe.de
health-ri.nl
hessen.de
hypotheses.org
ictu.nl
incibe.es
ine.es
informationssicherheitsbeauftragter-dresden.de
ing-ism.de
ipo.nl
ishare.eu
its-mobility.de
jtc1info.org
juntadeandalucia.es
juridicas.com
kadaster.nl
kbvg.nl
legiscope.com
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
oecd-ilibrary.org
oecd.org
officialstatistics.org
officielebekendmakingen.nl
om.nl
openjustice.be
openkritis.de
opennederland.nl
parlementairemonitor.nl
pdok.nl
personalausweisportal.de
prodwaregroup.com
prosoz.de
protecciondata.es
protecciondatos-lopd.com
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
smartcountry.berlin
springerprofessional.de
surf.nl
sva.nl
taylorwessing.com
tcontas.pt
telusio.com
tweedekamer.nl
twobirds.com
un-dco.org
un-ggim-europe.org
unctad.org
unece.org
unesco.org
unesco.org.uk
ungeneva.org
unievanwaterschappen.nl
unsceb.org
vbo-feb.be
vng.nl
vngrealisatie.nl
waarderingskamer.nl
walhalla.de
whitecase.com
wikipedia.org
xoev.de
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

